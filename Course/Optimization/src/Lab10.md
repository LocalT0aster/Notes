# Introduction to Optimization

## Problems Sheet 10

---

### Problem 1: Minimize $f(x) = x^2 + 2x$
**Subject to:** $-3 \leq x \leq 5$

#### a) Use the dichotomous method with $M = 0.1$ and $M = 0.2$, solving iterations 1–4, and estimate error.

##### Dichotomous Method ($M = 0.1$)
**Iteration 1:**
$I_0 = (-3, 5)$
- $x_1 = (5 - 3 - 0.1)/2 = 0.95$
- $x_2 = (5 - 3 + 0.1)/2 = 1.05$
- $f(x_1) = 2.8025$, $f(x_2) = 3.2025$

Since $f(x_1) < f(x_2)$:
$I_1 = (-3, 1.05)$

**Iteration 2:**
- $x_1 = (1.05 - 3 - 0.1)/2 = -1.025$
- $x_2 = (1.05 - 3 + 0.1)/2 = -0.925$
- $f(x_1) = -0.999375$, $f(x_2) = -0.994375$

Since $f(x_1) < f(x_2)$:
$I_2 = (-3, -0.925)$

**Iteration 3:**
- $x_1 = (-0.925 - 3 - 0.1)/2 = -2.0125$
- $x_2 = (-0.925 - 3 + 0.1)/2 = -1.9125$
- $f(x_1) = 0.0251562$, $f(x_2) = -0.167344$

Since $f(x_1) > f(x_2)$:
$I_3 = (-2.0125, -0.925)$

**Iteration 4:**
- $x_1 = (-0.925 - 2.0125 - 0.1)/2 = -1.51875$
- $x_2 = (-0.925 - 2.0125 + 0.1)/2 = -1.41875$
- $f(x_1) = -0.730898$, $f(x_2) = -0.824648$

Since $f(x_1) > f(x_2)$:
$I_4 = (-1.51875, -0.925)$
Estimated solution:
$$
x_0 = \frac{x_R + x_L}{2} = \frac{-1.51875 - 0.925}{2} = -1.22188
$$

---

##### Dichotomous Method ($M = 0.2$)
**Iteration 1:**
$I_0 = (-3, 5)$
- $x_1 = (5 - 3 - 0.2)/2 = 0.9$
- $x_2 = (5 - 3 + 0.2)/2 = 1.1$
- $f(x_1) = 2.61$, $f(x_2) = 3.41$

Since $f(x_1) < f(x_2)$:
$I_1 = (-3, 1.1)$

**Iteration 2:**
- $x_1 = (-3 + 1.1 - 0.2)/2 = -1.05$
- $x_2 = (-3 + 1.1 + 0.2)/2 = -0.85$
- $f(x_1) = -0.9975$, $f(x_2) = -0.9775$

Since $f(x_1) < f(x_2)$:
$I_2 = (-3, -0.85)$

**Iteration 3:**
- $x_1 = (-3 - 0.85 - 0.2)/2 = -2.025$
- $x_2 = (-3 - 0.85 + 0.2)/2 = -1.825$
- $f(x_1) = 0.050625$, $f(x_2) = -0.319375$

Since $f(x_1) > f(x_2)$:
$I_3 = (-2.025, -0.85)$

**Iteration 4:**
- $x_1 = (-2.025 - 0.85 - 0.2)/2 = -1.5375$
- $x_2 = (-2.025 - 0.85 + 0.2)/2 = -1.3375$
- $f(x_1) = -0.711094$, $f(x_2) = -0.886094$

Since $f(x_1) > f(x_2)$:
$I_4 = (-1.5375, -0.85)$
Estimated solution:
$$
x_0 = \frac{x_R + x_L}{2} = \frac{-1.5375 - 0.85}{2} = -1.19375
$$

---

#### Error Estimation
- **Case $M = 0.1$:**
  $$
|x^* - x_0| \leq \frac{|x_R - x_L|}{2} = \frac{0.59375}{2} = 0.296875
$$

- **Case $M = 0.2$:**
  $$
|x^* - x_0| \leq \frac{|x_R - x_L|}{2} = \frac{0.6875}{2} = 0.34375
$$

---

#### b) Number of iterations for $\epsilon = 0.1$

##### Case $M = 0.1$:
$$
\frac{(b_1 - a_1)}{2^{n-1}} + M \cdot \frac{1}{2^n} \leq 0.1
$$
Solving inequality:
$$
n = 7
$$

##### Case $M = 0.2$:
$$
\frac{(5 - (-3))}{2^{n-1}} + 0.2 \cdot \frac{1}{2^n} \leq 0.4
$$
Solving inequality:
$$
n = 6
$$

---

### Problem 2: Use the golden section method to minimize $f(x) = x^2 + 2x$
**Subject to:** $-3 \leq x \leq 5$

#### a) Iterations 1–4

##### Iteration 1:
$I_0 = (-3, 5)$
- $x_1 = 5 - \frac{5-(-3)}{2} \cdot \sqrt{5}-1 = 1.94427$
- $x_2 = -3 + \frac{5-(-3)}{2} \cdot \sqrt{5}-1 = 0.055728$

Since $f(x_1) > f(x_2)$:
$I_1 = (-3, 0.055728)$

##### Iteration 2:
- $x_1 = -1.11146$
- $x_2 = 0.055728$

Since $f(x_1) < f(x_2)$:
$I_2 = (-3, 0.055728)$

##### Iteration 3:
- $x_1 = -1.83282$
- $x_2 = -1.11146$

Since $f(x_1) > f(x_2)$:
$I_3 = (-1.83282, 0.055728)$

##### Iteration 4:
- $x_1 = -1.11146$
- $x_2 = -0.665631$

Since $f(x_1) < f(x_2)$:
$I_4 = (-1.83282, -0.665631)$

Estimated solution:
$$
x_0 = \frac{x_R + x_L}{2} = \frac{-1.83282 - 0.665
