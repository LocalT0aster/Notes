# CSE206 — Week 12 Notes — Estimation intro (statistics, confidence intervals, point estimators, unbiasedness)
**Lectures:** CSE206_Fa24-12.pdf
**Lab/Tutorial:** week12.pdf

## 1. Big picture (5–10 bullets)
- This week starts the transition from probability to statistics, focusing on how to estimate unknown parameters from data.
- The main objects are statistics: functions of a sample used to learn about parameters like means, variances, and distribution limits.
- Confidence intervals are introduced as random intervals that contain the true parameter with a prescribed probability (confidence level).
- Specific confidence interval constructions are given for: a shift parameter in an exponential-type model, the mean of a normal distribution with known variance, and the variance of a normal distribution with known mean.
- Asymptotic confidence intervals are discussed: intervals built using the central limit theorem when exact distributions are messy.
- Point estimation is introduced: producing a single “best guess” for a parameter using an estimator (a statistic).
- Unbiasedness is defined as a key property of estimators: on average, the estimator equals the true parameter. Examples show both unbiased and biased estimators.
- The lab applies these ideas to measurement data: computing confidence intervals, unbiased estimates of variance and standard deviation, and interpreting sample means via CLT.

## 2. Key concepts and definitions

### 2.1 Statistics and parameter space
- Plain-language definition.
  - A statistic is any function of the sample data; it is itself a random variable.
  - Parameters are the unknown numerical characteristics of the distribution (for example, mean, variance, or a probability).
- Formal definition (statistic).
  - If \(\xi_1,\dots,\xi_n\) is a sample of a random variable \(\xi\), any measurable function
    \[
    T(\xi_1,\dots,\xi_n)
    \]
    is called a statistic.
- Parameter space.
  - Given a family of distributions \(\{F_\theta : \theta\in\Theta\}\), the set \(\Theta\) of all possible parameter values is the parameter space.
  - Examples:
    - Normal with mean 0, unknown variance \(\sigma^2\): \(\theta=\sigma^2\), \(\Theta=(0,\infty)\).
    - Normal with variance 1, unknown mean \(\mu\): \(\theta=\mu\), \(\Theta=\mathbb{R}\).
    - Binomial \(\text{Bin}(10,p)\): \(\theta=p\), \(\Theta=(0,1)\).
- Intuition / mental model.
  - Statistics summarize samples; parameters describe the underlying distribution we do not know. Estimation theory builds statistics that tell us something about parameters.

### 2.2 Confidence intervals: general idea
- Plain-language definition.
  - A confidence interval is a random interval (its endpoints depend on the sample) that is constructed so that it contains the true parameter with a chosen probability (confidence level).
  - It does not guarantee that a specific realized interval contains the parameter; instead, it guarantees that the procedure has the stated long-run success rate.
- Formal definition (Definition 1.2).
  - Let \(\theta\) be a parameter with space \(\Theta\). Let \(\hat{\theta}_1(\xi_1,\dots,\xi_n)\) and \(\hat{\theta}_2(\xi_1,\dots,\xi_n)\) be two statistics, and let \(0<\alpha<1\).
  - They form a confidence interval for \(\theta\) with confidence coefficient (level) \(1-\alpha\) if, for all \(\theta\in\Theta\):
    \[
    P\big(\hat{\theta}_1(\xi_1,\dots,\xi_n) < \theta < \hat{\theta}_2(\xi_1,\dots,\xi_n)\big) \ge 1-\alpha.
    \]
- Intuition / mental model.
  - Over many repeated samples, at least a fraction \(1-\alpha\) of the intervals constructed by this rule will contain the true parameter.

### 2.3 Example: confidence interval for a shift parameter using the minimum
- Model (Example 1.3).
  - The pdf is
    \[
    p_\xi(x;\theta) = e^{-(x-\theta)} I(x\ge\theta),
    \]
    where \(\theta>0\) is an unknown shift parameter.
  - This is an exponential-type distribution shifted by \(\theta\).
  - Let \(\xi_1,\dots,\xi_n\) be an i.i.d. sample from this distribution.
- Statistic used.
  - Let
    \[
    m = \min\{\xi_1,\dots,\xi_n\}.
    \]
  - Since \(\theta\) is below all observed values, we must have \(\theta<m\), so \(m\) is a natural upper endpoint for a confidence interval.
