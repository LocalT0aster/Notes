# Example in `C#`

This code demonstrates the Dependency Inversion Principle (DIP) in action. Let's break it down:

1. `IRelationshipBrowser` is an abstraction (an interface) that provides a method for finding all children of a person.
2. `Relationships` is a low-level module. It implements `IRelationshipBrowser`, providing the functionality to store relationships and find all children of a specific person.
3. `Research` is a high-level module. In the initial version (commented out), it directly depends on the `Relationships` class (a low-level module). This violates the DIP, as high-level modules should not depend on low-level modules.
4. To correct this, `Research` is refactored so that it depends on `IRelationshipBrowser` instead of `Relationships`. Now, `Research` no longer needs to know the details of how relationships are stored or how the `FindAllChildrenOf()` function is implemented. It only depends on the abstraction, not the specific low-level module.
5. In the `Main` method, `Research` is initialized with an instance of `Relationships`. However, since `Relationships` implements `IRelationshipBrowser`, this is fine: `Research` just sees it as an `IRelationshipBrowser`. This allows for the possibility of swapping out `Relationships` for a different implementation of `IRelationshipBrowser` in the future, without needing to change `Research`.

So, in this example, both high-level `Research` and low-level `Relationships` modules depend on the abstraction `IRelationshipBrowser`. Abstraction doesn't depend on details; details (Relationships) depend on abstractions `IRelationshipBrowser`. This is a perfect illustration of the Dependency Inversion Principle.

```csharp
// hl modules should not depend on low-level; both should depend on abstractions
// abstractions should not depend on details; details should depend on abstractions

public enum Relationship
{
    Parent,
    Child,
    Sibling
}

public class Person
{
    public string Name;
    // public DateTime DateOfBirth;
}

public interface IRelationshipBrowser
{
    IEnumerable<Person> FindAllChildrenOf(string name);
}

public class Relationships : IRelationshipBrowser // low-level
{
    private List<(Person, Relationship, Person)> relations
      = new List<(Person, Relationship, Person)>();

    public void AddParentAndChild(Person parent, Person child)
    {
        relations.Add((parent, Relationship.Parent, child));
        relations.Add((child, Relationship.Child, parent));
    }

    public List<(Person, Relationship, Person)> Relations => relations;

    public IEnumerable<Person> FindAllChildrenOf(string name)
    {
        return relations
          .Where(x => x.Item1.Name == name
                      && x.Item2 == Relationship.Parent).Select(r => r.Item3);
    }
}

public class Research
{
    public Research(Relationships relationships)
    {
        // high-level: find all of john's children
        //var relations = relationships.Relations;
        //foreach (var r in relations
        //  .Where(x => x.Item1.Name == "John"
        //              && x.Item2 == Relationship.Parent))
        //{
        //  WriteLine($"John has a child called {r.Item3.Name}");
        //}
    }

    public Research(IRelationshipBrowser browser)
    {
        foreach (var p in browser.FindAllChildrenOf("John"))
        {
            Console.WriteLine($"John has a child called {p.Name}");
        }
    }

    static void Main(string[] args)
    {
        var parent = new Person { Name = "John" };
        var child1 = new Person { Name = "Chris" };
        var child2 = new Person { Name = "Matt" };

        // low-level module
        var relationships = new Relationships();
        relationships.AddParentAndChild(parent, child1);
        relationships.AddParentAndChild(parent, child2);

        new Research(relationships);

    }
}
```

<!--Back Button-->
[<kbd><br><- Return<br></kbd>](../DIP.md)
