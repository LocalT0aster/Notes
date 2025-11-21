# CSE206 — Week 10 Notes — Gamma sampling, couplings, building Uni/Normal, optimal transport intro
**Lectures:** CSE206_Fa24-10.pdf  
**Lab/Tutorial:** week10.pdf  

## 1. Big picture (5–10 bullets)
- This week finishes the discussion of sampling methods (with Gamma distribution as a key example) and introduces the Gamma distribution in detail.  
- The Gamma distribution generalizes exponential and chi-squared distributions, with parameters controlling scale and “shape” (waiting time to the \(t\)-th event).  
- Rejection sampling is applied concretely to generate Gamma random variables when inversion is not simple.  
- The notion of coupling is formalized: constructing random variables with given marginals on a common probability space, including independent couplings.  
- Product σ-algebras and product probability measures are used to build joint spaces where given marginals live together.  
- Couplings are used to construct arbitrary multivariate normal vectors and to connect probabilistic models to optimal transportation problems.  
- The week 10 recap lab reuses and reinforces multivariate normals, change-of-variables, convolutions, sampling (inversion and rejection), and Markov/Chebyshev bounds.  

## 2. Key concepts and definitions

### 2.1 Gamma distribution
- Plain-language definition.  
  - The Gamma distribution models the waiting time until the \(t\)-th event in a Poisson process with rate \(\lambda\), or more generally, has a flexible positive-valued shape controlled by parameters \(\lambda\) (rate) and \(t\) (shape).  
- Formal definition (if needed).  
  - A random variable \(\xi\) has Gamma distribution with parameters \(\lambda>0\) and \(t>0\), written \(\xi\sim\text{Gamma}(\lambda,t)\), if its pdf is  
    \[
    p_\xi(x) = \frac{1}{\Gamma(t)}\lambda^t x^{t-1} e^{-\lambda x} I(x>0),
    \]  
    where \(\Gamma(t)\) is the Gamma function  
    \[
    \Gamma(t) = \int_0^\infty x^{t-1}e^{-x}\,dx.
    \]  
- Important special cases (from lecture).  
  - If \(t=1\), then \(\xi\sim\text{Exp}(\lambda)\).  
  - If \(\lambda=1/2\) and \(t=n/2\) for integer \(n\), then \(\xi\sim\chi^2(n)\) (chi-squared distribution).  
- Mean and variance.  
  - For \(\xi\sim\text{Gamma}(\lambda,t)\):  
    \[
    E\xi = \frac{t}{\lambda},\quad \text{Var}(\xi) = \frac{t}{\lambda^2}.
    \]  
- Scaling property.  
  - If \(\xi\sim\text{Gamma}(1,t)\), then \(\xi/\lambda\sim\text{Gamma}(\lambda,t)\). This is used in the sampling algorithm.  
- Intuition / mental model.  
  - Think of a Poisson process: if the number of events in time \(s\) is Poisson\((\lambda s)\), then the waiting time to the \(t\)-th event is Gamma\((\lambda,t)\).  

### 2.2 Sampling exponential and Gamma distributions
- Exponential via inversion (revisited).  
  - For \(\xi\sim\text{Exp}(\lambda)\), the cdf is \(F(x)=1-e^{-\lambda x}\) for \(x\ge0\).  
  - Let \(\zeta\sim\text{Uni}(0,1)\). Setting \(\zeta = 1-e^{-\lambda x}\) and solving for \(x\) gives  
    \[
    x = -\frac{1}{\lambda}\log(1-\zeta),
    \]  
    equivalent to \(x=-\frac{1}{\lambda}\log\zeta\) since \(1-\zeta\) is also uniform.  
  - Thus, \(x=-\frac{1}{\lambda}\log\zeta\) has exponential distribution with parameter \(\lambda\).  
- Gamma via rejection (Example 1.1).  
  - Goal: sample from \(\text{Gamma}(\lambda,t)\) for \(t>1\).  
  - Case \(\lambda=1\):  
    - Proposal distribution: exponential with parameter \(1/t\), pdf \(p_\eta(x)=\frac{1}{t}e^{-x/t}I(x>0)\).  
    - Target pdf: \(p_\xi(x)=\frac{1}{\Gamma(t)}x^{t-1}e^{-x}I(x>0)\).  
    - Choose  
      \[
      b = e^{1-t}t^t / \Gamma(t),
      \]  
      and verify that for all \(x>0\):  
      \[
      bp_\eta(x) = b\frac{1}{t}e^{-x/t} \ge p_\xi(x).
      \]  
    - Define acceptance event  
      \[
      E = \{b\zeta p_\eta(\eta)\le p_\xi(\eta)\},
      \]  
      where \(\zeta\sim\text{Uni}(0,1)\) and \(\eta\sim\text{Exp}(1/t)\) are independent.  
    - Conditionally on \(E\), \(\eta\) has the desired Gamma\((1,t)\) distribution.  
  - General \(\lambda>0\):  
    - First sample \(\tilde{\xi}\sim\text{Gamma}(1,t)\) using the algorithm above.  
    - Then set \(\xi = \tilde{\xi}/\lambda\), which yields \(\xi\sim\text{Gamma}(\lambda,t)\).  
