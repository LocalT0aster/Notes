# L03 — Verification Methods Flashcards

**Source:** https://sqrbok.github.io/content/material/sqr/RQ_L03_Verification.html

**Cards:** 16

> [!tip] Active recall
> Answer every part before revealing the answer. For design/essay questions, the answer is a grading checklist: alternative designs can also be correct when justified.

### Q1 — Four verification techniques

> [!question] Question
> List the four INCOSE-style verification techniques, define each, and give a suitable use.

> [!answer]- Answer / self-check
> - **Inspection:** examine an artifact without executing it; e.g. requirements/design review.
> - **Analysis:** use models/calculations/static reasoning; e.g. timing or static-analysis proof.
> - **Demonstration:** operate the item and observe behavior, usually without precise instrumentation; e.g. show an installation/workflow.
> - **Test:** execute under controlled conditions and compare measured outputs to expected results.
> Matrix: product not run + human observation → inspection; not run + calculation/model evidence → analysis; run + human observation → demonstration; run + detailed measured data → testing. Choose the evidence a particular requirement needs.

### Q2 — Inspection formality spectrum

> [!question] Question
> Order four inspection/review techniques from formal to informal and state when each fits.

> [!answer]- Answer / self-check
> A defensible order: **Fagan inspection → formal technical/peer review → walkthrough → desk check/ad-hoc review**. Formal inspections fit high-risk or regulated artifacts; walkthroughs are useful for shared understanding; informal review is cheap for low-risk/local changes.
> A walkthrough is author-led explanation; an inspection is led by a trained non-author moderator and participants prepare individually before the meeting.

### Q3 — Inspection vs testing

> [!question] Question
> Compare inspection and testing across at least three dimensions and explain why they complement each other.

> [!answer]- Answer / self-check
> Inspection is **static**, can start before executable code, and is strong for omissions, standards, maintainability, and design defects. Testing is **dynamic**, requires executable behavior, and exposes runtime failures, interactions, timing, and environment effects. They overlap but find different defect classes; defense in depth reduces blind spots.

### Q4 — Safety vs liveness properties

> [!question] Question
> Define safety and liveness properties with examples.

> [!answer]- Answer / self-check
> - **Safety:** “something bad never happens.” Example: a balance never becomes negative without an authorized overdraft.
> - **Liveness:** “something good eventually happens.” Example: every accepted job eventually completes or reaches a terminal failure state.
> Safety violations have finite bad prefixes; liveness concerns progress/eventuality.
> A model checker represents a liveness counterexample as an infinite non-progress run, usually a finite prefix followed by a repeating cycle.

### Q5 — Soundness, completeness, Rice's theorem

> [!question] Question
> Explain the soundness/completeness trade-off in static analysis and the implication of Rice's theorem.

> [!answer]- Answer / self-check
> - **Sound** (for a property): no real violations are missed, often at the cost of false positives.
> - **Complete/precise** in practice: avoids false alarms, but may miss real defects.
> Rice's theorem says non-trivial semantic program properties are undecidable in general, so practical tools approximate. Commercial tools choose a usable point on the false-positive/false-negative trade-off.

### Q6 — Four test levels

> [!question] Question
> Describe unit, integration, system, and acceptance testing: object, typical performer, and example defect.

> [!answer]- Answer / self-check
> - **Unit:** single function/class/component; developers; local logic defect.
> - **Integration:** component interfaces; developers/testers; contract/protocol mismatch.
> - **System:** complete system in representative environment; test team; end-to-end behavior/configuration failure.
> - **Acceptance:** business/user needs; customer/product stakeholders; requirement/fitness-for-use gap.
> Check unit outputs against intended local behavior, integration against interface contracts, system against system requirements, acceptance against user/business goals. A cents/euros contract mismatch may escape isolated unit tests but fail integration.

### Q7 — Mocks and test doubles

> [!question] Question
> What role do mocks play in unit testing?

> [!answer]- Answer / self-check
> Mocks replace collaborators so the unit is isolated and tests are deterministic/fast. They can supply controlled responses and verify interactions (calls, arguments, ordering). Over-mocking couples tests to implementation details, so mock boundaries rather than every internal object.
> A **stub** supplies canned responses; a **fake** is a lightweight working implementation; a **mock** verifies expected interactions, so it can detect an omitted required call that a response-only stub would not. Prefer real collaborators when practical, then faithful fakes; avoid making irrelevant implementation call sequences part of the contract.

### Q8 — Black-box vs white-box testing

> [!question] Question
> Compare required knowledge, defect focus, and a technique for black-box and white-box testing.

