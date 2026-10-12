# Lecture 10: Nonlinear Programming Algorithms (1)
**Dr. Mohammad Reza Bahrami**
*Innopolis University*
*Course of Optimization*
*Fall 2025*

---

## Materials Note
Materials are taken from different sources with modifications. I do not claim any authorship of these materials.
**Dr. Mohammad Reza Bahrami**

---

# Course: Introduction to Optimization

## Lecture 10: Nonlinear Programming (1)

---

### Content
- Unconstrained Problems
- Direct Search Method
- Gradient Method

---

## Nonlinear Programming Algorithms

### Mathematical Programming

Minimize $f(\mathbf{X})$
Subject to:
$$
g_j(\mathbf{X}) \leq 0, \quad j = 1, 2, \dots, m
$$
$$
l_j(\mathbf{X}) = 0, \quad j = 1, 2, \dots, p
$$
$$
\mathbf{x} \in \mathcal{X}
$$

In **Linear Optimization**, $\mathcal{X} = \mathbb{R}^+$ and the objective and constraints are linear functions of $\mathbf{x}$.
In contrast, **Nonlinear Continuous Optimization** involves (some of) nonlinear objectives and constraints.

---

## Unconstrained Algorithms

### Direct Search Method

- Primarily applicable to strictly unimodal single-variable functions.
- Identifies an interval of uncertainty containing the optimal solution point.
- Iteratively narrows this interval until a desired level of accuracy is achieved.

#### Two Key Methods:
1. **Dichotomous Method**
2. **Golden Section Method**

Both methods seek to maximize $f(\mathbf{x})$ over an interval $[a, b]$ that includes the optimal point $\mathbf{x}^*$.

---

### General Step (Iteration)
Let $I^{(i)} = (\mathbf{x}_l, \mathbf{x}_u)$ be the current uncertainty interval. Initially, $\mathbf{x}_l = a$, $\mathbf{x}_u = b$.

#### **Dichotomous Method**
$$
\mathbf{x}_L = \frac{\mathbf{x}_u + \mathbf{x}_l}{2} - \Delta
$$
$$
\mathbf{x}_R = \frac{\mathbf{x}_u + \mathbf{x}_l}{2} + \Delta
$$

#### **Golden Section Method**
$$
\mathbf{x}_L = \mathbf{x}_u - \frac{5-1}{2}(\mathbf{x}_u - \mathbf{x}_l)
$$
$$
\mathbf{x}_R = \mathbf{x}_l + \frac{5-1}{2}(\mathbf{x}_u - \mathbf{x}_l)
$$

The selection ensures $\mathbf{x}_L < \mathbf{x}_m < \mathbf{x}_R < \mathbf{x}^*$.

---

### Interval Update Rules
1. If $f(\mathbf{x}_L) > f(\mathbf{x}_R)$, then $\mathbf{x}_L < \mathbf{x}^* < \mathbf{x}_R$.
   - Set $\mathbf{x}_u = \mathbf{x}_R$ and update interval: $I^{(i)} = (\mathbf{x}_L, \mathbf{x}_R)$.

2. If $f(\mathbf{x}_L) < f(\mathbf{x}_R)$, then $\mathbf{x}_m < \mathbf{x}^* < \mathbf{x}_u$.
   - Set $\mathbf{x}_l = \mathbf{x}_L$ and update interval: $I^{(i)} = (\mathbf{x}_L, \mathbf{x}_u)$.

3. If $f(\mathbf{x}_L) = f(\mathbf{x}_R)$, then $\mathbf{x}_m < \mathbf{x}^* < \mathbf{x}_R$.
   - Set $\mathbf{x}_l = \mathbf{x}_L$ and $\mathbf{x}_u = \mathbf{x}_R$.

---

### Convergence Properties
- The interval length decreases at each step: $I^{(i+1)} \leq \alpha I^{(i)}$.
- **Golden Section Method** recycles computations, reducing the number of evaluations by half.

#### Golden Ratio ($\alpha$)
$$
\alpha = \frac{\sqrt{5} - 1}{2} \approx 0.618
$$

---

### Example: Maximizing $f(x) = 3x^2 - x + 20$

**Constraints:** $0 \leq x \leq 2$ and $2 \leq x \leq 3$.

#### Iteration 1 (Dichotomous vs. Golden Section)
- **Initial Interval:** $[0, 3]$.
- **Golden Section:**
  $$
  \mathbf{x}_L = 3 - 0.618(3 - 0) = 1.146, \quad f(\mathbf{x}_L) = 3.438
 
$$
  $$
  \mathbf{x}_R = 0 + 0.618(3 - 0) = 1.854, \quad f(\mathbf{x}_R) = 5.562
 
$$
- **Update:** $I^{(1)} = (1.146, 3)$.

---

### Convergence Rate & Iterations

For the bisection method:
$$
c^* - c \leq \frac{b-a}{2^n}
$$
**Number of iterations ($n$)** required to achieve tolerance $\epsilon$:
$$
n \geq \log_2\left(\frac{b-a}{\epsilon}\right)
$$

Example: $\epsilon = 10^{-6}$, $a = 3$, $b = 4$:
$$
n \geq \log_2(1) - \log_{10}(10^{-6}) \approx 9.9658 \implies n = 10.
$$

---

## Gradient Method

### Overview
Optimizes twice-differentiable functions via **steepest ascent**.

- **Termination:** When the gradient vector $\nabla f(\mathbf{X})$ becomes null (necessary but not sufficient condition).
- **Initial Point:** $\mathbf{X}^0 = (\mathbf{x}_1^0, \mathbf{x}_2^0)$.

### Step Size Selection
$$
\mathbf{X}^{(i+1)} = \mathbf{X}^{(i)} + r^{(i)} \nabla f(\mathbf{X}^{(i)})
$$
where $r^{(i)}$ maximizes:
$$
h(r) = f\left[\mathbf{X}^{(i)} + r \nabla f(\mathbf{X}^{(i)})\right].
$$

---

### Example: Maximizing $f(x_1, x_2) = 4x_1^2 + 6x_2 - 2x_1x_2 - 2x_1x_2^2 - 2x_2^3$

#### Exact Optimum:
$$
(\mathbf{x}_1^*, \mathbf{x}_2^*) = \left( \frac{4}{9}, \frac{5}{6} \right)
$$

#### Iteration 1 (Initial Point: $\mathbf{X}^0 = (1, 1)$)
- Gradient:
$$
\nabla f(\mathbf{X}^0) = (-2, 0).
$$
- Next point:
$$
\mathbf{X}^{(1)} = (1 - 2r, 1), \quad h(r) = f(1 - 2r, 1).
$$
- Optimal $r^{(1)} = \frac{1}{4} \implies \mathbf{X}^{(1)} = (0.5, 1).$

---

#### Iteration 2
- Gradient:
$$
\nabla f(\mathbf{X}^{(1)}) = (0, 1).
$$
- Next point:
$$
\mathbf{X}^{(2)} = (0.5, 1 + r), \quad h(r) = f(0.5, 1 + r).
$$
- Optimal $r^{(2)} = \frac{1}{3} \implies \mathbf{X}^{(2)} = \left(\frac{5}{6}, \frac{4}{3}\right).$

---

#### Iteration 3 & Termination
- Gradient:
$$
\nabla f(\mathbf{X}^{(3)}) \approx (0, 0.25).
$$
- Further iterations refine the solution until convergence to $\nabla f(\mathbf{X}^*) \approx 0$.

**Final Approximate Optimum:**
$$
\mathbf{X} = (0.3438, 1.3125)
$$

---
```
