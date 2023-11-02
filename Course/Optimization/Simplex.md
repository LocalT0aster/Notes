# Simplex Method

## ChatGPT 4 Explanation

The Simplex method is a popular algorithm used for solving linear programming problems. Linear programming (LP) is a technique for finding the maximum or minimum value of a linear objective function subject to linear equality and linear inequality constraints.

Let's break down the main components:

1. **Objective Function**: This is a linear function that we want to maximize or minimize. For instance, $Z = c_1x_1 + c_2x_2$ where $Z$ is the objective function and $x_1$ and $x_2$ are decision variables.

2. **Constraints**: These are the limitations or restrictions on the decision variables. They can be equalities or inequalities. For example, $a_1x_1 + a_2x_2 \leq b$.

3. **Non-negativity Constraint**: The decision variables are usually non-negative, i.e., $x_1 \geq 0$ and $x_2 \geq 0$.

The Simplex method is an iterative method that starts at a feasible solution and moves along the edges of the feasible region (defined by the constraints) to reach the optimal solution.

Here's a step-by-step breakdown of the Simplex method:

1. **Initialization**: Start with a feasible solution. This is typically a corner point (or vertex) of the feasible region. If the problem is in standard form, the initial feasible solution can often be found using the slack variables.

2. **Check Optimality**: Determine if the current solution is optimal. If all the coefficients of the objective function (in the row of the tableau representing the objective function) are non-positive (for a maximization problem) or non-negative (for a minimization problem), then the current solution is optimal.

3. **Pivot Operation**: If the current solution is not optimal:
    - Choose a non-basic variable (column) with a positive coefficient in the objective function row (for a maximization problem) to increase its value.
    - Determine which basic variable (row) will decrease to zero first as the chosen non-basic variable increases. This is done by dividing the right-hand side of each constraint by the corresponding element in the column of the chosen non-basic variable. The row with the smallest non-negative quotient is the one to exit.
    - Perform row operations to make the chosen non-basic variable the new basic variable (pivot in).

4. **Iterate**: Go back to step 2 and repeat until an optimal solution is found.

It's worth noting that while the Simplex method is powerful and can solve large LP problems, it doesn't guarantee polynomial-time performance. In practice, however, it's often very efficient.

## ChatGPT 4 Example

Alright, let's solve the given linear programming problem using the Simplex method.

Given:

Maximize
$$Z = 5x_1 + 4x_2 + 3x_3$$

Subject to:
$$
\begin{align*}
2x_1 + 3x_2 + x_3 &\leq 5 \\
4x_1 + x_2 + 2x_3 &\leq 11 \\
3x_1 + 4x_2 + 2x_3 &\leq 8 \\
x_1, x_2, x_3 &\geq 0 \\
\end{align*}
$$

**Step 1: Convert the inequalities to standard form.**

We can do this by adding slack variables.

- Let's add $s_1$ to the first constraint, $s_2$ to the second constraint, and $s_3$ to the third constraint.

$$
\begin{align*}
2x_1 + 3x_2 + x_3 + s_1 &= 5 \\
4x_1 + x_2 + 2x_3 + s_2 &= 11 \\
3x_1 + 4x_2 + 2x_3 + s_3 &= 8 \\
\end{align*}
$$

Where $s_1, s_2, s_3 \geq 0$.

**Step 2: Set up the initial Simplex tableau.**

The tableau will contain rows for each constraint and the objective function. It will also include columns for each variable and slack variable, as well as a column for the right-hand side (RHS) values of the constraints.

Let's construct this tableau.

```python
import numpy as np
import pandas as pd

# Coefficients of constraints and objective function
A = np.array([
    [2, 3, 1, 1, 0, 0, 5],    # Coefficients for the first constraint
    [4, 1, 2, 0, 1, 0, 11],   # Coefficients for the second constraint
    [3, 4, 2, 0, 0, 1, 8],    # Coefficients for the third constraint
    [-5, -4, -3, 0, 0, 0, 0]  # Negative of coefficients of the objective function
])

# Convert to a pandas DataFrame for better visualization
columns = ['x1', 'x2', 'x3', 's1', 's2', 's3', 'RHS']
index = ['Row1', 'Row2', 'Row3', 'Z']

tableau = pd.DataFrame(A, columns=columns, index=index)
tableau
```

Here's the initial Simplex tableau:

$$
\begin{array}{|c|c|c|c|c|c|c|}
\hline
& x_1 & x_2 & x_3 & s_1 & s_2 & s_3 & \text{RHS} \\
\hline
\text{Row1} & 2 & 3 & 1 & 1 & 0 & 0 & 5 \\
\text{Row2} & 4 & 1 & 2 & 0 & 1 & 0 & 11 \\
\text{Row3} & 3 & 4 & 2 & 0 & 0 & 1 & 8 \\
Z & -5 & -4 & -3 & 0 & 0 & 0 & 0 \\
\hline
\end{array}
$$

**Step 3: Iteration**

Starting with the tableau above, we'll follow the Simplex steps to optimize the function:

1. Identify the entering variable (non-basic variable) by finding the most negative coefficient in the last row (for maximization problems). In this case, $x_1$ with a coefficient of -5 is the most negative.
2. Identify the departing variable (basic variable). We do this by looking at the ratios of the RHS to the column entries of the entering variable and choosing the smallest non-negative ratio. This step determines which constraint is "tightest" or most binding as the entering variable increases.

