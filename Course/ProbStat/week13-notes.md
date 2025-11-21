# CSE206 — Week 13 Notes — UMVU, risk, Cauchy caveat, sample median asymptotics
**Lectures:** CSE206_Fa24-13.pdf
**Lab/Tutorial:** none

## 1. Big picture (5–10 bullets)
- This week continues estimation theory, focusing on how to compare estimators and when a “best” unbiased estimator exists.
- The risk function measures how bad an estimator is on average, using a chosen loss function such as squared error.
- Uniform minimum variance unbiased (UMVU) estimators are unbiased estimators that have the smallest possible variance among all unbiased estimators, for every parameter value.
- In common models (normal, Bernoulli, uniform), familiar statistics like the sample mean and a scaled sample maximum are UMVU estimators for natural parameters.
- The sample mean can fail dramatically when the underlying distribution has no mean or variance (Cauchy model), so alternative estimators like the sample median are needed.
- The sample median is defined carefully using the ordered sample and has good asymptotic behavior for continuous distributions.
- A general asymptotic result shows that, under mild conditions, the sample median is approximately normal around the true median when the sample size is large, with a variance depending on the underlying density at the median.

## 2. Key concepts and definitions

### 2.1 Risk function and loss
- Plain-language definition.
  - A loss function measures how big the error is when we use an estimator instead of the true parameter.
  - The risk function is the expected loss; it tells us on average how far off an estimator is for each possible value of the parameter.
- Formal definitions.
  - Let $\rho:\mathbb{R}\to[0,+\infty)$ be a loss function such that $\rho(0)=0$ and $\rho(t)$ increases as $|t|$ increases.
  - For an estimator $\hat{\theta}(\xi_1,\dots,\xi_n)$, the $\rho$-risk function is
    $$
    R(\hat{\theta},\theta) = E_\theta\big[\rho\big(\hat{\theta}(\xi_1,\dots,\xi_n)-\theta\big)\big],
    $$
    where $E_\theta$ is expectation under the model with true parameter $\theta$.
- Important special case: squared error.
  - If $\rho(t)=t^2$, then
    $$
    R(\hat{\theta},\theta) = E_\theta\big[(\hat{\theta}-\theta)^2\big],
    $$
    which is the mean squared error.
  - When $\hat{\theta}$ is unbiased, mean squared error equals the variance of $\hat{\theta}$.
- Intuition / mental model.
  - Risk links an estimator and a loss function: lower risk means “better” performance with respect to that loss.
  - Comparing risk functions across estimators shows which estimator is preferable for each parameter value.

### 2.2 UMVU estimators
- Plain-language definition.
  - A UMVU estimator is an unbiased estimator that has the smallest variance among all unbiased estimators, for every value of the parameter.
  - “Uniform” refers to this minimal variance property holding uniformly over all parameter values.