- Confidence interval endpoints.
  - We set the upper endpoint as \(\hat{\theta}_2 = m\).
  - We look for a constant \(c_\alpha>0\) and define the lower endpoint as \(\hat{\theta}_1 = m - c_\alpha\) so that
    \[
    P(m - c_\alpha < \theta < m) = 1-\alpha
    \]
    for all \(\theta>0\). This is equivalent to
    \[
    P(m - \theta \ge c_\alpha) = \alpha.
    \]
- Intuition / mental model.
  - All sample values lie above \(\theta\). The smallest observation \(m\) is random but tends to be close to \(\theta\) if \(n\) is large; subtracting \(c_\alpha\) pushes the lower bound further down to guarantee the desired coverage.

### 2.4 Confidence intervals for normal models

#### 2.4.1 Mean with known variance
- Model.
  - The sample \(\xi_1,\dots,\xi_n\) comes from a normal distribution \(N(\theta,\sigma^2)\), where the variance \(\sigma^2\) is known and the mean \(\theta\) is unknown.
  - The sample mean is
    \[
    \bar{\xi}_n = \frac{1}{n}\sum_{j=1}^n \xi_j.
    \]
  - We know that \(\bar{\xi}_n\sim N(\theta,\sigma^2/n)\).
- Standard normal and quantiles.
  - Let \(\Phi\) be the cdf of a standard normal \(N(0,1)\). For each \(\alpha\in(0,1)\), the quantile \(z_\alpha\) is defined by
    \[
    \Phi(z_\alpha) = \alpha.
    \]
  - Interpret graphically: \(z_{1-\alpha/2}\) is the point so that the area under the standard normal to the left of it is \(1-\alpha/2\).
- Confidence interval.
  - Because
    \[
    \frac{\sqrt{n}(\bar{\xi}_n-\theta)}{\sigma}\sim N(0,1),
    \]
    we have
    \[
    P\left(z_{\alpha/2} \le \frac{\sqrt{n}(\bar{\xi}_n-\theta)}{\sigma} \le z_{1-\alpha/2}\right) = 1-\alpha.
    \]
  - Rearranging for \(\theta\) yields endpoints
    \[
    \hat{\theta}_1 = \bar{\xi}_n - \frac{\sigma z_{1-\alpha/2}}{\sqrt{n}},\quad
    \hat{\theta}_2 = \bar{\xi}_n - \frac{\sigma z_{\alpha/2}}{\sqrt{n}}.
    \]
  - Using symmetry of the normal density, \(z_{\alpha/2}=-z_{1-\alpha/2}\), this becomes the familiar symmetric interval
    \[
    \bar{\xi}_n \pm z_{1-\alpha/2}\frac{\sigma}{\sqrt{n}}.
    \]
- Intuition / mental model.
  - This interval is “centered” at the sample mean, and its half-width shrinks as \(1/\sqrt{n}\).
  - The factor \(z_{1-\alpha/2}\) controls the desired coverage probability: for 95% confidence, use about 1.96; for 99%, use about 2.58.

#### 2.4.2 Variance with known mean (chi-squared)
- Model.
  - Now assume \(\xi_1,\dots,\xi_n\sim N(\mu,\theta^2)\), where the mean \(\mu\) is known but the variance \(\theta^2\) is unknown.
  - Consider
    \[
    V_n = \sum_{j=1}^n (\xi_j-\mu)^2.
    \]
- Connection to chi-squared.
  - Each \((\xi_j-\mu)/\theta\) is standard normal \(N(0,1)\).
  - The sum of squares of \(n\) independent standard normals has a chi-squared distribution with \(n\) degrees of freedom, written \(\chi^2(n)\).
  - Therefore,
    \[
    \frac{V_n}{\theta^2} \sim \chi^2(n).
    \]
- Quantiles and confidence interval.
  - Let \(w_\alpha\) denote the \(\alpha\)-quantile of \(\chi^2(n)\): \(P(\chi^2(n)\le w_\alpha)=\alpha\).
  - Fix \(\alpha\in(0,1)\) and define
    \[
    \hat{\theta}_1 = \sqrt{\frac{V_n}{w_{1-\alpha/2}}},\quad
    \hat{\theta}_2 = \sqrt{\frac{V_n}{w_{\alpha/2}}}.
    \]
  - Then
    \[
    P(\hat{\theta}_1<\theta<\hat{\theta}_2) = 1-\alpha.
    \]
