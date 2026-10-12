# Lecture 9: Classical Optimization Theory (2)
**Dr. Mohammad Reza Bahrami**
*Innopolis University*
*Course of Optimization*
*Fall 2025*

---

## Course Information
Materials are taken from different sources with modifications. I do not claim any authorship of these materials.

---

# Lecture 9: Classical Optimization (2)

---

## Content

- [x] Constrained Problems
- [x] Sensitivity analysis in the Jacobian method
- [x] Equality constraints – Lagrangian Method
- [x] Inequality constraints – Karush-Kuhn-Tucker (KKT)

---

# Constrained Problems

---

# Sensitivity Analysis in the Jacobian Method

## Introduction
The Jacobian method is used to study how small changes in constraint right-hand sides affect the optimal value of $f$. Specifically, it examines the effect of changing $g_i(X) = 0$ to $g_i(X) + \Delta g_i$ on the optimal value of $f$.

This type of investigation is called **sensitivity analysis** and is similar to that in linear programming. However, sensitivity analysis in nonlinear programming holds only in a small neighborhood around an extreme point.

The equations for partial derivatives are given by:

$$
\frac{\partial f}{\partial Y, Z} = \frac{\partial^2 f}{\partial Y^2} + \frac{\partial^2 f}{\partial Z^2}
$$

$$
\frac{\partial g_i}{\partial X} = J_{i1} + C_{iZ}
$$

Given $\Delta g_i \neq 0$, the substitution yields:

$$
\Delta f = \left( \frac{\partial f}{\partial Y} \right)_0^{T} \left( \frac{\partial g_i}{\partial X} \right)^{-1} \Delta g_i + \text{terms involving } \frac{\partial^2 f}{\partial Z^2}
$$

Where:

$$
\frac{\partial Y}{\partial g_i} = J_{iY}^{-1} \left( \frac{\partial g_i}{\partial X} - C_{iZ} \right)
$$

$$
\frac{\Delta f}{\Delta g_i} = \left( \frac{\partial^2 f}{\partial Z^2} \right)_0^{T} \left( \frac{\partial Y}{\partial g_i} \right) + \nabla_{\lambda}^T \left( \frac{\partial f}{\partial X} \right)
$$

$$
\nabla_{\lambda} f = \frac{\partial f}{\partial Z} - \frac{\partial^2 f}{\partial Y^2} J_{iY}^{-1} C_{iZ}
$$

At an extreme (stationary) point $X^* = (Y^*, Z^*)$, the constrained gradient $\nabla_{\lambda} f$ must vanish:

$$
\frac{\Delta f}{Y_0, Z_0} = \left( \frac{\partial Y}{\partial g_i} \right)_0^{T} \left( \frac{\partial g_i}{\partial X} \right)
$$

The effect of small changes $\Delta g_i$ on the optimum value $f$ can be studied by evaluating:

$$
\frac{\Delta f}{\Delta g_i} = \left( \frac{\partial^2 f}{\partial Y^2} \right)_0^{T} J_{iY}^{-1}
$$

---

## Example

Consider the following problem:

- Objective:
  $$
  f(X) = x_1^* + x_2^* + x_3^*
 
$$

- Constraints:
  $$
  g_1(X) = x_1^* + x_2^* + 3x_3^* - 2 = 0
 
$$
  $$
  g_2(X) = 5x_1^* + 2x_2^* + x_3^* - 5 = 0
 
$$

Given $Y^0 = (x_1^*, x_2^*)$, the solution is approximately:

$$
X^* \approx (0.81, 0.28)
$$

The sensitivity coefficients are derived as follows:

$$
\frac{\partial f}{\partial x_1^*} = 2x_1^*
$$
$$
\frac{\partial f}{\partial x_2^*} = 2x_2^* \approx (1.62, 0.70)
$$

Consequently,

$$
\left( \frac{\Delta f}{\Delta g_1}, \frac{\Delta f}{\Delta g_2} \right) = \left[ \begin{array}{cc}
-3 & -5 \\
1 & -3
\end{array} \right]^{-1} \left[ \begin{array}{c}
\Delta g_1 \\
\Delta g_2
\end{array} \right]
$$

$$
= (0.0876, 0.3067)
$$

This implies:
- For $\Delta g_1 = 1$, $f$ increases by approximately **0.0876**.
- For $\Delta g_2 = 1$, $f$ increases by approximately **0.3067**.

---

# Equality Constraints – Lagrangian Method

## Introduction
In the Jacobian method, the sensitivity coefficients $\lambda$ are defined as:

$$
\lambda = \frac{\partial f}{\partial g_i}
$$

The equation $\Delta f - \lambda \Delta g_i = 0$ satisfies necessary conditions for stationary points because $\nabla_{\lambda} f = 0$.

---

## Formulation of Lagrangian Equations

