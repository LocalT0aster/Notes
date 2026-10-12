---
**Lecture 3: Simplex Method (Part 3)**
*Course: Introduction to Optimization*
*By Dr. Mohammad Reza Bahrami – Fall, 2024*

---

### **Materials**
Materials are taken from different sources with modifications.
I do not claim any authorship of these materials.

---

### **Lecture 3: Simplex Method (Part 3)**
*Course: Introduction to Optimization*
*By Dr. Mohammad Reza Bahrami – Fall, 2025*

---

## **1. The Simplex Method (Part 3)**
### **Artificial Starting Solution**

---

## **Computational Details of a Simplex Algorithm Using Tableau**
*(Example: Tatar-Paint Problem with Slack Variables)*

### **Problem Statement**
**Maximize:**
$$
z = 5x_1 + 4x_2 + 0s_1 + 0s_2 + 0s_3 + 0s_4
$$

**Subject to:**
$$
\begin{align*}
6x_1 + 4x_2 + s_1 &= 24 \\
x_1 + 2x_2 + s_2 &= 6 \\
-x_1 + x_2 + s_3 &= 1 \\
x_2 + s_4 &= 2
\end{align*}
$$
**Variables ≥ 0:**
$$
x_1, x_2, s_1, s_2, s_3, s_4 \geq 0
$$

---

### **Starting Simplex Tableau**
The initial tableau is constructed with slack variables $s_1, s_2, s_3, s_4$:

| Basic | $x_1$ | $x_2$ | $s_1$ | $s_2$ | $s_3$ | $s_4$ | **Sol.** |
|-------|---------|---------|---------|---------|---------|---------|----------|
|       |         |         |         |         |         |         |          |
| $z$-row | -5      | -4      | 0       | 0       | 0       | 0       | 0        |
| $s_1$   | 6       | 4       | 1       | 0       | 0       | 0       | 24       |
| $s_2$   | 1       | 2       | 0       | 1       | 0       | 0       | 6        |
| $s_3$   | -1      | 1       | 0       | 0       | 1       | 0       | 1        |
| $s_4$   | 0       | 1       | 0       | 0       | 0       | 1       | 2        |

---

### **Is the Starting Solution Optimal?**
The objective function $z = 5x_1 + 4x_2$ suggests improving by increasing nonbasic variables. Since $x_1$ has the most positive coefficient, it is selected as the entering variable.

**Simplex Optimality Condition:**
- The entering variable is the nonbasic variable with the **most negative** coefficient in the objective row.
- Here: $x_1$ (coefficient = -5).

---

### **Determining the Leaving Variable**
Compute ratios of RHS to positive coefficients under $x_1$:

| Basic | $x_1$ | Sol. | Ratio ($Sol./x_1$) |
|-------|---------|------|----------------------|
| $s_1$ | 6       | 24   | $24/6 = 4$        |
| $s_2$ | 1       | 6    | $6/1 = 6$         |
| $s_3$ | -1      | 1    | **Ignored (negative)** |
| $s_4$ | 0       | 2    | **∞ (zero denominator, ignored)** |

**Minimum Ratio:** $4$
→ Leaving variable: $s_1$, entering value: $x_1 = 4$.

---

### **Gauss-Jordan Row Operations**
#### **Step 1: Pivot Row Update**
- Replace $s_1$ in the Basic column with $x_1$.
- New pivot row (divide by pivot element, 6):
$$
\text{New } x_1\text{-row} = \frac{(6, 4, 1, 0, 0, 0, 24)}{6} = (1, \frac{2}{3}, \frac{1}{6}, 0, 0, 0, 4)
$$

#### **Step 2: Update Other Rows**
- **$z$-row:**
$$
\text{New } z\text{-row} = (-5, -4, 0, 0, 0, 0) + (5 \times \text{new pivot row})
$$
→ $(0, -\frac{2}{3}, \frac{1}{6}, 0, 0, 0, 20)$

- **$s_3$-row:**
$$
\text{New } s_3\text{-row} = (-1, 1, 0, 0, 1, 0) + (1 \times \text{new pivot row})
$$
→ $(0, \frac{5}{3}, 0, 0, 1, 0, 5)$

- **$s_2$-row:**
$$
\text{New } s_2\text{-row} = (1, 2, 0, 1, 0) - (\frac{1}{6} \times \text{new pivot row})
$$
→ $(0, \frac{4}{3}, -\frac{1}{6}, 1, 0, 0, 2)$