- Intuition / mental model.
  - We build a confidence interval for the standard deviation \(\theta\) by inverting the chi-squared distribution of the scaled sum of squared deviations from the known mean.

### 2.5 Asymptotic confidence intervals
- Setup.
  - For many distributions, exact finite-sample confidence intervals are difficult to derive. Instead, we can use the central limit theorem to build approximate (asymptotic) intervals.
  - A common model in measurement is
    \[
    \xi_j = \theta + \varepsilon_j,
    \]
    where \(\varepsilon_j\) are i.i.d. with mean 0 and variance \(\sigma^2\).
- CLT-based interval.
  - By CLT,
    \[
    \frac{S_n-n\theta}{\sigma\sqrt{n}} \xrightarrow{d} N(0,1),
    \]
    so for large \(n\) we have approximately
    \[
    P\left(\theta\in \left(\bar{\xi}_n - z_{1-\alpha/2}\frac{\sigma}{\sqrt{n}}, \bar{\xi}_n + z_{1-\alpha/2}\frac{\sigma}{\sqrt{n}}\right)\right)\approx 1-\alpha.
    \]
  - The endpoints here depend on \(n\) and become more accurate as \(n\to\infty\).
- Intuition / mental model.
  - Asymptotic intervals are approximate but practical, especially when sample sizes are large and we are comfortable with CLT approximations.

### 2.6 Point estimation and unbiasedness
- Point estimation.
  - A point estimator is a statistic used as a single-number “best guess” for a parameter (or a function of a parameter) given the sample.
  - Examples: sample mean for the population mean; maximum, or scaled mean, for the upper limit in a uniform model.
- Unbiased estimator (Definition 1.6).
  - An estimator \(\hat{\theta}(\xi_1,\dots,\xi_n)\) is unbiased if
    \[
    E\big[\hat{\theta}(\xi_1,\dots,\xi_n)\big] = \theta
    \]
    for all \(\theta\in\Theta\).
  - The bias is defined as \(E\hat{\theta}-\theta\). Unbiased means bias = 0.
- Example (1.7): estimating mean lifetime in an exponential model.
  - Suppose \(\xi_1,\dots,\xi_n\) are lifetimes with cdf \(F(x;\theta) = 1-e^{-\theta x}\).
  - The mean lifetime is
    \[
    \phi(\theta) = E\xi_1 = \frac{1}{\theta}.
    \]
  - The sample mean
    \[
    \bar{\xi}_n = \frac{1}{n}\sum_{j=1}^n \xi_j
    \]
    is an unbiased estimator of \(\phi(\theta)\), since \(E\bar{\xi}_n = \phi(\theta)\).
  - However, the statistic \(n/S_n = 1/\bar{\xi}_n\) is not an unbiased estimator of \(\theta\), because the function \(t\mapsto 1/t\) is strictly concave and Jensen’s inequality shows \(E(1/\bar{\xi}_n) > 1/E\bar{\xi}_n = \theta\).
- Example (1.8): when an unbiased estimator may not exist.
  - For a single Bernoulli\((\theta)\) observation with \(0<\theta<1\), no unbiased estimator exists for \(1/\theta\).
  - The unbiasedness condition
    \[
    \frac{1}{\theta} = E\hat{\phi}(\theta) = \hat{\phi}(\theta)(0)(1-\theta)+\hat{\phi}(\theta)(1)\theta
    \]
    cannot hold for all \(\theta\in(0,1)\) because the left-hand side becomes arbitrarily large as \(\theta\to 0\), while the right-hand side stays finite.
- Intuition / mental model.
  - Unbiasedness is desirable but not always possible; in some cases, there is no unbiased estimator for the parameter or function of interest.

## 3. Core formulas and how to use them

### 3.1 Confidence interval for the exponential-shift parameter (Example 1.3)
- Model.
  - pdf: \(p_\xi(x;\theta)=e^{-(x-\theta)}I(x\ge\theta)\). Sample: \(\xi_1,\dots,\xi_n\). Let \(m=\min\{\xi_1,\dots,\xi_n\}\).
