# Week 11 — Nonlinear Programming Algorithms II (Quadratic Programming + Linear Combinations)

## What you should be able to do after this week
- Recognize a quadratic programming (QP) model and its matrix form.
- State the KKT conditions specialized to QP (stationarity + feasibility + complementary slackness).
- Explain how (in the lecture) QP conditions are converted into a system that can be handled with a simplex-like Phase I approach.
- Explain the linear combinations method (successive linearization / solve LP subproblem + line search).

## Key ideas (intuition first)
- QP is “LP + curvature”: quadratic objective with linear constraints.
- If the quadratic form is concave for a maximization problem (negative definite $D$), the problem is well-behaved (single peak).
- For nonlinear objective + linear constraints, iteratively maximizing the linearized objective (gradient) is a practical strategy.

## Core theory and definitions

### Quadratic programming model (as stated in the lecture)
Maximize:
$$
z = C^T X + \frac{1}{2} X^T D X
$$
Subject to:
$$
AX \le b,\quad X \ge 0.
$$
Lecture assumption:
- $D$ is symmetric and negative definite $\Rightarrow$ objective is strictly concave (good for maximization).

### KKT conditions (QP perspective)
The lecture sets up multipliers for:
- Inequality constraints $AX \le b$ (multipliers $\lambda \ge 0$)
- Nonnegativity $-X \le 0$ (multipliers $\mu \ge 0$)

Complementary slackness forms shown:
- $\lambda_i s_i = 0$ for slack variables $s = b - AX \ge 0$
- $\mu_j x_j = 0$

### Linear combinations method (lecture description)
At iteration $k$ with feasible $X^k$, linearize:
$$
f(X) \approx f(X^k) + \nabla f(X^k)^T (X - X^k).
$$
Then solve the LP:
$$
\max \; w^k{}^T X \quad \text{where } w^k = \nabla f(X^k),
$$
subject to the original linear constraints.

If the LP solution $X^*$ improves the linearized objective beyond $X^k$, do a line search on the segment:
$$
X^{k+1} = (1-r)X^k + rX^*,
$$
choosing $r\in(0,1]$ to maximize $h(r)=f((1-r)X^k + rX^*)$.

## Methods / Algorithms

### QP solving workflow (from the lecture narrative)
1. Express the QP in matrix form ($C, D, A, b$).
2. Write KKT conditions (stationarity + primal/dual feasibility + complementarity).
3. Introduce slack variables and (if needed) artificial variables to find a feasible start.
4. Use a Phase I simplex-style process to satisfy feasibility, then optimize.

### Linear combinations method (practical steps)
1. Start from a feasible $X^0$.
2. Compute gradient $w^k = \nabla f(X^k)$.
3. Solve LP: maximize $w^k{}^T X$ subject to linear constraints.
4. If no improvement, stop.
5. Otherwise, line search on the segment from $X^k$ to $X^*$ and update.

## Worked examples

### Example A — QP via KKT + simplex-like iterations (Lab 11)
[Lab11.md](src/Lab11.md) includes two QP-style problems and shows:
- how to form $C$, $D$, $A$, $b$,
- how KKT conditions are written in an expanded tableau-like format,
- and how a Phase I procedure eliminates artificial variables.

Reported solutions include:
- Problem 1: $x_1^* = 1, x_2^* = 1$ (with reported slacks $s_1=5, s_2=11$ and multipliers 0).
- Problem 2: $x_1^* = 4/5, x_2^* = 6/5$ with a reported $\lambda_1 = 14/15$.

**Not found in provided materials:** [Lab11.md](src/Lab11.md) is cut off at the start of Problem 3 (“Gradient Descent with $\epsilon=0.01$”).

### Example B — Lecture 11 caution
The lecture’s QP worked example includes numeric tables/iterations, but some intermediate values appear inconsistent after conversion.
Treat the example primarily as a *template for the KKT-to-Phase-I setup* rather than as a clean numeric reference.

## Common mistakes & how to avoid them
- Confusing max vs min sign conventions when writing stationarity conditions for QP.
- Forgetting the nonnegativity multipliers $\mu$ and conditions $\mu_j x_j = 0$.
- Assuming $\nabla f=0$ at a constrained optimum (generally false; constraints supply the missing balance).
- In linear combinations method: taking the full step $r=1$ without line search (may reduce $f$ because the linearization is local).
- Ignoring definiteness/convexity assumptions that justify global optimality claims.

## Quick recap
- QP: quadratic objective + linear constraints; KKT is the core theory.
- Linear combinations method: iteratively solve LPs based on the gradient and move via line search.

## Exam prep

### Likely questions
- Write a QP in matrix form ($C, D, A, b$).
- Write KKT conditions and identify which constraints are active via complementary slackness.
- Explain how a Phase I approach finds feasibility when KKT introduces extra variables.
- Do one iteration of the linear combinations method (gradient → LP → line search).

### Checklist
- I can write QP KKT conditions clearly (including complementarity).
- I can explain why negative definite $D$ makes maximization “nice”.
- I can outline the linear combinations method and its stopping condition.

## Sources used
- [F25 - Intro to Opt -Lecture_11 - Nonlinear Programming (2).md](src/F25%20-%20Intro%20to%20Opt%20-Lecture_11%20-%20Nonlinear%20Programming%20%282%29.md)
- [Lab11.md](src/Lab11.md) (note: truncated near the end)

