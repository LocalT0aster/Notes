# L08 — Software Reliability Flashcards

**Source:** https://sqrbok.github.io/content/material/sqr/RQ_L08_Reliability.html

**Study notes:** https://sqrbok.github.io/content/material/sqr/SN_L08_Reliability.html

**Cards:** 15

> [!tip] Active recall
> Questions are copied verbatim from the pinned SQRBOK source. Answers are locally synthesized self-checks, not official model answers.

### Q1 — Fault, Error, Failure

**Card ID:** l08-reliability-001

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L08_Reliability.html#question-1-fault-error-failure

> [!question] Question
> ### Question 1: Fault, Error, Failure
>
> A web server crashes on requests larger than 8 KB because of a missing length check. It ran for months without trouble.
>
> 1. Name the fault, the activation, the error and the failure.
> 2. During the months without trouble, which of the three existed, and why did nobody notice?
> 3. Musa and Avizienis use the word "error" differently. State both meanings.

> [!answer]- Answer / self-check
> Use one case and keep levels distinct. Example CrowdStrike 2024: **fault** = invalid content/update accepted by validation/design; **error** = sensor/kernel code enters invalid memory/state while parsing it; **failure** = Windows hosts crash/boot-loop visibly. Fault is latent cause, error is incorrect internal state, failure is externally observed service deviation.
> For the source's server example: missing length check = **fault**; request >8 KB = **activation**; corrupt/invalid internal state = **error**; crash = **failure**. A dormant fault can exist during months with no triggering requests. Musa's “error” is a programmer's mistake; Avizienis's is a wrong system state; state which vocabulary you use.

### Q2 — Ariane 5

**Card ID:** l08-reliability-013

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L08_Reliability.html#question-2-ariane-5

> [!question] Question
> ### Question 2: Ariane 5
>
> Trace the Ariane 5 flight 501 loss through the fault–error–failure chain. Then explain why the backup inertial reference computer did not help, and what this says about duplicating software.

> [!answer]- Answer / self-check
> **Fault:** an unprotected 64-to-16-bit conversion in reused inertial-reference code. **Activation:** Ariane 5's flight values exceeded the Ariane 4 assumption. **Error:** overflow exception. **Component failure:** inertial computer shutdown; diagnostic data were then treated as flight data, leading to destructive commands and loss of the rocket. The backup ran the same faulty logic under the same conditions and failed too: identical redundancy does not remove common-mode design faults.

### Q3 — Hardware vs Software

**Card ID:** l08-reliability-002

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L08_Reliability.html#question-3-hardware-vs-software

> [!question] Question
> ### Question 3: Hardware vs Software
>
> Explain why the bathtub curve describes hardware but not software. When does a program's failure rate change?

> [!answer]- Answer / self-check
> Hardware has physical infant mortality and wear-out. Software does **not physically wear**: the same binary fails on triggering states/inputs. Its observed failure rate usually decreases as faults are removed, with spikes after changes that introduce new faults—often a downward/sawtooth pattern rather than a wear-out curve.

### Q4 — From Failure Data to Reliability

**Card ID:** l08-reliability-014

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L08_Reliability.html#question-4-from-failure-data-to-reliability

> [!question] Question
> ### Question 4: From Failure Data to Reliability
>
> A system logged 4 failures in 2,000 hours of stable operation.
>
> 1. Compute λ and the MTTF.
> 2. Compute the probability of no failure during a 24-hour run.
> 3. Its mean downtime per failure is 2 hours. Compute the availability.

> [!answer]- Answer / self-check
> **λ=4/2000=0.002/h; MTTF=1/λ=500 h**. Assuming stable use and a constant failure intensity with exponential time to failure, **R(24)=e^(−0.002×24)≈0.95313**. Steady-state availability **A=500/(500+2)≈0.996016=99.6016%**. A point estimate from four failures has substantial uncertainty; the exponential model is an assumption, not a consequence of the count.

### Q5 — Failure Intensity vs Failure Density

**Card ID:** l08-reliability-005

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L08_Reliability.html#question-5-failure-intensity-vs-failure-density

> [!question] Question
> ### Question 5: Failure Intensity vs Failure Density
>
> Describe a module that looks good by failure density but bad by failure intensity, and say which measure a user of the system would care about.

> [!answer]- Answer / self-check
> Low **failure density** can still be dangerous if one defect lies on a hot path used constantly → high failure intensity. Low average **failure intensity** can hide severe user unreliability if failures cluster by user/mode, are correlated, or have catastrophic severity. Always pair frequency with exposure, severity, and operational profile.

### Q6 — Severity Classes

**Card ID:** l08-reliability-003

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L08_Reliability.html#question-6-severity-classes

