# Singleton

> **Note**
> A component which is instantiated only once.

*A design pattern everyone loves to hate... but is it really that bad?*

> When discussing which patterns to drop, we found that we still love them all.
>
>
> (Not really — I'm in favor of dropping Singleton. Its use is almost always a design smell.)
>
> — Erich Gamma
>

## Intent

> **Important**
> **Intent**
> Ensure a class only has one instance, and provide a global point of access to it.

## Explanation

The Singleton design pattern ensures that a class has only one instance and provides a global point of access to it. This pattern is used when we need to ensure that only one object of a particular class is ever created. All further references to objects of the singleton class refer to the same underlying instance.

---

### Motivation to use

- For some components it only makes sense to have one in the syste
  - Database repository
  - Object factory
- E.g., the constructor call is expensive
  - We only do it once
  - We provide everyone with the same instance
- Want to prevent anyone creating additional copies
- Need to take care of lazy instantiation and thread safety

---

## Summary from the course

- Making a ‘safe’ singleton is easy: construct a static `Lazy<T>` and return its Value
- Singletons are difficult to test
- Instead of directly using a singleton, consider depending on an abstraction (e.g., an interface)
- Consider defining singleton lifetime in DI container

[<kbd><br><- Return<br></kbd>](DesignPatterns.md)
