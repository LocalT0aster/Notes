# Adapter

> Getting the interface you want from the interface you have.
>

<aside>
💡 A construct which adapts an existing interface X to conform to the required interface Y.

</aside>

## Intent:

### Convert the interface of a class into another interface clients expect. Adapter lets classes work together that couldn't otherwise because of incompatible interfaces.

## Explanation:

> The Adapter pattern is a structural design pattern that allows incompatible interfaces to work together. It wraps itself around an object to expose a standard interface that other objects expect to interact with. It's like a bridge between two incompatible interfaces, converting the interface of one class into an interface that the client expects.
>

---

### Motivation to use:

- Electrical devices have different power (interface) requirements
    - Voltage (5V, 220V)
    - Socket/plug type (Europe, UK, USA)
- We cannot modify our gadgets to support every possible interface
    - Some support possible (e.g., 120/220V)
- Thus, we use a special device (an adapter) to give us the interface
we require from the interface we have

---

## Summary from the course:

- Implementing an Adapter is easy
- Determine the API you have and the API you need
- Create a component which aggregates (has a reference to, …) the adaptee
- Intermediate representations can pile up: use caching and other optimizations

---