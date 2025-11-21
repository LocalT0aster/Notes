# CSE206 — Week 07 Notes — Poisson/Poisson process, continuous joint pdfs, conditional pdfs, transformations
**Lectures:** CSE206_Fa24-07-08.pdf
**Lab/Tutorial:** week07.pdf

## 1. Big picture (5–10 bullets)
- This week explains where the Poisson distribution comes from, via binomial limits and the Poisson process.
- Poisson variables model counts of rare events in fixed time or space intervals, and Poisson processes model such counts over time.
- Continuous random vectors are introduced: joint probability density functions (pdfs), marginal pdfs, and independence in the continuous setting.
- Uniform random vectors and multivariate normal (Gaussian) vectors are key examples of continuous random vectors.
- Conditional pdfs and conditional expectations for continuous random variables generalize the discrete notions you already know.
- Joint densities transform under changes of variables using the multivariate change-of-variables (Jacobian) formula.
- The lab reinforces Poisson approximations to binomial counts, and joint-density ideas via uniform distributions on regions (unit disk, angles on a circle) and trigonometric transformations.

## 2. Key concepts and definitions

### 2.1 Poisson random variable and Poisson approximation
- Plain-language definition.
  - A Poisson random variable counts how many times a certain type of event happens in a fixed interval when events are rare and occur independently at a constant average rate.
- Formal definition (if needed).
  - A random variable \(\xi\) has Poisson distribution with parameter \(\lambda>0\), written \(\xi\sim\text{Poi}(\lambda)\), if its pmf is
    \[
    P(\xi = x) = \frac{e^{-\lambda}\lambda^x}{x!} I(x\in\{0,1,2,\dots\}).
    \]
- Poisson as a limit of binomial (from Theorem 1.1).
  - Consider a sequence of binomial variables \(\xi_n\sim\text{Binomial}(n,p_n)\) with \(p_n n = \lambda\) (so \(p_n=\lambda/n\)).
  - For each fixed integer \(x\ge 0\):
    \[
    \lim_{n\to\infty} P(\xi_n = x) = \frac{e^{-\lambda}\lambda^x}{x!}.
    \]
  - In words: for large \(n\) and small \(p\), with \(np=\lambda\) fixed, the binomial pmf at \(x\) is well approximated by the Poisson pmf with parameter \(\lambda\).
- Intuition / mental model.
  - When you have many “tiny” independent opportunities for something to happen, each with very small probability, the count of successes behaves approximately like a Poisson variable.
- Tiny example (sketch).
  - Toss a coin \(n\) times with very small success probability \(p\) such that \(np=\lambda\). For moderate \(x\), the probability you see exactly \(x\) successes is close to Poisson\((\lambda)\) at \(x\).

### 2.2 Poisson process idea
- Plain-language description.
  - A Poisson process is a random model of event occurrences in time where:
    - events happen independently in disjoint time intervals,
    - the average number of events per unit time is \(\lambda\), and
    - the number of events in an interval of length \(r\) is approximately Poisson\((r\lambda)\).
- Informal construction (from the lecture).
  - Divide a unit time interval into \(N\) very small equal subintervals.
  - In each tiny subinterval, the event either does not occur or occurs exactly once, with probability \(p_N=\lambda/N\). The tiny counts \(\xi_j\) are (approximately) \(\text{Bernoulli}(p_N)\).
  - On a “middle-range” interval of length \(m/N\), the total count
    \[
    \xi = \xi_1+\dots+\xi_m \sim \text{Binomial}\left(m,\frac{\lambda}{N}\right).
    \]
  - With \(m/N=r\) fixed and \(N\) large, \(m\) is large and \(\lambda/N\) small, so \(\xi\) is approximately \(\text{Poi}(r\lambda)\) via the Poisson approximation.
- Intuition / mental model.
  - Events occur “continuously” in time, but when we zoom in enough, each tiny time slot almost never has more than one event; counts over longer intervals become Poisson-distributed.
