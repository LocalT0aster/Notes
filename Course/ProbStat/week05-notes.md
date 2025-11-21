# CSE206 — Week 05 Notes — Continuous r.v.s (multinomial/binomial review, pdf/cdf link, uniform, normal)
**Lectures:** CSE206_Fa24-05.pdf  
**Lab/Tutorial:** week05.pdf  

## 1. Big picture (5–10 bullets)
- This week reviews the binomial distribution and generalizes it to the multinomial distribution for multiple categories.  
- The multinomial distribution models counts of outcomes in several categories across repeated independent trials.  
- Continuous random variables are introduced formally, along with the idea of a probability density function (pdf).  
- For continuous random variables, probabilities are computed by integrating the pdf over sets (intervals, etc.).  
- The relationship between pdf and cumulative distribution function (cdf) is clarified using integration and differentiation.  
- Two key continuous distributions are presented: the continuous uniform distribution and the normal (Gaussian) distribution.  
- The lab focuses on deriving cdfs and pdfs of uniform distributions and functions of them (min, max), and on standardizing the normal distribution and squaring it.  

## 2. Key concepts and definitions

### 2.1 Binomial distribution (review)
- Plain-language definition.  
  - A binomial random variable counts the number of successes in a fixed number \(n\) of independent trials, where each trial has the same success probability \(p\).  
- Formal definition (if needed).  
  - A random variable \(\xi\) has binomial distribution with parameters \(n\) and \(p\), written \(\xi\sim \text{Binomial}(n,p)\), if its pmf is  
    \[
    p_\xi(x) = \binom{n}{x}p^x(1-p)^{n-x} I(x\in\{0,1,\dots,n\}).
    \]  
  - Expected value and variance (from previous lecture, recalled here):  
    \[
    E\xi = np,\quad \text{Var}(\xi) = np(1-p).
    \]  
  - A binomial random variable has the same distribution as the sum of \(n\) independent Bernoulli\((p)\) random variables.  
- Intuition / mental model.  
  - Think of \(n\) identical, independent “yes/no” experiments (coin tosses, passes/fails, hits/misses). The binomial counts how many “yes” outcomes occur.  
- Tiny example.  
  - Toss a coin \(n=10\) times, with success probability \(p\). Let \(\xi\) be the number of heads. Then \(\xi\sim\text{Binomial}(10,p)\), and  
    \[
    P(\xi=3) = \binom{10}{3}p^3(1-p)^7.
    \]  

### 2.2 Multinomial distribution
- Plain-language definition.  
  - The multinomial distribution generalizes the binomial to more than two categories. It gives the joint distribution of counts of each category in repeated independent trials.  
- Formal definition (if needed).  
  - Suppose we have independent random variables \(\xi_1,\dots,\xi_n\), each taking values in \(\{1,\dots,m\}\) with  
    \[
    P(\xi_k=j) = p_j,\quad j=1,\dots,m,\quad \sum_{j=1}^m p_j = 1.
    \]  
  - Define counts  
    \[
    \eta_j = \sum_{k=1}^n I(\xi_k = j),\quad j=1,\dots,m,
    \]  
    and the random vector  
    \[
    \eta = (\eta_1,\dots,\eta_m).
    \]  
  - The counts satisfy the constraint  
    \[
    \eta_1 + \dots + \eta_m = n.
    \]  
  - The joint pmf of \(\eta\) is  
    \[
    p_\eta(x_1,\dots,x_m)
      = P(\eta_1=x_1,\dots,\eta_m=x_m)
      = \binom{n}{x_1,\dots,x_m} p_1^{x_1}\dots p_m^{x_m}
    \]  
    for nonnegative integers \(x_1,\dots,x_m\) with \(x_1+\dots+x_m = n\), where the multinomial coefficient is  
    \[
    \binom{n}{x_1,\dots,x_m} = \frac{n!}{x_1!\dots x_m!}.
    \]  
- Intuition / mental model.  
  - Each trial picks one category among \(m\) possibilities (like faces of a die, or different scores).  
  - The multinomial distribution tells you the probability of seeing a specific “profile” \((x_1,\dots,x_m)\) of how many times each category occurred.  
