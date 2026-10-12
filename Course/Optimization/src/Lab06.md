# Introduction to Optimization
## Week 7: Problem Sheet 6

---

### **Problem 1. Solve the following LPP using an Interior-Point Algorithm**

**Maximize and minimize**
$$
F(x_1, x_2) = x_1 + x_2
$$

**Subject to:**
$$
\begin{cases}
2x_1 + 4x_2 \leq 16 \\
x_1 + 3x_2 \geq 9 \\
x_1 \geq 0 \\
x_2 \geq 0
\end{cases}
$$

---

#### **Solution**

Using constraints (1)-(4), the feasible solution space is visualized as follows:

- Boundary points:
  - $x_2 = 0$: $x_1 = 8$
  - $x_1 = 0$: $x_2 = 3$

The minimal and maximal values of $F$ are known from Lab 2, Problem 2:
- Minimal value: $F(0, 3) = 0 + 3 = 3$
- Maximal value: $F(6, 1) = 6 + 1 = 7$

Rewriting the problem in equality form:

**Maximize and minimize**
$$
F(x_1, x_2) = x_1 + x_2 + 0x_3 + 0x_4
$$

**Subject to:**
$$
\begin{cases}
2x_1 + 4x_2 + x_3 = 16 \\
x_1 + 3x_2 - x_4 = 9 \\
x_1 \geq 0, \quad x_2 \geq 0, \quad x_3 \geq 0, \quad x_4 \geq 0
\end{cases}
$$

---

#### **Iteration 1**
Initial interior trial solution:
$$
(x_1, x_2, x_3, x_4) = \left(\frac{7}{2}, \frac{7}{2}, 1, 2\right)
$$

**Matrix $D$:**
$$
D =
\begin{bmatrix}
\frac{1}{2} & 0 & 0 & 0 \\
0 & \frac{7}{2} & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 2
\end{bmatrix}
$$

**Matrix $A$:**
$$
A =
\begin{bmatrix}
2 & 4 & 1 & 0 \\
1 & 3 & 0 & -1
\end{bmatrix}
$$

**Compute $e = AD$ and $cD$:**

- $e$:
$$
e =
\begin{bmatrix}
\frac{7}{2} \\
\frac{1}{2} \\
0 \\
\frac{1}{2}
\end{bmatrix}
$$

- $cD$:
$$
cD =
\begin{bmatrix}
\frac{7}{2} & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 2
\end{bmatrix}
$$
(Note: The original matrix seems misaligned; corrected as $c = [1, 1, 0, 0]$, so $cD$ is derived from $Dc$.)

**Compute $P = I - A^T (AA^{-T})A$ and $cp = Pe$:**

- $AA^T$:
$$
AA^T =
\begin{bmatrix}
2^2 + 4^2 & 2 \cdot 1 + 4 \cdot 3 \\
1 \cdot 2 + 3 \cdot 4 & 1^2 + 3^2
\end{bmatrix} =
\begin{bmatrix}
20 & 14 \\
14 & 10
\end{bmatrix}
$$

- $F = AA^T$, $FI = (AA^T)^{-1}$:
$$
F^{-1} =
\frac{1}{20 \cdot 10 - 14^2}
\begin{bmatrix}
10 & -14 \\
-14 & 20
\end{bmatrix} =
\frac{1}{-4}{[}-5/2, \, 7 \\
\, 7, \, -5/2]
$$

- $H = (AA^T)^{-1} AA^T$:
$$
H =
\begin{bmatrix}
-5/2 & 7 \\
7 & -5/2
\end{bmatrix}
$$
(Note: Likely a typo in the original; corrected to standard inverse.)

- $P = I - H$:
$$
P =
\begin{bmatrix}
1 + \frac{5}{2} & -7 \\
-7 & 1 + \frac{5}{2}
\end{bmatrix}^{-1} \text{ (Corrected for clarity)}
$$

**Compute $cp$:**
$$
cp = Pe =
\begin{bmatrix}
0.256627 \\
-0.00191 \\
-0.229844 \\
0.0541131
\end{bmatrix}
$$

**Identify the most negative component:**
$$
\nu = 0.229844
$$

**Update trial solution $x$:**
$$
e + \frac{\alpha}{\nu} cp =
\begin{bmatrix}
\frac{7}{2} \\
1 \\
1 \\
2
\end{bmatrix} +
\frac{0.5}{0.229844} \cdot
\begin{bmatrix}
0.256627 \\
-0.00191 \\
-0.229844 \\
0.0541131
\end{bmatrix} =
\begin{bmatrix}
x_1 \\
x_2 \\
x_3 \\
x_4
\end{bmatrix}
$$

**Next trial solution:**
$$
(x_1, x_2, x_3, x_4) = (0.779132, 3.48543, 0.5, 2.23543)
$$

---

#### **Iteration 2-5**
The following solutions were obtained through successive iterations:

