# CSE206 — Week 09 Notes — Multivariate normal basics, chi-squared, convolution, inversion/rejection sampling
**Lectures:** CSE206_Fa24-09.pdf  
**Lab/Tutorial:** week09.pdf  

## 1. Big picture (5–10 bullets)
- This week continues the study of multivariate normal distributions, focusing on marginals, independence criteria, and sums of Gaussian variables.  
- A key fact: any component of a multivariate normal vector is normal, and for Gaussian vectors, zero covariance (diagonal covariance matrix) implies independence.  
- Sums and linear combinations of independent Gaussian variables remain Gaussian; their means and variances transform linearly.  
- The convolution formula is introduced for the distribution of sums of independent random variables (both discrete and continuous).  
- Two general sampling (simulation) methods are presented: inversion and rejection, both based on a `Uni(0,1)` source.  
- The lab introduces the chi-squared distribution as the sum of squares of independent standard normals, and revisits inversion and rejection methods in concrete tasks.  

## 2. Key concepts and definitions

### 2.1 Marginals of a multivariate normal distribution
- Plain-language statement.  
  - If \(\xi=(\xi_1,\dots,\xi_d)\) has a multivariate normal distribution, then each component \(\xi_j\) is itself a (univariate) normal random variable.  
- Formal result (from Example 1.1).  
  - Let \(\xi\sim N^d(\mu,K)\), where \(\mu=(\mu_1,\dots,\mu_d)\) and \(K\) is the \(d\times d\) covariance matrix.  
  - Then the first component \(\xi_1\) is \(N(\mu_1,k_{11})\), where \(k_{11}\) is the \((1,1)\) entry of \(K\).  
  - The same holds for any component \(\xi_j\): \(\xi_j\sim N(\mu_j,k_{jj})\).  
- Intuition / mental model.  
  - A multivariate normal is like a “Gaussian cloud” in \(\mathbb{R}^d\); looking at any coordinate is like slicing along that axis, which yields a 1D Gaussian.  

### 2.2 Independence criterion for Gaussian random variables
- Plain-language statement.  
  - For Gaussian random variables that are components of the same multivariate normal vector, zero covariance is enough to guarantee independence.  
- Formal result.  
  - Let \(\xi=(\xi_1,\xi_2)\) be a bivariate normal vector with covariance matrix  
    \[
    \text{Cov}(\xi) =
    \begin{pmatrix}
    \sigma_1^2 & 0\\
    0 & \sigma_2^2
    \end{pmatrix}.
    \]  
  - Then the joint pdf factors:  
    \[
    p_\xi(x_1,x_2) = p_{\xi_1}(x_1)p_{\xi_2}(x_2),
    \]  
    and \(\xi_1,\xi_2\) are independent normal random variables.  
  - More generally, if \(\xi=(\xi_1,\dots,\xi_d)\sim N^d(\mu,K)\) and the covariance matrix \(K\) is diagonal (i.e., components are pairwise uncorrelated), then \(\xi_1,\dots,\xi_d\) are independent.  
- Important caveat (Example 1.2).  
  - It is crucial that the variables be components of the same multivariate normal vector.  
  - Example: let \(\xi\sim N(0,1)\), and let \(\eta\) be independent of \(\xi\) with \(P(\eta=1)=P(\eta=-1)=1/2\). Define \(\xi_1=\xi\), \(\xi_2=\eta\xi\).  
  - Both \(\xi_1\) and \(\xi_2\) are \(N(0,1)\). Also \(E(\xi_1\xi_2)=E(\xi^2\eta)=E\eta\cdot E\xi^2=0\), so covariance is zero.  
  - However, \(\xi_1,\xi_2\) are not independent (knowing \(\xi_1\) and \(\xi_2\) lets you recover \(\eta\)), so uncorrelated Gaussian variables are not necessarily independent unless they come from a multivariate normal vector.  
- Intuition / mental model.  
  - Within the multivariate normal family, the covariance matrix fully encodes dependence; zero off-diagonal entries mean “no linear dependence” and actually imply independence.  

### 2.3 Sums and linear combinations of Gaussian random variables
- Plain-language statement.  
  - Any linear combination of independent Gaussian (normal) random variables is itself Gaussian.  
