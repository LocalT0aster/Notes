# CSE206 — Week 14 Notes — Estimation methods (moments, MLE), hypothesis testing setup (Type I/II, critical regions)
**Lectures:** CSE206_Fa24-14.pdf
**Lab/Tutorial:** week14.pdf

## 1. Big picture (5–10 bullets)
- This week introduces two foundational methods for building estimators: the method of moments and the maximum likelihood method.
- The method of moments matches sample moments (averages of powers) to theoretical moments to solve for parameter estimates.
- Maximum likelihood picks parameter values that make the observed sample most probable under the model.
- The lecture then moves to hypothesis testing: formalizing null and alternative hypotheses, significance level, critical regions, and Type I/II errors.
- Normal-approximation tests (using the central limit theorem) are shown in practice, including choosing a critical value for a given significance level.
- The shifted exponential distribution serves as a running example for both estimation methods and for showing that MMEs and MLEs can differ.
- The lab reinforces computing MMEs and MLEs in specific models and setting up and interpreting hypothesis tests based on binomial and normal models.

## 2. Key concepts and definitions

### 2.1 Method of moments
- Plain-language definition.
  - The method of moments estimates parameters by equating sample moments (computed from the data) to the model’s theoretical moments and solving for the parameters.
- Formal definitions.
  - For a sample \(\xi_1,\dots,\xi_n\), the \(k\)-th sample moment is
    \[
    M_k(\xi_1,\dots,\xi_n) = \frac{1}{n}\sum_{j=1}^n \xi_j^k.
    \]
  - Suppose the distribution \(F(x;\theta_1,\dots,\theta_m)\) has theoretical moments
    \[
    \alpha_k(\theta_1,\dots,\theta_m) = E_\theta[\xi^k],\quad k=1,\dots,m.
    \]
  - The method-of-moments estimators (MMEs) \(\hat{\theta}_1,\dots,\hat{\theta}_m\) are obtained by solving the system
    \[
    \alpha_k(\theta_1,\dots,\theta_m) = M_k(\xi_1,\dots,\xi_n),\quad k=1,\dots,m,
    \]
    for \(\theta_1,\dots,\theta_m\), provided this system has a unique solution and the solutions depend continuously on the sample.
- Asymptotic properties (stated).
  - If the solutions depend continuously/smoothly on the sample, then MMEs are consistent and asymptotically normal:
    \[
    \sqrt{n}(M_k - E\xi^k)\xrightarrow{d} N(0, E\xi^{2k} - (E\xi^k)^2),
    \]
    and this behavior passes through smooth transformations to the MMEs.
- Intuition / mental model.
  - The method of moments plugs sample-based quantities into the population moment formulas and solves backward for the parameters, relying on the law of large numbers to make sample moments close to true moments.

### 2.2 Maximum likelihood method
- Plain-language definition.
  - Maximum likelihood estimation (MLE) chooses parameter values that maximize the likelihood function: the joint probability (or density) of the observed data under the model.
- Formal definitions.
  - Suppose \(\xi\) has pmf/pdf \(p_\xi(x;\theta_1,\dots,\theta_m)\) and \(\xi_1,\dots,\xi_n\) is a sample.
  - The joint pmf/pdf of the sample (since the \(\xi_j\) are independent) is
    \[
    p_{\xi_1,\dots,\xi_n}(x_1,\dots,x_n;\theta_1,\dots,\theta_m)
      = \prod_{j=1}^n p_\xi(x_j;\theta_1,\dots,\theta_m).
    \]
  - For fixed observed values \(x_1,\dots,x_n\), the likelihood function is
    \[
    L_{x_1,\dots,x_n}(\theta_1,\dots,\theta_m)
      = \prod_{j=1}^n p_\xi(x_j;\theta_1,\dots,\theta_m).
    \]
  - The maximum likelihood estimator (MLE) \(\hat{\theta} = (\hat{\theta}_1,\dots,\hat{\theta}_m)\) is the parameter value where this function attains its maximum.
  - In practice, one often maximizes the log-likelihood
    \[
    \ell(\theta_1,\dots,\theta_m) = \ln L_{x_1,\dots,x_n}(\theta_1,\dots,\theta_m),
    \]
    since the logarithm is increasing and simplifies products into sums.
- Intuition / mental model.
  - MLEs choose parameters that make what we actually observed as likely as possible under the model, often leading to intuitive estimators like sample proportions and sample means.

