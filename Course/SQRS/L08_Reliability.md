# L08 — Software Reliability Flashcards

**Source:** https://sqrbok.github.io//content/material/sqr/RQ_L08_Reliability.html

**Cards:** 12

> [!tip] Active recall
> Answer every part before revealing the answer. For design/essay questions, the answer is a grading checklist: alternative designs can also be correct when justified.

### Q1 — Fault → error → failure in a real incident

> [!question] Question
> Trace one real incident through fault, error, and failure.

> [!answer]- Answer / self-check
> Use one case and keep levels distinct. Example CrowdStrike 2024: **fault** = invalid content/update accepted by validation/design; **error** = sensor/kernel code enters invalid memory/state while parsing it; **failure** = Windows hosts crash/boot-loop visibly. Fault is latent cause, error is incorrect internal state, failure is externally observed service deviation.

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
> A=99.9%, mean downtime per failure=2 min=0.033 h. Compute λ, MTTF, and failures/month (720 h) using the exact formula.

> [!answer]- Answer / self-check
> λ=(1−A)/(A×t_m)=0.001/(0.999×0.033) ≈ **0.0303 failures/h**. MTTF=1/λ ≈ **32.97 h**. Expected failures in 720 h ≈ **21.84**. High availability can coexist with frequent failures when recovery is very fast.

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

### Q9 — Why N-version independence fails

> [!question] Question
> Summarize Knight & Leveson and why it matters.

> [!answer]- Answer / self-check
> Setup: **27 independently developed versions**, same specification/language, tested on **1,000,000 random cases**. Coincident failures were far above the independence model (lecture shorthand ~**29×**). Causes included difficult/collinear inputs, numerical precision traps, and shared specification ambiguity. Therefore multiplying independent reliabilities can grossly overstate N-version safety.

### Q10 — Three-version majority voting

> [!question] Question
> Each version has Rc=0.95. Compute independent 2-of-3 reliability, then discuss 10% coincident failures.

> [!answer]- Answer / self-check
> Independent majority reliability = 3R²(1−R)+R³ = **0.99275**. A single version is **0.95**. If 10% of the 5% component failure probability is a common-mode event, there is already a **0.5% system-failure floor** before independent residual failures; a simple mixture gives effective reliability around **0.989** (exact value depends on the dependence model). Key lesson: correlation erodes the redundancy gain.

### Q11 — SLO error budget

> [!question] Question
> For 99.95% monthly availability and 50M requests, compute request/minute budgets and interpret 8 min outage + 5000 errors.

> [!answer]- Answer / self-check
> Allowed error fraction = 0.0005. Request budget = 50,000,000×0.0005 = **25,000 requests**. For a 30-day month: 43,200×0.0005 = **21.6 min** downtime budget. Eight outage minutes consume ~**37%** of the time budget; 5,000 failed requests consume **20%** of the request budget. Do not add minutes and requests directly—choose a consistent SLI/error-budget policy.

### Q12 — FIO vs SLO

> [!question] Question
> Explain how FIO and SLO express the same underlying idea in different eras/contexts.

> [!answer]- Answer / self-check
> Both set a **quantitative acceptable failure level** rather than demanding perfection. FIO is framed as allowable failure intensity during reliability engineering/testing; SLO sets a target for production service indicators. λ(t) corresponds to an error/failure-rate SLI, and “just-right reliability” corresponds to spending an **error budget** instead of overengineering beyond business need.