- Formal result (2D case from section 2).  
  - Suppose \(\xi_1,\xi_2\) are independent Gaussian random variables on the same probability space with means \(\mu_1,\mu_2\) and variances \(\sigma_1^2,\sigma_2^2\).  
  - Consider the linear transformation \(T:\mathbb{R}^2\to\mathbb{R}^2\),  
    \[
    T(x_1,x_2) = (x_1+x_2,\, x_1-x_2).
    \]  
  - The random vector \((\xi_1,\xi_2)\) is bivariate normal; applying the transformation yields a new Gaussian vector \((\xi_1+\xi_2,\xi_1-\xi_2)\).  
  - From the covariance calculation,  
    - \(\xi_1+\xi_2\sim N(\mu_1+\mu_2,\sigma_1^2+\sigma_2^2)\).  
    - \(\xi_1-\xi_2\sim N(\mu_1-\mu_2,\sigma_1^2+\sigma_2^2)\).  
- General statement.  
  - If \(\xi_1,\dots,\xi_d\) are independent Gaussian random variables and \(b_1,\dots,b_d\) are constants, then  
    \[
    \eta = b_1\xi_1+\dots+b_d\xi_d
    \]  
    is Gaussian with mean  
    \[
    E\eta = b_1E\xi_1+\dots+b_dE\xi_d,
    \]  
    and variance  
    \[
    \text{Var}(\eta) = b_1^2\text{Var}(\xi_1)+\dots+b_d^2\text{Var}(\xi_d),
    \]  
    because covariances vanish by independence.  
- Intuition / mental model.  
  - Linear combinations of independent Gaussians preserve the “bell shape”; sums only change mean and spread.  

### 2.4 Convolution: sums of independent random variables
- Plain-language definition.  
  - Convolution gives the distribution of a sum of independent random variables by “sliding” one distribution over the other.  
- Discrete case.  
  - Let \(\xi_1,\xi_2\) be independent discrete random variables with pmfs \(p_{\xi_1},p_{\xi_2}\). The pmf of \(\xi_1+\xi_2\) is  
    \[
    p_{\xi_1+\xi_2}(x) = \sum_y p_{\xi_1}(x-y)p_{\xi_2}(y).
    \]  
- Continuous case.  
  - Let \(\xi_1,\xi_2\) be independent continuous random variables with pdfs \(p_{\xi_1},p_{\xi_2}\). The pdf of \(\xi_1+\xi_2\) is  
    \[
    p_{\xi_1+\xi_2}(x) = \int_{\mathbb{R}} p_{\xi_1}(x-y)p_{\xi_2}(y)\,dy.
    \]  
- Generalization.  
  - The same idea extends inductively to sums of \(n\) independent variables.  
- Intuition / mental model.  
  - To get a total of \(x\), the first variable can be \(x-y\) while the second is \(y\); we sum (or integrate) over all possible matching \(y\).  

### 2.5 Inversion method for sampling
- Plain-language description.  
  - The inversion method uses a `Uni(0,1)` random variable \(\zeta\) and the inverse of a cdf to generate samples from a desired distribution.  
- Formal statement (Theorem 3.1).  
  - Let \(F\) be a distribution function and \(\zeta\sim\text{Uni}(0,1)\).  
  - (i) If \(F\) is strictly increasing and continuous, the random variable \(\xi = F^{-1}(\zeta)\) has cdf \(F\).  
  - (ii) If \(F\) is the cdf of a discrete random variable taking nonnegative integer values, define  
    \[
    \xi = k \quad \text{iff}\quad F(k-1) < \zeta \le F(k),
    \]  
    then \(\xi\) has distribution function \(F\).  
- Intuition / mental model.  
  - The cdf \(F\) maps the real line to \([0,1]\); applying the inverse mapping to a uniform random variable “pushes” uniform samples into samples with distribution \(F\).  
- Tiny example (from Example 3.2).  
  - Let \(\zeta_1,\dots,\zeta_n\) be independent `Uni(0,1)` variables. For each \(j\), define  
    \[
    \xi_j = I(\zeta_j\le p).
    \]  
  - Then each \(\xi_j\sim\text{Bernoulli}(p)\) and \(\xi_1+\dots+\xi_n\sim\text{Binomial}(n,p)\).  

