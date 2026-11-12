# L06 — Random Testing Flashcards

**Source:** https://sqrbok.github.io/content/material/sqr/RQ_L06_Random.html

**Study notes:** https://sqrbok.github.io/content/material/sqr/SN_L06_Random.html

**Cards:** 34

> [!tip] Active recall
> Questions are copied verbatim from the pinned SQRBOK source. Answers are locally synthesized self-checks, not official model answers.

### Q1 — What Makes Random Testing "Random"

**Card ID:** l06-random-001

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L06_Random.html#question-1-what-makes-random-testing-random

> [!question] Question
> ## Question 1: What Makes Random Testing "Random"
>
> What makes random testing "random" in the technical sense? What three conditions must be satisfied (Hamlet)?

> [!answer]- Answer / self-check
> 1. A **defined input distribution** (uniform or operational profile).
> 2. **Independent** random selections from that distribution.
> 3. An **oracle** that can automatically decide pass/fail.
> Random testing is statistical sampling, not haphazard picking.

### Q2 — Random vs Partition Testing

**Card ID:** l06-random-002

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L06_Random.html#question-2-random-vs-partition-testing

> [!question] Question
> ## Question 2: Random vs Partition Testing
>
> When would random testing be a poor choice compared to partition testing?

> [!answer]- Answer / self-check
> When the input space has known rare but high-risk regions/boundaries, pure random sampling may almost never hit them. If domain knowledge supports meaningful partitions, BVA/EP can allocate tests deliberately to those regions. Random excels when structure is weak or high-volume statistical evidence is the goal.

### Q3 — Statistical Confidence Limits

**Card ID:** l06-random-003

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L06_Random.html#question-3-statistical-confidence-limits

> [!question] Question
> ## Question 3: Statistical Confidence Limits
>
> A colleague says "we ran 10,000 random tests with no failures, so the software is bug-free." What is wrong with this claim? Use the formula $$C = 1-(1-F)^N$$ with a true failure rate of $F = 1/10{,}000$.

> [!answer]- Answer / self-check
> No finite random sample proves zero failure probability. It supports a bound relative to an assumed failure rate/distribution. For target F=10^-4 and N=10,000, confidence is only **≈63.2%** that at least one failure would have appeared if the true rate were 1 in 10,000. The conclusion is statistical, not absolute.

### Q4 — Reliability Calculation

**Card ID:** l06-random-004

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L06_Random.html#question-4-reliability-calculation

> [!question] Question
> ## Question 4: Reliability Calculation
>
> Calculate how many random tests are needed for 95% confidence that the failure rate is below 1 in 10,000.
>
> *Hint: Use $N = \frac{\ln(1-C)}{\ln(1-F)}$*

> [!answer]- Answer / self-check
> N = ln(1−0.95)/ln(1−0.0001) ≈ **29,956 tests** (round up).

### Q5 — Randoop Plateau Effect

**Card ID:** l06-random-005

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L06_Random.html#question-5-randoop-plateau-effect

> [!question] Question
> ## Question 5: Randoop Plateau Effect
>
> What is the "plateau effect" in Randoop and what causes it?

> [!answer]- Answer / self-check
> After initial rapid discovery, new sequences increasingly revisit already-explored states/behaviors; reachable novelty becomes harder to generate, so coverage and bug-finding rates flatten. The lecture notes Randoop's error-finding rate dropping toward zero after roughly a dozen hours in the cited study.

### Q6 — Hamlet's Argument for Random Testing

**Card ID:** l06-random-006

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L06_Random.html#question-6-hamlets-argument-for-random-testing

> [!question] Question
> ## Question 6: Hamlet's Argument for Random Testing
>
> Why did Hamlet (2006) argue that "only random testing will do" in certain scenarios? Name two such scenarios.

> [!answer]- Answer / self-check
> - **Large/unstructured domains** with no principled basis for partitioning.
> - **Persistent-state systems**, where valid tests are input sequences from reset and arbitrary sampled internal states may be unreachable.
> Random sampling preserves the real reachable-state distribution.

### Q7 — Oracle and Effectiveness

**Card ID:** l06-random-007

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L06_Random.html#question-7-oracle-and-effectiveness

> [!question] Question
> ## Question 7: Oracle and Effectiveness
>
> Explain the relationship between the oracle and the effectiveness of random testing. Compare crash detection, sanitizers, properties, and differential oracles.

> [!answer]- Answer / self-check
> - **Crash/hang:** very cheap, finds catastrophic failures only.
> - **Sanitizers:** detect memory/undefined/thread errors during execution.
> - **Properties/assertions:** check semantic invariants and widen bug classes.
> - **Differential oracle:** compare implementations/models to detect wrong outputs.
> Input generation can be excellent, but the oracle determines what failures become visible.

