# Optimization — Weekly Notes

Old AI notes by topic: [ByTopic/Optimization.md](ByTopic/Optimization.md)

## How to use this
- Work week-by-week in order; each `WeekXX.md` ends with an “Exam prep” section you can turn into practice questions.
- For each week: re-derive the key algorithms once without looking (simplex pivots, dual construction, KKT setup, etc.).
- Keep a running “mistakes list”: the “Common mistakes” sections are designed to seed it.

## Weekly notes

- [Week 1 — Introduction & Graphical Linear Programming](Week01.md)
  - Optimization problem statement, feasibility, modeling workflow
  - LP canonical form, slack variables, corner points/basic solutions
  - Graphical LP method and intuition for simplex
- [Week 2 — Simplex Method (Tableau Computations)](Week02.md)
  - Tableau mechanics, entering/leaving rules, Gauss–Jordan pivoting
  - Optimality and feasibility (ratio test) conditions
  - Slack interpretation (scarce vs abundant resources)
- [Week 3 — Artificial Variables (Big‑M and Two‑Phase Methods)](Week03.md)
  - When/why artificial variables are required
  - Big‑M setup and “fixing” the z-row
  - Two‑phase method and infeasibility detection
- [Week 4 — Simplex Special Cases & Graphical Sensitivity](Week04.md)
  - Degeneracy, redundancy, cycling intuition
  - Alternative optima and how simplex reveals them
  - Unboundedness and graphical sensitivity ranges (shadow prices)
- [Week 5 — Duality and Advanced Linear Programming](Week05.md)
  - Primal↔dual construction and primal–dual objective relationships
  - Dual values and simplex/reduced-cost interpretation
  - Advanced LP: bases, $B^{-1}$, revised simplex, bounded variables idea
- [Week 6 — Interior‑Point Methods (Projected Gradient + Centering)](Week06.md)
  - Interior-point intuition vs simplex
  - Projected gradient and scaling/centering iteration structure
  - Strict interior feasibility requirements and step-size logic
- [Week 7 — Transportation Problems (Transportation Simplex)](Week07.md)
  - Transportation LP model and balancing with dummy nodes
  - Initial BFS methods (NW corner, Vogel, Russell)
  - $u$-$v$ potentials, reduced costs, loop (cycle) adjustments
- [Week 8 — Classical Optimization I (Unconstrained + Newton)](Week08.md)
  - Stationary points, Hessian definiteness, higher-order tests (1D)
  - Newton–Raphson for equation solving and extrema finding
  - Equality constraints motivation (feasible directions)
- [Week 9 — Classical Optimization II (Lagrangian, KKT, Sensitivity)](Week09.md)
  - Lagrangian method and multiplier interpretation
  - KKT conditions and active-set thinking
  - Local sensitivity analysis and sufficiency ideas (bordered Hessian/convexity)
- [Week 10 — Nonlinear Programming Algorithms I (Direct Search + Gradient)](Week10.md)
  - 1D direct search (dichotomous, golden section), convergence/iteration counts
  - Gradient method with line search and common failure modes
- [Week 11 — Nonlinear Programming Algorithms II (QP + Linear Combinations)](Week11.md)
  - Quadratic programming form and KKT specialization
  - Phase-I-style feasibility approach (conceptual)
  - Linear combinations method (successive linearization + line search)

## Final review map
- Previous year Final sample: `Final24.md`
- Modeling → LP standard form → simplex tableaux → artificials (Big‑M / two‑phase)
- Simplex behavior → degeneracy / alternative optima / unboundedness → sensitivity (shadow prices)
- Duality ↔ reduced costs ↔ sensitivity interpretation ↔ revised simplex (matrix view)
- LP solvers: simplex (edge-walk) vs interior-point (interior path)
- Structured LPs: transportation model → $u$-$v$ potentials → loop pivots
- Calculus optimization: $\nabla f$, Hessian → Newton → equality constraints (Lagrange) → inequality constraints (KKT)
- NLP algorithms: direct search / gradient → constrained NLP (QP, linearization-based methods)
