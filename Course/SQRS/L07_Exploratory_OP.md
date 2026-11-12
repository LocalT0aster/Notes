# L07 — Exploratory Testing & Operational Profiles Flashcards

**Source:** https://sqrbok.github.io/content/material/sqr/RQ_L07_Exploratory_OP.html

**Study notes:** https://sqrbok.github.io/content/material/sqr/SN_L07_Exploratory_OP.html

**Cards:** 30

> [!tip] Active recall
> Questions are copied verbatim from the pinned SQRBOK source. Answers are locally synthesized self-checks, not official model answers.

### Q1 — ET vs OP Fundamental Difference

**Card ID:** l07-exploratory-op-001

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L07_Exploratory_OP.html#question-1-et-vs-op-fundamental-difference

> [!question] Question
> ## Question 1: ET vs OP Fundamental Difference
>
> What is the fundamental difference between exploratory testing and operational profile-based testing?

> [!answer]- Answer / self-check
> **Exploratory testing (ET)** is human, adaptive, qualitative discovery: learning, design, and execution happen together. **Operational-profile (OP) testing** is quantitative: test frequency is allocated according to measured/estimated real usage probabilities, mainly to assess reliability where users spend time.

### Q2 — Scripted and Exploratory Together

**Card ID:** l07-exploratory-op-002

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L07_Exploratory_OP.html#question-2-scripted-and-exploratory-together

> [!question] Question
> ## Question 2: Scripted and Exploratory Together
>
> Why does the lecture recommend using scripted and exploratory testing together? What does each approach do well, and what does each miss?

> [!answer]- Answer / self-check
> Scripted tests systematically verify known requirements/regressions and provide repeatability. ET follows observations and heuristics to find unanticipated interactions, usability issues, and edge cases. Combining them covers **known expected behavior + emergent unknown behavior**; “coverage” here is broader than line coverage.

### Q3 — ET vs Ad-Hoc Testing

**Card ID:** l07-exploratory-op-003

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L07_Exploratory_OP.html#question-3-et-vs-ad-hoc-testing

> [!question] Question
> ## Question 3: ET vs Ad-Hoc Testing
>
> How does exploratory testing differ from ad-hoc testing?

> [!answer]- Answer / self-check
> ET is structured by **charters, heuristics, time-boxed sessions, notes/results, and debriefing**. Test design is adaptive, but accountable. Ad-hoc testing lacks an explicit mission/process and is harder to reproduce, review, or manage.

### Q4 — Coupon System Example

**Card ID:** l07-exploratory-op-004

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L07_Exploratory_OP.html#question-4-coupon-system-example

> [!question] Question
> ## Question 4: Coupon System Example
>
> Explain the coupon system example. Why couldn't scripted testing find those bugs?

> [!answer]- Answer / self-check
> The tester chained unusual actions—reapply coupons, combine with sale items, remove cart items after discount, use multiple tabs. These interactions were outside predefined scripts. ET uses each observation to generate the next hypothesis, so it explores emergent state combinations rather than only specified happy paths.

### Q5 — Charter Definition

**Card ID:** l07-exploratory-op-005

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L07_Exploratory_OP.html#question-5-charter-definition

> [!question] Question
> ## Question 5: Charter Definition
>
> What is a charter and why is it important for exploratory testing? Give the template format.

> [!answer]- Answer / self-check
> A charter gives a session a mission without prescribing exact steps. Template: **Explore [target] using [resources/heuristics] to discover [information/risks].** It focuses exploration and makes the session reviewable.

### Q6 — Hendrickson's Heuristics

**Card ID:** l07-exploratory-op-006

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L07_Exploratory_OP.html#question-6-hendricksons-heuristics

> [!question] Question
> ## Question 6: Hendrickson's Heuristics
>
> Describe three of Hendrickson's heuristics and give an example for each.

