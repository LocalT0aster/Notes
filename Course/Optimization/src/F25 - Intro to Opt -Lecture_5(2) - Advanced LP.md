# Lecture 5 (Part 2): Advanced Linear Programming

**Instructor:** Dr. Mohammad Reza Bahrami
**University:** Innopolis University
**Course:** Introduction to Optimization
**Semester:** Fall, 2025

---

## Content

### Advanced Linear Programming Topics
1. Simplex Method Fundamentals
2. Revised Simplex Method
3. Bounded-Variables Algorithm

---

## Simplex Method Fundamentals

In linear programming, the feasible solution space forms a convex set if the line segment joining any two distinct feasible points also lies within the set.

An **extreme point** of this convex set is a feasible point that cannot lie on a line segment joining any other two distinct feasible points in the set. These extreme points are equivalent to corner points, as previously defined.

![Figure illustrating convex sets](Note: Description omitted for brevity; assume it shows (a) a convex set with six extreme points and (b) a non-convex set.)

The graphical solution of an LP demonstrates that the optimal solution is always associated with a feasible extreme (corner) point of the solution space. This aligns intuitively because any feasible point in the LP’s solution space can be expressed as a convex combination of its extreme points.

For example, consider the convex set (a) from the figure above. A convex combination of the extreme points $X_1, X_2, \dots, X_6$ identifies any feasible point $X$ as:

$$
X = \alpha_1 X_1 + \alpha_2 X_2 + \alpha_3 X_3 + \alpha_4 X_4 + \alpha_5 X_5 + \alpha_6 X_6,
$$

where $\sum_{i=1}^6 \alpha_i = 1$ and $\alpha_i \geq 0$.

This shows that a finite number of extreme points completely define the infinite set of feasible solutions. This principle is foundational to the **simplex method**.

---

## From Extreme Points to Basic Solutions

### Problem Representation
The general LP problem can be expressed in matrix form as:

- $X$ = an $n$-vector representing variables.
- $A$ = $(m \times n)$ constraint coefficient matrix.
- $b$ = column vector of right-hand side values.
- $C$ = $n$-vector of objective function coefficients.

The problem is written as:
$$
\text{Maximize or minimize } z = C^T X,
$$
subject to:
$$
AX = b, \quad X \geq 0.
$$

**Note:** The last $m$ elements of $X^T$ represent the initial basic variables. Thus, the rightmost $m$ columns of $A$ form an identity matrix $I$.

### Basic Solution Definition

A **basic solution** to $AX = b$ is obtained by setting $n - m$ variables to zero and solving for the remaining $m$ unknowns, provided a unique solution exists.

The theory of linear programming establishes:
> Extreme points of $\{X \mid AX = b, X \geq 0\}$ are equivalent to basic solutions of $AX = b$.

Thus, basic solutions provide all necessary information to determine the optimal LP solution. Non-negativity constraints ($X \geq 0$) restrict the search to feasible basic solutions.

---

### Formal Definition and Basis

The system $AX = b$ can be written in vector form as:

$$
\sum_{j=1}^n P_j x_j = b,
$$

where $P_j$ is the $j$-th column of matrix $A$.

A subset of $m$ vectors forms a **basis** $B$ if they are linearly independent, making $B$ nonsingular. The basic variables' vector $X_B$ satisfies:

$$
B X_B = b.
$$

Using the inverse $B^{-1}$, the associated basic solution is:

$$
X_B = B^{-1} b.
$$

If $B^{-1} b \geq 0$, then $X_B$ is feasible. The remaining $n - m$ variables are nonbasic and set to zero.

---

### Example: Basic Solutions

Consider the system:
$$
\begin{align*}
x_1 + 3x_2 - x_4 &= 2, \\
-2x_1 - 2x_2 - 2x_3 &= -8.
\end{align*}

**Summary of Results:**

| Basis $B$       | $B X_B = b$                          |
|-------------------|----------------------------------------|
| $(P_1, P_2)$    | $\begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 7 \\ -8 \end{bmatrix}$ (Infeasible) |
| $(P_1, P_3)$    | $\begin{bmatrix} x_1 \\ x_3 \end{bmatrix} = \begin{bmatrix} 4 \\ -2 \end{bmatrix}$ (Infeasible) |
| $(P_2, P_3)$    | $\begin{bmatrix} x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 4 \\ 2 \end{bmatrix}$ (Feasible) |

---

## Generalized Simplex Tableau in Matrix Form

### Problem Setup
The LP problem can be rewritten as:

$$
\begin{bmatrix}
0 \\
- C^T
\end{bmatrix}
=
\begin{bmatrix}
A & I_n \\
0 & 0
\end{bmatrix}
X,
$$

where $I_n$ is the identity matrix of size $n$.

Given a feasible basis $B$, the basic variables' vector $X_B = B^{-1} b$. The objective function value is:

$$
z = C^T X_B = C^T B^{-1} b.
$$

---

### Simplex Tableau Construction

The complete tableau in matrix form is derived from original equations as:

