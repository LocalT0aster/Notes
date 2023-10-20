# Example in `C#`

This example demonstrates the Interface Segregation Principle (ISP). Let's break down the example:

In the first part of the code, an interface `IMachine` is defined with three methods: `Print`, `Fax`, and `Scan`. This interface is then implemented by two classes, `MultiFunctionPrinter` and `OldFashionedPrinter`. The `MultiFunctionPrinter` can handle all the methods, as it's a multifunction device. However, `OldFashionedPrinter` can only print, and it throws exceptions for `Fax` and `Scan` methods, which indicates a design issue.

This problem arises because the `IMachine` interface is not correctly segregated. It assumes that any machine will want to perform all three functions (print, fax, and scan), which is not the case for an `OldFashionedPrinter`.

To solve this, the ISP is applied by creating separate interfaces for each responsibility: `IPrinter` and `IScanner`. Now, each class can implement only the interfaces it requires. The `Printer` class only implements `IPrinter`, and the `Photocopier` class implements both `IPrinter` and `IScanner`, since it can handle both functionalities.

Further, the code introduces an `IMultiFunctionDevice` interface that combines the `IPrinter` and `IScanner` interfaces. The `MultiFunctionMachine` struct then implements this interface, demonstrating how you can compose objects with multiple capabilities by combining these segregated interfaces.

So, in this refactored design, no class is forced to implement methods it does not need, which is the essence of the Interface Segregation Principle.

```csharp
public class Document
{
}

public interface IMachine
{
    void Print(Document d);
    void Fax(Document d);
    void Scan(Document d);
}

// ok if you need a multifunction machine
public class MultiFunctionPrinter : IMachine
{
    public void Print(Document d)
    {
        //
    }

    public void Fax(Document d)
    {
        //
    }

    public void Scan(Document d)
    {
        //
    }
}

public class OldFashionedPrinter : IMachine
{
    public void Print(Document d)
    {
        // yep
    }

    public void Fax(Document d)
    {
        throw new NotImplementedException();
    }

    public void Scan(Document d)
    {
        throw new NotImplementedException();
    }
}

public interface IPrinter
{
    void Print(Document d);
}

public interface IScanner
{
    void Scan(Document d);
}

public class Printer : IPrinter
{
    public void Print(Document d)
    {

    }
}

public class Photocopier : IPrinter, IScanner
{
    public void Print(Document d)
    {
        throw new NotImplementedException();
    }

    public void Scan(Document d)
    {
        throw new NotImplementedException();
    }
}

public interface IMultiFunctionDevice : IPrinter, IScanner //
{

}

public struct MultiFunctionMachine : IMultiFunctionDevice
{
    // compose this out of several modules
    private IPrinter printer;
    private IScanner scanner;

    public MultiFunctionMachine(IPrinter printer, IScanner scanner)
    {
        if (printer == null)
        {
            throw new ArgumentNullException(paramName: nameof(printer));
        }
        if (scanner == null)
        {
            throw new ArgumentNullException(paramName: nameof(scanner));
        }
        this.printer = printer;
        this.scanner = scanner;
    }

    public void Print(Document d)
    {
        printer.Print(d);
    }

    public void Scan(Document d)
    {
        scanner.Scan(d);
    }
}
```

[<kbd><br><- Return<br></kbd>](../ISP.md)
