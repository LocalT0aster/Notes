# L00 — Course Introduction & CI/CD Flashcards

**Source:** https://sqrbok.github.io/content/material/sqr/RQ_L00_Intro_CICD.html

**Study notes:** https://sqrbok.github.io/content/material/sqr/SN_L00_Intro_CICD.html

**Cards:** 15

> [!tip] Active recall
> Answer every part before revealing the answer. These synthesized self-checks follow SQRBOK's L00 revision questions; empirical figures below are those reported by the linked study notes, not independently re-estimated benchmarks.

### Q1 — Name the quality that failed

> [!question] Question
> Which quality characteristic failed in CrowdStrike Falcon (July 2024), Knight Capital (2012), and Log4j (December 2021)? Explain each mapping.

> [!answer]- Answer / self-check
> - **CrowdStrike → availability:** a faulty content update crashed Windows hosts and interrupted services.
> - **Knight Capital → maintainability:** obsolete code remained reachable during an inconsistent deployment, producing unintended trades. Deployment/configuration discipline also matters.
> - **Log4j → security:** attacker-controlled logging input could trigger remote code execution.
> These are the lecture's primary mappings, not claims that only one quality was affected.

### Q2 — From an incident to a requirement

> [!question] Question
> Why name the failed quality rather than say “buggy”? Turn one L00 incident into a checkable requirement.

> [!answer]- Answer / self-check
> A named characteristic identifies the outcome to protect, the measure and the verification method. For availability after an update: **While deploying a sensor-content update to a representative Windows staging fleet, all hosts shall remain bootable and the sensor shall pass its startup health check.** Test the update and recovery path before rollout; a canary gate can stop wider deployment on failures. This is an illustrative requirement, not a guarantee against every production failure.

### Q3 — Interpret the national poor-quality estimate

> [!question] Question
> Name three areas in the US$2.41T estimate for 2022. Why not add the areas? Compute the rise from US$2.08T in 2020 and compare it with 15% inflation.

> [!answer]- Answer / self-check
> Areas include **operational failures**, **legacy-system problems**, **unsuccessful projects**, and **finding/fixing defects**; technical debt was estimated separately. Categories overlap, so adding them double-counts costs. Rise = (2.41−2.08)/2.08 × 100 ≈ **15.87%**, close to 15% inflation. Inflation-adjusted increase ≈ 1.1587/1.15−1 = **0.75%**. Treat the extrapolated total as an order-of-magnitude estimate; this comparison alone does not establish a worsening real quality trend.

### Q4 — Measure the team's own quality cost

> [!question] Question
> A team of five logs 25 bugs in a month, taking an average of 4 person-hours per bug to find, fix and release. At 160 hours/person/month, what share of capacity is this, and why is it useful?

> [!answer]- Answer / self-check
> 25×4 = **100 person-hours**. Capacity = 5×160 = **800 person-hours**; share = 100/800 = **12.5%**. The team can track this local, operationally defined measure and evaluate prevention work. It excludes unlogged bugs and wider customer/business losses unless those are recorded separately.

### Q5 — Defect density and benchmark limits

> [!question] Question
> Define defect density. A library has 20 user-reported defects in its first year and 8,000 LOC. Compare its density with the 109-project median of 4.3 and mean of 7.47 defects/KLOC. Why can the comparison mislead?

> [!answer]- Answer / self-check
> Defect density = counted defects / code size. Here **20/8 = 2.5 post-release defects/KLOC**, below the sample median **4.3**. The median better represents a typical sampled project because extreme values pull up the mean **7.47**. Compare only with compatible definitions: physical/logical LOC, generated/test code, defect severity/duplicates, reporting window, usage and detection effort differ. A lower reported density does not itself prove better quality.

### Q6 — Define continuous integration

> [!question] Question
> Define CI and explain three practices and what happens when each is skipped.

> [!answer]- Answer / self-check
> **CI:** developers integrate into a shared main line at least daily, with each integration verified by an automated build and tests.
> - **Frequent small integrations:** skipping them lets incompatible changes accumulate.
> - **Automated reproducible build/tests on every change:** skipping them delays feedback and misses environment/integration failures.
> - **Fix a red build first:** skipping this leaves an untrusted baseline and masks new failures.

### Q7 — Delivery versus deployment

> [!question] Question
> Distinguish continuous delivery from continuous deployment. Why do both depend on CI?

