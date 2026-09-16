# L03 — Verification Methods Flashcards

**Source:** https://sqrbok.github.io//content/material/sqr/RQ_L03_Verification.html

**Cards:** 11

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

### Q2 — Inspection formality spectrum

> [!question] Question
> Order four inspection/review techniques from formal to informal and state when each fits.

> [!answer]- Answer / self-check
> A defensible order: **Fagan inspection → formal technical/peer review → walkthrough → desk check/ad-hoc review**. Formal inspections fit high-risk or regulated artifacts; walkthroughs are useful for shared understanding; informal review is cheap for low-risk/local changes.

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

### Q7 — Mocks and test doubles

> [!question] Question
> What role do mocks play in unit testing?

> [!answer]- Answer / self-check
> Mocks replace collaborators so the unit is isolated and tests are deterministic/fast. They can supply controlled responses and verify interactions (calls, arguments, ordering). Over-mocking couples tests to implementation details, so mock boundaries rather than every internal object.

### Q8 — Black-box vs white-box testing

> [!question] Question
> Compare required knowledge, defect focus, and a technique for black-box and white-box testing.

> [!answer]- Answer / self-check
> - **Black-box:** uses specification/interface, not implementation; targets missing/incorrect behavior and input-domain faults; techniques include EP, BVA, decision tables.
> - **White-box:** uses code/control/data structure; targets unexecuted branches, path/condition/data-flow issues; techniques include statement/branch/MC/DC coverage.

### Q9 — Google-style test pyramid

> [!question] Question
> Explain the 70/20/10 pyramid and the ice-cream-cone anti-pattern.

> [!answer]- Answer / self-check
> Typical ratio: about **70% unit/small**, **20% integration/service**, **10% end-to-end/UI**. Lower-level tests are faster, more deterministic, and easier to diagnose; a small number of E2E tests protects critical flows. The **ice-cream cone** reverses this with many slow/brittle UI tests and too little fast unit coverage.

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
> No single technique covers all attributes.
