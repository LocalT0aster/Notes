# Introduction to Optimization

## Problems Sheet 11

---

### Problem 1: Maximize
```
f(x_1, x_2) = 2x_1 + 4x_2 - x_2_1 - 2x_2²
```
subject to:
```
x_1 + 2x_2 ≤ 8,
2x_1 - x_2 ≤ 12,
x_1 ≥ 0, x_2 ≥ 0.
```

#### Solution

The problem can be expressed in matrix form as:

**Maximize**
```
z = (2, 4) · [x_1; x_2]
```
subject to:
```
A·X ≤ b
X ≥ 0,
```
where:
- `C = (2, 4)`
- `D` is the Hessian matrix of second derivatives:
  ```
  D =
  [-1   0
   0  -2]
  ```
- `A` is the constraint coefficient matrix:
  ```
  A =
  [1    2
   2   -1]
  ```
- `b = [8; 12]`
- `I` is the identity matrix.

**KKT Conditions**:
```
[−2D·A AT 0 −I 0 0]
[Xᵀ λᵀ µᵀ sᵀ] =
[C b S U]

μj xj = 0, λi s_i = 0 for all i and j,
where λ, U, S, X ≥ 0.
```

**Simplex Method Iterations**:

#### Initial Tableau
```
Basic | r   R_1    R_2     s_1      s_2
x_1    | 0   2     -2     1       2
x_2    | 0   -4    4      2       -1
λ_1    | 0   1     2      0       0
λ_2    | 0   2     -1     0       0
µ_1    | 0   -1    0      0       0
µ_2    | 0    0   -1      0       0
s_1    | 0    0    0      1       0
s_2    | 0    0    0      0       1
R_1    | 1    1     0     0       0
R_2    | 1    0     1     0       0

ci: [2, 4]
b: [8, 12]
```

**Iteration 0**:
- **x_2 enters**, **R_2 leaves**.

#### Iteration 1:
```
Basic | r   R_1      R_2    s_1      s_2
x_1    | -2  2       0     1       2
x_2    | -4  0       4     2       -1
λ_1    | -3  1       2     0       0
λ_2    | -1  2      -1     0       0
µ_1    |  1  -1      0     0       0
µ_2    |  1   0     -1     0       0
s_1    |  0   0      0     1       0
s_2    |  0   0      0     0       1
R_1    |  0   1      0     0       0
R_2    |  1   0     1/4   -1/2    1/4

ci: [2, 4]
```

#### Iteration 2:
```
Basic | r   R_1      R_2    s_1      s_2
x_1    |  0  1       0     0       0
x_2    |  0   0      1     0       0
λ_1    |  0  1/2    -1/4   1/2    -1/4
λ_2    |  0   1      0     0       0
µ_1    |  0  -1/2    1/6    -1/6    1/6
µ_2    |  0   0      0     0       0
s_1    |  0   0      0     1       0
s_2    |  0   0      0     0       1
R_1    |  1/2 1/3    2/3   1/6    -1/6

ci: [0, 0]
```

**Optimal Solution**:
```
x*_1 = 1, x*_2 = 1,
s_1 = 5, s_2 = 11,
λ_1 = λ_2 = µ_1 = µ_2 = 0.
```

---

### Problem 2: Maximize
```
f(x_1, x_2) = 2x_1 + 6x_2 - x_2_1 + 2x_1·x_2 - 2x_2²
```
subject to:
```
x_1 + x_2 ≤ 2,
−x_1 + 2x_2 ≤ 2,
x_1 ≥ 0, x_2 ≥ 0.
```

#### Solution

The problem can be expressed similarly with:

- `C = (2, 6)`
- `D` is the Hessian:
  ```
  D =
  [-1   1
   1  -2]
  ```

**Initial Tableau**:
```
Basic | r    R_1     R_2      s_1       s_2
x_1    | 0    2     -2      1        -1
x_2    | 0   -2     4       1         2
λ_1    | 0    1     1       0         0
λ_2    | 0   -1     2       0         0
µ_1    | 0   -1      0      0         0
µ_2    | 0     0    -1       0        0
s_1    | 0     0     0      1         0
s_2    | 0     0     0      0         1
R_1    | 1     1     0       0        0
R_2    | 1     0     1       0        0

ci: [2, 6]
b: [2, 2]
```

**Simplex Iterations**:

#### Iteration 0:
- **x_1 enters**, **R_1 leaves**.

#### Iteration 1:
```
Basic | r    R_1     R_2      s_1       s_2
x_1    | -1   1      0      3/2     -1/2
x_2    | -2   0      4      1         2
λ_1    | -2   1      1      0         0
λ_2    | -1   -1     2      0         0
µ_1    |  1  -1       0      0         0
µ_2    |  1    0     -1      0         0
s_1    |  0    0      0      1         0
s_2    |  0    0      0      0         1
R_1    |  0   1/3    2/3    1/6       -1/6

ci: [−1, −1]
```

#### Iteration 2:
```
Basic | r    R_1     R_2      s_1       s_2
x_1    |  0   1/3    2/3    5/3     -2/3
x_2    |  0    0      0      0         1
λ_1    |  0    0      1      0         0
λ_2    |  0   -1      0     -1/2      1/2
µ_1    |  0   -1/3   -2/3   -1/6      1/6
µ_2    |  0    1/3   -1/3    1/6      -1/6

ci: [0, 0]
```

**Optimal Solution**:
```
x*_1 = 4/5, x*_2 = 6/5,
s_2 = 2/5, λ_1 = 14/15,
s_1 = λ_2 = µ_1 = µ_2 = 0.
```

---

### Problem 3: Gradient Descent with ε = 0.01

#### Initial
