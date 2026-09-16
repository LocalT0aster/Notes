# L07 — Exploratory Testing & Operational Profiles Flashcards

**Source:** https://sqrbok.github.io//content/material/sqr/RQ_L07_Exploratory_OP.html

**Cards:** 30

> [!tip] Active recall
> Answer every part before revealing the answer. For design/essay questions, the answer is a grading checklist: alternative designs can also be correct when justified.

### Q1 — Exploratory testing vs operational-profile testing

> [!question] Question
> State the fundamental difference between ET and operational-profile-based testing.

> [!answer]- Answer / self-check
> **Exploratory testing (ET)** is human, adaptive, qualitative discovery: learning, design, and execution happen together. **Operational-profile (OP) testing** is quantitative: test frequency is allocated according to measured/estimated real usage probabilities, mainly to assess reliability where users spend time.

### Q2 — Why scripted + exploratory improves coverage

> [!question] Question
> What complementary defect classes do scripted and exploratory testing target?

> [!answer]- Answer / self-check
> Scripted tests systematically verify known requirements/regressions and provide repeatability. ET follows observations and heuristics to find unanticipated interactions, usability issues, and edge cases. Combining them covers **known expected behavior + emergent unknown behavior**; “coverage” here is broader than line coverage.

### Q3 — ET vs ad-hoc testing

> [!question] Question
> How is exploratory testing different from unstructured ad-hoc testing?

> [!answer]- Answer / self-check
> ET is structured by **charters, heuristics, time-boxed sessions, notes/results, and debriefing**. Test design is adaptive, but accountable. Ad-hoc testing lacks an explicit mission/process and is harder to reproduce, review, or manage.

### Q4 — Coupon-system ET example

> [!question] Question
> Why did exploratory testing find coupon bugs that scripted cases missed?

> [!answer]- Answer / self-check
> The tester chained unusual actions—reapply coupons, combine with sale items, remove cart items after discount, use multiple tabs. These interactions were outside predefined scripts. ET uses each observation to generate the next hypothesis, so it explores emergent state combinations rather than only specified happy paths.

### Q5 — Exploratory charter

> [!question] Question
> What is a charter and what template should you remember?

> [!answer]- Answer / self-check
> A charter gives a session a mission without prescribing exact steps. Template: **Explore [target] using [resources/heuristics] to discover [information/risks].** It focuses exploration and makes the session reviewable.

### Q6 — Hendrickson heuristics

> [!question] Question
> Describe three exploratory-testing heuristics with examples.

> [!answer]- Answer / self-check
> Any three: **None/Some/All** (permissions/items); **Too Big/Too Small/Just Right** (upload sizes); **Zero/One/Many** (item count); **Beginning/Middle/End** (position); **CRUD**; data-type attacks; injection. A good answer names the heuristic, the perturbation, and the likely defect class.

### Q7 — Session-Based Test Management

> [!question] Question
> Why was SBTM created and what are its four pillars?

> [!answer]- Answer / self-check
> SBTM makes exploratory work **manageable and auditable** without scripting it. Four pillars: **Charter, Time box (often 60–120 min), Reviewable result/notes, Debriefing**.

### Q8 — Whittaker's five districts

> [!question] Question
> Name Whittaker's five exploratory-testing districts and their focus.

> [!answer]- Answer / self-check
> - **Business:** core value/features.
> - **Historical:** legacy/bug-prone areas.
> - **Entertainment:** unusual/adversarial behavior.
> - **Tourist:** first-time/visible user experience.
> - **Hotel:** background/supporting/long-running operations.
> Specific tours sit inside these districts.

### Q9 — Five levels of exploration

> [!question] Question
> Describe the five levels from freestyle to fully scripted and when to use them.

> [!answer]- Answer / self-check
> 1. **Freestyle:** only product; maximum discovery, least repeatability.
> 2. **High exploration:** charter/goals.
> 3. **Medium:** charter + starting points/data.
> 4. **Low exploration:** detailed activities but tester judgment remains.
> 5. **Fully scripted:** exact steps/results.
> Use more exploration for discovery/uncertainty; more scripting for repeatability/regulatory regression.

### Q10 — Evidence for ET effectiveness

> [!question] Question
> Summarize the empirical evidence cited for exploratory testing.

