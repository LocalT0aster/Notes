# SOLID principle

---

### Definition:

SOLID is an acronym for five key principles in object-oriented design and programming:

1. [Single responsibility principle (SRP)](SRP.md): A class should have only one reason to change.
2. [Open-Closed Principle (OCP)](OCP.md): Software entities should be open for extension but closed for modification.
3. [Liskov Substitution Principle (LSP)](LSP.md): Subtypes must be substitutable for their base types.
4. [Interface Segregation Principle (ISP)](ISP.md): Clients should not be forced to depend on interfaces they do not use.
5. [Dependency Inversion Principle (DIP)](DIP.md): High-level modules should not depend on low-level modules. Both should depend on abstractions.

These principles aim to make software designs more understandable, flexible, and maintainable.

---

## Summary from the course:

- (SRP) Single Responsibility Principle:
    - A class should only have one reason to change
    - Separation of concerns — different classes handling different, independent tasks/problems
- (OCR) Open-Closed Principle:
    - Classes should be open for extension but closed for modification
- (LSP) Liskov Substitution Principle:
    - You should be able to substitute a base type for a subtype
- (ISP) Interface Segregation Principle:
    - Don’t put too much into an interface; split it into separate interfaces
    - YAGNI — You Ain’t Going to Need It
- (DIP) Dependency Inversion Principle:
    - High-level modules should not depend upon low-level ones; use abstractions
