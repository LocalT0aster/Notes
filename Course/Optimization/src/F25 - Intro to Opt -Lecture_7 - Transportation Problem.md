# Lecture 7: Transportation Problems

**Dr. Mohammad Reza Bahrami**
*Innopolis University*
*Course of Introduction to Optimization*
*Fall, 2023*

Materials are taken from different sources with modifications. I do not claim any authorship of these materials.

---

## Course: Introduction to Optimization
### Dr. Bahrami

---

# Transportation Problems

## Terminology Recap

| Destinations | Sources       |
|--------------|---------------|
| **D1**       | [80]          | **S1**       | 464, 75   |
| **D2**       | [65]          | **S2**       | 867, 352  |
| **D3**       | [70]          | **S3**       | 125       |
| **D4**       | [85]          |             |           |

- **Supply**: `si` from source `i`
- **Demand**: `dj` at destination `j`
- **Cost**: `c_ij` per unit distributed from source `i` to destination `j`

---

## Key Definitions

### Components
- **m sources** (e.g., S1, S2, S3)
- **n destinations** (e.g., D1, D2, D3, D4)

| Units of commodity | Supply (`si`)       | Demand (`dj`)      |
|--------------------|---------------------|--------------------|
|                    | [80]                | 464                |
|                    | [65]                | 867                |
|                    | [125]               | 352                |
|                    | [100]               | 690                |
|                    | [65]                | 682                |

---

## Transportation Problem Model

### Assumptions
1. **Requirements Assumption**:
   - Each source `i` has a fixed supply `si`, fully distributed to destinations.
   - Each destination `j` has a fixed demand `dj`, fully received from sources.

2. **Feasible Solutions Property**:
   A transportation problem has feasible solutions if and only if:
   $$
   \sum_{i=1}^{m} s_i = \sum_{j=1}^{n} d_j
  
$$

3. **Cost Assumption**:
   The cost `c_ij` of distributing units from source `i` to destination `j` is proportional to the number of units transported:
   $$
   \text{Total Cost} = \sum_{i,j} c_{ij} x_{ij}
  
$$
   where $x_{ij}$ is the quantity shipped from source `i` to destination `j$.

---

### Problem Reformulation for Slack Cases
If supplies/demands are **maximum** rather than fixed:
- Introduce a **dummy source/destination** to absorb slack (unmet supply/demand).

---

## Setting Up the Transportation Simplex Method

### General Setup
The unstreamlined simplex method requires constructing a tableau with artificial variables $z_1, z_2, \dots, z_{mn}$ for equality constraints:
$$
\begin{align*}
\text{Row 0} & : \text{Objective function (converted to maximization)} \\
\text{Rows } i & : \text{Supply constraints: } x_{i1} + x_{i2} + \dots = s_i \\
\text{Columns } j & : \text{Demand constraints: } x_{1j} + x_{2j} + \dots = d_j
\end{align*}
$$

**Key Adjustments**:
- Eliminate artificial variables from row 0 using coefficients $u_i$ (row multiples) and $v_j$ (column multiples).

---

## Simplex Method Workflow

### Initial Basic Feasible Solution (BF)
1. **Select allocations**: Start with source/destination rows/columns under consideration.
2. **Allocate fully**:
   - Pick the next basic variable (`x_ij`) to satisfy the smaller of remaining supply (`si`) or demand (`dj`).
3. **Eliminate row/column** (whichever was exhausted first).
4. **Terminate if only one row/column remains**: Assign all non-selected variables to zero.

---

### Step-by-Step Rules
#### 1. Northwest Corner Rule
- Start at `x_11`.
- Move right (`xi,j+1`) if source `i` has remaining supply.
- Else, move down (`xi+1,j`).

#### 2. Vogel’s Approximation Method
For each row/column:
- Compute **difference** = (smallest cost) - (second smallest cost).
- Select the variable with the highest difference and lowest remaining cost.

#### 3. Russell’s Approximation Method
For each `x_ij` not yet selected:
$$
\Delta_{ij} = c_{ij} - u_i - v_j
$$
- Choose the variable with the **most negative** $\Delta_{ij}$ (highest absolute value).

---

## Optimality Test

A basic feasible solution is optimal if for all nonbasic variables $x_{ij}$:
$$
c_{ij} - u_i - v_j \geq 0
$$

**Steps**:
1. Compute $u_i$ and $v_j$ from the current tableau.
2. Check $\Delta_{ij}$ values to confirm optimality.

---
```

Here is the cleaned and structured Markdown version of your PDF text:

---

### **Lecture Notes on Transportation Problems**

#### **Introduction to Optimization**
**Dr. Bahrami**

---

### **Basic Variable Constraints**
For a basic variable $x_{ij}$, the condition $c_{ij} - u_i - v_j = 0$ must hold for each pair $(i, j)$ where $x_{ij}$ is basic.

There are $m + n - 1$ basic variables in the solution, leading to $m + n - 1$ equations. Since there are $m + n$ unknowns ($u_i$, $v_j$), one variable can be arbitrarily set without violating the constraints. This choice simplifies solving the system algebraically.

A convenient selection is:
- Choose the $u_i$ with the most allocations in its row (break ties arbitrarily).
- Set this $u_i = 0$.

This structure makes it straightforward to solve for remaining variables.

---

### **Lecture 7: Transportation Problems**
#### **Transportation Simplex Method**

**Slide 22:**
To derive values for $u_i$ and $v_j$, set $u_3 = 0$ (since row 3 has the highest allocations, 3). Solving sequentially yields the unknowns shown.

*Note:* This derivation depends on the current basic feasible solution (BF solution).

---

**Slide 23:**
Apply the optimality test by evaluating $c_{ij} - u_i - v_j$ from the table below. If any value is negative, the current BF solution is nonoptimal.

In this case:
- $c_{25} - u_2 - v_5 = -2$
- $c_{44} - u_4 - v_4 = -1$

Thus, the current solution is not optimal. The transportation simplex method must iterate to find a better BF solution.

---

**Slide 24:**
#### **Iteration Steps**

1. **Entering Basic Variable**
   The entering variable is chosen based on negative $c_{ij} - u_i - v_j$ values, as they reduce the objective function cost.
   Candidates: $x_{25}$ and $x_{44}$.
   Select the one with the most negative value (in absolute terms): **$x_{25}$**.

---

**Slide 25:**
#### **Step 2: Leaving Basic Variable**
Increasing an entering basic variable triggers compensating changes in other allocations to maintain supply/demand constraints. The first basic variable that hits zero becomes the leaving variable.

---

**Slide 26:**
#### **Step 3: New BF Solution**
Adjust allocations by:
- Adding the leaving variable’s value to recipient cells.
- Subtracting it from donor cells.

*Example:* If $x_{15} = 10$ is the leaving variable, update the tableau accordingly (nonbasic variables like $x_{15}$ are excluded in the new solution).

---

### **Tutorial 7: Transportation Problems**

#### **Problem 1**
Consider a transportation problem with:
- Plants: 4 (with monthly shipments of 10, 20, 20, and 10).
- Retailers: 4 (needing 20, 10, 10, and 20 shipments).

**Tasks:**
(a) Use **Vogel’s Approximation Method** to select the first basic variable manually.
(b) Use **Russell’s Approximation Method** to select the first basic variable manually.
(c) Apply the **northwest corner rule** to construct a complete initial BF solution.

---

#### **Problem 1 (Continued)**
*(Formulate as a transportation problem, apply rules, and iterate for optimality.)*

---
*Note:* Tables/figures referenced in slides are omitted here but should be included visually if available.
