# Strategy

> **Note**
> System behavior partially specified at runtime.

Enables the exact behavior of a system to be selected either at run-time (dynamic) or compile-time (static).
Also known as a policy (esp. in the C++ world).

## Intent

> **Important**
> **Intent**
> Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it.

## Explanation

The Strategy pattern is a behavioral design pattern that lets you define a family of algorithms, encapsulate each one, and make them interchangeable at runtime. The pattern allows the algorithm to vary independently from the clients that use it, promoting flexibility and loose coupling in software design.

---

### Motivation to use

- Many algorithms can be decomposed into higher- and lower- level parts
- Making tea can be decomposed into
  - The process of making a hot beverage (boil water, pour into cup); and
  - Tea-specific things (put teabag into water)
- The high-level algorithm can then be reused for making coffee or hot chocolate
  - Supported by beverage-specific strategies

---

## Summary from the course

- Define an algorithm at a high level
- Define the interface you expect each strategy to follow
- Provide for either dynamic or static composition of strategy in the overall algorithm

---