$$
\begin{bmatrix}
C_B & -c \\
B^{-1} A & 0 \\
\end{bmatrix}
\begin{bmatrix}
X_B \\
z \\
\end{bmatrix}
=
\begin{bmatrix}
- c^T B^{-1} b \\
b \\
\end{bmatrix}.
$$

For each nonbasic variable $x_j$, the tableau column is:

| Basic | $x_j$ | Solution ($z$) |
|-------|--------|------------------|
| $C_B B^{-1} P_j - c_j$ | $C_B B^{-1} b$ | $B^{-1} P_j$ |

---

### Example: Constructing the Tableau

**Problem:**
Maximize $z = x_1 + 4x_2 + 7x_3 + 5x_4$, subject to:
$$
\begin{align*}
2x_1 + x_2 + 2x_3 + 4x_4 &= 10, \\
3x_1 - x_2 - 2x_3 + 6x_4 &= 5,
\end{align*}
$$
with $x_i \geq 0$.

**Initial Basis:** $B = (P_1, P_2)$

- Basic variables: $X_B = [x_1, x_2]^T$
- Objective coefficients for basis: $C_B = [1, 4]$

Compute $B^{-1}$:

$$
\begin{bmatrix}
2 & 1 \\
3 & -1
\end{bmatrix}^{-1} =
\frac{1}{-5} \begin{bmatrix} -1 & -1 \\ -3 & 2 \end{bmatrix} =
\begin{bmatrix} 0.2 & 0.2 \\ 0.6 & -0.4 \end{bmatrix}.
$$

**Compute $X_B$:**

$$
X_B = B^{-1} b = \begin{bmatrix} 0.2 & 0.2 \\ 0.6 & -0.4 \end{bmatrix} \begin{bmatrix} 10 \\ 5 \end{bmatrix} = \begin{bmatrix} 3 \\ 2 \end{bmatrix}.
$$

**Tableau Columns:**

| Basic | $x_1$ | $x_2$ | $x_3$ | $x_4$ |
|-------|--------|--------|--------|--------|
| **$z$ Row:** | $0$   | $0$   | $1$  | $-3$ |
| **Solution ($X_B$):** | $3$   | $2$   | -      | -      |

**Objective Function Value:**

$$
z = C_B X_B = [1,4] \begin{bmatrix} 3 \\ 2 \end{bmatrix} = 10 + 8 = 19.
$$

---

## Revised Simplex Method

The revised simplex method follows the same iterative steps as the tableau simplex method but uses matrix manipulations instead of row operations. This approach improves computational accuracy and reduces machine roundoff errors.

### Algorithm Steps:

**Step 0:** Construct a starting basic feasible solution, with basis $B$ and objective coefficients vector $C_B$.

**Step 1:** Compute the inverse $B^{-1}$ using an appropriate method.

**Step 2:**
- For each nonbasic variable $x_j$, compute:
  $$
  z_j - c_j = C_B B^{-1} P_j - c_j.
 
$$
- If $z_j - c_j \geq 0$ (for maximization) or $\leq 0$ (for minimization), stop. The optimal solution is:
  $$
  X_B = B^{-1} b, \quad z = C_B X_B.
 
$$
- Otherwise, identify the entering variable $P_j$ with the most negative/positive value of $z_j - c_j$.

