# CSE206 — Week 02 Notes — Probability basics (Kolmogorov, combinatorial/geometric, independence, Bayes)
**Lectures:** CSE206_Fa24-02.pdf
**Lab/Tutorial:** week02.pdf

## 1. Big picture (5–10 bullets)
- This week introduces the formal mathematical foundations of probability using Kolmogorov’s axioms.
- We define sample spaces, events, σ-algebras, and probability measures as the basic building blocks of any probability model.
- We learn combinatorial and geometric probability: computing probabilities by counting outcomes or comparing areas/volumes.
- The key concept of independence is formalized, including pairwise vs mutual independence, and practical examples.
- Conditional probability is defined and interpreted as “probability after learning that B occurred”.
- The formula of total probability and Bayes’ formula link basic probabilities with conditional ones and “hypotheses”.
- The lab reinforces these ideas with many exercises on combinatorial probability, conditional probability, Bayes’ rule, and independence.
- Throughout, the emphasis is on clearly specifying the underlying probability space when problems become tricky.

## 2. Key concepts and definitions

### 2.1 Sample space, events, and σ-algebra
- Plain-language definition.
  - The sample space, usually written $\Omega$, is the set of all possible outcomes of an experiment.
  - An event is a subset of $\Omega$; it represents a statement about the outcome that can either occur or not.
  - A σ-algebra (σ-field) $\mathcal{F}$ is a collection of subsets of $\Omega$ that we are allowed to treat as events.
- Formal definition (if needed).
  - Sample space: $\Omega$ is a nonempty set (for example, $\{H, T\}$ when tossing one coin).
  - Event: any element of $\mathcal{F} \subseteq 2^\Omega$.
  - σ-algebra $\mathcal{F}$ satisfies:
    1. $\varnothing \in \mathcal{F}$.
    2. If $A \in \mathcal{F}$, then its complement $A^c = \Omega \setminus A \in \mathcal{F}$.
    3. If $A_1, A_2, \dots \in \mathcal{F}$, then $\bigcup_{j=1}^\infty A_j \in \mathcal{F}$.
- Intuition / mental model.
  - $\Omega$ lists everything that can happen; $\mathcal{F}$ lists exactly which questions (“events”) we are allowed to assign probabilities to.
  - In simple finite examples we usually take $\mathcal{F} = 2^\Omega$ (all subsets), but for infinite $\Omega$ that is often too large or not practical.
- Tiny examples.
  - One coin toss: $\Omega = \{H, T\}$. Events include $\{H\}$ (“heads”), $\{T\}$ (“tails”), $\Omega$ (“certain event”), and $\varnothing$ (“impossible event”).
  - Two coin tosses: $\Omega = \{HH, HT, TH, TT\}$. Event “exactly one head” is $\{HT, TH\}$.
  - Urn of balls: if there are balls $B_1, B_2, R_1, R_2, R_3$, then $\Omega = \{B_1, B_2, R_1, R_2, R_3\}$ for one draw. For two ordered draws, $\Omega$ is the set of ordered pairs like $(B_1, R_1)$.

### 2.2 Probability measure and probability space
- Plain-language definition.
  - A probability measure $P$ assigns to each event a number between 0 and 1 that represents how likely it is.
  - A probability space is the triple $(\Omega, \mathcal{F}, P)$ that fully describes a probability model.
- Formal definition (if needed).
  - A probability measure is a function $P : \mathcal{F} \to [0,1]$ such that:
    1. $P(\varnothing) = 0$.
    2. $P(\Omega) = 1$.
    3. If $A_1, A_2, \dots$ are pairwise disjoint (mutually exclusive) events, then
       $$
       P\Bigl(\bigcup_{j=1}^\infty A_j\Bigr) = \sum_{j=1}^\infty P(A_j).
       $$
  - A probability space is the triple $(\Omega, \mathcal{F}, P)$.
- Intuition / mental model.
  - $\Omega$ and $\mathcal{F}$ specify “what can happen”; $P$ specifies how likely each event is.
  - In many textbook questions the probability space is not written explicitly, but if you get stuck, writing down $\Omega$, $\mathcal{F}$, and $P$ often clarifies the situation.
