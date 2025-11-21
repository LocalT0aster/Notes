# CSE206 — Week 03 Notes — Random vars (pmf/cdf, discrete families, joint/marginal/conditional)
**Lectures:** CSE206_Fa24-03.pdf
**Lab/Tutorial:** week03.pdf

## 1. Big picture (5–10 bullets)
- This week introduces random variables as functions on a probability space that produce numerical outcomes.
- We define indicator random variables, which connect events and random variables and are modeled as Bernoulli variables.
- Every random variable has a distribution function (cdf), and discrete ones also have a probability mass function (pmf).
- We focus on discrete random variables and key examples: Bernoulli, Binomial, discrete uniform, Geometric, and Poisson.
- Independence is extended from events to random variables, including equivalent conditions in terms of pmfs.
- Random vectors (several random variables together) are introduced with joint, marginal, and conditional pmfs.
- The lab builds practice in working with joint distributions, transforming random variables, and recognizing standard discrete distributions.

## 2. Key concepts and definitions

### 2.1 Random variables
- Plain-language definition.
  - A random variable is a numerical quantity whose value depends on the outcome of a random experiment.
  - Formally it is a function defined on the sample space, but usually we think of it just as “the number we measure.”
- Formal definition (if needed).
  - Given a sample space $\Omega$ with σ-algebra $\mathcal{F}$, a random variable $X$ is a function
    $$
    X:\Omega \to \mathbb{R}
    $$
    such that for every real number $x$, the set $\{\omega\in\Omega : X(\omega)\le x\}$ is in $\mathcal{F}$.
- Intuition / mental model.
  - The function $X$ “reads” the outcome $\omega$ and returns a number (e.g., number of heads, total score, waiting time).
  - The measurability condition (“$\{X\le x\}\in\mathcal{F}$”) just says “events described in terms of $X$” are legitimate events.
- Tiny example.
  - Toss a fair coin twice, with $\Omega = \{HH, HT, TH, TT\}$.
  - Let $X$ be “number of heads”: $X(HH)=2$, $X(HT)=1$, $X(TH)=1$, $X(TT)=0$. This is a random variable.

### 2.2 Indicator random variables
- Plain-language definition.
  - An indicator of an event $E$ is a random variable that is 1 when the event happens and 0 otherwise.
- Formal definition (if needed).
  - For $E \in \mathcal{F}$, the indicator function $I(E)$ is
    $$
    I(E)(\omega) = \begin{cases}
    1, & \omega\in E,\\
    0, & \omega\notin E.
    \end{cases}
    $$
- Intuition / mental model.
  - Indicators allow us to translate event statements into algebra with random variables (sums and products).
  - Many combinatorial probability problems can be rewritten using indicator variables and simplified.
- Tiny example.
  - In the network example from lecture 2, indicator variables $I(E_1),\dots,I(E_4)$ for working channels are used; the event “there is communication from $N_1$ to $N_3$” is
    $$
    (I(E_1)+I(E_2))(I(E_3)+I(E_4)) > 0.
    $$
  - Any indicator random variable is a Bernoulli random variable (see 2.6.1).

### 2.3 Distribution function (cdf) of a random variable
- Plain-language definition.
  - The distribution function (also called cumulative distribution function, cdf) of a random variable $X$ tells us, for each real number $x$, the probability that $X$ is at most $x$.
- Formal definition (if needed).
  - For a random variable $X$ on a probability space $(\Omega,\mathcal{F},P)$, its cdf is
    $$
    F_X(x) = P(X \le x), \quad x\in\mathbb{R}.
    $$
- Intuition / mental model.
  - $F_X(x)$ accumulates probability mass as $x$ increases; plotting $F_X$ shows how probability is distributed along the real line.
  - For discrete $X$, the cdf is a step function; for continuous $X$ (later), it will be continuous and usually smooth.
