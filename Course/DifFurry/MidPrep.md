# Differential Equations Midterm Preparation

## TOC

- [Differential Equations Midterm Preparation](#differential-equations-midterm-preparation)
  - [TOC](#toc)
  - [TODO](#todo)
  - [EX 1](#ex-1)
    - [Singular solutions](#singular-solutions)
      - [4.1)](#41)
      - [4.2)](#42)
      - [4.3)](#43)
    - [Additional parameter](#additional-parameter)
      - [4.4)](#44)
      - [4.5)](#45)
      - [4.6)](#46)
    - [Lab 4 Others](#lab-4-others)
      - [4.9)](#49)
      - [4.10)](#410)
  - [EX 2](#ex-2)
    - [Check for lin. dependance](#check-for-lin-dependance)
      - [6.1)](#61)
      - [6.2)](#62)
      - [6.3)](#63)
    - [Construct a homogeneous lin eq](#construct-a-homogeneous-lin-eq)
      - [6.4)](#64)
      - [6.5)](#65)
      - [6.6)](#66)
    - [Method of variations](#method-of-variations)
      - [6.11)](#611)
      - [6.12)](#612)
      - [6.13)](#613)
    - [Problems 6](#problems-6)
      - [6.14)](#614)
      - [6.15)](#615)
  - [EX 3](#ex-3)
    - [7 Solve](#7-solve)
      - [7.1)](#71)
      - [7.2)](#72)
      - [7.3)](#73)
    - [General form](#general-form)
      - [7.4)](#74)
      - [7.5)](#75)
      - [7.6)](#76)
    - [7 Solve Initial value](#7-solve-initial-value)
      - [7.7)](#77)
      - [7.8)](#78)
  - [EX 4](#ex-4)
  - [EX 5](#ex-5)
    - [Boundary Value Problems](#boundary-value-problems)
      - [7.9)](#79)
      - [7.10)](#710)
      - [7.11)](#711)
  - [Answers](#answers)

## TODO

- [ ] Lab 4: 9, 10, 1-6
- [ ] Lab 6: 1-6, 11-15
- [ ] Lab 7: 1-11

## EX 1

Special solutions for first-order equations - envelopes and families of singular points.

> Lab 4: 9, 10, 1-6

### Singular solutions

Find all solutions of given equations; indicate singular solutions if any; draw the integral curves.

#### 4.1)

> N241

$(y′)^2 − y 2 = 0$

#### 4.2)

> N245

$(y′)^2 − 4y^3 = 0$

#### 4.3)

> N249

$(y′)^3 + y^2 = yy′(y′ + 1)$

### Additional parameter

Solve solve given equation using an additional parameter.

#### 4.4)

> N267

$x = (y′)^3 + y′$

#### 4.5)

> N271

$y = (y′)^2 + 2(y′)^3$

#### 4.6)

> N283

$y′ = e^{xy′/y}$

### Lab 4 Others

#### 4.9)

> N297(в)

Find singular solution of a differential equation for a family of curves $y = C(x − C)^2$.

#### 4.10)

> N298

Define a curve, for which any tangent line and coordinate axes define a triangle of area $2a^2$.

## EX 2

Problems of linear independence of a system of functions and the Wronskian determinant.

> Lab 6: 1-6, 11-15

### Check for lin. dependance

Investigate if these functions are linearly dependent.

#### 6.1)

> N641

$(x+2), (x-2)$

$\begin{vmatrix}
    x+2&x-2\\
    1&1
\end{vmatrix} = 4 \ne 0 =>$
lin. indep.

#### 6.2)

> N660

$x^2,x|x|$

To determine if the functions $f(x) = x^2$ and $g(x) = x|x|$ are linearly dependent, we can set up the equation:

$$
c_1 f(x) + c_2 g(x) = 0
$$

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

$$
c_1 x^2 + c_2 x^2 = 0
$$

2. For $x < 0$:

$$
c_1 x^2 - c_2 x^2 = 0
$$

Let's solve for $c_1$ and $c_2$ in each case.

For $x \geq 0$, the relationship between the constants is $c_1 = -c_2$.

For $x < 0$, the relationship between the constants is $c_1 = c_2$.

This means that there isn't a single pair of constants $c_1$ and $c_2$ (other than the trivial solution where both are zero) that will make the linear combination of the two functions equal to zero for all $x$.

Hence, the functions $f(x) = x^2$ and $g(x) = x|x|$ are linearly independent.

#### 6.3)

> N649

$x, e^x, xe^x$

$$
\begin{vmatrix}
    x&e^x&xe^x\\
    1&e^x&e^x+xe^x\\
    0&e^x&2e^x+xe^x
\end{vmatrix}
 = x \begin{vmatrix}
    e^x&e^x+xe^x\\
    e^x&2e^x+xe^x
\end{vmatrix}
- \begin{vmatrix}
    e^x&xe^x\\
    e^x&2e^x+xe^x
\end{vmatrix} =
$$

$=2xe^{2x}+x^2e^{2x}-xe^{2x}-x^2e^{2x}-2e^{2x}-xe^{2x}+xe^{2x}=\\
=e^{2x}(x-2)=>$ lin. indep.

### Construct a homogeneous lin eq

Construct a homogeneous linear equation ofminimal order which has the following certain solutions.

#### 6.4)

> N674

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

#### 6.5)

> N676

$3x, x − 2, e^x + 1$

#### 6.6)

> N678

$e^x , \sinh(x), \cosh(x)$

### Method of variations

Find a solution of the equations using method of variations of parameters

#### 6.11)

> N575

$y'' − 2y′ + y = \frac{e^x}{x}$

#### 6.12)

> N580

$y′′ + y = 2 sec3(x)$

#### 6.13)

> N581

$x^3(y′′ − y ) = x^2 − 1$

### Problems 6

#### 6.14)

> N582

$y′′ − 2y′ + y = 0, y(2) = 1, y′(2) = −2$

#### 6.15)

> N586

$y′′′ − y′ = 0, y(0) = 3, y′(0) = −1, y′′(0) = 1$

## EX 3

Problems of solving non-homogeneous equations with constant coefficients and special right-hand sides.

> Lab 7: 1-8

### 7 Solve

Solve following equations:

#### 7.1)

> N533

$y′′ − 2y′ − 3y = e^{4x}$

#### 7.2)

> N544

$y′′ − 9y = e^{3x}\cos(x)$

#### 7.3)

> N546

$y′′ + y = x\sin(x)$

### General form

For given equations find general form for undetermined coefficients only.

#### 7.4)

> N549

$y′′ − 2y′ + 2y = e^x + x\cos(x)$

#### 7.5)

> N556

$y′′′ + y′ = \sin(x) + x\cos(x)$

#### 7.6)

> N563

$y^{IV} + y′′ = 7x − 3\cos(x)$

### 7 Solve Initial value

Find solution of given initial value problems.

#### 7.7)

> N583

$y′′ + y = 4e^x, y(0) = 4, y′(0) = −3$

#### 7.8)

> N588

$y^{IV} + y′′ = 2\cos(x), y(0) = −2, y′(0) = 1, y′′(0) = y′′′(0) = 0$

## EX 4

Tasks for using the method of variation of constants.

> Lab 6: 11-13

Covered in ex2.

- [6.11](#611)
- [6.12](#612)
- [6.13](#613)

## EX 5

Boundary value problems.

> Lab 7: 9-11

### Boundary Value Problems

Find solution of given boundary value problems.

#### 7.9)

> N751

$y′′ − y = 2x, y(0) = 0, y(1) = −1$

#### 7.10)

> N755

$y′′ + y = 1, y(0) = 0, y(\pi) = 0$

#### 7.11)

> N758

$y′′ − y = 1, y(0) = 0, y|_{x\rightarrow \infty}$ is bounded

## Answers

- [4.1)](#41) $y=Ce^{\pm x}$
- [4.2)](#42) $y(x+C)^2=1;y=0$
- [4.3)](#43) $4y=(x+C)^2;y=Ce^x$
- [4.4)](#44) $x=x=p^3+p,4y=3p^4+2p^2+C$
- [4.5)](#45) $x=3p^2+2p+C,y=2p^3+p^2;y=0$
- [4.6)](#46) $Cx=\ln(Cy);y=ex$
- [4.9)](#49) $y=0,27y=4x^3$
- [4.10)](#410) $xy=\pm a^2$
- [6.1)](#61) $indep$
- [6.2)](#62) $indep$
- [6.3)](#63) $indep$
- [6.4)](#64) $y''-y'\text{ctg}(x)=0$ or $y''\sin(x)-y'\cos(x)=0$
- [6.5)](#65) $y'''-y''=0$
- [6.6)](#66) $y''-y'=0$
- [6.11)](#611) $y=e^x(x\ln(|x|)+C_1x+C_2)$
- [6.12)](#612) $y=C_1\cos(x)+C_2\sin(x)-\frac{\cos(2x)}{\cos(x)}$
- [6.13)](#613) $y=-\frac{1}{x}+C_1e^x+C_2e^{-x}$
- [6.14)](#614) $y=(7-3x)e^{x-2}$
- [6.15)](#615) $y=2+e^{-x}$
- [7.1)](#71) $y=C_1e^{-x}+C_2e^{3x}$
- [7.2)](#72) $y=c_1e^{3x}+C_2e^{-3x}+e^{3x}(\frac{6}{37}\sin(x)-\frac{1}{37}\cos(x))$
- [7.3)](#73) $y=(C_1-\frac{x^2}{4})\cos(x)+(C_2+\frac{x}{4})\sin(x)$
- [7.4)](#74) $-$
- [7.5)](#75) $-$
- [7.6)](#76) $-$
- [7.7)](#77) $y=2\cos(x)-5\sin(x)+2e^x$
- [7.8)](#78) $y=x-x\sin(x)-2\cos(x)$
- [7.9)](#79) $y=(\frac{shx}{sh1})-2x$
- [7.10)](#710) $no solution$
- [7.11)](#711) $y=e^{-x}-1$

[<kbd><br><- Return<br></kbd>](DifFurry.md)
