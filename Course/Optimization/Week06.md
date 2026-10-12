# Week 6 — Interior‑Point Methods (Projected Gradient + Centering)

## What you should be able to do after this week
- Explain the core idea of interior-point methods vs simplex (interior path vs edge-walking).
- Describe the “projected gradient + centering/scaling” approach shown in the lecture.
- Write the projection matrix form used to keep moves feasible for equality constraints.
- Explain why the method needs a strictly interior starting point (all variables $>0$).
- Follow the logic of one iteration: scale → project → step size → unscale.

## Key ideas (intuition first)
- Simplex moves along the boundary; interior-point methods try to move **through the interior**.
- A naive gradient step usually breaks feasibility; projection keeps you on (or near) the constraint manifold.
- Centering/scaling tries to keep the current point away from boundaries so you can take meaningful steps.

## Core theory and definitions

### Interior-point “concepts” stated in the lecture
1. Move through the feasible region interior toward optimum.
2. Move in the direction that improves the objective fastest (gradient idea).
3. Transform/scale so the current point is near the “center” of the feasible region.

### Equality-form setup
The lecture rewrites inequalities using slack variables so feasibility is expressed as:
$$
Ax = b,\quad x \ge 0.
$$
To stay “interior”, we want $x>0$ (strictly).

### Projected gradient (lecture formula)
Projection matrix for equality constraints:
$$
P = I - A^T (A A^T)^{-1} A.
$$
Projected direction:
$$
c_p = Pc.
$$

## Methods / Algorithms

### One iteration (as described across the lecture material)
Given a strictly positive trial solution $x$:
1. Build diagonal scaling matrix $D = \mathrm{diag}(x)$.
2. Transform (work in scaled variables):
   - $A_{\tilde{w}} = A D^{-1}$
   - $c'_p = D^{-1} c$
3. Compute projection matrix (in transformed space) and projected gradient $c_p$.
4. Choose step size parameter $\alpha \in (0,1)$ (the examples use $\alpha = 0.5$).
5. Identify the most restrictive (most negative) component magnitude $\nu$ and update the trial point in scaled coordinates using:
   $$
   x_{\tilde{w}} = 1 + \frac{c_p}{\nu}.
   $$
6. Transform back: $x \leftarrow D x_{\tilde{w}}$.
7. Stop when the iterate changes very little (“virtually unchanged” in the notes).

## Worked examples

### Example A — Lecture example (structure)
Maximize $z = x_1 + 2x_2$ subject to $x_1 + x_2 \le 8$, $x \ge 0$.
The lecture:
- Starts from an interior point and adds a slack variable to get equality form.
- Shows why moving directly along $\nabla z$ breaks feasibility.
- Uses projection onto the constraint plane and a scaling step so the current trial point becomes $(1,1,1)$ in transformed coordinates.

### Example B — Lab interior-point iterations to a simplex optimum (numerical sequence)
[Lab06.md](src/Lab06.md) Problem 1 applies an interior-point style iteration and reports convergence to:
- $(x_1,x_2) \approx (6,1)$ with objective $F=7$
and shows intermediate iterates moving toward that corner.

### Example C — Notes quality watch-out (be skeptical)
Across [F25 - Intro to Opt -Lecture_6 - - An Interior-point Algorithm.md](src/F25%20-%20Intro%20to%20Opt%20-Lecture_6%20-%20-%20An%20Interior-point%20Algorithm.md) and [Lab06.md](src/Lab06.md), some matrices/vectors are visibly misaligned or contain typos (e.g., inconsistent dimensions in intermediate expressions).
When practicing, treat the *algorithmic structure* (scale → project → step → unscale) as the reliable takeaway, and re-derive dimensions if you compute by hand.

## Common mistakes & how to avoid them
- Starting on the boundary (some $x_i = 0$) makes $D^{-1}$ impossible; you need a strictly positive start.
- Forgetting to add slack variables (you need equality form to use the projection formula as written).
- Using $\alpha$ too large and stepping outside $x \ge 0$.
- Mixing up the roles of $A$, $c$, $D$, and “transformed” versions $A_{\tilde{w}}$, $c'_p$.

## Quick recap
- Interior-point methods can approach the optimum without walking edges.
- Projection keeps feasibility; scaling/centering keeps the iterate away from boundaries.
- The provided examples aim to show how the mechanics work rather than be perfectly clean numerically.

## Exam prep

### Likely questions
- Explain the difference between simplex and interior-point approaches.
- Write down the projection matrix $P$ used for equality constraints.
- Outline one iteration step-by-step (including why scaling is used).
- Explain why strict positivity is required in this formulation.

### Checklist
- I can explain the three interior-point “concepts” from the lecture.
- I can write and interpret $P = I - A^T(AA^T)^{-1}A$.
- I can explain the purpose of scaling $D$ and how it changes the problem.

## Sources used
- [F25 - Intro to Opt -Lecture_6 - - An Interior-point Algorithm.md](src/F25%20-%20Intro%20to%20Opt%20-Lecture_6%20-%20-%20An%20Interior-point%20Algorithm.md)
- [Lab06.md](src/Lab06.md)

