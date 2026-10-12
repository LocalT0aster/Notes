# Week 4 — Simplex Special Cases & Graphical Sensitivity

## What you should be able to do after this week
- Recognize degeneracy, alternative optima, and unboundedness in LPs (graphically and in simplex logic).
- Explain why degeneracy can lead to cycling and how it relates to redundant constraints.
- Explain what “alternative optima” means and how simplex reveals it (zero reduced cost).
- Interpret graphical sensitivity analysis results (dual prices, feasibility ranges, coefficient ranges).

## Key ideas (intuition first)
- Not every LP behaves “nicely” during simplex; special cases matter for diagnosis and interpretation.
- Sensitivity analysis answers “what if we change a coefficient a little?” — but only within validity ranges.
- Shadow prices / dual prices are a bridge between primal LP geometry and economic interpretation.

## Core theory and definitions

### Degeneracy
From the lecture:
- A tie in the minimum ratio test may be broken arbitrarily.
- If this leads to a basic variable taking value 0 in the next BFS, the solution is **degenerate**.
Implications:
- Objective value can fail to improve from one iteration to the next.
- In rare cases, simplex can **cycle** (repeat bases indefinitely).
- Degeneracy often signals a **redundant constraint**.

### Alternative optima
An LP can have infinitely many optimal solutions when the objective is parallel to a binding constraint.
Simplex symptom (as described):
- A nonbasic variable has a zero coefficient in the optimal tableau’s objective row → you can pivot without changing $z$.

### Unbounded solution
The feasible region can be unbounded in some direction.
If the objective can increase indefinitely in that direction, the LP is **unbounded**.
Simplex symptom (high-level):
- An entering variable can improve the objective but has no leaving variable (no positive coefficients in its column for the ratio test).

## Methods / Algorithms

### Graphical sensitivity analysis (what the lecture does)
Two common “what if” questions:
1. **Change RHS (resource capacity)**:
   - Dual price (shadow price) tells objective change per unit RHS change, but only within a **feasibility range**.
2. **Change objective coefficients**:
   - The optimal corner stays optimal as long as the objective slope stays within an **optimality range**.

## Worked examples

### Example A — Degeneracy and redundancy (lecture example)
Maximize $z = 3x_1 + 9x_2$ subject to:
$$
x_1 + 4x_2 \le 8,\quad x_1 + 2x_2 \le 4,\quad x \ge 0.
$$
The lecture’s discussion highlights:
- A tie in the leaving variable choice causes degeneracy.
- One constraint can be redundant (removing it does not change the feasible set).

### Example B — Alternative optima (lecture example)
Maximize $z = 2x_1 + 4x_2$ subject to:
$$
x_1 + 2x_2 \le 5,\quad x_1 + x_2 \le 4,\quad x \ge 0.
$$
The lecture states that any point on a line segment of feasible boundary can achieve the same optimum value $z=10$.

### Example C — Graphical sensitivity (JOBCO example in the lecture)
The lecture provides dual-price style conclusions:
- Dual price for machine 1: $\$14/\text{hr}$ valid for capacity range $(2.67, 16)$ hr (as stated).
- Dual price for machine 2: $\$2/\text{hr}$ valid for capacity range $4$ to $24$ hr.

For objective coefficients:
- The optimum stays at the same corner as long as:
  $$
  \frac{c_1}{c_2} \in \left(\frac{1}{3}, 2\right),
  $$
  which the lecture uses to check whether new revenues keep the same optimal solution.

**Not found in provided materials:** the simplex-tableau details for the unbounded example are cut off in the lecture file, so only the definition/intuition is fully available.

## Common mistakes & how to avoid them
- Assuming “degenerate” means “multiple optima” (it doesn’t; it means a basic variable is 0).
- Forgetting that alternative optima are expected when an objective is parallel to a binding constraint.
- Confusing “unbounded feasible region” with “unbounded objective” (you need both for an unbounded LP).
- Using sensitivity/shadow prices outside their feasibility/optimality ranges.

## Quick recap
- Degeneracy: tie in ratio test → BFS with a zero basic variable → possible cycling, possible redundancy.
- Alternative optima: more than one optimal corner; objective value unchanged along an edge.
- Unbounded: objective can increase without bound because constraints don’t stop improvement.
- Sensitivity: local “what if” analysis with explicit validity ranges.

## Exam prep

### Likely questions
- Identify whether a situation corresponds to degeneracy / alternative optimum / unboundedness.
- Explain (or spot) redundancy in constraints.
- Interpret a shadow price and its feasibility range from a graphical LP.
- Determine whether changing $c_1, c_2$ keeps the same graphical optimum.

### Checklist
- I can define degeneracy, alternative optima, and unboundedness.
- I can explain how each shows up in simplex reasoning.
- I can use feasibility/optimality ranges correctly (and say when they stop applying).

## Sources used
- [F25 - Intro to Opt -Lecture_4 - Special Cases.md](src/F25%20-%20Intro%20to%20Opt%20-Lecture_4%20-%20Special%20Cases.md)
- [Tutorial04.md](src/Tutorial04.md)