- Key probability calculation.
  - The event \(m\ge \theta+c\) means every \(\xi_j\ge \theta+c\).
  - Since shifts preserve exponential form,
    \[
    P(\xi_j\ge \theta+c) = e^{-c},\quad P(m\ge \theta+c) = e^{-nc}.
    \]
  - We choose \(c_\alpha\) to satisfy
    \[
    P(m-\theta\ge c_\alpha)=\alpha \quad\Rightarrow\quad e^{-nc_\alpha}=\alpha,
    \]
    so
    \[
    c_\alpha = -\frac{1}{n}\ln \alpha.
    \]
- Interval.
  - Take
    \[
    \hat{\theta}_2 = m,\quad \hat{\theta}_1 = m-c_\alpha = m+\frac{1}{n}\ln\alpha.
    \]
  - Then
    \[
    P(\hat{\theta}_1 < \theta < \hat{\theta}_2) = 1-\alpha.
    \]
- When to use it.
  - When you have a lower-bounded exponential-type distribution where the parameter is a shift; the minimum of the sample is a natural statistic.

### 3.2 Confidence interval for normal mean with known variance
- Model.
  - \(\xi_1,\dots,\xi_n\sim N(\theta,\sigma^2)\) i.i.d., \(\sigma^2\) known.
- Interval.
  - For confidence level \(1-\alpha\):
    \[
    \theta\in\left(\bar{\xi}_n - z_{1-\alpha/2}\frac{\sigma}{\sqrt{n}},\;\bar{\xi}_n + z_{1-\alpha/2}\frac{\sigma}{\sqrt{n}}\right),
    \]
    where \(z_{1-\alpha/2}\) is the quantile of the standard normal cdf \(\Phi\).
- Symbols.
  - \(\bar{\xi}_n\): sample mean.
  - \(\sigma\): known standard deviation.
  - \(n\): sample size.
  - \(\alpha\): desired error probability, e.g. 0.05 for 95% confidence.
- When to use it.
  - In measurement problems where the instrument variance is known from calibration and you want a confidence interval for the true mean.

### 3.3 Confidence interval for normal variance with known mean
- Model.
  - \(\xi_1,\dots,\xi_n\sim N(\mu,\theta^2)\) i.i.d., \(\mu\) known, \(\theta^2\) unknown.
  - Sum of squares: \(V_n=\sum_{j=1}^n (\xi_j-\mu)^2\).
- Interval.
  - Since \(V_n/\theta^2\sim\chi^2(n)\), the confidence interval for \(\theta\) at level \(1-\alpha\) is
    \[
    \theta\in\left(\sqrt{\frac{V_n}{w_{1-\alpha/2}}},\;\sqrt{\frac{V_n}{w_{\alpha/2}}}\right),
    \]
    where \(w_{\alpha}\) are chi-squared quantiles.
- When to use it.
  - When the mean is known (or effectively fixed) and you are evaluating the precision (variance) of a measurement device or process.

## 4. Worked examples

### 4.1 Confidence interval for a shift parameter via the minimum
- Setup.
  - Sample \(\xi_1,\dots,\xi_n\) from the distribution with pdf \(p_\xi(x;\theta)=e^{-(x-\theta)}I(x\ge\theta)\).
  - Parameter \(\theta>0\) is unknown. Let \(m=\min\{\xi_1,\dots,\xi_n\}\).
- Step 1: understand how \(m\) behaves.
  - Because \(x\ge\theta\), the minimum is always at least \(\theta\).
  - The event \(m\ge \theta+c\) occurs if and only if all observations satisfy \(\xi_j\ge \theta+c\).
  - For each \(j\),
    \[
    P(\xi_j\ge \theta+c) = e^{-c};
    \]
    then, using independence,
    \[
    P(m\ge\theta+c) = e^{-nc}.
    \]
- Step 2: choose \(c_\alpha\) for a given confidence level.
  - We want a lower endpoint \(\hat{\theta}_1 = m - c_\alpha\) so that
    \[
    P(\hat{\theta}_1 < \theta < m) = 1-\alpha.
    \]
  - This is equivalent to
    \[
    P(m-\theta \ge c_\alpha) = \alpha.
    \]
  - Using the formula above:
    \[
    P(m-\theta \ge c_\alpha) = e^{-nc_\alpha} = \alpha
    \quad\Rightarrow\quad
    c_\alpha = -\frac{1}{n}\ln\alpha.
    \]
- Step 3: write the interval.
  - A confidence interval with coefficient \(1-\alpha\) is
    \[
    \left(m + \frac{1}{n}\ln\alpha,\; m\right).
    \]
