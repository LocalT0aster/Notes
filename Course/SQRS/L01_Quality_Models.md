# L01 — Quality Models Flashcards

**Source:** https://sqrbok.github.io/content/material/sqr/RQ-L1-QM.html

**Cards:** 18

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
> - **CMMI-audited team:** manufacturing-based, emphasizing process conformance. A start-up shipping to learn can emphasize **value-based** quality, accepting known defects when fixing them costs more than the learning gained.

### Q3 — McCall's factor–criteria–metric hierarchy

> [!question] Question
> Explain McCall's three levels and illustrate them with Maintainability.

> [!answer]- Answer / self-check
> - **Factor:** external quality goal visible to stakeholders, e.g. Maintainability.
> - **Criteria:** internal properties that influence factors, e.g. simplicity/modularity/conciseness.
> - **Metrics:** measurements of criteria, e.g. cyclomatic complexity, coupling, LOC.
> McCall's original criteria use yes/no checklists: 30 of 40 modules meeting a modularity check gives **0.75**; criterion scores contribute to factor scores. Modern quantitative proxies are not identical to those original checklist metrics.
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
> A concrete estimate: adding a 2 ms audit operation to an 8 ms request raises latency **25%**. Test instrumentation can likewise trade testability against efficiency. A **direct** pair is maintainability–testability: clearer, modular code often makes both change and isolated testing easier. Relationships depend on design and need not be symmetric.

### Q6 — ISO 25010: security, reliability, maintainability

> [!question] Question
> Define Security, Reliability, and Maintainability and give a testable requirement for each. List all nine ISO/IEC 25010:2023 characteristics and relate them to McCall and the 2011 edition.

> [!answer]- Answer / self-check
> - **Security:** protection against unauthorized access/manipulation. Example: 100% of privileged endpoints require authenticated RBAC.
> - **Reliability:** continued correct service under stated conditions. Example: monthly availability ≥99.9%.
> - **Maintainability:** ease/effectiveness of analysis, modification, and testing. Example: a supported change class can be implemented and regression-tested within an agreed threshold.
> Good requirements include condition, component, attribute, threshold, and measurement.
> **2023 characteristics:** functional suitability, performance efficiency, compatibility, interaction capability, reliability, security, maintainability, flexibility, safety.
> In the lecture's mapping, plain renamings are McCall's correctness → functional suitability, efficiency → performance efficiency, usability → interaction capability. Security collects integrity; compatibility collects interoperability. Safety has no McCall counterpart. Compared with 2011, **usability → interaction capability**, **portability → flexibility**, and **safety is added**; quality in use moves to ISO/IEC 25019. ISO flexibility is not McCall flexibility (which maps to modifiability under maintainability).

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
> Reliability example for login: (1) choose reliability/availability; (2) define production traffic and a calendar-month window; (3) set a goal of dependable login; (4) measure successful valid login requests / valid login requests; (5) require **≥99.9% per month**; (6) check instrumentation, exclusions, achievable baseline and completeness, including dependency failures. The threshold is illustrative and must be agreed.

### Q8 — Turn vague quality claims into testable requirements

> [!question] Question
> Why is “fast and reliable” poor, and how should it be rewritten?

> [!answer]- Answer / self-check
> It is ambiguous, combines two attributes, and has no operating condition, threshold, or measurement. Split it. Example:
> - Under normal load, Search API p95 latency shall be <200 ms.
> - During production operation, monthly availability shall be ≥99.9%.
> Template: **While [condition and measurement window], the [component] shall [measure] [threshold].** A percentile bounds a specified share of requests; an average can hide a severe slow tail. Choose p95 or p99 according to user risk and include enough observations.

### Q9 — Product Quality vs Quality in Use

> [!question] Question
> Distinguish ISO product quality from quality in use and give a high-product-quality / low-quality-in-use example.

> [!answer]- Answer / self-check
> - **Product quality:** properties of the software itself (e.g. reliability, maintainability, security).
> - **Quality in use:** whether specific users achieve goals effectively, efficiently, safely, and satisfactorily in context.
> - Example: a reliable, maintainable tax tool can still have confusing workflows that cause users to file incorrectly.
> Detect that gap with representative users doing real tasks in their context: measure task completion, errors, time and satisfaction, rather than relying only on code or availability metrics.

### Q10 — Kano: must-haves vs delighters

> [!question] Question
> Explain Kano must-have, one-dimensional and attractive attributes; give two streaming-app examples of each.

