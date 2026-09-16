# L04 — Adequacy Criteria / Coverage Flashcards

**Source:** https://sqrbok.github.io//content/material/sqr/RQ_L04_Coverage.html

**Cards:** 32

> [!tip] Active recall
> Answer every part before revealing the answer. For design/essay questions, the answer is a grading checklist: alternative designs can also be correct when justified.

### Q1 — Coverage categories

> [!question] Question
> Match white-box, black-box, mutation, and requirements coverage to their focus.

> [!answer]- Answer / self-check
> - **White-box → code structure**.
> - **Black-box → input/specification space**.
> - **Mutation → fault-detection strength**.
> - **Requirements/state coverage → specification/required behavior**.

### Q2 — Coverage calculation

> [!question] Question
> A suite executes 45 of 60 statements. Compute statement coverage.

> [!answer]- Answer / self-check
> 45/60 × 100% = **75%**.

### Q3 — Two uses of coverage

> [!question] Question
> What are the two ways a coverage criterion can be used?

> [!answer]- Answer / self-check
> - **Generator/goal:** design or add tests until a criterion is satisfied.
> - **Measure/diagnostic:** measure an existing suite to find unexercised elements.
> Coverage is most useful as feedback about gaps, not as a claim of correctness.

### Q4 — Why 100% statement coverage can miss a fault

> [!question] Question
> Explain how a test can execute every statement yet miss division by zero in an if-controlled assignment.

> [!answer]- Answer / self-check
> Statement coverage does not require every decision outcome. A test taking the true branch can execute the assignment and later division, giving 100% statement coverage, while never taking the false branch where the divisor remains zero. **Branch coverage** forces both outcomes.

### Q5 — Branch vs statement test count

> [!question] Question
> How many tests are typically needed to cover both outcomes of a simple if-else, and how does that compare with statement coverage?

> [!answer]- Answer / self-check
> For a binary decision, **2 tests** are needed for 100% branch coverage (true + false). Statement coverage may need only **1** if one path executes all statements relevant to the metric; therefore branch coverage subsumes statement coverage but not vice versa.

### Q6 — Compound-predicate blind spot

> [!question] Question
> For `A && B`, what case can branch coverage miss and why does it matter?

> [!answer]- Answer / self-check
> Tests `(T,T)` and `(F,*)` cover true/false decision outcomes, but can miss **A=T, B=F** because short-circuit false can be achieved with A=F. A defect specifically involving B (or AND vs OR) may survive.

### Q7 — Cyclomatic complexity from graph

> [!question] Question
> A CFG has E=10 edges and N=8 nodes. Compute V(G).

> [!answer]- Answer / self-check
> V(G)=E−N+2 = 10−8+2 = **4** independent basis paths.

### Q8 — Cyclomatic complexity from decisions

> [!question] Question
> A function has five decision points. Compute cyclomatic complexity.

> [!answer]- Answer / self-check
> For a single connected function, V(G)=D+1 = 5+1 = **6**.

### Q9 — Basis path vs all paths

> [!question] Question
> Why use basis-path coverage instead of all paths? Fill the 4- and 10-decision examples.

> [!answer]- Answer / self-check
> All paths grow exponentially while basis paths grow roughly linearly with decisions.
> - 4 decisions: all paths ≈ **16**, basis paths **5**.
> - 10 decisions: all paths ≈ **1024**, basis paths **11**.
> Loops can make literal all-path coverage infinite.

### Q10 — Infeasible paths

> [!question] Question
> Define an infeasible path and give an example.

> [!answer]- Answer / self-check
> An infeasible path is present in the CFG but cannot occur for any valid execution because of data/semantic constraints. Example: test `x>0`, do not change x, then later require `x<=0`; that path combination cannot happen.

### Q11 — Condition-coverage test counts

> [!question] Question
> For `A && B`, compare Basic Condition, Multiple Condition, and MC/DC test counts.

> [!answer]- Answer / self-check
> Typical minimal sets:
> - **Basic condition:** 2 tests can make each condition T/F (e.g. TT, FF).
> - **Multiple condition:** **4** combinations TT, TF, FT, FF.
> - **MC/DC:** **3** tests, e.g. TT, TF, FT.

### Q12 — MC/DC requirements

