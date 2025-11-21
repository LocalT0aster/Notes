# CSE206 — Week 01 Notes — Descriptive stats (mean/median/SD, plots)
**Lectures:** CSE206_Fa24-01.pdf
**Lab/Tutorial:** week01.pdf

## 1. Big picture (5–10 bullets)
- Probability gives a precise mathematical way to talk about uncertainty in models of the real world.
- Statistics uses data (observations) to learn about the unknown “state of nature” behind those models.
- We describe data sets using descriptive statistics: measures of location (center) and measures of scattering (spread).
- The sample mean, median, and quantiles are different ways to say “where the data sit” on the number line.
- The sample standard deviation and mean absolute deviation describe how tightly or loosely data are clustered.
- Dot plots and histograms are visual tools to see the overall shape of a data set (center, spread, skewness, outliers).
- Outliers are atypical data points that can strongly influence the mean and standard deviation, but much less the median.
- The lab for week 1 gives practice computing these summaries, drawing dot plots and histograms, and comparing two groups.

## 2. Key concepts and definitions

### 2.1 Probability vs statistics
- Plain-language definition.
  - Probability is a branch of mathematics that encodes uncertainty and lets us compute chances of events under a model.
  - Statistics uses observed data to infer the unknown parameters or probabilities that define that model.
- Formal definition (if needed).
  - In probability, we assume a probability model is known: basic events have assigned probabilities, and we derive the probabilities of more complex events from them.
  - In statistics, we treat those probabilities or parameters as unknown and use data samples to estimate or test them.
- Intuition / mental model.
  - Probability: “If I know how the world works, what is the chance of this outcome?” (e.g., probability of five heads in a row for a fair coin).
  - Statistics: “From what I have observed, what can I say about how the world works?” (e.g., is this coin fair given the toss results?).
- Tiny example.
  - Probability question: assuming a fair coin, how likely is it that heads appears nearly half the time in many tosses?
  - Statistics question: I tossed a coin ten times and got eight heads; can I reasonably claim the coin is not fair?

### 2.2 State of nature, observations, and samples
- Plain-language.
  - The state of nature is the underlying reality or mechanism that generates data.
  - Observations are the actual values we record from that mechanism; the collection of observed values is a sample.
- Formal definition (if needed).
  - We assume there is an unknown probability distribution describing the phenomenon.
  - A sample is a finite sequence of real numbers \(x_1, \dots, x_n\) drawn from that distribution.
- Intuition / mental model.
  - Think of the state of nature as the complete list of all possible outputs, which we can never fully see, and the sample as a small subset we actually measure.
  - Examples from the lecture: all possible responses of a large AI model, all heights in a city, or all device lifetimes from a factory.
- Tiny example.
  - Population heights: the true heights of everyone in Kazan form the state of nature; the thousand peoe you measure in a study form your sample.

### 2.3 Sample mean (measure of location)
- Plain-language definition.
  - The sample mean is the average value of the data; it is one way to describe the center of a sample.
- Formal definition (if needed).
  - For a sample \(\{x_1, \dots, x_n\}\), the sample mean is
    \[
    \bar{x} = \frac{1}{n}\sum_{j=1}^n x_j.
    \]
  - It is the unique number \(\mu\) for which \(\sum_{j=1}^n (x_j - \mu) = 0\).
- Intuition / mental model.
  - Imagine the data points as weights on a number line; the mean is the balance point where the system is in equilibrium.
  - It is very sensitive to extreme values (outliers), because every data point enters the sum directly.
- Tiny example.
  - If reaction times in a tiny sample are \(180, 220, 200\) milliseconds, then
    \(\bar{x} = (180 + 220 + 200)/3 = 200\) ms.

### 2.4 Median and quantiles (more location measures)
- Plain-language definition.
  - The median is the “middle” value of an ordered sample.
  - Quantiles (such as quartiles) mark positions that split the ordered data into fixed fractions (like quarters).
