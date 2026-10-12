Here’s the cleaned and structured Markdown version of your PDF text:

---

# **Introduction to Optimization**
## **Week 2**

### **Problem 1: Solve the following LPP using the Simplex method.**

**Objective:**
Maximize
$$
F(x_1, x_2, x_3) = 9x_1 + 10x_2 + 16x_3
$$

**Constraints:**
$$
\begin{align*}
&18x_1 + 15x_2 + 12x_3 \leq 360, \\
&6x_1 + 4x_2 + 8x_3 \leq 192, \\
&5x_1 + 3x_2 + 3x_3 \leq 180, \\
&x_1, x_2, x_3 \geq 0.
\end{align*}
$$

---

### **Solution:**

#### **Step 1: Rewrite in Standard Form**
Convert inequalities to equalities by introducing slack variables $s_1, s_2, s_3$.

**Objective:**
Maximize
$$
F(x_1, x_2, x_3) = 9x_1 + 10x_2 + 16x_3
$$

**Constraints:**
$$
\begin{align*}
&18x_1 + 15x_2 + 12x_3 + s_1 = 360, \\
&6x_1 + 4x_2 + 8x_3 + s_2 = 192, \\
&5x_1 + 3x_2 + 3x_3 + s_3 = 180, \\
&x_1, x_2, x_3, s_1, s_2, s_3 \geq 0.
\end{align*}
$$

---

#### **Initial Simplex Table**

| Basic | $z$       | $s_1$ | $s_2$ | $s_3$ |
|-------|--------------|-----------|-----------|-----------|
| $x_1$ | $-9$       | 18        | 6         | 5         |
| $x_2$ | $-10$      | 15        | 4         | 3         |
| $x_3$ | $-16$      | 12        | 8         | 3         |
| $s_1$ | $0$      | 1         | 0         | 0         |
| $s_2$ | $0$      | 0         | 1         | 0         |
| $s_3$ | $0$      | 0         | 0         | 1         |

**Solution:** $[0, 360, 192, 180]$

---

#### **Iteration 1: Entering Variable $x_3$, Leaving Variable $s_2$**

Compute $\theta = \frac{b_i}{a_{i3}}$:
$$
\theta = \min\left(\frac{360}{12}, \frac{192}{8}, \frac{180}{3}\right) = 24.
$$

**New Basic Solution:**
- $x_3$ enters, $s_2$ leaves.

| Basic | $z$       | $s_1$ | $x_3$ | $s_3$ |
|-------|--------------|-----------|-----------|-----------|
| $x_1$ | $-9 + 4$   | 18        | 6/8      | 5         |
| $x_2$ | $-10 + 2$  | 15        | 4/8      | 3         |
| $s_1$ | $0$      | 1         | 0         | 0         |
| $x_3$ | $0$      | 12        | 1         | 3         |
| $s_2$ | $0$      | 0         | 8/8 = 1   | 0         |
| $s_3$ | $0$      | 0         | 0         | 1         |

**Solution:** $[72, 24, 192 - 24 \cdot 3, 108]$

---

#### **Iteration 2: Entering Variable $x_2$, Leaving Variable $s_1$**

Compute $\theta = \min\left(\frac{72}{9}, \frac{24}{\frac{1}{2}}, \frac{108}{\frac{3}{2}}\right) = 8$.

**New Basic Solution:**
- $x_2$ enters, $s_1$ leaves.

| Basic | $z$       | $x_2$   | $x_3$ | $s_3$ |
|-------|--------------|-------------|-----------|-----------|
| $x_1$ | $9$      | $\frac{5}{3}$ | $\frac{11}{3}$ | $\frac{3}{4} - \frac{1}{2}$ |
| $x_2$ | $0$      | $1$     | $0$   | $\frac{3}{2}$ |
| $s_1$ | $0$      | $0$     | $0$   | $-\frac{1}{6}$ |
| $x_3$ | $0$      | $0$     | $1$   | $0$    |
| $s_2$ | $-3/2$   | $\frac{5}{3}$ | $\frac{-17}{3}$ | $\frac{4}{3}$ |
| $s_3$ | $0$      | $0$     | $0$   | $1$    |

**Solution:** $[400, 8, 20, 96]$

---

#### **Optimal Solution:**
$$
x_1 = 0, \quad x_2 = 8, \quad x_3 = 20.
$$
Maximized value of $F(x) = 400$.

---

### **Problem 2: Solve the following LPP using Simplex method.**

**Objective:**
Maximize
$$
F(x_1, x_2, x_3, x_4, x_5, x_6) = 2x_1 + 3x_2 - x_4
$$

**Constraints:**
$$
\begin{align*}
&2x_1 - x_2 - 2x_4 + x_5 = 16, \\
&3x_1 + 2x_2 + x_3 - 3x_4 = 18, \\
&-x_1 + 3x_2 + 4x_4 + x_6 = 24, \\
&x_i \geq 0.
\end{align*}
$$

---

### **Solution:**

#### **Iteration 1:**
Basic variables: $x_5, x_3, x_2$.

| Basic | $z$       | $x_5$   | $x_3$ | $x_2$ |
|-------|--------------|-------------|-----------|-----------|
| $x_1$ | $-3$       | $\frac{5}{3}$ | $\frac{11}{3}$ | $-\frac{1}{3}$ |
| $x_2$ | $0$      | $0$     | $0$   | $1$    |
| $x_3$ | $9$      | $\frac{-5}{3}$ | $1$   | $-\frac{2}{3}$ |

**Solution:** $[0, 16, 18, 24]$

---

#### **Iteration 2:**
Basic variables: $x_5, x_1, x_2$.

| Basic | $z$       | $x_5$   | $x_1$ | $x_2$ |
|-------|--------------|-------------|-----------|-----------|
| $x_1$ | $0$      | $\frac{4}{3}$ | $1$   | $-\frac{1}{3}$ |
| $x_2$ | $0$      | $0$     | $0$   | $1$    |

**Solution:** $[282/11, 254/11, 6/11, 90/11]$

---

#### **Optimal Solution:**
$$
(x_1, x_2, x_3, x_4, x_5, x_6) = \left(\frac{
