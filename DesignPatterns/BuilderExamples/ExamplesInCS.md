# Builder Examples in `C#`

- [Builder Examples in `C#`](#builder-examples-in-c)
  - [Builder](#builder)
  - [Builder Facets](#builder-facets)
  - [Builder Inheritance](#builder-inheritance)
  - [Functional Builder](#functional-builder)
  - [Stepwise Builder](#stepwise-builder)

## Builder

```csharp
// Builder design pattern example
// from https://www.udemy.com/course/design-patterns-csharp-dotnet/
using System.Text;

class HtmlElement
{
    public string Name, Text;
    public List<HtmlElement> Elements = new List<HtmlElement>();
    private const int indentSize = 2;

    public HtmlElement()
    {

    }

    public HtmlElement(string name, string text)
    {
        Name = name;
        Text = text;
    }

    private string ToStringImpl(int indent)
    {
        var sb = new StringBuilder();
        var i = new string(' ', indentSize * indent);
        sb.Append($"{i}<{Name}>\n");
        if (!string.IsNullOrWhiteSpace(Text))
        {
            sb.Append(new string(' ', indentSize * (indent + 1)));
            sb.Append(Text);
            sb.Append("\n");
        }

        foreach (var e in Elements)
            sb.Append(e.ToStringImpl(indent + 1));

        sb.Append($"{i}</{Name}>\n");
        return sb.ToString();
    }

    public override string ToString()
    {
        return ToStringImpl(0);
    }
}

class HtmlBuilder
{
    private readonly string rootName;

    public HtmlBuilder(string rootName)
    {
        this.rootName = rootName;
        root.Name = rootName;
    }

    // not fluent
    public void AddChild(string childName, string childText)
    {
        var e = new HtmlElement(childName, childText);
        root.Elements.Add(e);
    }

    public HtmlBuilder AddChildFluent(string childName, string childText)
    {
        var e = new HtmlElement(childName, childText);
        root.Elements.Add(e);
        return this;
    }

    public override string ToString()
    {
        return root.ToString();
    }

    public void Clear()
    {
        root = new HtmlElement { Name = rootName };
    }

    HtmlElement root = new HtmlElement();
}

public class Demo
{
    static void Main(string[] args)
    {
        // if you want to build a simple HTML paragraph using StringBuilder
        var hello = "hello";
        var sb = new StringBuilder();
        sb.Append("<p>");
        sb.Append(hello);
        sb.Append("</p>");
        Console.WriteLine(sb);

        // now I want an HTML list with 2 words in it
        var words = new[] { "hello", "world" };
        sb.Clear();
        sb.Append("<ul>");
        foreach (var word in words)
        {
            sb.AppendFormat("<li>{0}</li>", word);
        }
        sb.Append("</ul>");
        Console.WriteLine(sb);

        // ordinary non-fluent builder
        var builder = new HtmlBuilder("ul");
        builder.AddChild("li", "hello");
        builder.AddChild("li", "world");
        Console.WriteLine(builder.ToString());

        // fluent builder
        sb.Clear();
        builder.Clear(); // disengage builder from the object it's building, then...
        builder.AddChildFluent("li", "hello").AddChildFluent("li", "world");
        Console.WriteLine(builder);
    }
}
```

## Builder Facets

```csharp
// Builder facets design pattern example
// from https://www.udemy.com/course/design-patterns-csharp-dotnet/
public class Person
{
    // address
    public string StreetAddress, Postcode, City;

    // employment
    public string CompanyName, Position;

    public int AnnualIncome;

    public override string ToString()
    {
        return $"{nameof(StreetAddress)}: {StreetAddress}, {nameof(Postcode)}: {Postcode}, {nameof(City)}: {City}, {nameof(CompanyName)}: {CompanyName}, {nameof(Position)}: {Position}, {nameof(AnnualIncome)}: {AnnualIncome}";
    }
}

public class PersonBuilder // facade
{
    // the object we're going to build
    protected Person person = new Person(); // this is a reference!

    public PersonAddressBuilder Lives => new PersonAddressBuilder(person);
    public PersonJobBuilder Works => new PersonJobBuilder(person);

    public static implicit operator Person(PersonBuilder pb)
    {
        return pb.person;
    }
}

public class PersonJobBuilder : PersonBuilder
{
    public PersonJobBuilder(Person person)
    {
        this.person = person;
    }

    public PersonJobBuilder At(string companyName)
    {
        person.CompanyName = companyName;
        return this;
    }

    public PersonJobBuilder AsA(string position)
    {
        person.Position = position;
        return this;
    }

    public PersonJobBuilder Earning(int annualIncome)
    {
        person.AnnualIncome = annualIncome;
        return this;
    }
}

public class PersonAddressBuilder : PersonBuilder
{
    // might not work with a value type!
    public PersonAddressBuilder(Person person)
    {
        this.person = person;
    }

    public PersonAddressBuilder At(string streetAddress)
    {
        person.StreetAddress = streetAddress;
        return this;
        // Console.WriteLine(person);
    }
}
```

## Builder Inheritance

```csharp
// Builder inheritance design pattern example
// from https://www.udemy.com/course/design-patterns-csharp-dotnet/
public class Person
{
    public string Name;

    public string Position;

    public DateTime DateOfBirth;

    public class Builder : PersonBirthDateBuilder<Builder>
    {
        internal Builder() { }
    }

    public static Builder New => new Builder();

    public override string ToString()
    {
        return $"{nameof(Name)}: {Name}, {nameof(Position)}: {Position}";
    }
}

public abstract class PersonBuilder
{
    protected Person person = new Person();

    public Person Build()
    {
        return person;
    }
}

public class PersonInfoBuilder<SELF> : PersonBuilder
  where SELF : PersonInfoBuilder<SELF>
{
    public SELF Called(string name)
    {
        person.Name = name;
        return (SELF)this;
    }
}

public class PersonJobBuilder<SELF>
  : PersonInfoBuilder<PersonJobBuilder<SELF>>
  where SELF : PersonJobBuilder<SELF>
{
    public SELF WorksAsA(string position)
    {
        person.Position = position;
        return (SELF)this;
    }
}

// here's another inheritance level
// note there's no PersonInfoBuilder<PersonJobBuilder<PersonBirthDateBuilder<SELF>>>!

public class PersonBirthDateBuilder<SELF>
  : PersonJobBuilder<PersonBirthDateBuilder<SELF>>
  where SELF : PersonBirthDateBuilder<SELF>
{
    public SELF Born(DateTime dateOfBirth)
    {
        person.DateOfBirth = dateOfBirth;
        return (SELF)this;
    }
}

internal class Program
{
    class SomeBuilder : PersonBirthDateBuilder<SomeBuilder>
    {

    }

    public static void Main(string[] args)
    {
        var me = Person.New
          .Called("Dmitri")
          .WorksAsA("Quant")
          .Born(DateTime.UtcNow)
          .Build();
        Console.WriteLine(me);
    }
}
```

## Functional Builder

```csharp
// functional Builder design pattern example
// from https://www.udemy.com/course/design-patterns-csharp-dotnet/
public class Person
{
    public string Name, Position;
}

public sealed class PersonBuilder
{
    public readonly List<Action<Person>> Actions
      = new List<Action<Person>>();

    public PersonBuilder Called(string name)
    {
        Actions.Add(p => { p.Name = name; });
        return this;
    }

    public Person Build()
    {
        var p = new Person();
        Actions.ForEach(a => a(p));
        return p;
    }
}

public static class PersonBuilderExtensions
{
    public static PersonBuilder WorksAsA
      (this PersonBuilder builder, string position)
    {
        builder.Actions.Add(p =>
        {
            p.Position = position;
        });
        return builder;
    }
}

public class FunctionalBuilder
{
    public static void Main(string[] args)
    {
        var pb = new PersonBuilder();
        var person = pb.Called("Dmitri").WorksAsA("Programmer").Build();
    }
}
```

## Stepwise Builder

```csharp
// stepwise Builder design pattern example
// from https://www.udemy.com/course/design-patterns-csharp-dotnet/
public enum CarType
{
    Sedan,
    Crossover
};
public class Car
{
    public CarType Type;
    public int WheelSize;
}

public interface ISpecifyCarType
{
    public ISpecifyWheelSize OfType(CarType type);
}

public interface ISpecifyWheelSize
{
    public IBuildCar WithWheels(int size);
}

public interface IBuildCar
{
    public Car Build();
}

public class CarBuilder
{
    public static ISpecifyCarType Create()
    {
        return new Impl();
    }

    private class Impl :
      ISpecifyCarType,
      ISpecifyWheelSize,
      IBuildCar
    {
        private Car car = new Car();

        public ISpecifyWheelSize OfType(CarType type)
        {
            car.Type = type;
            return this;
        }

        public IBuildCar WithWheels(int size)
        {
            switch (car.Type)
            {
                case CarType.Crossover when size < 17 || size > 20:
                case CarType.Sedan when size < 15 || size > 17:
                    throw new ArgumentException($"Wrong size of wheel for {car.Type}.");
            }
            car.WheelSize = size;
            return this;
        }

        public Car Build()
        {
            return car;
        }
    }
}

class Program
{
    static void Main(string[] args)
    {
        var car = CarBuilder.Create()
          .OfType(CarType.Crossover)
          .WithWheels(18)
          .Build();
        Console.WriteLine(car);
    }
}
```

[<kbd><br><- Return<br></kbd>](../Builder.md)