> [!question] Question
> State the three requirements of MC/DC.

> [!answer]- Answer / self-check
> 1. Every **decision** takes each outcome.
> 2. Every **condition** takes each outcome.
> 3. Each condition is shown to **independently affect** the decision outcome: change that condition alone (with relevant others fixed) and the decision changes.

### Q13 — MC/DC scaling

> [!question] Question
> How many tests are typically needed for MC/DC with five conditions, versus multiple-condition coverage?

> [!answer]- Answer / self-check
> MC/DC often needs **n+1 = 6** tests for 5 independent conditions, versus **2^5 = 32** for exhaustive multiple-condition coverage.

### Q14 — MC/DC independence for A && B && C

> [!question] Question
> Construct a minimal MC/DC set for `A && B && C` and show independence pairs.

> [!answer]- Answer / self-check
> Use baseline **TTT → T** plus **FTT → F**, **TFT → F**, **TTF → F**. Compare TTT with each one-condition change: those three pairs independently demonstrate A, B, and C.

### Q15 — MC/DC standards

> [!question] Question
> Match DO-178C, ISO 26262, and IEC 62304 to their domains and MC/DC use.

> [!answer]- Answer / self-check
> - **DO-178C → aerospace/airborne software**, MC/DC required at highest criticality (Level A).
> - **ISO 26262 → automotive**, MC/DC strongly recommended/used for high ASIL such as ASIL D.
> - **IEC 62304 → medical-device software**, structural coverage including strong criteria may be used for highest safety classes; follow project/regulatory interpretation.

### Q16 — Mutation score

> [!question] Question
> 72 of 100 mutants are killed; 10 are equivalent. Compute mutation score.

> [!answer]- Answer / self-check
> Equivalent mutants are excluded: 72/(100−10) = 72/90 = **80%**.

### Q17 — Mutation operators

> [!question] Question
> Name five mutation-operator categories with examples.

> [!answer]- Answer / self-check
> Examples: **arithmetic** `+→-`; **relational** `<→<=`; **logical** `&&→||`; **constant replacement** `0→1`; **statement deletion**. Other lecture operator sets may name AOR/ROR/LCR/UOI/ABS.

### Q18 — Pairwise reduction

> [!question] Question
> Four parameters each have three values: 81 exhaustive combinations. Roughly how many pairwise tests might suffice, and why?

> [!answer]- Answer / self-check
> A representative pairwise covering array can be around **9 tests** rather than 81 (exact minimum depends constraints/tool). It ensures every pair of parameter values appears; empirical interaction studies show most faults are triggered by low-order interactions.

### Q19 — N-switch coverage

> [!question] Question
> Differentiate 0-switch, 1-switch, and 2-switch state coverage.

> [!answer]- Answer / self-check
> - **0-switch:** cover all states (or individual transitions depending convention; in this lecture table, all states).
> - **1-switch:** cover every single state transition.
> - **2-switch:** cover every sequence/pair of two consecutive transitions.
> Higher N exercises longer state histories and grows rapidly.

### Q20 — What coverage does and does not measure

> [!question] Question
> State three things coverage measures and three it does not.

> [!answer]- Answer / self-check
> Coverage measures **executed code elements, traversed paths/branches, or exercised conditions/mutants**, depending metric. It does **not** prove oracle correctness, detect code that should exist but is missing, or guarantee requirements/usability/security coverage. High traversal ≠ high verification quality.

### Q21 — Coverage–effectiveness size confounding

> [!question] Question
> What confounder destroys much of the observed coverage/effectiveness correlation, and how large is the effect?

> [!answer]- Answer / self-check
> The confounder is **test-suite size**: more tests both raise coverage and find more faults. In the lecture evidence, controlling for size drives the coverage/effectiveness correlation toward ~0. Later figures attribute about **69%** of statement-coverage and **81.9%** of branch-coverage correlation to suite size.

### Q22 — Assertions vs coverage

> [!question] Question
> What correlates more strongly with test effectiveness: assertion quantity or coverage?

> [!answer]- Answer / self-check
> **Assertion quantity**. The cited study reports very strong correlations around **0.927–0.973**, while statement coverage alone is much weaker. Coverage measures exploration; assertions provide the oracle/verification.

