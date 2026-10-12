# Week 5 — Duality and Advanced Linear Programming

## What you should be able to do after this week
- Construct a dual LP from a primal LP using the lecture’s “equation form” rules.
- Explain weak/strong duality as stated in the notes (feasible primal/dual objective inequality; equality at optimum).
- Interpret dual variables as “values” associated with constraints (shadow-price idea).
- Explain how dual solutions can be extracted from simplex information (tableau/inverse viewpoint in the notes).
- Explain advanced LP viewpoints: extreme points, basic solutions, basis matrix $B$, reduced costs.
- Describe what the revised simplex method changes (matrix computations instead of full tableau).
- Describe how bounded-variable constraints can be handled conceptually.

## Key ideas (intuition first)
- Every LP has a “mirror” problem (dual) that puts values on constraints.
- Duality is both a mathematical theorem and a practical tool (bounds, sensitivity, computational choices).
- “Advanced” simplex is mostly about linear algebra: $B^{-1}$, reduced costs, and efficient updates.

## Core theory and definitions

### Dual construction (as summarized in the lecture)
For a primal written in equation form with nonnegative RHS and nonnegative variables, the lecture’s recipe is:
1. One dual variable per primal constraint.
2. One dual constraint per primal variable.
3. Primal RHS becomes dual objective coefficients.
4. Primal objective coefficients become dual RHS.
5. Constraint matrix is transposed into the dual.

The examples in the lecture also illustrate:
- Equality constraints lead to dual variables that are “unrestricted” (shown via the $y_2$ discussion).

### Primal–dual relationships (duality theorems in words)
The notes state:
- For any feasible pair (primal max, dual min):
  $$
  z \le w
  $$
- At optimality:
  $$
  z^* = w^*.
  $$

These are the key ideas behind:
- Bounding: any dual feasible point provides an upper bound on any primal feasible objective (for max vs min pairing).
- Optimality check: if you find feasible solutions with equal objective values, they are optimal.

## Methods / Algorithms

### Getting dual values from simplex information (lecture idea)
Two approaches are mentioned:
- Read dual values from tableau relationships tied to the original objective coefficients.
- Compute using the “optimal inverse” $B^{-1}$ (multiply objective coefficients by inverse information).

### Advanced LP building blocks (from the advanced LP lecture)
Key linear-algebra objects:
- Basis matrix $B$: selected columns of $A$ (linearly independent).
- Basic solution: $X_B = B^{-1} b$ with nonbasic variables set to 0.
- Reduced costs (for maximization, in the lecture’s notation):
  $$
  z_j - c_j = C_B B^{-1} P_j - c_j.
  $$

### Revised simplex (conceptual steps)
The lecture lists the core loop:
1. Start with a feasible basis $B$ and $C_B$.
2. Compute $B^{-1}$.
3. Compute reduced costs $z_j - c_j$ for nonbasic variables.
4. Choose entering variable by reduced cost sign.
5. Compute direction $B^{-1} P_j$ and apply the ratio test to pick leaving variable.
6. Update the basis (without carrying the full tableau).

**Not found in provided materials:** the revised simplex “Step 3” line in the lecture is cut off, and the later worked example has missing pieces (e.g., incomplete $Z_{B2}$ vector).

### Bounded-variables algorithm (0 ≤ x ≤ U, x ≥ L)
From the lecture:
- For lower bounds $X \ge L$: substitute $X = L + X'$, $X' \ge 0$.
- For upper bounds $X \le U$: treat bounds via modified feasibility calculations, comparing:
  - $\theta_1$ from nonnegativity constraints,
  - $\theta_2$ from upper-bound hits of basic variables,
  - $u_j$ (upper bound of the entering variable).

## Worked examples

### Example A — Primal ↔ dual conversion (lecture example)
Primal (max):
$$
z = 5x_1 + 12x_2 + 4x_3
$$
with one $\le$ constraint and one $=$ constraint (see the lecture file).

Dual (min) as written in the notes:
$$
w = 10y_1 + 8y_2
$$
with constraint directions and sign restrictions shown (including the “unrestricted” dual variable for the equality constraint).

### Example B — Duality numerics via a graphical problem (lab)
From [Lab05.md](src/Lab05.md) Problem 1:
- Primal optimum: $(x_1,x_2)=(2,6)$, objective $46$.
- Dual optimum: $(y_1,y_2)=(1,4)$, objective $46$.
This is a direct illustration of $z^*=w^*$.

### Example C — Advanced simplex result (lab)
[Lab05.md](src/Lab05.md) reports for the 3-variable LP:
- Optimal solution $(x_1,x_2,x_3)=(0,8,20)$ with $z_{\max}=400$.

## Common mistakes & how to avoid them
- Dual sign errors: forgetting that equality constraints produce unrestricted dual variables (as shown in the lecture’s example).
- Mixing “max primal ↔ min dual” pairing and reading the inequality $z \le w$ backwards.
- Treating “unbounded primal” and “infeasible dual” as unrelated: in LP duality they are tightly linked (see lab Problem 2 discussion).
- In revised simplex: confusing $B^{-1}b$ (basic values) with $B^{-1}P_j$ (direction for ratio test).

## Quick recap
- Duality gives bounds and an alternative way to solve/interpret an LP.
- Basic solutions and reduced costs are the algebra behind “corner points are enough”.
- Revised simplex and bounded-variable methods are efficiency/extension ideas built on the same core logic.

## Exam prep

### Likely questions
- Construct the dual of a given LP and state sign restrictions.
- Use weak/strong duality to justify bounds and optimality.
- Explain how dual variables relate to constraints (shadow-price intuition).
- Compute a basic solution $X_B = B^{-1}b$ for a given basis.
- Explain what reduced costs mean and how they guide entering-variable choice.

### Checklist
- I can build a dual LP from a primal (and check it against dimensions).
- I can state and apply $z \le w$ and $z^*=w^*$.
- I can compute $B^{-1}b$ and interpret feasibility.
- I can explain reduced costs and the revised simplex idea.

## Sources used
- [F25 - Intro to Opt -Lecture_5(1) - Duality.md](src/F25%20-%20Intro%20to%20Opt%20-Lecture_5%281%29%20-%20Duality.md)
- [F25 - Intro to Opt -Lecture_5(2) - Advanced LP.md](src/F25%20-%20Intro%20to%20Opt%20-Lecture_5%282%29%20-%20Advanced%20LP.md)
- [Lab05.md](src/Lab05.md)

