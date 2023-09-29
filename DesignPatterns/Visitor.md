# Visitor

> [!NOTE]
> Typically a tool for structure traversal rather than anything else.
> **Important**
> **Definition:**
> A pattern where a component (visitor) is allowed to traverse the entire inheritance hierarchy. Implemented by propagating a single visit() method throughout the entire hierarchy.

## Intent

Represent an operation to be performed on the elements of an object structure. Visitor lets you define a new operation without changing the classes of the elements on which it operates.

## Explanation

The Visitor design pattern is a behavioral pattern that allows you to add new behaviors to existing class hierarchies without altering any existing code. It involves a visitor class that defines a method for each type of element class that it can visit. These methods implement the specific behavior to be performed on that element. The element classes provide an 'accept' method that takes a visitor instance as an argument, effectively allowing the visitor to 'visit' them.

---

### Motivation to use

- Need to define a new operation on an entire class hierarchy
  - E.g., make a document model printable to HTML/Markdown
- Do not want to keep modifying every class in the hierarchy
- Need access to the non-common aspects of classes in the hierarchy
  - I.e., an extension method won't do
- Create an external component to handle rendering
  - But avoid type checks

---

## Summary from the course

- Propagate an `accept( Visitor v)` method throughout the entire hierarchy
- Create a visitor with `Visit(Foo)`, `Visit(Bar)`, … for each element in the hierarchy
- Each `accept()` simply calls visitor. `Visit(this)`
- Using dynamic, we can invoke right overload based on argument type alone
(dynamic dispatch)

---
