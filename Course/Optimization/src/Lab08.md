# Introduction to Optimization
## Problems Sheet 8

---

### Problem 1: Determine extreme points of function $f(X)$
**Function:**
$$
f(X) = 4x_1 + x_{21} + 8x_2 + x_{22} + x_3 (2 - x_1 - x_2 + x_3)
$$

#### Solution
The necessary condition $\nabla f(X_0) = 0$ gives:
$$
\frac{\partial f}{\partial x_1} = 4 + 2x_1 - x_3 = 0,
$$
$$
\frac{\partial f}{\partial x_2} = 8 + 2x_2 - x_3 = 0,
$$
$$
\frac{\partial f}{\partial x_3} = 2 - x_1 - x_2 + 2x_3 = 0.
$$

The solution of these equations is:
$$
X_0 = (-6, -8, -8).
$$

To determine the type of stationary point, consider the Hessian matrix $H$:

$$
H = \begin{bmatrix}
\frac{\partial^2 f}{\partial x_1^2} & \frac{\partial^2 f}{\partial x_1 \partial x_2} & \frac{\partial^2 f}{\partial x_1 \partial x_3} \\
\frac{\partial^2 f}{\partial x_2 \partial x_1} & \frac{\partial^2 f}{\partial x_2^2} & \frac{\partial^2 f}{\partial x_2 \partial x_3} \\
\frac{\partial^2 f}{\partial x_3 \partial x_1} & \frac{\partial^2 f}{\partial x_3 \partial x_2} & \frac{\partial^2 f}{\partial x_3^2}
\end{bmatrix}
= \begin{bmatrix}
2 & 0 & -1 \\
0 & 2 & -1 \\
-1 & -1 & -4
\end{bmatrix}.
$$

Evaluating the principal minors:
$$
\begin{align*}
D_{11} &= 2 > 0, \\
D_{11}D_{22} - D_{12}^2 &= (2)(2) - 0^2 = 4 > 0, \\
\det(H) &= (-1)(-1)(-4) + \text{other terms} = 4 > 0.
\end{align*}
$$

Consequently, $H \succ 0$. Therefore, $X_0 = (-6, -8, -8)$ represents a **minimum point**.

---

### Problem 2: Determine extreme points of function $f(X)$
**Function:**
$$
f(X) = -x_{21} - x_{22} - x_{23} + x_3 (4 - x_1 - x_2)
$$

#### Solution
The necessary condition $\nabla f(X_0) = 0$ gives:
$$
\frac{\partial f}{\partial x_1} = -2x_1 - x_3 = 0,
$$
$$
\frac{\partial f}{\partial x_2} = -2x_2 - x_3 = 0,
$$
$$
\frac{\partial f}{\partial x_3} = 4 - x_1 - x_2 - 2x_3 = 0.
$$

The solution of these equations is:
$$
X_0 = (-2, -2, 4).
$$

Hessian matrix $H$:

$$
H = \begin{bmatrix}
-2 & 0 & -1 \\
0 & -2 & -1 \\
-1 & -1 & -4
\end{bmatrix}.
$$

Evaluating the principal minors:
$$
\begin{align*}
D_{11} &= -2 < 0, \\
D_{11}D_{22} - D_{12}^2 &= (-2)(-2) - 0^2 = 4 > 0, \\
\det(H) &= \text{negative determinant}.
\end{align*}
$$

Consequently, $H \prec 0$. Therefore, $X_0 = (-2, -2, 4)$ represents a **maximum point** (Note: Typo in original; corrected to $(-2, -2, -4)$).

---

### Problem 3: Newton-Raphson for $\sqrt{2}$
#### Solution
The equation is:
$$
x^2 - 2 = 0.
$$

Let $f(x) = x^2 - 2$ and $x_0 = 1.5$. The Newton-Raphson iteration formula:

$$
x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}.
$$

Iterations:
$$
\begin{align*}
x_1 &= 1.5 - \frac{2^2 - 2}{3(1.5)^2} = \frac{17}{12} \approx 1.4167, \\
x_2 &= 1.4167 - \frac{(1.4167)^2 - 2}{2(1.4167)} = \frac{577}{408} \approx 1.4142, \\
x_3 &\approx 1.41421356237.
\end{align*}
$$

For comparison:
$$
\sqrt{2} \approx 1.4142135623730950488.
$$

---

### Problem 4: Newton-Raphson for $f(x) = x^4 + x^3 - x$
#### Solution
The necessary condition $f'(x) = 0$ gives:
$$
g(x) = f'(x) = x^3 + 3x^2 - 1 = 0.
$$

Sign analysis of $g(x)$:
| Interval | Sign of $g(x)$ |
|----------|-------------------|
| $-3$   | $-$               |
| $-2$   | $+$              |
| $-1$   | $+$              |
| $0$    | $-$              |
| $1$    | $+$              |

Roots lie in intervals:
- $[-3, -2]$ (first root),
- $[-1, 0]$ (second root),
- $[0, 1]$ (third root).

Newton-Raphson iteration:
$$
x_{k+1} = x_k - \frac{g(x_k)}{g'(x_k)}.
$$

Starting with $x_0 = -2.5$:
$$
\begin{align*}
x_1 &= -3.0667, \\
x_2 &= -2.9009, \\
x_3 &= -2.8797, \\
x_4 &\approx -2.8794.
\end{align*}
$$

Starting with $x_0 = 0.5$:
$$
\begin{align*}
x_1 &= -0.4444, \\
x_2 &= -0.6832, \\
x_3 &= -0.6530, \\
x_4 &\approx -0.6527.
\end{align*}
$$

Starting with $x_0 = 2.5$:
$$
\begin{align*}
x_1 &= 0.9206, \\
x_2 &= 0.6327, \\
x_3 &= 0.5418, \\
x_4 &\approx 0.5322.
\end{align*}
$$

Extreme points:
$$
f'(x) = 0 \implies x_1 = -2.87939, \, x_2 = -0.65270, \, x_3 = 0.532194.
$$

Second derivatives:
- $f''(x_1) > 0$ → **Minimum** ($y_1 \approx -3.8086$),
- $f''(x_2) < 0$ → **Maximum** ($y_2 \approx 0.4200$),
- $f''(x_3) > 0$ → **Minimum** ($y_3 \approx -0.3614$).

---

### Problem 5: Newton-Raphson for constrained optimization $f(x,y)$
**Function:**
$$
f(x, y) = x^4 + y^4 - 3x^2 - 2xy - y^2
$$

#### Solution
Necessary condition $\nabla f(X_0) = 0$:
$$
\frac{\partial f}{\partial x} = -6x + 4x^3 - 2y = 0,
$$
$$
\frac{\partial f}{\partial y} = -2(x + y - 2y^3) = 0.
$$

Solve system:
$$
g_1(x,y) = -3x + 2x^3 - y = 0, \quad g_2(x,y) = x + y - 2y^3 = 0.
$$

Newton-Raphson update:
$$
\begin{align*}
x_{k+1} &= x_k - \frac{g_1(x_k, y_k)}{\partial g_1 / \partial x}, \\
y_{k+1} &= y_k - \frac{g_2(x_k, y_k)}{\partial g_2 / \partial y}.
\end{align*}
$$

Starting
