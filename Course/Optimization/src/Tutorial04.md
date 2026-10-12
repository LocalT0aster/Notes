# Introduction to Optimization
## Week 4: Degeneracy, Alternative Optima, Unbounded Solution

---

### Problem 1. Solve the following LPP.
**Maximize**
F(x_1, x_2) = 6x_1 + 2x_2

**Subject to:**
1. -2x_1 + 3x_2 ≤ 3
2. x_1 + 2x_2 ≤ 9
3. 2x_1 − x_2 ≤ 5
4. x_1 + x_2 ≤ 5/2
5. x_1 ≥ 0
6. x_2 ≥ 0

---

**Solution**

Rewriting in standard form:
Maximize
F(x_1, x_2, s_1, s_2, s_3, s_4) = 6x_1 + 2x_2 + 0·s_1 + 0·s_2 + 0·s_3 + 0·s_4

**Subject to:**
1. -2x_1 + 3x_2 + s_1 = 3
2. x_1 + 2x_2 + s_2 = 9
3. 2x_1 − x_2 + s_3 = 5
4. x_1 + x_2 + s_4 = 5/2
5. x_1 ≥ 0, x_2 ≥ 0, s_1, s_2, s_3, s_4 ≥ 0

**Starting basic solution:** (x_1, x_2, s_1, s_2, s_3) = (0, 0, 24, 23, 10)

---

#### Iteration Table
| Basic | z       | s_1   | s_2   | s_3    | s_4     |
|-------|---------|------|------|-------|--------|
| **Iteration 0** |         |      |      |       |        |
| x_1    | -6      | -2   | 1    | 2     | 1      |
| x_2    | -2      | 3    | 2    | -1    | 1/2    |
| s_1    | 0       | 1    | 0    | 0     | 0      |
| s_2    | 0       | 0    | 1    | 0     | 0      |
| s_3    | 0       | 0    | 0    | 1     | -1/2   |

**Solution values:**
- x_1 = 3, x_2 = 4, s_1 = 5, s_3 = 5/2
- z = 15

---

| Basic | z       | s_1   | s_2   | x_1    | s_4     |
|-------|---------|------|------|-------|--------|
| **Iteration 1** |         |      |      |       |        |
| x_2    | -5      | 3/2  | 0    | 1/2   | 3/2    |
| s_1    | 0       | 1    | 0    | 0     | 0      |
| s_2    | 0       | 0    | 1    | 0     | 0      |
| x_1    | -5/3    | 2/3  | 0    | 1/3   | 4/3    |

**Solution values:**
- x_1 = 5/2, x_2 = 0
- z = 15

---

**Answer:** max F(x) = **15**, attained at (x_1, x_2) = **(5/2, 0)**

---

### Problem 2. Solve the following LPP using the graphical method.
**Maximize and minimize**
F(x_1, x_2) = x_1 + 2x_2

**Subject to:**
1. 2x_1 + 4x_2 ≤ 16
2. -4x_1 + 2x_2 ≤ 8
3. x_1 + 3x_2 ≥ 9
4. x_1 ≥ 0, x_2 ≥ 0

---

**Solution**

Rewriting in standard form:
Maximize F(x_1, x_2, s_1, s_2, s_3, R_1) = x_1 + 2x_2 + 0·s_1 + 0·s_2 + 0·s_3 − M·R_1

**Subject to:**
1. 2x_1 + 4x_2 + s_1 = 16
2. -4x_1 + 2x_2 + s_2 = 8
3. x_1 + 3x_2 − s_3 + R_1 = 9
4. x_1 ≥ 0, x_2 ≥ 0, s_1, s_2, s_3 ≥ 0, R_1 ≥ 0

**Starting basic solution:** (x_1, x_2, s_1, s_2, s_3) = (0, 0, 16, 8, 0)

---

#### Iteration Table
| Basic | z       | s_1   | s_2   | R_1    |
|-------|---------|------|------|-------|
| **Iteration 0** |         |      |      |       |
| x_2    | -302    | 4    | 2    | 3     |
| s_1    | 100     | 1    | 0    | 0     |
| s_2    | 0       | 0    | 1    | 0     |
| R_1    | -1      | 0    | 0    | 1     |

**Solution values:**
- x_1 = 6, x_2 = 4
- z = 8

---

| Basic | z       | s_3   | s_2   | x_2    |
|-------|---------|------|------|-------|
| **Iteration 1** |         |      |      |       |
| x_1    | -5      | 2/3  | 0    | 1/2   |
| s_3    | 4/3     | 1    | 0    | 0     |
| s_2    | 0       | 0    | 1    | 0     |

**Solution values:**
- x_1 = 6, x_2 = 1
- z = 8

---

**Answer:**
- **Max F(x) = 8**, attained at (x_1, x_2) = **(0, 4)**
- **Min F(x) = 8**, attained at (x_1, x_2) = **(6, 1)**

---

### Problem 3. Solve the following LPP using the M-method.
**Maximize**
F(x_1, x_2, x_3, x_4) = 2x_1 − 3x_2 + 6x_3 + x_4

**Subject to:**
1. x_1 + 2x_2 − 4x_3 ≤ 20
2. x_1 − x_2 + 2x_3 ≥ 10
3. 2x_1 + x_2 − 2x_3 + x_4 = 24
4. x_1, x_2, x_3, x_4 ≥ 0

---

**Solution**

Rewriting in standard form with artificial variable R_1 for constraint 2:
Maximize F(x_1, x_2, x_3, x_4, s_1, s_2, R_1) = 2x_1 − 3x_2 + 6x_3 + x_4 − M·R_1

**Subject to:**
1. x_1 + 2x_2 − 4x_3 + s_1 = 20
2. x_1 − x_2 + 2x_3 − s_2 + R_1 = 10
3. 2x_1 + x_2 − 2x_3 + x_4 = 24
4. x_1, x_2, x_3, x_4 ≥ 0, s_1, s_2, R_1 ≥ 0

**Starting basic solution:** (x_1, x_2, x_3, x_4, s_1, s_2, R_1) = (0, 0, 0, 24, 20, 0, 10)

---

#### Iteration Table
| Basic | z       | s_1   | R_1    | x_4     |
|-------|---------|------|-------|--------|
| **Iteration 0** |         |      |       |        |
| x_3    | -6      | -4   | 2     | -2     |
| s_1    | 1       | 1    | 0     | 0      |
| R