Taking partial derivatives with respect to all $x_j$, we get:

$$
\frac{\partial}{\partial x_j} (f - \lambda g) = 0, \quad j=1,2,...,n
$$

These equations, combined with the constraint equations $g_i(X) = 0$, yield feasible values of $X$ and $\lambda$.

The Lagrangian function is defined as:

$$
L(X, \lambda) = f(X) - \lambda^T g(X)
$$

The necessary conditions for stationary points are given by:

$$
\frac{\partial L}{\partial X} = 0, \quad \frac{\partial L}{\partial \lambda} = 0
$$

---

## Example

Consider the problem:

- Objective:
  $$
  f(X) = x_1^* + x_2^* + x_3^*
 
$$

- Constraints:
  $$
  g_1(X) = x_1^* + x_2^* + 3x_3^* - 2 = 0
 
$$
  $$
  g_2(X) = 2x_1^* + 2x_2^* + x_3^* - 5 = 0
 
$$

The Lagrangian function is:

$$
L(X, \lambda) = x_1^* + x_2^* + x_3^* - \lambda_1 (x_1^* + x_2^* + 3x_3^* - 2) - \lambda_2 (2x_1^* + 2x_2^* + x_3^* - 5)
$$

The necessary conditions are:

$$
\frac{\partial L}{\partial x_1^*} = 2x_1^* - \lambda_1 - 2\lambda_2 = 0
$$
$$
\frac{\partial L}{\partial x_2^*} = 2x_2^* - \lambda_1 - 2\lambda_2 = 0
$$
$$
\frac{\partial L}{\partial x_3^*} = 2x_3^* - 3\lambda_1 - \lambda_2 = 0
$$

And the constraint equations:

$$
\frac{\partial L}{\partial \lambda_1} = -(x_1^* + x_2^* + 3x_3^* - 2) = 0
$$
$$
\frac{\partial L}{\partial \lambda_2} = -(2x_1^* + 2x_2^* + x_3^* - 5) = 0
$$

The solution yields:

$$
X^* = (0.8043, 0.3478, 0.2826)
$$
$$
\lambda = (\lambda_1, \lambda_2) = (0.0870, 0.3043)
$$

These Lagrange multipliers match the sensitivity coefficients from the Jacobian method example.

---

# Inequality Constraints – Karush-Kuhn-Tucker (KKT) Conditions

## Introduction
This section extends the Lagrangian method to problems with inequality constraints:

Maximize $z = f(X)$

Subject to:
$$
g_i(X) \leq 0
$$

Inequality constraints can be converted into equality constraints using nonnegative slack variables.

---

## Slack Variables and KKT Conditions

Let $S_i^* \geq 0$ be the slack variable added to each constraint $g_i(X) \leq 0$. Define:

$$
S = (S_1^*, S_2^*, ..., S_m^*)
$$

The Lagrangian function becomes:

$$
L(X, S, \lambda) = f(X) - \lambda^T g(X) + S^T
$$

For optimality in maximization problems, $\lambda$ must satisfy:
- If $g_i(X) < 0$, then $\lambda_i > 0$.
- If $g_i(X) = 0$, then

Here is the cleaned Markdown version of your PDF text:

### Conditions
These conditions reduce to:
1. $\lambda_% \leq 0$
   $\lambda_* \leq 0$
   $\lambda_+ \leq 0$
   $\lambda_4 \leq 0$
   $\lambda_5 \leq 0$

2.
   $2x_% - 2\lambda_% - \lambda_* + \lambda_+ = 0$

3.
   $2x_* - \lambda_% + \lambda_4 = 0$

4.
   $2x_+ - \lambda_* + \lambda_5 = 0$

5.
   $\lambda_% (2x_% + x_*) - 5 = 0$

6.
   $\lambda_* (x_% + x_+) - 2 = 0$

7.
   $\lambda_+ (1) - x_% = 0$

8.
   $\lambda_4 (2) - x_* = 0$

9.
   $\lambda_5 x_+ = 0$

### Inequalities
- $2x_% + x_* \leq 5$
- $x_% + x_+ \leq 2$
- $x_% \geq 1$
- $x_* \geq 2$
- $x_+ \geq 0$

### Solution
The solution is:
$x_% = 1$, $x_* = 2$, $x_+ = 0$,
$\lambda_% = \lambda_* = \lambda_5 = 0$,
$\lambda_+ = -2$, $\lambda_4 = -4$.

---

Because both the function $f(X)$ and the solution space $g(X) \leq 0$ are convex, the Lagrangian $L_{X,S,\lambda}$ must be convex, and the resulting stationary point yields a global constrained minimum.

---
**Dr. Mohammad Reza Bahrami**
**Course:** Introduction to Optimization
**Lecture:** Classical Optimization (2)
**Date:** 24
```
