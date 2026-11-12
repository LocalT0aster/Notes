# L05 — Input Domain Testing Flashcards

**Source:** https://sqrbok.github.io/content/material/sqr/RQ_L05_Domain.html

**Study notes:** https://sqrbok.github.io/content/material/sqr/SN_L05_Domain.html

**Cards:** 26

> [!tip] Active recall
> Questions are copied verbatim from the pinned SQRBOK source. Answers are locally synthesized self-checks, not official model answers.

### Q1 — Core Definitions

**Card ID:** l05-domain-001

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L05_Domain.html#question-1-core-definitions

> [!question] Question
> ## Question 1: Core Definitions
>
> Match each testing term with its definition:
>
> | Term | Definition |
> |------|------------|
> | A. Test Case | 1. Mechanism to determine correct output |
> | B. Test Suite | 2. Values provided to system |
> | C. Oracle | 3. Input + expected output |
> | D. Test Input | 4. Collection of test cases |

> [!answer]- Answer / self-check
> - **Test input:** values supplied to the system.
> - **Oracle:** mechanism for deciding the correct/acceptable result.
> - **Test case:** input plus expected result/oracle/context.
> - **Test suite:** collection of test cases.

### Q2 — Positive Test Bias

**Card ID:** l05-domain-002

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L05_Domain.html#question-2-positive-test-bias

> [!question] Question
> ## Question 2: Positive Test Bias
>
> What is the positive test strategy (positive test bias)? Which tests does it tend to leave out, and why would line or branch coverage not reveal the gap?

> [!answer]- Answer / self-check
> Testers naturally choose inputs they expect to work. This over-samples valid/normal partitions and under-samples invalid, boundary, and adversarial cases. Counter it with explicit negative-test planning, partitioning, and incentives to find failures rather than merely confirm success.

### Q3 — Black-Box vs White-Box

**Card ID:** l05-domain-003

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L05_Domain.html#question-3-black-box-vs-white-box

> [!question] Question
> ## Question 3: Black-Box vs White-Box
>
> A tester has no access to source code and must test a payment gateway API. What testing approach should they use and why?

> [!answer]- Answer / self-check
> Use **black-box/specification-based testing**: derive equivalence partitions, boundaries, decision tables, state/contract cases, and negative inputs from the API specification and observable behavior. White-box structural criteria require implementation access.

### Q4 — Partition Requirements

**Card ID:** l05-domain-004

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L05_Domain.html#question-4-partition-requirements

> [!question] Question
> ## Question 4: Partition Requirements
>
> What two properties must equivalence partitions satisfy?

> [!answer]- Answer / self-check
> They must be **complete/exhaustive** (every possible input is in some partition) and **disjoint** (no input belongs to more than one partition for that partitioning dimension).

### Q5 — Weak vs Strong EP

**Card ID:** l05-domain-005

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L05_Domain.html#question-5-weak-vs-strong-ep

> [!question] Question
> ## Question 5: Weak vs Strong EP
>
> A system has three input variables with the following **valid** equivalence classes:
> - Variable A: 4 valid classes
> - Variable B: 3 valid classes
> - Variable C: 5 valid classes
>
> a) How many tests are needed for weak EP? For strong EP?
> b) Variable A also has 2 invalid classes and variable C has 1. How many tests does each approach need now, and why are the invalid classes counted separately?

> [!answer]- Answer / self-check
> Using the lecture formulas: **weak EP = max(4,3,5)=5** tests; **strong EP = 4×3×5=60** combinations.

### Q6 — Finding Equivalence Classes

**Card ID:** l05-domain-006

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L05_Domain.html#question-6-finding-equivalence-classes

> [!question] Question
> ## Question 6: Finding Equivalence Classes
>
> For a function that validates email addresses, identify at least 5 equivalence classes.

> [!answer]- Answer / self-check
> Possible classes: valid normal address; missing `@`; empty local part; empty domain; invalid/missing top-level domain; illegal characters; too-long local/domain/address; Unicode/IDN case; whitespace/control characters. Define expected behavior for each.

### Q7 — Partition Heuristics

**Card ID:** l05-domain-007

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L05_Domain.html#question-7-partition-heuristics