- Tiny example (from Example 1.2).
  - A server receives on average \(\lambda=180\) queries per hour. You want the distribution of the number of queries in a 10-minute interval.
  - Here, the 60-minute unit is split into six 10-minute blocks, so \(r = 10/60 = 1/6\). The mean in 10 minutes is \(r\lambda = 30\).
  - The count in 10 minutes is modeled as approximately \(\text{Poi}(30)\).

### 2.3 Continuous random vectors and joint pdf
- Plain-language definition.
  - A continuous random vector is a vector of random variables that has a joint pdf \(p_\xi(x_1,\dots,x_d)\); probabilities of regions in \(\mathbb{R}^d\) come from integrating this pdf.
- Formal definition (if needed).
  - A random vector \(\xi=(\xi_1,\dots,\xi_d):\Omega\to\mathbb{R}^d\) is continuous if there exists a nonnegative integrable function \(p_\xi:\mathbb{R}^d\to\mathbb{R}\) such that for every Borel set \(B\subset\mathbb{R}^d\):
    \[
    P(\xi\in B) = \int_B p_\xi(x)\,dx,
    \]
    where \(dx=dx_1\dots dx_d\) is the volume element.
- Basic properties.
  - For any fixed vector \(x\in\mathbb{R}^d\): \(P(\xi=x)=0\).
  - More generally, the probability that \(\xi\) lands in any “thin” lower-dimensional set (like a line in \(\mathbb{R}^2\)) is zero when \(\xi\) is continuous.
  - A random vector can fail to be continuous even if each component is continuous; for example \((X,X)\) with \(X\sim\text{Uni}(0,1)\) lives on the line \(\{(x,x):0<x<1\}\), which has zero area.
- Intuition / mental model.
  - Joint pdfs generalize 1D densities: they spread probability over areas (2D), volumes (3D), and higher-dimensional regions.
  - All probability questions about a continuous random vector can be answered by integrating its joint pdf over appropriate regions.

### 2.4 Marginal pdfs
- Plain-language definition.
  - Marginal pdfs are the densities of individual components of a random vector; they are obtained by integrating the joint pdf over the other variables.
- Formal definitions (if needed).
  - For a 2D random vector \(\xi=(\xi_1,\xi_2)\) with joint pdf \(p_\xi(x_1,x_2)\):
    \[
    p_{\xi_1}(x_1) = \int_{-\infty}^\infty p_\xi(x_1,x_2)\,dx_2,\quad
    p_{\xi_2}(x_2) = \int_{-\infty}^\infty p_\xi(x_1,x_2)\,dx_1.
    \]
  - For higher dimensions, integrate out all other coordinates to get each marginal pdf.
- Intuition / mental model.
  - Marginals tell you how each coordinate behaves on its own, ignoring the others.
  - They are continuous analogues of marginal pmfs for discrete random vectors.
- Tiny example (from Example 2.10).
  - Joint pdf on the triangle \(0<x_2\le x_1<1\):
    \[
    p_{\xi_1,\xi_2}(x_1,x_2) = \frac{1}{x_1} I(0<x_2\le x_1<1).
    \]
  - Marginal of \(\xi_1\): integrate over \(x_2\):
    \[
    p_{\xi_1}(x_1) = \int_0^{x_1} \frac{1}{x_1}I(0<x_1<1)\,dx_2 = I(0<x_1<1),
    \]
    so \(\xi_1\sim\text{Uni}(0,1)\).

### 2.5 Uniform and multivariate normal random vectors
- Uniform on a region \(R\subset\mathbb{R}^d\).
  - A random vector \(\xi\) has uniform distribution on a region \(R\) of positive volume (area if \(d=2\), volume if \(d=3\)), written \(\xi\sim\text{Uni}(R)\), if
    \[
    p_\xi(x) = \frac{1}{|R|}I(x\in R),
    \]
    where \(|R|\) is the area/volume of \(R\).
  - Intuition: every point in the region is equally likely; this formalizes “geometric probability”.