- Tiny example (from lecture’s interpretation).  
  - \(n\) players play a game and get scores 1 to \(m\). Each score \(j\) occurs with probability \(p_j\), independently across players.  
  - The random vector \(\eta\) counts how many players got each score. The multinomial pmf gives \(P(\eta_1=x_1,\dots,\eta_m=x_m)\).  
  - When \(m=2\), this reduces to the binomial distribution for one of the counts.  

### 2.3 Continuous random variables and pdf
- Plain-language definition.  
  - A continuous random variable uses a density function instead of a pmf; probabilities of intervals are given by integrals of the density.  
  - For a continuous random variable, \(P(\xi=x)=0\) for every single point \(x\); only intervals (or more general sets) can have positive probability.  
- Formal definition (if needed).  
  - A random variable \(\xi\) is continuous if there exists a function \(p_\xi:\mathbb{R}\to\mathbb{R}\) such that:  
    1. \(p_\xi(x)\ge 0\) for all \(x\).  
    2. \(\displaystyle\int_{-\infty}^\infty p_\xi(x)\,dx = 1.\)  
    3. For any Borel set \(B\subset\mathbb{R}\),  
       \[
       P(\xi\in B) = \int_B p_\xi(x)\,dx.
       \]  
  - The function \(p_\xi\) is called the probability density function (pdf) or simply density of \(\xi\).  
- Intuition / mental model.  
  - Imagine probability “spread out” smoothly over the real line rather than concentrated at countable points.  
  - The height of the density curve at \(x\) reflects how likely values near \(x\) are, but densities themselves can exceed 1 (only areas must be \(\le1\)).  
- Tiny example.  
  - A continuous uniform random variable on \((0,1)\) has density \(p_\xi(x)=1\) for \(0<x<1\), and 0 otherwise. For any interval \((a,b)\subset(0,1)\),  
    \[
    P(a<\xi<b) = \int_a^b 1\,dx = b-a.
    \]  

### 2.4 Relationship between pdf and cdf (continuous case)
- Plain-language definition.  
  - The cdf of a continuous random variable is the integral of its density; when the density is nice enough, it is the derivative of the cdf.  
- Formal relationship (if needed).  
  - For a continuous random variable \(\xi\) with pdf \(p_\xi\), the cdf is  
    \[
    F_\xi(x) = P(\xi\le x) = \int_{-\infty}^x p_\xi(t)\,dt.
    \]  
  - If \(p_\xi\) is continuous at \(x\), then by the fundamental theorem of calculus, \(F_\xi\) is differentiable at \(x\), and  
    \[
    F_\xi'(x) = p_\xi(x).
    \]  
  - Conversely, if a cdf \(F_\xi\) is continuously differentiable everywhere, then \(F_\xi'(x)\) is a density for \(\xi\).  
  - If \(F_\xi\) is continuous and piecewise continuously differentiable (with finitely or countably many non-differentiable isolated points \(x_1,x_2,\dots\)), we can take  
    \[
    p_\xi(x)=F_\xi'(x)I(x\notin\{x_1,x_2,\dots\}).
    \]  
- Intuition / mental model.  
  - The cdf accumulates area under the density curve; the density is the local “slope” of the cdf where it is differentiable.  
  - Changing the density at countably many points does not change the cdf or any probabilities.  
- Tiny example.  
  - For \(\xi\sim\text{Uniform}(a,b)\) with density \(p_\xi(x)=\frac{1}{b-a}I(a<x<b)\), the cdf is  
    \[
    F_\xi(x) =
    \begin{cases}
    0, & x\le a,\\[2pt]
    \dfrac{x-a}{b-a}, & a<x<b,\\[6pt]
    1, & x\ge b,
    \end{cases}
    \]  
    and differentiating on \((a,b)\) recovers the density \(1/(b-a)\).  

### 2.5 Continuous uniform distribution on \((a,b)\)
- Plain-language definition.  
  - A continuous uniform random variable on \((a,b)\) is a random number equally likely to fall anywhere between \(a\) and \(b\).  
- Formal definition (if needed).  
  - A random variable \(\xi\) has continuous uniform distribution on \((a,b)\), written \(\xi\sim\text{Uni}(a,b)\), if its pdf is  
    \[
    p_\xi(x) = \frac{1}{b-a}I(a<x<b).
    \]  
- Cdf, mean, and variance (from lecture).  
  - Cdf:  
    \[
    F_\xi(x) =
    \begin{cases}
    0, & x\le a,\\
    \dfrac{x-a}{b-a}, & a<x<b,\\
    1, & x\ge b.
    \end{cases}
    \]  
  - Mean (expectation):  
    \[
    E\xi = \frac{a+b}{2}.
    \]  
  - Second moment and variance (assuming \(a\ge 0\) in the lecture derivation):  
    \[
    E\xi^2 = \frac{a^2+ab+b^2}{3},\quad \text{Var}(\xi) = E\xi^2 - (E\xi)^2 = \frac{(b-a)^2}{12}.
    \]  
- Intuition / mental model.  
  - The mean is the midpoint of the interval; the variance depends only on the length of the interval, not its absolute position.  
- Tiny example.  
  - If \(\xi\sim\text{Uni}(0,1)\), then \(E\xi=1/2\) and \(\text{Var}(\xi)=1/12\).  

### 2.6 Normal (Gaussian) distribution
- Plain-language definition.  
  - The normal (Gaussian) distribution is a bell-shaped continuous distribution centered at \(\mu\) with spread controlled by \(\sigma>0\).  
- Formal definition (if needed).  
  - A random variable \(\xi\) has normal distribution with parameters \(\mu\in\mathbb{R}\) and \(\sigma^2>0\), written \(\xi\sim N(\mu,\sigma^2)\), if its pdf is  
    \[
    p_\xi(x) = \frac{1}{\sqrt{2\pi}\,\sigma}\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right).
    \]  
  - The cdf of a normal random variable does not have a closed form in terms of elementary functions.  
