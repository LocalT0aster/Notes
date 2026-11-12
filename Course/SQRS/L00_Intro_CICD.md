# L00 — Course Introduction & CI/CD Flashcards

**Source:** https://sqrbok.github.io/content/material/sqr/RQ_L00_Intro_CICD.html

**Study notes:** https://sqrbok.github.io/content/material/sqr/SN_L00_Intro_CICD.html

**Cards:** 15

> [!tip] Active recall
> Questions are copied verbatim from the pinned SQRBOK source. Answers are locally synthesized self-checks, not official model answers.

### Q1 — Naming the Quality That Failed

**Card ID:** l00-intro-cicd-001

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L00_Intro_CICD.html#question-1-naming-the-quality-that-failed

> [!question] Question
> ## Question 1: Naming the Quality That Failed
>
> For each incident, name the quality characteristic that failed and say in one sentence why:
>
> - the CrowdStrike Falcon update of July 2024;
> - the Knight Capital deployment of 2012;
> - the Log4j vulnerability of December 2021.

> [!answer]- Answer / self-check
> - **CrowdStrike → availability:** a faulty content update crashed Windows hosts and interrupted services.
> - **Knight Capital → maintainability:** obsolete code remained reachable during an inconsistent deployment, producing unintended trades. Deployment/configuration discipline also matters.
> - **Log4j → security:** attacker-controlled logging input could trigger remote code execution.
> These are the lecture's primary mappings, not claims that only one quality was affected.

### Q2 — From Incident to Requirement

**Card ID:** l00-intro-cicd-002

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L00_Intro_CICD.html#question-2-from-incident-to-requirement

> [!question] Question
> ## Question 2: From Incident to Requirement
>
> Why is it useful to name the failed quality characteristic, rather than just saying "the software was buggy"? Use one of the incidents in Question 1 to show the step from incident to a checkable requirement.

> [!answer]- Answer / self-check
> A named characteristic identifies the outcome to protect, the measure and the verification method. For availability after an update: **While deploying a sensor-content update to a representative Windows staging fleet, all hosts shall remain bootable and the sensor shall pass its startup health check.** Test the update and recovery path before rollout; a canary gate can stop wider deployment on failures. This is an illustrative requirement, not a guarantee against every production failure.

### Q3 — The National Cost Estimate

**Card ID:** l00-intro-cicd-003

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L00_Intro_CICD.html#question-3-the-national-cost-estimate

> [!question] Question
> ## Question 3: The National Cost Estimate
>
> The cost of poor software quality in the US in 2022 was estimated at "at least US$2.41 trillion".
>
> 1. Name three of the areas that make up the estimate.
> 2. Why can the areas not simply be added to get the total?
> 3. The 2020 estimate was US$2.08 trillion. Compute the rise in percent and compare it with the 15% inflation over the same two years. What does the comparison suggest?

> [!answer]- Answer / self-check
> Areas include **operational failures**, **legacy-system problems**, **unsuccessful projects**, and **finding/fixing defects**; technical debt was estimated separately. Categories overlap, so adding them double-counts costs. Rise = (2.41−2.08)/2.08 × 100 ≈ **15.87%**, close to 15% inflation. Inflation-adjusted increase ≈ 1.1587/1.15−1 = **0.75%**. Treat the extrapolated total as an order-of-magnitude estimate; this comparison alone does not establish a worsening real quality trend.

### Q4 — Your Own Cost of Poor Quality

**Card ID:** l00-intro-cicd-004

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L00_Intro_CICD.html#question-4-your-own-cost-of-poor-quality

> [!question] Question
> ## Question 4: Your Own Cost of Poor Quality
>
> A team of five logs 25 bugs in a month, at an average of 4 hours each to find, fix and release. How many hours is that, and what share of the team's capacity, assuming 160 working hours per person per month? Why is this number more useful to the team than the national estimate?

> [!answer]- Answer / self-check
> 25×4 = **100 person-hours**. Capacity = 5×160 = **800 person-hours**; share = 100/800 = **12.5%**. The team can track this local, operationally defined measure and evaluate prevention work. It excludes unlogged bugs and wider customer/business losses unless those are recorded separately.

### Q5 — Defect Density

