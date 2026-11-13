# L01 — Quality Models Flashcards

**Source:** https://sqrbok.github.io/content/material/sqr/RQ-L1-QM.html

**Study notes:** https://sqrbok.github.io/content/material/sqr/SN-L1-QM.html

**Cards:** 18

> [!tip] Active recall
> Questions are copied verbatim from the pinned SQRBOK source. Answers are locally synthesized self-checks, not official model answers.

### Q1 — Garvin's Views — Definitions

**Card ID:** l01-quality-models-001

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ-L1-QM.html#question-1-garvins-views--definitions

> [!question] Question
> ## Question 1: Garvin's Views — Definitions
>
> Explain the difference between the **user-based** and **manufacturing-based** views of quality.
>
> Give one software example in which the same product is judged high quality in one view and low quality in the other.

> [!answer]- Answer / self-check
> - **User-based:** quality = fitness for the user's purpose / satisfaction.
> - **Manufacturing-based:** quality = conformance to specification and process; defects are deviations.
> - Example: an app can conform perfectly to its specification yet frustrate users; manufacturing quality is high while user-based quality is low.

### Q2 — Garvin's Views — Which View Dominates?

**Card ID:** l01-quality-models-002

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ-L1-QM.html#question-2-garvins-views--which-view-dominates

> [!question] Question
> ## Question 2: Garvin's Views — Which View Dominates?
>
> For ONE of the following ways of working, say which Garvin view dominates and justify your answer:
>
> - Scrum or XP, where work is accepted by customer demo
> - a team audited against a process standard such as CMMI
> - a medical-device project that must pass FDA validation
> - a start-up shipping weekly to learn what customers want

> [!answer]- Answer / self-check
> Choose any one example and justify the dominant view:
> - **Scrum or XP, accepted by customer demo → user-based:** the customer judges whether the increment meets their needs.
> - **Team audited against CMMI → manufacturing-based:** the audit emphasizes conformance to defined processes.
> - **Medical-device project passing FDA validation → manufacturing-based:** documented evidence of meeting safety and performance requirements drives acceptance; validation also checks fitness for intended use.
> - **Start-up shipping weekly to learn what customers want → user-based:** frequent releases reveal whether the product meets actual customer needs.

### Q3 — Garvin's Eight Dimensions

**Card ID:** l01-quality-models-011

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ-L1-QM.html#question-3-garvins-eight-dimensions

> [!question] Question
> ## Question 3: Garvin's Eight Dimensions
>
> Name Garvin's eight dimensions of product quality. Using the piano example (Steinway and Yamaha), explain why a firm need not compete on all eight, and give a software analogue.

> [!answer]- Answer / self-check
> **Performance, features, reliability, conformance, durability, serviceability, aesthetics, perceived quality.** The lecture contrasts Steinway's tone with Yamaha's reliability/conformance: excellence on every dimension is not necessary or economical. Likewise, a creative drawing app may differentiate by features/aesthetics while a payment SDK prioritizes reliability/conformance. State whose needs determine the choice.

### Q4 — The Quality Model Hierarchy

**Card ID:** l01-quality-models-012

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ-L1-QM.html#question-4-the-quality-model-hierarchy

> [!question] Question
> ## Question 4: The Quality Model Hierarchy
>
> Take the requirement "the payment service must be reliable". Walk it down the quality model hierarchy (characteristic → subcharacteristic → measure), then add a threshold to turn it into a requirement. Explain what each step removes from the original sentence.

> [!answer]- Answer / self-check
> **Reliability → recoverability → mean time to restore service in minutes → ≤5 minutes per quarter in production.** The characteristic chooses the quality; the subcharacteristic selects recovery rather than another reliability aspect; the measure defines observable evidence; the requirement adds condition, window and acceptable threshold. The model identifies measures, but the project's requirements choose thresholds.

### Q5 — Internal and External Quality

**Card ID:** l01-quality-models-013

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ-L1-QM.html#question-5-internal-and-external-quality

> [!question] Question
> ## Question 5: Internal and External Quality
>
> What is the difference between internal and external quality measures? Give two examples of each, and explain why a quality model has to connect them.

