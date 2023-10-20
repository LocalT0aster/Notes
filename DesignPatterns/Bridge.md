# Bridge

> **Note**
> Connecting components together through abstractions.

A mechanism that decouples an interface (hierarchy) from an implementation (hierarchy).

## Intent

> **Important**
> **Intent**
> Decouple an abstraction from its implementation so that the two can vary independently.

## Explanation

The Bridge design pattern is a structural design pattern that decouples an abstraction from its implementation, so they can vary independently. This pattern involves an interface (the "bridge") that makes the functionality of concrete classes independent from the interface implementer classes. The bridge pattern is particularly useful when both the class and what it does can evolve independently.

---

### Motivation to use

- Bridge prevents a ‘Cartesian product’ complexity explosion
- Example: Base class `ThreadScheduler`
  - Can be preemptive or cooperative
  - Can run on Windows or Unix
  - End up with with a 2x2 scenario: WindowsPTS, UnixPTS, WindowsCTS, UnixCTS
- Bridge pattern avoids the entity explosion

---

## Summary from the course

---

- Decouple abstraction from implementation
- Both can exist as hierarchies
- A stronger form of encapsulation

[<kbd><br><- Return<br></kbd>](DesignPatterns.md)
