# SVD decomposition, Pseudoinverse

## TOC

- [SVD decomposition, Pseudoinverse](#svd-decomposition-pseudoinverse)
  - [TOC](#toc)
  - [Explanation](#explanation)
  - [Solution](#solution)

## Explanation

Certainly! Let's dive into these topics.

### Singular Value Decomposition (SVD)

Singular Value Decomposition (SVD) is a factorization of a real or complex matrix. It generalizes the eigendecomposition of a square normal matrix to any $m \times n$ matrix via an extension of the polar decomposition. SVD is a fundamental theorem in linear algebra for its wide applications in signal processing, statistics, semantic indexing (like in search engines), and more.

SVD states that any $m \times n$ matrix $A$ can be decomposed into three matrices:

$$
A = U \Sigma V^*
$$

where:

- $U$ is an $m \times m$ unitary matrix (orthogonal in the real case).
- $\Sigma$ (often represented as $S$ in real matrices) is an $m \times n$ diagonal matrix with non-negative real numbers on the diagonal.
- $V^*$ (the conjugate transpose of $V$) is an $n \times n$ unitary matrix (orthogonal in the real case).

The diagonal entries of $\Sigma$ are known as the singular values of $A$. The columns of $U$ and $V$ are called the left-singular vectors and right-singular vectors of $A$, respectively.

### Pseudoinverse

The pseudoinverse, or Moore-Penrose inverse, of a matrix $A$ is a generalization of the inverse matrix. The pseudoinverse exists for any matrix and possesses unique properties that are especially useful when the matrix does not have an inverse (i.e., it is not invertible or square).

For matrix $A$, the pseudoinverse is denoted as $A^+$. If $A$ is a $m \times n$ matrix, then $A^+$ is a $n \times m$ matrix. The pseudoinverse can be computed using the SVD of $A$:

$$
A^+ = V \Sigma^+ U^*
$$

where:

- $V$ and $U$ are the same matrices from the SVD of $A$.
- $\Sigma^+$ is the pseudoinverse of $\Sigma$, which is formed by taking the reciprocal of each non-zero element on the diagonal, leaving zeros in place, and then transposing the matrix.

The pseudoinverse is particularly useful in solving linear least squares problems, which are common in data fitting. It is used when the system of equations does not have a unique solution or when the equation system is over-determined (there are more equations than unknowns).

Would you like to see a numerical example of how SVD or pseudoinverse is computed for a specific matrix?

## Solution

Let's solve this task step by step:

10. Find the SVD and the pseudoinverse of the matrix:
    $A=\begin{bmatrix}
    1 & 0 & 1 \\
    0 & 1 & 0
    \end{bmatrix}$. (10 pts.)

The Singular Value Decomposition (SVD) of the matrix

$$
A = \begin{bmatrix}
    1 & 0 & 1 \\
    0 & 1 & 0
\end{bmatrix}
$$

is given by the matrices $U$, $\Sigma$, and $V^T$, which are:

$$
U = \begin{bmatrix}
    1 & 0 \\
    0 & 1
\end{bmatrix}, \quad
\Sigma = \begin{bmatrix}
    \sqrt{2} & 0 & 0 \\
    0 & 1 & 0
\end{bmatrix}, \quad
V^T = \begin{bmatrix}
    \frac{1}{\sqrt{2}} & 0 & \frac{1}{\sqrt{2}} \\
    0 & 1 & 0 \\
    -\frac{1}{\sqrt{2}} & 0 & \frac{1}{\sqrt{2}}
\end{bmatrix}
$$

The pseudoinverse $A^+$ of the matrix $A$ is:

$$
A^+ = \begin{bmatrix}
    0.5 & 0 \\
    0 & 1 \\
    0.5 & 0
\end{bmatrix}
$$

The pseudoinverse matrix $A^+$ can be used to solve linear systems where $A$ is not square or is rank-deficient, for example in least squares problems.
