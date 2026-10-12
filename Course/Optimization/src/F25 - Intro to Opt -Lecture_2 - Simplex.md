# Lecture 2: Simplex Method (Part 2)

**Dr. Mohammad Reza Bahrami**
*Innopolis University*
*Course of Introduction to Optimization*
*Fall, 2025*

---

## Content

- [x] The Simplex Method (part 2)
  - [ ] Iterative Nature of the Simplex Method
  - [ ] Computational Details of a Simplex Algorithm Using Table
  - [ ] Artificial Starting Solution

---

## Iterative Nature of the Simplex Method

The simplex method always begins at the origin, where all decision variables $x_j$ ($j = 1, 2, \dots, n$) are zero.

In this scenario:
- Point A represents the origin ($x_1 = x_2 = 0$), with an objective value $z = 0$.

The question arises: Can increasing nonbasic variables $x_1$ and $x_2$ above their current zero values improve (increase) $z$?

To answer this, we examine the objective function:

**Maximize**
$z = 2x_1 + 3x_2$

An increase in either $x_1$ or $x_2$ will improve $z$. However, the simplex method does not allow simultaneous increases.

Instead, it selects one variable at a time based on the highest rate of improvement. Here:
- The rate for $x_1$ is 2.
- The rate for $x_2$ is 3.

Thus, we choose to increase $x_2$.

---

### Path to Optimum
The simplex method moves along edges between corner points (e.g., A → B → C). Each iteration corresponds to a new corner point. It never crosses the solution space directly; it follows feasible paths.

---

## Computational Details of a Simplex Algorithm Using Table

### Tatar-Paint Problem Example
**Maximize**
$z = 5x_1 + 4x_2$

**Subject to:**
$$
\begin{align*}
6x_1 + 4x_2 + s_1 &= 24 \\
x_1 + 2x_2 + s_2 &= 6 \\
-x_1 + x_2 + s_3 &= 1 \\
x_2 + s_4 &= 2
\end{align*}
$$
with $x_1, x_2, s_1, s_2, s_3, s_4 \geq 0$.

Rewrite the objective as:
$$
z - 5x_1 - 4x_2 = 0
$$

---

### Initial Simplex Tableau

| Basic       | $z$   | $x_1$ | $x_2$ | $s_1$ | $s_2$ | $s_3$ | $s_4$ | Sol. |
|-------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|------|
| **z-row**   | 1         | -5        | -4        | 0         | 0         | 0         | 0         | 0    |
| $s_1$   |           | 6         | 4         | 1         | 0         | 0         | 0         | 24   |
| $s_2$   |           | 1         | 2         | 0         | 1         | 0         | 0         | 6    |
| $s_3$   |           | -1        | 1         | 0         | 0         | 1         | 0         | 1    |
| $s_4$   |           | 0         | 1         | 0         | 0         | 0         | 1         | 2    |

---

### Is the Starting Solution Optimal?
The objective function $z = 5x_1 + 4x_2$ suggests improving by increasing nonbasic variables. In the tableau, the most negative coefficient in the objective row is for $x_1$, so it enters the basis.

**Entering Variable:** $x_1$

---

### Determining the Leaving Variable
Compute ratios of RHS to positive coefficients under $x_1$:

| Basic | Sol. | Ratio ($\text{Sol.} / x_k$) |
|-------|------|--------------------------------|
| $s_1$ | 24   | $24/6 = 4$                  |
| $s_2$ | 6    | $6/1 = 6$                   |
| $s_3$ | 1    | Negative (ignore)               |
| $s_4$ | 2    | Undefined (zero denominator, ignore) |

**Leaving Variable:** $s_1$

---

### Swapping Variables: Gauss-Jordan Operations
Replace $s_1$ with $x_1$:

1. **Pivot Row:**
   - New $x_1$-row = Current $s_1$-row ÷ 6:
     $$
(6, 4, 1, 0, 0, 0, 24) / 6 = (1, 2/3, 1/6, 0, 0, 0, 4)
$$

