# Iterator

> **Note**
> How traversal of data structures happens and who makes it happen.

An object that facilitates the traversal of a data structure.

## Intent

> **Important**
> **Intent**
> Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation.

## Explanation

The Iterator design pattern provides a way to access elements of a collection object sequentially without exposing its underlying representation. It introduces an iterator object that encapsulates the details of iteration, allowing different collections to be navigated with a common interface.

---

### Motivation to use

- Iteration (traversal) is a core functionality of various data structures
- An iterator is a class that facilitates the traversal
  - Keeps a reference to the current element
  - Knows how to move to a different element
- Iterator is an implicit construct
  - .NET builds a state machine around your yield return statements

---

## Summary from the course

- An iterator specified how you can traverse an object
- An iterator object, unlike a method, cannot be recursive
- Generally, an `IEnumerable<T>`-returning method is enough
- Iteration works through duck typing — you need a `GetEnumerator()` that yields a
type that has Current and `MoveNext()`

---

[<kbd><br><- Return<br></kbd>](DesignPatterns.md)
