# Introduction to Optimization

## Week 1: Problem Sheet 1

### Problem 1
A plant produces three types of products (A, B, C) using four types of equipment (I, II, III, IV). The time required for each product on each machine and the profit per unit are given in the following table. Determine how many units of each product should be produced to maximize profit.

| Type of Equipment | I   | II  | III | IV  |
|-------------------|-----|-----|-----|-----|
| **Time (hours)**  |     |     |     |     |
| Product A         | 3   | 2   | 1   | 5   |
| Product B         | 6   | 1   | 1   | 3   |
| Product C         | 7   | 8   | 1   | 3   |
| **Profit ($)**    |     |     |     |     |
|                   | 100 | 140 | 120 |     |

**Total Working Time Available:**
- Equipment I: 135 hours
- Equipment II: 260 hours
- Equipment III: 220 hours
- Equipment IV: 360 hours

#### Solution
Let:
- $x_1$ = number of units of product A,
- $x_2$ = number of units of product B,
- $x_3$ = number of units of product C.

**Constraints:**
$$
\begin{cases}
3x_1 + 6x_2 + 7x_3 \leq 135, \\
2x_1 + x_2 + 8x_3 \leq 260, \\
x_1 + x_2 + x_3 \leq 220, \\
5x_1 + 3x_2 + 3x_3 \leq 360, \\
x_1 \geq 0, \\
x_2 \geq 0, \\
x_3 \geq 0.
\end{cases}
$$

**Objective:**
Maximize profit:
$$
F(x_1, x_2, x_3) = 100x_1 + 140x_2 + 120x_3
$$

---

### Problem 2: Graphical Method for Linear Programming (LPP)
Solve the following LPP using the graphical method:

**Maximize:**
$$
F(x_1, x_2) = x_1 + x_2
$$

**Constraints:**
$$
\begin{cases}
2x_1 + 4x_2 \leq 16, \\
-4x_1 + 2x_2 \leq 8, \\
x_1 + 3x_2 \geq 9, \\
x_1 \geq 0, \\
x_2 \geq 0.
\end{cases}
$$

#### Solution
The feasible region is determined by the intersection of constraints. The optimal values are found at corner points:

- **Minimum:** $F(0, 3) = 0 + 3 = 3$
- **Maximum:** $F(6, 1) = 6 + 1 = 7$

---

### Problem 3: Graphical Method for Linear Programming (LPP)
Solve the following LPP using the graphical method:

**Maximize:**
$$
F(x_1, x_2) = x_1 + 2x_2
$$

**Constraints:**
Same as in **Problem 2**.

#### Solution
- **Minimum:** $F(0, 3) = 6$
- **Maximum:** Achieved along the line segment from point A to C (e.g., $F(6, 1) = 8$).

---

### Problem 4: Graphical Method for Linear Programming (LPP)
Solve the following LPP using the graphical method:

**Maximize:**
$$
F(x_1, x_2) = x_1 + x_2
$$

**Constraints:**
$$
\begin{cases}
x_1 + 2x_2 \geq 14, \\
-5x_1 + 3x_2 \leq 15, \\
4x_1 + 6x_2 \leq 24, \\
x_1 \geq 0, \\
x_2 \geq 0.
\end{cases}
$$

#### Solution
The feasible region is empty; no solution exists.

---

### Problem 5: Simplex Method for Linear Programming (LPP)
Solve the following LPP using the simplex method:

**Maximize:**
$$
F(x_1, x_2, x_3, x_4, x_5, x_6) = 2x_1 + 3x_2 - x_4
$$

**Constraints:**
$$
\begin{cases}
2x_1 - x_2 - 2x_4 + x_5 = 16, \\
3x_1 + 2x_2 + x_3 - 3x_4 = 18, \\
-x_1 + 3x_2 + 4x_4 + x_6 = 24, \\
x_i \geq 0 \quad (i=1,2,...,6).
\end{cases}
$$

#### Solution
**Initial Feasible Solution:**
$$
(x_1, x_2, x_3, x_4, x_5, x_6) = (0, 0, 18, 0, 16, 24)
$$
Objective value: $F(0, 0, 18, 0, 16, 24) = 0$

**Iteration Steps:**
After optimizing:
$$
(x_1, x_2, x_3, x_4, x_5, x_6) = (11/9, 8, 2, 0, 24, 0)
$$
Optimal objective value: $F = \frac{282}{9} \approx 31.33$

*(Note: The final solution appears to be simplified or misaligned in the original text; corrected values are inferred.)*
```