- Basic properties (from lecture).
  - $\lim_{x\to -\infty}F_X(x)=0$.
  - $\lim_{x\to +\infty}F_X(x)=1$.
  - $F_X$ is non-decreasing (never goes down as $x$ increases).
  - $F_X$ is right-continuous (no “jumps” from the right).
- Tiny example.
  - For $X$ = number of heads in two tosses of a fair coin, possible values are 0, 1, 2, and the lecture gives
    $$
    F_X(x)=\begin{cases}
    0, & x<0,\$$2pt]
    1/4, & 0\le x<1,\$$2pt]
    3/4, & 1\le x<2,\$$2pt]
    1, & x\ge 2.
    \end{cases}
    $$

### 2.4 Discrete random variables and probability mass function (pmf)
- Plain-language definition.
  - A random variable is discrete if it takes values only in a countable set (finite or countably infinite), and all probability is concentrated on those values.
- Formal definition (if needed).
  - $X$ is discrete if there exists a countable set $C\subset\mathbb{R}$ such that $P(X\in C)=1$.
  - Its probability mass function (pmf) is
    $$
    p_X(x)=P(X=x),\quad x\in\mathbb{R}.
    $$
  - For a discrete random variable,
    $$
    \sum_{x\in\mathbb{R}} p_X(x) = 1,
    $$
    and since $X$ is discrete, only countably many terms are non-zero.
- Intuition / mental model.
  - Discrete variables are used for counts (number of visitors, tosses until first tails, number of successes, etc.).
  - The pmf is a “table” of probabilities at points; the cdf is the running sum of those probabilities up to $x$.
- Relationship between pmf and cdf (for discrete).
  - If the values of a discrete $X$ with positive probability can be ordered $x_1<x_2<x_3<\dots$, then
    $$
    p_X(x_j) = F_X(x_j) - \lim_{x\to x_j^-}F_X(x).
    $$
  - So the size of the jump of the cdf at $x_j$ equals the pmf value at $x_j$.
- Tiny example.
  - For $X$ = number of heads in two tosses:
    $$
    p_X(0)=1/4,\quad p_X(1)=1/2,\quad p_X(2)=1/4,\quad p_X(x)=0 \text{ otherwise},
    $$
    and the cdf is as in 2.3.

### 2.5 Independence of random variables
- Plain-language definition.
  - Several random variables are independent if knowing the values of some of them does not change the probability distribution of the others.
- Formal definition (if needed).
  - Random variables $\xi_1,\dots,\xi_n$ on the same probability space are independent if for all real numbers $x_1,\dots,x_n$:
    $$
    P(\xi_1\le x_1,\dots,\xi_n\le x_n) = F_{\xi_1}(x_1)\cdots F_{\xi_n}(x_n).
    $$
  - For discrete random variables, this is equivalent to saying that for all $x_1,\dots,x_n$
    $$
    P(\xi_1 = x_1,\dots,\xi_n = x_n) = p_{\xi_1}(x_1)\cdots p_{\xi_n}(x_n),
    $$
    and equivalently that events $\{\xi_1=x_1\},\dots,\{\xi_n=x_n\}$ are independent.
- Intuition / mental model.
  - Independence extends the idea “$P(A\cap B)=P(A)P(B)$” to statements about multiple random variables.
  - For discrete variables, the joint pmf factors into the product of the individual pmfs.
- Tiny example.
  - Independent Bernoulli trials: if $\xi_1,\dots,\xi_n$ are independent $\text{Bernoulli}(p)$ variables, then for any pattern $(x_1,\dots,x_n)\in\{0,1\}^n$,
    $$
    P(\xi_1=x_1,\dots,\xi_n=x_n) = \prod_{j=1}^n p^{x_j}(1-p)^{1-x_j}.
    $$

### 2.6 Notable discrete random variables

#### 2.6.1 Bernoulli random variable
- Definition.
  - A random variable $\xi$ is Bernoulli with parameter $p$ if
    $$
    P(\xi=1)=p,\quad P(\xi=0)=1-p,
    $$
    usually with $q=1-p$. We write $\xi\sim \text{Bernoulli}(p)$.
