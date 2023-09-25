# Flyweight

> Space optimization!
>

<aside>
💡 A space optimization technique that lets us use less memory by storing externally the data associated with similar objects.

</aside>

## Intent:

### Use sharing to support large numbers of fine-grained objects efficiently.

## Explanation:

> The Flyweight design pattern is a structural pattern used for efficiency, mainly to reduce the memory usage when dealing with a large number of objects that share many common state-independent properties. Instead of creating each object from scratch, the pattern uses sharing to support large numbers of fine-grained objects efficiently, by reusing existing instances of objects with the same values.
>

---

### Motivation to use:

- Avoid redundancy when storing data E.g., MMORPG
    - Plenty of users with identical first/last names
    - No sense in storing same first/last name over and over again
    - Store a list of names and pointers to them
- .NET performs string interning, so an identical string is stored only once
- E.g., bold or italic text in the console
    - Don't want each character to have a formatting character
    - Operate on ranges (e.g., line number, start/end positions)

---

## Summary from the course:

- Store common data externally
- Define the idea of ‘ranges’ on homogeneous collections and store data related to those ranges
- .NET string interning is the Flyweight pattern

---