> [!answer]- Answer / self-check
> Any three: **None/Some/All** (permissions/items); **Too Big/Too Small/Just Right** (upload sizes); **Zero/One/Many** (item count); **Beginning/Middle/End** (position); **CRUD**; data-type attacks; injection. A good answer names the heuristic, the perturbation, and the likely defect class.

### Q7 — Session-Based Test Management

**Card ID:** l07-exploratory-op-007

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L07_Exploratory_OP.html#question-7-session-based-test-management

> [!question] Question
> ## Question 7: Session-Based Test Management
>
> Explain Session-Based Test Management (SBTM). Why was it created? What are its four parts?

> [!answer]- Answer / self-check
> SBTM makes exploratory work **manageable and auditable** without scripting it. Four pillars: **Charter, Time box (often 60–120 min), Reviewable result/notes, Debriefing**.

### Q8 — Whittaker's Districts

**Card ID:** l07-exploratory-op-008

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L07_Exploratory_OP.html#question-8-whittakers-districts

> [!question] Question
> ## Question 8: Whittaker's Districts
>
> Name four of Whittaker's tour districts, say what each focuses on, and give one tour from each.

> [!answer]- Answer / self-check
> - **Business:** core value/features.
> - **Historical:** legacy/bug-prone areas.
> - **Entertainment:** unusual/adversarial behavior.
> - **Tourist:** first-time/visible user experience.
> - **Hotel:** background/supporting/long-running operations.
> Specific tours sit inside these districts.

### Q9 — Five Levels of Exploration

**Card ID:** l07-exploratory-op-009

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L07_Exploratory_OP.html#question-9-five-levels-of-exploration

> [!question] Question
> ## Question 9: Five Levels of Exploration
>
> Describe the five levels of exploration (Ghazi et al. 2017). When should you use each?

> [!answer]- Answer / self-check
> 1. **Freestyle:** only product; maximum discovery, least repeatability.
> 2. **High exploration:** charter/goals.
> 3. **Medium:** charter + starting points/data.
> 4. **Low exploration:** detailed activities but tester judgment remains.
> 5. **Fully scripted:** exact steps/results.
> Use more exploration for discovery/uncertainty; more scripting for repeatability/regulatory regression.

### Q10 — ET Effectiveness Evidence

**Card ID:** l07-exploratory-op-010

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L07_Exploratory_OP.html#question-10-et-effectiveness-evidence

> [!question] Question
> ## Question 10: ET Effectiveness Evidence
>
> Summarize the experimental evidence comparing ET with test-case-based testing. What did the experiments measure, what did they find for defects and for effort, and how does a fixed total time change the result?

> [!answer]- Answer / self-check
> Lecture summary: ET often finds **similar defect counts with much less total effort**, reported as roughly **4–6× more efficient** in some comparisons; equal-time experiments found substantially more defects (about **4.6×** in one study); usability defects were especially strong; industry surveys report high adoption (~**88%**). Context and tester skill matter.

### Q11 — Defending ET to Management

**Card ID:** l07-exploratory-op-011

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L07_Exploratory_OP.html#question-11-defending-et-to-management

> [!question] Question
> ## Question 11: Defending ET to Management
>
> A manager says "ET is just ad-hoc testing." How would you respond with evidence?

> [!answer]- Answer / self-check
> Show structure: charters, heuristics, time boxes, session notes, debriefing, coverage/risk notes, and regression conversion. Then cite evidence that controlled studies found ET comparable or better in defect detection/efficiency. The key difference is **adaptive design with accountability**, not absence of method.

### Q12 — More Defects, Less Coverage

**Card ID:** l07-exploratory-op-012

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L07_Exploratory_OP.html#question-12-more-defects-less-coverage

> [!question] Question
> ## Question 12: More Defects, Less Coverage
>
> In Shah et al.'s comparison, exploratory testing found the most defects but covered the fewest specified functions. How can both be true, and what does it imply for planning tests?

