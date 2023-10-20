# Builder

> **Note**
> When construction gets a little bit too complicated.

When piecewise object construction is complicated, provide an API for doing it succinctly.

## Intent

> **Important**
> **Intent**
> Separate the construction of a complex object from its representation so that the same construction process can create different representations.

## Explanation

The Builder design pattern is a creational pattern that provides a way to construct a complex object step by step. It separates the construction of an object from its representation so that the same construction process can create different representations. This is useful when you need to create an object with lots of possible configuration options.

---

### Motivation to use

- Some objects are simple and can be created in a single constructor call
- Other objects require a lot of ceremonies to create
- Having an object with 10 constructor arguments is not productive
- Instead, opt for piecewise construction
- Builder provides an API for constructing an object step-by-step

---

## Summary from the course

- A builder is a separate component for building an object
- Can either give the builder a constructor or return it via a static function
- To make the builder fluent, return this
- Different facets of an object can be built with different builders working in tandem via a base class

---

## Examples

[Examples in C#](BuilderExamples/ExamplesInCS.md)

[<kbd><br><- Return<br></kbd>](DesignPatterns.md)
