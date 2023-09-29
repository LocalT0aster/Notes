# Command

> **Warning**
> ***YOU SHALL NOT PASS!***

An object which represents an instruction to perform a particular action. Contains all the information necessary for the action to be taken.

## Intent

> **Important**
> **Intent**
> Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.

## Explanation

The Command design pattern encapsulates a request as an object, thereby letting you parameterize other objects with different requests, queue or log requests, and support undoable operations. It involves three components:

1. Command: Declares an interface for executing an operation.
2. Concrete Command: Defines a binding between a Receiver object and an action.
3. Invoker: Asks the command to carry out the request.

This pattern decouples the sender (Invoker) and receiver (Receiver) of a request, promoting loose coupling and flexibility.

---

### Motivation to use

- Ordinary C# statements are perishable
  - Cannot undo a field/property assignment
  - Cannot directly serialize a sequence of actions (calls)
- Want an object that represents an operation
  - X should change its property Y to Z
  - X should do W()
- Uses: GUI commands, multi-level undo/redo, macro recording and more!

---

## Summary from the course

- Encapsulate all details of an operation in a separate object
- Define instruction for applying the command (either in the command itself, or elsewhere)
- Optionally define instructions for undoing the command
- Can create composite commands (a.k.a. macros)

---