> [!answer]- Answer / self-check
> Coverage records **where execution went**, not how fault-revealing the inputs/oracles were. ET concentrates on anomalies, boundaries, interactions, and defect-dense areas rather than uniformly traversing code. It can therefore get more fault information per executed path while leaving benign code uncovered.

### Q13 — Operational Profile Definition

**Card ID:** l07-exploratory-op-013

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L07_Exploratory_OP.html#question-13-operational-profile-definition

> [!question] Question
> ## Question 13: Operational Profile Definition
>
> What is an operational profile? Give a concrete example with probabilities.

> [!answer]- Answer / self-check
> An OP is the **set of operations and their occurrence probabilities** for a defined user population/mode. Example: login 0.20, search 0.50, checkout 0.20, account admin 0.10; probabilities sum to 1. It is a quantitative model of real use.

### Q14 — Function vs Operation vs Run

**Card ID:** l07-exploratory-op-014

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L07_Exploratory_OP.html#question-14-function-vs-operation-vs-run

> [!question] Question
> ## Question 14: Function vs Operation vs Run
>
> Explain the difference between a function, an operation, and a run (Musa 1993).

> [!answer]- Answer / self-check
> - **Function:** user-visible capability/requirement, e.g. relocate telephone.
> - **Operation:** design-level task invoked to provide a function, e.g. remove + install.
> - **Run:** one concrete execution of an operation.
> The OP is usually built at operation/run granularity useful for testing.

### Q15 — Operational Modes

**Card ID:** l07-exploratory-op-015

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L07_Exploratory_OP.html#question-15-operational-modes

> [!question] Question
> ## Question 15: Operational Modes
>
> What is an operational mode? Give three examples.

> [!answer]- Answer / self-check
> A mode is a context with a distinct usage distribution. Examples: **peak vs off-peak**, **customer vs admin**, **normal vs degraded/maintenance**, **novice vs expert**, **normal vs emergency**. The same operation can have different probability in each mode.

### Q16 — Profile Probabilities Sum to 1.0

**Card ID:** l07-exploratory-op-016

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L07_Exploratory_OP.html#question-16-profile-probabilities-sum-to-10

> [!question] Question
> ## Question 16: Profile Probabilities Sum to 1.0
>
> Why must operational profile probabilities sum to 1.0? What happens if the sum is greater or less?

> [!answer]- Answer / self-check
> They represent a complete probability distribution over mutually considered operations in the mode. A sum >1 double-counts/over-allocates probability; <1 means missing/unallocated behavior. Rates should be normalized: p_i = rate_i / Σ rates.

### Q17 — 6-Step OP Procedure

**Card ID:** l07-exploratory-op-017

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L07_Exploratory_OP.html#question-17-6-step-op-procedure

> [!question] Question
> ## Question 17: 6-Step OP Procedure
>
> Walk through the six-step OP procedure using a university enrollment system as an example.

> [!answer]- Answer / self-check
> 1. Determine **operational modes** (registration peak/normal).
> 2. Identify **initiators** (students, staff, scheduled jobs).
> 3. Choose **representation** (table/tree).
> 4. List **operations** (search course, enroll, drop, pay, etc.).
> 5. Estimate/measure **occurrence rates** from logs/surveys.
> 6. Normalize to **probabilities** and validate with stakeholders.

### Q18 — Tabular vs Graphical Representation

**Card ID:** l07-exploratory-op-018

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L07_Exploratory_OP.html#question-18-tabular-vs-graphical-representation

> [!question] Question
> ## Question 18: Tabular vs Graphical Representation
>
> When should you use tabular vs. graphical (tree) representation for an operational profile?

> [!answer]- Answer / self-check
> Use a **table** for a small/flat operation set with one/few initiator types. Use a **graph/tree** when there are multiple initiator classes, modes, or hierarchical operations and the structure aids understanding. Start simple; add hierarchy when it reduces ambiguity.

### Q19 — OP Calculation (Practical)

**Card ID:** l07-exploratory-op-019

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L07_Exploratory_OP.html#question-19-op-calculation-practical

