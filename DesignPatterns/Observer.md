# Observer

> **Note**
> An observer is an object that wishes to be informed about events happening in the system. The entity generating the events is an observable.

## Intent

> **Important**
> **Intent**
> Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

## Explanation

The Observer pattern is a behavioral design pattern that allows an object (the "subject") to notify other objects (the "observers") about changes in its state. Observers subscribe to the subject, and whenever the subject undergoes a change, it broadcasts to all subscribed observers. This pattern promotes loose coupling between the subject and observers.

---

### Motivation to use

- We need to be informed when certain things happen
  - Object’s property changes
  - Object does something
  - Some external event occurs
- We want to listen to events and notified when they occur
- Built into C# with the event keyword
  - But then what is this `IObservable<T>` / `IObserver<T>` for?
  - What about `INotifyPropertyChanging`/ `Changed`?
  - And what are `BindingList<T>`/ `ObservableCollection<T>`?

---

## Summary from the course

- Observer is an intrusive approach: an observable must provide an event to subscribe to
- Special care must be taken to prevent issues in multithreaded scenarios
- .NET comes with observable collections
- `IObserver<T>`/ `IObservable<T>` are used in stream processing (Reactive Extensions)

---
