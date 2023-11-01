# 18 19 20

## 18. Properties of Determinants

determinant of A = det(A) = |A|
determinant - function : $\underset{n\times n}A \to \mathbb R$
$|A| \neq 0 \iff A$ invertable
Properties that define determinant:

1. $|I| = 1$
2. $|P_{ij}\cdot A| = - |A|$
3. $det\begin{bmatrix}ta & tb \\ c &d \\\end{bmatrix} = t\cdot det\begin{bmatrix}a & b \\ c &d \\\end{bmatrix}$
4. $det\begin{bmatrix}a + a’ & b + b’ \\ c &d \\\end{bmatrix} = det\begin{bmatrix}a & b \\ c &d \\\end{bmatrix} + det\begin{bmatrix}a’ & b’ \\ c &d \\\end{bmatrix}$

Just properties:

1. 2 equal rows ⇒ det = 0
2. E - elimination matrix with 1 at main diagonal ⇒ det(EA) = det(A)
3. Row of 0-es ⇒ |A| = 0
4. $\underset{n\times n}A$ RREF $⇒$ det$(\underset{n\times n}A) = \prod\limits_{i=1}^{n} a_{i,i}$
5. $|A| = 0 \iff A$ singular
6. $det(A\cdot B) = |A|\cdot|B|$
7. $det(2\cdot A) = 2^n \cdot |A|$
8. $|A| = |A^T|$

## 19. Determinant Formulas and Cofactors

$|A| = \sum\limits_{n! terms}+a_{1\alpha} \cdot a_{2\beta} \cdot a_{3\gamma} \cdot …$
$(\alpha, \beta, \gamma, …) = permutations of (1,2,3, …)$

$|\underset{n\times n}A| = \sum\limits_{i = 1}^n (-1)^{n-1} a_{1,i} det(C(a_{1,i}))$

## 20. Cramer's Rule, Inverse Matrix, and Volume

$\begin{bmatrix} a & b \\ c & d \\ \end{bmatrix}^{-1} = \frac{1}{ad - cd} \begin{bmatrix} d & -b \\ -c & a \\ \end{bmatrix}$

$\underset{n\times n}A^{-1} = \frac{1}{|A|} \underset{n\times n}C ^ T$

[<kbd><br><- Return<br></kbd>](../FinalPrep.md)
