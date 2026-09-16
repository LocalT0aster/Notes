# L06 — Random Testing Flashcards

**Source:** https://sqrbok.github.io//content/material/sqr/RQ_L06_Random.html

**Cards:** 34

> [!tip] Active recall
> Answer every part before revealing the answer. For design/essay questions, the answer is a grading checklist: alternative designs can also be correct when justified.

### Q1 — What makes random testing random?

> [!question] Question
> State Hamlet's three conditions for technically random testing.

> [!answer]- Answer / self-check
> 1. A **defined input distribution** (uniform or operational profile).
> 2. **Independent** random selections from that distribution.
> 3. An **oracle** that can automatically decide pass/fail.
> Random testing is statistical sampling, not haphazard picking.

### Q2 — When partition testing beats random

> [!question] Question
> When is random testing a poor choice relative to partition testing?

> [!answer]- Answer / self-check
> When the input space has known rare but high-risk regions/boundaries, pure random sampling may almost never hit them. If domain knowledge supports meaningful partitions, BVA/EP can allocate tests deliberately to those regions. Random excels when structure is weak or high-volume statistical evidence is the goal.

### Q3 — No failures does not mean bug-free

> [!question] Question
> Why does 10,000 failure-free random tests not prove correctness? Use C=1−(1−F)^N.

> [!answer]- Answer / self-check
> No finite random sample proves zero failure probability. It supports a bound relative to an assumed failure rate/distribution. For target F=10^-4 and N=10,000, confidence is only **≈63.2%** that at least one failure would have appeared if the true rate were 1 in 10,000. The conclusion is statistical, not absolute.

### Q4 — Random tests for 95% confidence

> [!question] Question
> How many failure-free tests give 95% confidence that F < 1/10,000?

> [!answer]- Answer / self-check
> N = ln(1−0.95)/ln(1−0.0001) ≈ **29,956 tests** (round up).

### Q5 — Randoop plateau effect

> [!question] Question
> What is the plateau effect in feedback-directed random testing and why does it happen?

> [!answer]- Answer / self-check
> After initial rapid discovery, new sequences increasingly revisit already-explored states/behaviors; reachable novelty becomes harder to generate, so coverage and bug-finding rates flatten. The lecture notes Randoop's error-finding rate dropping toward zero after roughly a dozen hours in the cited study.

### Q6 — Hamlet: when only random testing will do

> [!question] Question
> Name two situations Hamlet argues require random testing.

> [!answer]- Answer / self-check
> - **Large/unstructured domains** with no principled basis for partitioning.
> - **Persistent-state systems**, where valid tests are input sequences from reset and arbitrary sampled internal states may be unreachable.
> Random sampling preserves the real reachable-state distribution.

### Q7 — Oracle strength limits random testing

> [!question] Question
> Compare crash, sanitizer, property, and differential oracles.

> [!answer]- Answer / self-check
> - **Crash/hang:** very cheap, finds catastrophic failures only.
> - **Sanitizers:** detect memory/undefined/thread errors during execution.
> - **Properties/assertions:** check semantic invariants and widen bug classes.
> - **Differential oracle:** compare implementations/models to detect wrong outputs.
> Input generation can be excellent, but the oracle determines what failures become visible.

### Q8 — Fuzzing vs general random testing

> [!question] Question
> How does fuzzing differ from random testing and when should fuzzing be preferred?

> [!answer]- Answer / self-check
> Random testing samples a defined input distribution for broad/statistical goals. Fuzzing aggressively mutates/generates malformed inputs, usually guided by crashes, sanitizers, or coverage, to maximize fault discovery—especially parser, memory-safety, robustness, and security bugs. Choose fuzzing when adversarial input handling is central.

### Q9 — Three generations of fuzzing

> [!question] Question
> Describe black-box, white-box, and grey-box fuzzing and why grey-box dominates.

> [!answer]- Answer / self-check
> - **Black-box:** random/mutational inputs without program feedback.
> - **White-box:** symbolic/concolic execution and constraint solving.
> - **Grey-box:** lightweight coverage feedback guides mutations (AFL/libFuzzer).
> Grey-box combines very high execution throughput with enough feedback to reach new code, avoiding much of symbolic execution's path/solver cost.

### Q10 — Persistent fuzz bug classes

> [!question] Question
> What does recurrence of similar fuzz-found bug classes over 16 years imply?

> [!answer]- Answer / self-check
> Tooling improved, but organizations repeatedly reintroduced the same robustness/input-handling mistakes. This suggests security/reliability is not solved by one tool generation: prevention, safer APIs/languages, regression suites, and continuous fuzzing must accompany discovery.

### Q11 — Directed grey-box fuzzing

> [!question] Question
> What is directed grey-box fuzzing, and why can AFLGo beat symbolic execution on targets like Heartbleed?