> [!question] Question
> ## Question 7: Partition Heuristics
>
> Match the heuristic to its example:
>
> | Heuristic | Example |
> |-----------|---------|
> | A. Range-based | 1. US regions (Northeast, South, Midwest, West) |
> | B. Enumeration | 2. Age groups (0–12, 13–19, 20–64, 65–120) |
> | C. Error types | 3. Input that causes "File not found" error |

> [!answer]- Answer / self-check
> - Age bands → **range-based**.
> - US regions / finite named options → **enumeration**.
> - Inputs that trigger “file not found” → **error-type** partition.

### Q8 — Boundary Fault Types

**Card ID:** l05-domain-008

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L05_Domain.html#question-8-boundary-fault-types

> [!question] Question
> ## Question 8: Boundary Fault Types
>
> Classify each bug by its boundary fault type:
>
> | Bug | Type |
> |-----|------|
> | A. `if (x < 10)` should be `if (x <= 10)` | ? |
> | B. `if (x < 10)` should be `if (x < 20)` | ? |
> | C. Upper bound check is missing | ? |
>
> For an integer `x`, could any test tell bug A apart from the shift `if (x <= 9)`? Explain.

> [!answer]- Answer / self-check
> - `<` should be `<=` → **closure bug**.
> - `<10` should be `<11` → **boundary shift**.
> - No upper-bound condition → **missing boundary**.

### Q9 — ON/OFF Points

**Card ID:** l05-domain-009

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L05_Domain.html#question-9-onoff-points

> [!question] Question
> ## Question 9: ON/OFF Points
>
> For the condition `x >= 100`, identify:
> a) The ON point
> b) The OFF point
> c) Is the boundary open or closed?

> [!answer]- Answer / self-check
> For integer x: **ON = 100** (exact boundary), **OFF = 99** (just outside the accepted region). `>=` is a **closed** boundary because the boundary value is included.

### Q10 — BVA Test Count

**Card ID:** l05-domain-010

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L05_Domain.html#question-10-bva-test-count

> [!question] Question
> ## Question 10: BVA Test Count
>
> A function takes 3 numeric inputs.
> a) Testing each input at min, min+, max− and max while the others stay nominal, plus one all-nominal test: how many tests?
> b) Extreme point combinations (under, min, max, over for every input, all combined, plus one nominal point): how many tests?
> c) Why does one count grow linearly and the other exponentially, and what does each miss? (Note: "weak" in Weak 1×1 is unrelated to weak EP.)

> [!answer]- Answer / self-check
> Basic BVA = 4k+1 = 4×3+1 = **13**. Robust BVA = 6k+1 = 6×3+1 = **19**.

### Q11 — Closed vs Open Intervals

**Card ID:** l05-domain-011

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L05_Domain.html#question-11-closed-vs-open-intervals

> [!question] Question
> ## Question 11: Closed vs Open Intervals
>
> For the valid range $1 < x < 100$, which test points should be used?

> [!answer]- Answer / self-check
> For integer input, test the boundaries and immediately-inside values: **1 (ON, invalid), 2 (OFF/inside), 99 (inside), 100 (ON, invalid)**, plus a nominal interior value for a basic set. The key is testing both processing regions adjacent to each open boundary.

### Q12 — BVA Limitations

**Card ID:** l05-domain-012

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L05_Domain.html#question-12-bva-limitations

> [!question] Question
> ## Question 12: BVA Limitations
>
> Name three limitations of boundary value analysis.

> [!answer]- Answer / self-check
> BVA assumes faults cluster at boundaries; it does not systematically cover interactions among many parameters; it depends on identifying the right partitions/boundaries; and it does not solve oracle, state/history, timing, or missing-requirement problems. Any three with explanation are sufficient.

### Q13 — Decision Table Components

**Card ID:** l05-domain-013

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L05_Domain.html#question-13-decision-table-components

> [!question] Question
> ## Question 13: Decision Table Components
>
> What are the four main components of a decision table?

> [!answer]- Answer / self-check
> **Conditions**, **condition values/entries**, **actions/responses**, and **rules** (columns mapping a combination of condition values to actions).

### Q14 — Rule Count

**Card ID:** l05-domain-014

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L05_Domain.html#question-14-rule-count

> [!question] Question
> ## Question 14: Rule Count
>
> A decision table has 3 binary conditions (Y/N). How many rules are needed before consolidation?

