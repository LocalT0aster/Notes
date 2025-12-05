# Probability & Statistics — Formulas

Quick reference of the formulas used across the weekly notes, with brief explanations and symbol keys. See weekly notes for full context and examples.

## Week 01 — Descriptive stats
- Sample mean: $\bar{x} = \frac{1}{n}\sum_{j=1}^n x_j$. Average of the sample values.
- Median (odd $n$): $m = y_{(n+1)/2}$; (even $n$): $m = \frac{y_{n/2}+y_{n/2+1}}{2}$. Middle ordered value(s).
- Sample variance / SD: $s^2 = \frac{1}{n-1}\sum_{j=1}^n (x_j-\bar{x})^2$, $s=\sqrt{s^2}$. Uses $n-1$ to estimate population variance from a sample.
- Mean absolute deviation: $\text{m.a.d.} = \frac{1}{n}\sum_{j=1}^n |x_j-\bar{x}|$. Average absolute distance from the mean.
- Empirical CDF: $F_{\text{emp}}(x)=\frac{1}{n}\#\{j: x_j\le x\}$. Fraction of data at or below $x$.
  - Symbols: $x_j$ data points, $n$ sample size, $y_j$ ordered values, $\#\{\cdot\}$ count.

## Week 02 — Probability basics
- Kolmogorov axioms: $P(\varnothing)=0$, $P(\Omega)=1$, $P(\bigcup A_j)=\sum P(A_j)$ for disjoint $A_j$.
- Combinatorial probability (finite uniform): $P(E)=\frac{\#E}{n}$.
- Inclusion–exclusion (two events): $P(A\cup B)=P(A)+P(B)-P(A\cap B)$.
- Independence: $P(A\cap B)=P(A)P(B)$.
- Conditional probability: $P(A|B)=\frac{P(A\cap B)}{P(B)}$.
- Total probability / Bayes: $P(A)=\sum_j P(A|B_j)P(B_j)$; $P(B_j|A)=\frac{P(A|B_j)P(B_j)}{\sum_k P(A|B_k)P(B_k)}$.
  - Symbols: $A,B,B_j$ events; $\Omega$ sample space; $\#E$ count; $n$ outcomes.

## Week 03 — Random variables (discrete)
- CDF: $F_X(x)=P(X\le x)$ (step function for discrete $X$).
- PMF: $p_X(x)=P(X=x)$ with $\sum_x p_X(x)=1$.
- PMF/CDF link (discrete): jump at $x_j$ equals $p_X(x_j)=F_X(x_j)-\lim_{x\to x_j^-}F_X(x)$.
  - Symbols: $X$ random variable; $p_X$ pmf; $F_X$ cdf; $x_j$ support points.

## Week 04 — Expectation, variance, covariance
- Expectation (discrete): $E\xi=\sum_x x\,p_\xi(x)$; of a function: $E g(\xi)=\sum_x g(x)p_\xi(x)$.
- Variance: $\text{Var}(\xi)=E(\xi-E\xi)^2=E\xi^2-(E\xi)^2$.
- Linearity: $E\left(\sum_j \xi_j\right)=\sum_j E\xi_j$; $\text{Var}(c\xi)=c^2\text{Var}(\xi)$; for independent $\xi_j$, $\text{Var}(\sum_j \xi_j)=\sum_j \text{Var}(\xi_j)$.
- Covariance / correlation: $\text{Cov}(\xi_1,\xi_2)=E\xi_1\xi_2-E\xi_1E\xi_2$; $\rho=\frac{\text{Cov}(\xi_1,\xi_2)}{\sqrt{\text{Var}(\xi_1)\text{Var}(\xi_2)}}$.
- Markov: $P(\xi\ge x)\le \frac{E\xi}{x}$ for $\xi\ge0$; Chebyshev: $P(|\xi-E\xi|\ge x)\le \frac{\text{Var}(\xi)}{x^2}$.
  - Symbols: $\xi,\xi_j$ random variables; $p_\xi$ pmf; $g$ measurable function; $c$ constant; $x>0$ bound.

## Week 05 — Continuous r.v.s, pdf/cdf, normal
- PDF/CDF link: $F_\xi(x)=\int_{-\infty}^x p_\xi(t)\,dt$; if $F_\xi$ differentiable, $p_\xi(x)=F'_\xi(x)$.
- Uniform $(a,b)$: $p_\xi(x)=\frac{1}{b-a}I(a<x<b)$; $F_\xi(x)=0$ ($x\le a$), $(x-a)/(b-a)$ ($a<x<b$), $1$ ($x\ge b$); $E\xi=\frac{a+b}{2}$, $\text{Var}(\xi)=\frac{(b-a)^2}{12}$.
- Normal $(\mu,\sigma^2)$ pdf: $p_\xi(x)=\frac{1}{\sqrt{2\pi}\sigma}\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$; standardization $\eta=\frac{\xi-\mu}{\sigma}\sim N(0,1)$.
  - Symbols: $p_\xi$ pdf; $F_\xi$ cdf; $I(\cdot)$ indicator; $\mu,\sigma$ mean/SD; $a,b$ interval endpoints.

## Week 06 — Hypergeometric, exponential, Cauchy, transforms
- Hypergeometric pmf: $P(\xi=x)=\frac{\binom{b}{x}\binom{N-b}{n-x}}{\binom{N}{n}}$; $E\xi=\frac{bn}{N}$; $\text{Var}(\xi)=\frac{bn(N-b)(N-n)}{N^2(N-1)}$.
- Exponential pdf: $p_\xi(x)=\lambda e^{-\lambda x}I(x\ge0)$; $E\xi=1/\lambda$; $\text{Var}(\xi)=1/\lambda^2$; memoryless $P(\xi>t+s|\xi>t)=P(\xi>s)$.
- Cauchy pdf: $p_\xi(x)=\frac{1}{\pi(1+x^2)}$ (no finite moments).
- Expectation via density: $E\xi=\int x p_\xi(x)\,dx$; $E g(\xi)=\int g(x)p_\xi(x)\,dx$.
- Density of $f(\xi)$ (invertible $f$): $p_\eta(y)=p_\xi(f^{-1}(y))\left|\frac{d}{dy}f^{-1}(y)\right|I(y\in \text{image})$.
  - Symbols: $N$ population size, $b$ good items, $n$ draws; $\lambda$ rate; $f$ transformation; $\eta=f(\xi)$.

## Week 07 — Poisson, joint pdfs, conditionals, transforms
- Poisson pmf: $P(\xi=k)=\frac{\lambda^k e^{-\lambda}}{k!}$ for $k\in\mathbb{N}$.
- Joint pdf to marginal: $p_{\xi_1}(x_1)=\int p_{\xi}(x_1,x_2)\,dx_2$ (similarly for other components).
- Conditional pdf (continuous): $p_{\xi_2|\xi_1}(x_2|x_1)=\frac{p_{\xi}(x_1,x_2)}{p_{\xi_1}(x_1)}$.
- Transformation with Jacobian (invertible map $T$): $p_\eta(y)=p_\xi(T^{-1}(y))\left|\det J_{T^{-1}}(y)\right|$.
  - Symbols: $\lambda$ rate; $p_\xi$ joint pdf; $J_{T^{-1}}$ Jacobian of inverse map; $\eta=T(\xi)$.

## Week 09 — Multivariate normal, chi-squared, sampling
- Multivariate normal pdf: $p_\xi(x)=\frac{1}{(2\pi)^{d/2}\sqrt{\det K}}\exp\left(-\frac{1}{2}(x-\mu)^T K^{-1}(x-\mu)\right)$.
- Chi-squared (sum of squares of $d$ iid $N(0,1)$): cdf/pdfs as special case (noted in lecture).
- Inversion sampling: $\xi=F^{-1}(U)$ with $U\sim \text{Uni}(0,1)$ gives cdf $F$.
- Exponential sampling via inversion: $X=-\frac{1}{\lambda}\ln U$ has $F(x)=1-e^{-\lambda x}$.
  - Symbols: $\mu$ mean vector, $K$ covariance matrix, $d$ dimension; $U$ uniform(0,1).

## Week 10 — Couplings, transport (selected formulas)
- Standardization of sums (CLT-style): $\frac{S_n-n\mu}{\sigma\sqrt{n}}$ used for normal approximations.
- Transport cost intuition (no specific closed form given in notes; see week10 text for details).
  - Symbols: $S_n$ sum, $\mu$ mean, $\sigma$ SD.

## Week 11 — WLLN, Bernstein, CLT
- Bernstein bound (Bernoulli sample mean): $P\left(\left|\frac{S_n}{n}-p\right|\ge\varepsilon\right)\le 2e^{-n\varepsilon^2/4}$.
- Chebyshev for Bernoulli: $P\left(\left|\frac{S_n}{n}-p\right|\ge\varepsilon\right)\le \frac{p(1-p)}{n\varepsilon^2}$.
- CLT normalization: $\frac{S_n-n\mu}{\sigma\sqrt{n}}\xrightarrow{d}N(0,1)$; sample mean version $\frac{\bar{\xi}_n-\mu}{\sigma/\sqrt{n}}\xrightarrow{d}N(0,1)$.
  - Symbols: $S_n$ sum of iid with mean $\mu$, variance $\sigma^2$; $p$ Bernoulli parameter; $\varepsilon>0$ tolerance.

## Week 12 — Estimation and confidence intervals
- Shifted exponential-type CI (minimum-based): for pdf $e^{-(x-\theta)}I(x\ge\theta)$, with sample minimum $m$, choose $c_\alpha$ s.t. $P(m-\theta\ge c_\alpha)=\alpha$; interval $(m-c_\alpha,\,m)$ has level $1-\alpha$.
- Normal mean, variance known: $\bar{\xi}_n \pm z_{1-\alpha/2}\frac{\sigma}{\sqrt{n}}$ is a $(1-\alpha)$ CI for $\theta$.
- Normal variance, mean known: based on $\chi^2$ (see week12 text for exact quantiles).
  - Symbols: $\bar{\xi}_n$ sample mean; $\sigma$ known SD; $z_{1-\alpha/2}$ standard normal quantile; $m$ sample minimum; $\alpha$ significance.

## Week 13 — Risk, UMVU, median asymptotics
- Risk (squared error): $R(\hat{\theta},\theta)=E_\theta[(\hat{\theta}-\theta)^2]$.
- Sample median definition: for ordered $\xi_{(1)}\le\dots\le\xi_{(n)}$, median is $\xi_{(j+1)}$ if $n=2j+1$; $(\xi_{(j)}+\xi_{(j+1)})/2$ if $n=2j$.
- Asymptotic normality (informal): $\sqrt{n}(\text{median}-\theta)\xrightarrow{d}N\left(0,\frac{1}{4p_\xi(\theta)^2}\right)$ when density at median $\theta$ is positive.
  - Symbols: $\hat{\theta}$ estimator; $\theta$ true parameter; $p_\xi$ density at median.

## Week 14 — Method of moments, MLE, hypothesis testing
- Sample moments: $M_k=\frac{1}{n}\sum_{j=1}^n \xi_j^k$; method-of-moments solves $\alpha_k(\theta)=M_k$.
- Likelihood (iid): $L(\theta)=\prod_{j=1}^n p_\xi(x_j;\theta)$; log-likelihood $\ell(\theta)=\sum_{j=1}^n \ln p_\xi(x_j;\theta)$.
- One-sided normal test (variance known): reject $H_0:\theta=\theta_0$ if $\bar{\xi}_n\ge \theta_0+z_{1-\alpha}\frac{\sigma}{\sqrt{n}}$.
  - Symbols: $\xi_j$ sample; $\alpha_k$ theoretical moments; $\theta$ parameter(s); $p_\xi$ model density/pmf; $\sigma$ known SD; $z_{1-\alpha}$ quantile.

## Week 15 — Hypothesis testing II
- Power function (conceptual): $\beta(\theta)=P_\theta(\text{reject }H_0)$; aim for small Type I, large power on $H_1$.
- Unbiased/consistent tests: see week15 notes for specific constructions; formulas follow the same critical-value pattern as week14.
  - Symbols: $\beta(\theta)$ power; $\alpha$ significance; $H_0,H_1$ hypotheses.

[<kbd><br><- Return (ProbStat)<br></kbd>](ProbStat.md)