- Intuition / mental model.  
  - The graph of the density is symmetric around \(x=\mu\), highest at \(\mu\), and decreases rapidly as \(x\) moves away from \(\mu\).  
  - The parameters \(\mu\) and \(\sigma\) represent the “center” and “spread” of the distribution.  
- Empirical “68–95–99.7” rule (from lecture).  
  - About 68% of the probability lies in \([\mu-\sigma,\mu+\sigma]\).  
  - About 95% lies in \([\mu-2\sigma,\mu+2\sigma]\).  
  - About 99.7% lies in \([\mu-3\sigma,\mu+3\sigma]\).  
- Standard normal distribution and transformation.  
  - When \(\mu=0\) and \(\sigma=1\), \(\xi\sim N(0,1)\) is called a standard normal random variable.  
  - The lecture states and the lab asks you to show that if \(\xi\sim N(\mu,\sigma^2)\) and  
    \[
    \eta = \frac{\xi-\mu}{\sigma},
    \]  
    then \(\eta\sim N(0,1)\). This operation is called standardization.  
- Tiny example.  
  - If \(\xi\sim N(3,4)\) (mean 3, variance 4, so \(\sigma=2\)), then  
    \[
    \eta = \frac{\xi-3}{2}
    \]  
    has standard normal distribution \(N(0,1)\).  

## 3. Core formulas and how to use them

### 3.1 Multinomial pmf and multinomial coefficient
- Formula.  
  - If \(\eta=(\eta_1,\dots,\eta_m)\sim \text{Multinom}(n,m;p_1,\dots,p_m)\), then for nonnegative integers \(x_1,\dots,x_m\) with \(x_1+\dots+x_m=n\):  
    \[
    P(\eta_1=x_1,\dots,\eta_m=x_m) = \binom{n}{x_1,\dots,x_m}p_1^{x_1}\dots p_m^{x_m},
    \]  
    where  
    \[
    \binom{n}{x_1,\dots,x_m} = \frac{n!}{x_1!\dots x_m!}.
    \]  
- Symbols.  
  - \(n\): number of trials.  
  - \(m\): number of categories.  
  - \(p_j\): probability of category \(j\) in each trial.  
  - \(\eta_j\): count of category \(j\) over \(n\) trials.  
- When to use it.  
  - When each trial can result in one of several outcomes, and trials are independent with fixed outcome probabilities.  
  - To compute probabilities of given count profiles (e.g., “exactly 3 players score 1, 5 score 2, and 2 score 3”).  
- Common mistakes.  
  - Forgetting the constraint \(x_1+\dots+x_m=n\) (those cases automatically have probability 0).  
  - Confusing multinomial coefficients with binomial coefficients (they generalize them, but are used when there are more than two categories).  