- Formal definition (if needed).
  - Reorder the sample into an increasing sequence \(y_1 \le \dots \le y_n\).
  - If \(n\) is odd, the median \(m\) is \(y_{(n+1)/2}\).
  - If \(n\) is even, the median is
    \[
    m = \frac{y_{n/2} + y_{n/2 + 1}}{2}.
    \]
  - For a positive integer \(q\), the \(k\)-th \(q\)-quantile is the value \(y_j\) such that roughly \(k/q\) of the values lie below \(y_j\) and the rest above it.
- Intuition / mental model.
  - The median is a center that is robust: moving a few extreme points far away does not change it much, as long as the order around the middle stays the same.
  - Quartiles cut the ordered data into four blocks of equal size and help describe spread and skewness.
- Tiny example.
  - For the ordered data \( \{1, 3, 5, 9, 10\} \) (\(n = 5\)), the median is the third value: \(m = 5\).
  - For \(\{1, 3, 5, 9\}\) (\(n = 4\)), the median is \((3 + 5)/2 = 4\).

### 2.5 Standard deviation and mean absolute deviation (measures of scattering)
- Plain-language definition.
  - The standard deviation measures how far, on average in a squared sense, data points are from the mean.
  - The mean absolute deviation (m.a.d.) measures how far, on average, data points are from the mean using absolute distances.
- Formal definition (if needed).
  - For a sample \(\{x_1, \dots, x_n\}\) with mean \(\bar{x}\), the (sample) standard deviation is
    \[
    s = \sqrt{\frac{1}{n - 1}\sum_{j=1}^n (x_j - \bar{x})^2}.
    \]
  - The mean absolute deviation is
    \[
    \text{m.a.d.} = \frac{1}{n}\sum_{j=1}^n |x_j - \bar{x}|.
    \]
  - The sample variance is \(s^2\), the square of the standard deviation.
- Intuition / mental model.
  - Both numbers describe how “together” or “spread out” the data are, but standard deviation penalizes large deviations more strongly because of the square.
  - Standard deviation and m.a.d. are insensitive to adding a constant to all data (a shift), but they scale when all data are multiplied by a constant.
- Tiny example.
  - If a small sample is \(\{9, 10, 11\}\), then \(\bar{x} = 10\).
  - The deviations are \(-1, 0, +1\); the m.a.d. is \((1 + 0 + 1)/3 = 2/3\).
  - The standard deviation is \(\sqrt{[(1^2 + 0^2 + 1^2)/(3 - 1)]} = \sqrt{1} = 1\).

### 2.6 Dot plots and histograms (data representation)
- Plain-language definition.
  - A dot plot places a dot for each data point in one of several equal-width cells along the horizontal axis.
  - A histogram uses rectangles over those cells; the height of each rectangle is the frequency (or relative frequency) of data in that cell.
- Formal definition (if needed).
  - Let \(x_{\min}\) and \(x_{\max}\) be the minimum and maximum data values.
  - Choose a number of cells \(N\) and partition \([x_{\min}, x_{\max}]\) into \(N\) subintervals of equal length.
  - Dot plot: for each subinterval, draw a column of dots, one per data point in that interval.
  - Histogram: for each subinterval, draw a rectangle with base the subinterval and height equal to the number of data points (or relative frequency) in that interval.
- Intuition / mental model.
  - Dot plots are very clear for small to moderate samples: you can see each point and where it falls.
  - Histograms are better for large samples, letting you see overall shape (e.g., symmetric, skewed, multimodal) without tracking individual values.
- Tiny example.
  - For the sample \(\{10, -2, -4.5, -7.8, -1, 0, 0, 0, 3, 3, 0, 5, -1, 0, -2, -2, -7.7, 10, 10, 11, -2, -3\}\) from the lecture, the instructor shows dot plots and histograms that change shape when the number of cells \(N\) changes.

### 2.7 Outliers and empirical distribution function
- Plain-language definition.
  - Outliers are data points that look atypical or far from the bulk of the sample.
  - The empirical distribution function (EDF), denoted \(F_{\text{emp}}(x)\), describes, for each \(x\), the proportion of data values that are \(\le x\).