> [!question] Question
> ## Question 19: OP Calculation (Practical)
>
> Calculate the operational profile for this system:
>
> | Endpoint | Rate/hr |
> |----------|---------|
> | GET /users | 4,000 |
> | POST /orders | 2,500 |
> | GET /products | 3,000 |
> | PUT /users | 500 |

> [!answer]- Answer / self-check
> Total = **10,000/hr**. Probabilities:
> - GET /users = **0.40**
> - POST /orders = **0.25**
> - GET /products = **0.30**
> - PUT /users = **0.05**
> Sum = 1.00.

### Q20 — AT&T and HP Results

**Card ID:** l07-exploratory-op-020

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L07_Exploratory_OP.html#question-20-att-and-hp-results

> [!question] Question
> ## Question 20: AT&T and HP Results
>
> What were the results of OP adoption at AT&T and HP? Why should the AT&T figure not be quoted as the effect of the profile alone?

> [!answer]- Answer / self-check
> Lecture summary: **AT&T Definity PBX** reported about **10× fewer customer problems** and roughly halved the test cycle; **HP** reported at least **50% reduction in test time/cost**. Treat these as historical case evidence, not universal guarantees.

### Q21 — Operational Coverage

**Card ID:** l07-exploratory-op-021

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L07_Exploratory_OP.html#question-21-operational-coverage

> [!question] Question
> ## Question 21: Operational Coverage
>
> Explain usage-weighted coverage and operational coverage (the published 1/3/9 rule), each with a worked example. How do they differ from traditional coverage?

> [!answer]- Answer / self-check
> Traditional coverage weights each code element equally. **Operational coverage weights coverage by usage probability**: roughly Σ(coverage of operation_i × usage_i). It asks whether the suite covers what users actually do frequently, making it more relevant to reliability under field usage.

### Q22 — Android Cloud Profiles

**Card ID:** l07-exploratory-op-022

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L07_Exploratory_OP.html#question-22-android-cloud-profiles

> [!question] Question
> ## Question 22: Android Cloud Profiles
>
> What are Android Cloud Profiles and why do they matter? What percentage of methods do users exercise?

> [!answer]- Answer / self-check
> They are usage-derived profiles of methods exercised by real Android users, used to guide optimization/testing relevance. Lecture figures: profiles available for about **99.89%** of top apps; average profile size about **7.88% of methods**; automated tools reached <~70% of profile coverage. The striking point is how small the actually-used method slice can be.

### Q23 — Saturation

**Card ID:** l07-exploratory-op-023

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L07_Exploratory_OP.html#question-23-saturation

> [!question] Question
> ## Question 23: Saturation
>
> What is saturation in profile-based testing? Why do OP and ET complement each other once it occurs? No study gives a threshold for switching: which signals would you use to decide?

> [!answer]- Answer / self-check
> OP efficiently covers high-probability behavior first. As automated/usage-driven coverage saturates (lecture discussion around **~70%**), additional OP tests yield diminishing novelty. ET then targets the remaining uncertain/rare/interacting behavior with human reasoning—**quantitative first, qualitative exploration next**.

### Q24 — Two-Phase Testing Strategy

**Card ID:** l07-exploratory-op-024

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L07_Exploratory_OP.html#question-24-two-phase-testing-strategy

> [!question] Question
> ## Question 24: Two-Phase Testing Strategy
>
> Describe the two-phase testing strategy. When should OP come first, and what would you do first without usage data?

> [!answer]- Answer / self-check
> Phase 1: build OP, allocate tests by usage, measure operational coverage, continue until saturation. Phase 2: use ET charters/tours focused by OP/risk, discover edge/usability/interaction defects, convert discoveries to regression tests. OP first cheaply secures common real-world behavior and gives ET a risk map.

### Q25 — Startup Testing Decision

**Card ID:** l07-exploratory-op-025

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L07_Exploratory_OP.html#question-25-startup-testing-decision

