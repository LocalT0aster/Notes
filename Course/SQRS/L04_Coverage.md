# L04 — Adequacy Criteria / Coverage Flashcards

**Source:** https://sqrbok.github.io/content/material/sqr/RQ_L04_Coverage.html

**Study notes:** https://sqrbok.github.io/content/material/sqr/SN_L04_Coverage.html

**Cards:** 32

> [!tip] Active recall
> Questions are copied verbatim from the pinned SQRBOK source. Answers are locally synthesized self-checks, not official model answers.

### Q1 — Coverage Categories

**Card ID:** l04-coverage-001

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L04_Coverage.html#question-1-coverage-categories

> [!question] Question
> ## Question 1: Coverage Categories
>
> Match each coverage category with its focus area:
>
> | Category | Focus |
> |----------|-------|
> | A. White Box | 1. Input space |
> | B. Black Box | 2. Code structure |
> | C. Mutation | 3. Specification |
> | D. Requirements | 4. Fault detection |

> [!answer]- Answer / self-check
> - **White-box → code structure**.
> - **Black-box → input/specification space**.
> - **Mutation → fault-detection strength**.
> - **Requirements/state coverage → specification/required behavior**.

### Q2 — Coverage Formula

**Card ID:** l04-coverage-002

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L04_Coverage.html#question-2-coverage-formula

> [!question] Question
> ## Question 2: Coverage Formula
>
> A test suite executes 45 out of 60 statements. What is the statement coverage?

> [!answer]- Answer / self-check
> 45/60 × 100% = **75%**.

### Q3 — Two Uses of Coverage

**Card ID:** l04-coverage-003

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L04_Coverage.html#question-3-two-uses-of-coverage

> [!question] Question
> ## Question 3: Two Uses of Coverage
>
> What are the two ways coverage criteria can be used? Explain each with an example.

> [!answer]- Answer / self-check
> - **Generator/goal:** design or add tests until a criterion is satisfied.
> - **Measure/diagnostic:** measure an existing suite to find unexercised elements.
> Coverage is most useful as feedback about gaps, not as a claim of correctness.

### Q4 — Statement Coverage Weakness

**Card ID:** l04-coverage-004

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L04_Coverage.html#question-4-statement-coverage-weakness

> [!question] Question
> ## Question 4: Statement Coverage Weakness
>
> Consider this code:
>
> ```python
> x = 0
> if condition:
>     x = 4
> y = z / x
> ```
>
> A test with `condition=True` achieves 100% statement coverage. Why is this problematic?

> [!answer]- Answer / self-check
> Statement coverage does not require every decision outcome. A test taking the true branch can execute the assignment and later division, giving 100% statement coverage, while never taking the false branch where the divisor remains zero. **Branch coverage** forces both outcomes.

### Q5 — Branch vs Statement

**Card ID:** l04-coverage-005

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L04_Coverage.html#question-5-branch-vs-statement

> [!question] Question
> ## Question 5: Branch vs Statement
>
> How many tests are needed for 100% branch coverage on an `if-else` statement? How does this compare to statement coverage?

> [!answer]- Answer / self-check
> For a binary decision, **2 tests** are needed for 100% branch coverage (true + false). Statement coverage may need only **1** if one path executes all statements relevant to the metric; therefore branch coverage subsumes statement coverage but not vice versa.

### Q6 — Compound Predicate Problem

**Card ID:** l04-coverage-006

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L04_Coverage.html#question-6-compound-predicate-problem

> [!question] Question
> ## Question 6: Compound Predicate Problem
>
> For `if (A && B)`, branch coverage requires only 2 tests. What combination is never tested, and why is this a problem?

> [!answer]- Answer / self-check
> Tests `(T,T)` and `(F,*)` cover true/false decision outcomes, but can miss **A=T, B=F** because short-circuit false can be achieved with A=F. A defect specifically involving B (or AND vs OR) may survive.

### Q7 — Cyclomatic Complexity Calculation

**Card ID:** l04-coverage-007

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L04_Coverage.html#question-7-cyclomatic-complexity-calculation