> [!answer]- Answer / self-check
> 2^3 = **8 rules**.

### Q15 — Checksum Verification

**Card ID:** l05-domain-015

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L05_Domain.html#question-15-checksum-verification

> [!question] Question
> ## Question 15: Checksum Verification
>
> A decision table has one condition with 3 values and two yes/no conditions, so 3 × 2 × 2 = 12 rules. After consolidation it has 5 rules that cover {2, 3, 1, 4, 2} of the original rules. Does the checksum confirm the consolidation? Could an overlap between two merged rules together with a missing combination still sum to 12? What else would you check to be sure that each original combination is covered exactly once?

> [!answer]- Answer / self-check
> The cover counts sum to 2+3+1+4+2 = **12**, so the checksum passes. You still need to verify the merged rules truly have identical actions and valid don't-care conditions.

### Q16 — The 8-Step Method

**Card ID:** l05-domain-016

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L05_Domain.html#question-16-the-8-step-method

> [!question] Question
> ## Question 16: The 8-Step Method
>
> Put the Beizer 8-step decision table method in correct order:
>
> A. Specify expected outputs per rule
> B. List the conditions with their values
> C. Verify the checksum
> D. Fill the columns with all combinations
> E. Develop one test case per rule
> F. List the actions
> G. Calculate the number of rules
> H. Identify common actions and consolidate

> [!answer]- Answer / self-check
> A useful order: **list actions → list conditions/values → calculate rule count → enumerate combinations → specify actions per rule → consolidate common-action rules with don't-cares → verify checksum → derive tests (one per resulting rule)**.

### Q17 — When to Use Decision Tables

**Card ID:** l05-domain-017

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L05_Domain.html#question-17-when-to-use-decision-tables

> [!question] Question
> ## Question 17: When to Use Decision Tables
>
> Which scenarios are good fits for decision table testing?
>
> | Scenario | Good Fit? |
> |----------|-----------|
> | A. Tax calculation with multiple brackets and deductions | ? |
> | B. Performance testing under load | ? |
> | C. Access control based on role, department, and time | ? |
> | D. Continuous output (temperature prediction) | ? |

> [!answer]- Answer / self-check
> Good fits are logic with discrete interacting conditions: **tax calculation** and **access control**. Load-performance behavior and continuous prediction are not primarily decision-table problems.

### Q18 — How Many Conditions Trigger a Failure?

**Card ID:** l05-domain-018

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L05_Domain.html#question-18-how-many-conditions-trigger-a-failure

> [!question] Question
> ## Question 18: How Many Conditions Trigger a Failure?
>
> Kuhn, Wallace and Gallo (2004) traced failures in four systems to the number of interacting inputs (parameters) that triggered them. What range of failures needed only one or two inputs, and what was the largest number any failure needed? What does this suggest about pairwise testing?

> [!answer]- Answer / self-check
> The lecture uses the memorable rule **about 90%**; the cited interaction datasets often show roughly **93% cumulative by 2-way**. The point is that pairwise covers a large majority, not all, interaction faults.

### Q19 — Pairwise Test Reduction

**Card ID:** l05-domain-019

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L05_Domain.html#question-19-pairwise-test-reduction

> [!question] Question
> ## Question 19: Pairwise Test Reduction
>
> A configuration has 34 yes/no switches.
> a) How many tests does "all combinations" need?
> b) What is the lower bound for a pairwise suite from the product of the two largest value counts?
> c) Show that 4 tests cover all pairs for 3 switches. How many tests do 34 switches need, and why is the product bound not reached?

> [!answer]- Answer / self-check
> Exhaustive = 2^34 = **17,179,869,184** combinations. The lecture example uses about **29 pairwise tests**—an enormous reduction while still covering every value pair.

### Q20 — Interaction Strength Selection

**Card ID:** l05-domain-020

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L05_Domain.html#question-20-interaction-strength-selection

> [!question] Question
> ## Question 20: Interaction Strength Selection
>
> Using the Kuhn et al. (2004) data, argue which combination strategy suits each context (an opinion question: justify your choice, there is no single right answer): each choice (every class at least once), pairwise, or 3-way and more:
>
> | Context | Strength |
> |---------|----------|
> | A. General UI testing | ? |
> | B. Medical device software | ? |
> | C. Business-critical financial system | ? |

