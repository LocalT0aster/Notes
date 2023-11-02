# Kholodov lecture notes from @kupamonke

## lecture 4

$(AB)^{-1} = B^{-1}A^{-1}$

if $AA^{-1}=I$ then $(A^T)^{-1}$ = $(A^{-1})^T$

асимптотическая сложность решения квадратной системы уравнений (если за одну операцию принять сложение и умножение) заданной матрицей n$\times$n Ъ($n^3$)

A - matrix

we want to get L and U: A = LU and L-lower triangular matrix, U - upper triangular matrix

иногда мы при этом хотим выебнуться и раскладываем на LDU, D - diagonal matrix

$\begin{bmatrix}  1 & 0 & 0\\0 & 1 & 0\\ 0 & 0 & 1  \end{bmatrix}$

A(X+$\delta$X) = $b +\delta b$

symmetric matrix for $A_{m\times n}$ $A^TA$ (n$\times$n) or $AA^T$ (m$\times$m)

## lecture 6

column space of matrix

column space of$\begin{bmatrix} 1 & 0 & 0\\0 & 1 & 0\\ 0 & 0 & 1\\0 & 0 & 1 \end{bmatrix}$3D subspace of $\mathbb R^4$

null space of A all X : AX=0

## холодов 3

### vector space

(с 1 лекции аглы-1) - Vector space V over $\mathbb R$ is a collection of vectors together with operations
1$)\bar a + \bar b$ 2)$\lambda a, \lambda \in \mathbb R$

union of 2 subspaces - not subspace, intersection - subspace

### column space of matrix A(mxn)

C($A_{m\times n}$)  $\in \mathbb R^m$

$rg(A_{m\times n})D$ in $\mathbb R^m$

The column space of matrix A$\begin{bmatrix} \bar a_1&…&\bar a_m \end{bmatrix}$ = <$\bar a_1,…,\bar a_m$>

row space - пошёл нахуй

### null space

null space of A all X : $AX=0$

ту ту ту

$\forall$ $A_{n\times n}$ : |$A$| $\neq$ 0 $AX=0$ $\iff$ x = $\bar 0$

пиздец как же маркер скрипит

$\forall$ LES AX=B, it solvable $\iff B \in <\bar a_1,…,\bar a_m>$

перекур

row rank = column rank $\forall$ matrix

classification of solutions: (refer to решение СЛУ МФТИ лекция 1)

## Холодов 4

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

[<kbd><br><- Return (FinalPrep)<br></kbd>](FinalPrep.md)
[<kbd><br><- Return (AGLA2)<br></kbd>](AGLA2.md)
