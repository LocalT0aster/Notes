# Composite

> **Note**
> Treating individual and aggregate objects uniformly.

A mechanism for treating individual (scalar) objects and compositions of objects in a uniform manner.

## Intent

> **Important**
> **Intent**
> Compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly.

## Explanation

The Composite design pattern is a structural design pattern that allows you to compose objects into tree structures to represent part-whole hierarchies. It lets clients treat individual objects and compositions of objects uniformly. In other words, a composite object can be treated the same as an individual object, allowing recursive structures to be easily built and manipulated.

---

### Motivation to use

- Objects use other objects’ fields/properties/members through inheritance and composition
- Composition lets us make compound objects
  - E.g., a mathematical expression composed of simple expressions; or
  - A grouping of shapes that consists of several shapes
- Composite design pattern is used to treat both single (scalar) and composite objects uniformly
  - I.e., Foo and Collection< Foo> have common APIs

---

## Summary from the course

---

- Objects can use other objects via inheritance/composition
- Some composed and singular objects need similar/identical behaviors
- Composite design pattern lets us treat both types of objects uniformly
- C# has special support for the enumeration concept
- A single object can masquerade as a collection with yield return this;
