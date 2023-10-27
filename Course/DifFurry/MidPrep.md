# Differential Equations Midterm Preparation

## TOC

- [Differential Equations Midterm Preparation](#differential-equations-midterm-preparation)
  - [TOC](#toc)
  - [EX 1](#ex-1)
  - [EX 2](#ex-2)
    - [Check for lin. dependance](#check-for-lin-dependance)
      - [lin. dependance 1)](#lin-dependance-1)
      - [lin. dependance 2)](#lin-dependance-2)
      - [lin. dependance 3)](#lin-dependance-3)
    - [Construct a homogeneous lin eq](#construct-a-homogeneous-lin-eq)
      - [1)](#1)
  - [EX 3](#ex-3)
  - [EX 4](#ex-4)
  - [EX 5](#ex-5)

## EX 1

Special solutions for first-order equations - envelopes and families of singular points.
> Lab 4: 9, 10, 1-6

## EX 2

Problems of linear independence of a system of functions and the Wronskian determinant.
> Lab 6: 1-6, 11-15

### Check for lin. dependance

Investigate if these functions are linearly dependent.

#### lin. dependance 1)

$(x+2), (x-2)\\
\begin{vmatrix}
    x+2&x-2\\
    1&1
\end{vmatrix}=4 \ne 0 =>$ lin. indep.

#### lin. dependance 2)

$x^2,x|x|$

To determine if the functions $f(x) = x^2$ and $g(x) = x|x|$ are linearly dependent, we can set up the equation:

$$c_1 f(x) + c_2 g(x) = 0$$

Where $c_1$ and $c_2$ are constants. If there exist non-trivial solutions (i.e., not both zero) for $c_1$ and $c_2$ that satisfy this equation for all $x$, then the functions are linearly dependent. Otherwise, they are linearly independent.

Let's break it down:

1. For $f(x) = x^2$:
   If $x \geq 0$ then $f(x) = x^2$
   If $x < 0$ then $f(x) = x^2$

2. For $g(x) = x|x|$:
   If $x \geq 0$ then $g(x) = x^2$
   If $x < 0$ then $g(x) = -x^2$

Given these expressions for the two functions, let's examine their linear combination for both the cases of $x$:

1. For $x \geq 0$:
$$c_1 x^2 + c_2 x^2 = 0$$

2. For $x < 0$:
$$c_1 x^2 - c_2 x^2 = 0$$

Let's solve for $c_1$ and $c_2$ in each case.

For $x \geq 0$, the relationship between the constants is $c_1 = -c_2$.

For $x < 0$, the relationship between the constants is $c_1 = c_2$.

This means that there isn't a single pair of constants $c_1$ and $c_2$ (other than the trivial solution where both are zero) that will make the linear combination of the two functions equal to zero for all $x$.

Hence, the functions $f(x) = x^2$ and $g(x) = x|x|$ are linearly independent.

#### lin. dependance 3)

$x, e^x, xe^x\\$
$\begin{vmatrix}
    x&e^x&xe^x\\
    1&e^x&e^x+xe^x\\
    0&e^x&2e^x+xe^x
\end{vmatrix}
=x\begin{vmatrix}
    e^x&e^x+xe^x\\
    e^x&2e^x+xe^x
\end{vmatrix}
-\begin{vmatrix}
    e^x&xe^x\\
    e^x&2e^x+xe^x
\end{vmatrix}=$
$=2xe^{2x}+x^2e^{2x}-xe^{2x}-x^2e^{2x}-2e^{2x}-xe^{2x}+xe^{2x}=\\
=e^{2x}(x-2)=>$ lin. indep.

### Construct a homogeneous lin eq

Construct a homogeneous linear equation ofminimal order which has the following certain solutions.

#### 1)

$1, \cos(x)$

Thank you for pointing that out. Let's reassess the problem.

Given the solutions:

1. $y_1 = 1$ - This suggests that $y_1' = 0$ and $y_1'' = 0$.
2. $y_2 = \cos(x)$ - We've already computed the first three derivatives, which are $y_2' = -\sin(x)$, $y_2'' = -\cos(x)$, and $y_2''' = \sin(x)$.

Now, let's consider a general second-order differential equation:

$$
y'' + a_1 y' + a_0 y = 0
$$

Given that $y_1 = 1$ is a solution, all its derivatives are zero, and we can deduce:

$$
a_0 = 0
$$

Next, plugging in the second solution $y_2 = \cos(x)$ and its derivatives, we get:

$$
y_2'' + a_1 y_2' = 0
$$

Given our previous calculations, we can solve for $a_1$. Let's proceed with this approach.

The coefficient $a_1$ is found to be $-\frac{1}{\tan(x)}$, which can be expressed as $-\cot(x)$ or $-\text{ctg}(x)$.

Thus, the homogeneous linear differential equation of minimal order that has the solutions $y_1 = 1$ and $y_2 = \cos(x)$ is indeed:

$$
y'' - y' \cdot \text{ctg}(x) = 0
$$

Thank you for pointing out the oversight, and I apologize for the confusion earlier. Your provided solution is correct.

## EX 3

Problems of solving non-homogeneous equations with constant coefficients and special right-hand sides.
> Lab 7: 1-8

## EX 4

Tasks for using the method of variation of constants.
> Lab 6: 11-13

## EX 5

Boundary value problems.
> Lab 7: 9-11

[<kbd><br><- Return<br></kbd>](DifFurry.md)
