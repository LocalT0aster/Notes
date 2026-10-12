# Week 8 — Classical Optimization I (Unconstrained + Newton)

## What you should be able to do after this week
- Define local vs global maxima/minima and what a stationary point is.
- Apply the necessary condition $\nabla f(X^*) = 0$ for unconstrained extrema.
- Classify stationary points using the Hessian definiteness test (min/max/saddle).
- Explain the higher-order derivative rule for 1D stationary points (first nonzero derivative).
- Use Newton–Raphson iterations to solve $f(x)=0$ (and understand its role in optimization tasks).
- Describe (at a high level) how equality constraints motivate constrained-derivative (Jacobian) ideas.

## Key ideas (intuition first)
- “Zero gradient” is necessary for an unconstrained optimum, but not sufficient (saddles exist).
- The Hessian tells you local curvature: bowl up (min), bowl down (max), mixed (saddle).
- Newton’s method is a fast local method — great near the solution, risky far away.

## Core theory and definitions

### Extrema and stationary points
For differentiable $f$:
- **Necessary condition** for an unconstrained extremum:
  $$
  \nabla f(X^*) = 0.
  $$
Points satisfying this are **stationary**; they can be minima, maxima, or saddles.

### Hessian test (sufficient conditions)
Let $H(X)$ be the Hessian matrix at a stationary point $X^*$:
- If $H(X^*)$ is **positive definite** → local minimum.
- If $H(X^*)$ is **negative definite** → local maximum.
- If $H(X^*)$ is **indefinite** → saddle point.

### Higher-order condition (1D)
If $f'(x^*)=f''(x^*)=\cdots=f^{(n-1)}(x^*)=0$ and $f^{(n)}(x^*)\ne 0$:
- $n$ odd → inflection point.
- $n$ even → min if $f^{(n)}(x^*)>0$, max if $f^{(n)}(x^*)<0$.

## Methods / Algorithms

### Newton–Raphson (1D)
Solve $f(x)=0$ via:
$$
x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}.
$$
Stop when iterates change very little or $|f(x_k)|$ is small.

Practical note:
- Newton is local; a poor starting point can diverge or jump to an unintended root.

### Equality constraints preview (Jacobian method idea)
Lecture 8 starts discussing how, under equality constraints $g(X)=0$, feasible directions are restricted.
The notes introduce constrained-derivative/Jacobian machinery and example calculations, but the formatting in the provided file is noisy; focus on the conceptual takeaway:
- “You can’t move in an arbitrary direction; feasible moves must stay on the constraint surface.”

## Worked examples

### Example A — Newton method for $\sqrt{2}$ (Lab 8)
Solve $x^2 - 2 = 0$ with $x_0 = 1.5$:
$$
x_{k+1} = x_k - \frac{x_k^2 - 2}{2x_k}.
$$
[Lab08.md](src/Lab08.md) shows convergence to $\sqrt{2}\approx 1.414213562$ in a few iterations.

### Example B — Newton for locating extrema (Lab 8 style)
For $f(x)$, stationary points solve $f'(x)=0$. Newton can be applied to $g(x)=f'(x)$.
[Lab08.md](src/Lab08.md) demonstrates this for $g(x)=x^3+3x^2-1$ using different starting points to land on different roots.

### Example C — “Be skeptical” about algebraic details
Some expressions in [F25 - Intro to Opt -Lecture_8- Classical Optimization (1).md](src/F25%20-%20Intro%20to%20Opt%20-Lecture_8-%20Classical%20Optimization%20%281%29.md) and [Lab08.md](src/Lab08.md) include typos/inconsistent symbols after conversion from slides/PDF.
When you compute by hand, re-check:
- dimensions (vector vs scalar),
- sign conventions,
- whether you are solving $f=0$ (root finding) or $\nabla f=0$ (stationary points).

## Common mistakes & how to avoid them
- Treating $\nabla f=0$ as “guaranteed optimum” (it’s only necessary).
- Applying the Hessian test without evaluating at the stationary point.
- Confusing positive definite vs “positive determinant” (definiteness is stronger than a single determinant check).
- Using Newton’s method when $f'(x)$ is zero/near-zero (division blow-up).
- Stopping Newton too early (always check either residual $|f(x_k)|$ or step size).

## Quick recap
- Unconstrained optimum → check $\nabla f=0$, then classify using the Hessian.
- Newton–Raphson is a powerful local solver for equations, often used inside optimization routines.

## Exam prep

### Likely questions
- Find stationary points of a multivariable $f$ and classify them with Hessian definiteness.
- Use the higher-order derivative test for a 1D stationary point.
- Perform 2–3 Newton iterations for a scalar equation (and estimate error).
- Explain the difference between root finding and optimization.

### Checklist
- I can compute $\nabla f$ and $H$ and use them correctly.
- I can distinguish minimum/maximum/saddle via curvature.
- I can do Newton iterations and interpret convergence behavior.

## Sources used
- [F25 - Intro to Opt -Lecture_8- Classical Optimization (1).md](src/F25%20-%20Intro%20to%20Opt%20-Lecture_8-%20Classical%20Optimization%20%281%29.md)
- [Lab08.md](src/Lab08.md)