**Card ID:** l00-intro-cicd-005

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L00_Intro_CICD.html#question-5-defect-density

> [!question] Question
> ## Question 5: Defect Density
>
> 1. Define defect density.
> 2. A library of 8,000 lines of code had 20 defects reported by users in its first year. Compute its post-release defect density and compare it with the median of the 109-project benchmark.
> 3. Why is the benchmark median a better "typical value" than its mean of 7.47?
> 4. Give two reasons why comparing your project's figure with the benchmark can mislead.

> [!answer]- Answer / self-check
> Defect density = counted defects / code size. Here **20/8 = 2.5 post-release defects/KLOC**, below the sample median **4.3**. The median better represents a typical sampled project because extreme values pull up the mean **7.47**. Compare only with compatible definitions: physical/logical LOC, generated/test code, defect severity/duplicates, reporting window, usage and detection effort differ. A lower reported density does not itself prove better quality.

### Q6 — Continuous Integration

**Card ID:** l00-intro-cicd-006

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L00_Intro_CICD.html#question-6-continuous-integration

> [!question] Question
> ## Question 6: Continuous Integration
>
> Define continuous integration in one sentence. Then list three of its practices and explain what goes wrong if a team skips each one.

> [!answer]- Answer / self-check
> **CI:** developers integrate into a shared main line at least daily, with each integration verified by an automated build and tests.
> - **Frequent small integrations:** skipping them lets incompatible changes accumulate.
> - **Automated reproducible build/tests on every change:** skipping them delays feedback and misses environment/integration failures.
> - **Fix a red build first:** skipping this leaves an untrusted baseline and masks new failures.

### Q7 — Delivery or Deployment?

**Card ID:** l00-intro-cicd-007

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L00_Intro_CICD.html#question-7-delivery-or-deployment

> [!question] Question
> ## Question 7: Delivery or Deployment?
>
> What is the difference between continuous delivery and continuous deployment? Why do both depend on CI?

> [!answer]- Answer / self-check
> **Continuous delivery** keeps passing changes ready for release, with a release decision still possible. **Continuous deployment** automatically releases passing changes to production. Both need a trustworthy, reproducible green CI pipeline to establish that a candidate is releasable; release automation alone is not CI.

### Q8 — The Red Build

**Card ID:** l00-intro-cicd-008

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L00_Intro_CICD.html#question-8-the-red-build

> [!question] Question
> ## Question 8: The Red Build
>
> A teammate pushes a change and the CI build turns red ten minutes before you planned to push your own work.
>
> 1. What should happen first, according to CI practice?
> 2. Why is reverting the faulty commit often the quickest fix?
> 3. Why should you not push your change on top of the red build?

> [!answer]- Answer / self-check
> **Restore the green baseline first.** Notify/coordinate with the author and investigate; reverting the faulty commit is often faster than diagnosing and repairing it on the main line. Additional pushes make attribution harder and can hide new failures behind the existing one. Repair and verify the reverted change separately before reintegration.

### Q9 — Reading a Workflow

**Card ID:** l00-intro-cicd-009

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L00_Intro_CICD.html#question-9-reading-a-workflow

> [!question] Question
> ## Question 9: Reading a Workflow
>
> A GitHub Actions workflow runs these steps on every push: check out the code, set up Python 3.12, `pip install -r requirements.txt`, `ruff check .`, `pytest`.
>
> 1. Which steps are quality gates, and what does each one check?
> 2. The test step fails. Is the build green or red, and what does the author see?
> 3. Name one check the workflow does not perform that a later stage of a pipeline might add.

> [!answer]- Answer / self-check
> Checkout, interpreter setup and dependency installation prepare the job. **Ruff** checks configured static/lint rules; **pytest** executes tests and checks their assertions. A failing test makes the job/build **red** under normal fail-on-error configuration; the author sees a failed commit/PR check and can inspect its log (notifications depend on settings). Later stages could add dependency/security scanning, integration tests or load tests. A required status check can block merge.

### Q10 — Does CI Make Projects Better?

**Card ID:** l00-intro-cicd-010

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L00_Intro_CICD.html#question-10-does-ci-make-projects-better

