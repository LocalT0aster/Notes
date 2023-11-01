# AGLA 2 Final preparation

## Notes From @kupamonke

### Нахождение обратной матрицы $2 \times 2$

$A = \begin {bmatrix} a & b \\ c & d \\ \end{bmatrix}$

$A^{-1} = \frac{1}{|A|}\begin {bmatrix} d & -b \\ -c & a \\ \end{bmatrix}$

### Нахождение обратной матрицы $3 \times 3$

$A = \begin{bmatrix}
a & b & c \\
d & e & f \\
g & h & i \\
\end{bmatrix}$

$A^{-1} = \frac{1}{|A|} \bar A$

$\bar A = {(A^c_{+-})}^T$

$A_{+-}^c$ - матрица дополнительных миноров (кофакторов) $A_{+-}^c[i][j]$ это **определитель матрицы, полученной из исходной вычеркиванием строки $i$ и столбца $j$, при этом если $(i+j)\%2 = 1$ то мы умножаем полученный определитель на $-1$**.

### Нахождение собственный значений и векторов (**Eigenvalues and Eigenvectors**)

**Eigenvectors $\vec x :$ $A\vec x = \lambda \vec x$**

**Eigenvalues $\lambda \in \mathbb C: A\vec x = \lambda \vec x$**

$|A| = 0 ⇒ \lambda = 0$ - eigenvalue

$\sum \lambda = Tr(A)$

$\prod \lambda = |A|$

$A\vec x = \lambda \vec x \iff (A - \lambda I)\vec x = 0 ⇒ |A - \lambda I| = 0$
$I$ - identity matrix

Из $|A - \lambda I| = 0$ находим собственные значения, зная их из $(A - \lambda I)\vec x = 0$ находим собсвенные вектора для каждого собственного значения $(x_i = N(A-\lambda_i I))$

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ea507abd-6458-45dd-8dd9-7fa168128c97/Untitled.png)

### 1 задание

$S = \begin {bmatrix} x_1 & \ldots & x_n \\\end{bmatrix}$

$AS = S\Lambda , \Lambda = \begin {bmatrix} \lambda_1 & 0 & 0 \\ 0 & \ddots & 0 \\ 0 & 0 & \lambda_n \\ \end{bmatrix}$

$S^{-1}AS = \Lambda$

$Ax = \lambda x ⇒ A^2 x = A\lambda x = \lambda Ax = \lambda^2 x$

$A^2 = S \Lambda^2 S^{-1}$

$A^k = S\Lambda^k S^{-1}$

![1.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5b404105-730f-4beb-9a2c-8c827d90767c/1.jpg)

### 2 задание

Диагонализируем матрицы A и B
$A = Q\Lambda Q^{-1}$
$B = S \Lambda S^{-1}$
$B = M^{-1}AM$
$S \Lambda S^{-1} = M^{-1} Q\Lambda Q^{-1} M ⇒ S = M^{-1}Q ⇒ M = QS^{-1}$

$M = QS^{-1}$

![2.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f8267e99-ea27-40e8-a6fc-0ce674874e99/2.jpg)

### 3 задание

$A^T = A ⇒$ $A = \begin{bmatrix}
a & b & c \\
b & d & e \\
c & e & f \\
\end{bmatrix}$

Эту матрицу мы просто подставляем в уравнение и брутфорсом распиываем его

Матрица позитивна если выполнгено хотя бы одно из условий

1. $\lambda > 0$
2. subdeterminants > 0
3. all pivots > 0
4. $\forall x \neq \vec 0 x^T A x > 0$

### 4 задание

$\frac{d^2u}{dt^2} = A u$

$A ⇒ \{\lambda_1 … \lambda_n \} , \{x_1 … x_n \}$

$\omega_i = \sqrt{-\lambda_i}$

$u = (c_1 e^{i\omega_1 t} + \alpha_1 e^{-\omega_1t})\cdot x_1 + …$

$u = (a_1 cos(\omega_1 t) + b_1 sin(\omega_1 t))x_1 + …$

$\forall i$ $a_i, b_i, c_i, \alpha_i \in \mathbb R$

![4.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/db36b320-7ecd-4acd-93c2-c535290d3a4e/4.jpg)

### 5 задание

$Ax = b$ - no sol
$A^TA\bar x = A^Tb$ - least squares approximation

В этом задании вектор x будет равен $\begin {bmatrix} a\cdot sin(b) \\
a\cdot cos(b) \\ \end{bmatrix}$

![3.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/69dfdd04-6fe8-4604-87ff-0ff372d67a3b/3.jpg)

### 6 задание

<https://yutsumura.com/eigenvalues-of-a-hermitian-matrix-are-real-numbers/>

## Cholodov lecture notes from @kupamonke

### lecture 4

$(AB)^{-1} = B^{-1}A^{-1}$

if $AA^{-1}=I$ then $(A^T)^{-1}$ = $(A^{-1})^T$

