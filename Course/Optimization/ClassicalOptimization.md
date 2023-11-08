# Classical Optimization

## TOC

- [Classical Optimization](#classical-optimization)
  - [TOC](#toc)
  - [Lecture Topics](#lecture-topics)

## Lecture Topics

- Unconstrained Problems
- Constrained Problems
  - Sensitivity analysis in the Jacobian method
  - Equality constraints ― Lagrangian Method
  - Inequality constraints ― Karush-Kuhn-Tucker (KKT)

## ChatGPT 4 Explanation

Classical optimization is a vast field in mathematics and computer science that deals with finding the best solution from all feasible solutions. Here's a brief overview of the topics you've listed:

### Unconstrained Problems

Unconstrained optimization problems are those where the objective function needs to be optimized (either maximized or minimized) without any restrictions or constraints on the variables. The general form of an unconstrained optimization problem can be expressed as:

$$
\text{minimize (or maximize) } f(\mathbf{x})
$$

where $f(\mathbf{x})$ is the objective function and $\mathbf{x}$ represents the vector of variables. Classical methods for solving such problems include gradient descent, Newton's method, and the quasi-Newton methods such as the BFGS and the L-BFGS algorithms.

### Constrained Problems

Constrained optimization problems involve an objective function that needs to be optimized subject to a set of constraints. These constraints can be equalities, inequalities, or both.

#### Sensitivity Analysis in the Jacobian Method

The Jacobian method is a way of solving systems of equations, which is often a part of solving constrained optimization problems with equality constraints. Sensitivity analysis in this context refers to studying how the solution of the optimization problem changes with changes in the parameters of the problem. It can help in understanding the robustness of the solution and in identifying critical parameters that have a significant impact on the outcome.

#### Equality Constraints — Lagrangian Method

When dealing with equality constraints, the Lagrangian method (or Lagrange multipliers) is a strategy for finding the local maxima and minima of a function subject to equality constraints. For a problem of the form:

$$
\text{minimize (or maximize) } f(\mathbf{x})\\
\text{subject to } g_i(\mathbf{x}) = 0 \text{ for } i = 1, ..., m
$$

where $g_i(\mathbf{x})$ are the constraint functions, the Lagrangian $\mathcal{L}$ is formed as:

$$
\mathcal{L}(\mathbf{x}, \boldsymbol{\lambda}) = f(\mathbf{x}) + \sum_{i=1}^{m} \lambda_i g_i(\mathbf{x})
$$

where $\boldsymbol{\lambda}$ are the Lagrange multipliers. The solutions are found by solving the system of equations derived from setting the partial derivatives of the Lagrangian with respect to $\mathbf{x}$ and $\boldsymbol{\lambda}$ to zero.

#### Inequality Constraints — Karush-Kuhn-Tucker (KKT) Conditions

When the constraints include inequalities, the Karush-Kuhn-Tucker (KKT) conditions extend the idea of Lagrange multipliers. For a problem with both equality and inequality constraints:

$$
\text{minimize (or maximize) } f(\mathbf{x})\\
\text{subject to } g_i(\mathbf{x}) \leq 0 \text{ for } i = 1, ..., m\\
h_j(\mathbf{x}) = 0 \text{ for } j = 1, ..., p
$$

The KKT conditions introduce both Lagrange multipliers for the equality constraints and what are called KKT multipliers for the inequality constraints. The KKT conditions are necessary conditions for a solution to be optimal, and under certain conditions, they are also sufficient.

The KKT conditions include:

- Stationarity
- Primal feasibility
- Dual feasibility
- Complementary slackness

These conditions together help in finding the optimal solutions to the constrained optimization problem.

In summary, classical optimization provides a set of tools and methods to solve problems where one seeks to find the best possible decision within a defined set of possible decisions. The methods vary depending on the presence and type of constraints involved.

[<kbd><br><- Return<br></kbd>](Optimization.md)
