# Introduction to Optimization
## Week 3

---

### Problem 1: Solve using the M-method

**Objective:**
Minimize
F(x_1, x_2, x_3, x_4) = −2x_1 + 3x_2 − 6x_3 − x_4

**Constraints:**
- $2x_1 + x_2 - 2x_3 + x_4 = 24$
- $x_1 + 2x_2 + 4x_3 \leq 22$
- $x_1 - x_2 + 2x_3 \geq 10$
- $x_1, x_2, x_3, x_4 \geq 0$

---

**Solution:**

#### Convert to Standard Form
Maximize:
F(x_1, x_2, x_3, x_4, s_1, s_2) = $2x_1 - 3x_2 + 6x_3 + x_4$
subject to:
- $2x_1 + x_2 - 2x_3 + x_4 = 24$
- $x_1 + 2x_2 + 4x_3 + s_1 = 22$
- $x_1 - x_2 + 2x_3 - s_2 = 10$
- $x_1, x_2, x_3, x_4 \geq 0$, $s_1, s_2 \geq 0$

#### Add Artificial Variables
Add artificial variable R_1 to the third equation and penalize it in the objective function:
Maximize:
F(x_1, x_2, x_3, x_4, s_1, s_2, R_1) = $2x_1 - 3x_2 + 6x_3 + x_4 - M \cdot R_1$

Constraints:
- $2x_1 + x_2 - 2x_3 + x_4 = 24$
- $x_1 + 2x_2 + 4x_3 + s_1 = 22$
- $x_1 - x_2 + 2x_3 - s_2 + R_1 = 10$
- Non-negativity constraints for all variables.

#### Initial Basic Solution
$(x_1, x_2, x_3, x_4, s_1, s_2, R_1) = (0, 0, 0, 24, 22, 0, 10)$

Set $M = 100$.

---

#### Iteration 0
**Tableau:**
| Basic | z       | x_4      | s_1     | R_1      |
|-------|---------|----------|--------|---------|
| **x_1** | -2      | 2        | 1      | 1       |
| **x_2** | 3       | 1        | 2      | -1      |
| **x_3** | -6      | -2       | 4      | 2       |
| **x_4** | -1      | 0        | 0      | 0       |
| s_1    | 0       | 0        | 1      | 0       |
| s_2    | 0       | 0        | 0      | -1      |
| R_1    | 100     | 0        | 0      | 1       |

**Solution:**
- $x_4 = 24$
- $s_1 = 22$
- $R_1 = 10$

---

#### Update z-row
$z_{new} = z_{old} + (1 \cdot x_4 - 100 \cdot R_1)$

**Iteration 1:**
- **x_3 enters**, **R_1 leaves**

| Basic | z       | s_1     | R_1      | x_4      |
|-------|---------|--------|---------|----------|
| **x_1** | -100    | 2      | 1       | 1       |
| **x_2** | 104     | 1      | -1      | 2       |
| **x_3** | -208    | -2     | 4       | 2       |
| **x_4** | 0       | 0      | 0       | 1       |
| s_1    | 0       | 1      | 0       | 0       |
| s_2    | 100     | 0      | -1      | 0       |
| R_1    | 0       | 0      | 1       | 0       |

**Solution:**
- $x_3 = 2$
- $s_1 = 5$
- $R_1 = 0$

---

#### Iteration 2:
- **s_2 enters**, **s_1 leaves**

| Basic | z       | s_2     | x_3      | x_4      |
|-------|---------|--------|----------|----------|
| **x_1** | -5/2    | 3/2    | 1        | 1/2     |
| **x_2** | 6       | 7      | 0        | 1/2     |
| **x_3** | 0       | 0      | 1        | 0       |
| **x_4** | 0       | 0      | 0        | 1       |
| s_1    | 0       | 1/2    | 1/4     | 1/4     |
| s_2    | -13/15  | 10     | -1/3     | 1/3     |
| R_1    | 0       | 0      | 0        | 0       |

**Solution:**
- $x_2 = 6$
- $s_2 = 3.4$
- $x_3 = 2$

---

### Problem 2: Solve using the Two-Phase Method

**Objective:**
Maximize
F(x_1, x_2) = $x_1 + x_2$

**Constraints:**
- $2x_1 + 4x_2 \leq 16$
- $-4x_1 + 2x_2 \leq 8$
- $x_1 + 3x_2 \geq 9$
- $x_1, x_2 \geq 0$

---

#### Convert to Standard Form
Maximize:
F(x_1, x_2, s_1, s_2, s_3) = $x_1 + x_2$
subject to:
- $2x_1 + 4x_2 + s_1 = 16$
- $-4x_1 + 2x_2 + s_2 = 8$
- $x_1 + 3x_2 - s_3 = 9$
- Non-negativity constraints for all variables.

---

#### Phase I: Minimize Artificial Variable R_1
Minimize:
$r = R_1$

Subject to:
- $2x_1 + 4x_2 + s_1 = 16$
- $-4x_1 + 2x_2 + s_2 = 8$
- $x_1 + 3x_2 - s_3 + R_1 = 9$
- Non-negativity constraints.

**Initial Basic Solution:**
$(x_1, x_2, s_1, s_2, s_3, R_1) = (0, 0, 16, 8, 0, 9)$

---

#### Iteration 0:
| Basic | r       | s_1     | s_2      | R_1      |
|-------|---------|--------|---------|---------|
| **x_1** | 0       | 2      | -4      | 1       |
| **x_2** | 0       | 4      | 2       | 3       |
| s_1    | 0       | 1      | 0       | 0       |
| s_2    | 0       | 0      | 1       | 0       |
| s_3    | 0       | 0      | 0       | -1      |
| R_1    | 1       | 0      | 0       | 1       |

**Solution:**
- $s_1 = 16$
- $s_2 = 8$
- $R_1 = 9$

---

#### Update r-row
$r_{new} = r_{old} + (-1 \cdot R_1)$

**Iteration 1:**
- **x_2 enters**, **R_1 leaves**

| Basic | r       | s_1     | x_2      | s_2      |
|-------|---------|--------|---------|---------|
| **x_1** | -1
