# Lecture 6: An Interior-Point Algorithm

**Dr. Mohammad Reza Bahrami**
*Innopolis University*
*Course of Introduction to Optimization*
*Fall, 2025*

---

## Concepts of the Interior-Point Algorithm

### Concept 1: Shoot through the interior of the feasible region toward an optimal solution.
### Concept 2: Move in a direction that improves the objective function value at the fastest possible rate.
### Concept 3: Transform the feasible region to place the current trial solution near its center, thereby enabling large improvements when concept 2 is implemented.

---

## Problem Example

**Maximize** $z = x_1 + 2x_2$

**Subject to:**
$x_1 + x_2 \leq 8$
$x_1, x_2 \geq 0$

The optimal solution in this example is $(x_1, x_2) = (0, 8)$ with $z = 16$.

---

## Initial Setup and Trial Solution

- The algorithm requires an initial trial solution inside the feasible region.
- For this problem, we arbitrarily choose $(x_1, x_2) = (2, 2)$.

### Augmented Form of the Problem
**Maximize** $z = x_1 + 2x_2$

**Subject to:**
$x_1 + x_2 + x_3 = 8$
$x_1, x_2, x_3 \geq 0$

Here, $x_3$ is the slack variable for the constraint.

In general form:
- **Objective:** Maximize $z = c^T x$
- **Constraints:**
  - $Ax = b$
  - $x \geq 0$

For this example:
- $c = [1, 2, 0]$
- $A = \begin{bmatrix} 1 & 1 & 1 \\ 0 & 0 & 0 \end{bmatrix}$ (Note: Simplified to a single row for the equality constraint)
- $b = [8]$

---

## Initial Trial Solution in Augmented Form
The initial trial solution is $(x_1, x_2, x_3) = (2, 2, 4)$.

### Direction of Movement
To improve $z$ as quickly as possible, we move along the gradient direction:
$\nabla z = [1, 2, 0]$.

**Attempted Move:**
$(x_1, x_2, x_3) + \alpha \cdot \nabla z \rightarrow (3, 4, 4)$

However, this point is infeasible because $x_3 = 8 - 3 - 4 = 1 \neq 4$.

---

## Projected Gradient Implementation

### Projection onto Feasible Region
The feasible region is a triangle with vertices $(8,0,0)$, $(0,8,0)$, and $(0,0,8)$.

To project the point $(3,4,4)$ back into the feasible region:
- The direction perpendicular to the feasible plane (i.e., $x_1 + x_2 + x_3 = 8$) is $[1, 1, 1]$.
- Projecting $(3,4,4)$ onto this plane results in $(2, 3, 3)$.

The projected gradient vector is:
$c_p = (0, 1, -1)$.

---

## Computing the Projected Gradient

Using the projection matrix $P$:

$$
P = I - A^T (A A^T)^{-1} A
$$

For this example:

$$
A^T A =
\begin{bmatrix}
1 & 1 & 1 \\
0 & 0 & 0
\end{bmatrix}^T
\begin{bmatrix}
1 & 1 & 1 \\
0 & 0 & 0
\end{bmatrix}
= \begin{bmatrix}
1 & 1 & 1 \\
1 & 1 & 1 \\
1 & 1 & 1
\end{bmatrix} \quad \text{(Corrected for equality constraint)}
$$

$$
(P)^{-1} A = \begin{bmatrix}
\frac{2}{3} & -\frac{1}{3} & -\frac{1}{3} \\
-\frac{1}{3} & \frac{1}{3} & \frac{1}{3} \\
-\frac{1}{3} & \frac{1}{3} & \frac{1}{3}
\end{bmatrix}
$$

Thus, the projected gradient $c_p = P c$ is:

$$
c_p = \begin{bmatrix}
\frac{5}{6} & -\frac{1}{6} & -\frac{1}{3}
\end{bmatrix}^T
$$

---

## Step Size Selection ($\alpha$)

The step size $\alpha$ is chosen to ensure feasibility while maximizing improvement in $z$. A common heuristic is:

$$
\alpha = 0.5 \quad (\text{for this example})
$$

This ensures the solution remains within bounds and moves toward optimality effectively.

---

## Centering Scheme (Concept 3)

### Rescaling Variables

To center the trial solution, rescale variables so that $(x_1, x_2, x_3) = (2, 2, 4)$ becomes equidistant from all boundaries:

$$
\hat{x}_1 = \frac{x_1}{2}, \quad \hat{x}_2 = \frac{x_2}{2}, \quad \hat{x}_3 = \frac{x_3}{4}
$$

The new problem in rescaled coordinates:
**Maximize** $z = 2\hat{x}_1 + 4\hat{x}_2$

**Subject to:**
$2\hat{x}_1 + 2\hat{x}_2 + 4\hat{x}_3 = 8$
$\hat{x}_i \geq 0, \quad i = 1, 2, 3$

The trial solution $(1, 1, 1)$ is now equidistant from all boundaries.

---

## Iteration Summary

### Diagonal Matrix $D$ and Rescaled Variables
$$
D = \begin{bmatrix}
2 & 0 & 0 \\
0 & 2 & 0 \\
0 & 0 & 4
\end{bmatrix}, \quad \hat{x} = D^{-1} x
$$

The projected gradient in rescaled coordinates remains:
$$
c_p = \left[ \frac{5}{6}, -\frac{1}{6}, -\frac{1}{3} \right]
$$