- Intuition.
  - Models the outcome of a single “yes/no” experiment: success (1) or failure (0).
  - Indicator random variables are Bernoulli.
- Tiny example.
  - Toss a biased coin with probability $p$ of heads. Let $\xi = I(\text{heads})$. Then $\xi\sim\text{Bernoulli}(p)$.

#### 2.6.2 Binomial random variable
- Definition.
  - A random variable $\xi$ is binomial with parameters $n$ and $p$, written $\xi\sim\text{Bin}(n,p)$, if its pmf is
    $$
    p_\xi(x) = \binom{n}{x} p^x(1-p)^{n-x} I(x\in\{0,\dots,n\}).
    $$
- Intuition.
  - Models the number of successes in $n$ independent Bernoulli$(p)$ trials.
  - If $\xi_1,\dots,\xi_n$ are independent $\text{Bernoulli}(p)$ and $\xi = \xi_1+\dots+\xi_n$, then $\xi\sim\text{Bin}(n,p)$ (this is stated and will be proved in the next lecture).
- Tiny example.
  - Toss a coin $n=5$ times with success probability $p$. Then $\xi$ = “number of heads” is $\text{Bin}(5,p)$, and
    $$
    P(\xi=2) = \binom{5}{2} p^2 (1-p)^3.
    $$

#### 2.6.3 Discrete uniform random variable
- Definition.
  - A random variable $\xi$ has a discrete uniform distribution on a finite set $\{s_1,\dots,s_n\}$ if
    $$
    p_\xi(x) = \frac{1}{n} I(x\in\{s_1,\dots,s_n\}),
    $$
    written as $\xi\sim \text{Uni}(n)$ in the lecture.
- Intuition.
  - Each of the $n$ possible values is equally likely.
- Tiny example.
  - Rolling a fair die: $\xi$ = face value has
    $$
    P(\xi = k) = 1/6,\quad k=1,\dots,6.
    $$

#### 2.6.4 Geometric random variable
- Definition.
  - One version (used in the lecture): $\xi\sim\text{Geo}(p)$ has pmf
    $$
    p_\xi(x) = (1-p)^{x-1} p \, I(x\in\{1,2,3,\dots\}).
    $$
  - Alternative version sometimes used:
    $$
    p_\xi(x) = (1-p)^x p \, I(x\in\{0,1,2,\dots\}),
    $$
    with slightly different interpretation.
- Intuition.
  - First version: “trial number of the first success” in independent Bernoulli$(p)$ trials.
  - Second version: “number of failures before the first success.”
- Tiny example.
  - Toss a coin with success probability $p$ until the first head. If $\xi$ is the trial number of the first head, then
    $$
    P(\xi = x) = (1-p)^{x-1} p.
    $$

#### 2.6.5 Poisson random variable
- Definition.
  - A random variable $\xi$ has Poisson distribution with parameter $\lambda>0$, written $\xi\sim\text{Poi}(\lambda)$, if
    $$
    p_\xi(x) = e^{-\lambda} \frac{\lambda^x}{x!} I(x\in\mathbb{N}),
    $$
    where $\mathbb{N} = \{0,1,2,\dots\}$.
- Intuition.
  - Models counts of rare, independent events over a fixed time or space interval (interpretation will be discussed in a later lecture).
- Tiny example (from lab).
  - In a 20-second interval, the number of cars at an intersection may follow $\text{Poi}(6)$; e.g.,
    $$
    P(X=2) = e^{-6}\frac{6^2}{2!}.
    $$

### 2.7 Random vectors, joint, marginal, and conditional pmfs
- Plain-language definition.
  - A random vector is an ordered collection of random variables defined on the same probability space.
  - The joint pmf describes probabilities of all combinations of their values; marginal pmfs give distributions of individual components; conditional pmfs describe one component given another.