- Full-rank Gaussian random vector.
  - Let \(K\) be a symmetric positive-definite \(d\times d\) matrix and \(\mu\in\mathbb{R}^d\). A random vector \(\xi\) has multivariate normal distribution \(N^d(\mu,K)\) if its pdf is
    \[
    p_\xi(x) = \frac{1}{(2\pi)^{d/2}\sqrt{\det K}}
              \exp\left(-\frac12 (x-\mu)\cdot K^{-1}(x-\mu)\right),
    \]
    where \(\cdot\) is the usual dot product.
  - In 2D this is called a full-rank bivariate normal. Its covariance matrix \(K\) encodes variances and covariance between the two components.
- Intuition / mental model.
  - Uniform vectors represent “pure randomness” inside a fixed shape; multivariate normals represent bell-shaped clouds in higher dimensions, with ellipses/ellipsoids as contours.

### 2.6 Independence in terms of pdfs
- Plain-language definition.
  - Two continuous random variables \(\xi_1,\xi_2\) are independent if knowing one tells you nothing about the other; this shows up as a factorization of the joint pdf into the product of marginals.
- Formal definition (continuous case).
  - For continuous \(\xi=(\xi_1,\dots,\xi_d)\), the components are independent if for all \((x_1,\dots,x_d)\):
    \[
    p_\xi(x_1,\dots,x_d) = p_{\xi_1}(x_1)\cdots p_{\xi_d}(x_d),
    \]
    except possibly on sets of measure zero (isolated points do not matter for integration).
- Intuition / mental model.
  - Independence means that the joint density “separates” into one factor for each component; there is no “interaction term”.
  - Failure of factorization over a region of nonzero area/volume indicates dependence.
- Tiny examples.
  - Example 2.5 (independent uniforms): if
    \[
    p_\xi(x_1,x_2) = I((x_1,x_2)\in(0,1)\times(0,1)),
    \]
    then \(p_{\xi_1}(x_1)=I(0<x_1<1)\), \(p_{\xi_2}(x_2)=I(0<x_2<1)\), and
    \[
    p_\xi(x_1,x_2)=p_{\xi_1}(x_1)p_{\xi_2}(x_2),
    \]
    so \(\xi_1,\xi_2\) are independent.
  - In Example 2.6, the joint pdf is nonconstant over a triangular region and does not factor into a product of marginals; the components are dependent.

### 2.7 Conditional pdf and conditional expectation (continuous)
- Plain-language definition.
  - The conditional pdf \(p_{\xi_2|\xi_1}(x_2|x_1)\) describes the distribution of \(\xi_2\) when we condition on \(\xi_1=x_1\), for continuous variables.
  - The conditional expectation \(E[\xi_2|\xi_1=x_1]\) is the mean of this conditional distribution; as a function of \(x_1\), it is a new random variable \(E[\xi_2|\xi_1]\).
- Formal definitions (if needed).
  - For a continuous random vector \((\xi_1,\xi_2)\) with joint pdf \(p_{\xi_1,\xi_2}(x_1,x_2)\) and marginals \(p_{\xi_1},p_{\xi_2}\):
    \[
    p_{\xi_2|\xi_1}(x_2|x_1) = \frac{p_{\xi_1,\xi_2}(x_1,x_2)}{p_{\xi_1}(x_1)} I(p_{\xi_1}(x_1)\ne 0).
    \]
  - For a fixed \(x_1\) with \(p_{\xi_1}(x_1)>0\), this function in \(x_2\) integrates to 1.
  - Conditional expectation given \(\xi_1=x_1\):
    \[
    E[\xi_2|\xi_1=x_1] = \int_{-\infty}^\infty x_2\,p_{\xi_2|\xi_1}(x_2|x_1)\,dx_2.
    \]
- Intuition / mental model.
  - Conditional pdfs and expectations are continuous analogues of discrete conditional pmfs and conditional means: they describe how one variable behaves if the other’s value is fixed.