> [!question] Question
> ## Question 7: Cyclomatic Complexity Calculation
>
> A control flow graph has 10 edges and 8 nodes. Calculate $$V(G)$$.

> [!answer]- Answer / self-check
> V(G)=E−N+2 = 10−8+2 = **4** independent basis paths.

### Q8 — Alternative Formula

**Card ID:** l04-coverage-008

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L04_Coverage.html#question-8-alternative-formula

> [!question] Question
> ## Question 8: Alternative Formula
>
> A function has 5 decision points (if, while, etc.). What is its cyclomatic complexity?

> [!answer]- Answer / self-check
> For a single connected function, V(G)=D+1 = 5+1 = **6**.

### Q9 — Basis Path vs All Paths

**Card ID:** l04-coverage-009

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L04_Coverage.html#question-9-basis-path-vs-all-paths

> [!question] Question
> ## Question 9: Basis Path vs All Paths
>
> Why is basis path coverage preferred over all-path coverage? Complete this table for a function whose decisions follow one another **in sequence** (not nested):
>
> | Decisions | All Paths | Basis Paths |
> |-----------|-----------|-------------|
> | 4 | ? | ? |
> | 10 | ? | ? |

> [!answer]- Answer / self-check
> All paths grow exponentially while basis paths grow roughly linearly with decisions.
> - 4 decisions: all paths ≈ **16**, basis paths **5**.
> - 10 decisions: all paths ≈ **1024**, basis paths **11**.
> Loops can make literal all-path coverage infinite.

### Q10 — Unfeasible Paths

**Card ID:** l04-coverage-010

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L04_Coverage.html#question-10-unfeasible-paths

> [!question] Question
> ## Question 10: Unfeasible Paths
>
> What is an unfeasible path? Give an example.

> [!answer]- Answer / self-check
> An infeasible path is present in the CFG but cannot occur for any valid execution because of data/semantic constraints. Example: test `x>0`, do not change x, then later require `x<=0`; that path combination cannot happen.

### Q11 — Condition Coverage Test Count

**Card ID:** l04-coverage-011

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L04_Coverage.html#question-11-condition-coverage-test-count

> [!question] Question
> ## Question 11: Condition Coverage Test Count
>
> For predicate `if (A && B)`, how many tests does each coverage type require?
>
> | Coverage Type | Tests Required |
> |---------------|----------------|
> | Basic Condition | ? |
> | Multiple Condition | ? |
> | MC/DC | ? |

> [!answer]- Answer / self-check
> Typical minimal sets:
> - **Basic condition:** 2 tests can make each condition T/F (e.g. TT, FF).
> - **Multiple condition:** **4** combinations TT, TF, FT, FF.
> - **MC/DC:** **3** tests, e.g. TT, TF, FT.

### Q12 — MC/DC Requirements

**Card ID:** l04-coverage-012

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L04_Coverage.html#question-12-mcdc-requirements

> [!question] Question
> ## Question 12: MC/DC Requirements
>
> What are the three requirements for MC/DC coverage?

> [!answer]- Answer / self-check
> 1. Every **decision** takes each outcome.
> 2. Every **condition** takes each outcome.
> 3. Each condition is shown to **independently affect** the decision outcome: change that condition alone (with relevant others fixed) and the decision changes.

### Q13 — MC/DC Test Count

**Card ID:** l04-coverage-013

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L04_Coverage.html#question-13-mcdc-test-count

> [!question] Question
> ## Question 13: MC/DC Test Count
>
> How many tests are needed for MC/DC coverage of a predicate with 5 conditions? Compare to Multiple Condition coverage ($$2^5$$).

> [!answer]- Answer / self-check
> MC/DC often needs **n+1 = 6** tests for 5 independent conditions, versus **2^5 = 32** for exhaustive multiple-condition coverage.

### Q14 — MC/DC Independence Pairs

**Card ID:** l04-coverage-014

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L04_Coverage.html#question-14-mcdc-independence-pairs