> [!question] Question
> ## Question 25: Startup Testing Decision
>
> A startup has limited testing time. Should they build an OP or train testers in ET? Why?

> [!answer]- Answer / self-check
> It depends on evidence. If it has reliable telemetry and a stability/reliability goal, a lightweight OP quickly prioritizes scarce test effort. If usage is still changing and telemetry is sparse, **ET may deliver more value first** because it explores uncertainty. A pragmatic startup often starts with simple telemetry-derived frequencies + a few high-risk ET charters.

### Q26 — Accountability Mechanisms

**Card ID:** l07-exploratory-op-026

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L07_Exploratory_OP.html#question-26-accountability-mechanisms

> [!question] Question
> ## Question 26: Accountability Mechanisms
>
> SBTM makes exploratory testing reportable through session reports and debriefings. What does an operational profile, together with operational coverage, give a manager to judge how much testing each operation received and when usage-based testing is enough?

> [!answer]- Answer / self-check
> **SBTM** accountability is qualitative/session-based: charter, time spent, notes, findings, debrief. **OP** accountability is quantitative: operation list, rates/probabilities, allocated tests, operational coverage/reliability results. One records reasoning/work; the other records usage-weighted allocation/evidence.

### Q27 — Banking App Strategy (Practical)

**Card ID:** l07-exploratory-op-027

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L07_Exploratory_OP.html#question-27-banking-app-strategy-practical

> [!question] Question
> ## Question 27: Banking App Strategy (Practical)
>
> Design a testing strategy for a banking mobile app using both OP and ET. Include specific charters and tours.

> [!answer]- Answer / self-check
> OP: derive frequencies for login, balance, transfer, bill pay, card controls; weight regression/reliability runs accordingly and split modes (normal/peak/fraud incident). ET charters: transfer limits/boundaries, concurrent sessions, interrupted network, stale balances, role/security tours, money-tour around fees/rounding. Convert every confirmed ET defect to regression.

### Q28 — Operational vs Traditional Coverage

**Card ID:** l07-exploratory-op-028

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L07_Exploratory_OP.html#question-28-operational-vs-traditional-coverage

> [!question] Question
> ## Question 28: Operational vs Traditional Coverage
>
> Why does coverage weighted by use (usage-weighted or operational) give a more useful signal than traditional coverage? Name which one you use.

> [!answer]- Answer / self-check
> It discounts rarely used code and emphasizes heavily used behavior, so it aligns coverage with **field failure exposure** rather than code size alone. This helps reliability decisions; however rare safety/security paths can still be critical and must be covered by risk analysis even if usage probability is tiny.

### Q29 — Cloud Profiles Validation

**Card ID:** l07-exploratory-op-029

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L07_Exploratory_OP.html#question-29-cloud-profiles-validation

> [!question] Question
> ## Question 29: Cloud Profiles Validation
>
> Explain how Android Cloud Profiles support the claim "you cannot assume how users will use your software." What did comparing test tools by profile coverage show?

> [!answer]- Answer / self-check
> Observed profiles are sparse and differ from developer-authored baseline expectations; automated model-based explorers also miss a significant share of user-relevant behavior. The evidence says design intuition/test models are imperfect proxies for field usage—collect telemetry where possible and preserve exploration for the unknown remainder.

### Q30 — Lecture Summary

**Card ID:** l07-exploratory-op-030

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L07_Exploratory_OP.html#question-30-lecture-summary

> [!question] Question
> ## Question 30: Lecture Summary
>
> Explain the entire lecture in 5 minutes. Cover ET, OP, and how they bridge together.

> [!answer]- Answer / self-check
> ET = adaptive human discovery with charters/heuristics/SBTM. OP = quantitative operation probabilities used to prioritize tests and estimate reliability. OP gives efficient coverage of common behavior; ET finds emergent/rare/interacting problems. A strong strategy uses **OP first for usage-weighted confidence, ET after saturation, then regression-script discoveries**.
