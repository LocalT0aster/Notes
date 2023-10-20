# Template Method

> **Note**
> A high-level blueprint for an algorithm to be completed by inheritors.

Allows us to define the ‘skeleton’ of the algorithm, with concrete implementations defined in subclasses.

## Intent

> **Important**
> **Intent**
> Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure.

## Explanation

The Template Method pattern is a behavioral design pattern that defines the program skeleton in a method, called a template method, which defers some steps to subclasses. It lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure. This pattern allows to change parts of an algorithm without affecting its overall structure and order.

---

### Motivation to use

- Algorithms can be decomposed into common parts + specifics
- Strategy pattern does this through composition
  - High-level algorithm uses an interface
  - Concrete implementations implement the interface
- Template Method does the same thing through inheritance
  - Overall algorithm makes use of abstract member
  - Inheritors override the abstract members
  - Parent template method invoked

---

## Summary from the course

- Define an algorithm at a high level
- Define constituent parts as abstract methods/properties
- Inherit the algorithm class, providing necessary overrides

---

[<kbd><br><- Return<br></kbd>](DesignPatterns.md)