### 2.3 Hypothesis testing fundamentals
- Plain-language definitions.
  - Hypothesis testing uses data to decide between a null hypothesis \(H_0\) (e.g., “parameter equals a specified value”) and an alternative hypothesis \(H_1\) (e.g., “parameter differs from that value”).
  - The decision rule uses a test statistic (function of the sample) and a critical region where we reject \(H_0\).
  - The significance level \(\alpha\) controls the maximum probability of rejecting \(H_0\) when it is in fact true (Type I error).
- Formal setup (section 2.1).
  - The parameter space \(\Theta\) is partitioned into two disjoint sets:
    \[
    H_0:\theta\in\Theta_0,\quad H_1:\theta\in\Theta_1,
    \]
    with \(\Theta_0\cup\Theta_1=\Theta\) and \(\Theta_0\cap\Theta_1=\emptyset\).
  - Let \(t(\xi_1,\dots,\xi_n)\) be a statistic used as test statistic.
  - A test procedure partitions possible values of \(t\) (and hence \(\Omega\)) into an acceptance region \(R_0\) and a rejection region \(R_1\):
    - If \(t\in R_0\): do not reject \(H_0\).
    - If \(t\in R_1\): reject \(H_0\).
- Type I and Type II errors.
  - Type I error: rejecting \(H_0\) when \(H_0\) is actually true (\(\theta\in\Theta_0\)).
  - Type II error: failing to reject \(H_0\) when \(H_1\) is true (\(\theta\in\Theta_1\)).
- Significance level condition.
  - The test is designed so that the probability of Type I error is controlled:
    \[
    \alpha \ge \sup_{\theta\in\Theta_0}P_\theta(t\in R_1).
    \]
  - In many standard tests, \(\alpha\) is chosen (e.g., 0.05) and the critical region \(R_1\) is built so that the supremum equals \(\alpha\).
- Critical value.
  - In one-sided tests with monotone statistics, the rejection region is often of the form \(R_1=[t_\alpha,\infty)\), and the critical value \(t_\alpha\) satisfies
    \[
    P_\theta(t\ge t_\alpha)\le \alpha\quad\text{for every }\theta\in\Theta_0.
    \]
- Intuition / mental model.
  - Hypothesis testing is about balancing the risk of declaring a difference when none exists (Type I) against the risk of missing a real difference (Type II).
  - The significance level tells you how often you are willing to tolerate false alarms if the null hypothesis were true.

### 2.4 Example: normal test for a mean with known variance
- Model (Example 2.1).
  - \(\xi\sim N(\theta,\sigma^2)\) with known variance \(\sigma^2\). Sample \(\xi_1,\dots,\xi_n\).
  - Test \(H_0:\theta=\theta_0\) against \(H_1:\theta>\theta_0\).
  - Test statistic:
    \[
    t(\xi_1,\dots,\xi_n) = \bar{\xi}_n = \frac{1}{n}\sum_{j=1}^n \xi_j.
    \]
- Critical value.
  - Under \(H_0\), \(\bar{\xi}_n\sim N(\theta_0,\sigma^2/n)\).
  - Standardize:
    \[
    Z = \frac{\sqrt{n}(\bar{\xi}_n-\theta_0)}{\sigma}\sim N(0,1).
    \]
  - For a significance level \(\alpha\), choose \(z_{1-\alpha}\) so that \(P(Z\ge z_{1-\alpha})=\alpha\).
  - Corresponding critical value:
    \[
    t_\alpha = \theta_0 + z_{1-\alpha}\frac{\sigma}{\sqrt{n}}.
    \]
- Decision rule.
  - Reject \(H_0\) if \(\bar{\xi}_n\ge t_\alpha\).
  - Under \(H_0\), \(P(\bar{\xi}_n\ge t_\alpha)=\alpha\), so the test has Type I error probability \(\alpha\).
- Intuition / mental model.
  - If the observed sample mean is much larger than what we expect under \(H_0\) (in units of standard error), this counts as evidence against \(H_0\).

## 3. Core formulas and how to use them

### 3.1 Method of moments estimator (shifted exponential example)
- Model (from Example 1.1).
  - Shifted exponential distribution with pdf
    \[
    p_\xi(x;\theta) = e^{-(x-\theta)}I(x\ge \theta),
    \]
    \(\theta>0\) unknown. Sample: \(\xi_1,\dots,\xi_n\).
- First moment.
  - The model’s mean is \(\alpha_1(\theta)=E_\theta[\xi] = 1+\theta\).
  - The first sample moment is
    \[
    M_1(\xi_1,\dots,\xi_n) = \frac{1}{n}\sum_{j=1}^n \xi_j = \bar{\xi}_n.
    \]
