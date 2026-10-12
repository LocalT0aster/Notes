# Lecture 4: Special Cases in the Simplex Method

**Dr. Mohammad Reza Bahrami**
*Innopolis University*
*Course of Optimization*
*Fall 2025*

Materials are taken from different sources with modifications. I do not claim any authorship of these materials.
**Dr. Mohammad Reza Bahrami**

---

## Course: Introduction to Optimization
### Lecture 4: Special Cases

---

## Content
1. **Special Cases in the Simplex Method**
   - Degeneracy
   - Alternative Optima
   - Unbounded Solution
2. Graphical Sensitivity Analysis

---

## Degeneracy

In the application of the feasibility condition of the simplex method, a tie for the minimum ratio may occur and can be broken arbitrarily. When this happens, at least one basic variable will be zero in the next iteration, and the new solution is said to be **degenerate**.

Degeneracy can cause the simplex iterations to cycle indefinitely, thus never terminating the algorithm.
The condition also reveals the possibility of at least one redundant constraint.

### Example
**Maximize** $z = 3x_1 + 9x_2$

**Subject to:**
$$
x_1 + 4x_2 \leq 8
$$
$$
x_1 + 2x_2 \leq 4
$$
$$
x_1, x_2 \geq 0
$$

Using slack variables $x#$ and $x$$, the solution tableaus are:

| Iteration | Basic       | $x_1$ | $x_2$ | $x#$ | $x$$ | Solution          |
|-----------|-------------|----------|----------|---------|---------|-------------------|
| 0         |             | -3       | -9       | 0       | 0       | $z = 0$      |
|           | $x#$    |          |          | 1       | 0       | $x_2 = 8$    |
|           | $x$$    | 1        | 2        | 0       | 1       | $z = -3/4$   |
|           |             |          |          |         |         | $x# = 4, x_2 = 4$ |
|           | **$x"$ enters** | **$x#$ leaves** |            |           |           |                   |
|           | $x$$    | ¼        | 1        | ¼       | 0       | $z = 9/4$    |
|           |             |          |          |         |         | $x_2 = 2$    |
|           | **$x!$ enters** | **$x$ leaves** |            |           |           |                   |
|           | $x#$    | ½        | 0        | -1/2    | 1       | $z = 3/2$    |
|           |             |          |          |         |         | **Optimum**      |
|           |             |          |          |         |         | $x_1 = 2, x_2 = 0$ |

In iteration 0, $x#$ and $x$$ tie for the leaving variable, leading to degeneracy in iteration 1 because the basic variable $x$$ assumes a zero value. The optimum is reached after one additional iteration.

### Remarks
1. **Practical Implications of Degeneracy:**
   - In graphical solutions (Figure), three lines pass through the optimal point where $x_1 = 0, x_2 = 2$.
     This indicates overdetermination in a two-dimensional problem, suggesting redundancy in one constraint.
   - Redundancy means an associated constraint can be removed without altering the solution space. For example:
     - Constraint $x_1 + 4x_2 \leq 8$ is redundant,
     - Constraint $x_1 + 2x_2 \leq 4$ is not.
   - Identifying superfluous resources during implementation can be crucial and may reveal irregularities in modeling.

2. **Theoretical Implications:**
   - Degeneracy can lead to cycling in simplex iterations, where the objective value does not improve (e.g., $z = 18$ in iterations 1 and 2).
   - While cycling is rare, it has been observed in practice.
   - Special algorithms exist to avoid cycling but may slow computations significantly. Use these only if cycling is confirmed.

---

## Alternative Optima

An LP problem may have an infinite number of alternative optima when the objective function is parallel to a nonredundant binding constraint (i.e., a constraint satisfied as an equation at the optimal solution).

### Example
**Maximize** $z = 2x_1 + 4x_2$

**Subject to:**
$$
x_1 + 2x_2 \leq 5
$$
$$
x_1 + x_2 \leq 4
$$
$$
x_1, x_2 \geq 0
$$

Figure illustrates how alternative optima arise when the objective function is parallel to a binding constraint. Any point on the line segment BC represents an alternative optimum with $z = 10$.

### Tableau Iterations

| Iteration | Basic       | $x_1$ | $x_2$ | $x#$ | $x$$ | Solution          |
|-----------|-------------|----------|----------|---------|---------|-------------------|
| 0         |             | -2       | -4       | 0       | 0       | $z = 0$      |
|           | $x#$    |          |          | 1       | 0       | $x_2 = 5$    |
|           | $x$$    | 1        | 1        | 0       | 1       | $z = 0$      |
|           |             |          |          |         |         | $x_1 = 4, x_2 = 1$ |
|           | **$x"$ enters** | **$x#$ leaves** |            |           |           |                   |
|           | $x$$    | ½        | 1        | ½       | 0       | $z = 2$      |
|           |             |          |          |         |         | **Optimum**      |
|           |             |          |          |         |         | $x_1 = 5/2, x_2 = 0$ |

Iteration 1 yields the optimum solution at point B ($x_1 = 0, x_2 = 5/2$, $z = 10$). The zero coefficient of nonbasic variable $x_1$ in the optimal tableau indicates that $x_1$ can be made basic without altering $z$.

Iteration 2 switches to $x_1$ and $x$ as entering/leaving variables, yielding point C ($x_1 = 3, x_2 = 1$, $z = 10$).

### Remarks
- The simplex method finds corner-point optima (points B and C).
- Mathematically, all points on the line segment BC can be expressed as a nonnegative weighted average of B and C:
  $$
  x_1 = \alpha \cdot 0 + (1 - \alpha) \cdot 3 = 3 - \alpha
 
$$
  $$
  x_2 = \alpha \cdot \frac{5}{2} + (1 - \alpha) \cdot 1 = \frac{5\alpha}{2} + 1 - \alpha
 
