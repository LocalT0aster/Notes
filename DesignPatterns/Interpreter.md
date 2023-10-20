# Interpreter

> **Note**
> Interpreters are all around us. Even now, in this very room.

A component that processes structured text data. Does so by turning it into separate lexical tokens (lexing) and then interpreting sequences of said tokens (parsing).

## Intent

> **Important**
> **Intent**
> Given a language, define a representation for its grammar along with an interpreter that uses the representation to interpret sentences in the language.

## Explanation

The Interpreter design pattern is a behavioral pattern used when you want to define grammar for simple languages, represent sentences in the language, and interpret these sentences. In essence, it turns a string (or other representation) into an object in the program that can be processed. It's useful when the language it interprets is simple, changes infrequently, and performance is not a critical concern.

---

### Motivation to use

- Textual input needs to be processed
  - E.g., turned into OOP structures
- Some examples
  - Programming language compilers, interpreters and IDEs
  - HTML, XML and similar
  - Numeric expressions (3+4/5)
  - Regular expressions
- Turning strings into OOP based structures in a complicated process

---

## Summary from the course

- Barring simple cases, an interpreter acts in two stages
- Lexing turns text into a set of tokens, e.g.
  - 3*(4+5) > Lit[3] Star Lparen Lit[4] Plus Lit[5] Rparen
- Parsing tokens into meaningful constructs
  - → MultiplicationExpression[ Integer[3], AdditionExpression [ Integer[4], Integer[5] ]
- Parsed data can then be traversed

---

[<kbd><br><- Return<br></kbd>](DesignPatterns.md)