- Method-of-moments step.
  - Set
    \[
    \alpha_1(\theta) = M_1 \quad\Rightarrow\quad 1+\theta = \bar{\xi}_n.
    \]
  - Solve for \(\theta\):
    \[
    \hat{\theta}_{\text{MM}} = \bar{\xi}_n - 1 = \frac{S_n}{n}-1,
    \]
    where \(S_n=\sum_{j=1}^n\xi_j\).
- When to use it.
  - When the first moment exists and is simple, the method of moments often gives a quick estimator.
  - This estimator is consistent by law of large numbers as long as the first moment exists.

### 3.2 Maximum likelihood estimator (Bernoulli example)
- Model (Example 1.2).
  - \(\xi_1,\dots,\xi_n\sim \text{Bernoulli}(\theta)\) i.i.d., with pmf
    \[
    p_\xi(x;\theta) = \theta^x(1-\theta)^{1-x},\quad x\in\{0,1\}.
    \]
  - Let \(s_n=\sum_{j=1}^n x_j\) be the number of successes (ones) in the observed sample.
- Likelihood and log-likelihood.
  - Likelihood:
    \[
    L(\theta) = \prod_{j=1}^n p_\xi(x_j;\theta) = \theta^{s_n}(1-\theta)^{n-s_n}.
    \]
  - Log-likelihood:
    \[
    \ell(\theta) = \ln L(\theta) = s_n\ln\theta + (n-s_n)\ln(1-\theta).
    \]
- Maximization.
  - Differentiate with respect to \(\theta\):
    \[
    \frac{d\ell}{d\theta} = \frac{s_n}{\theta} - \frac{n-s_n}{1-\theta}.
    \]
  - Set derivative to zero:
    \[
    \frac{s_n}{\theta} = \frac{n-s_n}{1-\theta}
    \quad\Rightarrow\quad
    s_n(1-\theta) = \theta(n-s_n).
    \]
  - Solve for \(\theta\):
    \[
    s_n = n\theta \quad\Rightarrow\quad \hat{\theta}_{\text{ML}} = \frac{s_n}{n}.
    \]
- When to use it.
  - Any Bernoulli or binomial situation: the MLE for the success probability is the sample proportion.
  - This matches intuition and is also the MME from matching the first moment.

### 3.3 Normal mean test critical value
- Formula (from Example 2.1).
  - For testing \(H_0:\theta=\theta_0\) vs \(H_1:\theta>\theta_0\) using \(\bar{\xi}_n\) and significance level \(\alpha\):
    \[
    t_\alpha = \theta_0 + z_{1-\alpha}\frac{\sigma}{\sqrt{n}}.
    \]
- Symbols.
  - \(t_\alpha\): critical value for \(\bar{\xi}_n\).
  - \(\theta_0\): null hypothesis mean.
  - \(\sigma\): known standard deviation.
  - \(z_{1-\alpha}\): standard normal quantile with right-tail probability \(\alpha\).
- When to use it.
  - When designing a one-sided normal-approximation test for the mean with known variance.

## 4. Worked examples

### 4.1 Method of moments vs MLE for a shifted exponential
- Setup.
  - Model: shifted exponential with pdf
    \[
    p_\xi(x;\theta)=e^{-(x-\theta)}I(x\ge \theta).
    \]
  - Sample: \(\xi_1,\dots,\xi_n\). Let \(m=\min\{\xi_1,\dots,\xi_n\}\) and \(S_n=\sum_{j=1}^n\xi_j\).
- Step 1: method-of-moments estimator (MME).
  - Theoretical mean: \(\alpha_1(\theta)=1+\theta\).
  - Sample mean: \(\bar{\xi}_n=S_n/n\).
  - Equate: \(1+\theta=\bar{\xi}_n\Rightarrow\hat{\theta}_{\text{MM}}=\bar{\xi}_n-1\).
- Step 2: maximum likelihood estimator (MLE) (from tutorial Example 2.2).
  - The joint density:
    \[
    L(\theta) = \prod_{j=1}^n e^{-(x_j-\theta)} I(x_j\ge \theta)
             = e^{-(x_1+\dots+x_n)}e^{n\theta} I(\min x_j\ge \theta).
    \]
  - For fixed data, \(L(\theta)\) is zero if \(\theta>m\), and proportional to \(e^{n\theta}\) for \(\theta\le m\).
  - Since \(e^{n\theta}\) is increasing in \(\theta\), the maximum occurs at the largest \(\theta\) permitted by the indicator, namely \(\theta=m\).
  - So
    \[
    \hat{\theta}_{\text{ML}} = m = \min\{\xi_1,\dots,\xi_n\}.
    \]