> [!answer]- Answer / self-check
> - **Must-haves:** expected basics; absence causes strong dissatisfaction, presence earns little extra praise. E.g. playback works; billing/account access is correct.
> - **Delighters:** unexpected benefits; absence is tolerated, presence raises satisfaction. E.g. excellent automatic highlights; unusually smart cross-device recommendations.
> - **One-dimensional:** more gives proportionally more satisfaction, e.g. higher video resolution and a larger useful catalogue (within the relevant range).
> As markets mature, delighters can become performance attributes and eventually must-haves.

### Q11 — Garvin's eight dimensions

> [!question] Question
> Name the eight dimensions. Why can Steinway and Yamaha compete on different ones? Give a software analogue.

> [!answer]- Answer / self-check
> **Performance, features, reliability, conformance, durability, serviceability, aesthetics, perceived quality.** The lecture contrasts Steinway's tone with Yamaha's reliability/conformance: excellence on every dimension is not necessary or economical. Likewise, a creative drawing app may differentiate by features/aesthetics while a payment SDK prioritizes reliability/conformance. State whose needs determine the choice.

### Q12 — From a quality model to a requirement

> [!question] Question
> Refine “the payment service must be reliable” through characteristic → subcharacteristic → measure, then add a threshold. What ambiguity does each step remove?

> [!answer]- Answer / self-check
> **Reliability → recoverability → mean time to restore service in minutes → ≤5 minutes per quarter in production.** The characteristic chooses the quality; the subcharacteristic selects recovery rather than another reliability aspect; the measure defines observable evidence; the requirement adds condition, window and acceptable threshold. The model identifies measures, but the project's requirements choose thresholds.

### Q13 — Internal versus external measures

> [!question] Question
> Give two internal and two external quality measures. Why connect them?

> [!answer]- Answer / self-check
> **Internal:** cyclomatic complexity and coupling measured on code without executing it. **External:** response time and failure rate measured on the running system. Internal measures are available cheaply and early; the model relates them to externally valuable outcomes. The relationship is a hypothesis to validate, not proof that a good code score guarantees good service.

### Q14 — Quality assurance versus quality control

> [!question] Question
> Define QA and QC. Classify one PR review, an audit of whether all PRs were reviewed, and a release regression run.

> [!answer]- Answer / self-check
> **QA** provides confidence that quality requirements will be fulfilled; **QC** checks and corrects work products. Checking one PR against a coding standard is QC; auditing review compliance across the quarter is QA; running the regression suite on release 4.2 is QC. Planning sets objectives/processes; improvement raises the ability to fulfil them.

### Q15 — McCall is not orthogonal

> [!question] Question
> Which criteria do maintainability and testability share? What follows for an investment in modularity?

> [!answer]- Answer / self-check
> Shared criteria are **simplicity, self-descriptiveness and modularity**. Clear modules can both simplify changes and enable isolated tests. The factors are not independent: improving one criterion can improve several factors, and blindly summing their scores can double-count benefits.

### Q16 — Use ISO/IEC 25010 as a checklist

> [!question] Question
> Choose three product characteristics for a food-delivery app, write testable requirements, and justify dropping one.

> [!answer]- Answer / self-check
> Illustrative requirements: **performance efficiency:** under 1,000 concurrent shoppers, catalogue p95 latency ≤200 ms; **reliability:** successful valid order submissions ≥99.9% each month; **security:** every order-read request must be authorized for that customer or an explicitly permitted staff role, verified with cross-account tests. One could drop **safety** only if the scoped system cannot cause harm; document that assumption and revisit it if allergy handling, medical deliveries or vehicle control enter scope. Do not drop a characteristic merely because it is hard to measure.

### Q17 — Process quality

> [!question] Question
> Name the four process-quality groups. Why does a good process not guarantee a good product?

> [!answer]- Answer / self-check
> **Suitability, usability, manageability, evolvability**, here describing the process rather than the product. A disciplined process can still implement mistaken requirements, use an unsuitable model or miss a risk. Process quality influences product quality, which influences quality in use; neither link is a guarantee.

### Q18 — Quality pioneers

> [!question] Question
> Match PDCA, the quality trilogy, conformance to requirements, fishbone diagrams and CMM to their pioneers and one software practice each.

> [!answer]- Answer / self-check
> - **Deming** popularized **PDCA**, building on Shewhart: iterative process-improvement experiments.
> - **Juran:** planning–control–improvement trilogy: quality objectives, release checks and retrospectives.
> - **Crosby:** conformance to requirements: explicit acceptance criteria and prevention.
> - **Ishikawa:** fishbone/cause-and-effect diagram: incident root-cause exploration.
> - **Humphrey:** software process maturity/CMM: assess and improve an organization's development process.