### 3.2 Definition of continuous r.v., pdf, and probability of intervals
- Pdf-based probability formula.  
  - For a continuous random variable \(\xi\) with pdf \(p_\xi\):  
    \[
    P(a\le\xi\le b) = \int_a^b p_\xi(x)\,dx
    \]  
    for any real numbers \(a\le b\).  
- Symbols.  
  - \(p_\xi(x)\): probability density function.  
  - \(F_\xi(x)\): cdf, given by \(\int_{-\infty}^x p_\xi(t)\,dt\).  
- When to use it.  
  - When computing probabilities for continuous distributions (uniform, normal, etc.).  
  - When changing variables (e.g., computing the density of \(\xi^2\) or \(\max\{\xi_1,\dots,\xi_n\}\)).  
- Common mistakes.  
  - Treating the value \(p_\xi(x_0)\) as a probability; it is not a probability, only an intensity of likelihood.  
  - Forgetting that \(P(\xi=x_0)=0\) for continuous random variables.  

### 3.3 Uniform \((a,b)\): pdf, cdf, mean, variance
- Pdf and cdf.  
  - Pdf: \(p_\xi(x)=\frac{1}{b-a}I(a<x<b)\).  
  - Cdf:  
    \[
    F_\xi(x)=
    \begin{cases}
    0, & x\le a,\\
    \dfrac{x-a}{b-a}, & a<x<b,\\
    1, & x\ge b.
    \end{cases}
    \]  
- Mean and variance (from lecture derivation via integrals):  
  - \(E\xi = \dfrac{a+b}{2}\).  
  - \(\text{Var}(\xi) = \dfrac{(b-a)^2}{12}\).  
- When to use it.  
  - When modeling a quantity that is equally likely to be anywhere in a finite interval, with no preference for subintervals.  
- Common mistakes.  
  - Forgetting that the density is constant only between \(a\) and \(b\), and 0 outside.  
  - Using uniform on \((a,b)\) when the problem clearly has more structure (e.g., peaks, tails) that uniform cannot capture.  

### 3.4 Normal \((\mu,\sigma^2)\): pdf and standardization
- Pdf.  
  - \[
    p_\xi(x) = \frac{1}{\sqrt{2\pi}\,\sigma}\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right).
    \]  
- Standardization formula.  
  - If \(\xi\sim N(\mu,\sigma^2)\) and  
    \[
    \eta = \frac{\xi-\mu}{\sigma},
    \]  
    then \(\eta\sim N(0,1)\).  
- When to use it.  
  - To convert any normal variable to a standard normal variable so you can use standard tables or numerical functions to find probabilities.  
  - To relate probabilities like \(P(\xi\le t)\) to standard normal probabilities \(P(Z\le z)\).  
- Common mistakes.  
  - Forgetting to subtract \(\mu\) before dividing by \(\sigma\).  
  - Using \(\sigma^2\) instead of \(\sigma\) in the denominator.  

## 4. Worked examples

### 4.1 Multinomial interpretation with players’ scores
- Setup (from lecture interpretation).  
  - There are \(n\) video-game players, each playing independently.  
  - Each player’s score is an integer in \(\{1,2,\dots,m\}\).  
  - The probability of score \(j\) is \(p_j\) (same for each player), with \(p_1+\dots+p_m=1\).  
  - Define counts \(\eta_j\) = number of players who get score \(j\); the vector \(\eta=(\eta_1,\dots,\eta_m)\) has multinomial distribution.  
- Step 1: express the counts as sums of indicators.  
  - Let \(\xi_k\) be the score of player \(k\).  
  - For each score \(j\),  
    \[
    \eta_j = \sum_{k=1}^n I(\xi_k = j),
    \]  
    so \(\eta_j\) counts how many players got score \(j\).  
  - These counts satisfy \(\eta_1+\dots+\eta_m = n\).  
- Step 2: compute the probability of a specific profile.  
  - Fix nonnegative integers \(x_1,\dots,x_m\) with \(x_1+\dots+x_m=n\).  
  - The event \(\{\eta_1=x_1,\dots,\eta_m=x_m\}\) means exactly \(x_1\) players got score 1, \(x_2\) players got score 2, etc.  
  - For any specific assignment of scores to players consistent with this profile, the probability (by independence) is  
    \[
    p_1^{x_1}\dots p_m^{x_m}.
    \]  
  - The number of such assignments is the multinomial coefficient  
    \[
    \binom{n}{x_1,\dots,x_m} = \frac{n!}{x_1!\dots x_m!}.
    \]  