> [!question] Question
> ## Question 14: MC/DC Independence Pairs
>
> For `if (A && B && C)`, construct a minimal MC/DC test suite showing which pairs demonstrate each condition's independence.

> [!answer]- Answer / self-check
> Use baseline **TTT → T** plus **FTT → F**, **TFT → F**, **TTF → F**. Compare TTT with each one-condition change: those three pairs independently demonstrate A, B, and C.

### Q15 — MC/DC Standards

**Card ID:** l04-coverage-015

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L04_Coverage.html#question-15-mcdc-standards

> [!question] Question
> ## Question 15: MC/DC Standards
>
> Which standard requires MC/DC, for which domain and which level of software? Why would a standard choose MC/DC over multiple condition coverage?

> [!answer]- Answer / self-check
> - **DO-178C → aerospace/airborne software**, MC/DC required at highest criticality (Level A).
> - **ISO 26262 → automotive**, MC/DC strongly recommended/used for high ASIL such as ASIL D.
> - **IEC 62304 → medical-device software**, structural coverage including strong criteria may be used for highest safety classes; follow project/regulatory interpretation.

### Q16 — Mutation Score

**Card ID:** l04-coverage-016

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L04_Coverage.html#question-16-mutation-score

> [!question] Question
> ## Question 16: Mutation Score
>
> A test suite kills 72 mutants out of 100 total. 10 are equivalent mutants. What is the mutation score?

> [!answer]- Answer / self-check
> Equivalent mutants are excluded: 72/(100−10) = 72/90 = **80%**.

### Q17 — Mutation Operators

**Card ID:** l04-coverage-017

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L04_Coverage.html#question-17-mutation-operators

> [!question] Question
> ## Question 17: Mutation Operators
>
> Name five categories of mutation operators and give an example of each.

> [!answer]- Answer / self-check
> Examples: **arithmetic** `+→-`; **relational** `<→<=`; **logical** `&&→||`; **constant replacement** `0→1`; **statement deletion**. Other lecture operator sets may name AOR/ROR/LCR/UOI/ABS.

### Q18 — Pairwise Testing

**Card ID:** l04-coverage-018

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L04_Coverage.html#question-18-pairwise-testing

> [!question] Question
> ## Question 18: Pairwise Testing
>
> 4 parameters x 3 values each = 81 exhaustive combinations. How many tests does pairwise testing typically require? Why is this sufficient?

> [!answer]- Answer / self-check
> A representative pairwise covering array can be around **9 tests** rather than 81 (exact minimum depends constraints/tool). It ensures every pair of parameter values appears; empirical interaction studies show most faults are triggered by low-order interactions.

### Q19 — N-Switch Coverage

**Card ID:** l04-coverage-019

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L04_Coverage.html#question-19-n-switch-coverage

> [!question] Question
> ## Question 19: N-Switch Coverage
>
> What is the difference between 0-switch, 1-switch, and 2-switch coverage?

> [!answer]- Answer / self-check
> - **0-switch:** cover all states (or individual transitions depending convention; in this lecture table, all states).
> - **1-switch:** cover every single state transition.
> - **2-switch:** cover every sequence/pair of two consecutive transitions.
> Higher N exercises longer state histories and grows rapidly.

### Q20 — Coverage Limitations

**Card ID:** l04-coverage-020

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L04_Coverage.html#question-20-coverage-limitations

> [!question] Question
> ## Question 20: Coverage Limitations
>
> What does coverage measure, and what does it NOT measure? Complete the table:
>
> | Coverage Measures | Does NOT Measure |
> |-------------------|------------------|
> | ? | Oracle correctness |
> | ? | Missing code |
> | ? | Requirements coverage |

> [!answer]- Answer / self-check
> Coverage measures **executed code elements, traversed paths/branches, or exercised conditions/mutants**, depending metric. It does **not** prove oracle correctness, detect code that should exist but is missing, or guarantee requirements/usability/security coverage. High traversal ≠ high verification quality.

### Q21 — Size Confounding

