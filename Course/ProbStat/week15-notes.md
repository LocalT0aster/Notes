# CSE206 — Week 15 Notes — Hypothesis testing II (power, unbiased/consistent tests)
**Lectures:** CSE206_Fa24-15.pdf
**Lab/Tutorial:** none

## 1. Big picture (5–10 bullets)
- This week continues hypothesis testing, focusing on Type I and Type II errors and the trade-off between them.
- For normal models with known variance, explicit formulas for Type I and Type II error probabilities are derived using standard normal quantiles.
- The power function of a test is introduced: the probability that the test correctly rejects the null hypothesis when the alternative is true.
- Tests are called unbiased when their power under any alternative parameter is at least as large as the significance level.
- Tests are called consistent if, for any fixed alternative, the power tends to 1 as sample size grows.
- The lecture uses the normal model as a main example, but the definitions and ideas are general and apply to other models as well.

## 2. Key concepts and definitions

### 2.1 Recap: hypothesis tests, errors, and critical regions
- Hypotheses.
  - The parameter space $\Theta$ is split into two disjoint parts:
    $$
    H_0:\theta\in\Theta_0,\quad H_1:\theta\in\Theta_1,
    $$
    where $H_0$ is the null hypothesis and $H_1$ is the alternative.
- Statistic and decision rule.
  - A test statistic $t(\xi_1,\dots,\xi_n)$ is used to decide.
  - The real line is partitioned into:
    - acceptance region $R_0$: if $t\in R_0$, do not reject $H_0$;
    - critical (rejection) region $R_1$: if $t\in R_1$, reject $H_0$.
- Type I and Type II errors.
  - Type I error: reject $H_0$ when $H_0$ is actually true ($\theta\in\Theta_0$).
  - Type II error: fail to reject $H_0$ when $H_1$ is true ($\theta\in\Theta_1$).
- Significance level.
  - The test is designed to keep the probability of Type I error below a prescribed level $\alpha$:
    $$
    \alpha \ge \sup_{\theta\in\Theta_0}P_\theta(t\in R_1).
    $$
  - In many standard tests, equality is achieved (the “worst-case” Type I error probability is exactly $\alpha$).

### 2.2 Example: Type I and Type II errors in a normal mean test
- Model (Example 1.1).
  - $\xi\sim N(\theta,\sigma^2)$, $\sigma^2$ known. Sample $\xi_1,\dots,\xi_n$.
  - Test statistic: sample mean
    $$
    t(\xi_1,\dots,\xi_n) = \bar{\xi}_n = \frac{1}{n}\sum_{j=1}^n \xi_j.
    $$
  - Hypotheses: $H_0:\theta=\theta_0$; alternative $H_1:\theta=\theta_1$ with $\theta_1>\theta_0$ (simple alternative).
  - Critical region of the form $R_1 = [t_\alpha,\infty)$.
- Type I error probability.
  - Under $H_0$: $\bar{\xi}_n\sim N(\theta_0,\sigma^2/n)$.
  - Standardize:
    $$
    Z=\frac{\sqrt{n}(\bar{\xi}_n-\theta_0)}{\sigma}\sim N(0,1).
    $$
  - Type I error probability is
    $$
    P_{\theta_0}(\bar{\xi}_n\ge t_\alpha)
      = P\left(Z\ge \frac{\sqrt{n}(t_\alpha-\theta_0)}{\sigma}\right).
    $$
  - The critical value is chosen so this equals $\alpha$, giving
    $$
    t_\alpha = \theta_0 + z_{1-\alpha}\frac{\sigma}{\sqrt{n}},
    $$
    where $z_{1-\alpha}$ is the standard normal quantile with right-tail area $\alpha$.
- Type II error probability (for a simple alternative $\theta_1$).
  - Under $H_1$: $\bar{\xi}_n\sim N(\theta_1,\sigma^2/n)$.
  - Type II error is
    $$
    \beta(\theta_1) = P_{\theta_1}(\bar{\xi}_n < t_\alpha)
      = P\left(\frac{\sqrt{n}(\bar{\xi}_n-\theta_1)}{\sigma} < \frac{\sqrt{n}(t_\alpha-\theta_1)}{\sigma}\right).
    $$
  - In terms of $Z\sim N(0,1)$:
    $$
    \beta(\theta_1) = P\left(Z < \frac{\sqrt{n}(t_\alpha-\theta_1)}{\sigma}\right).
    $$
  - Plug $t_\alpha=\theta_0 + z_{1-\alpha}\sigma/\sqrt{n}$:
    $$
    \frac{\sqrt{n}(t_\alpha-\theta_1)}{\sigma}
      = z_{1-\alpha} - \frac{\sqrt{n}(\theta_1-\theta_0)}{\sigma},
    $$
    so
    $$
    \beta(\theta_1) = P\left(Z < z_{1-\alpha} - \frac{\sqrt{n}(\theta_1-\theta_0)}{\sigma}\right).
    $$
