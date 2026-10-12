# Tutorial 3: Simplex Method (Version 2)
**Dr. Mohammedreza Bahrami**
Innopolis University
Course of Introduction to Optimization

## Fall 2024

---

### Content
- Simplex method
- M-Method
- Two Phase Method

---

## Problem 1 (Part 1/2)

Develop the z-row after substituting out artificial variables:

**Maximize**
$$
z = 5x_1 + 6x_2
subject to:
-2x_1 + 3x_2 ≤ 3,
x_1 + 2x_2 ≤ 5,
6x_1 + 7x_2 ≤ 3,
x_1 ≥ 0, x_2 ≥ 0.
$$

---

## Problem 1 (Part 2/2)

### Solution

**Initial Tableau:**
Basic Variables: z, s_3, s_4, R_1
z-row:
| x_1 | x_2 | s_3 | s_4 | R_1 | b_1 |
|---|----|----|---|----|---|
| -5 | -6 | 0  | 0  | M  | 0  |

Constraints:
-2x_1 + 3x_2 + R_1 = 3
x_1 + 2x_2 + s_3 = 5
6x_1 + 7x_2 + s_4 = 3

**Updated z-row after substitution:**
New z-row = Old z-row + (-M × R_1 row)

```
| x_1 | x_2 | s_3 | s_4 | R_1 |
|----|----|----|----|----|
-5+2M | -6-3M | 1   | 6    | -2
0     | 2    | 0   | 0    | 0
0     | 0    | 1   | 0    | 0
0     | 0    | 0   | 1    | 0
-3M   | 5    | 3   | 3    |
```

---

## Problem 2 (Part 1/2)

Develop the z-row after substituting artificial variables:

**Minimize**
```
z = 3x_1 + 6x_2

subject to:
x_1 + 2x_2 ≤ 5,
6x_1 + 7x_2 ≤ 3,
4x_1 + 8x_2 ≥ 5,

with slack/surplus variables:
x_1 + 2x_2 + s_1 = 5,
- (4x_1 + 8x_2) - x_3 + R_1 = 5
```

---

## Problem 2 (Part 2/2)

### Solution

**Initial Tableau:**
```
Basic Variables: z, s_1, s_2, R_1
z-row:
| x_1 | x_2 | x_3 | s_1 | s_2 | R_1 | b_1 |
|----|----|----|----|----|----|----|
| -3 | -6 | 0  | 1  | 6  | 4  | 0  |

Constraints:
x_1 + 2x_2 + s_1 = 5
6x_1 + 7x_2 + s_2 = 3
- x_3 + R_1 = -5 (adjusted for ≥ constraint)

**Updated z-row after substitution:**
New z-row = Old z-row + (M × R_1 row)
```
| x_1 | x_2 | x_3 | s_1 | s_2 | R_1 |
|----|----|----|----|----|----|
-3+M  | -6+M | -M | 1   | 2   | 4
0     | 2    | 0  | 0   | 1   | 0
0     | 0    | 1  | 0   | 0   | -1
5M    | 5    | 3  | 5   |
```

---

## Problem 3

**Minimize**
```
z = 2x_1 + 3x_2 − 5x_3
subject to:
x_1 + x_2 + x_3 = 7,
2x_1 - 5x_2 + x_3 ≥ 10,

with artificial variables R_1 and R_2:

x_1 + x_2 + x_3 + R_1 = 7,
2x_1 − 5x_2 + x_3 + R_2 = 10
```

Using M-Method, the new z-row becomes:
```
z + (-2+3M)x_1 + (-3-4M)x_2 + (5+2M)x_3 = 17M
```

---

## Problem 3 Solution

### Phase I Tableau and Intermediate Steps:

**Intermediate Table:**
```
Basic Variables: x_1, x_2, x_3, R_1, R_2, z
z-row:
| x_1 | x_2 | x_3 | R_1 | R_2 |
|----|----|----|----|----|
-2+3M  | -3-4M | 5+2M | 0   | 0

Constraints:
R1: 1x_1 + 1x_2 + 1x_3 = 7
R2: 2x_1 − 5x_2 + x_3 = 10
```

**Optimal Solution (Phase I):**
```
Basic Variables: z, x_2, x_1, x_3
z-row:
| x_1 | x_2 | x_3 |
|----|----|----|
-2   | -8+3.5M | 6+0.5M/2 |

Iterative steps and final tableau adjustments lead to:

**Optimum Solution (Phase II):**
```
Optimal z = -14
x_1 = 3, x_2 = 0, x_3 = 4
```

---

## Problem 4

**Maximize**
```
z = 2x_1 + 3x_2 − 5x_3
subject to:
x_1 + x_2 + x_3 = 7,
2x_1 - 5x_2 + x_3 ≥ 10,

with non-negativity constraints: x_1, x_2, x_3 ≥ 0

Using Two Phase Method:

---

## Problem 4 Solution (Phase I)

### Phase I Tableau
**Row Definitions:**
```
I: R1 = x_1 + x_2 + x_3 - s_1 = 7
II: R2 = 2x_1 −5x_2 + x_3 - s_2 = 10

Basic Variables:
| r | R1 | R2 |
|---|----|----|
| x_1 | 1  | 2  |
| x_2 | 1  | -5 |
| x_3 | 1  | 1  |

Slack and Artificial Variables:
| s_1 | s_2 | R_1 | R_2 |
|----|----|----|----|
| 0  | 0  | -1 | -1 |

Updated Solution Values:
```
Solutions: (Phase I)
| r   | R1 | R2 |
|-----|----|----|
| 0   | 7  | 10 |
```

---

## Problem 4 Solution (Phase II)

### Phase II Tableau

**Final z-row and Basic Variables:**
```
z-row:
| x_1 | x_2 | x_3 |
|----|----|----|
-2   | -3 | 5  |

Constraints:
x_2 = 1/7, x_1 = 6/7
Optimal Solution:
z = 45/7 ≈ 6.43

---
**Summary of Optimal Values:**
```
Solutions (Phase II):
| z    | x_2   | x_1   |
|------|------|------|
| 102/7| 4/7  | 45/7 |
```
