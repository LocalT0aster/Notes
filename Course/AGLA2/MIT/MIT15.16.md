# 15 - 16. Projections onto Subspaces

## 15

### Projection $\vec p$ of $\vec b$ on $\vec a$ $\neq \vec 0$

$\vec e = \vec b - \vec p$  (error vector )
$\vec p = x\vec a, x \in \mathbb R$
$\vec a \cdot (\vec b - \vec p) = 0$ $\iff x\vec a^T\vec a = \vec a^T\vec b$  $\iff x$ $= \frac{\vec a^T\vec b}{\vec a^T\vec a}$   $\vec p = \vec ax = \vec a\frac{\vec a^T\vec b}{\vec a^T\vec a}$

$p=P\vec b, P = \frac{\vec a\vec a^T}{\vec a^T\vec a}$

in general P ‘ll be projection matrix, in this simple case size of this matrix $1\times 1$, and it’s rank = 1

$P^T = P$, $P^2 = P$

$AX=b$ may have no solutions, but we can project $b$ onto $C(A)$ to find closest solution $\bar x : A\bar x = p$

### Projection $\vec p$ of $\vec b$ on plane a : a = <$\vec a_1, \vec a_2$>

$A=[\vec a_1, \vec a_2]$
$\vec e = \vec b - \vec p$
$p = x_1\vec a_1 + x_2\vec a_2$ = Ax

$\begin{cases}
\vec a_1 \cdot (\vec b - \vec p) = 0 \\\
\vec a_2 \cdot (\vec b - \vec p) = 0 \\\
\end{cases}$ $\iff (b-Ax) \perp a$ $\iff$ $\begin{cases}
\vec a_1 \cdot (\vec b - Ax) = 0 \\\
\vec a_2 \cdot (\vec b - Ax) = 0 \\\
\end{cases}$ $\iff$$\begin{bmatrix}
a_1^T \\\
a_2^T \\\
\end{bmatrix}$$[b-Ax] =$ $\begin{bmatrix}
0 \\\
0 \\\
\end{bmatrix}$$\iff A^T(b - Ax) = 0$

Since $b - Ax = e$, $e = N(A^T)$ ⇒ $e\perp$ C(A)

 $x = (A^TA)^{-1} A^Tb$

$p = A(A^TA)^{-1} A^Tb$

$P = A(A^T A)^{-1}A^T$

pay attention to $A(A^T A)^{-1}A^T \neq AA^{-1}A^{T^{-1}} A^T = I$ because $A$ - not square matrix $\iff$ not invertable

### Least squares fitting by a line

we have n = 3 points on plane and want to fit them by best straight line

$(x_1, y_1),(x_2, y_2),(x_3, y_3)$, $y = kx + b$ : $\sum\limits_{i=1}^3 e_i^2$ minimal

$Ax = b$ - no sol
$A^TA\bar x = A^Tb$ - least squares approximation

## ****16. Projection Matrices and Least Squares****

Projection onto perpendicular space
$\vec p = P\vec b$
$\vec p + \vec e = \vec b$
$\vec e = (I - P)b$

[<kbd><br><- Return<br></kbd>](MIT.md)