$$

- **Practical Significance:**
  Alternative optima allow choosing among multiple solutions without compromising the objective value.
  For example, in a product-mix scenario:
  - At B: Only activity $x_2$ is positive.
  - At C: Both activities are positive.
  If this represents product manufacturing, producing two products (C) may be advantageous over one (B).

---

## Unbounded Solution

In some LP models, the solution space is unbounded in at least one variable—meaning variables can increase indefinitely without violating constraints. The objective value may also become unbounded.

### Irregularities
- **Poor Model Construction:** Indicates missing key constraints.
- **Incorrect Coefficient Estimations:** May lead to unbounded solutions.

---

### Example (Unbounded Objective Value)
**Maximize** $z = 2x_1 + x_2$

**Subject to:**
$$
x_1 - x_2 \leq 10
$$
$$
2x_1 \leq 40
$$
$$
x_1, x_2 \geq 0
$$

#### Starting Iteration Tableau

| Basic       | $x_1$ | $x_2$ | $x#$ | $x$$ | Solution          |
|-------------|----------|----------|---------|---------|-------------------|
|             | -2       | -1       | 0       | 0       | $z = 0$      |
| $x#$    | 1        | -1       | 1       | 0       | $x_

Here is the rewritten text in clean, well-structured Markdown:

---

# Graphical Sensitivity Analysis

Using similar computations, you can verify that the dual price for machine **2** capacity is **$2/hr**, and it remains valid for changes in machine **2** capacity within the line segment DE.

- Minimum machine 2 capacity [at point D = (4, 0)]:
  $1 \times 4 + 3 \times 0 = 4$ hr
- Minimum machine 2 capacity [at point E = (0, 8)]:
  $1 \times 0 + 3 \times 8 = 24$ hr

Thus, the dual price of **$2/hr** for machine **2** remains applicable for the range:

$$
4 \, \text{hr} \leq \text{Machine 2 Capacity} \leq 24 \, \text{hr}
$$

The computed limits for machines **1** and **2** are referred to as the feasibility ranges.

---

### Question 1.
If JOBCO can increase the capacity of both machines, which machine should receive priority?

From the dual prices for machines **1** and **2**, each additional hour of machine **1** increases revenue by **$14**, whereas only **$2** for machine **2**. Thus, priority should be given to machine **1**.

---

### Question 2.
A suggestion is made to increase the capacities of machines **1** and **2** at an additional cost of **$10/hr** for each machine. Is this advisable?

- For machine **1**, the net revenue per hour = $14 - 10 = \$4$
- For machine **2**, the net revenue per hour = $2 - 10 = -\$8$

Hence, only machine **1** should be considered for capacity increase.

---

### Question 3.
If the capacity of machine **1** is increased from **8 to 13 hrs**, how will this impact the optimum revenue?

The dual price for machine **1** is **$14** and applies in the range **(2.67, 16)** hr. The proposed increase (to **13 hrs**) falls within the feasibility range.

Revenue increase = $14 \times (13 - 8) = \$70$
Total revenue will then be:
$$128 + $70 = \$198$

---

### Question 4.
Suppose that the capacity of machine **1** is increased to **20 hrs**. How will this affect the optimum revenue?

The proposed change falls outside the feasibility range **(2.67, 16)** hr.

Thus, we can only conclude an increase up to **16 hrs**.
Note: Falling outside the feasibility range does not mean there is no solution; it simply means available information is insufficient for a complete decision.

---

### Question 5.
How can we determine the new optimum values of the variables associated with a change in a resource?

The optimum values of the variables will **change**.

---

## Example: Changes in Objective Coefficients

The figure shows the graphical solution space of the JOBCO problem. The optimal point is at **C** ($x_1 = 3.2$, $x_2 = 1.6$, $z = \$128$).

Changes to revenue units (objective-function coefficients) alter the slope of $z$. As long as the objective function lies between lines **BF** and **DE**, the optimum solution at point C remains unchanged.

### Determining Ranges for Objective Function Coefficients

The general form of the objective function is:

$$
\text{Maximize } z = c_1 x_1 + c_2 x_2
$$

If we pivot $z$ around point **C** and allow it to rotate clockwise or counterclockwise, the optimum solution remains at **C** as long as:

$$
z = c_1 x_1 + c_2 x_2 \quad \text{is between} \quad x_1 + 3x_2 = 8 \quad \text{and} \quad 2x_1 + x_2 = 8
$$

This implies the ratio:

$$
\frac{c_1}{c_2}
$$

varies between $\frac{1}{3}$ and **2**, yielding the optimality range:

$$
\frac{1}{3} c_1 \leq c_2 \quad \text{and} \quad c_1 \leq 2 c_2
$$

---

### Example – Continued

#### Question 1.
Suppose the unit revenues for products **1** and **2** are changed to **$35** and **$25**, respectively. Will the current optimum remain unchanged?

The new objective function is:

$$
\text{Maximize } z = 35 x_1 + 25 x_2
$$

Check optimality range:
$$
\frac{35}{25} = 1.4 \quad \text{(within)} \quad (0.33, 2)
$$

Since the ratio falls within this range, the solution at **C** remains optimal.

However, the optimum value of $z$ changes to:

$$
35 \times 3.2 + 25 \times 1.6 = \$152
$$

---

#### Question 2.
If the unit revenue for product **2** is fixed at its current value ($c_2 = \$20$), what is the associated optimality range for $c_1$?

Substituting $c_2 = 20$ into:

$$
\frac{1}{3} c_1 \leq 20 \quad \text{and} \quad c_1 \leq 40
$$

Thus, the optimality range is:

$$
6.67 \leq c_1 \leq 40
$$
