# Introduction to Optimization
## Week 8: Problem Sheet 7

---

### **Problem 1**
In three warehouses $A_1$, $A_2$, and $A_3$ there are units of one type of product. The quantities available are:
- $A_1$: 140 units,
- $A_2$: 180 units,
- $A_3$: 160 units.

These products must be shipped by truck to four distributing warehouses $B_1$, $B_2$, $B_3$, $B_4$, and $B_5$ with fixed demands:
- $B_1$: 60 units,
- $B_2$: 70 units,
- $B_3$: 120 units,
- $B_4$: 130 units,
- $B_5$: 100 units.

The total supply equals the total demand (480 units). The shipping costs from $A_i$ to $B_j$ are given in the table below. Use the **Northwest Corner Rule** and the **minimal element method** to determine any feasible shipment plan.

#### Shipping Cost Table
| Source \ Destination | B1  | B2  | B3   | B4  | B5  |
|---------------------|-----|-----|------|-----|-----|
| $A_1$             | 2   | 8   | 9    |     |     |
|                     |     |     |      | 3   |     |
| $A_2$             |     | 4   | 7    | 1   | 4   |
| $A_3$             |     |     | 3    | 7   | 2   |

#### Solution

##### **Northwest Corner Rule**
| Source \ Destination | B1 (60) | B2 (70) | B3 (110) | B4 (70) | B5 (100) |
|---------------------|---------|---------|----------|---------|---------|
| $A_1$             | 2       |         |          |         |         |
|                     |         | 3       |          |         |         |
| $A_2$             |         |         | 7        |         |         |
|                     |         |         |          | 4       |         |
| $A_3$             |         |         |          |         | 2       |

**Total cost:**
$S = 2 \cdot 60 + 3 \cdot 70 + 4 \cdot 10 + 1 \cdot 110 + 4 \cdot 70 + 7 \cdot 60 + 2 \cdot 100 = 1380$

##### **Minimal Element Method**
| Source \ Destination | B1 (60) | B2 (70) | B3 (120) | B4 (80) | B5 (40) |
|---------------------|---------|---------|----------|---------|---------|
| $A_1$             | 2       |         |          |         |         |
|                     |         | 7       |          |         |         |
| $A_2$             |         |         | 3        |         |         |
|                     |         |         |          | 4       |         |
| $A_3$             |         |         |          |         | 1       |

**Total cost:**
$S = 2 \cdot 60 + 7 \cdot 70 + 1 \cdot 120 + 2 \cdot 80 + 7 \cdot 50 + 1 \cdot 40 = 1380$

---

### **Problem 2**
In three warehouses $A_1$, $A_2$, and $A_3$ there are units of one type of product. The quantities available are:
- $A_1$: 160 units,
- $A_2$: 140 units,
- $A_3$: 170 units.

These products must be shipped to four distributing warehouses $B_1$, $B_2$, $B_3$, and $B_4$ with fixed demands:
- $B_1$: 120 units,
- $B_2$: 50 units,
- $B_3$: 190 units,
- $B_4$: 110 units.

The shipping costs from $A_i$ to $B_j$ are given in the table below. Use the **Northwest Corner Rule** and the **minimal element method** to determine any feasible shipment plan.

#### Shipping Cost Table
| Source \ Destination | B1 (120) | B2 (50)  | B3 (190) | B4 (110) |
|---------------------|----------|----------|----------|----------|
| $A_1$             | 7        |          |          |          |
|                     |          | 8        |          |          |
| $A_2$             |          |          | 5        |          |
|                     |          |          |          | 9        |
| $A_3$             |          |          |          | 1        |

#### Solution

##### **Northwest Corner Rule**
| Source \ Destination | B1 (120) | B2 (40)  | B3 (130) | B4 (110) |
|---------------------|----------|----------|----------|----------|
| $A_1$             | 7        |          |          |          |
|                     |          | 8        |          |          |
| $A_2$             |          |          | 5        |          |
|                     |          |          |          | 9        |
| $A_3$             |          |          |          |          |

**Total cost:**
$S = 7 \cdot 120 + 8 \cdot 40 + 5 \cdot 10 + 9 \cdot 130 + 3 \cdot 60 + 6 \cdot 110 = 3230$

##### **Minimal Element Method**
| Source \ Destination | B1 (120) | B2 (160) | B3 (50)  | B4 (90)  |
|---------------------|----------|----------|----------|----------|
| $A_1$             |          |          |          |          |
|                     | 7        |          |          |          |
| $A_2$             |          |          |          |          |
|                     |          | 4        |          |          |
| $A_3$             |          |          |          |          |

**Total cost:**
$S = 1 \cdot 160 + 4 \cdot 120 + 8 \cdot 20 + 2 \cdot 50 + 3 \cdot 30 + 6 \cdot 90 = 1530$

---

### **Problem 3**
Use **Vogel’s Approximation Method** to determine any feasible shipment plan.

#### Shipping Cost Table (same as Problem 2)
| Source \ Destination | B1 (120) | B2 (50)  | B3 (190) | B4 (110) |
|---------------------|----------|----------|----------|----------|
| $A_1$             | 7        |          |          |          |
|                     |          | 8        |          |          |
| $A_2$             |          |          | 5        |          |
|                     |          |          |          | 9        |
| $A_3$             |          |          |          | 1        |

#### Solution
**By Columns**
| Source \ Destination | B1       | B2       | B3 (140) | B4 (110) |
|---------------------|----------|----------|----------|----------|
| $A_1$             |          | 4        |          |          |
|                     | 7 (120)  |          |          |          |
| $A_2$             |          |          |          |          |
|                     |          |          | 5 (30)   |          |
| $A_3$             |          |          |          |          |
|                     |          |          |          | 1 (60)   |

**By Rows**
| Source \ Destination | B1       | B2       | B3 (140) | B4 (50)  |
|---------------------|----------|----------|----------|----------|
| $A_1$             |          |          |          |          |
|                     | 7        |          |          |          |
|                     |          |          |          |          |
|                     |          |          | 5 (20)   |          |
| $A_3$             |          |          |          |          |

**Total cost:**
$S = 1 \cdot 50 + 2 \