- Step 3: compare the estimators.
  - MME: \(\bar{\xi}_n-1\).
  - MLE: \(m\).
  - They differ in finite samples, even though both aim to estimate the same parameter \(\theta\).
- Check your intuition.
  - In this model, the shift parameter \(\theta\) is the lower bound of the support; the minimum is naturally tied to that boundary and becomes the MLE.
  - The method-of-moments estimator relies on the mean, which is also affected by the exponential tail; both approaches use different features of the distribution.

### 4.2 Hypothesis test for normal mean with known variance
- Setup (simplified from Example 2.1).
  - \(\xi_1,\dots,\xi_n\sim N(\theta,\sigma^2)\); \(\sigma^2\) known.
  - We want to test \(H_0:\theta=\theta_0\) vs \(H_1:\theta>\theta_0\) with significance \(\alpha\).
  - Test statistic: \(\bar{\xi}_n\).
- Step 1: distribution under \(H_0\).
  - Under \(H_0\), \(\bar{\xi}_n\sim N(\theta_0,\sigma^2/n)\).
  - Standardize:
    \[
    Z = \frac{\sqrt{n}(\bar{\xi}_n-\theta_0)}{\sigma}\sim N(0,1).
    \]
- Step 2: choose critical value.
  - We need \(t_\alpha\) such that
    \[
    P_{H_0}(\bar{\xi}_n\ge t_\alpha) = \alpha.
    \]
  - In terms of \(Z\):
    \[
    \alpha = P(Z\ge z_{1-\alpha})\quad\Rightarrow\quad t_\alpha=\theta_0 + z_{1-\alpha}\frac{\sigma}{\sqrt{n}}.
    \]
- Step 3: decision rule.
  - If the realized sample mean \(\bar{x}_n\ge t_\alpha\), reject \(H_0\); otherwise, do not reject.
- Check your intuition.
  - A very large observed mean compared to what \(H_0\) predicts (in standard error units) is rare under \(H_0\) and thus counts as evidence for \(H_1\).
  - The choice of \(\alpha\) controls how “rare” is considered rare enough to reject.

## 5. Lab/Tutorial essentials (week14.pdf)

### 5.1 What the lab asked you to do
- Problems 1–3: method of moments, MLE, and bias in simple models.
  - Problem 1: Given a sample \(12, 11.2, 13.5, 12.3, 13.8, 11.9\) from a distribution with density
    \[
    f(x;\theta)=\frac{\theta}{1+\theta}\frac{1}{x^{1+\theta}},\quad x>1,
    \]
    find the maximum likelihood estimate of \(\theta\).
  - Problem 2: For a binomial random variable \(X\), show that \(\hat{P}=X/n\) is an unbiased estimator of \(p\), whereas
    \[
    \hat{P}=\frac{X+\sqrt{n}/2}{n+\sqrt{n}}
    \]
    is biased.
  - Problem 3: For \(n\) Bernoulli trials with parameter \(p\), derive the MLE for \(p\) (sample proportion).
- Problems 4–8: framing hypotheses and locating critical regions.
  - Problem 4: For a claim about average fat content not exceeding 1.5 g per serving, write \(H_0,H_1\) and decide whether the critical region is on the upper tail.
  - Problem 5: For a claim that 60% of new residences are 3-bedroom homes, state \(H_0,H_1\) for a sample-based test and identify whether rejection should be for large or small observed proportions.
  - Problem 6: For a claim that at least 30% of the public is allergic, explain what Type I and Type II errors mean in this context.
  - Problem 7: For a binomial test of \(p=0.6\) with \(n=10\) and critical region \(\{X\le 3\}\), compute Type I and Type II error probabilities for various true \(p\).
  - Problem 8: Repeat the previous problem with \(n=50\) and a normal approximation, critical region \(X\le 24\).
- Problems 9–10: normal-approximation tests for means.
  - Problem 9: With sample mean 71.8 years from 100 recorded deaths and known \(\sigma=8.9\), test whether mean life span exceeds 70 years at \(\alpha=0.05\).
  - Problem 10: With sample mean 7.8 kg and known \(\sigma=0.5\) for breaking strength, test \(H_0:\mu=8\) vs \(H_1:\mu\ne 8\) at \(\alpha=0.01\).

