# Null Object

> A behavioral design pattern with no behaviors 🙂
>

<aside>
💡 A no-op object that conforms to the required interface, satisfying a dependency requirement of some other object.

</aside>

## Intent:

### The Null Object pattern encapsulates the absence of an object by providing a substitutable alternative that offers do nothing behavior.

## Explanation:

> The Null Object design pattern provides a default object that does nothing in place of a null reference, preventing null reference exceptions. It defines an abstract interface for a certain task, and if there's no data to be processed, instead of using a null reference, a null object implementing this interface is used. This reduces the need for null checking and improves code readability and robustness.
>

---

### Motivation to use:

- When component A uses component B, it typically assumes that B is non-null
    - You inject B, not B? or some Option<B>
    - You do not check for null (?.) on every call
- There is no option of telling A not to use an instance of B
    - Its use is hard-coded
- Thus, we build a no-op, non-functioning inheritor of B and pass it into A

---

## Summary from the course:

- Implement the required interface
- Rewrite the methods with empty bodies
    - If method is non-void, return default(T)
    - If these values are ever used, you are in trouble
- Supply an instance of Null Object in place of actual object
- Dynamic construction possible
    - With associated performance implications

---