# L05 — Input Domain Testing Flashcards

**Source:** https://sqrbok.github.io//content/material/sqr/RQ_L05_Domain.html

**Cards:** 26

> [!tip] Active recall
> Answer every part before revealing the answer. For design/essay questions, the answer is a grading checklist: alternative designs can also be correct when justified.

### Q1 — Core test definitions

> [!question] Question
> Match test case, test suite, oracle, and test input to their definitions.

> [!answer]- Answer / self-check
> - **Test input:** values supplied to the system.
> - **Oracle:** mechanism for deciding the correct/acceptable result.
> - **Test case:** input plus expected result/oracle/context.
> - **Test suite:** collection of test cases.

### Q2 — Positive test bias

> [!question] Question
> What is positive test bias and how does it affect coverage?

> [!answer]- Answer / self-check
> Testers naturally choose inputs they expect to work. This over-samples valid/normal partitions and under-samples invalid, boundary, and adversarial cases. Counter it with explicit negative-test planning, partitioning, and incentives to find failures rather than merely confirm success.

### Q3 — Black-box choice for a payment API

> [!question] Question
> With no source-code access, what approach should test a payment gateway and why?

> [!answer]- Answer / self-check
> Use **black-box/specification-based testing**: derive equivalence partitions, boundaries, decision tables, state/contract cases, and negative inputs from the API specification and observable behavior. White-box structural criteria require implementation access.

### Q4 — Equivalence-partition properties

> [!question] Question
> What two properties must equivalence partitions satisfy?

> [!answer]- Answer / self-check
> They must be **complete/exhaustive** (every possible input is in some partition) and **disjoint** (no input belongs to more than one partition for that partitioning dimension).

### Q5 — Weak vs strong EP counts

> [!question] Question
> A has 4 classes, B has 3, C has 5. Compute weak and strong EP counts.

> [!answer]- Answer / self-check
> Using the lecture formulas: **weak EP = max(4,3,5)=5** tests; **strong EP = 4×3×5=60** combinations.

### Q6 — Email equivalence classes

> [!question] Question
> Give at least five useful equivalence classes for email validation.

> [!answer]- Answer / self-check
> Possible classes: valid normal address; missing `@`; empty local part; empty domain; invalid/missing top-level domain; illegal characters; too-long local/domain/address; Unicode/IDN case; whitespace/control characters. Define expected behavior for each.

### Q7 — Partition heuristics

> [!question] Question
> Match range-based, enumeration, and error-type partitioning to examples.

> [!answer]- Answer / self-check
> - Age bands → **range-based**.
> - US regions / finite named options → **enumeration**.
> - Inputs that trigger “file not found” → **error-type** partition.

### Q8 — Boundary fault types

> [!question] Question
> Classify `<` vs `<=`, wrong numeric boundary, and missing upper bound.

> [!answer]- Answer / self-check
> - `<` should be `<=` → **closure bug**.
> - `<10` should be `<11` → **boundary shift**.
> - No upper-bound condition → **missing boundary**.

### Q9 — ON/OFF points for x >= 100

> [!question] Question
> Identify ON and OFF points and whether the boundary is open/closed.

> [!answer]- Answer / self-check
> For integer x: **ON = 100** (exact boundary), **OFF = 99** (just outside the accepted region). `>=` is a **closed** boundary because the boundary value is included.

### Q10 — BVA test counts

> [!question] Question
> For three input variables, compute basic and robust BVA counts.

> [!answer]- Answer / self-check
> Basic BVA = 4k+1 = 4×3+1 = **13**. Robust BVA = 6k+1 = 6×3+1 = **19**.

### Q11 — Open interval test points

> [!question] Question
> For valid range `1 < x < 100`, which boundary points should be tested?

> [!answer]- Answer / self-check
> For integer input, test the boundaries and immediately-inside values: **1 (ON, invalid), 2 (OFF/inside), 99 (inside), 100 (ON, invalid)**, plus a nominal interior value for a basic set. The key is testing both processing regions adjacent to each open boundary.

### Q12 — BVA limitations

> [!question] Question
> Name three limitations of boundary value analysis.

> [!answer]- Answer / self-check
> BVA assumes faults cluster at boundaries; it does not systematically cover interactions among many parameters; it depends on identifying the right partitions/boundaries; and it does not solve oracle, state/history, timing, or missing-requirement problems. Any three with explanation are sufficient.

### Q13 — Decision-table components

> [!question] Question
> What are the four main components of a decision table?

> [!answer]- Answer / self-check
> **Conditions**, **condition values/entries**, **actions/responses**, and **rules** (columns mapping a combination of condition values to actions).

### Q14 — Decision-table rule count

> [!question] Question
> Three independent binary conditions: how many complete rules before consolidation?