- Intuition / mental model.  
  - Inversion is easy for exponential because its cdf is explicitly invertible.  
  - For general Gamma with \(t>1\), the cdf has no simple inverse, so rejection sampling with a suitably chosen exponential envelope is used.  

### 2.3 Couplings: product spaces and independent coupling
- Plain-language idea.  
  - A coupling places two (or more) given random variables on a common probability space in such a way that each keeps its original distribution; an independent coupling does this while also making them independent.  
- Product measurable space.  
  - Given measurable spaces \((\Omega_1,\mathcal{F}_1)\) and \((\Omega_2,\mathcal{F}_2)\), their product space is \(\Omega_1\times\Omega_2\).  
  - The product σ-algebra \(\mathcal{F}_1\otimes\mathcal{F}_2\) is the smallest σ-algebra containing all rectangles \(E_1\times E_2\) with \(E_1\in\mathcal{F}_1\), \(E_2\in\mathcal{F}_2\).  
- Product probability measure.  
  - If \((\Omega_1,\mathcal{F}_1,P_1)\) and \((\Omega_2,\mathcal{F}_2,P_2)\) are probability spaces, their product measure \(P_1\times P_2\) is defined on \(\mathcal{F}_1\otimes\mathcal{F}_2\) by  
    \[
    (P_1\times P_2)(E_1\times E_2) = P_1(E_1)P_2(E_2),
    \]  
    and extended to the whole σ-algebra.  
