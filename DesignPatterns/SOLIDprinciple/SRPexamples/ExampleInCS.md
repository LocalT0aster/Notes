# Example in `C#`

## Example WRONG code

The "wrong" code violates the Single Responsibility Principle (SRP) because the `Journal` class is handling two separate concerns: managing journal entries and managing the persistence of those entries to a file.

```csharp
using System.Diagnostics;

// Just stores a couple of journal entries and ways of
// working with them
public class Journal
{
    // secret journal entries
    private readonly List<string> entries = new List<string>();

    private static int count = 0;

    public int AddEntry(string text)
    {
        entries.Add($"{++count}: {text}");
        return count; // memento pattern!
    }

    public void RemoveEntry(int index)
    {
        entries.RemoveAt(index);
    }

    public override string ToString()
    {
        return string.Join(Environment.NewLine, entries);
    }

    // breaks single responsibility principle
    public void Save(string filename, bool overwrite = false)
    {
        File.WriteAllText(filename, ToString());
    }

    // breaks single responsibility principle
    public void Load(string filename)
    {
        File.ReadAllText(filename).Split('\n');
    }
}

public class Demo
{
    static void Main(string[] args)
    {
        var j = new Journal();
        j.AddEntry("I cried today.");
        j.AddEntry("I ate a bug.");
        Console.WriteLine(j);

        var filename = @"c:\temp\journal.txt";
        j.Save(filename);
        Process.Start(filename);
    }
}
```

## Example FIXED code

The `Journal` class is responsible not just for maintaining the journal entries, but also for saving and loading them from a file.  This violates SRP because a change in how we store the journal entries would require changes to the `Journal` class.

```csharp
using System.Diagnostics;

// Just stores a couple of journal entries and ways of
// working with them
public class Journal
{
    private readonly List<string> entries = new List<string>();

    private static int count = 0;

    public int AddEntry(string text)
    {
        entries.Add($"{++count}: {text}");
        return count; // memento pattern!
    }

    public void RemoveEntry(int index)
    {
        entries.RemoveAt(index);
    }

    public override string ToString()
    {
        return string.Join(Environment.NewLine, entries);
    }
}
// handles the responsibility of persisting objects
public class Persistence
{
    public void SaveToFile(Journal journal, string filename, bool overwrite = false)
    {
        if (overwrite || !File.Exists(filename))
            File.WriteAllText(filename, journal.ToString());
    }
}

public class Demo
{
    static void Main(string[] args)
    {
        var j = new Journal();
        j.AddEntry("I cried today.");
        j.AddEntry("I ate a bug.");
        Console.WriteLine(j);

        var p = new Persistence();
        var filename = @"c:\temp\journal.txt";
        p.SaveToFile(j, filename);
        Process.Start(filename);
    }
}
```

The `Journal` class now only handles journal entries, while a new `Persistence` class is introduced to handle saving the `Journal` object to a file. This adheres to the SRP because each class now has a single responsibility: `Journal` for managing entries, and `Persistence` for managing file operations.

Now, if you need to change how journal entries are stored, you only need to modify the `Persistence` class, not `Journal`. Similarly, if the way we manage journal entries changes, we only update `Journal`, not `Persistence`. This separation of concerns makes the code easier to maintain and understand.

<!--Back Button-->
[<img src="../../../img/back.svg" style="width:8em;">](../SRP.md)