асимптотическая сложность решения квадратной системы уравнений (если за одну операцию принять сложение и умножение) заданной матрицей n$\times$n Ъ($n^3$)

A - matrix

we want to get L and U: A = LU and L-lower triangular matrix, U - upper triangular matrix

иногда мы при этом хотим выебнуться и раскладываем на LDU, D - diagonal matrix

$\begin{bmatrix}  1 & 0 & 0\\0 & 1 & 0\\ 0 & 0 & 1  \end{bmatrix}$

A(X+$\delta$X) = $b +\delta b$

symmetric matrix for $A_{m\times n}$ $A^TA$ (n$\times$n) or $AA^T$ (m$\times$m)

### lecture 6

column space of matrix

column space of$\begin{bmatrix} 1 & 0 & 0\\0 & 1 & 0\\ 0 & 0 & 1\\0 & 0 & 1 \end{bmatrix}$3D subspace of $\mathbb R^4$

null space of A all X : AX=0

### холодов 3

#### vector space

(с 1 лекции аглы-1) - Vector space V over $\mathbb R$ is a collection of vectors together with operations
1$)\bar a + \bar b$ 2)$\lambda a, \lambda \in \mathbb R$

union of 2 subspaces - not subspace, intersection - subspace

#### column space of matrix $A_{m\times n}$

C($A_{m\times n}$)  $\in \mathbb R^m$

$rg(A_{m\times n})D$ in $\mathbb R^m$

The column space of matrix A$\begin{bmatrix} \bar a_1&…&\bar a_m \end{bmatrix}$ = <$\bar a_1,…,\bar a_m$>

row space - пошёл нахуй

#### null space

null space of A all X : $AX=0$

ту ту ту

$\forall$ $A_{n\times n}$ : |$A$| $\neq$ 0 $AX=0$ $\iff$ x = $\bar 0$

пиздец как же маркер скрипит

$\forall$ LES AX=B, it solvable $\iff B \in <\bar a_1,…,\bar a_m>$

перекур

row rank = column rank $\forall$ matrix

classification of solutions: (refer to решение СЛУ МФТИ лекция 1)

### Холодов 4

| $rg(A_{m\times n}) = r$ | full column and row rank $r=n=m$ | full column rank $r=n<m$ | full row rank $r = m < n$ | $r<m, r < n$ |
| --- | --- | --- | --- | --- |
| RREF | $I_{n\times n}$ | $\begin{bmatrix} I_{n\times n}\\0_{m-n\times n}\end{bmatrix}$ | $\begin{bmatrix} I_{m\times m} & F_{m\times n-m}\end{bmatrix}$ | $\begin{bmatrix} I_{r\times r} & F_{r\times n-r}\\0_{m-r\times r} & 0_{m-r \times n - r}\end{bmatrix}$ |
| Number of solutions of $A\vec x=\vec b$ | 1 | $\vec b \in C(A) ⇒ 1$
$\vec b \not\in C(A) ⇒ \emptyset$ | $\infty$ | $\vec b \in C(A) ⇒ \infty$
$\vec b \not\in C(A) ⇒ \emptyset$ |

$\begin{bmatrix} I_{r\times r} & F_{r\times n-r}\\0_{m-r\times r} & 0_{m-r \times n - r}\end{bmatrix}$$\vec x = \vec b$  ⇒ $\vec x = \vec b + \begin{bmatrix} -F_{r\times n-r}\\ I_{m-r \times n - r}\end{bmatrix}\vec ъ$, where $\vec ъ$ - vector of arbitrary constants

4 fundamental matrix spaces of matrix $A_{m\times n}$:
r - rank of A

1) $N(A)$ null space {$\vec x | A\vec x = 0$} - $(n-r)D$ subspace in $\mathbb R^n$
2) $N(A^T)$ left null space {$\vec x | A^T\vec x = 0$} - $(m - r)D$ subspace in $\mathbb R^m$
3) $C(A)$ column space $rD$ subspace in $\mathbb R^m$
4) $C(A^T)$ row space $rD$ subspace in $\mathbb R^n$

subspace A $\perp$ subspace B$\iff$$\forall \vec a \in A, \vec b \in B$ ($\vec a \perp \vec b$)

$N(A^T)$ orthogonal $C(A)$
$N(A)$ orthogonal $C(A^T)$

## MIT Lecture notes from @kupamonke

- [9. Independence, Basis, and Dimension](MIT/MIT09.md)
- [10. The Four Fundamental Subspaces](MIT/MIT10.md)
- [15 - 16. Projections onto Subspaces](MIT/MIT15.16.md)
- [17. Orthogonal Matrices and Gram-Schmidt](MIT/MIT17.md)
- [18, 19, 20](MIT/MIT18.19.20.md)
- [21 (test 2)](MIT/MIT21.22.23.29.md)
- [24](MIT/MIT24.md)
- [28. Similar Matrices and Jordan Form](MIT/MIT28.md)

[<kbd><br><- Return<br></kbd>](AGLA2.md)