### Q8 — Fuzz vs Random Testing

**Card ID:** l06-random-008

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L06_Random.html#question-8-fuzz-vs-random-testing

> [!question] Question
> ## Question 8: Fuzz vs Random Testing
>
> How does fuzz testing differ from random testing, and when would you choose fuzzing over general random testing?

> [!answer]- Answer / self-check
> Random testing samples a defined input distribution for broad/statistical goals. Fuzzing aggressively mutates/generates malformed inputs, usually guided by crashes, sanitizers, or coverage, to maximize fault discovery—especially parser, memory-safety, robustness, and security bugs. Choose fuzzing when adversarial input handling is central.

### Q9 — Three Generations of Fuzzing

**Card ID:** l06-random-009

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L06_Random.html#question-9-three-generations-of-fuzzing

> [!question] Question
> ## Question 9: Three Generations of Fuzzing
>
> Explain the three generations of fuzzing (blackbox, whitebox, greybox). What does each add, and what does greybox fuzzing trade away compared with whitebox fuzzing?

> [!answer]- Answer / self-check
> - **Black-box:** random/mutational inputs without program feedback.
> - **White-box:** symbolic/concolic execution and constraint solving.
> - **Grey-box:** lightweight coverage feedback guides mutations (AFL/libFuzzer).
> Grey-box combines very high execution throughput with enough feedback to reach new code, avoiding much of symbolic execution's path/solver cost.

### Q10 — Miller's Persistent Bug Classes

**Card ID:** l06-random-010

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L06_Random.html#question-10-millers-persistent-bug-classes

> [!question] Question
> ## Question 10: Miller's Persistent Bug Classes
>
> Miller's fuzz studies found the same bug classes persisting for 16 years (1990-2006). What does this tell us about the software industry?

> [!answer]- Answer / self-check
> Tooling improved, but organizations repeatedly reintroduced the same robustness/input-handling mistakes. This suggests security/reliability is not solved by one tool generation: prevention, safer APIs/languages, regression suites, and continuous fuzzing must accompany discovery.

### Q11 — Directed Greybox Fuzzing

**Card ID:** l06-random-011

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L06_Random.html#question-11-directed-greybox-fuzzing

> [!question] Question
> ## Question 11: Directed Greybox Fuzzing
>
> What is directed greybox fuzzing and why was AFLGo able to find Heartbleed in 20 minutes when symbolic execution failed in 24 hours?

> [!answer]- Answer / self-check
> It biases coverage-guided mutation toward code locations of interest (e.g. changed/vulnerable functions). It keeps fuzzing throughput high and uses distance feedback rather than solving every path constraint. This can reach deep real paths quickly where symbolic execution suffers path explosion/solver difficulty; the lecture cites Heartbleed in ~20 min vs >24 h.

### Q12 — Crash Count vs Bug Count

**Card ID:** l06-random-012

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L06_Random.html#question-12-crash-count-vs-bug-count

> [!question] Question
> ## Question 12: Crash Count vs Bug Count
>
> Why is the finding that "57,142 unique crashes = only 9 actual bugs" (Klees 2018) important for fuzzing practice?

> [!answer]- Answer / self-check
> Crash deduplication heuristics dramatically overcount root causes: many inputs/stack traces can trigger the same defect. Evaluate fuzzers by **distinct confirmed bugs**, with repeated trials and statistical comparison—not raw crash-file counts.

### Q13 — Evaluating Fuzzers

**Card ID:** l06-random-013

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L06_Random.html#question-13-evaluating-fuzzers

> [!question] Question
> ## Question 13: Evaluating Fuzzers
>
> Klees et al. (2018) found that rankings of two fuzzers reversed between 6 and 24 hours of fuzzing. What should a fair comparison of two fuzzers include, and why?

> [!answer]- Answer / self-check
> Fuzzers differ in mutation operators, seed handling, instrumentation, search heuristics, and path biases. Their coverage/failure sets are only partly overlapping; diversity reduces correlated blind spots, so combining tools often finds many additional bugs.

### Q14 — QuickCheck Bug Distribution

**Card ID:** l06-random-014

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L06_Random.html#question-14-quickcheck-bug-distribution

> [!question] Question
> ## Question 14: QuickCheck Bug Distribution
>
> QuickCheck's authors found the errors divided roughly evenly between generators, properties and programs. Why is this surprising, and what does it say about writing properties?

