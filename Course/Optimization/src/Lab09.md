# Introduction to Optimization
## Problems Sheet 9

---

### Problem 1: Minimize using Lagrangian method
**Objective:**
Minimize
f(X) = x_2_1 + x_2_2 + x_3

**Constraints:**
g_1(X) = x_1 + x_2 + x_3 − 4 = 0,
g_2(X) = 2x_1 − 3x_2 − 12 = 0.

---

#### Solution:
- Number of variables: n = 3
- Number of constraints: m = 2

**Lagrangian Function:**
$$
L(x_1, x_2, x_3, \lambda_1, \lambda_2) = f(X) - \lambda_1 g_1(X) - \lambda_2 g_2(X)
$$
$$
= x_2_1 + x_2_2 + x_3 - \lambda_1 (x_1 + x_2 + x_3 - 4) - \lambda_2 (2x_1 - 3x_2 - 12).
$$

**Necessary Conditions:**
$$
\frac{\partial L}{\partial x_1} = 2x_1 - \lambda_1 - 2\lambda_2 = 0,
$$
$$
\frac{\partial L}{\partial x_2} = 2x_2 - \lambda_1 + 3\lambda_2 = 0,
$$
$$
\frac{\partial L}{\partial x_3} = 1 - \lambda_1 = 0,
$$
$$
\frac{\partial L}{\partial \lambda_1} = -(x_1 + x_2 + x_3 - 4) = 0,
$$
$$
\frac{\partial L}{\partial \lambda_2} = -(2x_1 - 3x_2 - 12) = 0.
$$

**Solution of Simultaneous Equations:**
$$
\begin{bmatrix}
x_1 \\
x_2 \\
x_3 \\
\lambda_1 \\
\lambda_2
\end{bmatrix}
=
\begin{bmatrix}
\frac{63}{26} \\
-\frac{31}{13} \\
\frac{103}{26} \\
\frac{25}{13} \\
0
\end{bmatrix}.
$$

**Extrema Point:**
$$
X_0 = \begin{bmatrix} x_{01} \\ x_{02} \\ x_{03} \end{bmatrix}
= \begin{bmatrix} \frac{63}{26} \\ -\frac{31}{13} \\ \frac{103}{26} \end{bmatrix}.
$$

---

#### Method 1: Sufficient Condition
The bordered Hessian $H$ is evaluated, and the determinant condition for sufficiency:
$$
(-1)^m \det(H) > 0,
$$
where $m = 2$. For this problem, it evaluates to $26 > 0$, confirming a minimum.

---

#### Method 2: Convexity Check
The objective function $f(X)$ is convex (verified via definition of convexity), ensuring $X_0$ is indeed the minimum point.

---

### Problem 2: Maximize using Lagrangian method
**Objective:**
Maximize
f(X) = x_1x_2 + x_2x_3

**Constraints:**
g_1(X) = x_1 + x_2 − 4 = 0,
g_2(X) = x_2 + x_3 − 4 = 0.

---

#### Solution:
**Lagrangian Function:**
$$
L(x_1, x_2, \lambda_1, \lambda_2) = f(X) - \lambda_1 g_1(X) - \lambda_2 g_2(X)
$$
$$
= x_1x_2 + x_2x_3 - \lambda_1 (x_1 + x_2 - 4) - \lambda_2 (x_2 + x_3 - 4).
$$

**Necessary Conditions:**
$$
\frac{\partial L}{\partial x_1} = x_2 - \lambda_1 = 0,
$$
$$
\frac{\partial L}{\partial x_2} = x_1 + x_3 - \lambda_1 - \lambda_2 = 0,
$$
$$
\frac{\partial L}{\partial x_3} = x_2 - \lambda_2 = 0,
$$
$$
\frac{\partial L}{\partial \lambda_1} = -(x_1 + x_2 - 4) = 0,
$$
$$
\frac{\partial L}{\partial \lambda_2} = -(x_2 + x_3 - 4) = 0.
$$

