# CSE206 — Week 06 Notes — Hypergeometric, Gamma/Exp/Cauchy, transforms of r.v.s
**Lectures:** CSE206_Fa24-06.pdf  
**Lab/Tutorial:** week06.pdf  

## 1. Big picture (5–10 bullets)
- Hypergeometric distribution models sampling without replacement from a finite population with “good” and “bad” items.  
- Moments of continuous random variables (means, variances, higher moments) can be computed directly from the pdf by integration.  
- The expectation of a function of a continuous random variable uses the same pattern as the discrete case: integrate \(g(x)\) against the density.  
- Two new continuous distributions are added: Cauchy (heavy-tailed, no moments) and exponential (nonnegative, memoryless).  
- The exponential distribution is a standard model for waiting times between events (e.g., failures, arrivals) and has mean \(1/\lambda\) and variance \(1/\lambda^2\).  
- A general change-of-variable method allows us to find the pdf of a function \(f(\xi)\) when the pdf of \(\xi\) is known.  
- The lab ties these ideas together: hypergeometric as a conditional binomial, Monte Carlo estimation of integrals, multinomial practice, and density transformations for Cauchy and exponential distributions.  

## 2. Key concepts and definitions

### 2.1 Hypergeometric distribution
- Plain-language definition.  
  - The hypergeometric distribution describes the number of “successes” when you draw \(n\) items from a finite population of size \(N\) without replacement, where \(b\) items are “good” and \(N-b\) are “bad”.  
- Formal definition (if needed).  
  - There are \(N\) tickets in a bag; \(b\) are good, \(N-b\) are bad. Draw \(n\) tickets without replacement. Let \(\xi\) be the number of good tickets drawn.  
  - Its pmf is  
    \[
    P(\xi = x) = \frac{\binom{b}{x}\binom{N-b}{n-x}}{\binom{N}{n}} I(x \in \{0,\dots,n\}),
    \]  
    with the understanding that \(\binom{\alpha}{\beta}=0\) if \(\beta>\alpha\).  
- Mean and variance (from lecture).  
  - Mean:  
    \[
    E\xi = \frac{bn}{N}.
    \]  
  - Variance:  
    \[
    \text{Var}(\xi) = \frac{bn(N-b)(N-n)}{N^2(N-1)}.
    \]  
- Intuition / mental model.  
  - Hypergeometric is like a binomial with a finite population and no replacement; the probability of success changes slightly after each draw.  
  - Mean \(\frac{bn}{N}\) is “sample size \(\times\) population fraction of good items”.  
- Tiny example.  
  - Box with \(N=20\) items, \(b=5\) defective, \(N-b=15\) good. Draw \(n=4\) without replacement.  
  - \(E\xi = (5\cdot 4)/20 = 1\) expected defective item.  

### 2.2 Moments of continuous random variables and expectation via density
- Plain-language definition.  
  - For continuous random variables, means and higher moments are computed by integrating against the density instead of summing against a pmf.  
- Formal definition (if needed).  
  - Let \(\xi\) be a continuous random variable with pdf \(p_\xi(x)\). If the integral exists, then  
    \[
    E\xi = \int_{-\infty}^{\infty} x\,p_\xi(x)\,dx.
    \]  
  - More generally, for a measurable function \(g:\mathbb{R}\to\mathbb{R}\):  
    \[
    Eg(\xi) = \int_{-\infty}^{\infty} g(x)\,p_\xi(x)\,dx,
    \]  
    whenever the integral converges. (This is Theorem 2.1 in the lecture.)  
- Intuition / mental model.  
  - This is the continuous analogue of \(E g(\xi) = \sum g(x)p_\xi(x)\) for discrete variables: sums are replaced by integrals.  
  - You never need the distribution of \(g(\xi)\) explicitly to compute its expectation.  
- Variance via density.  
  - For continuous \(\xi\) with mean \(E\xi\) and pdf \(p_\xi\),  
    \[
    \text{Var}(\xi) = E(\xi - E\xi)^2 = \int_{-\infty}^{\infty} (x - E\xi)^2 p_\xi(x)\,dx.
    \]  
  - Using the same trick as in the discrete case,  
    \[
    \text{Var}(\xi) = E\xi^2 - (E\xi)^2 = \int_{-\infty}^{\infty} x^2 p_\xi(x)\,dx - \left(\int_{-\infty}^{\infty} x p_\xi(x)\,dx\right)^2,
    \]  
    provided \(E\xi^2\) exists.  
