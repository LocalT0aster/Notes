# Week 2 — Simplex Method (Tableau Computations)

## What you should be able to do after this week
- Put an LP into standard/equation form suitable for simplex (slacks, nonnegativity, RHS ≥ 0).
- Build an initial simplex tableau and read a basic feasible solution (BFS) from it.
- Perform one full pivot step (choose entering/leaving variables + Gauss–Jordan updates).
- State the simplex optimality and feasibility (ratio test) rules used in the notes.
- Interpret slack variables as “resource status” (scarce vs abundant).

## Key ideas (intuition first)
- Simplex walks along edges of the feasible polytope from corner to corner.
- Each pivot swaps one basic variable with one nonbasic variable.
- The tableau is just a compact bookkeeping system for these swaps.
- Slacks tell you which constraints are binding (fully used resource) at the current solution.

## Core theory and definitions

### Standard form (as used here)
The simplex setup in the notes assumes:
- Constraints written as **equations** with nonnegative right-hand side.
- All variables (original + slack) are **nonnegative**.

### Tableau concepts
- **Basic variables** are listed in the “Basic” column; setting all nonbasic variables to 0 gives the BFS.
- The **z-row** (objective row) encodes whether increasing a nonbasic variable can improve $z$.

## Methods / Algorithms

### Tableau simplex algorithm (as presented)
1. **Start** with a BFS (often slacks basic, decision variables nonbasic = 0).
2. **Choose entering variable** (maximization):
   - Pick the nonbasic variable with the most negative coefficient in the z-row.
3. **Choose leaving variable** (feasibility / ratio test):
   - For the entering variable’s column, compute $\text{RHS}/a_{ij}$ for rows with $a_{ij} > 0$.
   - Take the smallest nonnegative ratio.
4. **Pivot (Gauss–Jordan)**:
   - Divide the pivot row by the pivot element.
   - Eliminate the entering column from all other rows (including the z-row).
5. **Stop** when no improving z-row coefficient exists:
   - For maximization: all z-row coefficients are nonnegative (in the convention used in the lecture).

### “Scarce vs abundant” resource interpretation
From the Tatar-Paint tableau discussion:
- A constraint is **scarce** if its slack variable is 0 at the solution (binding).
- A constraint is **abundant** if its slack is positive (not fully used).

## Worked examples

### Example A — Tatar-Paint: first tableau and first pivot (outline)
The lecture constructs the initial tableau with slack variables $s_1,\dots,s_4$ and objective
$$
z - 5x_1 - 4x_2 = 0.
$$
Then (for the maximization convention used):
- Entering variable: $x_1$ (most negative coefficient in z-row).
- Leaving variable: $s_1$ (smallest positive ratio).
- Pivot updates produce a new tableau, then $x_2$ is considered next.

### Example B — Tutorial problems (results provided)
Selected results stated in [Tutorial02.md](src/Tutorial02.md):
- Problem 1: maximize $x_1 + x_2$ → $x^* = (4,2)$, value $6$.
- Problem 2: maximize $x_1 + 2x_2$ → $x^* = (0,4)$, value $8$.
- Problem 3 (graphical): maximize/minimize $4x_1 + x_2$ → reported maximizer $x^* = (36/11, 5/11)$, value $149/11$.
- Problem 5: maximize $2x_1 + 3x_2 + 4x_3$ → $x^* = (1,3,0)$, value $11$.

### Example C — Lab 2 notes (partial and truncated)
[Lab02.md](src/Lab02.md) includes:
- A simplex-table example for maximize $9x_1 + 10x_2 + 16x_3$ with the reported optimum $x_1 = 0, x_2 = 8, x_3 = 20$ and objective value $400$.
- A second problem statement that is **cut off mid-solution** (“Not found in provided materials” beyond the visible partial tableau).

## Common mistakes & how to avoid them
- Pivoting on a zero/negative pivot element (breaks feasibility).
- Doing the ratio test using rows with $a_{ij} \le 0$ (those don’t bound the entering variable).
- Mixing “maximize” vs “minimize” sign conventions for the z-row.
- Losing track of which variables are basic vs nonbasic after a pivot.
- Arithmetic slips in Gauss–Jordan updates (always re-check the pivot column becomes a unit vector).

## Quick recap
- Simplex = repeat (enter → leave → pivot) until optimality.
- Tableau encodes the current BFS and how objective changes if you increase nonbasic variables.
- Slacks provide a direct interpretation of binding constraints.

## Exam prep

### Likely questions
- Convert a small LP to equation form and write its initial tableau.
- Given a tableau, identify the current BFS and objective value.
- Perform one pivot step correctly (enter/leave + updated tableau).
- Explain the meaning of a slack variable being 0 vs positive.

### Checklist
- I can build an initial tableau from an LP in standard form.
- I can choose entering/leaving variables using the lecture’s rules.
- I can pivot and read the next BFS.
- I can decide when a tableau is optimal (for the max convention used).

## Sources used
- [F25 - Intro to Opt -Lecture_2 - Simplex.md](src/F25%20-%20Intro%20to%20Opt%20-Lecture_2%20-%20Simplex.md)
- [Tutorial02.md](src/Tutorial02.md)
- [Lab02.md](src/Lab02.md)

