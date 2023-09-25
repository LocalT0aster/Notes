# Example in C#

This is a classic example of the Liskov Substitution Principle (LSP) in action, using a `Rectangle` and `Square` example.

The idea behind LSP is that you should be able to use a derived class (a class that inherits from another class, like `Square` from `Rectangle` here) in place of its base class without causing any issues or changes in behavior.

In this example, `Square` is a subclass of `Rectangle`. Because a square is a special kind of rectangle (where width equals height), it might seem logical to model this relationship using inheritance.

However, there's a problem with this design. A `Square` object's `Width` and `Height` are always equal. When you set either property, the `Square` class sets both `Width` and `Height` to the new value. This represents a violation of the Liskov Substitution Principle because a `Square` doesn't behave the same way as a `Rectangle`.

In the `Demo` class's `Main` method, you can see the issue. When you create a `Rectangle` object and set its `Width` and `Height` independently, it behaves as expected. But when you create a `Square` object (which should be substitutable for `Rectangle` according to LSP), it doesn't behave as a rectangle should. Setting the `Width` to 4 also sets the `Height` to 4, causing the area to be 16 instead of the expected 12 (if it behaved as a rectangle with width 4 and height 3).

So, this code example illustrates a violation of the Liskov Substitution Principle, showing that even though a square is a kind of rectangle in the real world, this relationship doesn't necessarily translate well into an object-oriented design.

```csharp
// using a classic example
public class Rectangle
{
    //public int Width { get; set; }
    //public int Height { get; set; }

    public virtual int Width { get; set; }
    public virtual int Height { get; set; }

    public Rectangle()
    {

    }

    public Rectangle(int width, int height)
    {
        Width = width;
        Height = height;
    }

    public override string ToString()
    {
        return $"{nameof(Width)}: {Width}, {nameof(Height)}: {Height}";
    }
}

public class Square : Rectangle
{
    //public new int Width
    //{
    //  set { base.Width = base.Height = value; }
    //}

    //public new int Height
    //{
    //  set { base.Width = base.Height = value; }
    //}

    public override int Width // nasty side effects
    {
        set { base.Width = base.Height = value; }
    }

    public override int Height
    {
        set { base.Width = base.Height = value; }
    }
}

public class Demo
{
    static public int Area(Rectangle r) => r.Width * r.Height;

    static void Main(string[] args)
    {
        Rectangle rc = new Rectangle(2, 3);
        Console.WriteLine($"{rc} has area {Area(rc)}");

        // should be able to substitute a base type for a subtype
        /*Square*/
        Rectangle sq = new Square();
        sq.Width = 4;
        Console.WriteLine($"{sq} has area {Area(sq)}");
    }
}
```
