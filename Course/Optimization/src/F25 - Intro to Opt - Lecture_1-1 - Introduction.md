# Lecture 1-1: Introduction

**Dr. Mohammad Reza Bahrami**
*Innopolis University*
*Course of Introduction to Optimization*
*Fall, 2025*

Materials are taken from different sources with modifications. I do not claim any authorship of these materials.

---

## Lecture 1: Introduction
### Course: Introduction to Optimization

**By Dr. Bahrami – Fall 2025**

---

## Content

- [ ] **Why Study Optimization?**
- [ ] **Importance of Optimization**
- [ ] **Usage and Applications**
    - Some Examples of Optimization using Data
        - Least-Squares Fitting of Data
        - Training of Artificial Neural Networks
        - Traveling Salesman Problem
- [ ] **Introduction to Optimization**
    - Optimization Problem Models
    - Categories of Optimization Problems
    - Optimization Problems Phases
    - Statement of an Optimization Problem
- [ ] **Linear Programming**

---

## 1. Why Study Optimization?

### What is Optimization?
Optimization refers to the process or method used to minimize or maximize a given quantity.

This quantity is expressed by a mathematical function that depends on some parameters.

### Importance and Applications

Many practical applications in different disciplines (computer science, physics, economics) can be formulated as optimization problems. The goal is not just solving a problem but obtaining an optimal solution.

### How Optimization Works
Optimization problems are formulated using mathematical functions.
Criteria for the existence and uniqueness of optima are derived by mathematical techniques.
Solution algorithms are iterative and approximate, with convergence speed and accuracy being critical considerations.

### Benefits of Knowing Optimization
If we understand optimization methods:
- We can apply them to engineering and scientific problems.
- We can refine these methods and adapt them for specialized scenarios.

---

## 2. Some Examples of Optimization Using Data

### Least-Squares Fitting of Data
Three measurements are given:

- $b_1$ at $t = -1$
- $b_2$ at $t = 0$
- $b_3$ at $t = 2$

Given:
$b_1 = 1$, $b_2 = 1$, $b_3 = 3$.

Find the affine-linear function $C + Dt$:

The equations for a line passing through all three points are:

$$
\begin{cases}
C - D = 1 \\
C = 1 \\
C + 2D = 3
\end{cases}
$$