- Independent coupling construction (section 2.2.3).  
  - Suppose \(\xi_1:\Omega_1\to\mathbb{R}\), \(\xi_2:\Omega_2\to\mathbb{R}\) are random variables on different spaces.  
  - On \(\Omega_1\times\Omega_2\) with measure \(P_1\times P_2\), define  
    \[
    \xi_1'(\omega_1,\omega_2)=\xi_1(\omega_1),\quad \xi_2'(\omega_1,\omega_2)=\xi_2(\omega_2).
    \]  
  - Then:  
    1. \(\xi_1'\) has the same distribution as \(\xi_1\).  
    2. \(\xi_2'\) has the same distribution as \(\xi_2\).  
    3. \(\xi_1',\xi_2'\) are independent by construction.  
- General coupling definition.  
  - A coupling of two random variables \(\xi_1,\xi_2\) is any pair \((\xi_1',\xi_2')\) defined on the same probability space such that \(\xi_1'\) has the same distribution as \(\xi_1\) and \(\xi_2'\) as \(\xi_2\). There is no requirement that they be independent.  
- Intuition / mental model.  
  - Independent couplings allow us to talk about independence even when the original variables lived on different spaces.  
  - More general couplings encode different joint behaviors for the same marginals (used later in optimal transport).  

### 2.4 Constructing basic continuous random variables from Uni(0,1)
- Uniform random variable (Example 2.1).  
  - Choose \(\Omega=(0,1)\), \(\mathcal{F}\) the Borel σ-algebra on \((0,1)\), and let \(P\) be Lebesgue measure restricted to \((0,1)\) (extended from intervals).  
  - Define \(\xi(\omega) = \omega\). Then \(\xi\) has the \(\text{Uni}(0,1)\) distribution.  
  - Alternative: take \(\Omega=(-1,1)\) with scaled Lebesgue measure and \(\xi(\omega)=\frac{1}{2}(1+\omega)\), again obtaining \(\text{Uni}(0,1)\).  
- Standard normal \(N(0,1)\) (Example 2.2).  
  - Use the same \((\Omega,\mathcal{F},P)\) as above. Let \(F(x)\) be the standard normal cdf  
    \[
    F(x) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^x e^{-t^2/2}\,dt,
    \]  
    which is continuous, strictly increasing, and maps \(\mathbb{R}\) to \((0,1)\).  
  - Define \(\eta(\omega)=F^{-1}(\omega)\). Then \(\eta\) has distribution \(N(0,1)\) by the inversion method.  
- General multivariate normal \(N^d(\mu,K)\) (Example 2.4).  
  - Step 1: build an independent coupling of \(d\) standard normals using \((0,1)^d\) and the inversion method coordinate-wise; call the resulting vector \(\xi'\sim N^d(0,I_d)\).  
  - Step 2: choose a linear transformation \(T:\mathbb{R}^d\to\mathbb{R}^d\) such that \(TT^\top = K\) (e.g., via Cholesky).  
  - Step 3: define \(\eta = \mu + T\xi'\), which then has distribution \(N^d(\mu,K)\).  
- Intuition / mental model.  
  - Any continuous distribution can, in principle, be constructed on a probability space starting from a uniform variable plus appropriate transformations.  

### 2.5 Optimal transportation (high-level)
- Plain-language idea.  
  - Given an initial mass distribution (random variable \(\xi\)) and a target distribution (\(\eta\)), we want to move mass from \(\xi\) to \(\eta\) at minimal cost, where cost depends on how far each “particle” is moved.  
- Transport maps and couplings.  
  - A transport map \(T:\mathbb{R}^d\to\mathbb{R}^d\) moves mass by sending \(x\mapsto T(x)\). The cost is  
    \[
    E[c(\xi,T(\xi))] = \int c(x,T(x))p_\xi(x)\,dx,
    \]  
    under the constraint that \(T(\xi)\) and \(\eta\) have the same distribution.  
  - Monge’s formulation seeks  
    \[
    d_M(\xi,\eta) = \inf\{E[c(\xi,T(\xi))] : T\text{ pushes }\xi\text{ to }\eta\}.
    \]  
  - Kantorovich’s relaxation instead looks at all couplings \((\xi',\eta')\) of \(\xi,\eta\) and considers  
    \[
    \inf\{E[c(\xi',\eta')]\},
    \]  
    where the infimum is taken over all couplings. Transport maps correspond to special couplings.  
- Intuition / mental model.  
  - Transport maps move each point deterministically; couplings consider all possible joint distributions with given marginals, allowing randomized transportation plans and leading to a more tractable optimization problem.  

## 3. Core formulas and how to use them

### 3.1 Gamma pdf, mean, and variance
- Pdf.  
  - \[
    p_\xi(x) = \frac{1}{\Gamma(t)}\lambda^t x^{t-1}e^{-\lambda x}I(x>0).
    \]  
- Mean and variance.  
  - \[
    E\xi = \frac{t}{\lambda},\quad \text{Var}(\xi)=\frac{t}{\lambda^2}.
    \]  
- Scaling property.  
  - If \(\xi\sim\text{Gamma}(1,t)\), then \(\xi/\lambda\sim\text{Gamma}(\lambda,t)\).  
- When to use it.  
  - To model sums of independent exponentials, waiting time to the \(t\)-th event in a Poisson process, and chi-squared distributions.  

### 3.2 Rejection sampling condition
- Condition for valid envelope.  
  - Given target density \(p_\xi(x)\) and proposal density \(p_\eta(x)\), choose \(b>1\) such that  
    \[
    p_\xi(x)\le b p_\eta(x)\quad \text{for all }x.
    \]  
  - Define acceptance event \(E=\{b\zeta p_\eta(\eta)\le p_\xi(\eta)\}\) with \(\zeta\sim\text{Uni}(0,1)\).  
- Key properties.  
  - Conditionally on \(E\), \(\eta\) has pdf \(p_\xi\).  
  - The acceptance probability is \(P(E)=1/b\), so the expected number of iterations until acceptance is \(b\).  
- When to use it.  
  - When inversion is difficult and it is easy to sample from a proposal density that pointwise dominates the target up to a constant factor.  

### 3.3 Linear combinations and covariance (recap from lab)
- For a random vector \(\xi=(\xi_1,\xi_2,\xi_3)^T\) with mean vector \(\mu\) and covariance matrix \(K\), and linear form \(\eta = a^T\xi\) (where \(a\in\mathbb{R}^3\)):  
  - Mean:  
    \[
    E\eta = a^T\mu.
    \]  
  - Variance:  
    \[
    \text{Var}(\eta) = a^T K a.
    \]  
- When to use it.  
  - In lab tasks involving multivariate normals (week10 recap): to compute means and variances of linear combinations and to optimize variance with respect to parameters.  

## 4. Worked examples

### 4.1 Sampling Gamma(λ,t) via rejection (outline)
- Setup.  
  - Target distribution: \(\xi\sim\text{Gamma}(1,t)\) with pdf  
    \[
    p_\xi(x) = \frac{1}{\Gamma(t)}x^{t-1}e^{-x}I(x>0).
    \]  
  - Proposal: \(\eta\sim\text{Exp}(1/t)\) with pdf \(p_\eta(x)=\frac{1}{t}e^{-x/t}I(x>0)\).  
  - Choose \(b = e^{1-t}t^t/\Gamma(t)\) so that \(p_\xi(x)\le bp_\eta(x)\) for all \(x>0\).  
- Step 1: compute \(bp_\eta(x)\).  
  -  
    \[
    bp_\eta(x) = \frac{e^{1-t}t^t}{\Gamma(t)}\cdot\frac{1}{t}e^{-x/t}
               = \frac{e^{1-t}t^{t-1}}{\Gamma(t)}e^{-x/t}.
    \]  
- Step 2: show \(bp_\eta(x)\ge p_\xi(x)\).  
  - Compare  
    \[
    bp_\eta(x)\quad\text{and}\quad p_\xi(x)=\frac{1}{\Gamma(t)}x^{t-1}e^{-x}.
    \]  
  - Rearranging the inequality \(bp_\eta(x)\ge p_\xi(x)\) leads to  
    \[
    e^{1-t}t^{t-1}e^{-x/t} \ge x^{t-1}e^{-x},
    \]  
    which holds for all \(x>0\) by the choice of \(b\) (this is to be checked in detail as part of understanding the method).  
- Step 3: acceptance event and algorithm.  
  - Generate \((\zeta,\eta)\) with \(\zeta\sim\text{Uni}(0,1)\), \(\eta\sim\text{Exp}(1/t)\), independent.  
  - Accept \(\eta\) as a sample from \(\text{Gamma}(1,t)\) if  
    \[
    b\zeta p_\eta(\eta)\le p_\xi(\eta).
    \]  
  - Otherwise reject and try again.  
  - Divide accepted samples by \(\lambda\) to get Gamma\((\lambda,t)\).  
- Check your intuition.  
  - Exponential is a natural proposal for Gamma because for large \(x\) both tails decay exponentially; the extra polynomial factor \(x^{t-1}\) is compensated by the acceptance probability.  

### 4.2 Constructing N(0,1) from Uni(0,1)
- Setup (Example 2.2, simplified).  
  - Use the probability space \(\Omega=(0,1)\) with Borel σ-algebra and Lebesgue measure, and let \(\xi(\omega)=\omega\sim\text{Uni}(0,1)\).  
  - We want a random variable \(\eta\) with distribution \(N(0,1)\).  
- Step 1: define the standard normal cdf.  
  -  
    \[
    F(x) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^x e^{-t^2/2}\,dt.
    \]  
  - \(F\) is continuous, strictly increasing, and maps \(\mathbb{R}\) onto \((0,1)\).  
- Step 2: invert the cdf.  
  - Define \(\eta(\omega)=F^{-1}(\xi(\omega))=F^{-1}(\omega)\).  
  - By the inversion method, \(\eta\) has cdf \(F\), i.e., \(\eta\sim N(0,1)\).  
- Check your intuition.  
  - Uniform samples \(\omega\) are mapped through the inverse cdf of the normal to produce values that have the correct normal distribution.  

## 5. Lab/Tutorial essentials (week10.pdf)

### 5.1 What the lab asked you to do (recap)
- Multivariate normal computations.  
  - Given a mean vector \(\mu\) and covariance matrix \(K\) for a 3D vector \(\xi\), compute means and variances of several linear combinations (e.g., \(\eta=\xi_1-\xi_3\), etc.).  
  - Given a covariance matrix depending on parameter \(\lambda\), find the value of \(\lambda\) that minimizes the variance of a specific linear combination \(\zeta=\lambda\xi_1+2\xi_2-\xi_3\).  
- Transformations of joint distributions.  
  - For discrete \(X_1,X_2\) with given joint pmf \(f(x_1,x_2)\), find the distribution of \(Y=X_1X_2\).  
  - For a continuous joint density \(f(x,y)\) describing initial amount and amount sold, derive the pdf of the remainder via change-of-variables.  
  - For current \(I\) and resistance \(R\) with given independent densities, derive the pdf of power \(W=I^2R\).  
- Sums of random variables and convolution.  
  - For independent \(\text{Uni}(0,1)\) variables, compute pdfs of \(\xi_1+\xi_2\) and \(\xi_1+\xi_2+\xi_3\) and a probability involving the sum, using convolution.  
- Sampling methods.  
  - Use inversion to sample exponentials (revisiting earlier week).  
  - In rejection method context, show mean number of steps before acceptance is \(1/P(E)=b\).  
- Markov and Chebyshev inequalities.  
  - Compare the Chebyshev bound \(P(|\xi-E\xi|\le 3\sqrt{\text{Var}\xi})\ge 8/9\) with exact probabilities for normal, exponential, and uniform distributions.  
  - Use Chebyshev to find how many trials are needed so that empirical frequencies stay within 0.05 of the true probability with specified confidence levels.  
- Other requested problems (links back to earlier weeks).  
  - Cauchy transformations as in week 6.  
  - Conditional expectation \(E[\xi_2|\xi_1]\) for the uniform unit disk, as in week 7.  

### 5.2 How to solve / approach them (brief)
- Multivariate normal linear combinations.  
  - Use \(E(a^T\xi)=a^T\mu\) and \(\text{Var}(a^T\xi)=a^TKa\).  
  - For minimizing variance with respect to \(\lambda\), treat \(a(\lambda)\) as the coefficient vector and differentiate \(\text{Var}(\zeta)=a(\lambda)^TKa(\lambda)\) with respect to \(\lambda\).  
- Joint transformation problems.  
  - For discrete transformations \(Y=g(X_1,X_2)\), compute \(P(Y=y)\) by summing \(f(x_1,x_2)\) over all pairs that produce \(y\).  
  - For continuous transformations, identify the mapping from \((X,Y)\) to new variables and use Jacobians or cdf methods to get the new pdf.  
- Convolution of uniforms.  
  - For \(\xi_1,\xi_2\sim\text{Uni}(0,1)\), their sum has triangular pdf: increasing on \((0,1)\), decreasing on \((1,2)\).  
  - For three uniforms, convolve again or recall known piecewise polynomial shapes.  
- Markov/Chebyshev comparisons.  
  - Use exact cdfs or known tail probabilities for normal, exponential, and uniform distributions to see that Chebyshev’s bound is conservative.  
  - For number of trials, apply Chebyshev to the sample proportion and solve for \(n\).  

### 5.3 Mini practice
- Practice 1: Gamma identification.  
  - Question: What special distributions are obtained from Gamma\((\lambda,t)\) when \(t=1\) or \(\lambda=1/2,t=n/2\)?  
  - Brief answer: \(t=1\) gives \(\text{Exp}(\lambda)\); \(\lambda=1/2,t=n/2\) gives \(\chi^2(n)\).  
- Practice 2: independent coupling idea.  
  - Question: If \(\xi_1\sim\text{Uni}(0,1)\) and \(\xi_2\sim\text{Uni}(-2,0)\) on different spaces, how can you construct an independent coupling?  
  - Brief answer: Take \(\Omega=\Omega_1\times\Omega_2\) with product measure and define \(\xi_1'(\omega_1,\omega_2)=\xi_1(\omega_1)\), \(\xi_2'(\omega_1,\omega_2)=\xi_2(\omega_2)\); then \((\xi_1',\xi_2')\) is an independent coupling with the desired marginals.  
- Practice 3: exponential sampling via inversion.  
  - Question: Given \(U\sim\text{Uni}(0,1)\), how do you obtain a sample from \(\text{Exp}(\lambda)\)?  
  - Brief answer: Set \(X=-\frac{1}{\lambda}\log U\).  

## 6. Quick recap
- The Gamma distribution unifies exponential and chi-squared families and naturally models waiting times to the \(t\)-th event in a Poisson process, with mean \(t/\lambda\) and variance \(t/\lambda^2\).  
- Rejection sampling provides a practical way to generate Gamma samples when inversion is not available, using an exponential proposal and a constant envelope.  
- Couplings formalize how to place given marginals on a common probability space, with independent couplings built from product spaces and product measures; this underlies constructions of multivariate normals.  
- Basic continuous distributions like \(\text{Uni}(0,1)\) and \(N(0,1)\) can be constructed explicitly from probability spaces using Lebesgue measure and the inversion method.  
- Optimal transport reframes transport maps and costs in terms of couplings, leading to the Monge–Kantorovich formulation.  
- The week 10 recap lab ties together multivariate normals, change-of-variables, convolution, sampling via inversion and rejection, and Markov/Chebyshev bounds as a consolidation of earlier material.  


[<kbd><br><- Return (ProbStat)<br></kbd>](ProbStat.md)
