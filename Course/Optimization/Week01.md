# Week 1 — Introduction & Graphical Linear Programming

## What you should be able to do after this week
- Explain what an optimization problem is (decision variables, objective, constraints, feasible set).
- Classify problems (continuous vs discrete, linear vs nonlinear, convex vs nonconvex).
- Formulate simple real situations as linear programs (LPs).
- Rewrite LP constraints into a standard/canonical form (including slack variables).
- Solve a 2-variable LP graphically and interpret why an optimum happens at a corner point.
- Describe the simplex idea at a high level (move between basic feasible solutions).

## Key ideas (intuition first)
- Optimization is a structured way to pick “the best” option under constraints.
- Good optimization is mostly good modeling: define choices, constraints, and what “best” means.
- In LP, the feasible region is a polygon/polytope; “best” occurs at a corner (extreme point).
- Graphical LP is the “picture version” of the simplex method.

## Core theory and definitions

### What is an optimization problem?
Find a decision vector $X = [x_1, \ldots, x_n]^T$ that minimizes (or maximizes) an objective:
$$
\min f(X)
$$
subject to constraints:
- Inequalities $g_j(X) \le 0$, $j=1,\ldots,m$
- Equalities $l_k(X) = 0$, $k=1,\ldots,p$

Key terms:
- **Feasible**: satisfies all constraints.
- **Feasible set**: all feasible solutions.
- **Optimal**: feasible and best objective value.
- **Infeasible model**: no feasible solution exists.

### Categories you should recognize
- **Continuous vs discrete/combinatorial** (variables live in $\mathbb{R}^n$ vs integers/binaries).
- **Linear vs nonlinear** (objective/constraints linear or not).
- **Convex optimization** (in the notes: a convexity inequality for constraints is given; practically, convex problems are “well-behaved” and easier to solve reliably).

### Linear programming (LP) and standard forms
One canonical LP form in the materials is:
- Maximize $z = c^T x$
- Subject to $Ax \le b$, $x \ge 0$

Common rewrites used throughout the course:
- Turn $\le$ constraints into equations with **slack variables** $s \ge 0$:
  $$
  a^T x \le b \quad \Rightarrow \quad a^T x + s = b,\; s \ge 0
  $$
- Equality constraints can be viewed as “tight” constraints in the model (and later handled with specialized simplex starts).

### Corner points and basic solutions (graphical ↔ algebraic)
In algebraic form, corner points correspond to **basic solutions**:
- With $m$ equations in $n$ variables, set $n-m$ variables to zero (nonbasic) and solve for the remaining $m$ (basic).
- A **basic feasible solution (BFS)** is a basic solution that also satisfies nonnegativity.

The materials note that the number of potential corner points is combinatorial:
$$
\binom{n}{m} = \frac{n!}{(n-m)!\,m!}.
$$

## Methods / Algorithms

### Graphical LP solution (2 variables)
1. Plot each constraint boundary line.
2. Shade the feasible side (including $x_1 \ge 0, x_2 \ge 0$).
3. Find all corner points (intersections of active constraints).
4. Evaluate the objective at corner points (or slide an iso-objective line) and select the best.

### Simplex method (the “essence”)
1. Start from an initial BFS (often the slack-variable solution at the origin).
2. Pick one variable to enter the basis to improve the objective.
3. Pick a leaving variable to preserve feasibility.
4. Pivot (Gauss–Jordan) to get the next BFS.
5. Stop when no improving move exists.

Terminology that appears later:
- **Dictionary**: an equation system expressing basic variables in terms of nonbasic ones.
- **Basic variables**: variables on the left-hand side of a dictionary.
- **Nonbasic variables**: set to zero to get a BFS.

## Worked examples

### Example A — Ticket purchase as an optimization model (modeling mindset)
From the notes: buying airline tickets over five weeks with weekend discounts.
- Alternatives (ticket combinations) must satisfy “depart Monday, return Wednesday” each week.
- Objective is total cost.
- The provided comparison shows the cheapest plan is “cover every trip with a weekend-spanning discounted round trip” (Option (c)), total cost $\$1600$.

### Example B — Tatar-Paint LP (graphical optimum)
Maximize:
$$
z = 5x_1 + 4x_2
$$
Subject to the raw material and demand constraints listed in the lectures.

Graphical solution result in the notes:
- Optimal point at the intersection of the first two constraints: $x_1 = 3$, $x_2 = 1.5$
- Objective value: $z = 21$ (interpreted as $\$21{,}000$ in the lecture narrative).

### Example C — Diet LP (min-cost mix)
Minimize:
$$
z = 0.3x_1 + 0.9x_2
$$
Subject to the nutrition constraints (≥ feed mass, ≥ protein %, ≤ fiber %) and $x \ge 0$.

Provided optimal solution:
- $x_1 \approx 470.6$, $x_2 \approx 329.4$
- Cost $\approx \$437.64/\text{day}$

## Common mistakes & how to avoid them
- Forgetting nonnegativity constraints when plotting the feasible set.
- Solving “by eye” at a non-corner point (LP optimum is at an extreme point).
- Mixing up which side of a line corresponds to $\le$ vs $\ge$.
- Writing an LP model without units (what is “1 unit” of $x_i$?).
- Using graphical methods beyond 2 variables.

## Quick recap
- Optimization = objective + constraints + decision variables.
- LPs are special because geometry gives structure: extreme points matter.
- Graphical method and simplex are the same idea at different scales.

## Exam prep

### Likely questions
- Define feasible set / feasible solution / optimal solution / infeasible model.
- Convert a small LP into canonical/equation form using slack variables.
- Solve a 2-variable LP graphically and justify why the optimum is at a corner.
- Interpret a model: what do $x_i$, constraints, and slacks mean in words?

### Checklist
- I can state an optimization problem in symbols and in words.
- I can classify a problem as LP/NLP and continuous/discrete.
- I can convert $\le$ constraints to equations with slacks.
- I can solve a 2-variable LP graphically (corner points + objective values).

## Sources used
- [F25 - Intro to Opt - Lecture_1-1 - Introduction.md](src/F25%20-%20Intro%20to%20Opt%20-%20Lecture_1-1%20-%20Introduction.md)
- [F25 - Intro to Opt - Lecture_1-2 - Graphical.md](src/F25%20-%20Intro%20to%20Opt%20-%20Lecture_1-2%20-%20Graphical.md)
- [Lab01.md](src/Lab01.md)

