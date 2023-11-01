# 21, 22, 23, 29

## 21. Eigenvalues

**Eigenvectors $\vec x :$ $A\vec x = \lambda \vec x$**

**Eigenvalues $\lambda \in \mathbb C: A\vec x = \lambda \vec x$**

$|A| = 0 ⇒ \lambda = 0$ - eigenvalue

$\sum \lambda = Tr(A)$

$\prod \lambda = |A|$

$A\vec x = \lambda \vec x \iff (A - \lambda I)\vec x = 0 ⇒ |A - \lambda I| = 0$
$I$ - identity matrix

## 22. Diagonalization and Powers of A

$\forall i \in \{1,…,n\} A\vec x_i = \lambda_i \vec x_i$

$S = \begin {bmatrix} x_1 & \ldots & x_n \\\end{bmatrix}$

$AS = S\Lambda , \Lambda = \begin {bmatrix} \lambda_1 & 0 & 0 \\ 0 & \ddots & 0 \\ 0 & 0 & \lambda_n \\ \end{bmatrix}$

$S^{-1}AS = \Lambda$

$Ax = \lambda x ⇒ A^2 x = A\lambda x = \lambda Ax = \lambda^2 x$

$A^2 = S \Lambda^2 S^{-1}$

$A^k = S\Lambda^k S^{-1}$

## 23. Differential Equations and $e^{At}$

$u(0) = \begin{bmatrix} u_1(0) \\ u_2(0) \\ \end{bmatrix} = \begin{bmatrix} 1 \\ 0 \\ \end{bmatrix}$

$\begin{cases} \frac{du_1}{dt} = -u_1 + 2u_2 \\ \frac{du_2}{dt} = u_1 - 2u_2 \\ \end{cases}$

$A = \begin{bmatrix} -1 & 2 \\ 1 & -2 \\ \end{bmatrix}$

$\frac{du}{dt} = Au$

$\lambda = \{0, - 3\}$

$x = \{\begin{bmatrix} 2 \\ 1 \\ \end{bmatrix}, \begin{bmatrix} 1 \\ -1 \\ \end{bmatrix}\}$

$u(t) = c_1 e^{\lambda_1 t} x_1 + c_2 e^{\lambda_2 t} x_2; c_1,c_2 \in \mathbb R$

1. Stability if $u(t) \to 0 ,e^{\lambda t} \to 0 ,Re(\lambda) < 0$
2. Steady state if $\lambda_i = 0$  ^ $\forall j \in \{1,2,...,i-1,i+1,...,n-1,n\}$  $\lambda_i \leq 0$
3. blow up if $\lambda > 0$ ((Для Егора Полякова) если хотя бы одна лямбда больше нуля то $u(t)$ расходится при $u \to \infty$)

$e^{At} = I + At + \frac{(At)^2}{2} + … = \sum\limits_{i = 0}^\infty \frac{(At)^i}{i!}$

$(I - At)^{-1} = I + At + (At)^2 + … = \sum\limits_{i = 0}^\infty (At)^i$

$det(e^A) = e^{\lambda_1 + … + \lambda_n} = e^{Tr(A)}$

## 29. SVD decomposition

$A = S\Lambda S^{-1}$

$A = Q\Lambda Q^T$

$AV = U\Sigma$

[<kbd><br><- Return<br></kbd>](../FinalPrep.md)
