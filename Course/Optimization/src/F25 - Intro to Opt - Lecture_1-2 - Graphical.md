# Lecture 2: Graphical LP Solution & Simplex Method (Part 1)
**Dr. Mohammad Reza Bahrami**
*Innopolis University*
*Course of Introduction to Optimization*
*Fall, 2025*

---

## Content
- [Graphical LP Solution](#graphical-lp-solution)
- [Transition from Graphical to Algebraic Solution](#transition-from-graphical-to-algebraic-solution)
- [The Essence of the Simplex Method](#the-essence-of-the-simplex-method)

---

## Graphical LP Solution

### Tatar-Paint Problem (Example)
Consider the Tatar-Paint problem:

**Objective:**
Maximize
$$
z = 5x_1 + 4x_2
$$

**Constraints:**
1. $6x_1 + 4x_2 \leq 24$  (1)
2. $x_1 + 2x_2 \leq 6$          (2)
3. $-x_1 + x_2 \leq 1$          (3)
4. $x_2 \leq 2$                (4)
5. $x_1 \geq 0$                (5)
6. $x_2 \geq 0$                (6)

**Key Points:**
- The problem has infinitely many feasible solutions.
- Graphical methods help identify the optimal solution by examining corner points of the feasible region.

---

### Example 1: Tatar-Paint Problem (Maximization)
#### Step 1: Determine Feasible Solution Space
The feasible region is represented graphically as a polygon (ABCDEF in Figure).

#### Step 2: Determine Optimum Solution
- The objective function $z = 5x_1 + 4x_2$ increases in the direction of its gradient.
- The optimal solution occurs at point **C**, where further movement leads to infeasibility.

**Solution:**
Solve equations (1) and (2):
$$
6x_1 + 4x_2 = 24 \quad \text{(1)}
$$
$$
x_1 + 2x_2 = 6 \quad \text{(2)}
$$

Solving gives:
$$
x_1 = 3, \quad x_2 = 1.5
$$
Thus,
$$
z = (5 \times 3) + (4 \times 1.5) = 21
$$

**Daily Profit:** \$21,000.

---

### Example 2: Diet Problem (Minimization)
#### Step 1: Determine Feasible Solution Space
The model is:
$$
\text{Minimize } z = 0.3x_1 + 0.9x_2
$$
**Constraints:**
1. $x_1 + x_2 \geq 800$  (1)
2. $0.21x_1 - 0.30x_2 \leq 0$  (2)
3. $0.03x_1 - 0.01x_2 \geq 0$  (3)
4. $x_1, x_2 \geq 0$

#### Step 2: Determine Optimum Solution
The optimal solution is the intersection of constraints (1) and (2):
$$
x_1 + x_2 = 800
$$
$$
0.21x_1 - 0.30x_2 = 0 \implies x_1 = 470.6, \quad x_2 = 329.4
$$

**Minimum Cost:**
$$
z = (0.3 \times 470.6) + (0.9 \times 329.4) = \$437.64/\text{day}
$$

---

## Transition from Graphical to Algebraic Solution

### Graphical vs. Algebraic Methods
| **Graphical Method**                     | **Algebraic Method**                          |
|-------------------------------------------|----------------------------------------------|
| Plot all constraints                      | Represent solution space with $m$ equations in $n$ variables ($m < n$). |
| Nonnegativity constraints are implicit.   | Explicitly include nonnegativity conditions.  |
| Solution space consists of infinitely many feasible points. | Same infinite solutions, but analyzed algebraically. |

### Basic Solutions and Corner Points
- **Corner points** in the graphical solution correspond to **basic solutions** in algebraic form.
- Basic solutions are found by setting $n - m$ nonbasic variables to zero and solving for the remaining $m$ variables.

#### Maximum Number of Corner Points:
$$
C_8 = \frac{n!}{(n-m)! \, m!}
$$

### Example: Two-Variable LP
**Problem:**
Maximize $z = 2x_1 + 3x_2$
Subject to:
$$
2x_1 + x_2 \leq 4, \quad x_1 + 2x_2 \leq 5, \quad x_1, x_2 \geq 0
$$

**Algebraic Representation:**
Add slack variables $s_1, s_2$:
$$
\begin{align*}
2x_1 + x_2 + s_1 &= 4 \\
x_1 + 2x_2 + s_2 &= 5 \\
x_1, x_2, s_1, s_2 &\geq 0
\end{align*}
$$

**Basic Solutions:**
| Nonbasic Variables | Basic Variables | Basic Solution       | Associated Corner Point | Feasible? | Objective Value $z$ |
|--------------------|-----------------|----------------------|------------------------|-----------|-----------------------|
| $(x_1, x_2)$     | $s_1, s_2$    | $(0, 0), (4, 5)$   | **A**                  | Yes       | 0                     |
| $(x_1, s_1)$     | $x_2, s_2$    | $(4, -3)$          | **F**                  | No        | –                     |
| $(x_1, s_2)$     | $x_2, s_1$    | $(2.5, 1.5)$       | **B**                  | Yes       | 7.5                   |
| $(x_2, s_1)$     | $x_1, s_2$    | $(2, 3)$           | **D**                  | Yes       | 4                     |
| $(x_2, s_2)$     | $x_1, s_1$    | $(5, -6)$          | **E**                  | No        | –                     |
| $(s_1, s_2)$     | $x_1, x_2$    | $(1, 2)$           | **C** (Optimum)        | Yes       | 8                     |

---

## The Essence of the Simplex Method

### Standard Form Requirements
- All constraints are equations with nonnegative RHS.
- All variables are nonnegative.

### Simplex Iterations
1. Start with an initial feasible solution (e.g., set all original variables to zero).
2. Identify which basic variable can increase $z$ most efficiently (entry row).
3. Determine the limiting constraint for increasing that variable (exit column).
4. Perform pivot operations to update the basis.
5. Repeat until no further improvement is possible.

### Example: Simplex Method Application
**Problem:**
Maximize:
$$
z = 5x_1 + 4x_2 + 3x_3
$$
Subject to:
$$
\begin{align*}
2x_1 + 3x_2 + x_3 &\leq 5 \\
4x_1 + x_2 + 2x_3 &\leq 11 \\
3x_1 + 4x_2 + 2x_3 &\leq 8 \\
x_1, x_2, x_3 &\geq 0
\end{align*}
$$

**Step-by-Step:**
- Introduce slack variables $s_1, s_2, s_3$.
- Initial feasible solution: $(x_1, x_2, x_3) = (0, 0, 0)$, with slacks:
  $$
  s_1 = 5, \quad s_2 = 11, \quad s_3 = 8.
 
$$
- Objective value $z = 0$.
- Iterate until optimality is achieved.

---
**By Dr. Bahrami – Fall 2025**
---

# The Simplex Method - Example

Since all of these conditions must be met, we see that $x_1$ cannot exceed the smallest bound:
$$
x_1 \leq \frac{2}{2}
$$

Our improved solution is then:
$$
\begin{align*}
x_1 &= 5 \\
x_2 &= 0 \\
x_3 &= 0 \\
s_1 &= 0 \\
s_2 &= 1 \\
s_3 &= \frac{1}{2}
\end{align*}
$$

What made the first step easy was that we had one group of variables initially set to zero, and the rest were explicitly expressed in terms of these.

We must rewrite the equations in (2) so that $x_1$, $s_2$, $s_3$, and $z$ are functions of $x_2$, $x_3$, and $s_1$.

To this end:
$$
x_1 = \frac{5}{2} - \frac{3}{2}s_1 - \frac{1}{2}x_2 - \frac{1}{2}x_3
$$

Performing analogous row operations for $s_2$, $s_3$, and $z$, we can rewrite the equations:
$$
z = 12.5 - 2.5s_1 - 3.5x_2 + 0.5x_3
$$
subject to:
$$
\begin{align*}
x_1 &= 2.5 - 0.5s_! - 1.5x_2 - 0.5x_3 \\
s_2 &= 1 + 2s_1 + 5x_2 \\
s_3 &= 0.5 + 1.5s_1 + 0.5x_2 - 0.5x_3
\end{align*}
$$

---

**Lecture 2: Graphical Solution & Simplex Method (1)**

**Course:** Introduction to Optimization

Now, increasing $s_1$ or $x_2$ decreases the objective function value. Since only $x_3$ has a positive coefficient in $z$, it is the only variable we can increase further.

We need to determine how much $x_1$ (denoted as $x$) can be increased without violating non-negativity constraints for dependent variables ($x_1, s_2, s_3$).

From the equations:
- The equation for $s_2$ is unaffected by changes in $x_3$,
- Bounds from $x_3$ and $s_3$ give:
  $$
  x_3 \leq 5, \quad x_3 \leq 1
 
$$

Current solution values:
$$
\begin{align*}
x_1 &= 2 \\
x_2 &= 0 \\
x_3 &= 1 \\
s_1 &= 0 \\
s_2 &= 1 \\
s_3 &= 0
\end{align*}
$$
The objective function value is $z = 13$.

---

**Lecture 2: Graphical Solution & Simplex Method (1)**

Current solution values:
$$
\begin{align*}
x_1 &= 2 \\
x_2 &= 0 \\
x_3 &= 1 \\
s_1 &= 0 \\
s_2 &= 1 \\
s_3 &= 0
\end{align*}
$$

We must determine if further increases in $z$ are possible. Rewriting equations with $z$, $x_1$, $x_3$ and $s_2$ expressed as functions of $s!$, $s_3$, and $x_1$:

From the last equation:
$$
x_3 = 1 + 3s_1 + x_1 - 2s_3
$$
Performing row operations, we get:
$$
z = 13 - s_1 - 3x_2 - s_3
$$

Subject to:
$$
\begin{align*}
x_1 &= 2 - 2s_1 - 2x_2 + s_3 \\
s_2 &= 1 + 2s_1 + 5x_2 \\
x_3 &= 1 + 3s_1 + x_2 - 2s_3
\end{align*}
$$

---

**Lecture 2: Graphical Solution & Simplex Method (1)**

We are now ready for the third iteration. The first step is to identify an independent variable that, if increased, would increase $z$. However, no such variable exists since all coefficients in $z$ are negative.

Since our current solution yields $z = 13$, it is optimal.

---

**Lecture 2: Graphical Solution & Simplex Method (1)**

**Course:** Introduction to Optimization

**By Dr. Bahrami – Fall 2025**

### The Simplex Method – Some Terminology
- **Dictionaries**: Systems of equations (2), (3), and (4) encountered along the way.
- **Basic Variables**: Excluding $z$, variables on the left-hand side (dependent variables).
- **Nonbasic Variables**: Variables on the right-hand side (independent variables).
- **Basic Feasible Solutions**: Solutions where nonbasic variables are set to zero.
