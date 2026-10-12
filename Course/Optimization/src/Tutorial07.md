# Tutorial 6: Interior-Point Algorithm
**Dr. Ramil Nasibullin**
*Email:* nasibullinramil@gmail.com
*Innopolis University*
*Course of Introduction to Optimization*
*Fall, 2025*

---

## Problem 1

### Objective and Constraints
Maximize:
$$
Z = 2x_1 + 5x_2 + 7x_3
$$

Subject to:
$$
x_1 + 2x_2 + 3x_3 = 6
$$
and
$$
x_1, x_2, x_3 \geq 0
$$

### Tasks
1. Graph the feasible region.
2. Find the gradient of the objective function and project it onto the feasible region.
3. Starting from $(x_1, x_2, x_3) = (1, 1, 1)$, perform two iterations of the interior-point algorithm.

---

#### Iteration 1
**Initial trial solution:** $(x_1, x_2, x_3) = (1, 1, 1)$

Define:
$$
D = \begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

Matrix $A$ and vector $c$:
$$
A =
\begin{bmatrix}
1 & 2 & 3
\end{bmatrix},
$$
$$
c =
\begin{bmatrix}
5 \\ 7
\end{bmatrix}
$$

**Step 1:** Compute $e = AD$:
$$
e = \begin{bmatrix} 1 & 2 & 3 \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 2 & 3 \end{bmatrix}
$$

**Step 2:** Compute $AAT$:
$$
AAT = (1)^2 + (2)^2 + (3)^2 = 14
$$

Compute $Dc$:
$$
Dc =
\begin{bmatrix}
5 \\ 7
\end{bmatrix} = \begin{bmatrix} 5 \\ 7
\end{bmatrix}
$$

**Step 3:** Compute $P = I - A e^T / (AAT)$:
$$
Pe = \frac{1}{14} \begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix} \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} - \begin{bmatrix} 2 \\ 5 \\ 7 \end{bmatrix} = \frac{1}{14} \begin{bmatrix}
1 \\ 2 \\ 3
\end{bmatrix} - \begin{bmatrix} 2 \\ 5 \\ 7
\end{bmatrix}
$$

$$
P =
\begin{bmatrix}
0.92857143 & -0.14285714 & -0.21428571 \\
-0.14285714 & 0.71428571 & -0.42857143 \\
-0.21428571 & -0.42857143 & 0.35714286
\end{bmatrix}
$$

Compute $cp$:
$$
cp = Pe =
\begin{bmatrix}
0.92857143 \times 1 + (-0.14285714) \times 2 + (-0.21428571) \times 3 \\
-0.14285714 \times 1 + 0.71428571 \times 2 + (-0.42857143) \times 3 \\
-0.21428571 \times 1 + (-0.42857143) \times 2 + 0.35714286 \times 3
\end{bmatrix} =
\begin{bmatrix}
0.28571429 \\
-0.07142857 \\
-0.35714286
\end{bmatrix}
$$

**Step 4:** Identify the largest absolute value in $cp$:
$$
\nu = 0.35714286
$$

Compute updated solution:
$$
x =
\begin{bmatrix}
1 + (0.92857143 \times 1) / 0.35714286 \\
1 + (-0.14285714 \times 1) / 0.35714286 \\
1 + (-0.21428571 \times 1) / 0.35714286
\end{bmatrix} \approx
\begin{bmatrix}
1.48 \\
0.88 \\
\end{bmatrix}
$$

**Updated trial solution:**
$$
(x_1, x_2, x_3) = (1.48, 0.88)
$$

---

#### Iteration 2

**Initial trial solution:** $(x_1, x_2, x_3) = (1.48, 0.88)$

Define:
$$
D =
\begin{bmatrix}
0.4 & 0 & 0 \\
0 & 1.48 & 0 \\
0 & 0 & 0.88
\end{bmatrix}
$$

Compute $e = AD$:
$$
e =
\begin{bmatrix}
0.4 \times 1 + 2 \times 0 + 3 \times 0 \\
0 \times 1 + 2 \times 1.48 + 3 \times 0 \\
0 \times 1 + 2 \times 0 + 3 \times 0.88
\end{bmatrix} = (0.4, 2.96, 2.64)
$$

Compute $AAT$:
$$
AAT = (0.4)^2 + (2.96)^2 + (2.64)^2 = 15.8912
$$

Compute $Dc$:
$$
Dc =
\begin{bmatrix}
0 \times 5 + 1.48 \times 7 \\
0 \times 5 + 0.88 \times 7
\end{bmatrix} = (10.36, 6.16)
$$

Compute $P = I - A e^T / (AAT)$:
$$
Pe =
\begin{bmatrix}
0.98993153 & -0.07450665 & -0.06645187 \\
-0.07450665 & 0.44865083 & -0.49174386 \\
-0.06645187 & -0.49174386 & 0.56141764
\end{bmatrix}
$$

Compute $cp$:
$$
cp =
\begin{bmatrix}
0.23126863 \\
-0.23373339 \\
-0.16874748
\end{bmatrix}
$$

**Step 4:** Largest absolute value in $cp$:
$$
\nu = 0.23373339
$$

Compute updated solution:
$$
x =
\begin{bmatrix}
1 + (0.98993153 \times 1) / 0.23373339 \\
1 + (-0.07450665 \times 1) / 0.23373339 \\
1 + (-0.06645187 \times 1) / 0.23373339
\end{bmatrix} \approx
\begin{bmatrix}
1.59367289 \\
0.4 \\
0.56682059
\end{bmatrix}
$$

**Updated trial solution:**
$$
(x_1, x_2, x_3) = (2.358635, 0.352)
$$

---

## Problem 2

### Objective and Constraints
Maximize:
$$
z = 2x_1 + 5x_2
$$

Subject to:
$$
5x_1 + 4x_2 \leq 12
$$
$$
2x_1 + 7x_2 \leq 10
$$
and
$$
x_1, x_2 \geq 0
$$

### Tasks
1. Graph the feasible region.
2. Find the gradient of the objective function and project it onto the feasible region.
3. Starting from $(x_1, x_2) = (1, 1)$, perform two iterations of the interior-point algorithm.

---

#### Iteration 1

**Initial trial solution:** $(x_1, x_2, x_3, x_4) = (1, 1, 3, 1)$

Define:
$$
D =
\begin{bmatrix}
1 & 0 & 3 & 0 \\
0 & 1 & 0 & 1
\end{bmatrix}
$$

Matrix $A$ and vector $c$:
$$
A =
\begin{bmatrix}
5 & 4 & 1 & 0 \\