- Step 3: write the multinomial pmf.  
  - Multiplying the number of assignments by the probability of each gives  
    \[
    P(\eta_1=x_1,\dots,\eta_m=x_m)
      = \binom{n}{x_1,\dots,x_m}p_1^{x_1}\dots p_m^{x_m},
    \]  
    matching the formula in Section 3.1.  
- Check your intuition.  
  - This generalizes the binomial: with \(m=2\), counts \(\eta_1,\eta_2\) correspond to failure and success counts, and the pmf reduces to a binomial distribution in one component.  

### 4.2 Continuous uniform \((a,b)\): cdf, mean, variance
- Setup (from lecture and lab).  
  - Let \(\xi\sim \text{Uni}(a,b)\), with density \(p_\xi(x)=\frac{1}{b-a}I(a<x<b)\).  
- Step 1: compute the cdf.  
  - For \(x\le a\):  
    \[
    F_\xi(x) = P(\xi\le x) = 0,
    \]  
    because \(\xi\) can only take values greater than \(a\).  
  - For \(a<x<b\):  
    \[
    F_\xi(x) = P(\xi\le x) = P(a<\xi\le x) = \int_a^x \frac{1}{b-a}\,dt = \frac{x-a}{b-a}.
    \]  
  - For \(x\ge b\):  
    \[
    F_\xi(x) = 1,
    \]  
    since all probability mass lies in \((a,b)\).  
- Step 2: compute the mean \(E\xi\) (lecture uses an integral involving \(1-F_\xi\); we can also integrate \(x p_\xi(x)\)).  
  - Using the standard expectation formula for continuous \(\xi\):  
    \[
    E\xi = \int_{-\infty}^{\infty} x p_\xi(x)\,dx = \int_a^b x\cdot\frac{1}{b-a}\,dx
         = \frac{1}{b-a}\left[\frac{x^2}{2}\right]_a^b
         = \frac{b^2-a^2}{2(b-a)} = \frac{a+b}{2}.
    \]  
- Step 3: compute \(E\xi^2\) and \(\text{Var}(\xi)\).  
  - Similarly,  
    \[
    E\xi^2 = \int_a^b x^2\cdot\frac{1}{b-a}\,dx
           = \frac{1}{b-a}\left[\frac{x^3}{3}\right]_a^b
           = \frac{b^3-a^3}{3(b-a)} = \frac{a^2+ab+b^2}{3}
    \]  
    (using the algebraic identity for \(b^3-a^3\)).  
  - Then  
    \[
    \text{Var}(\xi) = E\xi^2 - (E\xi)^2
                    = \frac{a^2+ab+b^2}{3} - \left(\frac{a+b}{2}\right)^2
                    = \frac{(b-a)^2}{12}.
    \]  
- Check your intuition.  
  - The midpoint \((a+b)/2\) is the “center” of the interval, which fits the idea of equal likelihood across \((a,b)\).  
  - The variance grows with the square of the interval length \(b-a\), meaning wider intervals give more spread.  

## 5. Lab/Tutorial essentials (week05.pdf)

### 5.1 What the lab asked you to do
- Problem 1: continuous uniform cdf and differentiability.  
  - Find and plot the cdf of a continuous uniform random variable with parameters \(a\) and \(b\).  
  - Identify where the cdf is differentiable and where it is not.  
- Problem 2: max and min of independent uniform variables.  
  - Let \(\xi_1,\dots,\xi_n\) be independent \(\text{Uni}(a,b)\) random variables.  
  - Find and plot the cdf of \(M = \max\{\xi_1,\dots,\xi_n\}\) and \(m = \min\{\xi_1,\dots,\xi_n\}\).  
  - Find and plot a pdf for each of these random variables.  
- Problem 3: standardization of a normal variable.  
  - Let \(\xi\sim N(\mu,\sigma^2)\). Prove that  
    \[
    \eta = \frac{\xi-\mu}{\sigma}
    \]  
    has distribution \(N(0,1)\).  
- Problem 4: distribution of the square of a standard normal variable.  
  - Let \(\xi\) be standard normal. Find the pdf of \(\xi^2\).  

