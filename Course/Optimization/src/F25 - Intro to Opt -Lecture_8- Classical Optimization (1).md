# Lecture 8: Classical Optimization Theory (1)

**Dr. Mohammad Reza Bahrami**
*Innopolis University*
*Course of Optimization*
*Fall 2025*

---

## Course Materials
Materials are taken from different sources with modifications.
No authorship claimed by Dr. Mohammad Reza Bahrami.

---

# Lecture: Introduction to Optimization

## Lecture 8: Classical Optimization (1)

---

### Content
- [Unconstrained Problems](#unconstrained-problems)
- [Constrained Problems](#constrained-problems)

---

## Unconstrained Problems

A point $X! = (x"_!, ..., x_#!, ..., x$!)$ is an **extreme point** of a function $f(X)$, defining either a maximum or minimum:

For a **maximum**:
$$
f(X_0 + h) \leq f(X!)
$$
for all $h = (h"_ , ..., h#_, ..., h$ )$, where $h#$ is sufficiently small for all $j$.

For a **minimum**:
$$
f(X! ) \leq f(X_0 + h)
$$

### Single-Variable Function Example
A single-variable function $f(x)$ over the range $a \leq x \leq b$:
- Points $x! , x"_ , x#_, x$_, and $x%$ are extrema.
  - $x! , x#_, x%$: **Local/Global maxima**.
  - $x"_ , x$_: **Local minima**.

The global maximum value is:
$$
f(x%) = \max \{ f(x!), f(x#_), f(x%)\}
$$

### Weak vs. Strong Extrema
- A point $X!$ is a **weak maximum** if:
  $$
  f(X_0 + h) \leq f(X!)
 
$$
- A point $X!$ is a **strong maximum** if:
  $$
  f(X_0 + h) < f(X!)
 
$$

### Necessary Condition for Extrema
The first derivative (slope) of $f$ equals zero at all extrema.
This property also holds for inflection and saddle points, e.g., $x($.

**Note**: If a point with zero slope is not an extremum, it must be an inflection or saddle point.

---

## Necessary and Sufficient Conditions

### Assumption
First and second partial derivatives of $f(X)$ are continuous for all $X$.

#### Theorem 1: Necessary Condition
A necessary condition for $X!$ to be an extreme point is:
$$
\nabla f(X!) = 0
$$
Since this condition also holds at inflection and saddle points, these solutions are called **stationary points**.

#### Theorem 2: Sufficient Conditions
For a stationary point $X!$, the Hessian matrix $H$ evaluated at $X!$ must satisfy:
- If $H$ is **positive definite**, then $X!$ is a **minimum**.
- If $H$ is **negative definite**, then $X!$ is a **maximum**.

---

### Example

Consider the function:
$$
f(x"_ , x), x& = x"_^2 + 2x& + (x)_x& - x")_x - x&)
$$

#### Necessary Condition
Solve for zero gradient:
$$
\frac{\partial f}{\partial x"_} = 1 - 2x"_ = 0 \implies x"_ = \frac{1}{2}
$$
$$
\frac{\partial f}{\partial x)} = x& - 2(x)_ = 0 \implies x& = 2(x)
$$
$$
\frac{\partial f}{\partial x&} = 2 + (x)_ - 2x& = 0 \implies (x) = 4 - 2x&
$$

The solution is:
$$
X! = \begin{bmatrix}
\frac{1}{2} \\
3 \\
3
\end{bmatrix}
$$

#### Hessian Matrix $H$
$$
H =
\begin{bmatrix}
-2 & 1 & 4 \\
1 & 2 & 0 \\
4 & 0 & -2
\end{bmatrix}
$$
Evaluated at $X!$:
$$
H = \begin{bmatrix}
0 & 3 & 3 \\
3 & 6 & 0 \\
3 & 0 & -2
\end{bmatrix}
$$

Since the Hessian is indefinite, $X!$ is a **saddle point**.

---

### Theorem 3: Higher-Order Conditions

For a stationary point $y!$ of $f(y)$, if the first ($n-1$) derivatives are zero and $f^{(n)}(y!) \neq 0$:
- If $n$ is **odd**, $y!$ is an **inflection point**.
- If $n$ is **even**:
  - $f^{(n)}(y!) > 0 \implies$ minimum.
  - $f^{(n)}(y!) < 0 \implies$ maximum.

---

### Example (Graphical Analysis)

#### Function $f(y) = y^*$
- Stationary point: $y! = 0$.
- Second derivative:
  $$
  f''(y) = 4y& + 2, \quad f''(0) = 2 > 0
 
$$
Since $n=2$ (even), $y! = 0$ is a **minimum**.

#### Function $g(y) = y&$
- Stationary point: $g'(y) = 3y) = 0 \implies y! = 0$.
- Second derivative:
  $$
  g''(y) = 6, \quad g''(0) = 6 \neq 0
 
$$
Since $n=1$ (odd), $y! = 0$ is an **inflection point**.

---

## Newton-Raphson Method

### Problem Statement
Solve nonlinear equations $f_i(X) = 0$ for $i = 1, ..., m$.

#### Iterative Formula
Given initial guess $X^-$, use Taylor expansion:
$$
f_i(X) \approx f_i(X^-) + \nabla f_i(X^-) (X - X^-)
$$
Approximate system becomes:
$$
A^- + B^- (X - X^-) = 0
$$
If $B^-$ is nonsingular, solve for $X$:
$$
X = X^- - (B^-)^{-1} A^-
$$

### Convergence
- Iteration stops when successive points $X^-$ and $X^{-1} \approx X^-$.
- For a single-variable function $f(x)$, the update is:
  $$
  x^{-1} = x^- - \frac{f(x^-)}{f'(x^-)}
 
$$

### Example

Consider $g(x) = (3x - 2)^2(2x - 3)$.

#### Stationary Points
Solve $g'(x) = 0$:
$$
72x&^2 - 468x + 241 = 0
$$
Using Newton-Raphson with initial guess $x! = 10$:

| Iteration | $x^-$   |
|-----------|------------|
| Start     | 10         |
| 1st       | ≈ 1.5      |

The method converges to $x = 1.5$.

**Note**: Three stationary points exist at $x = \frac{3}{2}, x = \frac{1}{2}, x = 1$. Additional initial guesses yield the other two.

---

## Constrained Problems

### Equality Constraints: Jacobian Method
#### Problem Statement
Minimize $z = f(X)$ subject to:
$$
g(X) = 0
$$
where $X = (x"_ , x), ..., x$$ and $g = (g"_ , g), ..., g5_6$.

### Constrained Derivatives Concept
The gradient of $f$ at feasible points is derived using the Jacobian matrix.

#### Stationary Point Identification
- Compute constrained derivatives.
- Vanishing gradients identify stationary points for constrained problems.

---

## Equality Constraints: Detailed Method

### Mathematical Development
Using Taylor expansion around a point $X + \Delta X$:
$$
f(X + \Delta X) - f(X) = \nabla f(X) \cdot \Delta X + O(\|\Delta X\|^2)
$$
$$
g(X + \Delta X) - g(X) = \nabla g(X) \cdot \Delta X + O(\|\Delta X\|^2)
$$

For feasibility $g(X) = 0$, the reduced system:
$$
\nabla f(X) \cdot \Delta X = 0, \quad \nabla g(X) \cdot \Delta X = 0
$$
This yields $m+1$ equations in $n+1$ unknowns ($\partial f/\partial x_j$, $\partial X/\partial x_j$).

---

### Jacobian Matrix Setup

Define:
$$
X = (Y, Z)
$$
where $Y = y! , ..., y($ and $Z = z! , ..., z*( )$.

Gradient vectors rewritten in terms of $Y$ and $Z

# Equality Constraints - Constrained Derivatives (Jacobian) Method

## Example

Consider the following problem:

**Objective function:**
$$
f(X) = x_1^2 + 3x_2^2 + 5x_3^2
$$

**Equality constraints:**
$$
g_1(X) = x_1' + 2x_2 + x_3 - 11 = 0
$$
$$
g_2(X) = x_1'' + 2x_1' + x_3' - 14 = 0
$$

Given the feasible point $X^* = (1, 2, 3)$, we study the variation in $f(X)$ ($\partial f / \partial x$) in its feasible neighborhood.

Let:
$$
Y = (x_1', x_3')
$$
$$
Z = x_2
$$

**Partial derivatives of $f$:**
$$
\frac{\partial f}{\partial Y} =
\begin{bmatrix}
\partial f / \partial x_1' & \partial f / \partial x_3'
\end{bmatrix}^T = (2x_1' + 5x_3', 10x_1'x_3')
$$

$$
\frac{\partial f}{\partial Z} =
\frac{\partial f}{\partial x_2} = 6x_2
$$

**Jacobian of constraints $J$:**
$$
J =
\begin{bmatrix}
\partial g_1 / \partial x_1' & \partial g_1 / \partial x_3' & \partial g_1 / \partial x_2 \\
\partial g_2 / \partial x_1'' & \partial g_2 / \partial x_1' & \partial g_2 / \partial x_3'
\end{bmatrix}
$$

At $X^* = (1, 2, 3)$:
$$
J =
\begin{bmatrix}
0 & 2 & 2 \\
2 & 2 & 0
\end{bmatrix}
$$

**Constraint gradients $C$:**
$$
C =
\frac{\partial g}{\partial x} =
\begin{bmatrix}
\partial g_1 / \partial x_1' & \partial g_1 / \partial x_3' & \partial g_1 / \partial x_2 \\
\partial g_2 / \partial x_1'' & \partial g_2 / \partial x_1' & \partial g_2 / \partial x_3'
\end{bmatrix}^T =
\begin{bmatrix}
0 & 2 & 2 \\
2 & 2 & 0
\end{bmatrix}^T =
\begin{bmatrix}
0 & 2 \\
2 & 2 \\
2 & 0
\end{bmatrix}
$$

---

### Example – Continuation

Suppose we estimate $\partial f / \partial x_1'$ for a small change $\Delta x_2 = 0.01$.

Using the formula:
$$
\frac{\partial f}{\partial Y, Z} = \left( \frac{\partial f}{\partial Z} - J^T C \Delta Z \right) \frac{\partial Z}{\partial X}
$$

Compute $J^T C$:
$$
J^T =
\begin{bmatrix}
0 & 2 \\
2 & 2 \\
1 & 0
\end{bmatrix}
$$
$$
J^T C =
\begin{bmatrix}
3 & 6 \\
-2 & -4 \\
1 & 1.667
\end{bmatrix}
$$

The matrix multiplication yields:
$$
J^T C \Delta Z = \begin{bmatrix} 6 \\ 2 \\ 12 - 6 \end{bmatrix} \times 0.01 = \begin{bmatrix} 0.06 \\ 0.02 \\ 0.06 \end{bmatrix}
$$

Compute $\partial f / \partial x$:
$$
\frac{\partial f}{\partial Y, Z} =
\begin{bmatrix}
2x_1' + 5x_3' & 10x_1'x_3'
\end{bmatrix}^T - J^T C \Delta Z = (6.2 - 47, 30) \quad \text{(corrected for clarity)}
$$

$$
\partial f / \partial x_1' = 6.2 - (47 + 30) \approx -2.50
$$
$$
\frac{\Delta f}{\Delta x_2} = -0.4601
$$

---

### Feasible Adjustments for $\Delta x_1'$

For $\Delta x_2 = 0.01$, feasible changes in $x_1'$ and $x_3'$ are determined by:
$$
\Delta Y = -J^T C \Delta Z
$$
At $X^*$:
$$
\Delta x_1' = -0.0283, \quad \Delta x_3' = 0.0250
$$

**Comparison:**
- Approximated $\partial f / \partial x_2 = -0.4601$
- Direct finite difference: $f(X^* + \Delta X) - f(X^*) = -0.477$

---

## Example – Revised Problem

### Objective function:
$$
f(X) = x_1'' + x_2 + 5x_3
$$

### Equality constraints:
$$
g_1(X) = x_1' + x_2 + 3x_3 - 2 = 0
$$
$$
g_2(X) = 5x_1'' + 2x_2 + x_3 - 5 = 0
$$

Let:
$$
Y = (x_1', x_2), \quad Z = x_3
$$

**Partial derivatives of $f$:**
$$
\frac{\partial f}{\partial Y} =
\begin{bmatrix}
\partial f / \partial x_1' & \partial f / \partial x_2
\end{bmatrix}^T = (2x_1', 2x_2)
$$

$$
\frac{\partial f}{\partial Z} =
\frac{\partial f}{\partial x_3} = 2x_3
$$

**Jacobian $J$:**
At $X^*$:
$$
J =
\begin{bmatrix}
1 & 1 & 3 \\
5 & 2 & 1
\end{bmatrix}
$$

**Constraint gradients $C$:**
$$
C^T =
\begin{bmatrix}
1 & 5 \\
1 & 2 \\
3 & 1
\end{bmatrix}
$$

---

### Stationary Point Analysis

The equations for stationary points are:
$$
\nabla f = 0, \quad g_1(X) = 0, \quad g_2(X) = 0
$$
Or:
$$
\begin{bmatrix}
0 \\
1 \\
3
\end{bmatrix} x_1' + \begin{bmatrix}
0 \\
2 \\
5
\end{bmatrix} x_2 + \begin{bmatrix}
-2 \\
-5
\end{bmatrix} x_3 = 0
$$

Solving gives approximate solution:
$$
X^* \approx (0.81, 0.35, 0.28)
$$

**Sufficiency Check:**
For $x_3$ as the independent variable, from $\nabla f = 0$:
$$
\frac{\partial f}{\partial x_1'} = 10 \, dx_1' \\
\frac{\partial f}{\partial x_2} = -28 \, dx_2 \\
\frac{\partial f}{\partial x_3} = 2 \, dx_3
$$

Using Jacobian method:
$$
dx_1' = \frac{-\begin{vmatrix}
-5 & 2 \\
-2 & 1
\end{vmatrix}}{\begin{vmatrix}
1 & 3 \\
5 & 1
\end{vmatrix}} dx_3 = \frac{-(-7)}{(1 - 15)} dx_3 = -\frac{7}{-14} \, dx_3 = 0.5 \, dx_3
$$

$$
dx_2 = \frac{\begin{vmatrix}
1 & 3 \\
5 & 1
\end{vmatrix}}{\begin{vmatrix}
1 & 3 \\
5 & 1
\end{vmatrix}} dx_3 = \frac{(-14)}{-14} \, dx_3 = -1 \, dx_3
$$

$$
\frac{\partial f}{\partial x_3} = 2 \, dx_3 > 0
$$
Thus, $X^*$ is a **minimum** point.
```