> [!answer]- Answer / self-check
> **Internal:** cyclomatic complexity and coupling measured on code without executing it. **External:** response time and failure rate measured on the running system. Internal measures are available cheaply and early; the model relates them to externally valuable outcomes. The relationship is a hypothesis to validate, not proof that a good code score guarantees good service.

### Q6 — QA versus QC

**Card ID:** l01-quality-models-014

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ-L1-QM.html#question-6-qa-versus-qc

> [!question] Question
> ## Question 6: QA versus QC
>
> Define quality assurance and quality control. For each of the following, say which it is and why:
>
> - a) a reviewer checks one pull request against the coding standard
> - b) an auditor confirms that every pull request in the last quarter was reviewed before merge
> - c) a tester runs the regression suite on release 4.2

> [!answer]- Answer / self-check
> **QA** provides confidence that quality requirements will be fulfilled; **QC** checks and corrects work products. Checking one PR against a coding standard is QC; auditing review compliance across the quarter is QA; running the regression suite on release 4.2 is QC. Planning sets objectives/processes; improvement raises the ability to fulfil them.

### Q7 — McCall's Model Structure

**Card ID:** l01-quality-models-003

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ-L1-QM.html#question-7-mccalls-model-structure

> [!question] Question
> ## Question 7: McCall's Model Structure
>
> McCall's model has three levels: **factors**, **criteria** and **metrics**.
>
> Explain the purpose of each level. Use **maintainability** to illustrate all three, and explain how a criterion is scored.

> [!answer]- Answer / self-check
> - **Factor:** external quality goal visible to stakeholders, e.g. Maintainability.
> - **Criteria:** internal properties that influence factors, e.g. simplicity/modularity/conciseness.
> - **Metrics:** measurements of criteria, e.g. cyclomatic complexity, coupling, LOC.
> McCall's original criteria use yes/no checklists: 30 of 40 modules meeting a modularity check gives **0.75**; criterion scores contribute to factor scores. Modern quantitative proxies are not identical to those original checklist metrics.
> - The model links measurable internals → criteria → stakeholder-facing quality factors.

### Q8 — McCall's Categories

**Card ID:** l01-quality-models-004

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ-L1-QM.html#question-8-mccalls-categories

> [!question] Question
> ## Question 8: McCall's Categories
>
> Pick **one** of McCall's three categories and list its factors. For each factor, write one sentence on what it means for a mobile banking app.

> [!answer]- Answer / self-check
> Know the factor sets:
> - **Product Operation:** correctness, reliability, efficiency, integrity, usability.
> - **Product Revision:** maintainability, flexibility, testability.
> - **Product Transition:** portability, reusability, interoperability.
> Then translate each selected factor into a banking-app example.

### Q9 — McCall Is Not Orthogonal

**Card ID:** l01-quality-models-015

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ-L1-QM.html#question-9-mccall-is-not-orthogonal

> [!question] Question
> ## Question 9: McCall Is Not Orthogonal
>
> McCall's criteria for maintainability and for testability overlap. Name the shared criteria and explain one consequence, good or bad, for a team that invests in modularity.

> [!answer]- Answer / self-check
> Shared criteria are **simplicity, self-descriptiveness and modularity**. Clear modules can both simplify changes and enable isolated tests. The factors are not independent: improving one criterion can improve several factors, and blindly summing their scores can double-count benefits.

### Q10 — Quality Attribute Trade-offs

**Card ID:** l01-quality-models-005

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ-L1-QM.html#question-10-quality-attribute-trade-offs

> [!question] Question
> ## Question 10: Quality Attribute Trade-offs
>
> Pick one pair and explain the trade-off with a concrete software example, including a rough number:
>
> - integrity and efficiency
> - usability and efficiency
> - testability and efficiency
>
> Then give one pair whose relationship is **direct** and explain why.