- Formal definitions (if needed).
  - Random vector $X = (X_1,\dots,X_d): \Omega\to\mathbb{R}^d$.
  - Joint pmf for discrete $X$:
    $$
    p_X(x_1,\dots,x_d) = P(X_1=x_1,\dots,X_d=x_d),
    $$
    with
    $$
    \sum_{(x_1,\dots,x_d)} p_X(x_1,\dots,x_d) = 1.
    $$
  - For $d=2$, marginals are
    $$
    p_{X_1}(x) = \sum_y p_X(x,y),\quad p_{X_2}(y) = \sum_x p_X(x,y).
    $$
  - For $d=3$, 2D marginals (projections) are sums over the remaining coordinate, e.g.,
    $$
    p_{X_1,X_2}(x,y) = \sum_z p_{X_1,X_2,X_3}(x,y,z),
    $$
    and similarly for others.
  - Conditional pmf of $X_1$ given $X_2=y$ (if $P(X_2=y)>0$):
    $$
    p_{X_1|X_2}(x|y) = \frac{P(X_1=x,X_2=y)}{P(X_2=y)} = \frac{p_X(x,y)}{p_{X_2}(y)}.
    $$
- Intuition / mental model.
  - Joint pmf captures full dependence between components; marginals forget some information; conditional pmfs tell you how one component behaves when the other is fixed.
  - Independence of components shows up as factorization of the joint pmf: $p_X(x,y) = p_{X_1}(x)p_{X_2}(y)$.
- Tiny example (from lecture Example 3.1 idea).
  - Two dice are thrown. Let $X_1$ = sum of the two results, $X_2$ = difference. The pair $X=(X_1,X_2)$ is a random vector. Its joint pmf is defined on the set of possible $(\text{sum},\text{difference})$ pairs, and marginals can be obtained by summing over the other coordinate.

## 3. Core formulas and how to use them

### 3.1 Cdf and pmf for discrete random variables
- Formulas.
  - Cdf: $F_X(x)=P(X\le x)$.
  - Pmf: $p_X(x)=P(X=x)$.
  - Relationship (discrete case with ordered support $x_1<x_2<\dots$):
    $$
    p_X(x_j) = F_X(x_j) - \lim_{x\to x_j^-} F_X(x).
    $$
- When to use them.
  - To compute probabilities like $P(a\le X\le b)$ for discrete $X$: sum $p_X(x)$ over integers in that range, or use differences of the cdf.
- Common mistakes.
  - Mixing up cdf and pmf; the cdf is cumulative, the pmf is pointwise.
  - Forgetting that the cdf for discrete $X$ is right-continuous with jumps at points where $p_X(x)>0$.

### 3.2 pmfs of Bernoulli, Binomial, Geometric, Poisson (discrete uniform is trivial)
- Bernoulli$(p)$.
  - $$
    P(\xi=1)=p,\quad P(\xi=0)=1-p.
    $$
- Binomial$(n,p)$.
  - $$
    P(\xi=x) = \binom{n}{x} p^x(1-p)^{n-x},\quad x=0,1,\dots,n.
    $$
- Geometric$(p)$ (version counting trial of first success).
  - $$
    P(\xi=x) = (1-p)^{x-1}p,\quad x=1,2,\dots.
    $$
- Poisson$(\lambda)$.
  - $$
    P(\xi=x) = e^{-\lambda}\frac{\lambda^x}{x!},\quad x=0,1,2,\dots.
    $$
- Discrete uniform on $\{s_1,\dots,s_n\}$.
  - $$
    P(\xi = s_j) = 1/n,\quad j=1,\dots,n.
    $$
- When to use them.
  - Bernoulli: single success/failure.
  - Binomial: fixed number of independent trials with same success probability.
  - Geometric: number of independent trials until first success.
  - Poisson: counts of events in continuous time/space where events are rare and roughly independent (interpretation in later lectures).
- Common mistakes.
  - Using Binomial when the number of trials is not fixed.
  - Using Geometric when the probability of success changes between trials.
  - Forgetting to restrict $x$ to its proper support (e.g., nonnegative integers).

