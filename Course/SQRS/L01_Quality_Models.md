# L01 — Quality Models Flashcards

**Source:** https://sqrbok.github.io//content/material/sqr/RQ-L1-QM.html

**Cards:** 10

> [!tip] Active recall
> Answer every part before revealing the answer. For design/essay questions, the answer is a grading checklist: alternative designs can also be correct when justified.

### Q1 — Garvin: user vs manufacturing quality

> [!question] Question
> Contrast Garvin's user-based and manufacturing-based views. Give a software example where they judge the same product differently.

> [!answer]- Answer / self-check
> - **User-based:** quality = fitness for the user's purpose / satisfaction.
> - **Manufacturing-based:** quality = conformance to specification and process; defects are deviations.
> - Example: an app can conform perfectly to its specification yet frustrate users; manufacturing quality is high while user-based quality is low.

### Q2 — Garvin views in development methods

> [!question] Question
> Choose Scrum, XP, RUP, or FDA-style Waterfall and identify the Garvin view that tends to dominate. Justify it.

> [!answer]- Answer / self-check
> A defensible mapping is enough if justified. Typical examples:
> - **Scrum / XP:** user-based dominates because feedback and delivered value drive acceptance.
> - **FDA-validated Waterfall:** manufacturing-based dominates because documented conformance and traceability are central.
> - **RUP:** often blends product/manufacturing views through architecture, artifacts, and disciplined process.

### Q3 — McCall's factor–criteria–metric hierarchy

> [!question] Question
> Explain McCall's three levels and illustrate them with Maintainability.

> [!answer]- Answer / self-check
> - **Factor:** external quality goal visible to stakeholders, e.g. Maintainability.
> - **Criteria:** internal properties that influence factors, e.g. simplicity/modularity/conciseness.
> - **Metrics:** measurements of criteria, e.g. cyclomatic complexity, coupling, LOC.
> - The model links measurable internals → criteria → stakeholder-facing quality factors.

### Q4 — McCall's three categories

> [!question] Question
> Pick one McCall category, list its factors, and explain them for a mobile banking app.

> [!answer]- Answer / self-check
> Know the factor sets:
> - **Product Operation:** correctness, reliability, efficiency, integrity, usability.
> - **Product Revision:** maintainability, flexibility, testability.
> - **Product Transition:** portability, reusability, interoperability.
> Then translate each selected factor into a banking-app example.

### Q5 — Quality-attribute trade-offs

> [!question] Question
> Explain one Perry inverse relationship: Integrity–Efficiency, Usability–Efficiency, or Flexibility–Integrity.

> [!answer]- Answer / self-check
> Trade-offs mean improving one attribute can impose cost on another. Examples: encryption/access checks improve **integrity** but add CPU/latency; richer UI improves **usability** but consumes resources; highly configurable extension points improve **flexibility** but enlarge the attack surface. State the mechanism, not just the pair.

### Q6 — ISO 25010: security, reliability, maintainability

> [!question] Question
> Define Security, Reliability, and Maintainability and give one testable requirement for each.

> [!answer]- Answer / self-check
> - **Security:** protection against unauthorized access/manipulation. Example: 100% of privileged endpoints require authenticated RBAC.
> - **Reliability:** continued correct service under stated conditions. Example: monthly availability ≥99.9%.
> - **Maintainability:** ease/effectiveness of analysis, modification, and testing. Example: a supported change class can be implemented and regression-tested within an agreed threshold.
> Good requirements include condition, component, attribute, threshold, and measurement.

### Q7 — Firesmith's six-step quality-requirement process

> [!question] Question
> Apply the six-step process to a fast search API.

> [!answer]- Answer / self-check
> 1. Determine relevant quality characteristics.
> 2. Consider system/use context.
> 3. Define quality criteria.
> 4. Select measures.
> 5. Specify a threshold requirement.
> 6. Evaluate testability, feasibility, and completeness.
> Example result: under normal load (<1000 concurrent users), search p95 latency shall be <200 ms.

### Q8 — Turn vague quality claims into testable requirements

> [!question] Question
> Why is “fast and reliable” poor, and how should it be rewritten?

> [!answer]- Answer / self-check
> It is ambiguous, combines two attributes, and has no operating condition, threshold, or measurement. Split it. Example:
> - Under normal load, Search API p95 latency shall be <200 ms.
> - During production operation, monthly availability shall be ≥99.9%.

### Q9 — Product Quality vs Quality in Use

> [!question] Question
> Distinguish ISO product quality from quality in use and give a high-product-quality / low-quality-in-use example.

> [!answer]- Answer / self-check
> - **Product quality:** properties of the software itself (e.g. reliability, maintainability, security).
> - **Quality in use:** whether specific users achieve goals effectively, efficiently, safely, and satisfactorily in context.
> - Example: a reliable, maintainable tax tool can still have confusing workflows that cause users to file incorrectly.

### Q10 — Kano: must-haves vs delighters

> [!question] Question
> Explain Kano must-have attributes and delighters; give two streaming-app examples of each.

> [!answer]- Answer / self-check
> - **Must-haves:** expected basics; absence causes strong dissatisfaction, presence earns little extra praise. E.g. playback works; billing/account access is correct.
> - **Delighters:** unexpected benefits; absence is tolerated, presence raises satisfaction. E.g. excellent automatic highlights; unusually smart cross-device recommendations.
> As markets mature, delighters can become performance attributes and eventually must-haves.
