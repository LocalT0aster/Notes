# Decorator

> **Note**
> Adding behavior without altering the class itself.

Facilitates the addition of behaviors to individual objects without inheriting from them.

## Intent

> **Important**
> **Intent**
> Attach additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.

## Explanation

The Decorator design pattern allows behavior to be added to an individual object, either statically or dynamically, without affecting the behavior of other objects from the same class. It involves a set of decorator classes that mirror the type of the decorated object but add or override behavior. This pattern is useful when you need to extend the functionality of a class, but subclassing is not ideal because it leads to high-class complexity and potential code duplication.

---

### Motivation to use

- Want to augment an object with additional functionality
- Do not want to rewrite or alter existing code (OCP)
- Want to keep new functionality separate (SRP)
- Need to be able to interact with existing structures
- Two options:
  - Inherit from required object if possible; some objects are sealed
  - Build a Decorator, which simply references the decorated object(s)

---

## Summary from the course

---

- A decorator keeps the reference to the decorated object(s)
- May or may not proxy over calls
  - Use R# Generate Delegated Members
- Exists in a static variation
  - `X<Y<Foo>>`
  - Very limited due to inability to inherit from type parameters
