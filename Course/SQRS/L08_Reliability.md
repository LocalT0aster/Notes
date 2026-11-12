# L08 — Software Reliability Flashcards

**Source:** https://sqrbok.github.io/content/material/sqr/RQ_L08_Reliability.html

**Cards:** 17

> [!tip] Active recall
> Answer every part before revealing the answer. For design/essay questions, the answer is a grading checklist: alternative designs can also be correct when justified.

### Q1 — Fault → error → failure in a real incident

> [!question] Question
> Trace one real incident through fault, error, and failure.

> [!answer]- Answer / self-check
> Use one case and keep levels distinct. Example CrowdStrike 2024: **fault** = invalid content/update accepted by validation/design; **error** = sensor/kernel code enters invalid memory/state while parsing it; **failure** = Windows hosts crash/boot-loop visibly. Fault is latent cause, error is incorrect internal state, failure is externally observed service deviation.
> For the source's server example: missing length check = **fault**; request >8 KB = **activation**; corrupt/invalid internal state = **error**; crash = **failure**. A dormant fault can exist during months with no triggering requests. Musa's “error” is a programmer's mistake; Avizienis's is a wrong system state; state which vocabulary you use.

### Q2 — Hardware vs software reliability curves

> [!question] Question
> Why does the hardware bathtub curve not apply to software?

> [!answer]- Answer / self-check
> Hardware has physical infant mortality and wear-out. Software does **not physically wear**: the same binary fails on triggering states/inputs. Its observed failure rate usually decreases as faults are removed, with spikes after changes that introduce new faults—often a downward/sawtooth pattern rather than a wear-out curve.

### Q3 — Failure Severity Classification

> [!question] Question
> Design four severity classes for a hospital patient portal.

> [!answer]- Answer / self-check
> Use **human-life/capability impact** as the primary criterion. Example: C1 life-threatening wrong/hidden critical result; C2 severe clinical delay/data corruption; C3 non-critical feature outage with workaround; C4 cosmetic/minor inconvenience. Define objective boundaries and examples so stakeholders classify failures consistently.

### Q4 — FIO from availability

> [!question] Question
> A=99.9%, mean downtime per failure=2 min=1/30 h. Compute exact and approximate λ, MTTF and the lecture's expected failures over 720 h.

> [!answer]- Answer / self-check
> λ=(1−A)/(A×t_m)=0.001/(0.999/30) ≈ **0.030030 failures/operating-hour**. MTTF=1/λ = **33.3 h**. The lecture's λ×720 estimate is **21.62 failures**; accounting for uptime in 720 calendar hours gives λ×A×720 = **21.6**. Approximation λ≈(1−A)/t_m = **0.03/h**, 0.1% below exact. Keep 2/60 exact until the final rounding. High availability can coexist with frequent failures when recovery is fast.

### Q5 — When failure metrics mislead

> [!question] Question
> Give cases where failure density and failure intensity each hide a reliability problem.

> [!answer]- Answer / self-check
> Low **failure density** can still be dangerous if one defect lies on a hot path used constantly → high failure intensity. Low average **failure intensity** can hide severe user unreliability if failures cluster by user/mode, are correlated, or have catastrophic severity. Always pair frequency with exposure, severity, and operational profile.

### Q6 — Fault prevention vs fault tolerance

> [!question] Question
> Compare prevention and tolerance for meeting an FIO.

> [!answer]- Answer / self-check
> **Prevention** reduces introduced faults (reviews, safer design, standards) and is cheapest early, but cannot guarantee zero faults. **Tolerance** continues correct/acceptable service despite faults (redundancy, retries, failover, recovery) and is vital when failures are unavoidable/critical, but adds complexity/cost and may suffer common-mode failures. Use both by risk.

### Q7 — Backward recovery and domino effect

> [!question] Question
> Explain rollback in a two-service order/ship scenario and contrast forward recovery.

> [!answer]- Answer / self-check
> If A rolls back after it already sent “ship” to B, A's restored state no longer matches B's committed action. To regain consistency B may also need rollback/compensation, possibly forcing further rollbacks—the **domino effect**. Forward recovery instead moves to a new consistent state, e.g. compensating transaction/cancel shipment, without rewinding all participants.

### Q8 — Goel–Okumoto release calculation

> [!question] Question
> Given a=80 faults, b=0.03/week, FIO=1/week, compute λ(0), λ(20), time to FIO, and faults found by release.

> [!answer]- Answer / self-check
> λ(t)=ab·e^(−bt), m(t)=a(1−e^(−bt)).
> - λ(0)=80×0.03 = **2.4/week**.
> - λ(20)=2.4e^-0.6 ≈ **1.317/week**.
> - Set 1=2.4e^-0.03t → t≈ **29.18 weeks**.
> - m(t)=80(1−1/2.4)≈ **46.7 faults** found.
> Remaining faults = a·e^(−bt)=FIO/b=**33.3** (expected counts need not be integers).

### Q9 — Why N-version independence fails

> [!question] Question
> Summarize Knight & Leveson and why it matters.

> [!answer]- Answer / self-check
> The current source reports **27 independently developed versions** of an anti-missile program, tested on **1,000,000 random cases**. Two or more versions failed together in **1,255 cases versus 127 predicted** under independence (about **9.9×**); independence was rejected at 99% confidence. Shared logical slips, finite-precision arithmetic and hard inputs caused correlated failures. Diversity can help, but multiplying independent reliabilities overstates its benefit when that assumption fails.