> [!answer]- Answer / self-check
> It biases coverage-guided mutation toward code locations of interest (e.g. changed/vulnerable functions). It keeps fuzzing throughput high and uses distance feedback rather than solving every path constraint. This can reach deep real paths quickly where symbolic execution suffers path explosion/solver difficulty; the lecture cites Heartbleed in ~20 min vs >24 h.

### Q12 — Crashes are not bugs

> [!question] Question
> Why is “57,142 unique crashes = 9 bugs” important?

> [!answer]- Answer / self-check
> Crash deduplication heuristics dramatically overcount root causes: many inputs/stack traces can trigger the same defect. Evaluate fuzzers by **distinct confirmed bugs**, with repeated trials and statistical comparison—not raw crash-file counts.

### Q13 — Why multiple fuzzers help

> [!question] Question
> Why can a portfolio of fuzzers find substantially more bugs than any one?

> [!answer]- Answer / self-check
> Fuzzers differ in mutation operators, seed handling, instrumentation, search heuristics, and path biases. Their coverage/failure sets are only partly overlapping; diversity reduces correlated blind spots, so combining tools often finds many additional bugs.

### Q14 — QuickCheck bug distribution

> [!question] Question
> Why is finding bugs in implementations, specifications, and generators surprising/useful?

> [!answer]- Answer / self-check
> PBT is not only testing the implementation: writing executable properties exposes **specification mistakes**, and generators/shrinkers are themselves test infrastructure that can be wrong. Roughly one-third in each category shows that formalizing properties improves the whole testing model.

### Q15 — Hypothesis byte-stream representation

> [!question] Question
> What problem does a universal byte-stream representation solve?

> [!answer]- Answer / self-check
> It separates complex typed generation from the underlying search/shrink representation. Hypothesis can shrink and mutate a generic byte stream, then map it into structured values, avoiding a bespoke shrinker/search strategy for every data type and enabling reusable feedback.

### Q16 — Why JQF is ~1000× better than random PBT

> [!question] Question
> How does JQF/Zest achieve the reported improvement?

> [!answer]- Answer / self-check
> It combines **property-based structured generators** with **coverage-guided fuzzing**. Inputs remain semantically valid/structured, while coverage feedback evolves seeds toward new program behavior. The cited benchmark found a bug in ~5k executions that random PBT missed after millions.

### Q17 — The hardest part of PBT

> [!question] Question
> Why do practitioners struggle to know which properties to test?

> [!answer]- Answer / self-check
> Examples specify one expected result; properties must express general truths across huge input spaces. Useful invariants often require deep domain knowledge, alternate models, round trips, metamorphic relations, or differential oracles. The generator is usually easier than discovering a powerful invariant.

### Q18 — PBT vs fuzzing time budgets

> [!question] Question
> What do short PBT runs vs hours/days of fuzzing imply about integration?

> [!answer]- Answer / self-check
> PBT is commonly a **developer/CI test** with fast feedback (milliseconds to seconds). Fuzzing is often a **continuous/campaign** activity that spends long budgets exploring coverage. They can share generators/oracles, but operate at different feedback loops.

### Q19 — Coupling effect

> [!question] Question
> Explain the mutation-testing coupling effect.

> [!answer]- Answer / self-check
> Complex faults are often coupled to simple faults: a test set capable of killing simple mutants tends also to kill the vast majority of more complex mutants. This motivates using a small set of simple mutation operators instead of generating every possible complex mutant.

### Q20 — Equivalent mutant problem

> [!question] Question
> Why are equivalent mutants persistently difficult?

> [!answer]- Answer / self-check
> An equivalent mutant changes syntax but not observable program behavior for any input, so no test can kill it. Determining semantic equivalence is undecidable in general; 10–40% equivalence rates can waste analysis effort and distort mutation scores unless filtered.

### Q21 — Small code model vs GPT-4 for mutant equivalence

> [!question] Question
> Why might a 110M code-specific model outperform a much larger general model?

> [!answer]- Answer / self-check
> Task/data alignment can matter more than parameter count: a model trained/fine-tuned on code representations and the exact equivalence task learns structural signals that a general conversational model may not. The lecture cites UniXCoder ~86.6% F1 vs GPT-4 ~55.9% on that benchmark; treat it as task-specific evidence, not a universal model ranking.

### Q22 — Crossfire in mutation testing

> [!question] Question
> What is the crossfire phenomenon?

> [!answer]- Answer / self-check
> A single well-designed test often kills **multiple mutants**. Mutation-guided test improvement therefore has compounding returns: you do not necessarily need one new test per surviving mutant.

### Q23 — Should mutation score reach 100%?

> [!question] Question
> A team has 85% mutation score. Should it automatically chase 100%?

> [!answer]- Answer / self-check
> Not automatically. Surviving mutants may be equivalent, trivial, unreachable, or extremely costly to target; returns diminish near the top. Investigate high-value survivors, exclude justified equivalents, and prioritize risk. 100% is meaningful only if the mutant set and oracle justify it.

### Q24 — Mutation testing vs PBT

> [!question] Question
> Compare how mutation testing and property-based testing improve test quality.