> [!answer]- Answer / self-check
> Lecture summary: ET often finds **similar defect counts with much less total effort**, reported as roughly **4–6× more efficient** in some comparisons; equal-time experiments found substantially more defects (about **4.6×** in one study); usability defects were especially strong; industry surveys report high adoption (~**88%**). Context and tester skill matter.

### Q11 — Responding to “ET is just ad-hoc”

> [!question] Question
> How would you rebut that claim with process and evidence?

> [!answer]- Answer / self-check
> Show structure: charters, heuristics, time boxes, session notes, debriefing, coverage/risk notes, and regression conversion. Then cite evidence that controlled studies found ET comparable or better in defect detection/efficiency. The key difference is **adaptive design with accountability**, not absence of method.

### Q12 — The ET coverage paradox

> [!question] Question
> Why can ET achieve lower structural coverage but comparable defect counts?

> [!answer]- Answer / self-check
> Coverage records **where execution went**, not how fault-revealing the inputs/oracles were. ET concentrates on anomalies, boundaries, interactions, and defect-dense areas rather than uniformly traversing code. It can therefore get more fault information per executed path while leaving benign code uncovered.

### Q13 — Operational profile definition

> [!question] Question
> Define an operational profile and give probabilities.

> [!answer]- Answer / self-check
> An OP is the **set of operations and their occurrence probabilities** for a defined user population/mode. Example: login 0.20, search 0.50, checkout 0.20, account admin 0.10; probabilities sum to 1. It is a quantitative model of real use.

### Q14 — Function vs operation vs run

> [!question] Question
> Distinguish Musa's function, operation, and run.

> [!answer]- Answer / self-check
> - **Function:** user-visible capability/requirement, e.g. relocate telephone.
> - **Operation:** design-level task invoked to provide a function, e.g. remove + install.
> - **Run:** one concrete execution of an operation.
> The OP is usually built at operation/run granularity useful for testing.

### Q15 — Operational mode

> [!question] Question
> What is an operational mode? Give examples.

> [!answer]- Answer / self-check
> A mode is a context with a distinct usage distribution. Examples: **peak vs off-peak**, **customer vs admin**, **normal vs degraded/maintenance**, **novice vs expert**, **normal vs emergency**. The same operation can have different probability in each mode.

### Q16 — Why probabilities sum to 1

> [!question] Question
> Why must OP probabilities total 1.0?

> [!answer]- Answer / self-check
> They represent a complete probability distribution over mutually considered operations in the mode. A sum >1 double-counts/over-allocates probability; <1 means missing/unallocated behavior. Rates should be normalized: p_i = rate_i / Σ rates.

### Q17 — Musa six-step OP procedure

> [!question] Question
> Walk through the six steps for a university enrollment system.

> [!answer]- Answer / self-check
> 1. Determine **operational modes** (registration peak/normal).
> 2. Identify **initiators** (students, staff, scheduled jobs).
> 3. Choose **representation** (table/tree).
> 4. List **operations** (search course, enroll, drop, pay, etc.).
> 5. Estimate/measure **occurrence rates** from logs/surveys.
> 6. Normalize to **probabilities** and validate with stakeholders.

### Q18 — Tabular vs graphical OP

> [!question] Question
> When should an OP be tabular vs graphical?

> [!answer]- Answer / self-check
> Use a **table** for a small/flat operation set with one/few initiator types. Use a **graph/tree** when there are multiple initiator classes, modes, or hierarchical operations and the structure aids understanding. Start simple; add hierarchy when it reduces ambiguity.

### Q19 — Operational-profile calculation

> [!question] Question
> Rates are GET /users 4000, POST /orders 2500, GET /products 3000, PUT /users 500 per hour. Compute probabilities.

> [!answer]- Answer / self-check
> Total = **10,000/hr**. Probabilities:
> - GET /users = **0.40**
> - POST /orders = **0.25**
> - GET /products = **0.30**
> - PUT /users = **0.05**
> Sum = 1.00.

### Q20 — AT&T and HP operational-profile results

> [!question] Question
> What industrial results are cited for OP adoption?

> [!answer]- Answer / self-check
> Lecture summary: **AT&T Definity PBX** reported about **10× fewer customer problems** and roughly halved the test cycle; **HP** reported at least **50% reduction in test time/cost**. Treat these as historical case evidence, not universal guarantees.

### Q21 — Operational coverage

