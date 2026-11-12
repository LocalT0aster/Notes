# L03 — Verification Methods Flashcards

**Source:** https://sqrbok.github.io/content/material/sqr/RQ_L03_Verification.html

**Study notes:** https://sqrbok.github.io/content/material/sqr/SN_L03_Verification.html

**Cards:** 16

> [!tip] Active recall
> Questions are copied verbatim from the pinned SQRBOK source. Answers are locally synthesized self-checks, not official model answers.

### Q1 — Four Verification Methods

**Card ID:** l03-verification-001

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L03_Verification.html#question-1-four-verification-methods

> [!question] Question
> ## Question 1: Four Verification Methods
>
> List the four verification methods (inspection, analysis, testing, demonstration) and give a one-sentence definition of each.
>
> Two questions separate them: is the product run, and does the evidence come from people's observation or from calculation and measured data? Place each method on these two questions, and give one software requirement for which each method is the most appropriate choice.

> [!answer]- Answer / self-check
> - **Inspection:** examine an artifact without executing it; e.g. requirements/design review.
> - **Analysis:** use models/calculations/static reasoning; e.g. timing or static-analysis proof.
> - **Demonstration:** operate the item and observe behavior, usually without precise instrumentation; e.g. show an installation/workflow.
> - **Test:** execute under controlled conditions and compare measured outputs to expected results.
> Matrix: product not run + human observation → inspection; not run + calculation/model evidence → analysis; run + human observation → demonstration; run + detailed measured data → testing. Choose the evidence a particular requirement needs.

### Q2 — Verification or Validation?

**Card ID:** l03-verification-012

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L03_Verification.html#question-2-verification-or-validation

> [!question] Question
> ## Question 2: Verification or Validation?
>
> A program does exactly what its specification says, and users still cannot do their job with it. Has it failed verification, validation, or both? Explain with the two questions "did we build the product right?" and "did we build the right product?".

> [!answer]- Answer / self-check
> **Verification:** did we build the product right, against its specification? It can pass here. **Validation:** did we build the right product for the intended use? It fails. The specification may be incomplete or wrong; conformance alone does not establish fitness for purpose.

### Q3 — The Review Spectrum

**Card ID:** l03-verification-002

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L03_Verification.html#question-3-the-review-spectrum

> [!question] Question
> ## Question 3: The Review Spectrum
>
> Name **four** review types from the most to the least formal. Explain how a walkthrough differs from an inspection: who leads it, and what the participants do before the meeting.

> [!answer]- Answer / self-check
> A defensible order: **Fagan inspection → formal technical/peer review → walkthrough → desk check/ad-hoc review**. Formal inspections fit high-risk or regulated artifacts; walkthroughs are useful for shared understanding; informal review is cheap for low-risk/local changes.
> A walkthrough is author-led explanation; an inspection is led by a trained non-author moderator and participants prepare individually before the meeting.

### Q4 — Inspection vs Testing

**Card ID:** l03-verification-003

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L03_Verification.html#question-4-inspection-vs-testing

> [!question] Question
> ## Question 4: Inspection vs Testing
>
> Compare inspection and testing across **three** dimensions: what they observe (fault or failure), when they can start, and which kinds of fault they find. Explain why using both is recommended.

> [!answer]- Answer / self-check
> Inspection is **static**, can start before executable code, and is strong for omissions, standards, maintainability, and design defects. Testing is **dynamic**, requires executable behavior, and exposes runtime failures, interactions, timing, and environment effects. They overlap but find different defect classes; defense in depth reduces blind spots.

### Q5 — Safety vs Liveness Properties

**Card ID:** l03-verification-004

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L03_Verification.html#question-5-safety-vs-liveness-properties

> [!question] Question
> ## Question 5: Safety vs Liveness Properties
>
> Define **safety** and **liveness** properties and give one software example of each.
>
> Why is a safety violation easier for a model checker to show than a liveness violation? Describe the shape of the counterexample in each case.

> [!answer]- Answer / self-check
> - **Safety:** “something bad never happens.” Example: a balance never becomes negative without an authorized overdraft.
> - **Liveness:** “something good eventually happens.” Example: every accepted job eventually completes or reaches a terminal failure state.
> Safety violations have finite bad prefixes; liveness concerns progress/eventuality.
> A model checker represents a liveness counterexample as an infinite non-progress run, usually a finite prefix followed by a repeating cycle.

### Q6 — Writing a Property in LTL

**Card ID:** l03-verification-013

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L03_Verification.html#question-6-writing-a-property-in-ltl