> [!answer]- Answer / self-check
> **Mutation** perturbs the program and asks whether the existing suite notices—an oracle/test-strength assessment. **PBT** generates many inputs from a model and checks general properties—an input/oracle generation strategy. Together, mutation can expose weak properties while PBT can generate cases that kill mutants.

### Q25 — Branch coverage vs mutation

> [!question] Question
> Does branch coverage subsume mutation testing or vice versa?

> [!answer]- Answer / self-check
> No. Structural traversal and fault sensitivity are different dimensions. A suite can cover every branch yet fail to kill simple mutants because its assertions are weak; a mutation-focused suite may still omit structurally irrelevant branches. Use both when the risk justifies it.

### Q26 — Random vs partition testing

> [!question] Question
> Is random testing better than partition testing?

> [!answer]- Answer / self-check
> Neither universally. Partition testing is efficient when meaningful risk-based subdomains/boundaries are known. Random testing is simple, scalable, statistically analyzable, and attractive when the space is unstructured or the operational distribution matters. At scale, modestly more random tests can erase small partition advantages in some studies.

### Q27 — Define fuzz testing

> [!question] Question
> Define fuzzing and distinguish it from generic random testing by input, focus, and oracle.

> [!answer]- Answer / self-check
> Fuzzing automatically feeds unexpected/malformed or mutated inputs to find robustness/security defects. Inputs are often mutation/coverage-guided rather than independent operational samples; the focus is bug discovery rather than unbiased reliability estimation; common oracles are crashes, hangs, sanitizers, assertions, and coverage signals.

### Q28 — Oracle bottleneck

> [!question] Question
> What is the oracle problem and why does it bottleneck random testing?

> [!answer]- Answer / self-check
> Generating millions of inputs is cheap; knowing the correct output for millions of inputs is not. Without an automated oracle, random tests can only reveal obvious crashes/hangs. Strong properties, models, differential implementations, or sanitizers expand what automated random generation can actually detect.

### Q29 — Oracle evolution across four techniques

> [!question] Question
> Trace how the oracle changes from random testing through fuzzing, PBT, and mutation testing.

> [!answer]- Answer / self-check
> - **Random:** external/reference oracle or simple expected result.
> - **Fuzzing:** often crash/hang/sanitizer oracle; increasingly semantic assertions.
> - **PBT:** executable **properties/invariants** are the oracle.
> - **Mutation:** the existing test suite itself is evaluated as the oracle—does it fail on injected faults?
> The progression shifts from simple failure signals toward richer semantic/test-quality checks.

### Q30 — Choose one technique by project context

> [!question] Question
> If limited to one technique, how should the choice vary by project type?

> [!answer]- Answer / self-check
> Tie the technique to dominant risk: parser/network/security boundary → coverage-guided fuzzing; mathematical/serialization/data-structure library → PBT; mature suite whose adequacy is uncertain → mutation testing; unstructured/stateful domain or reliability sampling → random testing. The justification matters more than a universal winner.

### Q31 — Persistent bug classes vs advanced mutant detection

> [!question] Question
> What does the contrast between recurring fuzz bug classes and strong ML mutant detection suggest?

> [!answer]- Answer / self-check
> Local tool capability can improve dramatically while organizational/systemic defect causes persist. Better analysis does not automatically change unsafe APIs, incentives, review practice, legacy code, or deployment pressure. Reliability requires both advanced detection **and** prevention/process feedback.

### Q32 — Testing strategy for a JSON parser

> [!question] Question
> Combine random testing, fuzzing, PBT, and mutation testing for a JSON parser.

> [!answer]- Answer / self-check
> - Random: sample valid/invalid JSON across size/depth distributions.
> - Fuzz: seed with corpus, mutate bytes/tokens, use coverage + ASan/UBSan, dictionary for JSON syntax.
> - PBT: generate ASTs; property `parse(serialize(ast)) == ast`; metamorphic whitespace/key-order cases.
> - Mutation: mutate parser conditions/operators and ensure the suite kills them.
> Persist every discovered failure as regression input.

### Q33 — Why JQF-style convergence matters

> [!question] Question
> Why is convergence of PBT and coverage-guided fuzzing significant?

> [!answer]- Answer / self-check
> PBT provides **structured valid generators and semantic properties** but random search wastes executions; fuzzing provides **coverage-guided search** but raw byte mutation struggles with structured input. Combining them keeps valid structured inputs while steering toward new behavior, addressing central weaknesses of both.

### Q34 — Pesticide paradox across techniques

> [!question] Question
> How does the pesticide paradox apply to random, fuzz, PBT, and mutation testing?

> [!answer]- Answer / self-check
> Repeatedly using the same distributions, seeds, properties, or mutation operators eventually stops finding new defects because the program/test suite adapts or the search saturates. Universal mitigation: **diversify and refresh**—new seeds/distributions/properties/operators/tools, feedback from production, and regression plus exploration.