- Intuition / mental model.
  - $t_\alpha$ is chosen to control the Type I error probability at $\alpha$; this simultaneously determines the Type II error probabilities for specific alternative values.
  - Larger separation $\theta_1-\theta_0$ or larger sample size $n$ reduces $\beta(\theta_1)$ (the chance of missing a real difference).

### 2.3 Power function
- Plain-language definition.
  - The power function of a test, $W(\theta)$, tells you how likely the test is to reject the null hypothesis for each possible parameter value.
  - For parameters in $\Theta_1$ (where the alternative holds), higher power means a better test (less likely to miss a real effect).
- Formal definition.
  - For a given critical region $R_1$:
    $$
    \beta(\theta) = P_\theta(t\in R_0) = P_\theta(\text{Type II error}),\quad \theta\in\Theta_1,
    $$
    and
    $$
    W(\theta) = 1-\beta(\theta) = P_\theta(t\in R_1),\quad \theta\in\Theta_1.
    $$
  - $W(\theta)$ is the power function.
- Example (normal, composite alternative).
  - With $H_0:\theta=\theta_0$ and composite alternative $H_1:\theta>\theta_0$, critical region $R_1 = [t_\alpha,\infty)$, the power function is
    $$
    W(\theta)
     = P_\theta(\bar{\xi}_n\ge t_\alpha)
     = P\left(Z\ge \frac{\sqrt{n}(t_\alpha-\theta)}{\sigma}\right)
     = \Phi\left(\frac{\sqrt{n}(\theta-\theta_0)}{\sigma} - z_{1-\alpha}\right),
    $$
    where $\Phi$ is the standard normal cdf.
- Intuition / mental model.
  - $W(\theta)$ is small near the boundary between null and alternative and increases as $\theta$ moves farther into the alternative region, ideally approaching 1.

### 2.4 Unbiased and consistent tests
- Unbiased test.
  - A test is called unbiased if its power under any alternative is at least as large as its significance level.
  - Formal condition: if
    $$
    W(\theta)\ge \alpha\quad \text{for all }\theta\in\Theta_1,
    $$
    then the test is unbiased.
  - Equivalent statements (from lecture):
    - The probability of not committing Type II error is at least $\alpha$ for all $\theta\in\Theta_1$.
    - The probability of falling in the critical region $R_1$ is at least $\alpha$ whenever $H_1$ is true.
    - The probability of correct rejection (when $H_1$ is true) is at least as large as the probability of wrong rejection (when $H_0$ is true).
- Consistent test.
  - A test is consistent if, for any fixed alternative $\theta\in\Theta_1$, the power tends to 1 as the sample size $n\to\infty$:
    $$
    W(\theta)\to 1\quad (n\to\infty).
    $$
- Intuition / mental model.
  - Unbiasedness ensures the test is not systematically “weak” under the alternative relative to its false-alarm rate.
  - Consistency ensures that with enough data, the test almost certainly detects any fixed difference from the null.

## 3. Core formulas and how to use them

### 3.1 Type I error and critical value (normal mean test)
- Given $\xi_1,\dots,\xi_n\sim N(\theta,\sigma^2)$, testing $H_0:\theta=\theta_0$ vs $H_1:\theta>\theta_0$:
  - Test statistic: $\bar{\xi}_n$.
  - Standardization under $H_0$:
    $$
    Z = \frac{\sqrt{n}(\bar{\xi}_n-\theta_0)}{\sigma}\sim N(0,1).
    $$
  - Choose critical value
    $$
    t_\alpha = \theta_0 + z_{1-\alpha}\frac{\sigma}{\sqrt{n}}
    $$
    so that
    $$
    P_{\theta_0}(\bar{\xi}_n\ge t_\alpha) = \alpha.
    $$
- When to use it.
  - In one-sided normal-approximation tests for means with known variance, to set the decision threshold corresponding to a desired significance level.

### 3.2 Type II error and power (normal mean test)
- For alternative $\theta_1>\theta_0$:
  - Type II error probability:
    $$
    \beta(\theta_1) = P_{\theta_1}(\bar{\xi}_n< t_\alpha)
                   = P\left(Z < z_{1-\alpha} - \frac{\sqrt{n}(\theta_1-\theta_0)}{\sigma}\right),
    $$
    with $Z\sim N(0,1)$.
  - Power:
    $$
    W(\theta_1) = 1-\beta(\theta_1)
                = \Phi\left(\frac{\sqrt{n}(\theta_1-\theta_0)}{\sigma} - z_{1-\alpha}\right).
    $$
- When to use it.
  - To calculate the probability of correctly rejecting the null hypothesis under specific alternative values and to understand how sample size and effect size affect power.

## 4. Worked examples

### 4.1 Type I and Type II errors for a normal test
- Setup.
  - $\xi_1,\dots,\xi_n\sim N(\theta,\sigma^2)$, $\sigma^2$ known.
  - Test $H_0:\theta=\theta_0$ vs $H_1:\theta=\theta_1$ with $\theta_1>\theta_0$.
  - Test statistic: $\bar{\xi}_n$. Critical region: $R_1=[t_\alpha,\infty)$.
