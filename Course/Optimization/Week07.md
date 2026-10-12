# Week 7 — Transportation Problems (Transportation Simplex)

## What you should be able to do after this week
- Write the standard transportation LP model (supplies, demands, costs, shipments).
- Check whether a transportation problem is balanced and fix it with a dummy source/destination if needed.
- Construct an initial basic feasible solution (BFS) using:
  - Northwest corner rule
  - Vogel’s approximation method (VAM)
  - Russell’s approximation method (RAM)
- Perform the transportation optimality test using potentials $u_i, v_j$ and reduced costs.
- Explain (and conceptually execute) a transportation simplex improvement step via a closed loop.

## Key ideas (intuition first)
- Transportation problems are structured LPs: constraints are “row sums = supply” and “column sums = demand”.
- This structure enables specialized methods that are much faster than general simplex on a full tableau.
- The $u$-$v$ potential method is a compact way to compute reduced costs and test optimality.

## Core theory and definitions

### Transportation model
Decision variables:
- $x_{ij}$: quantity shipped from source $i$ to destination $j$

Objective (typically minimization):
$$
\min \sum_{i=1}^m \sum_{j=1}^n c_{ij} x_{ij}
$$

Constraints:
- Supply (each source ships its supply):
  $$
  \sum_{j=1}^n x_{ij} = s_i
  $$
- Demand (each destination receives its demand):
  $$
  \sum_{i=1}^m x_{ij} = d_j
  $$
- Nonnegativity: $x_{ij} \ge 0$

Feasibility condition (stated explicitly in the lecture):
$$
\sum_i s_i = \sum_j d_j.
$$
If not balanced, add a dummy row/column to absorb the slack.

### Basic feasible solutions
For a balanced $m\times n$ transportation problem:
- A BFS has $m+n-1$ basic variables (allocations).

## Methods / Algorithms

### Initial BFS construction

#### Northwest corner rule
1. Start at the top-left cell $(1,1)$.
2. Allocate as much as possible: $\min(\text{remaining }s_1,\text{remaining }d_1)$.
3. If a supply is exhausted, move down; if a demand is exhausted, move right.
4. Continue until all supplies/demands are satisfied.

#### Vogel’s approximation method (VAM)
1. For each row/column, compute the **penalty** = (smallest cost) − (second smallest cost).
2. Pick the row/column with the largest penalty.
3. In that row/column, allocate as much as possible to the cheapest remaining cell.
4. Update supplies/demands and repeat.

#### Russell’s approximation method (RAM)
The lecture defines:
$$
\Delta_{ij} = c_{ij} - u_i - v_j
$$
and suggests choosing the most negative $\Delta_{ij}$ (largest improvement) when building or improving solutions.

### Optimality test (u–v potentials)
For basic cells $(i,j)$, enforce:
$$
c_{ij} - u_i - v_j = 0.
$$
There are $m+n$ unknowns $u_i, v_j$, but only $m+n-1$ basic equations, so one potential can be set arbitrarily (the lecture suggests picking a row with many allocations and setting its $u_i = 0$).

For nonbasic cells, compute reduced costs:
$$
\Delta_{ij} = c_{ij} - u_i - v_j.
$$
For a minimization transportation problem:
- If all $\Delta_{ij} \ge 0$, the BFS is optimal.
- If some $\Delta_{ij} < 0$, pick a negative $\Delta_{ij}$ as the entering cell.

### Transportation simplex improvement (conceptual)
1. Choose an entering nonbasic cell with $\Delta_{ij} < 0$.
2. Form a **closed loop** through basic cells in the tableau, alternating horizontal/vertical moves.
3. Mark alternating + and − signs along the loop (entering cell is +).
4. Increase shipments on + cells and decrease on − cells by $\theta$, where $\theta$ is the smallest shipment on a − cell.
5. The cell that hits 0 leaves the basis; update the BFS.

## Worked examples

### Example A — “How to compute $u_i, v_j$” (lecture tactic)
Given a BFS, the lecture notes:
- Write $c_{ij} - u_i - v_j = 0$ for each basic allocation.
- Fix one potential (e.g., set $u_k = 0$).
- Solve sequentially for the remaining $u$’s and $v$’s.

### Example B — Lab transportation starts (NW corner and minimal element)
[Lab07.md](src/Lab07.md) contains full setups and partial computations for transportation instances, including:
- A 3-source / 5-destination problem solved by:
  - Northwest corner rule
  - Minimal element method
  with a reported total cost $S = 1380$ for the shown allocations.

**Not found in provided materials:** [Lab07.md](src/Lab07.md) ends mid-expression in Problem 3’s total-cost computation, so the final numeric cost there is incomplete.

### Example C — Slide-style transportation simplex iteration (lecture narrative)
The lecture explains:
- If some reduced costs are negative (e.g., $c_{25}-u_2-v_5=-2$), the BFS is not optimal.
- Choose the most negative reduced cost as the entering cell.
- Update allocations along the induced loop; the first basic variable to hit 0 leaves the basis.

## Common mistakes & how to avoid them
- Forgetting to balance the problem ($\sum s_i$ must equal $\sum d_j$); fix with a dummy row/column.
- Counting basics incorrectly; you typically want $m+n-1$ allocations (degenerate BFS needs special care).
- Solving for $u_i, v_j$ without fixing one potential (system is underdetermined by 1).
- Using the optimality condition with the wrong sign convention (transportation is usually a minimization).
- Building an invalid loop (must alternate row/column moves and return to the entering cell).

## Quick recap
- Transportation problems have specialized structure.
- Build an initial BFS (NW/Vogel/Russell), compute potentials, test reduced costs.
- If nonoptimal, pivot via a closed-loop adjustment until all reduced costs are nonnegative.

## Exam prep

### Likely questions
- Formulate a transportation model and check the balance condition.
- Construct an initial BFS by NW corner or VAM.
- Compute $u_i, v_j$ and reduced costs $\Delta_{ij}$.
- Perform one transportation simplex improvement step (loop + $\theta$).

### Checklist
- I can write the transportation LP and explain each term.
- I can produce an initial BFS (NW corner / VAM).
- I can compute potentials and reduced costs for a given BFS.
- I can explain the loop adjustment and leaving-variable rule.

## Sources used
- [F25 - Intro to Opt -Lecture_7 - Transportation Problem.md](src/F25%20-%20Intro%20to%20Opt%20-Lecture_7%20-%20Transportation%20Problem.md)
- [Tutorial07.md](src/Tutorial07.md) (note: file content is an interior-point tutorial and is truncated)
- [Lab07.md](src/Lab07.md) (note: truncated near the end)