2. **Update Other Rows:**
   - $z$-row: $z \text{-row} - (-5) \times \text{New } x_1\text{-row} = (0, 3, -6, 1, 0, 0, 2)$
   - $s_2$: $s_2 \text{-row} - (1) \times \text{New } x_1\text{-row} = (0, 3/4, -1/6, 1, 0, 0, 2)$
   - $s_3$: $s_3 \text{-row} - (-1) \times \text{New } x_1\text{-row} = (0, 5/3, 0, 0, 1, 0, 5)$
   - $s_4$: Unchanged.

**New Tableau:**

| Basic       | $z$   | $x_1$ | $x_2$ | $s_1$ | $s_2$ | $s_3$ | $s_4$ | Sol. |
|-------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|------|
| **z-row**   | 0         | -2/3      | 5/6       | 0         | 0         | 0         | 0         | 20   |
| $x_1$   | 1         | 2/3       | 1/6       | 0         | 0         | 0         | 0         | 4    |
| $s_2$   |           | 0         | 4/3       | -1/6      | 1         | 0         | 0         | 2    |
| $s_3$   |           | 0         | 5/3       | 0         | 0         | 1         | 0         | 5    |
| $s_4$   |           | 0         | 1         | 0         | 0         | 0         | 1         | 2    |

---

### Next Iteration: Entering Variable $x_2$
Compute ratios for $x_2$:

| Basic       | Sol. | Ratio ($\text{Sol.} / x_k$) |
|-------------|------|--------------------------------|
| $s_2$   | 2    | $2/(4/3) = 1.5$             |
| $s_3$   | 5    | $5/(5/3) = 3$               |
| $s_4$   | 2    | $2/1 = 2$                  |

**Leaving Variable:** $x_2$

---

### Gauss-Jordan Operations for New Pivot

1. **Pivot Row:**
   - New $x_2$-row = Current $s_2$-row ÷ (4/3):
     $$
     (0, 3/4, -1/6, 1, 0, 0, 2) / (4/3)
     $$

2. **Update Other Rows:**
   - $z$-row: $z\text{-row} - (-3) \times \text{New } x_2\text{-row} = (0, 0, 3/4, 1/2, 0, 0, 21)$
   - $x_1$: $x_1\text{-row} - (3) \times \text{New } x_2\text{-row} = (0, 1, 1/4, -1/2, 0, 0, 3)$
   - $s_3$:

# Simplex Table

The solution also gives the status of the resources.

A resource is designated as **scarce** if its associated slack variable is zero—that is, the activities (variables) of the model have used the resource completely. Otherwise, if the slack is positive, then the resource is **abundant**.

The following table classifies the constraints of the model:

| Resource         | Slack Value       | Status   |
|------------------|-------------------|----------|
| Raw material M1  | s_1 = 0            | Scarce   |
| Raw material M2  | s_2 = 0            | Scarce   |
|                  | s_3 = 5            | Abundant |
|                  | s_4 = 2            |          |

---

# Lecture 2: Simplex Method (Part 2)

**Course:** Introduction to Optimization
**By Dr. Bahrami – Fall 2025**

---

## Summary of the Simplex Method

### Optimality Condition
- In a **maximization** problem, the entering variable is the nonbasic variable with the most negative coefficient in the z-row.
- In a **minimization** problem, the entering variable is the nonbasic variable with the most positive coefficient in the z-row.
- The optimum is reached at the iteration where all coefficients in the z-row are nonnegative (for maximization) or nonpositive (for minimization).

### Feasibility Condition
For both maximization and minimization problems:
- The leaving variable is the basic variable associated with the smallest nonnegative ratio, provided its denominator is strictly positive.

---

### Gauss-Jordan Row Operations

1. **Pivot Row**
   - Replace the leaving variable in the Basic column with the entering variable.
   - New pivot row = Current pivot row ÷ Pivot element

2. **All Other Rows (Including z-row)**
   - New row = (Current row) – (Pivot column coefficient) × (New pivot row)
