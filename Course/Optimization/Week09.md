# Week 9 — Classical Optimization II (Lagrangian, KKT, Sensitivity)

## What you should be able to do after this week
- Set up and solve equality-constrained problems using the Lagrangian method.
- Interpret Lagrange multipliers as sensitivity coefficients (local “shadow prices”).
- Write the Karush–Kuhn–Tucker (KKT) conditions for inequality-constrained problems.
- Use second-order/sufficiency ideas mentioned in the materials (bordered Hessian, convexity/concavity checks).
- Explain why sensitivity analysis in nonlinear programming is local (valid near a stationary point).

## Key ideas (intuition first)
- Constraints “push back” on the objective: multipliers quantify that push.
- KKT is the nonlinear analogue of “optimality conditions” from LP duality.
- In convex settings, KKT conditions are powerful: stationary points are globally optimal.

## Core theory and definitions

### Sensitivity analysis (Jacobian method)
Lecture 9 discusses how small changes $\Delta g_i$ in equality constraints affect the optimal objective value $\Delta f$.
Practical takeaway emphasized in the notes:
- This is valid only in a small neighborhood around the stationary point (nonlinear behavior can change quickly).

### Lagrangian method (equality constraints)
For:
$$
\min f(X)\quad \text{s.t.}\quad g(X)=0,
$$
define:
$$
L(X,\lambda) = f(X) - \lambda^T g(X).
$$
Necessary conditions:
- Stationarity: $\frac{\partial L}{\partial X} = 0$
- Feasibility: $\frac{\partial L}{\partial \lambda} = -g(X)=0$

Lecture 9 also connects $\lambda$ to sensitivity coefficients.

### KKT conditions (inequality constraints)
For a problem with inequalities (as introduced in Lecture 9), KKT conditions include:
- Primal feasibility: $g_i(X^*) \le 0$
- Dual feasibility: multipliers satisfy sign constraints (lecture text is partially truncated, but the standard form used in the course is consistent with $\lambda_i \ge 0$ for $\le$-type constraints in minimization settings; for maximization the sign convention must match the chosen Lagrangian)
- Stationarity: gradient balance between objective and active constraints
- Complementary slackness: multiplier $\times$ slack is 0 (active constraints have nonzero multipliers; inactive constraints have zero multipliers)

**Not found in provided materials:** the KKT section in [F25 - Intro to Opt -Lecture_9- Classical Optimization (2).md](src/F25%20-%20Intro%20to%20Opt%20-Lecture_9-%20Classical%20Optimization%20%282%29.md) is cut off mid-sentence; later a separate block of “conditions/solution” appears without full setup. Use it mainly as a template for the condition types.

## Methods / Algorithms

### Solving equality-constrained problems via Lagrange multipliers
1. Write $L(X,\lambda)$.
2. Compute partial derivatives w.r.t. all $x_j$ and $\lambda_i$.
3. Solve the resulting system of equations.
4. Check sufficiency via bordered Hessian or convexity (if applicable).

### Active-set thinking for KKT (how to reason)
At optimum:
- Some constraints are **active** ($g_i(X^*)=0$) and act like equalities.
- Others are **inactive** ($g_i(X^*)<0$) with zero multipliers (by complementary slackness).

## Worked examples

### Example A — Lagrangian method with two equalities (Lab 9)
[Lab09.md](src/Lab09.md) Problem 1 sets up:
- $L(x_1,x_2,x_3,\lambda_1,\lambda_2)$,
- solves the stationarity + feasibility equations,
- and then checks sufficiency via bordered Hessian or convexity.

The lab provides a fully worked solution vector for $(x_1,x_2,x_3,\lambda_1,\lambda_2)$.

### Example B — Multipliers as sensitivities (Lecture 9)
Lecture 9 includes an example where the Lagrange multipliers match sensitivity coefficients (numbers reported around $(0.087, 0.304)$).
Interpretation: small increases in the constraint RHSs change the optimal objective approximately by these rates.

### Example C — KKT solution snippet (lecture)
The lecture contains a “conditions + solution” block that concludes a particular inequality-constrained example with a specific $x$ and $\lambda$ assignment.
Because the problem statement is incomplete in the provided file, treat this as:
- a checklist of KKT condition types (stationarity, inequalities, complementary slackness),
not as a fully reproducible worked example.

## Common mistakes & how to avoid them
- Wrong sign convention in the Lagrangian (especially between max vs min).
- Forgetting complementary slackness (it’s what links “active constraints” to nonzero multipliers).
- Solving stationarity equations but forgetting to enforce feasibility.
- Applying sensitivity conclusions far away from the stationary point.
- Using a bordered Hessian test without keeping track of the $(-1)^m$ sign factor mentioned in the lab.

## Quick recap
- Lagrangian method handles equalities by adding multipliers and solving stationarity + feasibility.
- KKT extends this to inequalities with multiplier sign rules and complementary slackness.
- Sensitivity analysis in nonlinear programming is local.

## Exam prep

### Likely questions
- Build and solve a Lagrangian system for a small equality-constrained problem.
- Interpret multipliers as sensitivity coefficients.
- Write KKT conditions for a given inequality-constrained problem and identify active constraints.
- Explain why convexity/concavity makes KKT solutions globally optimal.

### Checklist
- I can form $L(X,\lambda)$ and derive the necessary equations.
- I can write KKT conditions and explain each part.
- I can reason about which constraints should be active/inactive.

## Sources used
- [F25 - Intro to Opt -Lecture_9- Classical Optimization (2).md](src/F25%20-%20Intro%20to%20Opt%20-Lecture_9-%20Classical%20Optimization%20%282%29.md)
- [Lab09.md](src/Lab09.md) (note: truncated near the end)

