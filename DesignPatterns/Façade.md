# Façade

> **Note**
> Exposing several components through a single interface.

Provides a simple, easy to understand/user interface over a large and sophisticated body of code.

## Intent

> **Important**
> **Intent**
> Provide a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use.

## Explanation

The Facade design pattern provides a unified interface to a set of interfaces in a subsystem. It simplifies the subsystem from the client's perspective by hiding the complexity behind a simplified, high-level API, making the subsystem easier to use.

---

### Motivation to use

---

- Balancing complexity and presentation/usability
- Typical home
  - Many subsystems (electrical, sanitation)
  - Complex internal structure (e.g., floor layers)
  - End user is not exposed to internals
- Same with software!
  - Many systems working to provide flexibility, but...
  - API consumers want it to ‘just work’

## Summary from the course

---

- Build a Facade to provide a simplified API over a set of classes
- May wish to (optionally) expose internals through the facade
- May allow users to ‘escalate’ to use more complex APIs if they need to

[<kbd><br><- Return<br></kbd>](DesignPatterns.md)