### Q10 — Three-version majority voting

> [!question] Question
> Each version has Rc=0.95. Compute independent 2-of-3 reliability. Then use a mixture: 1% of inputs fail all three versions; otherwise each independently fails with probability 0.04.

> [!answer]- Answer / self-check
> Independent majority reliability = 3R²(1−R)+R³ = **0.99275**. Mixture failure probability = 0.01 + 0.99×(3×0.04²×0.96+0.04³) = **0.01462528**; reliability = **0.98537472**. The mixture's component reliability is 1−(0.01+0.99×0.04)=0.9504, approximately 0.95. A voter cannot mask an input that defeats all versions together.

### Q11 — SLO error budget

> [!question] Question
> For a 99.95% successful-request SLO over 30 days and 50M evenly spread requests, calculate the budget and consumption by A: 6 min full outage; B: 3 min full outage; C: 4000 failed requests. Postmortems are required above 20% per incident; freeze only when the whole budget is spent.

> [!answer]- Answer / self-check
> Budget = 50M×0.0005 = **25,000 failed requests**, equivalent to **21.6 minutes** of full outage under uniform traffic. Rate=50M/43,200≈1157.407 requests/min. **A:** ≈6944.44 failures, **27.78%** of budget; **B:** ≈3472.22, **13.89%**; **C:** 4000, **16%**. Total ≈14,416.67 failures, **57.67%** spent, **42.33%** left. Only A exceeds the strict >20% postmortem threshold; shipping may continue under the stated policy. Use a common request denominator; the time conversion depends on uniform traffic.

### Q12 — FIO vs SLO

> [!question] Question
> Explain how FIO and SLO express the same underlying idea in different eras/contexts.

> [!answer]- Answer / self-check
> Both set a **quantitative acceptable failure level** rather than demanding perfection. FIO is framed as allowable failure intensity during reliability engineering/testing; SLO sets a target for production service indicators. λ(t) corresponds to an error/failure-rate SLI, and “just-right reliability” corresponds to spending an **error budget** instead of overengineering beyond business need.
> A 100% target leaves zero room for failures and change; its cost can exceed user benefit. Choose objectives by consequence, operating conditions and economic value rather than assuming perfect reliability is attainable.

### Q13 — Ariane 5 and identical backups

> [!question] Question
> Trace Ariane 5 flight 501 through fault–activation–error–failure, and explain why its backup did not protect it.

> [!answer]- Answer / self-check
> **Fault:** an unprotected 64-to-16-bit conversion in reused inertial-reference code. **Activation:** Ariane 5's flight values exceeded the Ariane 4 assumption. **Error:** overflow exception. **Component failure:** inertial computer shutdown; diagnostic data were then treated as flight data, leading to destructive commands and loss of the rocket. The backup ran the same faulty logic under the same conditions and failed too: identical redundancy does not remove common-mode design faults.

### Q14 — Derive reliability from failure data

> [!question] Question
> Four failures occur in 2000 operating hours; mean downtime per failure is 2 hours. Compute λ, MTTF, R(24 h) and availability. State assumptions.

> [!answer]- Answer / self-check
> **λ=4/2000=0.002/h; MTTF=1/λ=500 h**. Assuming stable use and a constant failure intensity with exponential time to failure, **R(24)=e^(−0.002×24)≈0.95313**. Steady-state availability **A=500/(500+2)≈0.996016=99.6016%**. A point estimate from four failures has substantial uncertainty; the exponential model is an assumption, not a consequence of the count.

### Q15 — FIO from a mission reliability target

> [!question] Question
> Require R(4 h)≥0.995. What maximum failure intensity follows under a constant-intensity model?

> [!answer]- Answer / self-check
> R(t)=e^(−λt), so **λ≤−ln(0.995)/4≈0.00125314/h** (about one failure per 798 operating hours). Use common time units and the intended operational profile; changing usage or nonconstant intensity invalidates a simple extrapolation.

### Q16 — Growth-model limits under continuous delivery

> [!question] Question
> Why does fitting one reliability growth curve to a shop deploying features several times daily mislead? What replaces one-off certification?

> [!answer]- Answer / self-check
> Classical growth models assume stable code and usage, representative tests and effective fixes. New features inject/change faults and traffic changes activation rates, so the fitted decay no longer describes one fixed fault population. Use **production SLIs, rolling-window SLOs, error-budget policies and continuous monitoring**, alongside per-release verification; these manage changing service behavior rather than certify a frozen version once.

### Q17 — Acceptance checks in recovery blocks

> [!question] Question
> Give an acceptance check for square root and sorting. Why is a complete sort check harder than merely checking order?

> [!answer]- Answer / self-check
> For nonnegative finite x and candidate y, require y≥0 and **abs(y²−x)≤ε×max(1,x)**, with tolerance chosen for the numeric range. For sorting require **nondecreasing output plus exactly the same multiset as the input** (not just length or sum). Checking order is linear, but exact permutation checking needs additional storage/counting or comparable processing, and must preserve duplicates. These are runtime acceptance checks for a recovery block, not user-acceptance testing.
