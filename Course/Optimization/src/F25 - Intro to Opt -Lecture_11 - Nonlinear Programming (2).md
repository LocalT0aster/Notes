# Lecture 11: Nonlinear Programming Algorithms (2)
**Dr. Mohammad Reza Bahrami**
*Innopolis University*
*Course of Optimization*
*Fall 2025*

---

## Course Materials
Materials are taken from different sources with modifications. I do not claim any authorship of these materials.
*Dr. Mohammad Reza Bahrami*

---

# Lecture: Introduction to Optimization
**Lecture 11: Nonlinear Programming (2)**

---

## Content

- [Constrained Problems](#constrained-problems)
- [Quadratic Programming](#quadratic-programming)
- [Linear Combinations Method](#linear-combinations-method)

---

## Nonlinear Programming Algorithms
### Constrained Algorithms

The general constrained nonlinear programming problem is defined as:

Maximize (or minimize) $z = f(\mathbf{X})$

**Subject to:**
$$
g(\mathbf{X}) \leq 0
$$
- The nonnegativity conditions, $\mathbf{X} \geq 0$, are part of the constraints.
- At least one of the functions $f(\mathbf{X})$ and $g(\mathbf{X})$ is nonlinear, and all functions are continuously differentiable.
- Erratic behavior of nonlinear functions precludes developing a single algorithm for the general model.
- The most general applicable result is the **KKT conditions**.
- This section presents several indirect algorithms.

---

## Quadratic Programming

A quadratic programming problem is defined as:

Maximize $z = \mathbf{C}^T \mathbf{X} + \frac{1}{2} \mathbf{X}^T \mathbf{D} \mathbf{X}$

Where:
$$
\mathbf{X}^T \mathbf{D} \mathbf{X}
$$ defines a quadratic form.

**Subject to:**
$$
\mathbf{A} \mathbf{X} \leq \mathbf{b}, \\
\mathbf{X} \geq 0.
$$

Variables:
$$
\mathbf{X} = [x_1, x_2, ..., x_m]^T,
$$
$$
\mathbf{C} = [c_1, c_2, ..., c_m]^T,
$$
$$
\mathbf{b} = [b_1, b_2, ..., b_n]^T.
$$

Matrices:
$$
\mathbf{A} =
\begin{bmatrix}
a_{11} & \cdots & a_{1m} \\
\vdots & \ddots & \vdots \\
a_{n1} & \cdots & a_{nm}
\end{bmatrix},
\quad
\mathbf{D} =
\begin{bmatrix}
d_{11} & \cdots & d_{1m} \\
\vdots & \ddots & \vdots \\
d_{m1} & \cdots & d_{mm}
\end{bmatrix}.
$$

**Note:**
- $\mathbf{D}$ is assumed symmetric and negative definite, meaning $z$ is strictly concave.
- The constraints are linear, guaranteeing a convex solution space.

---

### Problem Formulation with Slack Variables

The problem can be written as:
Maximize $z = \mathbf{C}^T \mathbf{X} + \frac{1}{2} \mathbf{X}^T \mathbf{D} \mathbf{X}$

Subject to:
$$
\mathbf{G} \mathbf{X} =
\begin{bmatrix}
\mathbf{A} \\
-\mathbf{I} \\
\end{bmatrix}
\mathbf{X} -
\begin{bmatrix}
\mathbf{b} \\
0 \\
\end{bmatrix}
\leq 0,
$$
$$
\mathbf{X} \geq 0.
$$

Lagrange multipliers:
$$
\lambda = [\lambda_1, \lambda_2, ..., \lambda_m]^T,
\quad
\mu = [\mu_1, \mu_2, ..., \mu_n]^T,
$$
corresponding to constraints $\mathbf{A} \mathbf{X} - \mathbf{b} \leq 0$ and $-\mathbf{X} \leq 0$, respectively.

Applying KKT conditions:
$$
\lambda_i \geq 0, \quad \mu_j \geq 0,
$$
$$
\nabla z - \lambda^T \nabla g(\mathbf{X}) = 0,
$$
where $\nabla g(\mathbf{X})$ is the gradient of the constraints.

For slack variables $s$:
$$
\lambda_i s_i = 0, \quad i = 1, 2, ..., m.
$$

Define slack variables $S = b - A\mathbf{X} \geq 0$.

The conditions reduce to:
$$
-2\mathbf{D}\mathbf{X} + \lambda^T \mathbf{A}^T - \mu^T = \mathbf{C},
$$
$$
A\mathbf{X} + S = \mathbf{b}, \quad \mu^T \mathbf{X} = 0,
$$

with $\lambda, \mu, S, X \geq 0$.

Since $\mathbf{D}$ is symmetric:
$$
-2D\mathbf{X}^T + \mathbf{A}^T \lambda - \mu = \mathbf{C}^T.
$$

Thus, the necessary conditions can be combined as:

$$
\begin{bmatrix}
-\mathbf{2D} & \mathbf{A}^T \\
\mathbf{A} & -\mathbf{I}
\end{bmatrix}
\begin{bmatrix}
\mathbf{X} \\
\lambda
\end{bmatrix}
=
\begin{bmatrix}
\mathbf{C} \\
\mu^T \\
0 \\
\mathbf{b} - S
\end{bmatrix},
$$

with $\lambda, \mu, S, X \geq 0$.

The solution is obtained using **Phase I of the two-phase method**.

---

### Example

Consider:
Maximize $z = 4x_1 + 6x_2 - 2x_1^2 - 2x_1 x_2 - 2x_2^2$

Subject to:
$$
x_1 + 2x_2 \leq 2,
$$
$$
x_1, x_2 \geq 0.
$$

Matrix form:
Maximize $z = [4, 6]^T \mathbf{X} + \frac{1}{2} \mathbf{X}^T \mathbf{D} \mathbf{X}$

Where:
$$
\mathbf{A} =
\begin{bmatrix}
1 & 2 \\
\end{bmatrix},
\quad
\mathbf{b} = [2],
$$
$$
\mathbf{D} =
\begin{bmatrix}
-2 & -1 \\
-1 & -2 \\
\end{bmatrix}.
$$

KKT conditions matrix setup:

$$
\begin{bmatrix}
4 & 6 & \lambda_1 & \mu_1 & s_1 \\
2 & 4 & 0 & 0 & 0 \\
-1 & -2 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
\end{bmatrix}
$$

Initial tableau (Phase I) with artificial variables $R_1, R_2$:

Iteration 1:
- Entering variable: $x_1$, $\mu_1 = 0$.

Iteration 2:
- Entering variable: $x_2$, $\mu_2 = 0$.

Iteration 3:
- Multiplier $\lambda_1$ becomes basic because $s_1 = 0$.

Optimal feasible solution:
$$
\mathbf{X} = \begin{bmatrix}
\frac{5}{3}, \\
\frac{6}{3}
\end{bmatrix},
$$
with $z = 4.16$.

---

## Linear Combinations Method

This method addresses the problem where all constraints are linear:

Maximize $z = f(\mathbf{X})$

**Subject to:**
$$
\mathbf{A} \mathbf{X} \leq \mathbf{b}, \\
\mathbf{X} \geq 0.
$$

The procedure is based on the steepest-ascent (gradient) method.

### Notes:
- The direction given by the gradient vector may not yield a feasible solution for constrained problems.
- The gradient will not be zero at the optimum point in constrained cases, so modifications are needed.

---

### Method Steps

Let $\mathbf{X}^k$ be the feasible trial point at iteration $k$. Expand $f(\mathbf{X})$ around $\mathbf{X}^k$ using Taylor’s series:

$$
f(\mathbf{X}) \approx f(\mathbf{X}^k) + \nabla f(\mathbf{X}^k)^T (\mathbf{X} - \mathbf{X}^k).
$$

Determine a feasible point $\mathbf{X}^* = \mathbf{X}^k^*$ such that $f(\mathbf{X})$ is maximized under linear constraints.

The problem reduces to solving:
Maximize $w^k^T \mathbf{X} = \nabla f(\mathbf{X}^k)^T \mathbf{X}$

**Subject to:**
$$
\mathbf{A} \mathbf{X} \leq \mathbf{b}, \\
\mathbf{X} \geq 0.
$$

If $w^k^T \mathbf{X}^* > w^k^T \mathbf{X}^k$, then:
$$
f(\mathbf{X}^*) > f(\mathbf{X}^k) \quad \text{only if } \mathbf{X}^* \text{ is near } \mathbf{X}^k,
$$
but there exists a point $\mathbf{X}^{k#}$ on the line segment between $\mathbf{X}^k$ and $\mathbf{X}^*$ such that:
$$
f(\mathbf{X}^{k#}) > f(\mathbf{X}^k).
$$

Define:
$$
\mathbf{X}^{k#} = (1 - r) \mathbf{X}^k + r \mathbf{X}^*,
$$
where $0 < r \leq 1$.

Maximize the function of $r$:
$$
h(r) = f((1-r)\mathbf{X}^k + r\mathbf{X}^*).
$$

Repeat until $w^k^T \mathbf{X}^* \leq w^k^T \mathbf{X}^k$, terminating with $\mathbf{X}^k$ as the best solution.

---

### Example

Maximize:
$$