> [!answer]- Answer / self-check
> **Continuous delivery** keeps passing changes ready for release, with a release decision still possible. **Continuous deployment** automatically releases passing changes to production. Both need a trustworthy, reproducible green CI pipeline to establish that a candidate is releasable; release automation alone is not CI.

### Q8 — Respond to a red build

> [!question] Question
> CI turns red just before your planned push. What comes first, why revert, and why avoid adding another change?

> [!answer]- Answer / self-check
> **Restore the green baseline first.** Notify/coordinate with the author and investigate; reverting the faulty commit is often faster than diagnosing and repairing it on the main line. Additional pushes make attribution harder and can hide new failures behind the existing one. Repair and verify the reverted change separately before reintegration.

### Q9 — Read a GitHub Actions workflow

> [!question] Question
> A push runs checkout, Python setup, dependency installation, `ruff check .`, then `pytest`. Which are quality gates? What if pytest fails? Name a possible later check.

> [!answer]- Answer / self-check
> Checkout, interpreter setup and dependency installation prepare the job. **Ruff** checks configured static/lint rules; **pytest** executes tests and checks their assertions. A failing test makes the job/build **red** under normal fail-on-error configuration; the author sees a failed commit/PR check and can inspect its log (notifications depend on settings). Later stages could add dependency/security scanning, integration tests or load tests. A required status check can block merge.

### Q10 — CI evidence versus causation

> [!question] Question
> A study reports 0.54 releases/month with CI, 0.24 without, and 0.34 before adoption in the eventual CI group. What follows and what does not?

> [!answer]- Answer / self-check
> CI projects released **2.25×** as often as non-CI projects; within the adopting group the rise was **0.54/0.34 ≈ 1.59×**. These are associations consistent with benefits, not proof that CI caused the difference. Adopters already released more frequently; team maturity, project activity and other simultaneous changes may confound the comparison.

### Q11 — Shape the test pyramid

> [!question] Question
> Label the pyramid. Why are 80/15/5 and 70/20/10 compatible advice, and why keep a wide base in CI?

> [!answer]- Answer / self-check
> Bottom to top: **many unit tests → fewer integration tests → few end-to-end tests**. The Google book's **80/15/5** and earlier blog's **70/20/10** describe approximate proportions **by test count**, not universal optima or runtime budgets. Fast, isolated tests give quick and localizable feedback; broad E2E tests add confidence in critical flows but are slower and more brittle.

### Q12 — CI at Google scale

> [!question] Question
> With about 150M test runs/day and a commit each second, why not test every commit independently? What can the system do instead?

> [!answer]- Answer / self-check
> Re-running every affected suite separately for every commit is too costly and slow. **Batch commits**, identify affected test targets, and prioritize/select tests likely to fail. A target is a test suite that may run repeatedly; daily runs are not distinct tests. Selection saves resources but must manage the risk of missed regressions and retain wider checks.

### Q13 — Interpret 37% statement coverage

> [!question] Question
> What does the other 63% mean? Give two reasons 100% statement coverage does not prove correctness.

> [!answer]- Answer / self-check
> **63% of instrumented statements did not execute in this test run/suite.** Investigate missing tests, unreachable/unused code and instrumentation scope. Even 100% can execute code without useful assertions, miss input/branch combinations, or miss requirements never implemented. Coverage measures execution, not correctness.

### Q14 — Flaky tests and trust

> [!question] Question
> Define flaky tests, give two causes, and explain why occasional false failures damage more than execution time.

> [!answer]- Answer / self-check
> A **flaky test** can pass or fail on unchanged code under ostensibly equivalent conditions. Causes include network/timing races and shared-state/test-order dependencies. The lecture's industrial example had flaky failures in about **1 suite run in 20**. Repeated false alarms teach people to ignore red builds, so real regressions can pass unnoticed. Diagnose and remove nondeterminism rather than routinely retrying until green.

### Q15 — Quality after deployment

> [!question] Question
> What is the error budget for a 99.9% SLO, and how does SRE extend CI beyond deployment?

> [!answer]- Answer / self-check
> Error budget = **1−0.999 = 0.1%** of the measured events/window: for 1M requests, **1,000 failed requests**. A time-based 30-day availability SLO allows **43.2 minutes**, but request and time budgets are interchangeable only under suitable traffic assumptions. SRE monitors production SLIs, automates response/recovery and uses budget consumption to balance release speed and reliability.
