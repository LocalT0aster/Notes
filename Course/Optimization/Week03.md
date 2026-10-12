# Week 3 — Artificial Variables (Big‑M and Two‑Phase Methods)

## What you should be able to do after this week
- Detect when slack variables are not enough to start simplex (equality and $\ge$ constraints).
- Convert constraints to an equation form using slack/surplus and (when needed) artificial variables.
- Set up the **Big‑M method** objective and correctly “substitute out” basic artificial variables from the z-row.
- Explain the **two‑phase method** and how Phase I detects infeasibility.

## Key ideas (intuition first)
- Simplex needs a starting BFS. If the “obvious” slack-based BFS doesn’t exist, we manufacture one.
- Artificial variables are bookkeeping devices: they make a starting basis possible, but must end at 0.
- Two-phase is the clean way to avoid picking a numeric $M$; Big‑M bakes the “remove artificials” goal into the objective.

## Core theory and definitions

### When do we need artificial variables?
From the lecture notes:
- If constraints are not all “$\le$ with nonnegative RHS”, adding only slack variables may not yield a BFS.
- Typical triggers:
  - Equality constraints $=$
  - “$\ge$” constraints (after adding a surplus variable, you still may not have an identity column)

### Big‑M (M‑method)
Idea: penalize artificial variables heavily so the algorithm drives them to 0.
- For **maximization**: subtract $M R_i$ terms from the objective.
- For **minimization**: add $M R_i$ terms to the objective.

Practical watch-out (noted in the lecture remarks):
- Big $M$ does **not** magically fix infeasibility; if the model is infeasible, at least one artificial variable stays positive.

### Two‑phase method
Phase I:
- Add artificial variables where needed.
- Optimize an auxiliary objective (typically: minimize the sum of artificial variables).
- If the Phase I optimum is positive → **no feasible solution** for the original problem.

Phase II:
- Start from the feasible basis found in Phase I.
- Restore the original objective and continue simplex.

## Methods / Algorithms

### Constraint conversion checklist (operational)
1. Ensure RHS is nonnegative (multiply the whole constraint by $-1$ if needed).
2. For $\le$: add slack $+s$.
3. For $\ge$: subtract surplus $-s$ and add artificial $+R$.
4. For $=$: add artificial $+R$.
5. Build the initial tableau with the artificial variables as basic (where needed).
6. Fix the objective row:
   - If an artificial variable is basic, eliminate its column from the z-row by adding/subtracting a multiple of that constraint row (as shown in tutorial problems).

### Big‑M vs Two‑phase (how to choose)
- If you want a single-phase simplex run: Big‑M.
- If you want to avoid a large numeric constant $M$: Two‑phase.

## Worked examples

### Example A — “Develop the z-row after substituting artificial variables”
[Tutorial03.md](src/Tutorial03.md) focuses on exactly this skill: once an artificial variable is basic, the initial z-row must be adjusted.

Illustrative pattern (as stated in the tutorial solutions):
- Start with a z-row that contains an $M$ coefficient on $R_1$.
- Then update:
  $$
  \text{New z-row} = \text{Old z-row} + (-M)\times(\text{row of }R_1)
  $$
  for a maximization problem (sign follows the chosen convention).

### Example B — Two‑phase overview (lecture)
The lecture outlines:
1. Add artificial variables.
2. Phase I objective eliminates them.
3. Phase II solves the original objective using the Phase I feasible basis.

**Not found in provided materials:** the Phase I example tableau in [F25 - Intro to Opt -Lecture_3 - Artifitial.md](src/F25%20-%20Intro%20to%20Opt%20-Lecture_3%20-%20Artifitial.md) is cut off mid-tableau, so later numeric steps are missing.

### Example C — Lab problems (partial)
[Lab03.md](src/Lab03.md) includes an M‑method problem and a two‑phase problem, but the document is truncated during the Phase I iterations.
Use it as a template for how the model is rewritten (standard form + artificials), even if later pivots are not visible.

## Common mistakes & how to avoid them
- Forgetting that $\ge$ constraints introduce a **surplus** variable first (then often an artificial).
- Not eliminating basic artificial variables from the z-row before pivoting.
- Using the wrong sign for the $M$ penalty (depends on max vs min).
- Declaring feasibility too early: in two-phase, you need the Phase I optimum value.
- Numerical instability with huge $M$ (a reason the two-phase method is preferred conceptually).

## Quick recap
- Artificial variables give you a starting basis; your algorithm must “kick them out”.
- Big‑M: do it via penalties in the objective.
- Two‑phase: do it via an auxiliary Phase I objective, then solve the real objective in Phase II.

## Exam prep

### Likely questions
- Decide whether an LP needs artificials and show the standard-form conversion.
- Write the Phase I objective for a given model.
- Adjust the z-row to eliminate basic artificial variables.
- Explain how infeasibility is detected in Phase I.

### Checklist
- I can rewrite $\le,\ge,=$ constraints into equation form with correct variables.
- I can set up Big‑M or Phase I correctly.
- I can do the “substitute out artificials” z-row step without sign mistakes.
- I can state the feasibility decision rule for Phase I.

## Sources used
- [F25 - Intro to Opt -Lecture_3 - Artifitial.md](src/F25%20-%20Intro%20to%20Opt%20-Lecture_3%20-%20Artifitial.md)
- [Tutorial03.md](src/Tutorial03.md)
- [Lab03.md](src/Lab03.md)