> [!question] Question
> ### Question 6: Severity Classes
>
> Define four failure severity classes for a hospital patient portal (test results, appointments, messages to doctors). State which criterion you chose (cost, system capability, human life or environment), why, and give one failure per class.

> [!answer]- Answer / self-check
> Use **human-life/capability impact** as the primary criterion. Example: C1 life-threatening wrong/hidden critical result; C2 severe clinical delay/data corruption; C3 non-critical feature outage with workaround; C4 cosmetic/minor inconvenience. Define objective boundaries and examples so stakeholders classify failures consistently.

### Q7 — FIO from Availability

**Card ID:** l08-reliability-004

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L08_Reliability.html#question-7-fio-from-availability

> [!question] Question
> ### Question 7: FIO from Availability
>
> A payment system must be available 99.9% of the time. Mean downtime per failure is 2 minutes.
>
> 1. Using the exact formula, compute the maximum failure intensity λ.
> 2. Compute the corresponding MTTF.
> 3. How many failures does this allow in 720 hours?
> 4. Compute λ with the approximation λ ≈ (1 − A)/t<sub>m</sub> and compare.

> [!answer]- Answer / self-check
> λ=(1−A)/(A×t_m)=0.001/(0.999/30) ≈ **0.030030 failures/operating-hour**. MTTF=1/λ = **33.3 h**. The lecture's λ×720 estimate is **21.62 failures**; accounting for uptime in 720 calendar hours gives λ×A×720 = **21.6**. Approximation λ≈(1−A)/t_m = **0.03/h**, 0.1% below exact. Keep 2/60 exact until the final rounding. High availability can coexist with frequent failures when recovery is fast.

### Q8 — FIO from Reliability

**Card ID:** l08-reliability-015

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L08_Reliability.html#question-8-fio-from-reliability

> [!question] Question
> ### Question 8: FIO from Reliability
>
> A requirement says the probability of no failure during a 4-hour operation must be at least 0.995. What FIO follows?

> [!answer]- Answer / self-check
> R(t)=e^(−λt), so **λ≤−ln(0.995)/4≈0.00125314/h** (about one failure per 798 operating hours). Use common time units and the intended operational profile; changing usage or nonconstant intensity invalidates a simple extrapolation.

### Q9 — When to Stop Testing

**Card ID:** l08-reliability-008

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L08_Reliability.html#question-9-when-to-stop-testing

> [!question] Question
> ### Question 9: When to Stop Testing
>
> A Goel–Okumoto model fitted to test data gives a = 80 faults and b = 0.03 per week. The FIO is 1.0 failure per week.
>
> 1. What is λ(0)?
> 2. What is λ(20)?
> 3. After how many weeks is the FIO reached?
> 4. How many faults have been found by then, and how many remain?

> [!answer]- Answer / self-check
> λ(t)=ab·e^(−bt), m(t)=a(1−e^(−bt)).
> - λ(0)=80×0.03 = **2.4/week**.
> - λ(20)=2.4e^-0.6 ≈ **1.317/week**.
> - Set 1=2.4e^-0.03t → t≈ **29.18 weeks**.
> - m(t)=80(1−1/2.4)≈ **46.7 faults** found.
> Remaining faults = a·e^(−bt)=FIO/b=**33.3** (expected counts need not be integers).

### Q10 — Limits of Growth Models

**Card ID:** l08-reliability-016

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L08_Reliability.html#question-10-limits-of-growth-models

> [!question] Question
> ### Question 10: Limits of Growth Models
>
> A web shop deploys new features several times a day. Explain why a growth model fitted to its failure data would mislead, and name the approach used instead.

> [!answer]- Answer / self-check
> Classical growth models assume stable code and usage, representative tests and effective fixes. New features inject/change faults and traffic changes activation rates, so the fitted decay no longer describes one fixed fault population. Use **production SLIs, rolling-window SLOs, error-budget policies and continuous monitoring**, alongside per-release verification; these manage changing service behavior rather than certify a frozen version once.

### Q11 — Recovery and the Domino Effect

**Card ID:** l08-reliability-007

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L08_Reliability.html#question-11-recovery-and-the-domino-effect

> [!question] Question
> ### Question 11: Recovery and the Domino Effect
>
> Service A processes an order, sends "ship item" to Service B, and then detects an error and rolls back to a checkpoint taken before the message.
>
> 1. What must Service B do, and why?
> 2. How can this cascade further? Name the effect.
> 3. How would forward recovery handle A's error instead?

> [!answer]- Answer / self-check
> If A rolls back after it already sent “ship” to B, A's restored state no longer matches B's committed action. To regain consistency B may also need rollback/compensation, possibly forcing further rollbacks—the **domino effect**. Forward recovery instead moves to a new consistent state, e.g. compensating transaction/cancel shipment, without rewinding all participants.