- Step 1: choose $t_\alpha$ via Type I error condition.
  - Under $H_0$:
    $$
    \bar{\xi}_n\sim N(\theta_0,\sigma^2/n),\quad Z=\frac{\sqrt{n}(\bar{\xi}_n-\theta_0)}{\sigma}\sim N(0,1).
    $$
  - Require $P_{\theta_0}(\bar{\xi}_n\ge t_\alpha)=\alpha$, so
    $$
    \alpha = P\left(Z\ge \frac{\sqrt{n}(t_\alpha-\theta_0)}{\sigma}\right)
           = P(Z\ge z_{1-\alpha}),
    $$
    leading to
    $$
    t_\alpha = \theta_0 + z_{1-\alpha}\frac{\sigma}{\sqrt{n}}.
    $$
- Step 2: compute $\beta(\theta_1)$ for the simple alternative.
  - Under $H_1$: $\bar{\xi}_n\sim N(\theta_1,\sigma^2/n)$.
  - Type II error probability:
    $$
    \beta(\theta_1) = P_{\theta_1}(\bar{\xi}_n<t_\alpha)
                   = P\left(\frac{\sqrt{n}(\bar{\xi}_n-\theta_1)}{\sigma} < \frac{\sqrt{n}(t_\alpha-\theta_1)}{\sigma}\right).
    $$
  - Since the standardized variable is $N(0,1)$,
    $$
    \beta(\theta_1) = P\left(Z< z_{1-\alpha} - \frac{\sqrt{n}(\theta_1-\theta_0)}{\sigma}\right),
    $$
    and $W(\theta_1)=1-\beta(\theta_1)$.
- Check your intuition.
  - For fixed $\theta_1-\theta_0>0$, as $n$ increases, $\frac{\sqrt{n}(\theta_1-\theta_0)}{\sigma}$ grows, $\beta(\theta_1)$ shrinks, and $W(\theta_1)$ approaches 1: with enough data, the test almost surely detects the difference.

### 4.2 Power function for a one-sided normal test (composite alternative)
- Setup.
  - Same as above but with composite alternative $H_1:\theta>\theta_0$.
  - Critical region: $R_1=[t_\alpha,\infty)$ with $t_\alpha = \theta_0 + z_{1-\alpha}\sigma/\sqrt{n}$.
- Step 1: write power for general $\theta>\theta_0$.
  - For any $\theta\in \Theta_1=(\theta_0,\infty)$:
    $$
    W(\theta) = P_\theta(\bar{\xi}_n\ge t_\alpha)
              = P\left(\frac{\sqrt{n}(\bar{\xi}_n-\theta)}{\sigma}\ge \frac{\sqrt{n}(t_\alpha-\theta)}{\sigma}\right).
    $$
  - With $Z\sim N(0,1)$:
    $$
    W(\theta) = P\left(Z\ge z_{1-\alpha} - \frac{\sqrt{n}(\theta-\theta_0)}{\sigma}\right)
              = \Phi\left(\frac{\sqrt{n}(\theta-\theta_0)}{\sigma} - z_{1-\alpha}\right).
    $$
- Step 2: discuss unbiasedness and consistency.
  - For $\theta=\theta_0$, the power equals $\alpha$ by construction.
  - For $\theta>\theta_0$, the argument of $\Phi$ is larger than $-z_{1-\alpha}$, so $W(\theta)\ge\alpha$, confirming the test is unbiased.
  - For any fixed $\theta>\theta_0$, as $n\to\infty$, $\frac{\sqrt{n}(\theta-\theta_0)}{\sigma}\to\infty$, so $W(\theta)\to 1$: the test is consistent.
- Check your intuition.
  - An unbiased test gives at least as much probability of rejecting $H_0$ under any alternative as under $H_0$; a consistent test will almost certainly reject $H_0$ for any fixed true alternative parameter when enough data are available.

## 6. Quick recap
- Hypothesis testing compares a null $H_0$ and alternative $H_1$ using a test statistic and a critical region; decisions lead to either correct outcomes or Type I/II errors.
- The significance level $\alpha$ is an upper bound on the Type I error probability; in many tests, critical values are chosen so this bound is achieved exactly.
- For normal models with known variance, Type I and Type II error probabilities can be computed explicitly via standard normal quantiles.
- The power function $W(\theta) = P_\theta(\text{reject }H_0)$ quantifies how effective a test is at detecting deviations from $H_0$ across the alternative parameter space.
- A test is unbiased if its power is at least $\alpha$ for every parameter value in the alternative; this means it is never systematically weaker under the alternative than under the null.
- A test is consistent if, for any fixed alternative parameter, the power approaches 1 as the sample size grows, ensuring that large samples make true differences almost surely noticeable.
- The week 15 lecture uses the normal mean test to derive these ideas concretely, but the definitions and concepts generalize to a wide range of statistical testing problems.


[<kbd><br><- Return (ProbStat)<br></kbd>](ProbStat.md)