> [!question] Question
> ## Question 6: Writing a Property in LTL
>
> Using `[]` (always), `<>` (eventually) and `U` (until), write:
>
> (a) "the account balance is never negative";
> (b) "every placed order is eventually confirmed or rejected".
>
> Which of the two is a safety property? Give one correct behaviour of a real shop that would make (b) fail, and say what that shows about proved properties.

> [!answer]- Answer / self-check
> **`[](balance >= 0)`** is safety. For one identified order: **`[](placed -> <>(confirmed || rejected))`** is liveness; track the same order identity rather than letting another order's confirmation satisfy it. A legitimate permanently cancelled order violates the latter unless cancellation counts as rejection or another terminal outcome. A proof establishes the written property of its model, not the correctness of the chosen requirement. `p U q` additionally requires eventual q while p holds beforehand.

### Q7 — Rice's Theorem — Sound vs Complete

**Card ID:** l03-verification-005

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L03_Verification.html#question-7-rices-theorem--sound-vs-complete

> [!question] Question
> ## Question 7: Rice's Theorem — Sound vs Complete
>
> Explain the trade-off between **soundness** and **completeness** in static analysis, using the terms false positive and false negative.
>
> What does Rice's theorem tell us about the limits of static analysis? Why do practical bug finders accept both kinds of error instead of being sound?

> [!answer]- Answer / self-check
> - **Sound** (for a property): no real violations are missed, often at the cost of false positives.
> - **Complete/precise** in practice: avoids false alarms, but may miss real defects.
> Rice's theorem says non-trivial semantic program properties are undecidable in general, so practical tools approximate. Commercial tools choose a usable point on the false-positive/false-negative trade-off.

### Q8 — What a Clean Result Means

**Card ID:** l03-verification-014

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L03_Verification.html#question-8-what-a-clean-result-means

> [!question] Question
> ## Question 8: What a Clean Result Means
>
> pylint rates a function 10/10 and mypy reports no issues, yet the function divides by zero on an empty list. Explain why neither tool contradicts itself. What would a program verifier require before accepting the division?

> [!answer]- Answer / self-check
> The tools check configured lint/type properties, not every runtime behavior or the business contract. An empty list can be correctly typed. A verifier needs a proven nonzero divisor: for example a caller-established **nonempty-input precondition**, or code that handles/rejects the empty case with a suitable specification. Silence is meaningful only within a tool's stated guarantees and assumptions.

### Q9 — Fault, Error, Failure

**Card ID:** l03-verification-015

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L03_Verification.html#question-9-fault-error-failure

> [!question] Question
> ## Question 9: Fault, Error, Failure
>
> `num_zero` should count the zeros in a list, but its loop starts at index 1. For the inputs `[2, 7, 0]` and `[0, 7, 2]`, say whether each run reaches the fault, enters an error state, and fails. Use reachability, infection and propagation in your answer.