### 3.3 Independence and joint pmf
- Formula (discrete case).
  - Random variables $\xi_1,\dots,\xi_n$ are independent iff
    $$
    P(\xi_1 = x_1,\dots,\xi_n=x_n) = \prod_{j=1}^n p_{\xi_j}(x_j)
    $$
    for all $(x_1,\dots,x_n)$.
- When to use it.
  - To check whether two discrete random variables are independent: compute joint probabilities and compare to product of marginals.
  - To construct a joint distribution from known marginals under an independence assumption.
- Common mistakes.
  - Trying to verify independence using only marginal pmfs without checking joint probabilities.
  - Assuming independence from just one equality like $P(\xi_1=x_1|\xi_2=x_2)=P(\xi_1=x_1)$ for a single pair $(x_1,x_2)$; full independence must hold for all values.

### 3.4 Conditional pmf for discrete random vectors
- Formula.
  - If $X=(X_1,X_2)$ is a discrete random vector and $P(X_2=y)>0$, then
    $$
    p_{X_1|X_2}(x|y) = \frac{P(X_1=x,X_2=y)}{P(X_2=y)} = \frac{p_X(x,y)}{p_{X_2}(y)}.
    $$
- When to use it.
  - When you know or can compute the joint pmf and marginal pmf and need the conditional distribution of one component given another.
  - To formalize statements like “given that the difference of the dice outcomes is 0, the sum is uniformly distributed over even numbers between 2 and 12.”
- Common mistakes.
  - Forgetting to divide by $P(X_2=y)$.
  - Using the formula when $P(X_2=y)=0$; in that case the conditional pmf is conventionally taken as 0 for all $x$.

## 4. Worked examples

### 4.1 Birthday problem (warm-up from lecture)
- Setup.
  - There are $N$ people in a room. Assume 365 equally likely birthdays and ignore leap years.
  - Question: what is the probability that at least two people share a birthday?
- Step 1: define the sample space.
  - Each person gets a birthday in $\{1,\dots,365\}$.
  - A sample point is an ordered $N$-tuple $(\omega_1,\dots,\omega_N)$ with $\omega_j\in\{1,\dots,365\}$.
  - The sample space
    $$
    \Omega = \{(\omega_1,\dots,\omega_N): \omega_j\in\{1,\dots,365\}\}
    $$
    has size $365^N$.
- Step 2: compute the probability that all birthdays are different.
  - For all different birthdays, the first person has 365 choices, the second 364 choices, the third 363, and so on down to $365-N+1$.
  - Number of favorable outcomes: $365\cdot 364\cdot \dots\cdot (365-N+1)$.
  - Probability of all distinct birthdays:
    $$
    P(\text{all different}) = \frac{365\cdot 364\cdot \dots\cdot (365-N+1)}{365^N}.
    $$
- Step 3: compute the probability of at least one match.
  - Let $A$ be the event “at least two people share a birthday”. Then $A^c$ is “all birthdays are different”.
  - So
    $$
    P(A) = 1 - P(A^c) = 1 - \frac{365\cdot 364\cdot \dots\cdot (365-N+1)}{365^N}.
    $$
  - The lecture notes that for $N=23$ this probability already exceeds $1/2$.
- Check your intuition.
  - It is surprisingly likely to have a shared birthday with only 23 people; the key is that there are many possible pairs, not just matching your own birthday.

### 4.2 Cdf and pmf of the number of heads in two coin tosses
- Setup (from lecture).
  - Toss a fair coin twice. Let $X$ = number of heads in the two throws.
  - Sample space $\Omega = \{HH, HT, TH, TT\}$, each outcome has probability $1/4$.