### Q23 — Coverage criteria effectiveness

> [!question] Question
> What fault-detection rates are cited for statement coverage and data-flow coverage?

> [!answer]- Answer / self-check
> The lecture's Hemmati summary reports about **10%** for statement coverage versus about **85%** when data-flow (definition–use) coverage is included.

### Q24 — Coverage anti-patterns

> [!question] Question
> Name three coverage anti-patterns and why they are harmful.

> [!answer]- Answer / self-check
> Examples: tests written only to raise the number; threshold gaming (“ship at 85%”); tests that execute code with weak/no assertions; treating low coverage as an individual blame metric. They optimize the proxy and can create high coverage without fault-revealing checks.

### Q25 — Choosing a coverage criterion

> [!question] Question
> Match contexts to statement, branch, MC/DC, and basis-path coverage.

> [!answer]- Answer / self-check
> - Minimum bar for ordinary code → **Statement**.
> - Default stronger unit criterion → **Branch**.
> - Safety-critical DO-178C Level A → **MC/DC**.
> - Complex control flow → **Basis Path**.

### Q26 — Recommended coverage targets

> [!question] Question
> Recall the lecture's minimum/target levels for statement, branch, and mutation coverage.

> [!answer]- Answer / self-check
> Lecture guideline table:
> - **Statement:** min ~70%, target ~80%.
> - **Branch:** min ~75%, target ~85%.
> - **Mutation:** min ~60%, target ~80%.
> These are heuristics, not universal release guarantees.

### Q27 — Coverage tools by language

> [!question] Question
> Match JaCoCo, Coverage.py, LLVM-cov, and c8 to languages.

> [!answer]- Answer / self-check
> - **JaCoCo → Java**.
> - **Coverage.py → Python**.
> - **LLVM-cov → C/C++** (also LLVM-supported languages).
> - **c8 → JavaScript/TypeScript (Node/V8)**.

### Q28 — Oracle problem

> [!question] Question
> What is the oracle problem, and how can it be mitigated?

> [!answer]- Answer / self-check
> The oracle problem is deciding whether an observed output is **correct** for arbitrary test inputs. Mitigations: reference implementations, assertions/contracts, metamorphic relations/properties, differential testing, model-based expected results, sanitizers/crash oracles, and human/domain review.

### Q29 — Branch coverage vs mutation

> [!question] Question
> What is the relationship between branch coverage and mutation testing? Does either subsume the other?

> [!answer]- Answer / self-check
> They measure different things: branch coverage measures **structural traversal**; mutation measures whether tests **detect injected faults**. High branch coverage can have weak assertions and low mutation score; strong mutation tests may not imply every structural branch is covered. In general **neither subsumes the other**.

### Q30 — Why branch coverage is stronger

> [!question] Question
> Give a code example showing 100% statement coverage can miss a fault that branch coverage exposes.

> [!answer]- Answer / self-check
> Use an `if` without `else`: initialize `x=0`; if condition set `x=4`; then compute `z/x`. A true-condition test executes all statements but misses the false branch where x remains zero. Adding a false-condition test for branch coverage exposes the fault.

### Q31 — MC/DC for (A || B) && C

> [!question] Question
> For `((A || B) && C)`, give multiple-condition count and a minimal MC/DC set with independence pairs.

> [!answer]- Answer / self-check
> Multiple-condition coverage: **2^3 = 8**. One 4-test MC/DC set:
> - T1: A=T,B=F,C=T → T
> - T2: A=F,B=T,C=T → T
> - T3: A=F,B=F,C=T → F
> - T4: A=F,B=T,C=F → F
> Pairs: A=T1↔T3; B=T2↔T3; C=T2↔T4.

### Q32 — Critique “95% coverage = thoroughly tested”

> [!question] Question
> Evaluate the claim that 95% code coverage proves thorough testing.

> [!answer]- Answer / self-check
> Reject the inference, not the usefulness of the metric. Coverage says what code was traversed, not whether assertions were strong, requirements were complete, missing behavior was tested, or fault-revealing inputs were used. Cite size confounding, stronger association of assertions with effectiveness, and diminishing returns. Use coverage to find gaps alongside spec-based, mutation/data-flow, and oracle-quality evidence.