> [!answer]- Answer / self-check
> PBT is not only testing the implementation: writing executable properties exposes **specification mistakes**, and generators/shrinkers are themselves test infrastructure that can be wrong. Roughly one-third in each category shows that formalizing properties improves the whole testing model.

### Q15 — Hypothesis's Universal Representation

**Card ID:** l06-random-015

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L06_Random.html#question-15-hypothesiss-universal-representation

> [!question] Question
> ## Question 15: Hypothesis's Universal Representation
>
> What problem does Hypothesis's "single universal representation" of test cases solve?

> [!answer]- Answer / self-check
> It separates complex typed generation from the underlying search/shrink representation. Hypothesis can shrink and mutate a generic byte stream, then map it into structured values, avoiding a bespoke shrinker/search strategy for every data type and enabling reusable feedback.

### Q16 — JQF Improvement

**Card ID:** l06-random-016

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L06_Random.html#question-16-jqf-improvement

> [!question] Question
> ## Question 16: JQF Improvement
>
> On the Trie example, pure random generation found no failure in over 7 million executions while JQF's Zest found one after about 5,000. What does Zest do differently?

> [!answer]- Answer / self-check
> It combines **property-based structured generators** with **coverage-guided fuzzing**. Inputs remain semantically valid/structured, while coverage feedback evolves seeds toward new program behavior. The cited benchmark found a bug in ~5k executions that random PBT missed after millions.

### Q17 — PBT Property Challenge

**Card ID:** l06-random-017

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L06_Random.html#question-17-pbt-property-challenge

> [!question] Question
> ## Question 17: PBT Property Challenge
>
> In Goldstein et al. (2024), 16 of 30 practitioners said writing specifications slowed them down, and one called "not knowing what properties to test" the most common failure mode. Why is finding properties hard, and which kinds of property did practitioners use most?

> [!answer]- Answer / self-check
> Examples specify one expected result; properties must express general truths across huge input spaces. Useful invariants often require deep domain knowledge, alternate models, round trips, metamorphic relations, or differential oracles. The generator is usually easier than discovering a powerful invariant.

### Q18 — PBT vs Fuzzing Time Budgets

**Card ID:** l06-random-018

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L06_Random.html#question-18-pbt-vs-fuzzing-time-budgets

> [!question] Question
> ## Question 18: PBT vs Fuzzing Time Budgets
>
> Compare the time budgets of PBT (50ms-30s) versus fuzzing campaigns (hours/days). What does this reveal about their integration patterns?

> [!answer]- Answer / self-check
> PBT is commonly a **developer/CI test** with fast feedback (milliseconds to seconds). Fuzzing is often a **continuous/campaign** activity that spends long budgets exploring coverage. They can share generators/oracles, but operate at different feedback loops.

### Q19 — Coupling Effect

**Card ID:** l06-random-019

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L06_Random.html#question-19-coupling-effect

> [!question] Question
> ## Question 19: Coupling Effect
>
> Explain the coupling effect and why it justifies testing with simple mutations only.

> [!answer]- Answer / self-check
> Complex faults are often coupled to simple faults: a test set capable of killing simple mutants tends also to kill the vast majority of more complex mutants. This motivates using a small set of simple mutation operators instead of generating every possible complex mutant.

### Q20 — Equivalent Mutant Problem

**Card ID:** l06-random-020

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L06_Random.html#question-20-equivalent-mutant-problem

> [!question] Question
> ## Question 20: Equivalent Mutant Problem
>
> Why is the equivalent mutant problem the most persistent challenge in mutation testing? Use the share of equivalent mutants and the decidability of equivalence.

> [!answer]- Answer / self-check
> An equivalent mutant changes syntax but not observable program behavior for any input, so no test can kill it. Determining semantic equivalence is undecidable in general; 10–40% equivalence rates can waste analysis effort and distort mutation scores unless filtered.

### Q21 — Small vs Large LLMs for Mutant Detection

**Card ID:** l06-random-021

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L06_Random.html#question-21-small-vs-large-llms-for-mutant-detection

> [!question] Question
> ## Question 21: Small vs Large LLMs for Mutant Detection
>
> In Tian et al. (2024), a fine-tuned code model of modest size (UniXCoder) outperformed prompting large general models such as GPT-4 on equivalent mutant detection. Suggest reasons why training on code and fine-tuning for the task could matter more than model size.

> [!answer]- Answer / self-check
> Task/data alignment can matter more than parameter count: a model trained/fine-tuned on code representations and the exact equivalence task learns structural signals that a general conversational model may not. The lecture cites UniXCoder ~86.6% F1 vs GPT-4 ~55.9% on that benchmark; treat it as task-specific evidence, not a universal model ranking.

### Q22 — Crossfire Phenomenon