### Q12 — Acceptance Tests

**Card ID:** l08-reliability-017

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L08_Reliability.html#question-12-acceptance-tests

> [!question] Question
> ### Question 12: Acceptance Tests
>
> Write an acceptance test for a function that returns the square root of a number, and one for a function that sorts a list. Why is the second harder to make complete?

> [!answer]- Answer / self-check
> For nonnegative finite x and candidate y, require y≥0 and **abs(y²−x)≤ε×max(1,x)**, with tolerance chosen for the numeric range. For sorting require **nondecreasing output plus exactly the same multiset as the input** (not just length or sum). Checking order is linear, but exact permutation checking needs additional storage/counting or comparable processing, and must preserve duplicates. These are runtime acceptance checks for a recovery block, not user-acceptance testing.

### Q13 — Voting Reliability

**Card ID:** l08-reliability-009

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L08_Reliability.html#question-13-voting-reliability

> [!question] Question
> ### Question 13: Voting Reliability
>
> Three versions each have reliability R<sub>c</sub> = 0.95.
>
> 1. Compute the reliability of a 2-of-3 majority system, assuming independent failures and a perfect voter.
> 2. Now assume some failures are shared: an input makes all three versions fail together with probability 0.01, and on all other inputs each version fails on its own with probability 0.04. Compute the system reliability.
> 3. Which assumption did Knight and Leveson's experiment test, and what did it find (setup, the two key numbers, the conclusion)?

> [!answer]- Answer / self-check
> The current source reports **27 independently developed versions** of an anti-missile program, tested on **1,000,000 random cases**. Two or more versions failed together in **1,255 cases versus 127 predicted** under independence (about **9.9×**); independence was rejected at 99% confidence. Shared logical slips, finite-precision arithmetic and hard inputs caused correlated failures. Diversity can help, but multiplying independent reliabilities overstates its benefit when that assumption fails.
>
> Independent majority reliability = 3R²(1−R)+R³ = **0.99275**. Mixture failure probability = 0.01 + 0.99×(3×0.04²×0.96+0.04³) = **0.01462528**; reliability = **0.98537472**. The mixture's component reliability is 1−(0.01+0.99×0.04)=0.9504, approximately 0.95. A voter cannot mask an input that defeats all versions together.

### Q14 — Error Budget

**Card ID:** l08-reliability-011

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L08_Reliability.html#question-14-error-budget

> [!question] Question
> ### Question 14: Error Budget
>
> A streaming service has an SLO of 99.95% successful requests over a 30-day window and serves 50,000,000 requests in that window, spread evenly over time. This window it had three incidents:
>
> - incident A: a full outage of 6 minutes;
> - incident B: a full outage of 3 minutes;
> - incident C: a degraded period in which 4,000 requests failed.
>
> The team's policy, taken from the SRE Workbook's example: a postmortem is required for any single incident that uses *more than* 20% of the window's error budget; changes are frozen only when the budget is used up.
>
> 1. Compute the error budget in requests and in minutes of full outage.
> 2. Convert each outage to failed requests, and compute the share of the budget each incident used and the total.
> 3. Which incidents need a postmortem, and may the team keep shipping changes?

> [!answer]- Answer / self-check
> Budget = 50M×0.0005 = **25,000 failed requests**, equivalent to **21.6 minutes** of full outage under uniform traffic. Rate=50M/43,200≈1157.407 requests/min. **A:** ≈6944.44 failures, **27.78%** of budget; **B:** ≈3472.22, **13.89%**; **C:** 4000, **16%**. Total ≈14,416.67 failures, **57.67%** spent, **42.33%** left. Only A exceeds the strict >20% postmortem threshold; shipping may continue under the stated policy. Use a common request denominator; the time conversion depends on uniform traffic.

### Q15 — FIO and SLO

**Card ID:** l08-reliability-012

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L08_Reliability.html#question-15-fio-and-slo

> [!question] Question
> ### Question 15: FIO and SLO
>
> Explain why Musa's FIO and Google's SLO express the same idea, and what changed between them. Why is 100% the wrong target for both?

> [!answer]- Answer / self-check
> Both set a **quantitative acceptable failure level** rather than demanding perfection. FIO is framed as allowable failure intensity during reliability engineering/testing; SLO sets a target for production service indicators. λ(t) corresponds to an error/failure-rate SLI, and “just-right reliability” corresponds to spending an **error budget** instead of overengineering beyond business need.
> A 100% target leaves zero room for failures and change; its cost can exceed user benefit. Choose objectives by consequence, operating conditions and economic value rather than assuming perfect reliability is attainable.