| Iteration | $x$ Values                     |
|-----------|------------------------------------|
| 1         | $[0.779132, \, 3.48543, \, 0.5, \, 2.23543]$ |
| 2         | $[1.8806, \, 2.9972, \, 0.25, \, 1.8722]$   |
| 3         | $[3.8084, \, 2.0426, \, 0.2130, \, 0.9361]$   |
| 4         | $[4.7870, \, 1.5603, \, 0.1846, \, 0.4681]$   |
| 5 (Final) | $[5.999994, \, 1.000003, \, \approx 0, \, \approx 0]$ |

---

### **Problem 2. Solve the following LPP using an Interior-Point Algorithm**

**Maximize**
$$
F(x_1, x_2, x_3) = 9x_1 + 10x_2 + 16x_3
$$

**Subject to:**
$$
\begin{cases}
18x_1 + 15x_2 + 12x_3 \leq 360 \\
6x_1 + 4x_2 + 8x_3 \leq 192 \\
5x_1 + 3x_2 + 3x_3 \leq 180 \\
x_1, x_2, x_3 \geq 0
\end{cases}
$$

---

#### **Solution**

Rewriting in standard form (with slack variables $s_1, s_2, s_3$):

**Maximize**
$$
F(x_1, x_2, x_3) = 9x_1 + 10x_2 + 16x_3
$$

**Subject to:**
$$
\begin{cases}
18x_1 + 15x_2 + 12x_3 + s_1 = 360 \\
6x_1 + 4x_2 + 8x_3 + s_2 = 192 \\
5x_1 + 3x_2 + 3x_3 + s_3 = 180 \\
x_i, s_i \geq 0
\end{cases}
$$

**Initial interior solution:**
$$
(x_1, x_2, x_3, s_1, s_2, s_3) = (1, 1, 1, 315, 174, 169)
$$

---

#### **Iteration Results**
| Iteration | $x$ Values                                      |
|-----------|----------------------------------------------------|
| 1         | $[3.7980, \, 4.1264, \, 6.0200, \, 157.5, \, 5.1466, \, 10.7145]$ |
| 2         | $[4.1932, \, 78.75, \, \ldots]$                     |
*(Note: Iteration details omitted

Here is the cleaned and structured Markdown version of your PDF text:

# Phase II Problem Statement

**Objective:**
Maximize
```
F(x_1, x_2) = x_1 + x_2
```

**Subject to:**

| Constraint | Equation                                                                 |
|------------|--------------------------------------------------------------------------|
| (1)        | 2/3 x_1 + s_1 + 4/3 s_3 = 4                                                |
| (2)        | -14/3 x_1 + s_2 + 2/3 s_3 = 2                                             |
| (3)        | 1/3 x_1 + x_2 - 1/3 s_3 = 3                                              |

**Constraints:**
- $x_1 \geq 0$
- $x_2 \geq 0$
- $s_1 \geq 0$
- $s_2 \geq 0$
- $s_3 \geq 0$

---

### Initial Iteration (Iteration 0)

#### Basic Feasible Solution:
| Variable | Value       |
|----------|-------------|
| x_1       | -1          |
| s_1       | 2/3         |
| s_2       | -14/3       |
| x_2       | 1/3         |

| Variable | Value |
|----------|-------|
| x_1       | -1    |
| x_2       | 0     |
| s_1       | 0     |
| s_2       | 0     |
| s_3       | 4/3   |

#### Solution Vector:
```
z = [0, 4, 2, 3]
```

#### Reduced Costs (cᵢ):
```
ci = [0, 0, 1]
```

---

### Iteration Update
Using the formula:
```
z_new = z_old + (0 · x_3 Row + 0 · x_4 Row + 1 · x_2 Row)
where z_old = [0, 0, 0, 0, 0, 0, -1]
```

---

### Iteration 1

#### New Basic Solution:
| Variable | Value       |
|----------|-------------|
| x_3       | -2/3        |
| s_1       | 2/3         |
| s_2       | -14/3       |
| x_2       | 1/3         |

| Variable | Value       |
|----------|-------------|
| x_1       | 0           |
| x_2       | 1           |
| s_1       | 1           |
| s_2       | 0           |
| s_3       | -1/5        |

| Variable | Value       |
|----------|-------------|
| x_1       | 0           |
| x_2       | 0           |
| s_1       | 3/2         |
| s_2       | 7           |
| s_3       | -1/2        |

| Variable | Value       |
|----------|-------------|
| x_1       | -1/5        |
| x_2       | 4/3         |
| s_1       | 2/3         |
| x_2       | 17/15       |
| s_3       | 2           |

#### Solution Vector:
```
z = [3, 4, 2, 3, 7, 6, 30, 1]
```

**Optimal Solution:**
- Entering Variable: $x_1$
- Leaving Variable: $x_3$

#### Final Optimal Values:
$(x_1, x_2) = (6, 1)$

#### Objective Function Value:
```
F(x_1, x_2) = 7
```

---
```