**Card ID:** l04-coverage-021

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L04_Coverage.html#question-21-size-confounding

> [!question] Question
> ## Question 21: Size Confounding
>
> Inozemtseva & Holmes (2014) found that the coverage-effectiveness correlation becomes weak when they controlled for which variable? Lu et al. (2025) estimated how much of the apparent effect of statement and of branch coverage that variable explains: what were the figures?

> [!answer]- Answer / self-check
> The confounder is **test-suite size**: more tests both raise coverage and find more faults. In the lecture evidence, controlling for size drives the coverage/effectiveness correlation toward ~0. Later figures attribute about **69%** of statement-coverage and **81.9%** of branch-coverage correlation to suite size.

### Q22 — Assertions vs Coverage

**Card ID:** l04-coverage-022

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L04_Coverage.html#question-22-assertions-vs-coverage

> [!question] Question
> ## Question 22: Assertions vs Coverage
>
> According to Zhang & Mesbah (2015), what has a stronger correlation with test effectiveness: coverage or assertion quantity?

> [!answer]- Answer / self-check
> **Assertion quantity**. The cited study reports very strong correlations around **0.927–0.973**, while statement coverage alone is much weaker. Coverage measures exploration; assertions provide the oracle/verification.

### Q23 — Coverage Criteria Effectiveness

**Card ID:** l04-coverage-023

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L04_Coverage.html#question-23-coverage-criteria-effectiveness

> [!question] Question
> ## Question 23: Coverage Criteria Effectiveness
>
> In Hemmati (2015), a criterion counted as effective for a fault when the test that revealed the fault also increased that criterion's coverage. For what share of faults was statement coverage effective, and what share did control-flow plus def-use coverage reach? Why are these figures upper bounds?

> [!answer]- Answer / self-check
> The lecture's Hemmati summary reports about **10%** for statement coverage versus about **85%** when data-flow (definition–use) coverage is included.

### Q24 — Coverage Anti-Patterns

**Card ID:** l04-coverage-024

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L04_Coverage.html#question-24-coverage-anti-patterns

> [!question] Question
> ## Question 24: Coverage Anti-Patterns
>
> List three coverage anti-patterns and explain why each is problematic.

> [!answer]- Answer / self-check
> Examples: tests written only to raise the number; threshold gaming (“ship at 85%”); tests that execute code with weak/no assertions; treating low coverage as an individual blame metric. They optimize the proxy and can create high coverage without fault-revealing checks.

### Q25 — Coverage Level Selection

**Card ID:** l04-coverage-025

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L04_Coverage.html#question-25-coverage-level-selection

> [!question] Question
> ## Question 25: Coverage Level Selection
>
> Match each context with the appropriate coverage criterion:
>
> | Context | Criterion |
> |---------|-----------|
> | A. Minimum bar for any code | 1. MC/DC |
> | B. Default for unit tests | 2. Statement |
> | C. Safety-critical (DO-178C Level A) | 3. Branch |
> | D. Complex control flow | 4. Basis Path |

> [!answer]- Answer / self-check
> - Minimum bar for ordinary code → **Statement**.
> - Default stronger unit criterion → **Branch**.
> - Safety-critical DO-178C Level A → **MC/DC**.
> - Complex control flow → **Basis Path**.

### Q26 — Coverage Gates

**Card ID:** l04-coverage-026

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L04_Coverage.html#question-26-coverage-gates

> [!question] Question
> ## Question 26: Coverage Gates
>
> A team lead proposes a merge gate: "no pull request below 85% branch coverage." Using Marick (1997) and Inozemtseva & Holmes (2014), explain what this gate is likely to do to the tests people write. What would you use the coverage report for instead?

> [!answer]- Answer / self-check
> Lecture guideline table:
> - **Statement:** min ~70%, target ~80%.
> - **Branch:** min ~75%, target ~85%.
> - **Mutation:** min ~60%, target ~80%.
> These are heuristics, not universal release guarantees.

### Q27 — Tool Matching

**Card ID:** l04-coverage-027

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L04_Coverage.html#question-27-tool-matching