> [!question] Question
> Define operational coverage and contrast it with traditional coverage.

> [!answer]- Answer / self-check
> Traditional coverage weights each code element equally. **Operational coverage weights coverage by usage probability**: roughly Σ(coverage of operation_i × usage_i). It asks whether the suite covers what users actually do frequently, making it more relevant to reliability under field usage.

### Q22 — Android Cloud Profiles

> [!question] Question
> What are Android Cloud Profiles and what key numbers matter?

> [!answer]- Answer / self-check
> They are usage-derived profiles of methods exercised by real Android users, used to guide optimization/testing relevance. Lecture figures: profiles available for about **99.89%** of top apps; average profile size about **7.88% of methods**; automated tools reached <~70% of profile coverage. The striking point is how small the actually-used method slice can be.

### Q23 — OP–ET saturation handoff

> [!question] Question
> Why do OP and ET complement each other?

> [!answer]- Answer / self-check
> OP efficiently covers high-probability behavior first. As automated/usage-driven coverage saturates (lecture discussion around **~70%**), additional OP tests yield diminishing novelty. ET then targets the remaining uncertain/rare/interacting behavior with human reasoning—**quantitative first, qualitative exploration next**.

### Q24 — Two-phase testing strategy

> [!question] Question
> Describe the OP→ET strategy and why OP comes first.

> [!answer]- Answer / self-check
> Phase 1: build OP, allocate tests by usage, measure operational coverage, continue until saturation. Phase 2: use ET charters/tours focused by OP/risk, discover edge/usability/interaction defects, convert discoveries to regression tests. OP first cheaply secures common real-world behavior and gives ET a risk map.

### Q25 — Startup: OP or ET first?

> [!question] Question
> A startup has little test time. Should it build an OP or train testers in ET?

> [!answer]- Answer / self-check
> It depends on evidence. If it has reliable telemetry and a stability/reliability goal, a lightweight OP quickly prioritizes scarce test effort. If usage is still changing and telemetry is sparse, **ET may deliver more value first** because it explores uncertainty. A pragmatic startup often starts with simple telemetry-derived frequencies + a few high-risk ET charters.

### Q26 — Accountability: SBTM vs OP

> [!question] Question
> Compare how SBTM and operational profiles make testing accountable.

> [!answer]- Answer / self-check
> **SBTM** accountability is qualitative/session-based: charter, time spent, notes, findings, debrief. **OP** accountability is quantitative: operation list, rates/probabilities, allocated tests, operational coverage/reliability results. One records reasoning/work; the other records usage-weighted allocation/evidence.

### Q27 — Banking-app OP + ET strategy

> [!question] Question
> Design a combined strategy for a mobile banking app.

> [!answer]- Answer / self-check
> OP: derive frequencies for login, balance, transfer, bill pay, card controls; weight regression/reliability runs accordingly and split modes (normal/peak/fraud incident). ET charters: transfer limits/boundaries, concurrent sessions, interrupted network, stale balances, role/security tours, money-tour around fees/rounding. Convert every confirmed ET defect to regression.

### Q28 — Operational vs traditional coverage

> [!question] Question
> Why can operational coverage be a more useful signal?

> [!answer]- Answer / self-check
> It discounts rarely used code and emphasizes heavily used behavior, so it aligns coverage with **field failure exposure** rather than code size alone. This helps reliability decisions; however rare safety/security paths can still be critical and must be covered by risk analysis even if usage probability is tiny.

### Q29 — What Cloud Profiles teach about assumptions

> [!question] Question
> How do Android Cloud Profiles support “you cannot assume how users use software”?

> [!answer]- Answer / self-check
> Observed profiles are sparse and differ from developer-authored baseline expectations; automated model-based explorers also miss a significant share of user-relevant behavior. The evidence says design intuition/test models are imperfect proxies for field usage—collect telemetry where possible and preserve exploration for the unknown remainder.

### Q30 — Five-minute L07 summary

> [!question] Question
> Give a compact explanation of ET, OP, and their bridge.

> [!answer]- Answer / self-check
> ET = adaptive human discovery with charters/heuristics/SBTM. OP = quantitative operation probabilities used to prioritize tests and estimate reliability. OP gives efficient coverage of common behavior; ET finds emergent/rare/interacting problems. A strong strategy uses **OP first for usage-weighted confidence, ET after saturation, then regression-script discoveries**.
