# Design Patterns

---

Design patterns are standard solutions to common problems in software design. They represent best practices, providing a way to structure code in a way that's reusable, maintainable, and understandable. Patterns can be classified into three types: creational (for object creation), structural (for object relationships), and behavioral (for object interactions and responsibility distribution).

---

- [Design Patterns](#design-patterns)
  - [Before you begin studying design patterns](#before-you-begin-studying-design-patterns)
  - [Gamma categorization](#gamma-categorization)
  - [Patterns](#patterns)

## Before you begin studying design patterns

[Programming Basics & OOP](ProgrammingBasics&OOP.md)

[SOLID principle](SOLIDprinciple/README.md)

## Gamma categorization

---
> **Important**
> The "Gamma categorization" refers to the classification of design patterns proposed in the book "Design Patterns: Elements of Reusable Object-Oriented Software" by Erich Gamma and others. It categorizes design patterns into three types:

- Creational Patterns
  - Deal with the creation (construction) of objects
  - Explicit (constructor) vs. implicit (DI, reflection, etc.)
  - Wholesale (single statement) vs. piecewise (step-by-step)
- Structural Patterns
  - Concerned with the structure (e.g., class members)
  - Many patterns are wrappers that mimic the underlying class’ interface
  - Stress the importance of good API design
- Behavioral Patterns
  - They are all different; no central theme

---

## Patterns

| ***Creational***             | ***Structural***             | ***Behavioral***                                       |
| :--------------------------- | :--------------------------- | :----------------------------------------------------- |
| [🛠️ Builder](Builder.md)     | [🔌 Adapter](Adapter.md)     | [🔗 Chain of Responsibility](ChainOfResponsibility.md) |
| [🏭 Factory](Factory.md)     | [🌉 Bridge](Bridge.md)       | [🔘 Command](Command.md) |
| [🧬 Prototype](Prototype.md) | [🌳 Composite](Composite.md) | [📖 Interpreter](Interpreter.md) |
| [🔐 Singleton](Singleton.md) | [🎨 Decorator](Decorator.md) | [🔄 Iterator](Iterator.md) |
|                              | [🚪 Façade](Façade.md)       | [🤝 Mediator](Mediator.md) |
|                              | [🍃 Flyweight](Flyweight.md) | [📦 Memento](Memento.md) |
|                              | [🕵️ Proxy](Proxy.md)         | [0️⃣ Null Object](NullObject.md) |
|                              |                              | [👁️ Observer](Observer.md) |
|                              |                              | [🔄 State](State.md) |
|                              |                              | [💡 Strategy](Strategy.md) |
|                              |                              | [📜 Template Method](TemplateMethod.md) |
|                              |                              | [🚶 Visitor](Visitor.md) |

GPT4 was used to generate explanations.

Examples from the course:

[Design Patterns in C# and .NET: Learn Solutions to Common Problems](https://www.udemy.com/course/design-patterns-csharp-dotnet/)

Found on rutracker.org

[<img src="../img/back.svg" style="width:8em;">](../README.md)
