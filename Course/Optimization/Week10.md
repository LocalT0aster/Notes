# Week 10 — Nonlinear Programming Algorithms I (Direct Search + Gradient)

## What you should be able to do after this week
- Explain what makes nonlinear optimization different from LP (nonlinearity, local minima/maxima, algorithm variety).
- Apply 1D direct search methods for unimodal functions:
  - Dichotomous method
  - Golden section method
- State how fast each method shrinks the uncertainty interval and how iteration counts relate to tolerance.
- Describe (and compute one step of) the gradient (steepest ascent/descent) method with line search.

## Key ideas (intuition first)
- In 1D unimodal problems, optimization can be reduced to shrinking an interval containing the optimum.
- Golden section is efficient because it reuses function evaluations.
- In multi-D, “follow the gradient” is natural, but step size matters a lot.

## Core theory and definitions

### Unconstrained 1D direct search (as in the lecture)
Given a unimodal objective over $[a,b]$, maintain an **interval of uncertainty** that contains $x^*$.

#### Dichotomous method
Pick two close points around the midpoint:
$$
x_L = \frac{x_u + x_l}{2} - \Delta,\quad
x_R = \frac{x_u + x_l}{2} + \Delta.
$$
Compare $f(x_L)$ and $f(x_R)$ and keep the half-interval that must contain $x^*$.

#### Golden section method
Choose points using the golden ratio factor $\alpha \approx 0.618$ so that one point can be reused after shrinking:
$$
\alpha = \frac{\sqrt{5}-1}{2}.
$$
The lecture emphasizes reduced function evaluations compared to “fresh” bisection-style approaches.

### Gradient method (steepest ascent/descent)
Iterate:
$$
X^{(k+1)} = X^{(k)} + r^{(k)} \nabla f(X^{(k)})
$$
(for ascent; use minus for descent), where $r^{(k)}$ is chosen by line search:
$$
h(r) = f\left(X^{(k)} + r\nabla f(X^{(k)})\right).
$$

Stopping rule in the lecture:
- Gradient becomes (approximately) zero, or changes become negligible.

## Methods / Algorithms

### Direct search (practical steps)
1. Start with an interval $[a,b]$ that contains the optimum (assumed unimodal).
2. Evaluate at $x_L, x_R$ (dichotomous) or golden-section points.
3. Shrink the interval based on which evaluation is better.
4. Repeat until interval length ≤ tolerance $\epsilon$.

### Gradient method (practical steps)
1. Pick initial point $X^{(0)}$.
2. Compute gradient $\nabla f(X^{(k)})$.
3. Solve a 1D line search for $r^{(k)}$ along that direction.
4. Update $X^{(k+1)}$.
5. Stop when $\|\nabla f(X^{(k)})\|$ is small (necessary condition).

## Worked examples

### Example A — Dichotomous vs golden section (lecture-style)
Lecture 10 gives a worked comparison on a 1D polynomial example, showing how the interval shrinks and how golden section reuses evaluations.

### Example B — Lab sheet: minimizing $f(x)=x^2+2x$ on $[-3,5]$
[Lab10.md](src/Lab10.md) works through several iterations of:
- dichotomous method for different $M$ (called $M$ in the sheet),
- golden section iterations,
and includes interval-based error bounds.

**Not found in provided materials:** [Lab10.md](src/Lab10.md) is cut off mid-way through a later computation (the final estimate line is incomplete).

### Example C — Gradient method with line search (lecture)
Lecture 10 provides a multi-variable polynomial example and shows:
- computing $\nabla f$,
- updating $X$ using $r^{(k)}$ obtained from maximizing $h(r)$,
- iterating toward a stationary point.

## Common mistakes & how to avoid them
- Using direct search on a function that is not unimodal over the chosen interval.
- Mixing up “maximize” vs “minimize” when comparing $f(x_L)$ and $f(x_R)$.
- Incorrect golden-section point placement (the whole point is the reuse property).
- In gradient methods: picking a step size without a line search and overshooting badly.
- Concluding optimality from $\nabla f \approx 0$ without checking whether it’s max/min/saddle (Hessian logic from Weeks 8–9).

## Quick recap
- 1D unimodal optimization: shrink an interval (dichotomous/golden section).
- Multi-D unconstrained optimization: follow the gradient, but choose step size carefully.

## Exam prep

### Likely questions
- Perform 2–4 iterations of dichotomous or golden section for a 1D problem.
- Compute how many iterations are needed for a target $\epsilon$.
- Do one gradient step with a line search direction and compute the update.
- Explain why golden section is more evaluation-efficient than naive bisection-like methods.

### Checklist
- I can run the interval update rules without sign mistakes.
- I can state the golden ratio factor and how it shrinks the interval.
- I can compute $\nabla f$ and write a gradient-method update with line search.

## Sources used
- [F25 - Intro to Opt -Lecture_10 - NonLinear Programming (1).md](src/F25%20-%20Intro%20to%20Opt%20-Lecture_10%20-%20NonLinear%20Programming%20%281%29.md)
- [Lab10.md](src/Lab10.md) (note: truncated near the end)