- Formal definition.
  - An estimator $\hat{\theta}$ is called a UMVU (uniform minimum variance unbiased) estimator for $\theta$ if:
    - $\hat{\theta}$ is unbiased: $E_\theta[\hat{\theta}]=\theta$ for all $\theta\in\Theta$.
    - For any other unbiased estimator $\hat{\theta}'$, we have
      $$
      \text{Var}_\theta(\hat{\theta}) \le \text{Var}_\theta(\hat{\theta}')
      $$
      for all $\theta\in\Theta$.
- Examples from the lecture (facts).
  - Normal model: if $\xi\sim N(\mu,\sigma^2)$, then:
    - The sample mean $\bar{\xi}_n=S_n/n$ is UMVU for $\mu$.
    - The standard unbiased variance estimator $\hat{V}$ (built from squared deviations) is UMVU for $\sigma^2$.
  - Bernoulli model: if $\xi\sim \text{Bernoulli}(p)$, then $\bar{\xi}_n=S_n/n$ is UMVU for $p$.
  - Uniform model: if $\xi\sim\text{Uni}(0,\theta)$ (or $\text{Uni}(\theta)$ in the lecture’s notation) then
    $$
    \hat{\theta} = \frac{n+1}{n}\max\{\xi_1,\dots,\xi_n\}
    $$
    is UMVU for $\theta$.
- Intuition / mental model.
  - Among all unbiased estimators of a parameter, the UMVU estimator is the one that fluctuates least (has smallest variance), so it is in that sense the most “stable” unbiased choice.

### 2.3 Cauchy distribution and failure of the sample mean
- Cauchy model.
  - The (standard) Cauchy distribution has pdf
    $$
    p(x) = \frac{1}{\pi(x^2+1)}.
    $$
  - A location family Cauchy($\theta$) is defined by
    $$
    p(x;\theta) = \frac{1}{\pi((x-\theta)^2+1)},
    $$
    with parameter $\theta$ as a location (shift) parameter.
- Key property (mentioned).
  - For Cauchy($\theta$), neither the mean nor the variance exists (integrals defining them diverge).
  - If $\xi_1,\dots,\xi_n$ is a sample of Cauchy($\theta$), then for any $n$:
    $$
    \frac{1}{n}(\xi_1+\dots+\xi_n)
    $$
    also has the same Cauchy($\theta$) distribution.
  - Thus,
    $$
    P\left(\frac{\xi_1+\dots+\xi_n}{n}\ge x\right) = P(\xi\ge x)
    $$
    for all $x$, and the distribution of the sample mean does not concentrate as $n$ grows.
- Intuition / mental model.
  - Heavy tails make extreme observations common enough that the average remains as unstable as a single observation.
  - CLT fails because the second moment is infinite; the sample mean is not a suitable estimator of a central location here.

### 2.4 Quantiles, median, and sample median
- Quantiles.
  - For a distribution with cdf $F$, an $\alpha$-quantile $x_\alpha$ is a value satisfying
    $$
    F(x_\alpha) = \alpha,\quad 0<\alpha<1.
    $$
  - The median is the 0.5-quantile $x_{1/2}$.
- Cauchy median.
  - For Cauchy($\theta$) with pdf $p(x;\theta)=\pi^{-1}[(x-\theta)^2+1]^{-1}$, the median is $x_{1/2}=\theta$ because the distribution is symmetric around $\theta$.
- Sample median (Definition 2.1).
  - Given a sample $\xi_1,\dots,\xi_n$, sort them into increasing order:
    $$
    \xi_{(1)}\le \xi_{(2)}\le \dots\le \xi_{(n)}.
    $$
  - The sample median (denoted MAD in the lecture, though this is usually “median absolute deviation”) is
    $$
    \text{MAD}=
    \begin{cases}
      \xi_{(j+1)}, &\text{if } n=2j+1 \text{ (odd sample size)},\$$4pt]
      \frac{1}{2}(\xi_{(j)}+\xi_{(j+1)}), &\text{if } n=2j \text{ (even sample size)}.
    \end{cases}
    $$
- Intuition / mental model.
  - The sample median is the “middle” observation when data are ordered.
  - It is robust to extreme values and is a natural estimator of the distribution’s median (e.g., $\theta$ in Cauchy($\theta$)).

### 2.5 Asymptotic normality of the sample median
- Theorem 2.2 (informal).
  - Let $\xi$ be a continuous random variable with pdf $p_\xi$. Let $x_{1/2}$ be its median. Assume the density near the median is positive in the sense that
    $$
    \lim_{\delta\to 0^+}\frac{1}{2\delta}\int_{x_{1/2}-\delta}^{x_{1/2}+\delta} p_\xi(x)\,dx > 0.
    $$
  - Let MAD be the sample median of a sample of size $n$ from $\xi$. Then
    $$
    \sqrt{n}( \text{MAD} - x_{1/2}) \xrightarrow{d} Z\sim N\left(0,\frac{1}{4p_\xi(x_{1/2})^2}\right).
    $$
  - That is, for large $n$, the sample median is approximately normal around the true median, with variance decreasing like $1/n$.