> [!answer]- Answer / self-check
> **Fault:** wrong initial index. Both runs **reach** it and start with an incorrect loop-index state (**infection**, under the lecture's state definition). `[2,7,0]` still counts one zero correctly, so no observable **propagation/failure**. `[0,7,2]` misses the first zero and returns 0 instead of 1: the wrong state propagates to an externally wrong result. Reaching faulty code alone is insufficient; the oracle must observe the consequence.

### Q10 — Test Levels

**Card ID:** l03-verification-006

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L03_Verification.html#question-10-test-levels

> [!question] Question
> ## Question 10: Test Levels
>
> Describe the testing levels unit, integration, system and acceptance. For each, identify: (a) what the test is checked against and (b) one example of a defect that would be found at that level and not at a lower one.

> [!answer]- Answer / self-check
> - **Unit:** single function/class/component; developers; local logic defect.
> - **Integration:** component interfaces; developers/testers; contract/protocol mismatch.
> - **System:** complete system in representative environment; test team; end-to-end behavior/configuration failure.
> - **Acceptance:** business/user needs; customer/product stakeholders; requirement/fitness-for-use gap.
> Check unit outputs against intended local behavior, integration against interface contracts, system against system requirements, acceptance against user/business goals. A cents/euros contract mismatch may escape isolated unit tests but fail integration.

### Q11 — Test Doubles

**Card ID:** l03-verification-007

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L03_Verification.html#question-11-test-doubles

> [!question] Question
> ## Question 11: Test Doubles
>
> Distinguish a stub, a fake and a mock. What can a mock detect that a stub cannot?
>
> Why does Google prefer real implementations, then fakes, and advise against overusing interaction testing?

> [!answer]- Answer / self-check
> Mocks replace collaborators so the unit is isolated and tests are deterministic/fast. They can supply controlled responses and verify interactions (calls, arguments, ordering). Over-mocking couples tests to implementation details, so mock boundaries rather than every internal object.
> A **stub** supplies canned responses; a **fake** is a lightweight working implementation; a **mock** verifies expected interactions, so it can detect an omitted required call that a response-only stub would not. Prefer real collaborators when practical, then faithful fakes; avoid making irrelevant implementation call sequences part of the contract.

### Q12 — Black Box vs White Box

**Card ID:** l03-verification-008

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L03_Verification.html#question-12-black-box-vs-white-box

> [!question] Question
> ## Question 12: Black Box vs White Box
>
> Compare black-box and white-box testing. For each, describe: (a) where the tests come from, (b) what kind of gap it cannot see, and (c) one technique associated with it.
>
> A white-box test asserts that a 1,200 € order pays 20 € shipping, a value taken from the code because the specification is silent. What is wrong with this test's oracle?

> [!answer]- Answer / self-check
> - **Black-box:** uses specification/interface, not implementation; targets missing/incorrect behavior and input-domain faults; techniques include EP, BVA, decision tables.
> - **White-box:** uses code/control/data structure; targets unexecuted branches, path/condition/data-flow issues; techniques include statement/branch/MC/DC coverage.
> Black-box tests can miss unmentioned implementation behavior; white-box tests cannot reveal a requirement never implemented. Copying a €20 shipping expectation from the code when the specification is silent is a circular oracle: clarify intended behavior independently before asserting it.

### Q13 — Google's Test Pyramid

**Card ID:** l03-verification-009

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L03_Verification.html#question-13-googles-test-pyramid

> [!question] Question
> ## Question 13: Google's Test Pyramid
>
> *Software Engineering at Google* recommends a mix of about 80% unit, 15% integration and 5% end-to-end tests.
>
> What do these percentages count? Explain **why** this shape is recommended. What is the "ice cream cone" anti-pattern and why is it a problem? Is the ratio a measured optimum?

> [!answer]- Answer / self-check
> Google's book suggests **80% unit, 15% integration, 5% E2E by test count**; the earlier blog used **70/20/10**. Both are rules of thumb, not measured universal optima. Lower-level tests are faster, more deterministic, and easier to diagnose; a few E2E tests protect critical flows. The **ice-cream cone** reverses this with many slow/brittle UI tests and too little fast unit coverage.

### Q14 — Test-Driven Development

**Card ID:** l03-verification-016

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L03_Verification.html#question-14-test-driven-development

> [!question] Question
> ## Question 14: Test-Driven Development
>
> Describe the red–green–refactor cycle. The industrial case studies at Microsoft and IBM reported 40–90% lower defect density, while controlled experiments with TDD newcomers found no quality gain. Give two reasons the results may differ.

> [!answer]- Answer / self-check
> **Red:** write a test that fails for the intended missing behavior. **Green:** implement enough to pass. **Refactor:** improve structure while retaining behavior and green tests. Experience affects test design and fluency; task type matters (new simple code versus complex legacy changes). Industrial case studies also differ from controlled experiments in selection, baselines and confounders. The studies do not establish a uniform causal gain for every team.

### Q15 — Demonstration

**Card ID:** l03-verification-010

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L03_Verification.html#question-15-demonstration

> [!question] Question
> ## Question 15: Demonstration
>
> Define demonstration and explain how it differs from testing. Give **two** examples of demonstration activities in software development, and one property that can only be verified this way.

> [!answer]- Answer / self-check
> Demonstration verifies a requirement by **operating the system and observing that a capability is present**, when pass/fail can be established by observation rather than precise measurement. Examples: demonstrate successful installation/uninstallation; demonstrate a user workflow or failover procedure. If numerical limits must be measured, that is a test/analysis rather than mere demonstration.

### Q16 — Defense in Depth

**Card ID:** l03-verification-011

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L03_Verification.html#question-16-defense-in-depth

> [!question] Question
> ## Question 16: Defense in Depth
>
> Different verification methods suit different quality characteristics. For **maintainability**, **usability** and **reliability**, say which method or methods you would rely on most and why. Then explain why a team should not rely on one method alone, using a finding about the fault types different methods detect.

> [!answer]- Answer / self-check
> - **Maintainability:** inspection/design review + static analysis/code metrics; targeted tests for changeability.
> - **Usability:** demonstration/validation with representative users and task-based testing.
> - **Security:** combine threat/design inspection, SAST/static analysis, dynamic/penetration/fuzz testing, and dependency analysis.
> - **Reliability:** analysis of failure data/models plus execution under representative workloads and fault-injection tests.
> No single technique covers all attributes.