### 5.2 How to solve / approach them
- Problem 1: uniform cdf and differentiability.  
  - Use the definition of cdf as \(F_\xi(x)=P(\xi\le x)\) together with the uniform density on \((a,b)\) to derive the piecewise formula.  
  - Differentiability:  
    - On \((a,b)\), \(F_\xi(x)\) is linear, so differentiable with derivative \(1/(b-a)\).  
    - At \(x=a\) and \(x=b\), there are “corners” (changes in formula), so \(F_\xi\) is not differentiable there.  
    - Outside \([a,b]\) the function is constant (0 or 1), so differentiable.  
- Problem 2: cdf and pdf of max and min of independent uniforms.  
  - For \(M=\max\{\xi_1,\dots,\xi_n\}\):  
    - Use the identity  
      \[
      P(M\le x) = P(\xi_1\le x,\dots,\xi_n\le x)
      \]  
      and independence to get  
      \[
      F_M(x)=
      \begin{cases}
      0, & x\le a,\\
      \left(\dfrac{x-a}{b-a}\right)^n, & a<x<b,\\
      1, & x\ge b.
      \end{cases}
      \]  
    - Differentiate on \((a,b)\) to get the pdf of \(M\).  
  - For \(m=\min\{\xi_1,\dots,\xi_n\}\):  
    - Use the complement:  
      \[
      P(m > x) = P(\xi_1>x,\dots,\xi_n>x)
      \]  
      and independence, then  
      \[
      F_m(x) = 1 - P(m>x).
      \]  
    - Again, differentiate on \((a,b)\) to obtain the pdf.  
- Problem 3: standardizing a normal variable.  
  - Start from the pdf of \(\xi\sim N(\mu,\sigma^2)\).  
  - Perform a change of variable \(z=(x-\mu)/\sigma\) and show that the pdf of \(\eta\) matches the standard normal pdf \(\frac{1}{\sqrt{2\pi}}e^{-z^2/2}\).  
  - Conclude that \(\eta\sim N(0,1)\).  
- Problem 4: pdf of \(\xi^2\) when \(\xi\sim N(0,1)\).  
  - Let \(Y=\xi^2\). Use transformation techniques for continuous random variables.  
  - For \(y>0\), there are two preimages \(x=\sqrt{y}\) and \(x=-\sqrt{y}\).  
  - Apply the formula for transformed densities with multiple roots and use the standard normal pdf to deduce the density of \(Y\).  

### 5.3 Mini practice
- Practice 1: identifying uniform cdf behavior.  
  - Question: For \(\xi\sim \text{Uni}(a,b)\), at which points is \(F_\xi(x)\) not differentiable?  
  - Brief answer: At the endpoints \(x=a\) and \(x=b\); elsewhere the function is either constant (differentiable with derivative 0) or linear (differentiable with derivative \(1/(b-a)\)).  
- Practice 2: distribution of the maximum.  
  - Question: If \(\xi_1,\dots,\xi_n\) are i.i.d. \(\text{Uni}(0,1)\) and \(M=\max\{\xi_1,\dots,\xi_n\}\), what is \(P(M\le t)\) for \(0<t<1\)?  
  - Brief answer: \(P(M\le t) = P(\xi_1\le t,\dots,\xi_n\le t) = t^n\).  
- Practice 3: standardization of a normal.  
  - Question: \(\xi\sim N(5,9)\). What is the distribution of \((\xi-5)/3\)?  
  - Brief answer: \((\xi-5)/3\sim N(0,1)\).  

## 6. Quick recap
- The multinomial distribution generalizes the binomial to multiple categories, giving the joint distribution of category counts across independent trials.  
- Continuous random variables are defined via probability density functions; probabilities of sets are integrals of the density.  
- The pdf and cdf of a continuous random variable are linked: the cdf is the integral of the pdf, and the pdf is the derivative of the cdf where it exists.  
- The continuous uniform distribution on \((a,b)\) has constant density \(1/(b-a)\), mean \((a+b)/2\), and variance \((b-a)^2/12\).  
- The normal distribution \(N(\mu,\sigma^2)\) has bell-shaped density, with most probability mass within a few standard deviations of the mean, and can be standardized to \(N(0,1)\).  
- The week 5 lab emphasizes working with uniform cdfs and pdfs (including max and min), and with transformations of normal random variables (standardization and squaring).  


[<kbd><br><- Return (ProbStat)<br></kbd>](ProbStat.md)