**Card ID:** l06-random-022

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L06_Random.html#question-22-crossfire-phenomenon

> [!question] Question
> ## Question 22: Crossfire Phenomenon
>
> What is the "crossfire" phenomenon in mutation testing?

> [!answer]- Answer / self-check
> A single well-designed test often kills **multiple mutants**. Mutation-guided test improvement therefore has compounding returns: you do not necessarily need one new test per surviving mutant.

### Q23 — Mutation Score Target

**Card ID:** l06-random-023

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L06_Random.html#question-23-mutation-score-target

> [!question] Question
> ## Question 23: Mutation Score Target
>
> A team achieves 85% mutation score. Should they aim for 100%? Why or why not? Consider equivalent mutants and the cost of each remaining survivor.

> [!answer]- Answer / self-check
> Not automatically. Surviving mutants may be equivalent, trivial, unreachable, or extremely costly to target; returns diminish near the top. Investigate high-value survivors, exclude justified equivalents, and prioritize risk. 100% is meaningful only if the mutant set and oracle justify it.

### Q24 — Mutation vs PBT Comparison

**Card ID:** l06-random-024

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L06_Random.html#question-24-mutation-vs-pbt-comparison

> [!question] Question
> ## Question 24: Mutation vs PBT Comparison
>
> Compare how mutation testing and property-based testing approach test quality. How are they complementary?

> [!answer]- Answer / self-check
> **Mutation** perturbs the program and asks whether the existing suite notices—an oracle/test-strength assessment. **PBT** generates many inputs from a model and checks general properties—an input/oracle generation strategy. Together, mutation can expose weak properties while PBT can generate cases that kill mutants.

### Q25 — Branch Coverage and Mutation

**Card ID:** l06-random-025

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L06_Random.html#question-25-branch-coverage-and-mutation

> [!question] Question
> ## Question 25: Branch Coverage and Mutation
>
> *(Relies on L04, Adequacy Criteria.)* What is the relation between branch coverage and mutation testing? Does one subsume the other?

> [!answer]- Answer / self-check
> No. Structural traversal and fault sensitivity are different dimensions. A suite can cover every branch yet fail to kill simple mutants because its assertions are weak; a mutation-focused suite may still omit structurally irrelevant branches. Use both when the risk justifies it.

### Q26 — Plain versus Guided Random Testing

**Card ID:** l06-random-026

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L06_Random.html#question-26-plain-versus-guided-random-testing

> [!question] Question
> ## Question 26: Plain versus Guided Random Testing
>
> Feedback-directed testing and coverage-guided fuzzing choose later inputs because of earlier results; property-based tools skew their distribution towards edge values. Which of Hamlet's conditions for a reliability figure does each break, and what can you then no longer claim?

> [!answer]- Answer / self-check
> Neither universally. Partition testing is efficient when meaningful risk-based subdomains/boundaries are known. Random testing is simple, scalable, statistically analyzable, and attractive when the space is unstructured or the operational distribution matters. At scale, modestly more random tests can erase small partition advantages in some studies.
> For a reliability estimate, tests must be independent samples from the specified usage distribution. Feedback-directed testing and coverage-guided fuzzing adapt later inputs to earlier results, breaking that independence/fixed sampling model; edge-biased PBT does not sample the operational distribution. These can be excellent bug-finding tools, but their raw success counts cannot justify the same unbiased operational failure probability or simple independent-trial confidence bound.

### Q27 — Random Seeds

**Card ID:** l06-random-027

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L06_Random.html#question-27-random-seeds

> [!question] Question
> ## Question 27: Random Seeds
>
> In the AutoTest study, one seed found 5 bugs and another 23 for the same class in 30 minutes. What does this mean for how you run and report random testing?

> [!answer]- Answer / self-check
> Fuzzing automatically feeds unexpected/malformed or mutated inputs to find robustness/security defects. Inputs are often mutation/coverage-guided rather than independent operational samples; the focus is bug discovery rather than unbiased reliability estimation; common oracles are crashes, hangs, sanitizers, assertions, and coverage signals.
> One seed is not representative. Run **multiple independent seeds at equal budgets**, report the distribution/variability of unique bugs and the tool/version/configuration/budget, and preserve seeds plus minimized failing inputs for replay. Do not report only the best seed or treat duplicate crashes as distinct defects.

### Q28 — Oracle Problem

**Card ID:** l06-random-028

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L06_Random.html#question-28-oracle-problem

> [!question] Question
> ## Question 28: Oracle Problem
>
> What is the oracle problem? Why is it the bottleneck of random testing?