- Check your intuition.
  - As \(n\) grows, the minimum \(m\) tends to move closer to the true \(\theta\), and the width of the interval shrinks (\(c_\alpha\propto 1/n\)).
  - The interval is one-sided: the upper endpoint is the smallest observed value; the lower endpoint is lower than this by a small amount chosen to ensure coverage.

### 4.2 Confidence interval for a normal mean with known variance
- Setup.
  - \(\xi_1,\dots,\xi_n\sim N(\theta,\sigma^2)\); \(\sigma^2\) is known, \(\theta\) unknown.
  - Sample mean \(\bar{\xi}_n\) is observed from one sample.
- Step 1: standardize the sample mean.
  - We know \(\bar{\xi}_n\sim N(\theta,\sigma^2/n)\).
  - The standardized variable
    \[
    Z = \frac{\sqrt{n}(\bar{\xi}_n-\theta)}{\sigma}
    \]
    has distribution \(N(0,1)\).
- Step 2: form a central probability statement.
  - For \(0<\alpha<1\), pick quantiles \(z_{\alpha/2},z_{1-\alpha/2}\) of the standard normal so that
    \[
    P(z_{\alpha/2}\le Z\le z_{1-\alpha/2}) = 1-\alpha.
    \]
  - Substitute \(Z\):
    \[
    P\left(z_{\alpha/2}\le \frac{\sqrt{n}(\bar{\xi}_n-\theta)}{\sigma}\le z_{1-\alpha/2}\right) = 1-\alpha.
    \]
- Step 3: solve for \(\theta\).
  - Multiply through and rearrange:
    \[
    P\left(\bar{\xi}_n - \frac{\sigma z_{1-\alpha/2}}{\sqrt{n}}\le \theta\le \bar{\xi}_n - \frac{\sigma z_{\alpha/2}}{\sqrt{n}}\right) = 1-\alpha.
    \]
  - Using symmetry \(z_{\alpha/2}=-z_{1-\alpha/2}\), this becomes
    \[
    P\left(\bar{\xi}_n - z_{1-\alpha/2}\frac{\sigma}{\sqrt{n}}\le \theta\le \bar{\xi}_n + z_{1-\alpha/2}\frac{\sigma}{\sqrt{n}}\right) = 1-\alpha.
    \]
- Check your intuition.
  - The more measurements you collect (larger \(n\)), the narrower the interval becomes because the uncertainty of \(\bar{\xi}_n\) shrinks like \(1/\sqrt{n}\).
  - The z-quantile controls how conservative you are: 99% confidence requires a larger z-value and produces a wider interval than 95%.

## 5. Lab/Tutorial essentials (week12.pdf)

### 5.1 What the lab asked you to do
- Problem 1 (Sveshnikov 36.1): 99% confidence interval for a mean with known variance.
  - A constant is measured 25 times with normal errors of known standard deviation \(\sigma=10\) m and sample mean \(\bar{x}=100\) m.
  - Construct a 99% confidence interval for the true constant value.
- Problem 2 (Sveshnikov 36.2): grouped measurements and 95% confidence interval.
  - A table gives group means and sizes for 5 groups of measurements.
  - Treating all observations as independent normal errors, estimate the measured value (overall mean) and construct a 95% confidence interval.
- Problem 3 (Sveshnikov 35.1): unbiased estimate of standard deviation.
  - 12 measurements of a known height are given.
  - Assuming normal errors, compute an unbiased estimate of the standard deviation of measurement error.
- Problem 4 (Sveshnikov 35.2): unbiased estimate of variance when the true distance is known or unknown.
  - 8 independent distance measurements are given.
  - (a) If the true distance is known (375 m), find an unbiased estimate of variance.
  - (b) If the distance is unknown, find an unbiased estimate of variance using the sample mean.
- Problem 5 (Sveshnikov 36.3): simultaneous confidence for mean and standard deviation.
  - 40 measurements of a base length; sample mean and sample standard deviation are given.
  - Assuming normal errors, find the probability that the given relative intervals around the sample mean and sample standard deviation contain the true mean and standard deviation.
- Problem 6 (Sveshnikov 35.3): unbiased estimates for mean and standard deviation.
  - 15 measurements of maximal airplane speed are given.
  - Assume normal distribution with negligible measurement error; find unbiased estimates of expected value and standard deviation.
