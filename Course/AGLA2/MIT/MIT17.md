# 17. Orthogonal Matrices and Gram-Schmidt

## Orthogonal Matrices

orthogonal basis - basis $(e_1, e_2, … ,e_n)$ called orthogonal if $\forall i,j \in$ {$1,2,…,n$} $: i\neq j$ $e_i \perp e_j$

orthonormal basis - basis $(e_1, e_2, … ,e_n)$ called orthonormal if it orthogonal and $\forall i \in$ {$1,2,…,n$} $|e_i| = 1$

$(q_1,…,q_n)$ - orthonormal basis
$Q=\begin{bmatrix} q_1 q_2 … q_n\end{bmatrix}$

$Q^TQ = I$, because $q_i\cdot q_j = \begin{cases} 0, i\neq j \\ 1, i = j\end{cases}$

Matrix $A$ called orthogonal if it square and it’s inverse $A^{-1} = A ^ T$

orthogonal matrix $\iff$ columns orthonormal basis

Q has orthonormal columns ⇒ projection matrix onto $C(Q)$ $P = Q(Q^TQ)^{-1}Q^T = QQ^T$($= I$ if $Q$ - square)

## Gram-Schmidt

$(a,b,c)$ - independent vectors, columns of matrix $A$
our goal $A \to W \to Q$ : columns $(A,B,C)$ of $W$ are orthogonal, $Q$ is orthogonal matrix
$A=a$
$B = b - \frac{A^Tb}{A^TA}A$
$C = c - \frac{A^Tc}{A^TA}A - \frac{B^Tc}{B^TB}B$
$q_1 = \frac{A}{|A|}$
$q_2 = \frac{B}{|B|}$
$q_3 = \frac{C}{|C|}$
$A=QR$

$A = (\vec a_1,…,\vec a_n)$ - matrix of independent vectors
$Q = (\vec q_1,…,\vec q_n)$ - orthogonal matrix
$R$ - upper triangular

$q_1 = \frac{\vec a}{|\vec a|}$

$q_2^* = a_2 - (a_2\cdot q_1)q_1, q_2 = \frac{q_2^*}{|q_2^*|}$
$q_3^* = a_3 - (a_3\cdot q_1)q_1 - (a_3\cdot q_2)q_2, q_3 = \frac{q_3^*}{|q_3^*|}$
$R = Q^TA$

$R = \begin{bmatrix} |\vec a| & a_2\cdot q_1 & a_3\cdot q_1 \\ 0 & |q_2^*| & a_3\cdot q_2 \\ 0 & 0 & |q_3^*| \end{bmatrix}$

[<kbd><br><- Return<br></kbd>](MIT.md)