> [!answer]- Answer / self-check
> Lecture guideline: **2-way** for general/UI applications; around **3-way** for business-critical systems; **4–6 way** (plus other assurance techniques) for safety-critical/medical contexts. Risk, constraints, and evidence can justify different choices.

### Q21 — Combinatorial Testing Limitations

**Card ID:** l05-domain-021

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L05_Domain.html#question-21-combinatorial-testing-limitations

> [!question] Question
> ## Question 21: Combinatorial Testing Limitations
>
> Name three limitations of combinatorial testing.

> [!answer]- Answer / self-check
> It depends on correct parameter/value modeling; pairwise misses higher-order interactions; temporal/stateful behavior may not be represented; constraints/masking complicate generation; generated cases still need oracles. Combine it with EP/BVA and other techniques.

### Q22 — Technique Matching

**Card ID:** l05-domain-022

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L05_Domain.html#question-22-technique-matching

> [!question] Question
> ## Question 22: Technique Matching
>
> Match each scenario to the best primary technique:
>
> | Scenario | Technique |
> |----------|-----------|
> | A. Testing a numeric range 1-100 | ? |
> | B. Testing a system with 20 configuration options | ? |
> | C. Testing ATM withdrawal with multiple conditions | ? |
> | D. Testing user types: admin, manager, user, guest | ? |

> [!answer]- Answer / self-check
> - Numeric range 1–100 → **BVA** (after EP).
> - 20 configuration options → **pairwise/combinatorial**.
> - ATM with interacting rules → **decision table**.
> - Admin/manager/user/guest → **equivalence partitioning**.

### Q23 — Integration Order

**Card ID:** l05-domain-023

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L05_Domain.html#question-23-integration-order

> [!question] Question
> ## Question 23: Integration Order
>
> What is the recommended order for combining input domain techniques?

> [!answer]- Answer / self-check
> **Start with EP → refine boundaries with BVA → model complex conditional logic with decision tables → use pairwise/combinatorial generation when many parameters make combinations explode.** Pairwise optimizes a model; it should not replace good partitioning.

### Q24 — EP and BVA Relationship (Practical)

**Card ID:** l05-domain-024

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L05_Domain.html#question-24-ep-and-bva-relationship-practical

> [!question] Question
> ## Question 24: EP and BVA Relationship (Practical)
>
> Explain why boundary value analysis complements equivalence partitioning rather than replacing it. Provide an example.

> [!answer]- Answer / self-check
> EP chooses representative values from behaviorally similar regions; BVA targets the edges **between** those regions where off-by-one/closure faults cluster. Example: EP for age {underage, adult, senior}; BVA explicitly tests 17/18 and 64/65 around class boundaries.

### Q25 — Decision Table Construction (Practical)

**Card ID:** l05-domain-025

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L05_Domain.html#question-25-decision-table-construction-practical

> [!question] Question
> ## Question 25: Decision Table Construction (Practical)
>
> A login system has the following conditions:
> - Username known? (Y/N)
> - Password correct? (Y/N)
> - Account active? (Y/N)
>
> a) Create a complete decision table
> b) Consolidate using don't-care values
> c) Verify your consolidation with checksum

> [!answer]- Answer / self-check
> Start with 8 binary combinations. A compact consolidation can be:
> 1. Username invalid → reject (password/account don't care): covers 4.
> 2. Username valid, password invalid → reject: covers 2.
> 3. Username+password valid, account inactive → inactive/blocked: covers 1.
> 4. All valid/active → login success: covers 1.
> Checksum 4+2+1+1=8.

### Q26 — Critical Analysis (Practical)

**Card ID:** l05-domain-026

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L05_Domain.html#question-26-critical-analysis-practical

> [!question] Question
> ## Question 26: Critical Analysis (Practical)
>
> A team decides to use only pairwise testing for a safety-critical medical device control system. Evaluate this decision.

> [!answer]- Answer / self-check
> Pairwise alone is insufficient: it intentionally ignores many 3+ way interactions and does not address timing, state, structural coverage, hazards, or oracle quality. Use risk-driven higher-strength combinations plus requirements/hazard analysis, BVA/decision tables, structural criteria such as MC/DC where applicable, static analysis, reviews, and system validation.