- Formal definition (if needed).
  - For a sample \(\{x_1, \dots, x_n\}\), the EDF is
    \[
    F_{\text{emp}}(x) = \frac{1}{n}\#\{ j \in \{1, \dots, n\} : x_j \le x\}.
    \]
  - Outliers are not defined by a single formula in the lecture; their identification depends on the underlying state of nature and context.
- Intuition / mental model.
  - \(F_{\text{emp}}(x)\) is a step function that jumps up by \(1/n\) at each data point; it shows how the sample “accumulates” as \(x\) increases.
  - Outliers may lie outside a range such as \((\bar{x} - s, \bar{x} + s)\), but in many real problems this simple rule can mislead, so context is crucial.
- Tiny example.
  - For the sample \(\{22, 24, 35, 1, 1, 5, 6, 10, 13, 21, 10, 10, 40, 41, 47\}\) from the lecture, \(F_{\text{emp}}(x)\) is \(0\) for \(x < 1\), jumps to \(2/15\) at \(x = 1\), and eventually reaches \(1\) after the largest value \(47\).

## 3. Core formulas and how to use them

### 3.1 Sample mean
- Formula.
  - \[
    \bar{x} = \frac{1}{n}\sum_{j=1}^n x_j.
    \]
- Symbols.
  - \(x_1, \dots, x_n\): observed data values (the sample).
  - \(n\): sample size.
  - \(\bar{x}\): sample mean (average).
- When to use it.
  - To summarize the central tendency of quantitative data when you are not too worried about extreme values.
  - In many later results in probability and statistics, the sample mean is a basic building block.
- Common mistakes.
  - Forgetting to divide by \(n\) after summing.
  - Using rounded intermediate sums that cause unnecessary rounding error.
  - Treating the mean as robust to outliers (it is not).

### 3.2 Median and quantiles
- Formula / definition.
  - Order the data: \(y_1 \le \dots \le y_n\).
  - Median \(m\):
    - If \(n\) is odd, \(m = y_{(n+1)/2}\).
    - If \(n\) is even, \(m = (y_{n/2} + y_{n/2+1})/2\).
  - First and third quartiles are special quantiles located at roughly 25% and 75% positions in the ordered list.
- Symbols.
  - \(y_j\): \(j\)-th ordered value of the sample.
  - \(n\): sample size.
  - \(m\): sample median.
- When to use it.
  - To describe the center of data sets with clear skewness or outliers, where the mean might be misleading.
  - To split the data into parts and reason about where most values lie.
- Common mistakes.
  - Forgetting to order the data before taking the middle.
  - Miscounting indices when \(n\) is even.
  - Confusing median (position-based) with mean (value-based).

### 3.3 Trimmed mean (used in the lab)
- Formula / definition.
  - For a \(p\%\) trimmed mean:
    1. Order the data.
    2. Remove the smallest \(p\%\) and largest \(p\%\) of observations.
    3. Take the ordinary mean of the remaining data.
  - The lab uses a \(10\%\) trimmed mean.
- Symbols.
  - \(p\): trimming percentage.
  - \(n\): sample size; \(pn\) (rounded appropriately) observations are trimmed from each tail.
- When to use it.
  - When you want a measure of center that behaves like the mean but is less sensitive to a few extreme values.
  - To check whether outliers are heavily influencing the plain mean by comparing mean vs trimmed mean vs median.
- Common mistakes.
  - Forgetting to sort the data before trimming.
  - Removing the wrong number of observations from each tail.
  - Mixing up which data remain after trimming when computing the average.

### 3.4 Standard deviation and variance
- Formula.
  - Standard deviation:
    \[
    s = \sqrt{\frac{1}{n - 1}\sum_{j=1}^n (x_j - \bar{x})^2}.
    \]
  - Variance:
    \[
    s^2 = \frac{1}{n - 1}\sum_{j=1}^n (x_j - \bar{x})^2.
    \]
- Symbols.
  - \(x_j\): data points.
  - \(\bar{x}\): sample mean.
  - \(n\): sample size.
  - \(s\): sample standard deviation.
  - \(s^2\): sample variance.