> [!question] Question
> ## Question 27: Tool Matching
>
> Match the coverage tool to its language:
>
> | Tool | Language |
> |------|----------|
> | A. JaCoCo | 1. Python |
> | B. Coverage.py | 2. Java |
> | C. LLVM-cov | 3. JavaScript |
> | D. c8 | 4. C/C++ |

> [!answer]- Answer / self-check
> - **JaCoCo → Java**.
> - **Coverage.py → Python**.
> - **LLVM-cov → C/C++** (also LLVM-supported languages).
> - **c8 → JavaScript/TypeScript (Node/V8)**.

### Q28 — Oracle Problem

**Card ID:** l04-coverage-028

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L04_Coverage.html#question-28-oracle-problem

> [!question] Question
> ## Question 28: Oracle Problem
>
> What is the oracle problem in software testing? What are some mitigations?

> [!answer]- Answer / self-check
> The oracle problem is deciding whether an observed output is **correct** for arbitrary test inputs. Mitigations: reference implementations, assertions/contracts, metamorphic relations/properties, differential testing, model-based expected results, sanitizers/crash oracles, and human/domain review.

### Q29 — Branch Coverage and Mutation Relation

**Card ID:** l04-coverage-029

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L04_Coverage.html#question-29-branch-coverage-and-mutation-relation

> [!question] Question
> ## Question 29: Branch Coverage and Mutation Relation
>
> What is the relationship between branch coverage and mutation testing? Does one subsume the other?

> [!answer]- Answer / self-check
> They measure different things: branch coverage measures **structural traversal**; mutation measures whether tests **detect injected faults**. High branch coverage can have weak assertions and low mutation score; strong mutation tests may not imply every structural branch is covered. In general **neither subsumes the other**.

### Q30 — Branch vs Statement Coverage (Practical)

**Card ID:** l04-coverage-030

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L04_Coverage.html#question-30-branch-vs-statement-coverage-practical

> [!question] Question
> ## Question 30: Branch vs Statement Coverage (Practical)
>
> Explain why branch coverage is considered stronger than statement coverage. Provide a code example where 100% statement coverage fails to detect a fault that branch coverage would catch.

> [!answer]- Answer / self-check
> Use an `if` without `else`: initialize `x=0`; if condition set `x=4`; then compute `z/x`. A true-condition test executes all statements but misses the false branch where x remains zero. Adding a false-condition test for branch coverage exposes the fault.

### Q31 — MC/DC Calculation (Practical)

**Card ID:** l04-coverage-031

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L04_Coverage.html#question-31-mcdc-calculation-practical

> [!question] Question
> ## Question 31: MC/DC Calculation (Practical)
>
> Given predicate `if ((A || B) && C)`:
> a) How many tests for Multiple Condition coverage?
> b) Construct a minimal MC/DC test suite
> c) Show independence pairs for each condition

> [!answer]- Answer / self-check
> Multiple-condition coverage: **2^3 = 8**. One 4-test MC/DC set:
> - T1: A=T,B=F,C=T → T
> - T2: A=F,B=T,C=T → T
> - T3: A=F,B=F,C=T → F
> - T4: A=F,B=T,C=F → F
> Pairs: A=T1↔T3; B=T2↔T3; C=T2↔T4.

### Q32 — Critical Analysis (Practical)

**Card ID:** l04-coverage-032

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L04_Coverage.html#question-32-critical-analysis-practical

> [!question] Question
> ## Question 32: Critical Analysis (Practical)
>
> A project manager claims: "We achieved 95% code coverage, so our software is thoroughly tested." Critically evaluate this claim using evidence from recent research.

> [!answer]- Answer / self-check
> Reject the inference, not the usefulness of the metric. Coverage says what code was traversed, not whether assertions were strong, requirements were complete, missing behavior was tested, or fault-revealing inputs were used. Cite size confounding, stronger association of assertions with effectiveness, and diminishing returns. Use coverage to find gaps alongside spec-based, mutation/data-flow, and oracle-quality evidence.