> [!answer]- Answer / self-check
> Trade-offs mean improving one attribute can impose cost on another. Examples: encryption/access checks improve **integrity** but add CPU/latency; richer UI improves **usability** but consumes resources; highly configurable extension points improve **flexibility** but enlarge the attack surface. State the mechanism, not just the pair.
> A concrete estimate: adding a 2 ms audit operation to an 8 ms request raises latency **25%**. Test instrumentation can likewise trade testability against efficiency. A **direct** pair is maintainability–testability: clearer, modular code often makes both change and isolated testing easier. Relationships depend on design and need not be symmetric.

### Q11 — From McCall to ISO/IEC 25010

**Card ID:** l01-quality-models-006

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ-L1-QM.html#question-11-from-mccall-to-isoiec-25010

> [!question] Question
> ## Question 11: From McCall to ISO/IEC 25010
>
> List the nine characteristics of ISO/IEC 25010:2023. Which three are plain renamings of McCall factors? Which two collect content that McCall kept inside differently named factors, and which factors were they? Which characteristic has no McCall counterpart at all? Name two characteristics that the 2023 edition renamed or added compared with 2011.

> [!answer]- Answer / self-check
> - **Security:** protection against unauthorized access/manipulation. Example: 100% of privileged endpoints require authenticated RBAC.
> - **Reliability:** continued correct service under stated conditions. Example: monthly availability ≥99.9%.
> - **Maintainability:** ease/effectiveness of analysis, modification, and testing. Example: a supported change class can be implemented and regression-tested within an agreed threshold.
> Good requirements include condition, component, attribute, threshold, and measurement.
> **2023 characteristics:** functional suitability, performance efficiency, compatibility, interaction capability, reliability, security, maintainability, flexibility, safety.
> In the lecture's mapping, plain renamings are McCall's correctness → functional suitability, efficiency → performance efficiency, usability → interaction capability. Security collects integrity; compatibility collects interoperability. Safety has no McCall counterpart. Compared with 2011, **usability → interaction capability**, **portability → flexibility**, and **safety is added**; quality in use moves to ISO/IEC 25019. ISO flexibility is not McCall flexibility (which maps to modifiability under maintainability).

### Q12 — ISO/IEC 25010 as a Checklist

**Card ID:** l01-quality-models-016

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ-L1-QM.html#question-12-isoiec-25010-as-a-checklist

> [!question] Question
> ## Question 12: ISO/IEC 25010 as a Checklist
>
> For a food-delivery app, choose three ISO/IEC 25010 characteristics that matter and one that you would drop. For each kept characteristic write one testable requirement; for the dropped one, write the reason.

> [!answer]- Answer / self-check
> Illustrative requirements: **performance efficiency:** under 1,000 concurrent shoppers, catalogue p95 latency ≤200 ms; **reliability:** successful valid order submissions ≥99.9% each month; **security:** every order-read request must be authorized for that customer or an explicitly permitted staff role, verified with cross-account tests. One could drop **safety** only if the scoped system cannot cause harm; document that assumption and revisit it if allergy handling, medical deliveries or vehicle control enter scope. Do not drop a characteristic merely because it is hard to measure.

### Q13 — Writing a Quality Requirement

**Card ID:** l01-quality-models-008

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ-L1-QM.html#question-13-writing-a-quality-requirement

> [!question] Question
> ## Question 13: Writing a Quality Requirement
>
> A developer writes: *"The system shall be fast and reliable."*
>
> Explain why this is a poor quality requirement. Rewrite it as **two separate testable requirements** using the template:
>
> ```text
> While [condition, with any measurement window], the [component] shall [measure] [threshold].
> ```
>
> Explain why the performance requirement uses a percentile rather than an average.

> [!answer]- Answer / self-check
> It is ambiguous, combines two attributes, and has no operating condition, threshold, or measurement. Split it. Example:
> - Under normal load, Search API p95 latency shall be <200 ms.
> - During production operation, monthly availability shall be ≥99.9%.
> Template: **While [condition and measurement window], the [component] shall [measure] [threshold].** A percentile bounds a specified share of requests; an average can hide a severe slow tail. Choose p95 or p99 according to user risk and include enough observations.

### Q14 — The Six Steps

