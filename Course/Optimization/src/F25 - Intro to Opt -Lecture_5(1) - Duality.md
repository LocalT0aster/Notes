# Lecture 5 (Part 1): Duality Theory

**Dr. Mohammad Reza Bahrami**
*Innopolis University*
*Course of Optimization*
*Fall, 2025*

---

## Course: Introduction to Optimization

### Content

- [ ] **Duality Theory**
    - [x] Dual Problem
    - [x] Primal–dual Relationships

---

# Duality Theory

---

## Dual Problem

### Summary of Dual Construction (Equation Form Primal)

1. Assign a dual variable to each primal constraint.
2. Assign a dual constraint to each primal variable.
3. The right-hand side of primal constraints become coefficients in the dual objective function.
4. For each primal variable:
   - Its column is transposed into a row in the dual.
   - The coefficient from the primal objective becomes the dual right-hand side.
   - Remaining constraint coefficients form the left-hand side.

**Rules for Optimization and Signs:**
- All primal constraints are equations with nonnegative RHS, and all variables are nonnegative.

---

### Example: Primal to Dual Conversion

#### Primal Problem
Maximize $z = 5x_1 + 12x_2 + 4x_3$
Subjected to:
$$
x_1 + 2x_2 + x_3 \leq 10
$$
$$
2x_1 - x_2 + 3x_3 = 8
$$
$$
x_1, x_2, x_3 \geq 0
$$

**Equation Form:**
Maximize $z = 5x_1 + 12x_2 + 4x_3 + 0x_4$
Subjected to:
$$
x_1 + 2x_2 + x_3 + x_4 = 10
$$
$$
2x_1 - x_2 + 3x_3 + R = 8
$$
$$
x_1, x_2, x_3, x_4, R \geq 0
$$

#### Dual Problem
Minimize $w = 10y_1 + 8y_2$
Subjected to:
$$
y_1 + 2y_2 \geq 5
$$
$$
2y_1 - y_2 \geq 12
$$
$$
y_1 + 3y_2 \geq 4
$$
$$
y_1 \geq 0
$$
$$
y_2 \geq -M
$$
$y_2$ unrestricted

---

### Example: Minimization Primal to Dual Conversion

#### Primal Problem
Minimize $z = 15x_1 + 12x_2$
Subjected to:
$$
x_1 + 2x_2 \geq 3
$$
$$
2x_1 - 4x_2 \leq 5
$$
$$
x_1, x_2 \geq 0
$$

**Equation Form:**
Minimize $z = 15x_1 + 12x_2 + 0x_3 + 0x_4$
Subjected to:
$$
x_1 + 2x_2 - x_3 + 0x_4 = 3
$$
$$
2x_1 - 4x_2 + 0x_3 + x_4 = 5
$$
$$
x_1, x_2, x_3, x_4 \geq 0
$$

#### Dual Problem
Maximize $w = 3y_1 + 5y_2$
Subjected to:
$$
y_1 + 2y_2 \leq 15
$$
$$
2y_1 - 4y_2 \leq 12
$$
$$
-y_1 \leq 0
$$
$$
y_2 \leq 0
$$

**Rules:**
- $y_1 \geq 0, y_2 \leq 0$

---

## Primal–Dual Relationships

### Simplex Tableau Layout
The simplex tableau starts with an identity matrix for constraint coefficients of initial variables.

---

### Optimal Dual Solution
In linear programming (LP), the optimal solution of either primal or dual directly yields the other’s optimal solution. Computational efficiency may favor solving the dual if it has fewer constraints.

#### Two Methods to Determine Dual Values

**Method 1:**
- Identify starting primal basic variables and their corresponding dual variables.
- Use tableau coefficients from the original objective function to determine dual values:
  - $y_1 = \frac{29}{5}$
  - $y_2 = -\frac{2}{5} + M$

**Method 2:**
- Extract optimal inverse matrix elements under initial primal variables.
- Multiply by the original objective coefficients to find dual values:
  $$
  y_1, y_2 = (12, 5) \times \text{optimal inverse}
 
$$

---

### Primal–Dual Objective Values

For any feasible pair of solutions:
$$
\text{Objective value in maximization problem} \leq \text{Objective value in minimization problem}
$$

At optimality, the values are equal.

**Note:**
- Only optimization sense (maximize/minimize) matters.
- Optimum cannot occur with $z < w$.

---

### Example: Non-Optimal Solutions

#### Primal Solution
$x_1 = 0, x_2 = 0, x_3 = \frac{8}{3}$
Objective value (primal): $z = 5(0) + 12(0) + 4(\frac{8}{3}) = \frac{32}{3} \approx 10.67$

#### Dual Solution
$y_1 = 6, y_2 = 0$
Objective value (dual): $w = 10(6) + 8(0) = 60$

Since $z < w$, these are not optimal.

---

### Optimal Values Range
The optimum value of $z$ falls within the range $(\frac{32}{3}, 60)$.

---

## Simplex Tableau Computations

### Formulas for Iterations:

1. **Constraint Columns:**
   - Compute left-hand side and right-hand sides using inverse matrix elements.

2. **Objective Row (Reduced Cost):**
   $$
   z_j - c_j = a_{jB} \cdot \text{inverse}_{Bi}
  
$$
   where $a_{jB}$ is the coefficient of variable $x_j$ in the objective row, and $\text{inverse}_{Bi}$ are elements from the inverse matrix.

---

### Example Computations

#### Original Problem:
Maximize $z = 5x_1 + 12x_2 + 4x_3$
Subjected to:
$$
x_1 + 2x_2 + x_3 \leq 10
$$
$$
2x_1 - x_2 + 3x_3 = 8
$$

#### Optimal Inverse Matrix
$$
\begin{bmatrix}
\frac{2}{5} & -\frac{1}{5} \\
1 & \frac{1}{5}
\end{bmatrix}
$$

**Objective Row Computations:**
- For $x_4$ and $R$, use the inverse to determine reduced costs.
```

Here is your rewritten text in clean Markdown:

# Simplex Tableau Computations

## Example

**Objective:**
Maximize $z = 5x_1 + 12x_2 + 4x_3$

**Constraints:**
- $x_1 + 2x_2 + x_3 \leq 10$
- $2x_1 - x_2 + 3x_3 = 8$
- $x_1, x_2, x_3 \geq 0$

---

## Dual Problem

**Objective:**
Minimize $w = 10y_1 + 8y_2$

**Constraints:**
- $y_1 + 2y_2 \geq 5$
- $2y_1 - y_2 \geq 12$
- $y_1 + 3y_2 \geq 4$
- $y_1 \geq 0$
- $y_2 \geq -M$ (unrestricted in sign)

---

# Lecture 5: Duality Theory

Next, we demonstrate how the objective row computations are carried out with **Formula 2**.

The optimal values of the dual variables are:
$y_1 = 5$, $y_2 = -5$.

Let’s compute all the $z$-coefficients (as illustrated for $x_1$ and $R$).

Similar computations can be used to determine the $z$-coefficients of $x_2, x_3,$ and $x_4$.

---

# Course: Introduction to Optimization

**Note:** The original text appears incomplete or truncated at "Course: Introduction to Optimization" with no additional content.
```