> [!answer]- Answer / self-check
> - **Black-box:** uses specification/interface, not implementation; targets missing/incorrect behavior and input-domain faults; techniques include EP, BVA, decision tables.
> - **White-box:** uses code/control/data structure; targets unexecuted branches, path/condition/data-flow issues; techniques include statement/branch/MC/DC coverage.
> Black-box tests can miss unmentioned implementation behavior; white-box tests cannot reveal a requirement never implemented. Copying a €20 shipping expectation from the code when the specification is silent is a circular oracle: clarify intended behavior independently before asserting it.

### Q9 — Google-style test pyramid

> [!question] Question
> Explain the 80/15/5 pyramid, the earlier 70/20/10 split and the ice-cream-cone anti-pattern. What do the percentages count?

> [!answer]- Answer / self-check
> Google's book suggests **80% unit, 15% integration, 5% E2E by test count**; the earlier blog used **70/20/10**. Both are rules of thumb, not measured universal optima. Lower-level tests are faster, more deterministic, and easier to diagnose; a few E2E tests protect critical flows. The **ice-cream cone** reverses this with many slow/brittle UI tests and too little fast unit coverage.

### Q10 — Demonstration as verification

> [!question] Question
> Define demonstration and when it is the appropriate verification method; give two examples.

> [!answer]- Answer / self-check
> Demonstration verifies a requirement by **operating the system and observing that a capability is present**, when pass/fail can be established by observation rather than precise measurement. Examples: demonstrate successful installation/uninstallation; demonstrate a user workflow or failover procedure. If numerical limits must be measured, that is a test/analysis rather than mere demonstration.

### Q11 — Verification defense in depth

> [!question] Question
> Select effective verification techniques for maintainability, usability, and security.

> [!answer]- Answer / self-check
> - **Maintainability:** inspection/design review + static analysis/code metrics; targeted tests for changeability.
> - **Usability:** demonstration/validation with representative users and task-based testing.
> - **Security:** combine threat/design inspection, SAST/static analysis, dynamic/penetration/fuzz testing, and dependency analysis.
> - **Reliability:** analysis of failure data/models plus execution under representative workloads and fault-injection tests.
> No single technique covers all attributes.

### Q12 — Verification versus validation

> [!question] Question
> The program meets its specification but users cannot accomplish their work. Did verification or validation fail?

> [!answer]- Answer / self-check
> **Verification:** did we build the product right, against its specification? It can pass here. **Validation:** did we build the right product for the intended use? It fails. The specification may be incomplete or wrong; conformance alone does not establish fitness for purpose.

### Q13 — Write temporal properties

> [!question] Question
> With `[]` (always), `<>` (eventually), `U` (until), express a nonnegative balance and eventual confirmation/rejection of every placed order. Which is safety, and how could the second reject a legitimate shop behavior?

> [!answer]- Answer / self-check
> **`[](balance >= 0)`** is safety. For one identified order: **`[](placed -> <>(confirmed || rejected))`** is liveness; track the same order identity rather than letting another order's confirmation satisfy it. A legitimate permanently cancelled order violates the latter unless cancellation counts as rejection or another terminal outcome. A proof establishes the written property of its model, not the correctness of the chosen requirement. `p U q` additionally requires eventual q while p holds beforehand.

### Q14 — A clean tool report is not a proof

> [!question] Question
> Pylint gives 10/10 and mypy no issues, yet a function divides by zero on an empty list. Why no contradiction? What would a verifier need?

> [!answer]- Answer / self-check
> The tools check configured lint/type properties, not every runtime behavior or the business contract. An empty list can be correctly typed. A verifier needs a proven nonzero divisor: for example a caller-established **nonempty-input precondition**, or code that handles/rejects the empty case with a suitable specification. Silence is meaningful only within a tool's stated guarantees and assumptions.

### Q15 — Reachability, infection and propagation

> [!question] Question
> `num_zero` starts its loop at index 1 instead of 0. Trace `[2,7,0]` and `[0,7,2]` through fault, error and failure.

> [!answer]- Answer / self-check
> **Fault:** wrong initial index. Both runs **reach** it and start with an incorrect loop-index state (**infection**, under the lecture's state definition). `[2,7,0]` still counts one zero correctly, so no observable **propagation/failure**. `[0,7,2]` misses the first zero and returns 0 instead of 1: the wrong state propagates to an externally wrong result. Reaching faulty code alone is insufficient; the oracle must observe the consequence.

### Q16 — TDD and its evidence

> [!question] Question
> Describe red–green–refactor. Why could industrial reports of 40–90% lower defect density coexist with newcomer experiments showing no gain?

> [!answer]- Answer / self-check
> **Red:** write a test that fails for the intended missing behavior. **Green:** implement enough to pass. **Refactor:** improve structure while retaining behavior and green tests. Experience affects test design and fluency; task type matters (new simple code versus complex legacy changes). Industrial case studies also differ from controlled experiments in selection, baselines and confounders. The studies do not establish a uniform causal gain for every team.
