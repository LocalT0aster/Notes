# Introduction to Optimization
## Week 6: Problems Sheet 5

---

### Problem 1
**Construct the dual from the following problem:**

Maximize:
$$
z(x_1, x_2) = 2x_1 + 7x_2
$$

Subject to:
$$
\begin{cases}
-2x_1 + 3x_2 \leq 14, \\
x_1 + x_2 \leq 8, \\
x_1 \geq 0, \\
x_2 \geq 0.
\end{cases}
$$

**Using the graphical method find the primal and dual solutions.**

---

#### Solution
The dual problem is constructed as follows:

Minimize:
$$
w(y_1, y_2) = 14y_1 + 8y_2
$$

Subject to:
$$
\begin{cases}
-2y_1 + y_2 \geq 2, \\
3y_1 + y_2 \geq 7, \\
y_1 \geq 0, \\
y_2 \geq 0.
\end{cases}
$$

**Primal Solution Space:**
The feasible region for the primal problem is plotted with constraints:
- $-2x_1 + 3x_2 = 14$
- $x_1 + x_2 = 8$

Vertices (A, B, C):
- A: $(0, 0)$
- B: $(6, 2)$ from intersection of $x_1=0$ and $x_1 + x_2 = 8$
- C: $(2, 6)$ from intersection of $-2x_1 + 3x_2 = 14$ and $x_1 + x_2 = 8$

Optimal solution:
$$
(x_1, x_2) = (2, 6), \quad F(2, 6) = 46
$$

**Dual Solution Space:**
The feasible region for the dual problem is plotted with constraints:
- $-2y_1 + y_2 = 2$
- $3y_1 + y_2 = 7$

Vertices (A, B):
- A: $(0, 0)$
- B: $(1, 4)$ from intersection of both lines

Optimal solution:
$$
(y_1, y_2) = (1, 4), \quad w(1, 4) = 46
$$

---

### Problem 2
**Construct the dual from the following problem:**

Minimize:
$$
z(x_1, x_2) = -2x_1 - 3x_2
$$

Subject to:
$$
\begin{cases}
-4x_1 + 2x_2 \geq 4, \\
x_1 + x_2 \geq 6, \\
x_1 \geq 0, \\
x_2 \geq 0.
\end{cases}
$$

**Using the graphical method find the primal and dual solutions.**

---

#### Solution
The dual problem is constructed as follows:

Maximize:
$$
w(y_1, y_2) = 4y_1 + 6y_2
$$

Subject to:
$$
\begin{cases}
-4y_1 + y_2 \leq -2, \\
2y_1 + y_2 \leq -3, \\
y_1 \geq 0, \\
y_2 \geq 0.
\end{cases}
$$

**Primal Solution Space:**
The feasible region for the primal problem is unbounded (no finite solution exists).

**Dual Solution Space:**
Constraints:
- $-4y_1 + y_2 = -2$
- $2y_1 + y_2 = -3$

No intersection point within non-negative constraints, so the feasible set is empty.

---

### Problem 3
**Construct the dual from the following problem:**

Maximize:
$$
z(x_1, x_2, x_3) = x_1 + 2x_2 - x_3
$$

Subject to:
$$
\begin{cases}
-x_1 + 4x_2 - 2x_3 \leq 12, \\
x_1 + x_2 + 2x_3 \leq 17, \\
2x_1 - x_2 + 2x_3 = 4, \\
x_1 \geq 0, \\
x_2 \geq 0, \\
x_3 \geq 0.
\end{cases}
$$

**Using the M-method find the primal and dual solutions.**

---

#### Solution
The dual problem is constructed as follows:

Minimize:
$$
w(y_1, y_2, y_3) = 12y_1 + 17y_2 + 4y_3
$$

Subject to:
$$
\begin{cases}
-y_1 + y_2 + 2y_3 \geq 1, \\
4y_1 + y_2 - y_3 \geq 2, \\
-2y_1 + 2y_2 + 2y_3 \geq -1, \\
y_1 \geq 0, \\
y_2 \geq 0.
\end{cases}
$$

**Simplex Method Iterations (M-method):**
*(Note: Full tableau details omitted for brevity; key results provided.)*

Optimal solution from iterations:
$$
(x_1, x_2, x_3) = (14, 15, 2), \quad z_{\text{max}} = -400.
$$

---

### Problem 4
**Using the "Advanced Simplex Method" solve:**

Maximize:
$$
z(x_1, x_2, x_3, x_4, x_5, x_6) = 9x_1 + 10x_2 + 16x_3
$$

Subject to:
$$
\begin{cases}
18x_1 + 15x_2 + 12x_3 + x_4 = 360, \\
6x_1 + 4x_2 + 8x_3 + x_5 = 192, \\
5x_1 + 3x_2 + 3x_3 + x_6 = 180, \\
x_i \geq 0 \quad (i=1,\ldots,6).
\end{cases}
$$

---

#### Solution
**Iteration Steps:**
- Initial tableau: Basic variables $X_B^0 = (x_4, x_5, x_6)$
- Entering variable: $P_3$ (due to $\min(-9, -10, -16) = -16$)
- Leaving variable: $x_5$

**Iteration 1:**
Basic variables: $(x_4, x_3, x_6)$

Optimal solution:
$$
(x_1, x_2, x_3, x_4, x_5, x_6) = (0, 8, 20, 0, 0, 96), \quad z_{\text{max}} = 400.
$$

---

### Problem 5
**Using the "Advanced Simplex Method" solve:**

Maximize:
$$
z(x_1, x_2, x_3, x_4, x_5, x_6) = 8x_2 + 7x_4 + x_6
$$

Subject to:
$$
\begin{cases}
x_1 - 2x_2 - 3x_4 - 2x_6 = 12, \\
4x_2 + x_3 - 4x_4 - 3x_6 = 12, \\
5x_2 + 5x_4 + x_5 + x_6 = 25, \\
x_i \geq 0 \quad (i=1,\ldots,6).
\end{cases}
$$

---

#### Solution
**Iteration Steps:**
- Initial tableau: Basic variables $X_B^0 = (x_1, x_3, x_5)$
- Entering variable: $P_2$ (due to $\min(-8, -7, -1) = -8$)
- Leaving variable: $x_3$

**Iteration 1:**
Basic variables: $(x_1, x_2, x_5)$

Optimal solution:
$$
(x_1, x_2, x_3, x_4, x_5, x_6) = (23, 4, 0, 1, 0, 0), \quad z_{\text{max}} = 39.
$$