- Homework problems (selected).
  - Practice computing sample variances and standard deviations from raw data.
  - See how variance of the sample mean changes with sample size.
  - Apply CLT to interpret whether observed sample means are consistent with assumed population means.

### 5.2 How to solve / approach them
- Confidence intervals for mean with known \(\sigma\) (Problems 1 and 2).
  - Use the formula
    \[
    \bar{x} \pm z_{1-\alpha/2}\frac{\sigma}{\sqrt{n}},
    \]
    taking \(z_{1-\alpha/2}\) from normal tables (e.g., 2.58 for 99% level).
  - For grouped data, compute the overall sample mean and effective sample size \(n\) by weighting group means by their group sizes.
- Unbiased sample variance and standard deviation (Problems 3 and 4).
  - For unknown mean, use the unbiased sample variance formula
    \[
    S^2 = \frac{1}{n-1}\sum_{j=1}^n (x_j-\bar{x})^2.
    \]
  - For known mean, replace \(\bar{x}\) with the known true value and divide by \(n\) to keep it unbiased for variance.
  - The unbiased estimator of standard deviation is usually \(\sqrt{S^2}\), recognizing that taking the square root introduces slight bias but is standard practice.
- Probability that relative intervals contain true parameters (Problem 5).
  - For the mean interval, standardize \(\bar{x}\) using known or estimated standard error and use normal or t-distribution as appropriate.
  - For the standard deviation interval, relate \(\tilde{\sigma}_x\) and the true \(\sigma\) via the chi-squared distribution for \((n-1)S^2/\sigma^2\).
- Unbiased estimates for airplane speed (Problem 6).
  - Compute sample mean as an unbiased estimator of expected value.
  - Compute sample variance with denominator \(n-1\) and take its square root as the standard deviation estimate.

### 5.3 Mini practice
- Practice 1: confidence interval for normal mean with known variance.
  - Question: 25 independent measurements give \(\bar{x}=100\) and known \(\sigma=10\). What is the 95% confidence interval for the true mean?
  - Brief answer: \(n=25\), so \(\sigma/\sqrt{n}=10/5=2\). With \(z_{0.975}\approx 1.96\), interval is \(100\pm 1.96\cdot 2\approx (96.08,103.92)\).
- Practice 2: unbiased variance estimate with known mean.
  - Question: If measurements \(x_1,\dots,x_n\) are normal with known mean \(\mu\) and unknown variance \(\sigma^2\), what statistic is unbiased for \(\sigma^2\)?
  - Brief answer: \(V_n/n\), where \(V_n=\sum_{j=1}^n (x_j-\mu)^2\), is unbiased for \(\sigma^2\) because \(E(V_n)=n\sigma^2\).
- Practice 3: sample mean as an unbiased estimator.
  - Question: When is the sample mean \(\bar{\xi}_n\) an unbiased estimator of the population mean \(\mu\)?
  - Brief answer: Always, as long as each \(\xi_j\) has mean \(\mu\), because \(E\bar{\xi}_n = \frac{1}{n}\sum E\xi_j = \mu\).

## 6. Quick recap
- A statistic is any function of sample data; parameters are unknown constants that describe the distribution family.
- Confidence intervals are random intervals built from the sample that contain the true parameter with a prescribed long-run frequency \(1-\alpha\).
- For an exponential-type shifted distribution, the sample minimum leads to a one-sided confidence interval for the shift parameter.
- For a normal distribution with known variance, the standard confidence interval for the mean is \(\bar{x}\pm z_{1-\alpha/2}\sigma/\sqrt{n}\).
- For a normal distribution with known mean, the sum of squared deviations scaled by the variance follows a chi-squared distribution and yields confidence intervals for the standard deviation.
- Asymptotic confidence intervals use the central limit theorem to approximate coverage when exact intervals are hard to construct.
- Point estimators are statistics used as single-number guesses; unbiasedness means the estimator has the correct expectation across all parameter values.
- The sample mean is an unbiased estimator of the population mean; other intuitive estimators (like \(n/S_n\) in exponential models) can be biased.
- The week 12 lab practices constructing confidence intervals, computing unbiased variance and standard deviation estimates, and using CLT to interpret sample means in real measurement and quality-control contexts.


[<kbd><br><- Return (ProbStat)<br></kbd>](ProbStat.md)