- Intuition / mental model.
  - Although the sample median is defined via order statistics, it behaves similarly to the sample mean in large samples (approximately normal), but is more robust to outliers.
  - The variance depends on the density at the median: if the density is high there (steep cdf), the median is estimated more precisely.

## 3. Core formulas and how to use them

### 3.1 Risk function
- Formula.
  - For estimator $\hat{\theta}$ and loss $\rho$:
    $$
    R(\hat{\theta},\theta) = E_\theta\big[\rho(\hat{\theta}-\theta)\big].
    $$
- Symbols.
  - $\hat{\theta}$: estimator (statistic).
  - $\theta$: true parameter.
  - $E_\theta$: expectation under the model parameterized by $\theta$.
  - $\rho$: loss function, e.g., $\rho(t)=t^2$.
- When to use it.
  - When comparing estimators under a given loss; smaller risk is better.
  - For squared loss and unbiased estimators, minimizing risk is equivalent to minimizing variance.

### 3.2 UMVU characterization
- Condition.
  - $\hat{\theta}$ is UMVU if:
    1. Unbiasedness: $E_\theta(\hat{\theta})=\theta$ for all $\theta\in\Theta$.
    2. Minimum variance among unbiased estimators: for any unbiased $\hat{\theta}'$:
       $$
       \text{Var}_\theta(\hat{\theta}) \le \text{Var}_\theta(\hat{\theta}')
       $$
       for all $\theta$.
- When to use it.
  - In classical parametric models (normal, Bernoulli, uniform) to identify “best” unbiased estimators.
  - When asked which estimator is preferred among unbiased candidates.

### 3.3 Cauchy sample mean behavior
- Key property.
  - If $\xi_1,\dots,\xi_n$ are i.i.d. Cauchy($\theta$), then
    $$
    \frac{\xi_1+\dots+\xi_n}{n} \sim \text{Cauchy}(\theta)
    $$
    for all $n$.
- When to use it.
  - To show that the sample mean is not consistent (does not converge) for heavy-tailed distributions like Cauchy and that LLN/CLT assumptions fail (no finite mean/variance).
- Common misconceptions.
  - Assuming that the sample mean always becomes stable as $n$ grows; this is false when the underlying distribution lacks a mean or variance.

### 3.4 Sample median asymptotic variance
- Asymptotic variance formula.
  - Under the conditions of Theorem 2.2, as $n\to\infty$:
    $$
    \sqrt{n}(\text{MAD}-x_{1/2}) \xrightarrow{d} N\left(0,\frac{1}{4p_\xi(x_{1/2})^2}\right).
    $$
- When to use it.
  - To approximate the distribution of the sample median for large samples, enabling confidence intervals and error bars for medians.
  - Particularly useful when means are not robust or not defined (like Cauchy).

## 4. Worked examples

### 4.1 Risk of the sample mean in a Bernoulli model
- Setup.
  - Let $\xi_1,\dots,\xi_n\sim \text{Bernoulli}(\theta)$ be independent, and consider the estimator
    $$
    \hat{\theta} = \frac{1}{n}\sum_{j=1}^n \xi_j.
    $$
  - Take squared loss $\rho(t)=t^2$.
- Step 1: compute mean and variance.
  - $E_\theta[\xi_j]=\theta$, $\text{Var}_\theta(\xi_j)=\theta(1-\theta)$.
  - By linearity, $E_\theta[\hat{\theta}]=\theta$, so $\hat{\theta}$ is unbiased.
  - The variance is
    $$
    \text{Var}_\theta(\hat{\theta})
      = \frac{1}{n^2}\sum_{j=1}^n \text{Var}_\theta(\xi_j)
      = \frac{1}{n^2}\cdot n\theta(1-\theta)
      = \frac{\theta(1-\theta)}{n}.
    $$
- Step 2: risk under squared loss.
  - For squared loss $\rho(t)=t^2$, the risk is
    $$
    R(\hat{\theta},\theta) = E_\theta[(\hat{\theta}-\theta)^2]
      = \text{Var}_\theta(\hat{\theta}) = \frac{\theta(1-\theta)}{n}.
    $$
- Check your intuition.
  - As $n$ grows, the risk (mean squared error) shrinks like $1/n$, so the estimator becomes more accurate.
  - The risk is largest when $\theta=1/2$, where variance is maximized; it is smaller when $\theta$ is near 0 or 1.

### 4.2 Why the sample mean fails for Cauchy but the sample median works
- Setup.
  - Model: $\xi\sim \text{Cauchy}(\theta)$ with pdf
    $$
    p(x;\theta)=\frac{1}{\pi((x-\theta)^2+1)}.
    $$
  - Sample: $\xi_1,\dots,\xi_n$ i.i.d. from this distribution.
- Step 1: sample mean behavior.
  - Any finite average
    $$
    \bar{\xi}_n = \frac{1}{n}\sum_{j=1}^n \xi_j
    $$
    has the same Cauchy($\theta$) distribution as a single observation.
  - Thus, the distribution of $\bar{\xi}_n$ does not become more concentrated as $n$ grows; there is no shrinking variance or improved stability.
- Step 2: median as parameter of interest.
  - The median of the Cauchy($\theta$) distribution is its location parameter $\theta$, since the distribution is symmetric about $\theta$.
  - The sample median (Definition 2.1) is a natural estimator of the median of the distribution.
- Step 3: asymptotic behavior of the median.
  - Theorem 2.2 says that, under mild conditions on the pdf at the median,
    $$
    \sqrt{n}(\text{MAD}-\theta) \xrightarrow{d} N\left(0,\frac{1}{4p_\xi(\theta)^2}\right).
    $$
  - For Cauchy($\theta$), $p_\xi(\theta)=1/\pi$, so the limiting variance is
    $$
    \frac{1}{4p_\xi(\theta)^2} = \frac{1}{4}( \pi^2) = \frac{\pi^2}{4}.
    $$
  - Thus, for large samples, the sample median is approximately normal with mean $\theta$ and variance $\pi^2/(4n)$.
- Check your intuition.
  - Although the sample mean is “as unstable as one observation” in the Cauchy case, the sample median becomes more concentrated around $\theta$ as $n$ grows, and its fluctuation level is governed by a normal law.
  - For heavy-tailed distributions, robust estimators like the median can have better large-sample behavior than the mean.

## 6. Quick recap
- The risk function $R(\hat{\theta},\theta)=E_\theta[\rho(\hat{\theta}-\theta)]$ measures how good an estimator is with respect to a chosen loss; for squared loss and unbiased estimators, risk is the variance.
- UMVU estimators are unbiased estimators that have the smallest variance among all unbiased estimators for every parameter value; examples include the sample mean and unbiased variance in normal models, the sample proportion in Bernoulli, and a scaled maximum in uniform models.
- The Cauchy distribution shows that not all models have finite means or variances; for Cauchy($\theta$), the sample mean has the same Cauchy distribution for all sample sizes and does not stabilize.
- Quantiles and medians provide alternative targets for estimation; the median is the 0.5-quantile and serves as the natural location parameter in Cauchy($\theta$).
- The sample median is defined via the ordered sample and is robust to outliers; it is a natural estimator for a distribution’s median.
- Under general conditions on the pdf at the median, the sample median is asymptotically normal with variance depending on the density at the median, giving a consistent and approximately Gaussian estimator even when the mean may not exist.
- For models with good properties (normal, Bernoulli, uniform), UMVU estimators match familiar statistics; for heavy-tailed models (Cauchy), robust estimators like the median are needed.


[<kbd><br><- Return (ProbStat)<br></kbd>](ProbStat.md)