> [!answer]- Answer / self-check
> Generating millions of inputs is cheap; knowing the correct output for millions of inputs is not. Without an automated oracle, random tests can only reveal obvious crashes/hangs. Strong properties, models, differential implementations, or sanitizers expand what automated random generation can actually detect.

### Q29 — Oracle Evolution

**Card ID:** l06-random-029

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L06_Random.html#question-29-oracle-evolution

> [!question] Question
> ## Question 29: Oracle Evolution
>
> Trace the oracles across the four techniques: random testing, fuzz testing, property-based testing and mutation testing. (In mutation testing, the oracle is the test suite's own verdict: a mutant is killed when some test fails.)

> [!answer]- Answer / self-check
> - **Random:** external/reference oracle or simple expected result.
> - **Fuzzing:** often crash/hang/sanitizer oracle; increasingly semantic assertions.
> - **PBT:** executable **properties/invariants** are the oracle.
> - **Mutation:** the existing test suite itself is evaluated as the oracle—does it fail on injected faults?
> The progression shifts from simple failure signals toward richer semantic/test-quality checks.

### Q30 — Single Technique Selection

**Card ID:** l06-random-030

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L06_Random.html#question-30-single-technique-selection

> [!question] Question
> ## Question 30: Single Technique Selection
>
> If you could only apply one technique from this lecture to a new project, which would you choose and why? Consider different project types.

> [!answer]- Answer / self-check
> Tie the technique to dominant risk: parser/network/security boundary → coverage-guided fuzzing; mathematical/serialization/data-structure library → PBT; mature suite whose adequacy is uncertain → mutation testing; unstructured/stateful domain or reliability sampling → random testing. The justification matters more than a universal winner.

### Q31 — Bug Classes vs Tool Progress

**Card ID:** l06-random-031

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L06_Random.html#question-31-bug-classes-vs-tool-progress

> [!question] Question
> ## Question 31: Bug Classes vs Tool Progress
>
> The same kinds of programming errors kept appearing across Miller's studies from 1990 to 2006, while recent models reach an F1-score of about 87% on equivalent mutant detection. What does this contrast suggest about where testing tools have improved and where they have not?

> [!answer]- Answer / self-check
> Local tool capability can improve dramatically while organizational/systemic defect causes persist. Better analysis does not automatically change unsafe APIs, incentives, review practice, legacy code, or deployment pressure. Reliability requires both advanced detection **and** prevention/process feedback.

### Q32 — Testing Strategy Design (Practical)

**Card ID:** l06-random-032

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L06_Random.html#question-32-testing-strategy-design-practical

> [!question] Question
> ## Question 32: Testing Strategy Design (Practical)
>
> Design a testing strategy for a JSON parser that combines techniques from all four topics (random testing, fuzzing, PBT, mutation testing).

> [!answer]- Answer / self-check
> - Random: sample valid/invalid JSON across size/depth distributions.
> - Fuzz: seed with corpus, mutate bytes/tokens, use coverage + ASan/UBSan, dictionary for JSON syntax.
> - PBT: generate ASTs; property `parse(serialize(ast)) == ast`; metamorphic whitespace/key-order cases.
> - Mutation: mutate parser conditions/operators and ensure the suite kills them.
> Persist every discovered failure as regression input.

### Q33 — JQF's Significance (Practical)

**Card ID:** l06-random-033

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L06_Random.html#question-33-jqfs-significance-practical

> [!question] Question
> ## Question 33: JQF's Significance (Practical)
>
> Why might JQF's convergence of PBT and fuzzing be the most significant development across all four topics? Explain how it resolves limitations of both approaches.

> [!answer]- Answer / self-check
> PBT provides **structured valid generators and semantic properties** but random search wastes executions; fuzzing provides **coverage-guided search** but raw byte mutation struggles with structured input. Combining them keeps valid structured inputs while steering toward new behavior, addressing central weaknesses of both.

### Q34 — When Random Testing Stops Finding Bugs (Practical)

**Card ID:** l06-random-034

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L06_Random.html#question-34-when-random-testing-stops-finding-bugs-practical

> [!question] Question
> ## Question 34: When Random Testing Stops Finding Bugs (Practical)
>
> Randoop stopped finding new errors after about twelve hours, and Miller's fuzz studies kept finding the same kinds of bugs over sixteen years. What do these two observations say about how long a random-testing tool stays useful, and what would you change to keep finding bugs?

> [!answer]- Answer / self-check
> Repeatedly using the same distributions, seeds, properties, or mutation operators eventually stops finding new defects because the program/test suite adapts or the search saturates. Universal mitigation: **diversify and refresh**—new seeds/distributions/properties/operators/tools, feedback from production, and regression plus exploration.