### 2.6 Rejection method for sampling
- Plain-language description.  
  - The rejection (accept-reject) method simulates from a complicated density by sampling from a simpler “proposal” density and randomly accepting or rejecting points, such that accepted values follow the target density.  
- Setup (from section 3.2).  
  - Target density: \(p_\xi(x)\).  
  - Proposal density: \(p_\eta(x)\), with a constant \(b>1\) such that  
    \[
    p_\xi(x)\le b p_\eta(x)\quad \text{for all }x.
    \]  
  - Generate an independent pair \((\zeta,\eta)\) where \(\zeta\sim\text{Uni}(0,1)\) and \(\eta\) has pdf \(p_\eta\).  
  - Define event  
    \[
    E = \{b\zeta p_\eta(\eta)\le p_\xi(\eta)\}.
    \]  
- Main result (sketched in lecture).  
  - Conditional on the event \(E\) (acceptance), the random variable \(\eta\) has the target pdf \(p_\xi\).  
  - The probability of acceptance is \(1/b\), so the expected number of iterations (pairs generated) before acceptance is \(b\). (The lab asks you to show the mean number of steps before \(E\) occurs is \(1/(1/b)=b\), or equivalently, mean steps \(1/P(E)\).)  
- Algorithm.  
  1. Generate \((\zeta,\eta)\) from proposal.  
  2. If \(b\zeta p_\eta(\eta)\le p_\xi(\eta)\), accept \(\eta\) as a sample from \(p_\xi\); else, reject and try again.  
- Intuition / mental model.  
  - The inequality compares a scaled uniform value with the ratio \(p_\xi(\eta)/p_\eta(\eta)\); only points that lie “under the target curve” are accepted.  

## 3. Core formulas and how to use them

### 3.1 Marginals of multivariate normal
- For \(\xi\sim N^d(\mu,K)\):  
  - The \(j\)-th component \(\xi_j\) has  
    \[
    \xi_j\sim N(\mu_j,k_{jj}),
    \]  
    where \(k_{jj}\) is the \(j\)-th diagonal element of \(K\).  
- When to use it.  
  - Whenever you have a multivariate normal vector but only need the distribution of one coordinate or one linear combination.  

### 3.2 Independence criterion for Gaussians
- For \(\xi=(\xi_1,\dots,\xi_d)\sim N^d(\mu,K)\):  
  - If \(K\) is diagonal, then the components \(\xi_1,\dots,\xi_d\) are independent.  
  - In 2D: if \(\text{Cov}(\xi_1,\xi_2)=0\), then \(\xi_1,\xi_2\) are independent normals.  
- When to use it.  
  - To check independence in Gaussian models: you only need to inspect the covariance matrix.  

### 3.3 Convolution for sums
- Discrete:  
  - \[
    p_{\xi_1+\xi_2}(x) = \sum_{y} p_{\xi_1}(x-y)p_{\xi_2}(y).
    \]  
- Continuous:  
  - \[
    p_{\xi_1+\xi_2}(x) = \int_{\mathbb{R}} p_{\xi_1}(x-y)p_{\xi_2}(y)\,dy.
    \]  
- When to use it.  
  - To find pdfs or pmfs of sums of independent variables (e.g., sums of uniforms or exponentials in homework).  

### 3.4 Inversion method for exponentials (lab task)
- Exponential cdf.  
  - For \(\xi\sim\text{Exp}(\lambda)\):  
    \[
    F_\xi(x) = 1-e^{-\lambda x},\quad x\ge 0.
    \]  
- Inverse cdf.  
  - Set \(\zeta\sim\text{Uni}(0,1)\) and solve \(\zeta = 1-e^{-\lambda x}\) for \(x\):  
    \[
    e^{-\lambda x} = 1-\zeta \quad\Rightarrow\quad x = -\frac{1}{\lambda}\ln(1-\zeta).
    \]  
  - Since \(1-\zeta\) is also uniform on \((0,1)\), one often writes \(x = -\frac{1}{\lambda}\ln\zeta\).  
- When to use it.  
  - To generate exponential samples from a uniform RNG in simulations.  

## 4. Worked examples

### 4.1 Chi-squared distribution with 1 degree of freedom
- Setup (lab Problem 1).  
  - Let \(\xi\sim N(0,1)\). Define \(\eta=\xi^2\). We want the pdf of \(\eta\).  