- Tiny example (from Example 2.10).
  - With joint pdf \(p_{\xi_1,\xi_2}(x_1,x_2)=\frac{1}{x_1}I(0<x_2\le x_1<1)\), we already saw \(p_{\xi_1}(x_1)=I(0<x_1<1)\).
  - Then
    \[
    p_{\xi_2|\xi_1}(x_2|x_1) = \frac{1}{x_1}I(0<x_2\le x_1<1),
    \]
    which is the uniform density on \((0,x_1)\).
  - So, conditioned on \(\xi_1=x_1\), \(\xi_2\sim\text{Uni}(0,x_1)\).

### 2.8 Transformation of joint pdf under change of variables
- Plain-language definition.
  - When we apply a smooth, invertible transformation \(T\) to a continuous random vector, the new joint pdf is obtained by “transporting” the original pdf and multiplying by the absolute value of the Jacobian determinant of the inverse transformation.
- Formal statement (Theorem 4.1).
  - Let \(\xi=(\xi_1,\dots,\xi_d)\) be a continuous random vector with joint pdf \(p_\xi\) supported on \(D\subset\mathbb{R}^d\) (where \(p_\xi>0\)).
  - Let \(T:D\to\mathbb{R}^d\) be invertible, continuously differentiable with continuously differentiable inverse. Define \(\eta=T(\xi)\).
  - Then the joint pdf of \(\eta\) is
    \[
    p_\eta(y) = p_\xi(T^{-1}(y))\,\bigl|\det (T^{-1})'(y)\bigr|\,I(y\in T(D)),
    \]
    where \((T^{-1})'(y)\) is the Jacobian matrix of \(T^{-1}\) at \(y\), and \(|\det(\cdot)|\) is its absolute determinant.
- Intuition / mental model.
  - This is the multivariate version of the 1D formula \(p_Y(y)=p_X(x)\left|\frac{dx}{dy}\right|\) for \(Y=f(X)\).
  - The determinant of the Jacobian measures how volumes are stretched or compressed by the transformation; the pdf compensates accordingly.
- Tiny example (sketch: linear transformation of Gaussian).
  - If \(\xi\sim N^d(\mu,K)\) and \(\eta = T(\xi)\) for an invertible linear map \(T\), then Theorem 4.1 implies \(\eta\sim N^d(T\mu, TKT^\top)\).
  - This uses that the Jacobian of \(T^{-1}\) is the matrix \(T^{-1}\) itself.

## 3. Core formulas and how to use them

### 3.1 Poisson pmf and Poisson approximation
- Poisson pmf.
  - \[
    P(\xi=x) = \frac{e^{-\lambda}\lambda^x}{x!},\quad x=0,1,2,\dots.
    \]
- Poisson approximation to binomial.
  - For \(\xi_n\sim\text{Binomial}(n,p_n)\) with \(p_nn=\lambda\),
    \[
    P(\xi_n=x)\approx \frac{e^{-\lambda}\lambda^x}{x!}
    \]
    for fixed \(x\) when \(n\) is large and \(p_n\) is small.
- When to use it.
  - Large number of independent trials with small success probability and moderate expected count \(np\).
  - Many lab/homework tasks (e.g., typos per page, cupcakes without raisins, hurricanes per year) rely on this approximation.
- Common mistakes.
  - Using Poisson when \(n\) is small or \(p\) is not small (then the approximation may be poor).
  - Forgetting that Poisson mean and variance are both \(\lambda\).

### 3.2 Joint, marginal, and conditional pdfs
- Joint pdf to marginal pdf.
  - For continuous \((\xi_1,\xi_2)\):
    \[
    p_{\xi_1}(x_1) = \int_{-\infty}^\infty p_{\xi_1,\xi_2}(x_1,x_2)\,dx_2,\quad
    p_{\xi_2}(x_2) = \int_{-\infty}^\infty p_{\xi_1,\xi_2}(x_1,x_2)\,dx_1.
    \]
- Independence condition.
  - If
    \[
    p_{\xi_1,\xi_2}(x_1,x_2) = p_{\xi_1}(x_1)p_{\xi_2}(x_2)
    \]
    for all \((x_1,x_2)\) in a region of positive area, then \(\xi_1,\xi_2\) are independent.
- Conditional pdf.
  - For \(p_{\xi_1}(x_1)>0\):
    \[
    p_{\xi_2|\xi_1}(x_2|x_1) = \frac{p_{\xi_1,\xi_2}(x_1,x_2)}{p_{\xi_1}(x_1)}.
    \]
  - Conditional expectation:
    \[
    E[\xi_2|\xi_1=x_1] = \int x_2\,p_{\xi_2|\xi_1}(x_2|x_1)\,dx_2.
    \]
- When to use them.
  - To derive the behavior of one coordinate from the joint model (marginals).
  - To check independence (factorization).
  - To compute conditional probabilities in continuous settings, as in the triangle examples or unit disk lab problem.

### 3.3 Transformation of joint pdfs
- Change-of-variables formula (vector form).
  - For \(\eta = T(\xi)\),
    \[
    p_\eta(y) = p_\xi(T^{-1}(y))\,\bigl|\det (T^{-1})'(y)\bigr|I(y\in T(D)).
    \]
- When to use it.
  - When modeling smooth transformations of random vectors (e.g., going from Cartesian coordinates to polar, or from one linear combination of variables to another).
- Common mistakes.
  - Omitting the Jacobian determinant or forgetting the absolute value.
  - Not accounting for multiple pre-images when \(T\) is not one-to-one (then you must sum over pre-images).

## 4. Worked examples

### 4.1 Poisson approximation in a “middle-range” interval
- Setup (following Example 1.2).
  - Average rate: \(\lambda=180\) queries per hour to a server.
  - We want the distribution of the number of queries \(\xi\) in a 10-minute interval.
- Step 1: match to the Poisson process picture.
  - One hour is the “unit” interval.
  - A 10-minute interval is length \(r = 10/60 = 1/6\) of an hour.
  - The expected number of events in 10 minutes is \(r\lambda = (1/6)\cdot 180 = 30\).
- Step 2: approximate with Poisson.
  - Divide the hour into \(N\) very small subintervals; in each, a query occurs with probability about \(\lambda/N\).
  - The 10-minute interval covers \(m = rN\) small intervals, so
    \[
    \xi \sim \text{Binomial}\left(m,\frac{\lambda}{N}\right).
    \]
  - For large \(N\), \(m\) is large and \(\lambda/N\) small, with \(m\cdot(\lambda/N)=r\lambda=30\).
  - By Poisson approximation,
    \[
    P(\xi = x)\approx \frac{e^{-30}30^x}{x!},\quad x=0,1,2,\dots.
    \]
- Check your intuition.
  - The expected count in 10 minutes is 30; the Poisson model gives a distribution tightly clustered around this value, with variance also 30.
  - The approximation is good because the number of tiny opportunities is large and each has a very small probability.

### 4.2 Conditional pdf and probability in a triangular region
- Setup (from Example 2.10 and Example 2.11).
  - Joint pdf:
    \[
    p_{\xi_1,\xi_2}(x_1,x_2) = \frac{1}{x_1}I(0 < x_2 \le x_1 < 1).
    \]
  - This is supported on the triangle \(\{(x_1,x_2):0<x_2<x_1<1\}\).
- Step 1: find the marginal \(p_{\xi_1}(x_1)\).
  - Integrate over \(x_2\):
    \[
    p_{\xi_1}(x_1) = \int_0^{x_1} \frac{1}{x_1}I(0<x_1<1)\,dx_2
                   = I(0<x_1<1),
    \]
    so \(\xi_1\sim\text{Uniform}(0,1)\).
- Step 2: conditional pdf \(p_{\xi_2|\xi_1}(x_2|x_1)\).
  - Using the formula for conditional pdf:
    \[
    p_{\xi_2|\xi_1}(x_2|x_1) = \frac{p_{\xi_1,\xi_2}(x_1,x_2)}{p_{\xi_1}(x_1)}
                             = \frac{1}{x_1}I(0<x_2\le x_1<1).
    \]
  - For fixed \(x_1\in(0,1)\), this is the uniform density on \((0,x_1)\).
- Step 3: a conditional probability example.
  - Compute \(P(0<\xi_2<1/4|\xi_1=x_1)\).
  - Integrate the conditional pdf over \(x_2\in(0,1/4)\):
    \[
    P(0<\xi_2<1/4|\xi_1=x_1)
      = \int_0^{1/4} \frac{1}{x_1}I(0<x_2\le x_1<1)\,dx_2
      = \frac{\min\{1/4,x_1\}}{x_1}
      = \min\left\{1,\frac{1}{4x_1}\right\}.
    \]
  - Interpretation:
    - If \(x_1>1/4\), the conditional probability equals \((1/4)/x_1\).
    - If \(x_1\le 1/4\), then \((0,1/4)\) covers the whole range \((0,x_1)\), so the probability is 1.
- Check your intuition.
  - Once we fix \(\xi_1=x_1\), \(\xi_2\) is uniform on \((0,x_1)\). The chance that \(\xi_2\) lies in a subinterval is just relative length of that subinterval within \((0,x_1)\).

## 5. Lab/Tutorial essentials (week07.pdf)

### 5.1 What the lab asked you to do
- Problem 1: Poisson vs binomial comparison (5000 details).
  - 5000 items are tested; each fails with probability \(p=0.001\), tests are independent.
  - Find the probability that more than 1 fails using both the exact binomial distribution and the Poisson approximation.
- Problem 2: uniform distribution on the unit disk.
  - A random point in the unit disk (in \(\mathbb{R}^2\)) is chosen uniformly: joint pdf
    \[
    p_{\xi}(x,y) = \frac{1}{\pi}I(x^2+y^2<1).
    \]
  - Let \(\xi_1\) and \(\xi_2\) be the \(x\)- and \(y\)-coordinates.
  - Tasks:
    1. Find the marginal pdfs \(p_{\xi_1}\) and \(p_{\xi_2}\).
    2. Find the covariance matrix of \((\xi_1,\xi_2)\).
    3. Decide if \(\xi_1,\xi_2\) are independent and interpret your answer intuitively.
- Problem 3: conditional expectation on the unit disk.
  - For the previous question, find \(E[\xi_2|\xi_1]\), the conditional expectation of the second coordinate given the first.
- Homework problems (selected themes).
  - Poisson approximations: typos per page, raisins in cupcakes, hurricanes per year.
  - Exact binomial means and variances: Bernoulli trials (mice, truck tires).
  - Hypergeometric and combinatorial problems: drawing colored balls from urns.
  - Joint distribution on a circle: discrete distribution of an angle \(\zeta\), and transformations \(\eta=\cos\zeta\), \(\xi=\sin\zeta\), with questions about independence and correlation.
  - Correlation between counts of red cards and picture cards when sampling (with replacement) from a deck.
  - Expected sums in geometric-type stopping problems (biased die rolled until a 1 appears).

### 5.2 How to solve / approach them
- Poisson vs binomial (Problem 1).
  - Exact: use \(\xi\sim\text{Binomial}(n=5000,p=0.001)\). Compute \(P(\xi>1)=1-P(\xi=0)-P(\xi=1)\) using binomial pmf.
  - Poisson approximation: approximate \(\xi\) by \(\text{Poi}(\lambda=np=5)\) and compute \(1-P(\xi=0)-P(\xi=1)\) using Poisson pmf.
  - Compare results and note that the approximation is good because \(n\) is large, \(p\) small, and \(\lambda\) moderate.
- Uniform on unit disk (Problem 2).
  - Marginals: integrate the joint density over vertical or horizontal slices of the disk. For \(x\in(-1,1)\):
    \[
    p_{\xi_1}(x) = \int_{-\sqrt{1-x^2}}^{\sqrt{1-x^2}} \frac{1}{\pi}\,dy,
    \]
    and similarly for \(p_{\xi_2}(y)\).
  - Covariance matrix: use symmetry to argue \(E\xi_1=E\xi_2=0\), compute \(E\xi_1^2,E\xi_2^2\) by integrating \(x^2\) and \(y^2\) over the disk, and check that \(E[\xi_1\xi_2]=0\) by symmetry.
  - Independence: even though covariance is zero (uncorrelated), the marginals do not factorize the joint pdf on the disk, so \(\xi_1,\xi_2\) are not independent. Geometrically, knowing that \(x\) is large in magnitude restricts possible values of \(y\).
- Conditional expectation \(E[\xi_2|\xi_1]\) (Problem 3).
  - Given \(\xi_1=x\), \(\xi_2\) is uniform on the vertical segment in the disk at that \(x\), which runs from \(-\sqrt{1-x^2}\) to \(\sqrt{1-x^2}\).
  - Because this segment is symmetric around 0, the conditional mean of \(\xi_2\) is 0, so \(E[\xi_2|\xi_1]=0\) as a function.
- Angle and trigonometric transformations (Homework Problem 11).
  - Use the discrete pmf of \(\zeta\) to compute expectations of \(\cos\zeta\) and \(\sin\zeta\), their squares, and their product.
  - Check independence of \(\eta=\cos\zeta\) and \(\xi=\sin\zeta\) by comparing joint probabilities with products of marginals; check correlation by computing covariance and normalizing.
- Correlation between counts with replacement (Homework Problem 12).
  - Model the outcomes of each draw with indicator variables for “red” and “picture”; express \(\eta,\xi\) as sums of these indicators over \(K\) draws.
  - Use linearity of expectation and covariance formulas to get the correlation coefficient.

### 5.3 Mini practice
- Practice 1: choosing between binomial and Poisson.
  - Question: A factory produces items; each fails with probability \(0.002\) independently. You test 4000 items. Which model is better to approximate “number of failures”: binomial or Poisson?
  - Brief answer: The exact model is \(\text{Binomial}(4000,0.002)\), but because \(n\) is large and \(p\) small with \(\lambda=np=8\), Poisson\((8)\) is a good approximation.
- Practice 2: independence and geometry on a disk.
  - Question: For a point chosen uniformly on the unit disk, are the coordinates independent?
  - Brief answer: No. Knowing \(x\) close to 1 forces \(|y|\) to be small (since \(x^2+y^2<1\)); this geometric constraint means the joint density does not factor as a product of marginals.
- Practice 3: conditional expectation symmetry.
  - Question: In the same unit disk setup, what is \(E[Y|X=x]\)?
  - Brief answer: 0, because for a fixed \(x\), \(Y\) is uniformly distributed on a symmetric interval \([- \sqrt{1-x^2}, \sqrt{1-x^2}]\).

## 6. Quick recap
- The Poisson distribution arises as the limit of binomial counts when the number of trials is large and success probability is small, and as the natural count distribution in Poisson process models.
- Continuous random vectors are described by joint pdfs; marginal densities are obtained by integrating over other variables, and independence is characterized by factorization of the joint pdf into marginals.
- Uniform random vectors on regions and multivariate normal vectors are important examples, with the latter transforming nicely under linear maps.
- Conditional pdfs and expectations for continuous variables generalize discrete ideas and allow you to compute probabilities and means under conditions like “given \(\xi_1=x_1\)”.
- Joint densities transform under smooth invertible changes of variables via the Jacobian determinant, both in one and multiple dimensions.
- The week 7 lab connects Poisson approximations to practical problems and uses geometric joint densities (like the unit disk) to practice finding marginals, covariances, dependence, and conditional expectations.


[<kbd><br><- Return (ProbStat)<br></kbd>](ProbStat.md)