- Step 1: compute the pmf.
  - $X(\text{TT}) = 0$: one outcome, probability $1/4$.
  - $X(\text{HT}) = 1$ and $X(\text{TH}) = 1$: two outcomes, combined probability $2/4=1/2$.
  - $X(\text{HH}) = 2$: one outcome, probability $1/4$.
  - So
    $$
    p_X(0)=1/4,\quad p_X(1)=1/2,\quad p_X(2)=1/4,\quad p_X(x)=0 \text{ otherwise}.
    $$
- Step 2: compute the cdf $F_X(x)=P(X\le x)$.
  - For $x<0$, event $\{X\le x\}$ is empty, so $F_X(x)=0$.
  - For $0\le x<1$, only $X=0$ qualifies, so $F_X(x)=P(X=0)=1/4$.
  - For $1\le x<2$, $X=0$ or $X=1$ qualifies, so $F_X(x)=P(X=0)+P(X=1)=1/4+1/2=3/4$.
  - For $x\ge 2$, all outcomes satisfy $X\le x$, so $F_X(x)=1$.
  - This matches the piecewise function given in the lecture.
- Step 3: relate jumps of cdf to pmf.
  - At $x=0$, jump size is $F_X(0)-\lim_{x\to0^-}F_X(x)=1/4-0=1/4=p_X(0)$.
  - At $x=1$, jump size is $3/4-1/4=1/2=p_X(1)$.
  - At $x=2$, jump size is $1-3/4=1/4=p_X(2)$.
- Check your intuition.
  - This example shows how a discrete pmf and cdf encode the same information: the pmf gives probabilities at points, and the cdf is built from their cumulative sum.

## 5. Lab/Tutorial essentials (week03.pdf)

### 5.1 What the lab asked you to do
- Joint distributions and indicator variables.
  - Task 1: Let $\xi$ be the number of heads in two fair coin tosses and $\eta = I(\xi=2)$. Compute $P(\xi=x,\eta=y)$ for all suitable $(x,y)$.
  - Task 2: Let $\xi$ be Bernoulli$(p)$, define $\eta = 1-\xi$, $\zeta = \xi\eta$. Compute joint distributions $P(\xi=x,\eta=y)$ and $P(\xi=x,\zeta=z)$ for $0\le x,y,z\le1$.
- Derived discrete distributions and pmfs.
  - Task 3: Masha tosses $n$ coins, each showing tails with probability $p$. Tails are tossed again once. Find the pmf of the number of tails in the second round.
  - Task 4: Independent random variables $\xi$ and $\eta$ with the same pmf $p(x)=2^{-x}I(x\in\mathbb{N})$. Find $P(\min\{\xi,\eta\}\le x)$, $P(\eta>\xi)$, and $P(\xi\text{ divides }\eta)$.
- Sums of discrete random variables and conditional distributions.
  - Task 5: Independent Poisson r.v.s $\xi\sim\text{Poi}(\mu)$, $\eta\sim\text{Poi}(\nu)$. Show that $\xi+\eta\sim\text{Poi}(\mu+\nu)$ and that the conditional distribution of $\xi$ given $\xi+\eta=n$ is binomial; find its parameters.
  - Task 6: Prove that the sum of independent $\text{Bin}(n,p)$ and $\text{Bin}(m,p)$ is $\text{Bin}(n+m,p)$.
- Additional self-practice problems.
  - Checking that a given function is a valid pmf by finding a normalizing constant $c$.
  - Drawing cdfs for simple discrete distributions.
  - Computing probabilities for Poisson counts (e.g., cars at an intersection).
  - Modeling system reliability with binomial distributions (operational components).

### 5.2 How to solve / approach them
- Joint distributions involving indicators and Bernoulli variables.
  - Identify which combinations of values are possible; others automatically have probability 0.
  - Use the definition of indicator: $\eta=I(\xi=2)$ means $\eta=1$ only when $\xi=2$, and $\eta=0$ otherwise.
  - For $\xi,\eta,\zeta$ built from a Bernoulli variable, write out the two possible values of $\xi$ (0 or 1) and compute $\eta$ and $\zeta$ deterministically from them, then assign probabilities.