- When to use it.
  - To measure spread around the mean and compare variability between samples (e.g., control vs treatment groups in the lab).
  - As input to many later statistical procedures (confidence intervals, tests, etc.).
- Common mistakes.
  - Using \(n\) instead of \(n - 1\) when the formula is defined with \(n - 1\) in the lecture.
  - Forgetting to square the deviations before summing.
  - Taking the square root too early or forgetting it when going from variance to standard deviation.

### 3.5 Mean absolute deviation (m.a.d.)
- Formula.
  - \[
    \text{m.a.d.} = \frac{1}{n}\sum_{j=1}^n |x_j - \bar{x}|.
    \]
- Symbols.
  - \(x_j\): data points.
  - \(\bar{x}\): sample mean.
  - \(n\): sample size.
  - \(|\cdot|\): absolute value.
- When to use it.
  - When you want a measure of spread that treats all deviations linearly instead of squaring them.
  - As a way to see how much data typically differ from the mean without giving extra emphasis to outliers.
- Common mistakes.
  - Confusing m.a.d. with standard deviation; they are different quantities.
  - Forgetting to take absolute values before summing.

### 3.6 Empirical distribution function (EDF)
- Formula.
  - \[
    F_{\text{emp}}(x) = \frac{1}{n}\#\{ j \in \{1, \dots, n\} : x_j \le x\}.
    \]
