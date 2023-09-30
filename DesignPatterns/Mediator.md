# Mediator

> **Note**
> Facilitates communication between components.

A component that facilitates communication between other components without them necessarily being aware of each other or having direct (reference) access to each other.

## Intent

> **Important**
> **Intent**
> Define an object that encapsulates how a set of objects interact. Mediator promotes loose coupling by keeping objects from referring to each other explicitly, and it lets you vary their interaction independently.

## Explanation

The Mediator design pattern is a behavioral pattern that encapsulates how a set of objects interact. It promotes loose coupling by keeping objects from referring to each other explicitly, and it lets you vary their interaction independently. Instead of objects communicating directly with each other, they communicate indirectly through a mediator object.

---

### Motivation to use

- Components may go in and out of a system at any time
  - Chat room participants
  - Players in an MMORPG
- It makes no sense for them to have direct references to one another
  - Those references may go dead
- Solution: have then all refer to some central component that facilitates communication

---

## Summary from the course

- Create the mediator and have each object in the system refer to it E.g., in a field
- Mediator engages in bidirectional communication with its connected components
- Mediator has functions the components can call
- Components have functions the mediator can call
- Event processing (e.g., Rx) libraries make communication easier to implement

---

<!--Back Button-->
[<img src="../img/back.svg" style="width:8em;">](README.md)