- **$s_4$-row:**
$$
\text{New } s_4\text{-row} = (0, 1, 0, 0, 0) - (\frac{0}{6} \times \text{new pivot row})
$$
→ $(0, 1, 0, 0, 0, 1, 2)$

**Updated Tableau:**
| Basic | $x_1$ | $x_2$ | $s_1$ | $s_2$ | $s_3$ | $s_4$ | **Sol.** |
|-------|---------|---------|---------|---------|---------|---------|----------|
|       |         |         |         |         |         |         |          |
| $z$-row | 0      | -2/3    | 1/6     | 0       | 0       | 0       | 20       |
| $x_1$   | 1      | 2/3     | 1/6     | 0       | 0       | 0       | 4        |
| $s_2$   | 0      | 4/3     | -1/6    | 1       | 0       | 0       | 2        |
| $s_3$   | 0      | 5/3     | 0       | 0       | 1       | 0       | 5        |
| $s_4$   | 0      | 1       | 0       | 0       | 0       | 1       | 2        |

---

### **Iteration Summary**
- **Optimal Solution:** All $z$-row coefficients are nonnegative.
- **Decision Variables:**
  - $x_1 = 4$
  - $x_2 = \frac{3}{2}$ (from $s_2$ row: $2 / (\frac{4}{3}) = 1.5$)

---

## **Summary of Simplex Method**
### **Key Rules:**
1. **Optimality Condition:**
   - For maximization, enter the nonbasic variable with the most negative coefficient in the objective row.
   - Optimum reached when all $z$-row coefficients are ≥ 0.

2. **Feasibility Condition:**
   - Leaving variable is the basic variable with the smallest positive ratio (RHS/positive pivot element).

3. **Gauss-Jordan Operations:**
   - Replace leaving variable in Basic column with entering variable.
   - Divide pivot row by pivot element.
   - Subtract multiples of the pivot row from other rows.

---

## **Artificial Starting Solution**
### **When Slack Variables Are Insufficient**
- Problems with **equality/inequality constraints** (not all ≤) require artificial variables.
- Methods:
  1. **M-Method:** Penalize artificial variables in objective function ($-M$ for max, $+M$ for min).
  2. **Two-Phase Method:** First phase eliminates artificial variables; second solves original problem.

---

## **Example: M-Method**
### **Problem:**
Minimize $z = 4x_1 + x_2$
Subject to:
$$
\begin{align*}
3x_1 + x_2 &= 3 \\
4x_1 + 3x_2 &\geq 6 \\
x_1 + 2x_2 &\leq 4 \\
x_1, x_2 &\geq

Here’s the cleaned and structured Markdown version of your PDF text:

---

# Basic Solution
The starting basic solution is $R!$, $R"$, and $x_3 = (3, 6, 4)$.

---

## Lecture 3: Simplex Method Part (3)
**Course:** Introduction to Optimization
**Instructor:** Dr. Bahrami – Fall 2025

---

### M-Method Example Continued
The objective coefficients for $x_1$ and $x"$ are 4 and 1, respectively. A reasonable choice is $M = 100$.

#### Iteration 0
| Basic       | $x_1$ | $x"$ | $x#$ | $R!$   | $R"$   | $x$$ | Sol. | $z$          |
|-------------|----------|----------|----------|-----------|-----------|---------|-------|------------------|
|             | -4       | -1       | 0        | -100      | -100      | 0       |       |                  |
| $R!$    | 3        | 1        | 0        | 1         | 0         | 0       | 3     |                  |
| $R"$    | 4        | 3        | -1       | 0         | 1         | 0       | 6     |                  |
| $x$$    | 1        | 2        | 0        | 0         | 0         | 1       | 4     |                  |

**Current Basic Solution:**
- Nonbasic: $x_1 = x" = x# = 0$
- Basic: $R! = 3$, $R" = 6$, $x$ = 4
- Objective value: $z = (1, 0, 0) \cdot [3] + (1, 0, 0) \cdot [6] + (4 \times 0) = 9$