**Step 3:**
- Compute $B^{-

# Revised Simplex Algorithm

## Example

### Iteration 2

**Z_B2 = x_1, x_2, x_5, x₆**
**C_B2 = 5, 4, 0, 0**

|   | x_1   | x_2   | x_5   | x₆   |
|---|------|------|------|------|
| **Basis** | -1/4 | -1/2 |      |      |
|       6  | 4    | 0    | 0    |      |
|       -1/8 | 3/4 |      |      |      |

**P_1, P_2, P_5, P₆ = 1, 2, 0, 0**
**B_2⁻¹:**

|   | x_1   | x_2   | x_5   | x₆   |
|---|------|------|------|------|
| **Basic** | -1    | 1    |      |      |
|       3/8 | -5/4 |      |      |      |
|       0   | 1    |      | 1    |      |
|       1/8 | -3/4 |      |      |      |

**Nonbasic variables (zero level):**
- x_3 = 0
- x_4 = 0

Thus,

**Z_B2 = B_2 b = 3, , ,**

**z = C_B2 Z_B2 = 21**

---

### Optimality Computations:

**C_B2 B_2⁻¹:**

|   | x_1   | x_2   | x_5   | x₆   |
|---|------|------|------|------|
| **P_3, P_4** | 3    | 1    |      | 0    |
|       4    | 2    |      |      | 0    |

For $j = 3, 4$:

$$
z_j - c_j = C_B2 B_2⁻¹ P_3, P_4 - c_3, c_4
$$

$$
= \begin{bmatrix} 3 & 1 \\ 4 & 2 \end{bmatrix}
$$

Thus, $Z_B2$ is optimal, and computations end.

---

### Summary of Optimal Solution:
- **x_1 = 3**
- **x_2 = 1.5**
- **z = 21**

---

# Lecture 5: Advanced LP

## Course: Introduction to Optimization
**Dr. Bahrami**

---

# Bounded-Variables Algorithm

### Lower Bounds
Given $X \geq L$, substitute $X = L + X'$ where $X' \geq 0$. Solve the problem in terms of $X'$ (with lower bound zero). Back-substitute to find original $X$.

$$
X = L + X'
$$
$$
X' \geq 0
$$

### Upper-Bounding Constraints $X \leq U$

Maximize:
$$
z = C^T X \quad \text{subject to} \quad AX = b, \quad 0 \leq X \leq U
$$

The bounded algorithm uses only the main constraints $AX = b$ and $X \geq 0$. Upper bounds are implicitly handled by modifying feasibility conditions.

For a current basic feasible solution $X_B = B^{-1}b$, assume $P_j$ is entering (from regular optimality condition).

When nonbasic variables are zero:
$$
X_B i = b_i - B^{-1}P_j x_j
$$

**Conditions for Entering Variable $x_j$:**
1. Nonnegativity of basic variable: $X_B i \geq 0$
2. Upper bound on basic variable: $X_B i \leq U_{B,i}$ (where $U_B$ is the upper bounds vector for basic variables).
3. Upper bound on entering variable: $x_j \leq u_j$.

**Calculations:**
1. **Nonnegativity condition**:
   $$
   x_j \leq \theta_1 = \min_i \left( \frac{b_i}{B^{-1}P_j i} \right) \quad \text{if } B^{-1}P_j i > 0
  
$$

2. **Upper bound on basic variable**:
   $$
   b_i - U_{Bi} \leq x_j (B^{-1}P_j)_i \implies x_j \leq \theta_2 = \min_i \left( \frac{b_i - U_{Bi}}{- (B^{-1}P_j)_i} \right) \quad \text{if } B^{-1}P_j i < 0
  
$$

**Final Step for $x_j$:**
$$
x_j = \min \{ \theta_1, \theta_2, u_j \}
$$

---

### Change of Basis Rules:
- If $x_j = \theta_1$:
  - Leaving variable becomes nonbasic at zero level.
  - Use standard simplex method with $x_j$ entering and leaving variables.

- If $x_j = \theta_2$:
  - Leaving variable reaches upper bound.
  - Convert to zero-level by substitution: $X_B r = U_{Br} - X'_B r$, where $X'_B r \geq 0$.

- If $x_j = u_j$:
  - No change in basis; $x_j$ remains nonbasic at upper bound.
  - Substitute $x_j = u_j - x_j'$ to ensure zero-level for all nonbasic variables.

---

# Example

### Problem Statement:
Maximize:
$$
z = 3x_1 + 5y + 2x_3
$$
Subject to:
- $y + 2x_3 \leq 14$
- $2x_1 + 4y + 3x_3 \leq 43$
- $0 \leq x_1 \leq 4$
- $7 \leq y \leq 10$
- $0 \leq x_3 \leq 3$

**Substitution for lower bound on $y$:**
$$
y = x_2 + 7, \quad 0 \leq x_2 \leq 3
$$

---

### Iteration 0

**Basic Variables:**
|   | **x_1** | **x_2** | **x_3** | **x_4** | **x_5** |
|---|------|------|------|------|------|
| **Solution** | -3    | -5    | -2    | 0     | 0     |
| **z**        |       |       |       | 35    |

**Tableau:**

|   | x_1   | x_2   | x_3   | x_4   | x_5   |
|---|------|------|------|------|------|
| **Basis** |      |      |      | 1    |      |
|       x_4 | 1    | 1    | 2    | 1    | 0    |
|       4   |      |      |      | 4    |      |

|   | x_1   | x_2   | x_3   | x_4   | x_5   |
|---|------|------|------|------|------|
| **Basis** |      |      |      |      | 1    |
|       x_5 | 2    | 4    | 3    | 0    | 1    |
|       15  |      |      |      | 15   |      |

---

### Continuation (Iteration 0 to Iteration 1)

**Entering Variable: $x_2$**
$$
B^{-1}P_2 = [1, 4]^T, \quad z_2 - c_2 = -5
$$

Compute $\theta_1$:
$$
\theta_1 = \min \left( \frac{7}{1}, \frac{15}{4} \right) = 3.75 \quad (\text{for } x_5)
$$
Since all elements of $B^{-1}P_2 > 0$, $\theta_2 = \infty$.

Upper bound on $x_2$: $u_j = 3$

Thus:
$$
x_2 = \min \{ 3.75, \infty, 3 \} = 3
$$

Since $x_2 = u_j$, basis remains unchanged and $x_2$ becomes nonbasic at upper bound.

**Substitution:**
$$
y = x_2 + 7 \implies x_2 = 3 - x'_2
$$

New tableau:

|   | **x_1** | **x_2'** | **x_3** | **x_4** | **x_5** |
|---|------|---------|------|------|------|
| **Solution** |       |         |      | 4    | 15   |
| **z**        |
