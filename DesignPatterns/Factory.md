# Factory

> **Note**
> A component responsible solely for the wholesale (not piecewise) creation of objects.

## Explanation

The Factory design pattern is a creational pattern that provides an interface for creating objects in a superclass but allows subclasses to alter the type of objects that will be created. It's used when a class cannot anticipate the type of objects it needs to create, or when a class wants its subclasses to specify the objects it creates. This pattern helps to manage and maintain code that would otherwise become complex with direct instantiation.

---

### Motivation to use

- Object creation logic becomes too convoluted
- Constructor is not descriptive
  - Name mandated by name of containing type
  - Cannot overload with the same sets of arguments with different names
  - Can turn into ‘optional parameter hell’
- Object creation (non-piecewise, unlike Builder) can be outsourced to
  - A separate function (Factory Method)
  - That may exist in a separate class (Factory)
  - Can create a hierarchy of factories with Abstract Factory

---

## Factory Method

### FM Intent

> **Important**
> **Intent**
> Define an interface for creating an object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses.

### FM Explanation

**Factory Method** is a pattern that provides an interface for creating objects, but lets subclasses decide which class to instantiate. The Factory Method defers instantiation to subclasses. It's used when a class doesn't know the exact types and dependencies of the objects it should work with.

For example, imagine a logistics company that can transport goods by road, sea, or air. The base `Logistics` class wouldn't know what type of transport to create (truck, ship, or plane), as this depends on the specific logistics subclass (road, sea, or air logistics). So, the `Logistics` class would have a factory method like `createTransport()` that would be implemented in each subclass to produce the right kind of transport object.

---

## Abstract Factory

### AF Intent

> **Important**
> **Intent**
> Provide an interface for creating families of related or dependent objects without specifying their concrete classes.

### AF Explanation

**Abstract Factory** is like a factory of factories. It provides an interface for creating families of related or dependent objects without specifying their concrete classes. It's used when the system needs to be independent from the way the products it works with are created and composed.

Continuing the logistics example, let's say each type of transport also needs a suitable navigation system. Trucks need road maps, ships need sea charts, and planes need flight maps. These form two families of related objects: transports and navigation systems. An abstract factory, `LogisticsFactory`, could have methods like `createTransport()` and `createNavigationSystem()`. Specific factories like `RoadLogisticsFactory`, `SeaLogisticsFactory`, and `AirLogisticsFactory` would implement these methods to produce matching transport and navigation objects (e.g., a truck and a road map).

## Differences

To summarize, Factory Method is about creating one product, and the factory doesn't have to know all the possible types of products. Abstract Factory is about creating families of related products and orchestrating how they work together.

Factory Method is a pattern that lets subclasses decide which class to instantiate, focusing on single product creation. Abstract Factory, on the other hand, is a pattern that provides an interface for creating families of related or dependent objects, focusing on multiple related products. While Factory Method deals with the problem of creating objects without specifying the exact class to create, Abstract Factory addresses the problem of creating families of related objects without specifying their concrete classes.

---

## Summary from the course

- A factory method is a static method that creates objects
- A factory can take care of object creation
- A factory can be external or reside inside the object as an inner class
- Hierarchies of factories can be used to create related objects

---

## Examples

[Examples in C#](FactoryExamples/ExamplesInCS.md)

<!--Back Button-->
[<img src="../img/back.svg" style="width:8em;">](README.md)