Let's perform these steps to identify the pivot element.

```python
# Finding the entering column (pivot column)
pivot_column = np.argmin(tableau.iloc[-1, :-1])

# Compute the ratios for each row: RHS / pivot_column_element
# We exclude the last row (objective function) and only consider non-negative values
ratios = tableau.iloc[:-1, -1] / tableau.iloc[:-1, pivot_column]
valid_ratios = ratios.where(ratios > 0, np.inf)  # Replace negative values with infinity

# Finding the pivot row
pivot_row = valid_ratios.idxmin()

pivot_column, pivot_row
```

```txt
RESULT
(0, 'Row1')
```

The entering variable is $x_1$ (from the most negative coefficient in the last row) and the departing variable will come from Row1 (based on the smallest non-negative ratio).

This means the pivot element is the intersection of the column for $x_1$ and Row1.

**Step 4: Pivot Operation**

To perform the pivot operation:

1. Make the pivot element equal to 1 by dividing the entire pivot row by the pivot element.
2. Make all other elements in the pivot column equal to 0 by using the new pivot row to eliminate them.

Let's perform these operations on our tableau.

```python
# Correcting the indexing error and performing the pivot operation

# Convert pivot_row from string to integer index
pivot_row_idx = tableau.index.get_loc(pivot_row)

# Dividing the pivot row by the pivot element to make pivot element 1
tableau.iloc[pivot_row_idx] = tableau.iloc[pivot_row_idx] / tableau.iloc[pivot_row_idx, pivot_column]

# Making all other elements in the pivot column 0
for i in range(tableau.shape[0]):
    if i != pivot_row_idx:
        tableau.iloc[i] -= tableau.iloc[pivot_row_idx] * tableau.iloc[i, pivot_column]

tableau
```

After the pivot operation, our updated tableau looks like:

$$
\begin{array}{|c|c|c|c|c|c|c|}
\hline
& x_1 & x_2 & x_3 & s_1 & s_2 & s_3 & \text{RHS} \\
\hline
\text{Row1} & 1 & 1.5 & 0.5 & 0.5 & 0 & 0 & 2.5 \\
\text{Row2} & 0 & -5.0 & 0.0 & -2.0 & 1 & 0 & 1.0 \\
\text{Row3} & 0 & -0.5 & 0.5 & -1.5 & 0 & 1 & 0.5 \\
Z & 0 & 3.5 & -0.5 & 2.5 & 0 & 0 & 12.5 \\
\hline
\end{array}
$$

Now, we need to continue iterating until all coefficients in the Z-row are non-negative.

**Step 5: Continue Iterating**

We can see that the coefficient for $x_3$ in the Z-row is negative (-0.5). Hence, $x_3$ will be our next entering variable.

Let's identify the next pivot element by computing the ratios again.

```python
# Finding the next pivot column
pivot_column = np.argmin(tableau.iloc[-1, :-1])

# Compute the ratios for each row: RHS / pivot_column_element
ratios = tableau.iloc[:-1, -1] / tableau.iloc[:-1, pivot_column]
valid_ratios = ratios.where(ratios > 0, np.inf)  # Replace negative values with infinity

# Finding the pivot row
pivot_row = valid_ratios.idxmin()

pivot_column, pivot_row
```

```txt
RESULT
(2, 'Row3')
```

The next entering variable is $x_3$ and the departing variable will come from Row3.

Now, we'll repeat the pivot operation using the intersection of the column for $x_3$ and Row3 as our new pivot element.

Let's perform the pivot operation again on our tableau.

```python
# Convert pivot_row from string to integer index for the new pivot element
pivot_row_idx = tableau.index.get_loc(pivot_row)

# Dividing the pivot row by the pivot element to make pivot element 1
tableau.iloc[pivot_row_idx] = tableau.iloc[pivot_row_idx] / tableau.iloc[pivot_row_idx, pivot_column]

# Making all other elements in the pivot column 0
for i in range(tableau.shape[0]):
    if i != pivot_row_idx:
        tableau.iloc[i] -= tableau.iloc[pivot_row_idx] * tableau.iloc[i, pivot_column]

tableau
```

After the second pivot operation, our updated tableau is:

$$
\begin{array}{|c|c|c|c|c|c|c|}
\hline
& x_1 & x_2 & x_3 & s_1 & s_2 & s_3 & \text{RHS} \\
\hline
\text{Row1} & 1 & 2.0 & 0.0 & 2.0 & 0 & -1 & 2.0 \\
\text{Row2} & 0 & -5.0 & 0.0 & -2.0 & 1 & 0 & 1.0 \\
\text{Row3} & 0 & -1.0 & 1.0 & -3.0 & 0 & 2 & 1.0 \\
Z & 0 & 3.0 & 0.0 & 1.0 & 0 & 1 & 13.0 \\
\hline
\end{array}
$$

Now, all coefficients in the Z-row are non-negative, which means we have reached the optimal solution.

**Optimal Solution**:

- $Z = 13$
- $x_1 = 2$
- $x_2 = 0$ (Not in the basis)
- $x_3 = 1$
- $s_1 = 0$ (Not in the basis)
- $s_2 = 1$
- $s_3 = 0$ (Not in the basis)

[<kbd><br><- Return<br></kbd>](Optimization.md)