### Movement Direction
- The algorithm moves from $(1, 1, 1)$ along the direction of $c_p$.
- A step size $\alpha$ is chosen to ensure feasibility.

---

## Final Notes

The interior-point method efficiently handles large-scale problems by:
1. Staying in the feasible region’s interior.
2. Moving optimally using gradients.
3. Centering solutions for better convergence.

For small problems, it may be less efficient than simplex methods but excels in scalability and theoretical guarantees.
```

Here is the cleaned and structured Markdown version of your PDF text:

---

# **Introduction to Optimization**
**Lecture 6: An Interior-Point Algorithm**
*Instructor: Dr. Bahrami*

---

## **Iteration 1**

### **Step (Implicitly Described)**
- A trial solution $x_{\tilde{w}}$ is defined as:
  $$
  x_{\tilde{w}} = 1 + \frac{c_p}{v}
 
$$
  where $v$ is chosen such that the smallest component of $x_{\tilde{w}}$ equals zero when $\alpha = 1$.

- In original coordinates, this corresponds to:
  $$
  \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}
  =
  \begin{bmatrix} 0 \\ 2 \\ 0 \end{bmatrix}
 
$$
  (with $D$ scaling applied).

### **Values**
- $\alpha = 0.5$
- $c_p = \frac{7}{4}$, $v = \frac{1}{2}$
- Trial solution:
  $$
  x_{\tilde{w}} = \begin{bmatrix} 1 \\ \frac{3}{2} \\ 1 \end{bmatrix}
 
$$
- Transformed coordinates (after scaling):
  $$
  D^{-1}x_{\tilde{w}} =
  \begin{bmatrix}
  5/4 \\
  0 \\
  1/2
  \end{bmatrix}
 
$$

---

## **Summary of the Interior-Point Algorithm**

### **Steps**
1. **Initialization**:
   - Set diagonal matrix $D$ with current trial solution components:
     $$
     D =
     \begin{bmatrix}
     x_1 & 0 & \cdots & 0 \\
     0 & x_2 & \ddots & \vdots \\
     \vdots & \ddots & \ddots & 0 \\
     0 & \cdots & 0 & x_n
     \end{bmatrix}
    
$$

2. **Compute $A_{\tilde{w}}$ and $c_p'$**:
   - $A_{\tilde{w}} = AD^{-1}$
   - $c_p' = D^{-1}c$

3. **Project onto feasible region**:
   - Compute projection matrix $P$:
     $$
     P = I - A_{\tilde{w}}^T A_{\tilde{w}}
    
$$
   - Update $c_p = Pc_p'$.

4. **Generate trial solution**:
   - Set $x = Dx_{\tilde{w}}$ (for next iteration).
   - If $x$ is virtually unchanged, the algorithm has converged.

5. **Adjust for convergence check**:
   - Identify the negative component of $c_p$ with the largest absolute value as $v$.
   - Compute:
     $$
     x_{\tilde{w}} = 1 + \frac{c_p}{v}
    
$$
     where $\alpha \in (0,1)$ (e.g., $\alpha = 0.5$).

---

## **Iteration 2**

### **Step 1: Transformation**
- Current trial solution:
  $$
  x_{\tilde{w}} =
  \begin{bmatrix}
  7/2 \\
  0 \\
  2
  \end{bmatrix}
 
$$
- Rescaled variables (in new coordinates):
  $$
  D^{-1} =
  \begin{bmatrix}
  0 & 0 & 0 \\
  0 & 5/4 & 0 \\
  0 & 0 & 7/2
  \end{bmatrix}
 
$$
- Transformed solution:
  $$
  x_{\tilde{w}}^T = \begin{bmatrix} -1 \\ 8 \\ 0 \end{bmatrix}
 
$$

### **Step 2: Compute $A_{\tilde{w}}$ and $c_p'$**
$$
A_{\tilde{w}} =
\begin{bmatrix}
5/7 & 7/2 \\
2/7 & 2/2 \\
\end{bmatrix},
\quad
c_p' = D^{-1}c =
\begin{bmatrix} 2 \\ 0 \end{bmatrix}.
$$

### **Step 3: Project onto feasible region**
$$
P =
\begin{bmatrix}
-7/18 & 41/90 & -14/45 \\
-2/9 & -14/45 & 37/45 \\
-11/12 & \quad & \quad
\end{bmatrix},
\quad
c_p = P c_p' =
\begin{bmatrix} 133/60 \\ -41/15 \end{bmatrix}.
$$

### **Step 4: Determine $v$ and update**
$$
v = \left| -\frac{11}{12} \right| \approx 0.83,
\quad
x_{\tilde{w}} =
\begin{bmatrix}
1 + \frac{-41/15}{0.83} \\
\end{bmatrix}.
$$

### **Step 5: Trial Solution for Iteration 3**
$$
x = D x_{\tilde{w}} \approx \begin{bmatrix} 2.08 \\ 4.92 \end{bmatrix}.
$$

---

## **Trajectory Visualization (Original Coordinates)**
- Trial solutions:
  - Iteration 1: $(2, 2)$
  - Iteration 2: $(2.5, 3.5)$
  - Iteration 3: $(2.08, 4.92)$

- The algorithm converges toward the optimal solution:
  $$
  x_1 = 0, \quad x_2 = 8.
 
$$

---

*Figure references omitted for brevity.*
