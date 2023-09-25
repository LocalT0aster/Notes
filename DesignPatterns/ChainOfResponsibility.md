# Chain of Responsibility

> Sequence of handlers processing an event one after another.
>

<aside>
💡 A chain of components who all get a chance to process a command or a query, optionally having default processing implementation and an ability to terminate the processing chain.

</aside>

## Intent:

### Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. Chain the receiving objects and pass the request along the chain until an object handles it.

## Explanation:

> The Chain of Responsibility design pattern avoids coupling the sender of a request to its receiver by giving multiple objects a chance to handle the request. The request is passed along a chain of potential handlers until an object handles it or it reaches the end of the chain. This pattern is used to achieve loose coupling and dynamic runtime handling decisions in software systems.
>

---

### Motivation to use:

Chains of responsibility:

- Unethical behavior by an employee; who takes the blame?
    - Employee
    - Manager
    - CEO
- You click a graphical element on a form
    - Button handles it, stops further processing
    - Underlying group box
    - Underlying window
- CCG computer game
    - Creature has attack and defense values
    - Those can be boosted by other cards

---

## Summary from the course:

- Chain of Responsibility can be implemented as a chain of references or a centralized construct
- Enlist objects in the chain, possibly controlling their order
- Object removal from chain (e.g., in Dispose())

---