- Step 1: relate cdfs.  
  - For \(x>0\):  
    \[
    P(\eta\le x) = P(\xi^2\le x) = P(-\sqrt{x}\le \xi \le \sqrt{x}) = \Phi(\sqrt{x})-\Phi(-\sqrt{x}),
    \]  
    where \(\Phi\) is the standard normal cdf.  
  - Using symmetry, this equals \(2\Phi(\sqrt{x})-1\). For \(x\le0\): \(P(\eta\le x)=0\).  
- Step 2: differentiate to get pdf.  
  - For \(x>0\):  
    \[
    p_\eta(x) = \frac{d}{dx}P(\eta\le x) = \frac{d}{dx}(2\Phi(\sqrt{x})-1)
              = 2\phi(\sqrt{x})\cdot \frac{1}{2\sqrt{x}}
              = \frac{\phi(\sqrt{x})}{\sqrt{x}},
    \]  
    where \(\phi\) is the standard normal pdf.  
  - Since \(\phi(t)=\frac{1}{\sqrt{2\pi}}e^{-t^2/2}\), we obtain  
    \[
    p_\eta(x) = \frac{1}{\sqrt{2\pi}}x^{-1/2}e^{-x/2}I(x>0).
    \]  
- Step 3: recognize the chi-squared distribution.  
  - This is exactly the pdf of a chi-squared random variable with 1 degree of freedom, \(\chi^2(1)\).  
- Check your intuition.  
  - Squaring a standard normal makes all values nonnegative and increases weight near 0; the resulting distribution is skewed right and heavy towards small positive values.  

### 4.2 Chi-squared distribution with \(n\) degrees of freedom (outline)
- Setup (lab Problem 2).  
  - Let \(\xi_1,\dots,\xi_n\) be independent standard normals. Define  
    \[
    \xi = \xi_1^2+\dots+\xi_n^2.
    \]  
  - Show the pdf is  
    \[
    p_\xi(x)=f(x;n) = \frac{1}{2^{n/2}\Gamma(n/2)} x^{n/2-1}e^{-x/2}I(x>0),
    \]  
    i.e., chi-squared with parameter \(n\), written \(\xi\sim\chi^2(n)\).  
- Step 1: base case \(n=2\).  
  - Write \((\xi_1,\xi_2)\) in polar coordinates, exploit rotational symmetry, and derive the distribution of \(\xi_1^2+\xi_2^2\) (distance squared from the origin).  
  - Differentiate its cdf to obtain \(f(x;2)\).  
- Step 2: convolution step.  
  - Assume a variable with pdf \(f(\cdot;n)\) and an independent variable with pdf \(f(\cdot;2)\).  
  - Use the convolution formula to show their sum has pdf \(f(\cdot;n+2)\).  
- Step 3: induction.  
  - Starting from the base case \(n=2\) and repeatedly adding independent \(\xi_j^2\) terms, conclude the formula holds for all even \(n\), and with extra care for all integer \(n\ge1\).  
- Check your intuition.  
  - Summing squared standard normals corresponds to squared length of an \(n\)-dimensional Gaussian vector; as dimension increases, the distribution spreads out and its shape changes, but remains in the chi-squared family.  

## 5. Lab/Tutorial essentials (week09.pdf)

### 5.1 What the lab asked you to do
- Problem 1: pdf of \(\xi^2\) for \(\xi\sim N(0,1)\).  
  - Derive and recognize the chi-squared(1) distribution (see Worked Example 4.1).  
- Problem 2: chi-squared distribution with \(n\) degrees of freedom.  
  - For independent standard normals \(\xi_1,\dots,\xi_n\), show that \(\xi_1^2+\dots+\xi_n^2\) has pdf \(f(x;n)\) using polar coordinates and convolution.  
- Problem 3: distribution of \([n\zeta]+1\) for \(\zeta\sim\text{Uni}(0,1)\).  
  - Here \([\cdot]\) is the integer part; the aim is to find the discrete distribution (pmf) of this random variable.  
- Problem 4: mean number of steps in the rejection method.  
  - Show that the mean number of iterations needed before the event \(E\) occurs in the rejection algorithm is \(1/P(E)\), and given the acceptance probability is \(1/b\), the mean number of steps is \(b\) (equivalently, the expected number of trials before a success is geometric).  
