# Prototype

> **Note**
> A partially or fully initialized object that you copy (clone) and make use of.

*When it’s easier to copy an existing object to fully initialize a new one.*

## Intent

> **Important**
> **Intent**
> Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype.

## Explanation

The Prototype pattern is a creational design pattern that allows cloning objects, even complex ones, without coupling to their specific classes. All prototype classes have a common interface that makes it possible to copy objects safely. This pattern is especially useful when creating an object is expensive or complex. Instead of creating a new object, an existing prototype is cloned.

---

### Motivation to use

- Complicated objects (e.g., cars) aren’t designed from scratch
  - They reiterate existing designs
- An existing (partially or fully constructed) design is a Prototype
- We make a copy (clone) the prototype and customize it
- Requires ‘deep copy’ support
- We make the cloning convenient (e.g., via a Factory)

---

## Summary from the course

- To implement a prototype, partially construct an object and store it somewhere
- Clone the prototype
  - Implement your own deep copy functionality; or
  - Serialize and deserialize
- Customize the resulting instance

## Examples