- Tiny example.
  - Tossing a fair coin twice: $\Omega = \{HH, HT, TH, TT\}$, $\mathcal{F} = 2^\Omega$, and
    $$
    P(\{\omega\}) = \frac{1}{4} \quad \text{for each } \omega \in \Omega.
    $$
  - From this and additivity, you can compute probabilities of events such as “at least one head”.

### 2.3 Combinatorial probability (finite uniform spaces)
- Plain-language definition.
  - In many simple problems with a finite number of equally likely outcomes, the probability of an event is “favorable outcomes divided by total outcomes”.
- Formal definition (if needed).
  - Suppose $\Omega = \{\omega_1,\dots,\omega_n\}$, $\mathcal{F} = 2^\Omega$, and $P(\{\omega_j\}) = 1/n$ for all $j$. For any event $E \subseteq \Omega$,
    $$
    P(E) = \frac{\#E}{n},
    $$
    where $\#E$ is the number of elements in $E$.
- Intuition / mental model.
  - Many card, dice, and urn problems fall into this pattern: identify the sample space of equally likely outcomes and then count.
  - Counting relies on permutations and combinations:
    - $n!$ is the number of ways to order $n$ distinct items.
    - $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ counts subsets of size $k$ from $n$ distinct items.
- Tiny example.
  - Toss a fair die twice. The sample space has 36 equally likely outcomes $(1,1), (1,2), \dots, (6,6)$.
  - The event “sum is prime” (from the lecture) is obtained by counting the pairs with sum equal to 2, 3, 5, 7, 11, or 13 and dividing by 36.

### 2.4 Geometric probability
- Plain-language definition.
  - Geometric probability treats outcomes as points in a region of the plane (or space), and events as subregions.
  - The probability of the event is the ratio of the subregion’s area (or length/volume) to the total region’s area (or length/volume).
- Formal definition (if needed).
  - Let $\Omega$ be a region (for example, a square in $\mathbb{R}^2$) and let $E \subseteq \Omega$ be a subregion.
  - If all points of $\Omega$ are equally likely, then
    $$
    P(E) = \frac{\text{area}(E)}{\text{area}(\Omega)}.
    $$
- Intuition / mental model.
  - Instead of counting discrete outcomes we “measure” regions.
  - Many problems about random times, random lengths, or random points in an interval or square can be solved by drawing a picture and computing an area.
- Tiny example (from the lecture).
  - Two numbers $x,y$ are chosen at random in $[0,1]$. $\Omega$ is the unit square with corners $(0,0), (0,1), (1,0), (1,1)$.
  - The condition that $x,y,1$ form side lengths of a triangle reduces (since $x,y \le 1$) to $x + y \ge 1$.
  - The event region is
    $$
    R = \{(x,y)\in \Omega : x + y \ge 1\},
    $$
    a right triangle of area $1/2$. Hence $P(\text{triangle}) = 1/2$.

### 2.5 Independence (pairwise vs mutual)
- Plain-language definition.
  - Two events $A$ and $B$ are independent if learning that one occurred does not change the probability of the other.
  - For more than two events, mutual independence means every subcollection behaves like that: the probability that all events in the subcollection occur equals the product of their individual probabilities.
- Formal definition (if needed).
  - Two events $A,B$ are independent if
    $$
    P(A \cap B) = P(A)P(B).
    $$
  - Events $A_1,\dots,A_n$ are mutually independent if for any subcollection $A_{j_1},\dots,A_{j_k}$ (with $1 \le k \le n$) we have
    $$
    P(A_{j_1}\cap \dots \cap A_{j_k}) = P(A_{j_1})\dots P(A_{j_k}).
    $$
  - They are pairwise independent if every pair $A_i,A_j$ (with $i\ne j$) satisfies $P(A_i \cap A_j) = P(A_i)P(A_j)$.
- Intuition / mental model.
  - Independence means “no information flow”: knowing $A$ occurred does not change the odds of $B$.
  - Mutual independence is much stronger than pairwise independence; pairwise independence alone does not guarantee that every triple, quadruple, etc., is independent.
- Tiny example from the lecture.
  - Let $\Omega = \{\omega_1, \omega_2, \omega_3, \omega_4\}$ with each point having probability $1/4$.
  - Define $A = \{\omega_1,\omega_2\}$, $B = \{\omega_2,\omega_3\}$, $C = \{\omega_1,\omega_3\}$.
  - It can be checked that each pair is independent, but $A \cap B \cap C = \varnothing$, so
    $$
    P(A\cap B\cap C) = 0 \ne P(A)P(B)P(C),
    $$
    so mutual independence fails.

### 2.6 Conditional probability, total probability, and Bayes’ formula
- Plain-language definition.
  - The conditional probability $P(A|B)$ is the probability of $A$ after we are told that event $B$ has occurred.
  - The formula of total probability expresses the probability of an event by splitting according to a partition of the sample space.
  - Bayes’ formula gives the probability of a “cause” or hypothesis $B_j$ given an observed outcome $A$.
- Formal definitions (if needed).
  - Conditional probability (for $P(B) > 0$):
    $$
    P(A|B) = \frac{P(A\cap B)}{P(B)}.
    $$
  - Total probability: if $B_1,\dots,B_n$ are pairwise disjoint and $B = B_1\cup\dots\cup B_n$, then for any event $A$
    $$
    P(A\cap B) = \sum_{j=1}^n P(A\cap B_j).
    $$
    If in addition $A \subset B$, then $P(A) = \sum_{j=1}^n P(A\cap B_j)$.
  - Bayes’ formula: for pairwise disjoint events $B_1,\dots,B_n$ with $A \subset B_1\cup\dots\cup B_n$,
    $$
    P(B_j|A) = \frac{P(A|B_j)P(B_j)}{P(A|B_1)P(B_1)+\dots+P(A|B_n)P(B_n)}.
    $$
- Intuition / mental model.
  - Conditional probability narrows our “universe” to $B$; we then compare how much of $B$ also lies in $A$.
  - Total probability says: if the world is split into scenarios $B_1,\dots,B_n$, then the chance of $A$ is the weighted sum of the chances of $A$ in each scenario.
  - Bayes’ formula updates our belief about which scenario $B_j$ actually occurred once we observe $A$.
- Tiny examples from lecture and lab.
  - Fair coin tossed three times: define $A$ = “last two tosses are same”, $B$ = “last toss is heads”. Then $P(A|B)$ is computed as (number of outcomes where last is H and last two are same)/(number of outcomes where last is H).
  - Lecture example: 100 coins, one double-tailed, 99 honest. After seeing 10 tails in a row, Bayes’ formula gives a high probability that we picked the unfair coin.

## 3. Core formulas and how to use them

### 3.1 Kolmogorov axioms (probability measure)
- Formula / properties.
  - For a probability measure $P : \mathcal{F}\to[0,1]$:
    - $P(\varnothing) = 0$.
    - $P(\Omega) = 1$.
    - If $A_1,A_2,\dots$ are pairwise disjoint,
      $$
      P\Bigl(\bigcup_{j=1}^\infty A_j\Bigr) = \sum_{j=1}^\infty P(A_j).
      $$
  - From these, it follows that if $A \subseteq B$ then $P(A) \le P(B)$.
- Symbols.
  - $\Omega$: sample space.
  - $\mathcal{F}$: σ-algebra of events.
  - $P$: probability measure.
  - $A_j$: events.
- When to use it.
  - To check whether a function can be a valid probability measure.
  - To derive rules such as $P(A^c) = 1 - P(A)$ and monotonicity ($A \subseteq B \Rightarrow P(A) \le P(B)$).
- Common mistakes.
  - Forgetting that countable additivity is only guaranteed for disjoint events.
  - Treating probabilities as if they can exceed 1 or be negative.

### 3.2 Combinatorial probability formula
- Formula.
  - In a finite uniform probability space with $n$ equally likely outcomes, the probability of event $E$ is
    $$
    P(E) = \frac{\#E}{n}.
    $$
- Symbols.
  - $\#E$: number of outcomes favorable to event $E$.
  - $n$: total number of possible outcomes.
- When to use it.
  - In dice, cards, urns, and similar problems where all elementary outcomes are equally likely.
  - Combined with counting tools $n!$ and $\binom{n}{k}$.
- Common mistakes.
  - Using the formula when outcomes are not equally likely.
  - Miscounting the size of the sample space or the event (forgetting order vs no order).

### 3.3 Inclusion–exclusion principle
- Formula (for two events).
  - For events $A$ and $B$,
    $$
    P(A\cup B) = P(A) + P(B) - P(A\cap B).
    $$
- Formula (general version mentioned in lecture).
  - For events $A_1,\dots,A_n$,
    $$
    P\Bigl(\bigcup_{j=1}^n A_j\Bigr) = \sum_j P(A_j)
       - \sum_{i<j} P(A_i\cap A_j)
       + \sum_{i<j<k} P(A_i\cap A_j\cap A_k) - \dots + (-1)^{n+1}P(A_1\cap \dots \cap A_n).
    $$
- Symbols.
  - $A_i$: events.
  - $P(A_i)$, $P(A_i\cap A_j)$, etc.: probabilities of single, double, triple intersections, etc.
- When to use it.
  - When computing the probability that at least one among many events occurs, especially when events overlap in complicated ways (e.g., derangements problem in the tutorial).
- Common mistakes.
  - Forgetting to subtract intersections (double-counting).
  - Stopping the inclusion–exclusion series too early without justification.

### 3.4 Independence
- Formula.
  - Two events $A,B$:
    $$
    P(A\cap B) = P(A)P(B).
    $$
  - Mutually independent events $A_1,\dots,A_n$:
    $$
    P(A_{j_1}\cap \dots \cap A_{j_k}) = P(A_{j_1})\dots P(A_{j_k})
    $$
    for any subcollection.
- Symbols.
  - $A,B$: events.
  - $P(A)$, $P(B)$, $P(A\cap B)$: their probabilities.
- When to use it.
  - When the problem statement explicitly says events or trials are independent.
  - As a modeling assumption (for example, independent channels, independent test results), but you should be aware this is an assumption.
- Common mistakes.
  - Confusing independence with mutual exclusivity (disjoint events).
  - Assuming pairwise independence automatically implies mutual independence for three or more events (it does not).

### 3.5 Conditional probability, total probability, and Bayes’ formula
- Conditional probability formula.
  - For $P(B) > 0$,
    $$
    P(A|B) = \frac{P(A\cap B)}{P(B)}.
    $$
- Total probability formula (finite version used in lecture).
  - If $B_1,\dots,B_n$ are pairwise disjoint, and $B = B_1\cup\dots\cup B_n$, then
    $$
    P(A\cap B) = \sum_{j=1}^n P(A\cap B_j).
    $$
    If $A \subset B$, then $P(A) = \sum_j P(A\cap B_j)$. In many examples each $B_j$ is a “scenario” and we write $P(A\cap B_j) = P(A|B_j)P(B_j)$.
- Bayes’ formula.
  - For pairwise disjoint hypotheses $B_1,\dots,B_n$ covering event $A$,
    $$
    P(B_j|A) = \frac{P(A|B_j)P(B_j)}{\sum_{k=1}^n P(A|B_k)P(B_k)}.
    $$
- Symbols.
  - $A$: observed event.
  - $B_j$: hypotheses or underlying scenarios.
  - $P(A|B_j)$: likelihood of observing $A$ under hypothesis $B_j$.
- When to use them.
  - Conditional probability: whenever you need probabilities under an explicit condition (“given that…”).
  - Total probability: when an event’s occurrence can be decomposed according to mutually exclusive cases.
  - Bayes’ formula: when you know prior probabilities of hypotheses and likelihoods, and you want posterior probabilities of hypotheses after observing data.
- Common mistakes.
  - Swapping $P(A|B)$ with $P(B|A)$.
  - Forgetting to multiply by prior probabilities $P(B_j)$ in Bayes’ formula.
  - Failing to list all hypotheses $B_1,\dots,B_n$ in the denominator.

## 4. Worked examples

### 4.1 Combinatorial probability with colors (from Lecture Example 2.3)
- Setup (from the lecture).
  - A bag contains 15 balls: two yellow, two green, three blue, four red, and four white.
  - Four balls are drawn at random, with all 4-ball subsets equally likely.
  - Question: what is the probability that the four drawn balls include exactly one ball of each of the colors yellow, blue, red, and white (in any order)?
- Step 1: describe the sample space.
  - We are choosing 4 balls out of 15 balls without order.
  - The number of possible 4-element subsets is
    $$
    \#\Omega = \binom{15}{4}.
    $$
- Step 2: count favorable outcomes.
  - We need one yellow, one blue, one red, and one white ball.
  - Yellow: 2 choices.
  - Blue: 3 choices.
  - Red: 4 choices.
  - White: 4 choices.
  - Total number of favorable selections is
    $$
    \#E = 2 \times 3 \times 4 \times 4.
    $$
- Step 3: compute the probability.
  - In a uniform space,
    $$
    P(E) = \frac{\#E}{\#\Omega} = \frac{2\cdot 3\cdot 4\cdot 4}{\binom{15}{4}} = \frac{32}{455}.
    $$
- Check your intuition.
  - The probability is relatively small because we are asking for a very specific pattern of colors out of many possibilities.
  - Writing the sample space in terms of combinations clarifies why we divide by $\binom{15}{4}$.

### 4.2 Bayesian reasoning with rare events (from Lecture Example 5.4)
- Setup (lecture example).
  - There are 100 coins. One coin has tails on both sides (unfair), the other 99 are ordinary fair coins.
  - Petya picks one coin at random and tosses it 10 times. Each time, the result is tails.
  - We want the probability that Petya picked the unfair coin, given this observation.
- Step 1: define events and hypotheses.
  - $B_1$: “the chosen coin is honest”.
  - $B_2$: “the chosen coin is double-tailed”.
  - $A$: “10 consecutive tosses of the chosen coin all show tails”.
  - Prior probabilities:
    $$
    P(B_1) = 99/100,\quad P(B_2) = 1/100.
    $$
- Step 2: compute likelihoods $P(A|B_j)$.
  - If the coin is honest ($B_1$): the chance of 10 tails in a row is $(1/2)^{10} = 2^{-10}$.
  - If the coin is double-tailed ($B_2$): every toss is tails, so $P(A|B_2) = 1$.
- Step 3: apply Bayes’ formula for $P(B_2|A)$.
  - Bayes’ formula gives
    $$
    P(B_2|A) = \frac{P(A|B_2)P(B_2)}{P(A|B_1)P(B_1)+P(A|B_2)P(B_2)}.
    $$
  - Plug in the values:
    $$
    P(B_2|A)
      = \frac{1\cdot (1/100)}{2^{-10}\cdot (99/100) + 1\cdot (1/100)}
      = \frac{1}{\frac{99}{2^{10}} + 1}
      = \frac{1}{\frac{99}{1024} + 1}
      = \frac{1024}{1123} \approx 0.91.
    $$
  - The lecture writes this fraction explicitly and compares it to 1.
- Check your intuition.
  - Even though the unfair coin was initially very unlikely (1 out of 100), seeing a very unlikely outcome (10 tails in a row) makes that hypothesis much more plausible.
  - Bayes’ formula quantifies this intuition: the posterior probability of the unfair coin becomes very high.

## 5. Lab/Tutorial essentials (week02.pdf)

### 5.1 What the lab asked you to do
- Exercises on basic properties of conditional probability and total probability.
  - Prove that if $B \subset A_1\cup\dots\cup A_n$ with disjoint $A_i$, then $P(A_1|B)+\dots+P(A_n|B) = 1$.
- Combinatorial and discrete probability tasks.
  - Probability comparisons when choosing numbers (e.g., two different numbers from $\{1,\dots,100\}$).
  - Urn problems where some balls disappear or are transferred between urns; compute probabilities of colors and reverse-conditional probabilities.
  - Card problems: computing $P(A\cup B)$ for events like “jack” and “black suit” in a 36-card deck.
  - Dice problems: products, sums, and conditions like “sum is multiple of 3” when rolling dice.
- Problems involving independence and inclusion–exclusion.
  - Proving inequalities like $P(AB) \ge P(A)+P(B)-1$ and its generalization to many events.
  - Showing that certain games or settings are (or are not) fair by comparing win probabilities of players.
  - Using inclusion–exclusion to compute probabilities like “at least one volume is not in its correct position” or “at least one letter is fixed”.
- Geometric probability and continuous-time arrival problems.
  - Typical “meeting at the airport” question: husband and wife arrive uniformly at different intervals and wait certain periods; find probability that the husband ends up “in trouble”.
  - Lift problems with people choosing floors independently and uniformly, e.g., probability the lift stops on certain floors or at least a certain number of times.
- Bayes’ rule applications.
  - Problems involving test accuracy, diseases, and recovery probabilities, where you must find the probability of an underlying cause given an observed outcome.
  - Examples: attendance vs getting an A in Probability and Statistics; disease types vs recovery; trucks vs passenger cars refueling at a gas station.

### 5.2 How to solve / approach them
- Proving probability identities and inequalities.
  - Start from basic definitions: express $P(A|B)$ as $P(A\cap B)/P(B)$, and rewrite sums in terms of intersections.
  - For inequalities like $P(AB) \ge P(A)+P(B)-1$, rewrite $P(AB^c) = P(A) - P(AB)$ and use that probabilities are nonnegative.
- Combinatorial counting.
  - Carefully define the sample space: are you counting sequences (ordered) or sets (unordered)?
  - Use $\binom{n}{k}$ for unordered selections and $n!$ for permutations; for mixed-color urns, multiply choices per color when colors must be represented in specific counts.
  - In lift problems, model each person’s floor choice as independent and equally likely among allowed floors, then count favorable combinations.
- Conditional probability and Bayes in lab problems.
  - Identify hypotheses $B_1,\dots,B_n$ (e.g., which urn was chosen, which disease the patient had, whether a person attended lectures).
  - Compute $P(B_j)$ (priors) and $P(A|B_j)$ (likelihoods) explicitly.
  - Apply Bayes’ formula to get $P(B_j|A)$.
  - Check results against intuition: rare diseases or rare “bad” scenarios usually remain rare unless the observed data strongly favor them.
- Independence and fairness.
  - For games with alternating turns (card drawing, coin flipping), set up a probability tree or series (e.g., geometric series) to sum the probabilities of each player winning.
  - To check if a game is fair, compare the probability that each player wins under the rules.
  - For independence problems, look at $P(A\cap B)$ vs $P(A)P(B)$ using counts or algebraic manipulation.

### 5.3 Mini practice
- Practice 1: simple combinatorial probability.
  - Question: Two different numbers are chosen at random from $\{1,2,\dots,100\}$. What is the probability that the first number is greater than the second?
  - Brief answer: By symmetry, every unordered pair is equally likely, and in exactly half the ordered pairs the first element is greater, so the probability is $0.5$.
- Practice 2: conditional probability and Bayes (attendance problem style).
  - Question: Suppose $70\%$ of students who attend lectures get an A, $35\%$ of students attend lectures, and overall $25\%$ of students get an A. A randomly chosen student got an A. What is the probability that this student attended lectures?
  - Brief answer: Let $B$ = “attends lectures”, $A$ = “gets an A”. Then $P(B) = 0.35$, $P(A|B) = 0.70$, $P(A) = 0.25$. By Bayes’ formula,
    $$
    P(B|A) = \frac{P(A|B)P(B)}{P(A)} = \frac{0.70\cdot 0.35}{0.25} \approx 0.98.
    $$
- Practice 3: independence check.
  - Question: Let $P(A) = P(B) = 0.5$. Show that $P(AB) - P(A B) = 0$.
  - Brief answer: Write $P(AB) = P(A) - P(AB^c)$ and $P(A B) = P(A) - P(AB)$. Using $P(A) = 0.5$, this simplifies and the difference cancels to 0; this shows how complements interact with intersections when probabilities are 0.5.

## 6. Quick recap
- A probability space $(\Omega,\mathcal{F},P)$ consists of a sample space, a σ-algebra of events, and a probability measure that satisfies Kolmogorov’s axioms.
- Events are subsets of $\Omega$; operations like union, intersection, and complement have direct probabilistic interpretations (e.g., $A\cup B$ is “A or B”).
- In finite uniform spaces, probabilities reduce to counting: probability = (number of favorable outcomes)/(number of possible outcomes).
- Inclusion–exclusion corrects for overlaps when computing probabilities of unions of events.
- Geometric probability replaces counting by measuring areas or volumes, using ratios of areas to compute probabilities.
- Independence means that $P(A\cap B) = P(A)P(B)$; mutual independence is stronger than pairwise independence.
- Conditional probability $P(A|B) = P(A\cap B)/P(B)$ formalizes “probability of A given B has occurred”.
- The formula of total probability expresses $P(A)$ in terms of conditional probabilities across a partition of the sample space.
- Bayes’ formula updates the probabilities of hypotheses after observing data, and can dramatically shift probabilities when observations are unlikely under most hypotheses.
- The week 2 lab deepens these ideas through many exercises on combinatorial probability, conditional probability, independence, and Bayes’ rule in practical scenarios.


[<kbd><br><- Return (ProbStat)<br></kbd>](ProbStat.md)