**Card ID:** l01-quality-models-007

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ-L1-QM.html#question-14-the-six-steps

> [!question] Question
> ## Question 14: The Six Steps
>
> Apply the six steps to write a testable **reliability** requirement for a login service. Show your decision at each step.

> [!answer]- Answer / self-check
> 1. Determine relevant quality characteristics.
> 2. Consider system/use context.
> 3. Define quality criteria.
> 4. Select measures.
> 5. Specify a threshold requirement.
> 6. Evaluate testability, feasibility, and completeness.
> Example result: under normal load (<1000 concurrent users), search p95 latency shall be <200 ms.
> Reliability example for login: (1) choose reliability/availability; (2) define production traffic and a calendar-month window; (3) set a goal of dependable login; (4) measure successful valid login requests / valid login requests; (5) require **≥99.9% per month**; (6) check instrumentation, exclusions, achievable baseline and completeness, including dependency failures. The threshold is illustrative and must be agreed.

### Q15 — Quality in Use

**Card ID:** l01-quality-models-009

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ-L1-QM.html#question-15-quality-in-use

> [!question] Question
> ## Question 15: Quality in Use
>
> Explain the difference between product quality and quality in use. Give an example of a product with high product quality but low quality in use, and say how you would detect the problem.

> [!answer]- Answer / self-check
> - **Product quality:** properties of the software itself (e.g. reliability, maintainability, security).
> - **Quality in use:** whether specific users achieve goals effectively, efficiently, safely, and satisfactorily in context.
> - Example: a reliable, maintainable tax tool can still have confusing workflows that cause users to file incorrectly.
> Detect that gap with representative users doing real tasks in their context: measure task completion, errors, time and satisfaction, rather than relying only on code or availability metrics.

### Q16 — Process Quality

**Card ID:** l01-quality-models-017

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ-L1-QM.html#question-16-process-quality

> [!question] Question
> ## Question 16: Process Quality
>
> Name the four groups of process quality characteristics. Why does a high-quality process not guarantee a high-quality product?

> [!answer]- Answer / self-check
> **Suitability, usability, manageability, evolvability**, here describing the process rather than the product. A disciplined process can still implement mistaken requirements, use an unsuitable model or miss a risk. Process quality influences product quality, which influences quality in use; neither link is a guarantee.

### Q17 — Kano Model

**Card ID:** l01-quality-models-010

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ-L1-QM.html#question-17-kano-model

> [!question] Question
> ## Question 17: Kano Model
>
> Explain the difference between **must-be**, **one-dimensional** and **attractive** attributes. Classify two features of a video-streaming app into each category, and explain why a feature can move from attractive to must-be over time.

> [!answer]- Answer / self-check
> - **Must-haves:** expected basics; absence causes strong dissatisfaction, presence earns little extra praise. E.g. playback works; billing/account access is correct.
> - **Delighters:** unexpected benefits; absence is tolerated, presence raises satisfaction. E.g. excellent automatic highlights; unusually smart cross-device recommendations.
> - **One-dimensional:** more gives proportionally more satisfaction, e.g. higher video resolution and a larger useful catalogue (within the relevant range).
> As markets mature, delighters can become performance attributes and eventually must-haves.

### Q18 — Quality Pioneers

**Card ID:** l01-quality-models-018

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ-L1-QM.html#question-18-quality-pioneers

> [!question] Question
> ## Question 18: Quality Pioneers
>
> Match each idea to its pioneer and give one place it appears in software practice: Plan–Do–Check–Act; the quality trilogy; conformance to requirements; the fishbone diagram; the Capability Maturity Model.

> [!answer]- Answer / self-check
> - **Deming** popularized **PDCA**, building on Shewhart: iterative process-improvement experiments.
> - **Juran:** planning–control–improvement trilogy: quality objectives, release checks and retrospectives.
> - **Crosby:** conformance to requirements: explicit acceptance criteria and prevention.
> - **Ishikawa:** fishbone/cause-and-effect diagram: incident root-cause exploration.
> - **Humphrey:** software process maturity/CMM: assess and improve an organization's development process.