**Solution of Simultaneous Equations:**
$$
\begin{bmatrix}
x_1 \\
x_2 \\
x_3 \\
\lambda_1 \\
\lambda_2
\end{bmatrix}
=
\begin{bmatrix}
2 \\
2 \\
2 \\
2 \\
2
\end{bmatrix}.
$$

**Extrema Point:**
$$
X_0 = \begin{bmatrix} x_{01} \\ x_{02} \\ x_{03} \end{bmatrix} = \begin{bmatrix} 2 \\ 2 \\ 2 \end{bmatrix}.
$$

---

#### Hessian Analysis:
The bordered Hessian determinant $(-1)^m \det(H) = -4 < 0$ confirms that $X_0$ is a **maximum point**.

---

### Problem 3: Determine extreme points and their types
**Objective:**
Minimize/Maximize
f(X) = x_1x_2x_3

**Constraints:**
g_1(X) = 2x_1x_2 + x_2x_3 − 12 = 0,
g_2(X) = 2x_1 − x_2 − 8 = 0.

---

#### Solution:
**Lagrangian Function:**
$$
L(x_1, x_2, x_3, \lambda_1, \lambda_2) = f(X) - \lambda_1 g_1(X) - \lambda_2 g_2(X)
$$
$$
= x_1x_2x_3 - \lambda_1 (2x_1x_2 + x_2x_3 - 12) - \lambda_2 (2x_1 - x_2 - 8).
$$

**Necessary Conditions:**
$$
\frac{\partial L}{\partial x_1} = x_2x_3 - 2\lambda_1 x_2 - 2\lambda_2 = 0,
$$
$$
\frac{\partial L}{\partial x_2} = x_1x_3 - \lambda_1 (2x_1 + x_3) + \lambda_2 = 0,
$$
$$
\frac{\partial L}{\partial x_3} = x_1x_2 - \lambda_1 x_2 = 0,
$$
$$
\frac{\partial L}{\partial \lambda_1} = -(2x_1x_2 + x_2x_3 - 12) = 0,
$$
$$
\frac{\partial L}{\partial \lambda_2} = -(2x_1 - x_2 - 8) = 0.
$$

**Solutions:**
Two critical points:
$$
X_0 =
\begin{bmatrix}
3 \\
-2 \\
-12
\end{bmatrix},
\quad
Y_0 =
\begin{bmatrix}
-\frac{1}{3} \\
-\frac{26}{3} \\
-\frac{28}{39}
\end{bmatrix}.
$$

---

#### Case 1: Point $X_0$
Hessian bordered determinant:
$$
(-1)^m \det(H(X_0)) = -160 < 0,
$$
so $X_0$ is a **maximum point**.

---

#### Case 2: Point $Y_0$
Hessian bordered determinant:
$$
(-1)^m \det(H(Y_0)) = \frac{27040}{9} > 0,
$$
so $Y_0$ is a **minimum point**.

---

### Problem 4: Maximize with inequality constraints
**Objective:**
Maximize
f(X) = 2x_1 + 4x_2 − x_2_1 − 2x_2_2

**Constraints:**
$$
g_1(X) = x_1 + 2x_2 - 8 \leq 0,
$$
$$
g_2(X) = 2x_1 - x_2 - 12 \leq 0,
$$
$$
g_3(X) = -x_1 + s_{23} \leq 0,
$$
$$
g_4(X) = -x_2 + s_{24} \leq 0.
$$

---

#### Solution:
Slack variables introduced, Lagrangian function formed and solved numerically to yield:
$$
X_0 = (1, 1), \quad \lambda = (0, 0, 0, 0),
$$
with all slack variables positive.

**Sufficiency Check:**
- Hessian of $f$ is negative definite.
- Objective function $f(X)$ is concave.
Thus, $X_0$ is a **maximum point**.

---

### Problem 5: Minimize with inequality constraints
**Objective:**
Minimize
f(X) = 3x_2_1 + 4x_1x_2 + 5x_2_2

**Constraints:**
$$