To correct the inconsistency in the objective row:
$$
\text{New } z\text{-row} = \text{Old } z\text{-row} + (100 \times R! - \text{row}) + (100 \times R" - \text{row})
$$

#### Iteration 1
| Basic       | $x_1$ | $x"$ | $x#$ | $R!$   | $R"$   | $x$$ | Sol. | $z$          |
|-------------|----------|----------|----------|-----------|-----------|---------|-------|------------------|
|             | 696      | 399      | -100     | 0         | 0         | 0       |       | 900              |
| $R!$    | 3        | 1        | 0        | 1         | 0         | 0       | 3     |                  |
| $R"$    | 4        | 3        | -1       | 0         | 1         | 0       | 6     |                  |
| $x$$    | 1        | 2        | 0        | 0         | 0         | 1       | 4     |                  |

**Result:** $R!$ and $R"$ are now substituted out in the objective row, yielding $z = 900$.

#### Iteration 2
| Basic       | $x_1$ | $x"$ | $x#$ | $R!$   | $R"$   | $x$$ | Sol. | $z$          |
|-------------|----------|----------|----------|-----------|-----------|---------|-------|------------------|
|             | 0        | 167      | -100     | -232      | 0         | 0       |       | 204              |
| $x_1$   | 1        | 1/3      | 0        | 1/3       | 0         | 0       | 1     |                  |
| $R"$    | 0        | 5/3      | -1       | -4/3      | 1         | 0       | 2     |                  |
| $x$$    | 0        | 5/3      | 0        | -1/3      | 0         | 1       | 3     |                  |

**Objective Row:**
$$
z = \begin{bmatrix} 0 & 0 & 1/5 & -492/5 & -501/5 & 0 \\ 1 & 0 & 3/5 & -1/5 & 0 & 3/5 \\ 0 & 1 & -3/5 & -4/5 & 3/5 & 6/5 \\ 0 & 0 & 1 & 1 & -1 & 1 \end{bmatrix}
$$

**Optimum Solution:**
- $x_1 = 2/5$
- $x" = 9/5$
- $z = 17/5$

---

### Remarks
Using the penalty $M$ does not force an artificial variable to zero in the final iteration if the LP has no feasible solution. In such cases, at least one artificial variable will remain positive.

---

## Two-Phase Method

### Overview
The two-phase method avoids using a constant $M$, instead solving the problem in two phases:

#### Phase I:
1. Add artificial variables to constraints to ensure a basic feasible solution.
2. Minimize (or maximize) the sum of artificial variables.
   - If the minimum value is positive, no feasible solution exists.
   - Otherwise, proceed to Phase II.

#### Phase II:
- Use the feasible solution from Phase I as a starting point for the original problem.

---

### Example

#### Original Problem
Minimize $z = 4x_1 + x"$
Subject to:
$$
3x_1 + x" = 3 \\
4x_1 + 3x" - x# + R" = 6 \\
x_1 + 2x" + x$ = 4 \\
x_1, x", x#, x$, R!, R" \geq 0
$$

#### Phase I: Minimize $r = R! + R"$
Subject to:
$$
3x_1 + x" + R! = 3 \\
4x_1 + 3x" - x# + R" = 6 \\
x_1 + 2x" + x$ = 4 \\
$$

**Tableau:**
| Basic       | $x_1$ | $x"$ | $x#$ | $R!$   | $R"$   | $x$$ | Sol. | $r$          |
|-------------|----------|----------|----------|-----------|-----------|---------|-------|------------------|
|             | 0        | 0        | 0        | -1        | -1        | 0       |       | 0                |
| $R!$    | 3        | 1        | 0        | 1         | 0         | 0       | 3     |                  |
| $R"$    | 4        | 3        | -1       | 0         | 1         | 0       | 6     |                  |
| $x$$    | 1        | 2        | 0        | 0         | 0         | 1       | 4     |                  |

**Row Operation:**
$$
\text{New } r\text{-row} = \text{Old } r\text{-row} + (R! - \text{row}) + (R" - \text{row})
$$
Resulting in:
$$
r = 7x_1 + 4x" - x# + 0 R! + 0 R" + 0 x$
$$

#### Iteration Tableau (Phase I)
| Basic       | $x_1$ | $x"$ | $x#$ | $R!$   | $R"$   | $x$$ | Sol. | $r$          |
|-------------|----------|----------|----------|-----------|-----------|---------|-------|------------------|
|             | 7        | 4        | -1       | 0         | 0         | 0       |       | 9                |
| $R!$    | 3        | 1        | 0        | 1         | 0         | 0       | 3     |                  |
| $R"$    | 4        | 3        | -1       | 0         | 1         | 0       | 6     |                  |
| $x$$    |