> [!answer]- Answer / self-check
> 2^3 = **8 rules**.

### Q15 — Decision-table checksum

> [!question] Question
> Five consolidated rules cover {2,3,1,4,2} original rules. Is that valid for a 12-rule original table?

> [!answer]- Answer / self-check
> The cover counts sum to 2+3+1+4+2 = **12**, so the checksum passes. You still need to verify the merged rules truly have identical actions and valid don't-care conditions.

### Q16 — Beizer decision-table method

> [!question] Question
> Put the eight decision-table steps in order.

> [!answer]- Answer / self-check
> A useful order: **list actions → list conditions/values → calculate rule count → enumerate combinations → specify actions per rule → consolidate common-action rules with don't-cares → verify checksum → derive tests (one per resulting rule)**.

### Q17 — When decision tables fit

> [!question] Question
> Which scenarios fit decision tables: tax rules, load performance, role/department/time access, continuous temperature prediction?

> [!answer]- Answer / self-check
> Good fits are logic with discrete interacting conditions: **tax calculation** and **access control**. Load-performance behavior and continuous prediction are not primarily decision-table problems.

### Q18 — Low-order interaction finding

> [!question] Question
> What fraction of failures are triggered by one- or two-way parameter interactions?

> [!answer]- Answer / self-check
> The lecture uses the memorable rule **about 90%**; the cited interaction datasets often show roughly **93% cumulative by 2-way**. The point is that pairwise covers a large majority, not all, interaction faults.

### Q19 — 34 binary switches: exhaustive vs pairwise

> [!question] Question
> Compare test counts for all combinations and a pairwise suite.

> [!answer]- Answer / self-check
> Exhaustive = 2^34 = **17,179,869,184** combinations. The lecture example uses about **29 pairwise tests**—an enormous reduction while still covering every value pair.

### Q20 — Selecting interaction strength

> [!question] Question
> Map general UI, business-critical finance, and safety-critical medical software to typical interaction strengths.

> [!answer]- Answer / self-check
> Lecture guideline: **2-way** for general/UI applications; around **3-way** for business-critical systems; **4–6 way** (plus other assurance techniques) for safety-critical/medical contexts. Risk, constraints, and evidence can justify different choices.

### Q21 — Combinatorial-testing limits

> [!question] Question
> Name three limitations of combinatorial testing.

> [!answer]- Answer / self-check
> It depends on correct parameter/value modeling; pairwise misses higher-order interactions; temporal/stateful behavior may not be represented; constraints/masking complicate generation; generated cases still need oracles. Combine it with EP/BVA and other techniques.

### Q22 — Technique matching

> [!question] Question
> Pick the primary technique for numeric range, many configuration options, ATM multi-condition logic, and user-role categories.

> [!answer]- Answer / self-check
> - Numeric range 1–100 → **BVA** (after EP).
> - 20 configuration options → **pairwise/combinatorial**.
> - ATM with interacting rules → **decision table**.
> - Admin/manager/user/guest → **equivalence partitioning**.

### Q23 — Combining input-domain techniques

> [!question] Question
> What order should EP, BVA, decision tables, and pairwise be combined?

> [!answer]- Answer / self-check
> **Start with EP → refine boundaries with BVA → model complex conditional logic with decision tables → use pairwise/combinatorial generation when many parameters make combinations explode.** Pairwise optimizes a model; it should not replace good partitioning.

### Q24 — Why BVA complements EP

> [!question] Question
> Explain why BVA complements rather than replaces equivalence partitioning.

> [!answer]- Answer / self-check
> EP chooses representative values from behaviorally similar regions; BVA targets the edges **between** those regions where off-by-one/closure faults cluster. Example: EP for age {underage, adult, senior}; BVA explicitly tests 17/18 and 64/65 around class boundaries.

### Q25 — Login decision table

> [!question] Question
> Build and consolidate a decision table for username valid?, password valid?, account active?.

> [!answer]- Answer / self-check
> Start with 8 binary combinations. A compact consolidation can be:
> 1. Username invalid → reject (password/account don't care): covers 4.
> 2. Username valid, password invalid → reject: covers 2.
> 3. Username+password valid, account inactive → inactive/blocked: covers 1.
> 4. All valid/active → login success: covers 1.
> Checksum 4+2+1+1=8.

### Q26 — Pairwise-only safety-critical testing

> [!question] Question
> Evaluate using only pairwise testing for a medical-device control system.

> [!answer]- Answer / self-check
> Pairwise alone is insufficient: it intentionally ignores many 3+ way interactions and does not address timing, state, structural coverage, hazards, or oracle quality. Use risk-driven higher-strength combinations plus requirements/hazard analysis, BVA/decision tables, structural criteria such as MC/DC where applicable, static analysis, reviews, and system validation.