- Problem 5: inversion method for exponential distribution with parameter \(\lambda\).  
  - Use the inversion method to derive the sampling formula for \(\text{Exp}(\lambda)\) as in section 3.4.  
- Homework topics.  
  - Find constants and covariance matrices in multivariate normal densities.  
  - Work with joint normal distributions for vectors \((X_1,X_2,Y_1,Y_2)\).  
  - Compute probabilities involving distances when coordinates have normal errors.  
  - Use convolution and change-of-variable methods to get pdfs of sums, differences, products, and other functions of uniform and exponential random variables in 1D and 2D.  

### 5.2 How to solve / approach them
- Distribution of \([n\zeta]+1\) (Problem 3).  
  - Partition \((0,1)\) into intervals of length \(1/n\): \((0,1/n],(1/n,2/n],\dots,((n-1)/n,1]\).  
  - For each \(k\in\{1,\dots,n\}\),  
    \[
    P([n\zeta]+1=k) = P\left(\frac{k-1}{n}<\zeta\le\frac{k}{n}\right) = \frac{1}{n},
    \]  
    so \([n\zeta]+1\) is discrete uniform on \(\{1,\dots,n\}\).  
- Mean number of steps in rejection (Problem 4).  
  - Each iteration accepts with probability \(P(E)\) independently.  
  - The number of trials until the first success has a geometric distribution with mean \(1/P(E)\); if \(P(E)=1/b\), the expected number of steps is \(b\).  
- Inversion for exponential (Problem 5).  
  - Start from the cdf \(F(x)=1-e^{-\lambda x}\).  
  - Solve \(F(x)=\zeta\) for \(x\), giving \(x=-\frac{1}{\lambda}\ln(1-\zeta)\).  
  - Implement sampling as \(x=-\frac{1}{\lambda}\ln(U)\) with \(U\sim\text{Uni}(0,1)\).  
- Convolutions and transformations in homework.  
  - For sums/differences of uniforms and exponentials, apply the convolution formula directly.  
  - For products and more complicated functions, use change-of-variable techniques, possibly in 2D if combining two independent variables.  

### 5.3 Mini practice
- Practice 1: independence criterion for Gaussians.  
  - Question: Let \((\xi_1,\xi_2)\sim N^2(\mu,K)\) with covariance matrix  
    \(\begin{pmatrix}\sigma_1^2 & 0\\0&\sigma_2^2\end{pmatrix}\). Are \(\xi_1,\xi_2\) independent?  
  - Brief answer: Yes. For a bivariate normal vector, zero covariance (diagonal covariance matrix) implies the joint pdf factors as the product of two normal pdfs, so the components are independent.  
- Practice 2: distribution from integer part.  
  - Question: If \(\zeta\sim\text{Uni}(0,1)\), what is the distribution of \([5\zeta]+1\)?  
  - Brief answer: Discrete uniform on \(\{1,2,3,4,5\}\); each value occurs with probability \(1/5\).  
- Practice 3: exponential sampling.  
  - Question: Given a uniform random variable \(U\sim\text{Uni}(0,1)\), how can you generate a sample from \(\text{Exp}(\lambda)\)?  
  - Brief answer: Set \(X=-\frac{1}{\lambda}\ln U\); this has cdf \(1-e^{-\lambda x}\) and so is \(\text{Exp}(\lambda)\).  

## 6. Quick recap
- Any component of a multivariate normal vector is itself normally distributed, with mean and variance taken from the corresponding entries of the mean vector and covariance matrix.  
- For Gaussian random variables that are components of a multivariate normal, zero covariance (diagonal covariance matrix) implies independence, a special property not shared by general distributions.  
- Sums and linear combinations of independent Gaussian random variables remain Gaussian, with means and variances obtained via linearity and variance-addition.  
- The convolution formula gives the pmf/pdf of a sum of independent random variables by summing or integrating products of their distributions.  
- The inversion and rejection sampling methods allow us to simulate from many distributions starting from a `Uni(0,1)` source, and the lab applies these ideas to exponentials and general densities.  
- The lab also develops the chi-squared distribution as the sum of squares of independent standard normal variables, linking normal and chi-squared families.  


[<kbd><br><- Return (ProbStat)<br></kbd>](ProbStat.md)
