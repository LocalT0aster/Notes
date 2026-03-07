# Examples in `C#`

- [Examples in `C#`](#examples-in-c)
  - [Factory Method](#factory-method)
  - [Abstract Factory](#abstract-factory)

## Factory Method

```csharp
// Factory Method design pattern example
// from https://www.udemy.com/course/design-patterns-csharp-dotnet/
public class Point
{
    private double x, y;

    protected Point(double x, double y)
    {
        this.x = x;
        this.y = y;
    }

    public Point(double a,
      double b, // names do not communicate intent
      CoordinateSystem cs = CoordinateSystem.Cartesian)
    {
        switch (cs)
        {
            case CoordinateSystem.Polar:
                x = a * Math.Cos(b);
                y = a * Math.Sin(b);
                break;
            default:
                x = a;
                y = b;
                break;
        }

        // steps to add a new system
        // 1. augment CoordinateSystem
        // 2. change ctor
    }

    // factory property

    public static Point Origin => new Point(0, 0);

    // singleton field
    public static Point Origin2 = new Point(0, 0);

    // factory method

    public static Point NewCartesianPoint(double x, double y)
    {
        return new Point(x, y);
    }

    public static Point NewPolarPoint(double rho, double theta)
    {
        //...
        return null;
    }

    public enum CoordinateSystem
    {
        Cartesian,
        Polar
    }

    // make it lazy
    public static class Factory
    {
        public static Point NewCartesianPoint(double x, double y)
        {
            return new Point(x, y);
        }
    }
}

class PointFactory
{
    public static Point NewCartesianPoint(float x, float y)
    {
        return new Point(x, y); // needs to be public
    }
}

class Demo
{
    static void Main(string[] args)
    {
        var p1 = new Point(2, 3, Point.CoordinateSystem.Cartesian);
        var origin = Point.Origin;

        var p2 = Point.Factory.NewCartesianPoint(1, 2);
    }
}
```

## Abstract Factory

```csharp
// Abstract Factory design pattern example
// from https://www.udemy.com/course/design-patterns-csharp-dotnet/
public interface IHotDrink
{
    void Consume();
}

internal class Tea : IHotDrink
{
    public void Consume()
    {
        Console.WriteLine("This tea is nice but I'd prefer it with milk.");
    }
}

internal class Coffee : IHotDrink
{
    public void Consume()
    {
        Console.WriteLine("This coffee is delicious!");
    }
}

public interface IHotDrinkFactory
{
    IHotDrink Prepare(int amount);
}

internal class TeaFactory : IHotDrinkFactory
{
    public IHotDrink Prepare(int amount)
    {
        Console.WriteLine($"Put in tea bag, boil water, pour {amount} ml, add lemon, enjoy!");
        return new Tea();
    }
}

internal class CoffeeFactory : IHotDrinkFactory
{
    public IHotDrink Prepare(int amount)
    {
        Console.WriteLine($"Grind some beans, boil water, pour {amount} ml, add cream and sugar, enjoy!");
        return new Coffee();
    }
}

public class HotDrinkMachine
{
    public enum AvailableDrink // violates open-closed
    {
        Coffee, Tea
    }

    private Dictionary<AvailableDrink, IHotDrinkFactory> factories =
      new Dictionary<AvailableDrink, IHotDrinkFactory>();

    private List<Tuple<string, IHotDrinkFactory>> namedFactories =
      new List<Tuple<string, IHotDrinkFactory>>();

    public HotDrinkMachine()
    {
        //foreach (AvailableDrink drink in Enum.GetValues(typeof(AvailableDrink)))
        //{
        //  var factory = (IHotDrinkFactory) Activator.CreateInstance(
        //    Type.GetType("DotNetDesignPatternDemos.Creational.AbstractFactory." + Enum.GetName(typeof(AvailableDrink), drink) + "Factory"));
        //  factories.Add(drink, factory);
        //}

        foreach (var t in typeof(HotDrinkMachine).Assembly.GetTypes())
        {
            if (typeof(IHotDrinkFactory).IsAssignableFrom(t) && !t.IsInterface)
            {
                namedFactories.Add(Tuple.Create(
                  t.Name.Replace("Factory", string.Empty), (IHotDrinkFactory)Activator.CreateInstance(t)));
            }
        }
    }

    public IHotDrink MakeDrink()
    {
        Console.WriteLine("Available drinks");
        for (var index = 0; index < namedFactories.Count; index++)
        {
            var tuple = namedFactories[index];
            Console.WriteLine($"{index}: {tuple.Item1}");
        }

        while (true)
        {
            string s;
            if ((s = Console.ReadLine()) != null
                && int.TryParse(s, out int i) // c# 7
                && i >= 0
                && i < namedFactories.Count)
            {
                Console.Write("Specify amount: ");
                s = Console.ReadLine();
                if (s != null
                    && int.TryParse(s, out int amount)
                    && amount > 0)
                {
                    return namedFactories[i].Item2.Prepare(amount);
                }
            }
            Console.WriteLine("Incorrect input, try again.");
        }
    }

    //public IHotDrink MakeDrink(AvailableDrink drink, int amount)
    //{
    //  return factories[drink].Prepare(amount);
    //}
}

class Program
{
    static void Main(string[] args)
    {
        var machine = new HotDrinkMachine();
        //var drink = machine.MakeDrink(HotDrinkMachine.AvailableDrink.Tea, 300);
        //drink.Consume();

        IHotDrink drink = machine.MakeDrink();
        drink.Consume();
    }
}
```