- Tiny example.  
  - For \(\xi\sim\text{Uni}(a,b)\), the lecture re-derives  
    \[
    E\xi = \frac{a+b}{2},\quad E\xi^2 = \frac{a^2+ab+b^2}{3},\quad \text{Var}(\xi)=\frac{(b-a)^2}{12}
    \]  
    by integrating \(x p_\xi(x)\) and \(x^2 p_\xi(x)\).  

### 2.3 Moment generating function (mentioned)
- Plain-language definition.  
  - The moment generating function (mgf) of a random variable is a function whose derivatives at 0 give the moments.  
- Formal definition (if needed).  
  - For a random variable \(\xi\) (discrete or continuous), when the expectation exists:  
    \[
    \varphi_\xi(t) = Ee^{t\xi}.
    \]  
  - If \(\xi\) has a pdf \(p_\xi\), then  
    \[
    \varphi_\xi(t) = \int_{-\infty}^{\infty} e^{tx} p_\xi(x)\,dx.
    \]  
  - If \(\varphi_\xi\) is differentiable at \(t=0\), then \(\varphi_\xi'(0)=E\xi\). Higher derivatives (if they exist) give higher moments.  
- Intuition / mental model.  
  - The mgf packages all moments into a single function and is often used to recognize distributions and study sums of independent variables (though the lecture does not go further into this).  

### 2.4 Cauchy distribution
- Plain-language definition.  
  - The Cauchy distribution is a continuous distribution with very heavy tails; it does not have finite moments (no mean, no variance).  
- Formal definition (if needed).  
  - A random variable \(\xi\) has the Cauchy distribution if its pdf is  
    \[
    p_\xi(x) = \frac{1}{\pi(x^2+1)},\quad x\in\mathbb{R}.
    \]  
- Intuition / mental model.  
  - The density is sharply peaked at 0 but decays like \(1/x^2\); probabilities in the tails are large enough that integrals for moments diverge.  
  - It appears as the projection of a uniform direction on a circle/sphere, such as the intensity on the ground from a point source of radiation located above it.  
- Tiny example.  
  - If a particle is emitted from a point 1 m above the line and the emission angle \(\theta\) is uniform, the coordinate where it hits the ground has a Cauchy density.  

### 2.5 Exponential distribution
- Plain-language definition.  
  - The exponential distribution models the waiting time until a random event happens, with a constant rate \(\lambda\), and has the memoryless property.  
- Formal definition (if needed).  
  - A random variable \(\xi\) has exponential distribution with parameter \(\lambda>0\), written \(\xi\sim\text{Exp}(\lambda)\), if  
    \[
    p_\xi(x) = \lambda e^{-\lambda x} I(x\ge 0).
    \]  
  - It is supported on \([0,\infty)\): \(P(\xi\ge0)=1\).  
- Mean, variance, and moments (from lecture and lab tasks).  
  - Mean: \(E\xi = 1/\lambda\).  
  - Variance: \(\text{Var}(\xi)=1/\lambda^2\).  
  - More generally (lab Homework 8): the \(k\)-th moment satisfies \(E\xi^k = k!/\lambda^k\).  
- Memoryless property.  
  - For \(t,s\ge 0\):  
    \[
    P(\xi > t+s\,|\,\xi > t) = P(\xi > s).
    \]  
  - Intuition: if \(\xi\) is lifetime, the remaining time to failure does not depend on how long the item has already lasted.  
- Typical use cases.  
  - Time until next message, time until next failure, time until a radioactive decay, when the “rate” can be treated as constant over the time window considered.  

### 2.6 Density of a function of a random variable
- Plain-language definition.  
  - If \(\xi\) has a known density and we form a new variable \(\eta = f(\xi)\), we can often find the density of \(\eta\) using either cdfs or a change-of-variable formula.  
- Approach 1: via cdf.  
  - For any real \(y\),  
    \[
    F_\eta(y) = P(\eta\le y) = P(f(\xi)\le y).
    \]  
  - If \(F_\eta\) is continuous and piecewise continuously differentiable, then we may differentiate to get  
    \[
    p_\eta(y) = \frac{d}{dy}F_\eta(y).
    \]  
- Approach 2: via change of variables (invertible \(f\)).  
  - Assume \(\xi\) has pdf \(p_\xi\) and \(f:\mathbb{R}\to A\subset\mathbb{R}\) is injective and continuously differentiable, mapping the real line into an open set \(A\). Let \(\eta=f(\xi)\).  
  - The change-of-variable reasoning in the lecture gives the formula (for \(x\in A\)):  
    \[
    p_\eta(x) = p_\xi(f^{-1}(x))\left|\frac{d}{dx}f^{-1}(x)\right| I(x\in A),
    \]  
    where the indicator reflects that \(P(\eta\in A^c)=0\).  
- Intuition / mental model.  
  - The density of \(\eta\) redistributes the mass of \(\xi\) according to how the function \(f\) stretches or compresses the real line: the derivative of the inverse controls this stretching.  
- Tiny example outline.  
  - If \(\xi\sim\text{Uni}(0,1)\) and \(\eta = \sqrt{\xi}\), then \(f(x)=\sqrt{x}\) is invertible on \((0,1)\) with \(f^{-1}(y) = y^2\).  
  - The density of \(\eta\) is \(p_\eta(y) = p_\xi(y^2)\cdot 2y\) on \(0<y<1\).  

## 3. Core formulas and how to use them

### 3.1 Hypergeometric pmf, mean, and variance
- Pmf.  
  - \[
    P(\xi = x) = \frac{\binom{b}{x}\binom{N-b}{n-x}}{\binom{N}{n}},\quad x=0,1,\dots,n.
    \]  
- Mean.  
  - \[
    E\xi = \frac{bn}{N}.
    \]  
- Variance.  
  - \[
    \text{Var}(\xi) = \frac{bn(N-b)(N-n)}{N^2(N-1)}.
    \]  
- When to use it.  
  - In “without replacement” scenarios: drawing from a finite population of known composition (cards, balls, exam questions, bulbs in homework).  
- Common mistakes.  
  - Using binomial pmf when sampling without replacement from a small population; hypergeometric is more accurate.  
  - Forgetting that probabilities change after each draw in the hypergeometric setting.  

### 3.2 Expectation and variance of continuous random variables
- Expectation formula.  
  - For continuous \(\xi\) with pdf \(p_\xi\):  
    \[
    E\xi = \int_{-\infty}^{\infty} x\,p_\xi(x)\,dx.
    \]  
- Function of a random variable.  
  - \[
    Eg(\xi) = \int_{-\infty}^{\infty} g(x)\,p_\xi(x)\,dx.
    \]  
- Variance.  
  - \[
    \text{Var}(\xi) = \int_{-\infty}^{\infty} (x-E\xi)^2 p_\xi(x)\,dx
                    = \int_{-\infty}^{\infty} x^2 p_\xi(x)\,dx - \left(\int_{-\infty}^{\infty} x p_\xi(x)\,dx\right)^2.
    \]  
- When to use them.  
  - Any time you know a pdf and need mean, variance, or expectation of a function; especially for uniform, normal, exponential, and similar distributions.  
- Common mistakes.  
  - Forgetting limits of integration (e.g., integrating an exponential from \(-\infty\) instead of 0).  
  - Not checking whether the integral converges; for Cauchy, moments do not exist.  

### 3.3 Exponential distribution formulas
- Pdf and cdf.  
  - Pdf: \(p_\xi(x) = \lambda e^{-\lambda x} I(x\ge 0)\).  
  - Cdf: \(F_\xi(x) = 0\) for \(x<0\), and \(F_\xi(x) = 1 - e^{-\lambda x}\) for \(x\ge 0\).  
- Mean and variance.  
  - \(E\xi = 1/\lambda\), \(\text{Var}(\xi) = 1/\lambda^2\).  
- Memoryless property.  
  - For \(t,s\ge0\):  
    \[
    P(\xi > t+s\,|\,\xi > t) = P(\xi > s).
    \]  
- Higher moments (from homework).  
  - \(E\xi^k = k!/\lambda^k\).  
- When to use it.  
  - To model waiting times between independent events with constant rate (e.g., service times, lifetimes, inter-arrival times).  

### 3.4 Transformation formula for densities
- General change-of-variable formula (one-to-one case).  
  - If \(\eta=f(\xi)\), where \(\xi\) has pdf \(p_\xi\) and \(f\) is injective, differentiable with differentiable inverse, then for \(x\) in the image set \(A\):  
    \[
    p_\eta(x) = p_\xi(f^{-1}(x))\left|\frac{d}{dx}f^{-1}(x)\right|.
    \]  
- Cdf-based method.  
  - For any \(y\):  
    \[
    F_\eta(y) = P(f(\xi)\le y),
    \]  
    then differentiate with respect to \(y\) if the resulting cdf is smooth enough.  
- When to use them.  
  - When the new variable is a smooth function of the old one and you have the original pdf (e.g., squaring, reciprocals, rational transformations as in the Cauchy examples).  
- Common mistakes.  
  - Ignoring multiple branches when \(f\) is not one-to-one (then you must sum contributions from all pre-images).  
  - Forgetting the absolute value of the derivative of the inverse.  

## 4. Worked examples

### 4.1 Mean and variance of a hypergeometric variable via indicators
- Setup (from lecture).  
  - There are \(N\) tickets: \(b\) good, \(N-b\) bad. Draw \(n\) tickets without replacement. Let \(\xi\) be the number of good tickets drawn.  
- Step 1: represent \(\xi\) as a sum of indicators.  
  - Number the good tickets \(1,\dots,b\).  
  - Define indicator variables \(I_j\) for \(1\le j\le b\):  
    \[
    I_j = I(\text{the \(j\)-th good ticket was drawn}).
    \]  
  - Then  
    \[
    \xi = I_1 + \dots + I_b.
    \]  
- Step 2: compute \(E I_j\).  
  - Each ticket is equally likely to be among the \(n\) drawn.  
  - The probability that the \(j\)-th good ticket was selected is \(P(I_j=1)=n/N\).  
  - So \(E I_j = n/N\).  
- Step 3: compute the mean \(E\xi\).  
  - By linearity,  
    \[
    E\xi = E(I_1+\dots+I_b) = \sum_{j=1}^b E I_j = b\cdot \frac{n}{N} = \frac{bn}{N}.
    \]  
- Step 4: sketch of second moment and variance.  
  - Expand  
    \[
    E\xi^2 = E\left(\sum_{j=1}^b I_j\right)^2 = \sum_{j=1}^b E I_j^2 + \sum_{j\neq l} E(I_j I_l).
    \]  
  - Since \(I_j^2 = I_j\), the first sum gives \(b\cdot n/N\).  
  - For \(j\neq l\), \(I_j I_l=1\) only if both good tickets \(j\) and \(l\) were drawn; the lecture shows  
    \[
    E(I_j I_l) = \frac{n(n-1)}{N(N-1)}.
    \]  
  - Combine these to obtain  
    \[
    E\xi^2 = \frac{bn}{N} + b(b-1)\frac{n(n-1)}{N(N-1)},
    \]  
    and the given variance formula follows by subtracting \((E\xi)^2\).  
- Check your intuition.  
  - Expressing \(\xi\) as a sum of simple 0–1 variables and using linearity makes the mean and variance transparent without heavy combinatorics.  

### 4.2 Transforming a Cauchy variable (outline, as in lab task)
- Setup (based on lab Problem 4 and lecture section 4).  
  - Let \(\xi\) be Cauchy with pdf  
    \[
    p_\xi(x) = \frac{1}{\pi(1+x^2)}.
    \]  
  - Define a new random variable, for example, \(\eta = \frac{1}{1+\xi^2}\) or \(\zeta = \frac{\xi}{1+\xi^2}\). We want their pdfs.  
- Step 1: identify the transformation and its inverse (if invertible on a region).  
  - For \(\eta = \frac{1}{1+\xi^2}\), we have \(\eta\in(0,1]\) and the relation \(\xi^2 = \frac{1-\eta}{\eta}\), so \(\xi = \pm\sqrt{\frac{1-\eta}{\eta}}\).  
  - The mapping is not one-to-one; there are two branches (positive and negative).  
- Step 2: compute the pdf using multiple pre-images.  
  - For each \(y\in(0,1]\), add contributions from both roots:  
    \[
    p_\eta(y) = \sum_{\xi_i\in f^{-1}(y)} p_\xi(\xi_i)\left|\frac{d}{dy}\xi_i\right|.
    \]  
  - Apply this carefully using the Cauchy density and the derivative of \(\xi\) with respect to \(y\).  
- Step 3: sanity check (lecture emphasis).  
  - Verify that the resulting \(p_\eta(y)\) is nonnegative and integrates to 1 over its support.  
  - The lecture notes that if you obtain something that does not integrate to 1, a mistake was made.  
- Check your intuition.  
  - Squashing a heavy-tailed Cauchy variable through a bounded function like \(1/(1+\xi^2)\) creates a new variable supported on a bounded interval with a density that is more concentrated near values corresponding to \(\xi\) near 0.  

## 5. Lab/Tutorial essentials (week06.pdf)

### 5.1 What the lab asked you to do
- Problem 1: conditional hypergeometric via binomial sums.  
  - Let \(\xi\) and \(\eta\) be independent \(\text{Binomial}(n,p)\) variables and \(\zeta=\xi+\eta\). Prove that the conditional distribution of \(\xi\) given \(\zeta=N\) is hypergeometric with parameters \(2n,n,N\).  
- Problem 2: Monte Carlo integration via three estimators.  
  - Aim: approximate  
    \[
    I = \int_0^1 f(x)\,dx
    \]  
    where \(0\le f\le 1\) on \([0,1]\).  
  - Independent \(\xi,\eta\sim\text{Uni}(0,1)\). Define  
    \[
    \zeta_1 = I(\eta\le f(\xi)),\quad \zeta_2=f(\xi),\quad \zeta_3 = \frac12\bigl(f(\xi)+f(1-\xi)\bigr).
    \]  
  - Show all three have mean \(I\); then prove \(\text{Var}(\zeta_3)\le\text{Var}(\zeta_2)\le\text{Var}(\zeta_1)\).  
- Problem 3: multinomial practice with exam questions.  
  - 5 questions in topic 1, 7 in topic 2, 6 in topic 3, 6 in topic 4, 8 in topic 5, 4 in topic 6.  
  - You pick 20 questions:  
    - (a) Find \(P(\text{you choose }m_1,\dots,m_6\text{ questions in topics 1–6})\).  
    - (b) Find the probability that you selected at least one question from each topic.  
  - A friend picks 10 questions: find the probability he gets at least one from each topic.  
- Problem 4: transformations of a Cauchy random variable.  
  - Given \(\xi\) with Cauchy pdf \(p_\xi(x)=1/(\pi(1+x^2))\), find the pdfs of \(\eta = \xi/(1+\xi^2)\) and \(\zeta = 1/(1+\xi^2)\).  
- Homework (selected).  
  - Additional hypergeometric examples (e.g., bulbs and daffodils; waitress checking IDs).  
  - Exponential distribution practice: multi-day service times, explicit formulas for exponential moments, and expectations involving exponentials of exponentials.  
  - Another transformation problem: computing \(C\) in a pdf and then the pdf of \(1/\xi\).  

### 5.2 How to solve / approach them
- Conditional binomial-hypergeometric link (Problem 1).  
  - Write the joint pmf of \((\xi,\eta)\) as a product because they are independent and binomial.  
  - For fixed \(\zeta=N\), consider pairs \((x,N-x)\) with \(x=0,\dots,N\) as the only possibilities.  
  - Use the definition of conditional probability  
    \[
    P(\xi=x|\zeta=N) = \frac{P(\xi=x,\eta=N-x)}{\sum_k P(\xi=k,\eta=N-k)}
    \]  
    and show that this simplifies to the hypergeometric pmf with parameters \(2n,n,N\).  
- Monte Carlo estimators (Problem 2).  
  - For \(\zeta_1\): use the fact that \(\zeta_1\) is an indicator of the event \(\eta\le f(\xi)\). Condition on \(\xi\) and use independence of \(\eta\) to show \(E\zeta_1=I\).  
  - For \(\zeta_2\): use \(E\zeta_2 = E f(\xi)=\int_0^1 f(x)dx\).  
  - For \(\zeta_3\): use symmetry of \(\xi\) and \(1-\xi\); show its mean is the same and variance is reduced using covariance properties and the fact that averaging reduces variance.  
- Multinomial probabilities (Problem 3).  
  - For (a): total number of ways to choose 20 questions from 36, and number of ways to choose \(m_1\) from the 5 in topic 1, etc.; use the multinomial coefficient and treat topics as categories.  
  - For “at least one from each topic”: either count directly with inclusion–exclusion over missing topics, or compute the complement (cases where at least one topic is missing).  
  - For your friend’s 10 questions, repeat the logic with \(n=10\).  
- Transformations of Cauchy (Problem 4).  
  - For each new variable, explicitly write the mapping from \(\xi\) to \(\eta\) or \(\zeta\) and invert it (accounting for multiple branches).  
  - Use either the cdf method or the general transformation formula, summing over all pre-images.  
  - Check that the resulting pdfs integrate to 1 over their supports.  
- Exponential moments and expectations (homework).  
  - Use integration by parts to compute \(E\xi^k = \int_0^\infty x^k \lambda e^{-\lambda x}dx\).  
  - For expectations like \(E[\xi(1-e^{-a\xi})]\), exploit the linearity of expectation and known integrals for exponential tails.  

### 5.3 Mini practice
- Practice 1: recognizing hypergeometric.  
  - Question: A box has 5 tulip bulbs and 4 daffodil bulbs. Six bulbs are planted without replacement. What distribution should you use for the number of daffodils planted?  
  - Brief answer: Hypergeometric with \(N=9\), \(b=4\), \(n=6\); \(\xi\sim\text{Hypergeometric}(9,4,6)\).  
- Practice 2: memoryless exponential.  
  - Question: If \(\xi\sim\text{Exp}(\lambda)\) and we know the device has survived at least 3 years, what is \(P(\xi>3+2|\xi>3)\)?  
  - Brief answer: By memorylessness, \(P(\xi>5|\xi>3)=P(\xi>2)=e^{-\lambda\cdot 2}\).  
- Practice 3: simple density transformation.  
  - Question: If \(\xi\sim\text{Uni}(0,1)\) and \(\eta = 1-\xi\), what is \(p_\eta(y)\)?  
  - Brief answer: The map \(f(x)=1-x\) is invertible on \((0,1)\) with \(f^{-1}(y)=1-y\), and \(|d/dy f^{-1}(y)|=1\). Since \(p_\xi\equiv1\) on \((0,1)\), we get \(p_\eta(y)=1\) for \(0<y<1\): \(\eta\sim\text{Uni}(0,1)\).  

## 6. Quick recap
- Hypergeometric distribution models the number of “good” items in a sample without replacement; its pmf uses combinations, and its mean and variance can be derived via indicator variables.  
- For continuous random variables, expectations and variances are computed via integrals against the pdf, including expectations of functions \(g(\xi)\).  
- The Cauchy distribution has pdf \(1/[\pi(1+x^2)]\) and no finite moments, illustrating that not all distributions have a mean or variance.  
- The exponential distribution \(\text{Exp}(\lambda)\) models nonnegative waiting times, with mean \(1/\lambda\), variance \(1/\lambda^2\), and the memoryless property.  
- The density of a transformed random variable \(\eta=f(\xi)\) can be found by differentiating its cdf or using the change-of-variable formula with the inverse of \(f\).  
- The week 6 lab deepens understanding of hypergeometric distributions, Monte Carlo estimation of integrals, multinomial profiles of topics, and density transformations for Cauchy and exponential variables.  


[<kbd><br><- Return (ProbStat)<br></kbd>](ProbStat.md)