> [!question] Question
> ## Question 10: Does CI Make Projects Better?
>
> In the GitHub study, projects using CI released 0.54 times a month, projects without CI 0.24 times, and the CI projects had released 0.34 times a month before they adopted CI. What can you conclude about the effect of CI, and what can you not conclude?

> [!answer]- Answer / self-check
> CI projects released **2.25×** as often as non-CI projects; within the adopting group the rise was **0.54/0.34 ≈ 1.59×**. These are associations consistent with benefits, not proof that CI caused the difference. Adopters already released more frequently; team maturity, project activity and other simultaneous changes may confound the comparison.

### Q11 — The Test Pyramid

**Card ID:** l00-intro-cicd-011

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L00_Intro_CICD.html#question-11-the-test-pyramid

> [!question] Question
> ## Question 11: The Test Pyramid
>
> 1. Sketch the test pyramid and label its three layers.
> 2. Google's book recommends 80/15/5; the lecture slide shows 70/20/10. Why do the two splits not contradict each other?
> 3. Why does a CI pipeline need the base of the pyramid to be wide?

> [!answer]- Answer / self-check
> Bottom to top: **many unit tests → fewer integration tests → few end-to-end tests**. The Google book's **80/15/5** and earlier blog's **70/20/10** describe approximate proportions **by test count**, not universal optima or runtime budgets. Fast, isolated tests give quick and localizable feedback; broad E2E tests add confidence in critical flows but are slower and more brittle.

### Q12 — Testing at Google Scale

**Card ID:** l00-intro-cicd-012

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L00_Intro_CICD.html#question-12-testing-at-google-scale

> [!question] Question
> ## Question 12: Testing at Google Scale
>
> Google's CI system runs about 150 million tests a day, and developers commit about once a second. Why can it not test each commit on its own, and what does it do instead?

> [!answer]- Answer / self-check
> Re-running every affected suite separately for every commit is too costly and slow. **Batch commits**, identify affected test targets, and prioritize/select tests likely to fail. A target is a test suite that may run repeatedly; daily runs are not distinct tests. Selection saves resources but must manage the risk of missed regressions and retain wider checks.

### Q13 — Coverage

**Card ID:** l00-intro-cicd-013

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L00_Intro_CICD.html#question-13-coverage

> [!question] Question
> ## Question 13: Coverage
>
> A coverage report shows 37% statement coverage.
>
> 1. What does the remaining 63% tell you about the code?
> 2. Give two reasons why 100% statement coverage still does not show the code is correct.

> [!answer]- Answer / self-check
> **63% of instrumented statements did not execute in this test run/suite.** Investigate missing tests, unreachable/unused code and instrumentation scope. Even 100% can execute code without useful assertions, miss input/branch combinations, or miss requirements never implemented. Coverage measures execution, not correctness.

### Q14 — Flaky Tests

**Card ID:** l00-intro-cicd-014

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L00_Intro_CICD.html#question-14-flaky-tests

> [!question] Question
> ## Question 14: Flaky Tests
>
> 1. Define a flaky test and give two possible causes.
> 2. In one industrial project, about 1 test-suite run in 20 had a flaky failure. Why is the loss of trust worse than the time lost?

> [!answer]- Answer / self-check
> A **flaky test** can pass or fail on unchanged code under ostensibly equivalent conditions. Causes include network/timing races and shared-state/test-order dependencies. The lecture's industrial example had flaky failures in about **1 suite run in 20**. Repeated false alarms teach people to ignore red builds, so real regressions can pass unnoticed. Diagnose and remove nondeterminism rather than routinely retrying until green.

### Q15 — After Deployment

**Card ID:** l00-intro-cicd-015

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L00_Intro_CICD.html#question-15-after-deployment

> [!question] Question
> ## Question 15: After Deployment
>
> What is an error budget for a service with a 99.9% SLO, and how does SRE extend the CI mindset beyond deployment?

> [!answer]- Answer / self-check
> Error budget = **1−0.999 = 0.1%** of the measured events/window: for 1M requests, **1,000 failed requests**. A time-based 30-day availability SLO allows **43.2 minutes**, but request and time budgets are interchangeable only under suitable traffic assumptions. SRE monitors production SLIs, automates response/recovery and uses budget consumption to balance release speed and reliability.
