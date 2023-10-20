# Memento

> **Note**
> Keep a memento of an object’s state to return to that state.

 A token/handle representing the system state. Lets us roll back to the state when the token was generated. May or may not directly expose state information.

## Intent

> **Important**
> **Intent**
> Without violating encapsulation, capture and externalize an object's internal state so that the object can be restored to this state later.

## Explanation

The Memento design pattern allows for saving and restoring the state of an object without revealing its implementation details. It's typically used when you need to provide an undo functionality. The pattern involves three roles: the Originator (object whose state is saved), the Memento (object that stores the state), and the Caretaker (object that keeps track of multiple mementos but doesn't operate on their states).

---

### Motivation to use

- An object or system goes through changes
  - E.g., a bank account gets deposits and withdrawals
- There are different ways of navigating those changes
- One way is to record every change (Command) and teach a command to ‘undo’ itself
- Another is to simply save snapshots of the system

---

## Summary from the course

- Mementos are used to roll back states arbitrarily
- A memento is simply a token/handle class with (typically) no functions of its own
- A memento is not required to expose directly the state(s) to which it reverts the system
- Can be used to implement undo/redo

---

[<kbd><br><- Return<br></kbd>](DesignPatterns.md)