### 5.2 How to solve / approach them
- MLE problems (1 and 3).
  - Write down the likelihood \(L(\theta)\) as a product of densities or pmfs.
  - Take logarithms to get a sum; differentiate w.r.t. \(\theta\) or \(p\).
  - Solve the first-order condition \(d\ell/d\theta=0\) (or \(d\ell/dp=0\)) and check that it yields a maximum within the allowed parameter range.
- Unbiased vs biased estimator (Problem 2).
  - Compute \(E[\hat{P}]\) explicitly using the binomial pmf; for \(\hat{P}=X/n\) show \(E[\hat{P}]=p\).
  - For the second \(\hat{P}\), compute \(E[\hat{P}]\) and show it is not equal to \(p\) in general.
- Hypothesis formulation and critical regions (Problems 4–6).
  - Identify what parameter value corresponds to “no effect” or “company’s claim” and use it as \(H_0\).
  - Decide whether the alternative is one-sided (e.g., “greater than”) or two-sided (e.g., “different from”).
  - Decide from context whether unusually large or small values of the test statistic provide evidence against \(H_0\), and place the critical region accordingly.
  - For Type I/II errors, give verbal descriptions in terms of the real-world context.
- Type I/II probabilities (Problems 7–8).
  - For small \(n\), use binomial probabilities directly:
    \[
    P(\text{Type I}) = P(X\le 3|p=0.6).
    \]
  - For Type II errors, compute \(P(X>3|p=0.3),P(X>3|p=0.4),P(X>3|p=0.5)\).
  - For larger \(n\) (e.g., 50), use normal approximation to the binomial:
    \[
    X\approx N(np,np(1-p))
    \]
    and standardize to use normal cdfs.
- Normal-mean tests (Problems 9–10).
  - Use the test design from Example 2.1: compute
    \[
    Z = \frac{\bar{x}-\mu_0}{\sigma/\sqrt{n}}
    \]
    and compare to appropriate critical values \(z_{1-\alpha}\) (one-sided) or \(z_{1-\alpha/2}\) (two-sided).
  - Translate the result back into context: does the evidence support the manufacturer’s or agent’s claim at the chosen significance level?

### 5.3 Mini practice
- Practice 1: MLE in Bernoulli model.
  - Question: If \(X_1,\dots,X_n\) are i.i.d. Bernoulli with parameter \(p\), what is the MLE of \(p\)?
  - Brief answer: \(\hat{p}_{\text{ML}} = \frac{1}{n}\sum_{j=1}^n X_j\) (the sample proportion).
- Practice 2: formulating hypotheses.
  - Question: A company claims the mean breaking strength of its product is at least 8 kg. What are \(H_0\) and \(H_1\)?
  - Brief answer: Usually \(H_0:\mu=8\) (or \(\mu\ge 8\)) vs \(H_1:\mu<8\) if we are testing for a drop below 8.
- Practice 3: identifying Type I/II errors.
  - Question: In testing \(H_0:p=0.6\) vs \(H_1:p<0.6\) for late orders, what are Type I and Type II errors?
  - Brief answer: Type I error: reject \(H_0\) (conclude \(p<0.6\)) when in fact \(p=0.6\). Type II error: fail to reject \(H_0\) (keep \(p=0.6\)) when in fact \(p<0.6\).

## 6. Quick recap
- The method of moments estimates parameters by equating sample moments to theoretical moments and solving for the parameters; MMEs are typically consistent and asymptotically normal when moments and mappings behave well.
- Maximum likelihood chooses parameter values maximizing the likelihood of the observed data; in many standard models (Bernoulli, normal, exponential) MLEs coincide with intuitive estimators like proportions, means, or minima.
- MMEs and MLEs may differ, as seen in the shifted exponential model where \(\bar{x}-1\) (MME) and \(\min\{x_j\}\) (MLE) give different estimates for the same parameter.
- Hypothesis testing formalizes decisions about parameters via null/alternative hypotheses, test statistics, and critical regions, guided by the significance level \(\alpha\) which controls Type I error probability.
- Type I errors (false positives) occur when rejecting a true \(H_0\); Type II errors (false negatives) occur when failing to reject a false \(H_0\); the balance between them depends on the critical region and sample size.
- For normal data with known variance, tests on the mean use standardized sample means and normal quantiles, paralleling confidence interval constructions.
- The week 14 lab reinforces computation of MMEs/MLEs and practice in setting up and interpreting hypothesis tests for binomial and normal models, including Type I/II error probabilities and normal approximations.


[<kbd><br><- Return (ProbStat)<br></kbd>](ProbStat.md)