- Constructing pmfs from two-stage experiments (Masha’s coins).
  - Let the number of tails in the first round be a Binomial r.v. (with parameter $p$ and $n$ trials).
  - The second round involves tossing only those coins that were tails; the number of second-round tails is then Binomial with random number of trials.
  - Use the law of total probability over possible first-round counts and sum appropriately.
- Working with infinite discrete distributions.
  - For $\xi,\eta$ with pmf $p(x)=2^{-x}$:
    - To find $P(\min\{\xi,\eta\}\le x)$, think of the complement $P(\min\{\xi,\eta\}>x) = P(\xi>x,\eta>x)$ and use independence.
    - For $P(\eta>\xi)$, use symmetry or explicit summation over pairs $(k,\ell)$ with $\ell>k$.
    - For $P(\xi\text{ divides }\eta)$, sum over all integer pairs where $\eta$ is a multiple of $\xi$.
- Poisson and binomial sums and conditionals.
  - For the Poisson sum $\xi+\eta$: use the joint pmf of independent Poisson variables and sum over all ways to split total count $n$ into $k$ and $n-k$.
  - Show that the resulting pmf matches a Poisson$(\mu+\nu)$ form.
  - For the conditional distribution $P(\xi=k|\xi+\eta=n)$, apply the definition of conditional probability with the joint pmf and simplify to recognize a binomial pmf in $k$.
  - For the binomial sum, work with pmfs or use the interpretation as total successes in $n+m$ independent trials.
- Valid pmfs and cdfs.
  - When a function $f(x)$ is proposed as a pmf on a finite set of $x$-values, ensure $f(x)\ge 0$ and solve for the constant $c$ in $\sum f(x)=1$.
  - To draw the cdf from a table of values: order the support, then cumulatively add probabilities and plot the resulting step function.

### 5.3 Mini practice
- Practice 1: identifying a Bernoulli variable from an indicator.
  - Question: Let $E$ be the event “the number of heads in two tosses is 2”, and let $\eta = I(E)$. What is the distribution of $\eta$?
  - Brief answer: $\eta$ takes value 1 with probability $P(E)=1/4$ and 0 with probability $3/4$, so $\eta\sim\text{Bernoulli}(p)$ with $p=1/4$.
- Practice 2: recognizing a binomial distribution.
  - Question: A system has 5 independent components, each working with probability 0.92. Let $X$ be the number of working components. What is the distribution and pmf of $X$?
  - Brief answer: $X\sim\text{Bin}(5,0.92)$ with
    $$
    P(X=x) = \binom{5}{x} 0.92^x (0.08)^{5-x},\quad x=0,1,2,3,4,5.
    $$
- Practice 3: sum of independent Poisson variables.
  - Question: $\xi\sim\text{Poi}(2)$ and $\eta\sim\text{Poi}(3)$ are independent. What is the distribution of $\xi+\eta$?
  - Brief answer: By the lab result, $\xi+\eta\sim\text{Poi}(5)$.

## 6. Quick recap
- Random variables are measurable functions from the sample space to the real numbers; indicator variables connect events and random variables.
- Every random variable has a distribution function (cdf) $F_X(x)=P(X\le x)$ that is non-decreasing, right-continuous, and goes from 0 to 1.
- Discrete random variables “live” on a countable set; their pmf $p_X(x)=P(X=x)$ sums to 1 and determines the cdf via jumps.
- Independence is extended from events to random variables; for discrete variables, independence means the joint pmf factors as the product of the marginals.
- Standard discrete distributions introduced: Bernoulli, Binomial, discrete uniform, Geometric, and Poisson, each modeling a different type of counting process.
- Random vectors group several random variables; their behavior is described using joint, marginal, and conditional pmfs.
- The lab reinforces these ideas through problems on joint distributions, indicator variables, derived pmfs, sums of Poisson and binomial variables, and constructing valid discrete distributions.


[<kbd><br><- Return (ProbStat)<br></kbd>](ProbStat.md)