- Symbols.
  - \(x\): point on the horizontal axis where we evaluate the function.
  - \(x_j\): data points.
  - \(n\): sample size.
  - \(\#\{\cdot\}\): number of elements in the set.
- When to use it.
  - To visualize how the sample accumulates as values increase.
  - To connect sample behavior with quantiles (e.g., where \(F_{\text{emp}}\) crosses 0.25, 0.5, 0.75).
- Common mistakes.
  - Counting only strictly less than instead of “less than or equal”, which changes the step locations.
  - Forgetting to divide by \(n\), giving counts instead of proportions.

## 4. Worked examples

### 4.1 Effect of a single extreme value on mean, median, standard deviation, and m.a.d.
- Setup.
  - From the lecture: suppose we have one thousand data points, one of which is \(1000\) and all the rest are \(0\).
  - So the sample is \(x_1, \dots, x_{1000}\) with 999 zeros and a single 1000.
- Step 1: compute the sample mean.
  - The sum of all values is \(1000 + 0 + \dots + 0 = 1000\).
  - The sample size is \(n = 1000\).
  - The mean is
    \[
    \bar{x} = \frac{1000}{1000} = 1.
    \]
- Step 2: compute the median.
  - Order the data: 999 zeros, then one 1000 at the end.
  - For \(n = 1000\), the median is the average of the 500th and 501st ordered values.
  - Both the 500th and 501st values are 0, so the median is
    \[
    m = \frac{0 + 0}{2} = 0.
    \]
- Step 3: compute the standard deviation.
  - Deviations from the mean: 999 values equal to \((0 - 1) = -1\), and one value equal to \((1000 - 1) = 999\).
  - Sum of squared deviations:
    \[
    \sum_{j=1}^{1000} (x_j - \bar{x})^2 = 999^2 + 999 \cdot 1^2 = 999 \cdot 1000 = 999000.
    \]
  - The standard deviation is
    \[
    s = \sqrt{\frac{999000}{1000 - 1}} = \sqrt{\frac{999000}{999}} = \sqrt{1000} \approx 31.6.
    \]
- Step 4: compute the mean absolute deviation.
  - Absolute deviations: \(|1000 - 1| = 999\), and 999 copies of \(|0 - 1| = 1\).
  - Sum of absolute deviations is \(999 + 999 \cdot 1 = 1998\).
  - m.a.d. is
    \[
    \text{m.a.d.} = \frac{1998}{1000} = 1.998.
    \]
- Check your intuition.
  - The mean (1) lies close to the many zeros but is pulled away by the single large value.
  - The median (0) completely ignores the extreme 1000.
  - The standard deviation is very large because the squared deviation of 999 dominates.
  - The m.a.d. is closer in size to the mean and much smaller than the standard deviation.

### 4.2 Empirical distribution function and quantiles
- Setup.
  - From the lecture, consider the sample
    \(\{22, 24, 35, 1, 1, 5, 6, 10, 13, 21, 10, 10, 40, 41, 47\}\).
  - There are \(n = 15\) observations.
- Step 1: order the data.
  - Ordered sample: \(\{1, 1, 5, 6, 10, 10, 10, 13, 21, 22, 24, 35, 40, 41, 47\}\).
- Step 2: compute \(F_{\text{emp}}(x)\) at a few points.
  - For \(x < 1\), no observations are \(\le x\), so \(F_{\text{emp}}(x) = 0\).
  - At \(x = 1\), two observations are \(\le 1\), so
    \[
    F_{\text{emp}}(1) = \frac{2}{15}.
    \]
  - At \(x = 10\), seven observations are \(\le 10\), so
    \[
    F_{\text{emp}}(10) = \frac{7}{15}.
    \]
  - For any \(x\) between 41 and 47 (but less than 47), 14 observations are \(\le x\), so \(F_{\text{emp}}(x) = 14/15\).
  - For \(x \ge 47\), all 15 observations are \(\le x\), so \(F_{\text{emp}}(x) = 1\).
- Step 3: relate to quantiles.
  - The median is the 8th ordered value (since \(n = 15\)), which is \(13\).
  - At \(x = 13\), exactly 8 observations are \(\le 13\), so
    \[
    F_{\text{emp}}(13) = \frac{8}{15} \approx 0.53.
    \]
  - This is just above 0.5, consistent with the interpretation of the median as the 50%-quantile.
- Check your intuition.
  - As \(x\) moves along the horizontal axis, the EDF jumps up by \(1/15\) at each data point.
  - Reading off approximate levels like 0.25, 0.5, and 0.75 on the vertical axis helps locate quartiles and median.

## 5. Lab/Tutorial essentials (week01.pdf)

### 5.1 What the lab asked you to do
- Problem 1 (Walpole 1.2): reaction time of 20 amateur racers.
  - Compute the sample mean and sample median of the reaction-time data.
  - Compute the 10% trimmed mean.
  - Draw a dot plot of the data.
  - Compare mean, median, and trimmed mean to discuss possible outliers.
- Problem 2 (Walpole 1.5 and 1.11): effect of regular exercise on cholesterol.
  - Data are changes in cholesterol levels for a control and a treatment group.
  - Draw a dot plot for both groups on the same graph.
  - Compute mean, median, and 10% trimmed mean for each group.
  - Explain why the mean difference suggests one conclusion while median/trimmed mean suggest another.
  - Compute sample variance and sample standard deviation for each group.
- Problem 3 (Walpole 1.13): battery lifetime data (hours).
  - Compute sample mean and median.
  - Identify which value causes a substantial difference between mean and median.
  - Recalculate the mean without that value and compare.
- Problem 4 (Walpole 1.17): time to fall asleep for smokers (A) and nonsmokers (B).
  - Compute sample mean and sample standard deviation for each group.
  - Draw a dot plot for both groups on the same line.
  - Comment on how smoking appears to affect time to fall asleep.
- Problem 5 (Walpole 1.18): final exam scores in an elementary statistics course.
  - Construct a relative frequency histogram.
  - Sketch a smooth curve that approximates the distribution and discuss skewness.
  - Compute sample mean, sample median, and sample standard deviation.
- Problem 6 (Walpole 1.20): lifetime (seconds) of 50 fruit flies under a new spray.
  - Set up a relative frequency distribution.
  - Construct a relative frequency histogram.
  - Find the median.
- Problem 7: complete the Colab notebook linked at the end of the lab (practice using Python/Colab for descriptive statistics).

### 5.2 How to solve / approach them
- Computing means, medians, trimmed means.
  - Sum all values and divide by the sample size to get the mean.
  - Sort the data; take the middle value(s) to find the median.
  - For a 10% trimmed mean, sort the data, remove the smallest and largest 10% of observations, then compute the mean of what remains.
- Dot plots and histograms.
  - For dot plots, choose a horizontal axis that covers all data, split into equal-width cells, and place a dot in the appropriate cell for each observation.
  - For histograms, count how many observations fall in each cell (frequency) or divide by the total number of observations (relative frequency), then draw rectangles with those heights.
  - When comparing two groups (e.g., control vs treatment, smokers vs nonsmokers), plot them on the same axis to compare centers, spreads, and outliers visually.
- Interpreting outliers and robustness.
  - If the mean, median, and trimmed mean are close, there is little evidence of strong outliers.
  - If the mean is far away from the median and trimmed mean, this suggests that a few extreme values may be pulling the mean.
  - Recomputing the mean after removing a suspected extreme value is a way (used in the lab) to see how influential it is.
- Comparing groups with descriptive statistics.
  - For cholesterol and sleep-time problems, compare means to see differences in average level between groups.
  - Compare medians and trimmed means to see whether group differences are robust to outliers.
  - Compare standard deviations to see which group has more variability.
  - When commenting on “impact” (e.g., of smoking or treatment), base your reasoning on these differences and on the plots (dot plots, histograms).
- Relative frequency distributions and skewness.
  - To build a relative frequency distribution, define class intervals (bins), count how many observations fall in each, and divide by the total number of observations.
  - Plot these relative frequencies as a histogram and inspect whether the distribution is symmetric, right-skewed (long tail to the right), or left-skewed.
  - Use the shape to interpret how the bulk of the data and extreme values behave.

### 5.3 Mini practice
- Practice 1: mean vs median vs outlier.
  - Question: Consider a data set of 9 exam scores where 8 scores are between 60 and 80, and one score is 10. Which measure of center (mean or median) is more affected by the single low score?
  - Brief answer: The mean is much more affected, because it averages all values; the median depends only on the order and usually stays near the middle of the bulk of the data.
- Practice 2: interpreting a dot plot of two groups.
  - Question: In a dot plot, group A’s dots are mostly clustered tightly around 0 with a few large positive values, while group B’s dots are spread more evenly from negative to positive values. Which group likely has larger standard deviation, and what might that mean?
  - Brief answer: Group B likely has a larger standard deviation, indicating more variability in its measurements. Group A has a tighter core but a few outliers.
- Practice 3: trimmed mean reasoning.
  - Question: You compute a mean of 20 for a sample, but the 10% trimmed mean and the median are both close to 15. What does this suggest about the data?
  - Brief answer: It suggests there are some extreme high values that pull the plain mean upward; trimming and using the median reduce their influence and give a center near 15.

## 6. Quick recap
- Probability assumes a model with known probabilities and computes chances of events; statistics uses data to infer those unknown probabilities or parameters.
- The state of nature is the underlying reality (or probability distribution); a sample is the finite list of observed values.
- The sample mean \(\bar{x} = \frac{1}{n}\sum x_j\) is a natural measure of center but is sensitive to outliers.
- The median and other quantiles are location measures based on ordered positions and are more robust to extreme values.
- The sample standard deviation \(s\) and variance \(s^2\) measure how spread out the data are around the mean, with large deviations heavily weighted.
- The mean absolute deviation measures spread using absolute distances and usually gives a smaller value than the standard deviation for the same data.
- Dot plots and histograms turn raw data into visual summaries that reveal center, spread, skewness, and potential outliers.
- Outliers are atypical points whose importance must be judged in context; simple rules based on \((\bar{x} - s, \bar{x} + s)\) can be misleading.
- The empirical distribution function \(F_{\text{emp}}(x)\) counts the proportion of observations \(\le x\) and connects the sample to quantiles like the median.
- The week 1 lab reinforces these ideas by having you compute means, medians, trimmed means, standard deviations, draw dot plots and histograms, and interpret differences between groups.


[<kbd><br><- Return (ProbStat)<br></kbd>](ProbStat.md)