Since these cannot be solved exactly (points aren't colinear), least squares is used to find the best fit.

The objective function for least squares is:
$$
\sum_{i=1}^{3} \left( A_i x_i - b_i \right)^2
$$
where $A_1 = 1, \, A_2 = 0, \, A_3 = 2$.

Solving yields the best-fit line:
$$
C + Dt = \frac{9}{7} + \frac{4}{7}t
$$

---

### Training of Artificial Neural Networks

Given a training dataset with inputs $x!_1, x!_2, ..., x!n$ and outputs $y!_1, y!_2, ...$.

Objective: Minimize the misfit function:
$$
f = \sum_{i=1}^{n} (w_i x!_i + b - y!)
$$

In practice, neural networks involve multiple layers of concatenated transfer and activation functions.

---

### Traveling Salesman Problem

**Task:**
- Find a path with minimal cost/length.
- Visit each node exactly once.

Example: Determine the cheapest route visiting all cities in a graph where edge weights represent flight costs between cities (solve the traveling salesperson problem).

---

## 3. Optimization Problem Example: Tickets Purchase

### Scenario
A businessperson travels between Kazan (KZN) and Moscow (MOS) for five weeks.
- Weekly departures from KZN on Mondays, returns on Wednesdays.
- Regular roundtrip ticket costs $400; a 20% discount is applied if the trip spans a weekend.
- One-way tickets cost 75% of the regular roundtrip price ($300).

**Question:** How should tickets be bought for the five-week period?

### Problem Breakdown
1. **Decision Alternatives:**
   - Option (a): Five regular KZN-MOS-KZN trips.
   - Option (b): One KZN-MOS, four MOS-KZN-MOS spanning weekends, and one MOS-KZN.
   - Option (c): One KZN-MOS-KZN covering Monday of the first week and Wednesday of the last week; four MOS-KZN-MOS covering remaining legs.

2. **Constraints:**
   Must leave KZN on Monday and return by Wednesday each week.

3. **Objective Criterion:**
   Minimize total ticket cost.
   - Option (a): $5 \times \$400 = \$2000$
   - Option (b): $0.75 \times \$400 + 4 \times 0.8 \times \$400 + 0.75 \times \$400 = \$1880$
   - Option (c): $5 \times 0.8 \times \$400 = \$1600$

**Optimal Solution:** Option (c) is the cheapest.

---

## 4. Optimization Problem Models

### General Structure
A general optimization problem model can be structured as:

- **Maximize or minimize** an objective function.
- **Subject to constraints.**

### Definitions:
- A solution is feasible if it satisfies all constraints.
- The set of all feasible solutions is called the *feasible set*.
- An optimal solution is feasible and yields the best (maximum/minimum) value for the objective function.
- If no feasible solutions exist, the problem is infeasible.
- A solvable problem admits an optimal solution.

### Model Completeness
The quality of a model depends on its completeness in representing real-world systems.

---

## 5. Solving Optimization Problem Models

Methods include:
- **Mathematical Programming:** Techniques for minimizing/maximizing functions under constraints (e.g., linear, nonlinear programming).
- **Stochastic Processes:** Analyzing problems with random variables and known probability distributions.
- **Statistical Methods:** Building empirical models from experimental data.

### Classification of Optimization Techniques
| Category                          | Example Techniques                                                                 |
|-----------------------------------|----------------------------------------------------------------------------------|
| Mathematical Programming          | Linear Programming, Nonlinear Programming, Quadratic Programming                |
| Stochastic Programming            | Dynamic Programming, Integer Programming                                       |
| Network Methods                   | Network Flow Problems                                                           |
| Multiobjective Optimization       | Multiobjective Programming                                                       |
| Statistical Decision Theory       | Regression Analysis, Cluster Analysis                                           |
| Simulation & Reliability           | Queueing Theory, Renewal Theory                                                  |
| Non-Traditional Optimization      | Genetic Algorithms, Simulated Annealing, Particle Swarm Optimization              |

---

## 6. Categories of Optimization Problems

*(Note: Figure referenced but not included in text)*

### Key Techniques
In practice, Operations Research (OR) does not offer a single universal technique for all optimization problems.
- **Linear Programming:** For linear objective and constraint functions.
- **Integer Programming:** Variables must be integers.
- **Dynamic Programming:** Decompose into smaller sub-problems.
- **Network Programming:** Model as networks.
- **Nonlinear Programming:** Non-linear functions.

These are just a few among many available OR tools.

# Solving an Optimization Problem Model

## Key Points on OR Techniques and Algorithms

- Most optimization techniques in Operations Research (OR) do not yield solutions in closed-form formulas.
  Instead, they rely on **algorithms** that iteratively refine the solution toward optimality.

- Each iteration involves repetitive computations, which are typically tedious. In practice, computers are essential for executing these algorithms efficiently.

- Some mathematical models are so complex that standard optimization algorithms fail to find an optimal solution.
  In such cases, heuristics—intelligent search rules of thumb—may be used instead to approximate a good solution.

---

# Lecture 1: Introduction
## Course: Introduction to Optimization
**By Dr. Bahrami – Fall 2025**

---

## Phases of Implementing OR in Practice

The principal phases for implementing Operations Research (OR) include:

1. **Definition of the problem**.
2. **Construction of the model**.
3. **Solution of the model**.
4. **Validation of the model**.
5. **Implementation of the solution**.

| Real-world Problem | Interpretation of Math Solving |
|-------------------|--------------------------------|
| Mathematical Problem | Solutions of Math Probability |

**Phase 3 (Model Solution)** is well-defined and generally easier to implement in OR studies because it primarily involves solving well-structured mathematical models.

---

## Optimization: Purposeful Activity

- **Optimization** is a deliberate process aimed at achieving the best results under multiple alternatives with given constraints.
- An optimization problem involves determining the optimal structure or values of decision parameters.

---

# Statement of an Optimization Problem

An optimization (or mathematical programming) problem can be stated as:

Find $\mathbf{X} = \left[ x_1, x_2, \ldots, x_n \right]^T$ that minimizes:
$$
f(\mathbf{X})
$$

**Subject to the constraints:**

- **Inequality constraints:**
  $$
g_j(\mathbf{X}) \leq 0
$$
  $j = 1, 2, \ldots, m$

- **Equality constraints:**
  $$
l_k(\mathbf{X}) = 0
$$
  $k = 1, 2, \ldots, p$

**Where:**
- $\mathbf{X}$ is an n-dimensional decision vector.
- $f(\mathbf{X})$ is the objective (cost) function.
- $g_j(\mathbf{X})$ and $l_k(\mathbf{X})$ are inequality and equality constraints, respectively.

If there are no constraints, the problem is called **unconstrained optimization**.

---

# Mathematical Programming Types

### Combinatorial/Discrete Optimization
- Domain $\mathbf{X}$ consists of discrete sets (e.g., integral or binary vectors).

### Continuous Optimization
- Domain $\mathbf{X}$ includes continuous sets like:
  - Entire $\mathbb{R}^n$
  - Boxes: $\{ x : a \leq x \leq b\}$
  - Simplex: $\{ x \geq 0, \sum_i x_i = 1 \}$
- Objective and constraints are (at least) continuous on $\mathbf{X}$.

### Linear Optimization
- Variables $\mathbf{X} \in \mathbb{R}^n$.
- Objective and constraints are linear functions of $x$.

### Nonlinear Continuous Optimization
- Some objectives or constraints involve nonlinear functions.

---

### Convex Optimization Problem

A problem is convex if the objective and constraint functions satisfy:
$$
g_j(\alpha x + \beta y) \leq \alpha g_j(x) + \beta g_j(y)
$$
for all $x, y \in \mathbb{R}^n$ and $\alpha, \beta \geq 0$ with $\alpha + \beta = 1$.

---

# Linear Programming (LP)

## Examples of Optimization Problems

### Example 1: Linear Optimization Problem
**Problem:**
$$
x_R + x_S \leq 20
$$
Minimize $x_R$: subject to $x_R - x_S = 5$
$x_R, x_S \geq 0$

This is an **LP (Linear Programming)** problem.

### Example 2: Non-Linear Optimization Problem
**Problem:**
$$
x_R + x_S \leq 20
$$
Minimize $\exp(x_R)$ subject to $x_R - x_S = 5$
$x_R, x_S \geq 0$

This is **not an LP problem**.

---

### Example 3: Linear Constraints with Non-Standard Form
**Problem:**
$$
2x_1 + x_2 \geq 20 - x_3
$$
Subject to $x_1 - x_3 = 5$
$x_1, x_3 \geq 0$, $x_2 \leq 0$

This is an **LP problem** because constraints can be rewritten in standard form.

### Example 4: Infinitely Many Linear Constraints
**Problem:**
$$
i x_1 \geq 20 - x_3
$$
Subject to $x_1 - x_3 = 5$
$x_1, x_3 \geq 0$, $x_2 \leq 0$ for all $i \geq 2$

This is **not an LP problem** due to infinitely many constraints.

---

## Standard Forms of Linear Programs

### Rewriting Constraints
- Every linear inequality/equality can be rewritten so that the left-hand side is a weighted sum:
  $$
\sum_{j=1}^n a_j x_j \leq b
$$
  or equivalently,
  $$
-\sum_{j=1}^n a_j x_j \geq -b
$$

- Linear equalities can be represented by pairs of opposite inequalities:
  $$
\sum_{j=1}^n a_j x_j = b \implies \sum_{j=1}^n a_j x_j \leq b, \quad -\sum_{j=1}^n a_j x_j \leq -b
$$

### Canonical Form
Every LP problem can be rewritten in **canonical form**:
- Maximize $Y = c^T X$
- Subject to:
  $$
A X \leq B
$$
  $X \geq 0$

**Notations:**
- Term-wise: $c_i, a_{ij}, b_j$
- Matrix-vector: $C^T X \leq B$, where $A$ is the matrix of coefficients.

---

# Example 1: Modeling with Linear Programming

## Problem: Production Planning for Tatar-Paint
Tatar-Paint produces interior and exterior paints from two raw materials, M1 and M2. The goal is to maximize daily profit while adhering to constraints on material usage and demand limits.

### Data Table:
| Raw Material | Exterior Paint (tons/ton) | Interior Paint (tons/ton) | Daily Availability (tons) |
|--------------|---------------------------|---------------------------|---------------------------|
| M1           | 6                         | 4                         | 24                        |
| M2           | 1                         | 2                         | 6                         |

### Constraints:
- **Raw Material Usage:**
  - $6x_1 + 4x_2 \leq 24$ (M1)
  - $x_1 + 2x_2 \leq 6$ (M2)

- **Market Demand:**
  - $x_2 - x_1 \leq 1$
  - $x_2 \leq 2$

### Objective:
Maximize total profit:
$$
z = 5x_1 + 4x_2
$$

**Decision Variables:**
$x_1$: Tons of exterior paint produced daily
$x_2$: Tons of interior paint produced daily

---

# Example 2: Modeling with Linear Programming (Diet Problem)

## Diet Optimization for Ozark Farms
Ozark Farms needs to formulate a diet meeting nutritional requirements using corn and soybean meal.

### Nutritional Composition:
| Feedstuff | Protein (lb/lb) | Fiber (lb/lb) | Cost ($/lb) |
|-----------|-----------------|--------------|------------|
| Corn      | 0.09            | 0.02         | 0.30       |
| Soybean Meal | 0.60          | 0.06         | 0.90       |

### Requirements:
- Daily consumption of protein ≥ 800 lb.
- Daily consumption of fiber must meet specific bounds.

**Objective:**
Find the cheapest diet mixture that meets nutritional requirements.

---

Here’s the cleaned and structured Markdown version of your PDF text:

---

# Dietary Requirements
The dietary requirements of the special feed are at least **30% protein** and at most **5% fiber**.

# Objective
The goal is to determine the daily minimum-cost feed mix.

## Lecture 1: Introduction

### Course: Introduction to Optimization
**By Dr. Bahrami – Fall 2025**

---

### Example 2 - Modeling with LP

#### Decision Variables:
- $x_1$ = lb of corn in the daily mix
- $x_2$ = lb of soybean meal in the daily mix

#### Objective Function:
Minimize total daily cost (in dollars):
$$
z = 0.3x_1 + 0.9x_2
$$

#### Constraints:
1. **Daily feed requirement**:
   $$
x_1 + x_2 \geq 800
$$
2. **Protein requirement (≥30%)**:
   Protein content in $x_1$ lb of corn and $x_2$ lb of soybean meal is $(0.09x_1 + 0.6x_2)$ lb.
   This must satisfy:
   $$
   0.09x_1 + 0.6x_2 \geq 0.3(x_1 + x_2)
  
$$
   Simplified to:
   $$
   0.21x_1 - 0.30x_2 \leq 0
  
$$

3. **Fiber requirement (≤5%)**:
   Fiber content in $x_1$ lb of corn and $x_2$ lb of soybean meal is $(0.02x_1 + 0.06x_2)$ lb.
   This must satisfy:
   $$
   0.02x_1 + 0.06x_2 \leq 0.05(x_1 + x_2)
  
$$
   Simplified to:
   $$
   0.03x_1 - 0.01x_2 \geq 0
  
$$

4. **Non-negativity**:
   $x_1, x_2 \geq 0$

---

### Complete Model

**Objective:**
Minimize:
$$
z = 0.3x_1 + 0.9x_2
$$

**Subject to:**
1. $x_1 + x_2 \geq 800$
2. $0.21x_1 - 0.30x_2 \leq 0$
3. $0.03x_1 - 0.01x_2 \geq 0$
4. $x_1, x_2 \geq 0$

---

### Lecture 1: Introduction
*(Note: Pages 38 and 39 are repeated; the above content is consolidated.)*

---
