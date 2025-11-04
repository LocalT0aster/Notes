# Lecture 1 — Course Introduction & Lifecycle Models (pre-midterm rehearsal)

> Sources used this week: the live lecture transcript [1], **Course Introduction** slides [2], **Lifecycle Models** slides [3], and the **Software Lifecycle** slides (not delivered in class this year, but useful for self-study) [4]. I clearly mark where something comes only from [4].

---

## 1) Course mechanics & deliverables (know this first)

**What the course expects from you (and what it does *not*):**

* Team project (≈5–6 people) producing **documents and diagrams** (no coding required). Final exam = **project defence** (≈5′ talk + Q&A) based on those artifacts. [1], [2]
* **Assessment weights** (verbatim from intro): **Lab attendance 15%**; **Lab documents 30%**; **Midterm quiz 15%**; **Final project defence 40%**. [1]
* Labs mirror lifecycle steps: refine requirements with the “client” (your TA), justify an **architecture**, select **technologies/tools**, and **document** with UML + prose. [1], [2]

**Practical takeaways for the midterm:**

* Be able to **argue** a life-cycle/model choice for a project brief (e.g., “elevator control” example): constraints, risks, client literacy, and delivery mode. [1], [3]
* Be ready to **name, draw, and contrast** the core models (below) and relate them to **quality attributes** (availability, performance, security, modifiability, etc.). [2], [3]

---

## 2) What *software architecture* is (and isn’t)

**Working definition (course view):**

* A **high-level blueprint**—a **declarative partitioning of responsibilities** into **elements (components)** and **relations (connectors)**, with properties of both. Suppresses private/internal details. [2]
* Architecture gives **policy & structural guidance** to detailed design and construction; it is the **framework** connecting requirements to implementations. [2]

**Why architecture matters (exam-friendly bullets):**

* Determines **systemic properties** (security, performance, availability, scale, modifiability) that **cannot be “fixed later”** by local refactors alone. [2]
* **Exposes risks early**; helps coordinate teams (shared blueprint); aligns technology choice with business constraints. [2]
* **Right-weight, not heavy-weight**: investment depends on size, distribution, novelty, and desired product velocity. [2]

**Anti-patterns to recognize:**

* **Architecture astronautics**: abstractions so high they give no guidance to builders. [2]
* **Code-first / design-late**: unpredictable emergent properties; costly refactor, sometimes infeasible. [2]

**Representations you should know:**

* **Static vs dynamic views**; **components & connectors** diagrams; **UML** (class, sequence/activity, etc.); prose to remove ambiguity (e.g., directionality, payload types). [1], [2]

---

## 3) Lifecycle models you must be fluent in

For each model: **Idea → When to use → Strengths → Pitfalls → One-line diagnostic.**

### 3.1 Code-and-Fix (Build-and-Fix) — *incomplete lifecycle*

* **Idea:** Minimal upfront spec/design; build a version, show to client, **modify until accepted**. [3], [4]
* **Use when:** **Very small** scope with **clear, stable requirements** and **predictable behavior** (think << 1K LOC guideline in slides). [3]
* **Strengths:** Tiny overhead, quick start. [3]
* **Pitfalls:** Late discovery of early errors ⇒ cost spikes; **non-scalable** beyond trivial problems. [3], [4]
* **Diagnostic:** “We’ll just hack until they like it.” → That’s Code-and-Fix.

### 3.2 Waterfall (+ V-model variant) — *one-pass with feedback inside phases*

* **Idea:** Sequential phases (**Requirements → Design → Coding/Testing → Delivery/Maintenance**) with **verification after each**; phases “freeze” when signed off. [3]
* **Use when:** **Technically literate customer**, **stable complete specs**, and **need the full system at once** (typical: **government/military**). [1], [3]
* **Strengths:** **Traceability, visibility**, easier cost/schedule estimation; early feedback to previous *phase* (not whole iterations). [3]
* **Pitfalls:** **Rigid to change**; often **misses user expectations** if customer can’t validate via specs; needs **prototyping add-on** under higher risk. [3]
* **V-model:** Mirrors dev & test levels (requirements↔acceptance, design↔integration, detailed design↔unit tests). [3]
* **Diagnostic:** “Water never goes up” slide—sequential descent with checks. [1], [3]

### 3.3 Rapid Prototyping — *not a stand-alone lifecycle*

* **Idea:** Build throw-away prototypes to clarify **requirements/architecture**; **do not ship** the prototype. [3]
* **Use when:** **Client is not technically fluent**, product vision unclear; need to **reduce technical risk cheaply**. [3]
* **Strengths:** Shared understanding; early risk surfacing. [3]
* **Pitfalls:** **Temptation to ship prototype code** (under-tested/undocumented); must “throw away & redo” in the chosen main model. [3]
* **Diagnostic:** “Prototype is not a product.”

### 3.4 Incremental (and Evolutionary) — *feature-additive releases*

* **Idea:** Deliver **operational product each increment**; add subsystems stepwise; each release includes design→implementation→integration→test. [3]
* **Use when:** You can architect for **scalable evolution**; desire **earlier ROI**; environment supports **deployment of partial functionality**. [3]
* **Strengths:** Working product **at every step**; **flexible rollout**; easier maintenance via **straightforward expansion**. [3]
* **Pitfalls:** Requires **open, extensible architecture** and **stable upgrade path**; can **degenerate into Code-and-Fix** if concept keeps shifting. [3]
* **Diagnostic:** “Always shippable slice” with room to grow.

### 3.5 Spiral (Boehm) — *risk-driven iteration*

* **Idea:** Iterations (spirals) with **4 activities**: (1) **goals/alternatives/constraints**, (2) **evaluate & mitigate risks** (incl. prototypes), (3) **develop & verify**, (4) **plan next cycle**. [3]
* **Use when:** **Large internal** projects; organization has **risk management expertise**; high uncertainty. [3]
* **Strengths:** **Risk surfaced early**, supports **re-use** via alternative evaluation; smoother **transition to maintenance**. [3]
* **Pitfalls:** Expensive to run for small projects; **requires risk skills**; typically **in-house** context. [3]
* **Diagnostic:** “What’s our biggest risk this loop?” If that drives the plan, it’s Spiral.

### 3.6 Synchronize-and-Stabilize (Microsoft style)

* **Idea:** Time-boxed **synch** (frequent integration, testing) and **stabilize** (bug reduction, “freeze” slices) across 3–4 staged versions (critical → less critical features). [3]
* **Use when:** Product & tooling support **test automation** and **very frequent integration**. [3]
* **Strengths:** **Early & continuous testing**, always-integrated product, earlier detection of cross-module issues. [3]
* **Pitfalls:** Non-dev time spent on sync/stabilization; **rare outside Microsoft**; heavy CI discipline required. [3]
* **Diagnostic:** Regular “freezes” of an integrated slice with parallel streams continuing.

### 3.7 Object-Oriented / “Fountain” — *phase overlap & backtracks*

* **Idea:** **OOA/OOD phases interleave**; intensive interaction and backtracking; analysis artifacts (use-cases, object models) flow into design. [3]
* **Use when:** Team is **OO-mature**, process discipline in place; domain modeling central. [3]
* **Strengths:** **Parallelism** and **iteration within phases**; natural fit for OO reuse. [3]
* **Pitfalls:** Can **degenerate into CABTAB** (“code a bit, test a bit”) if discipline is weak. [4]
* **Diagnostic:** Blurred phase boundaries with explicit OO analysis/design loops.

---

## 4) The **software lifecycle stages** (from [4] — **self-study addition**)

> These slides were **not delivered in class this year**, but they’re great exam fodder and help justify model choices.

**Canonical stages** (methodology-agnostic): **Requirements → Specifications → Design (preliminary & detailed) → Implementation → Testing → Integration/Deployment → Maintenance → Decommissioning**. All stages produce **documentation** and inter-relate. [4]

**Economics you should memorize:**

* **Maintenance dominates**: ~**67%** of cost/time over the lifecycle; coding ≈ **5%**, testing ≈ **7%**, with substantial schedule share in requirements/design/integration. Detecting bugs **later** costs **exponentially** more. [4]
* Implication for architecture & models: invest **early** in clarifying requirements, risks, and architecture; choose models that **surface errors early** for your context. [4]

**Maintenance types:** corrective, adaptive, perfective (performance), and enhancing/updates. [4]

---

## 5) Architecture ↔ Process: agile, “right-weight” design, and trade-offs

* **Agile vs. architecture** is a false dichotomy: architecture provides a **framework for agile teams** so systemic qualities are addressed early, **delaying or avoiding costly refactors**. [2]
* **Right-weight design:** tailor architecture effort to **size, distribution, novelty, and velocity**; avoid both “no-design” and “analysis paralysis.” [2]

**Likely midterm prompts & how to answer:**

* *“Pick a lifecycle model for system X and defend it.”*
  -> State **context** (client literacy, risk, size), **primary quality attributes**, **delivery cadence**, then map to model **criteria** (e.g., Incremental for early ROI + modifiability; Waterfall + prototyping for stable, spec-driven gov project). Cite **trade-offs** explicitly. [2], [3], [4]
* *“Why can’t we just refactor architecture later?”*
  -> Because **systemic properties** derive from **global structure**; some changes are **cost-prohibitive or infeasible** post-hoc. [2]

---

## 6) Diagrams & documentation (what to produce in labs)

* **UML set** (tailor to your case):

  * **Static:** Class/package/component diagrams for **components & connectors** and interfaces.
  * **Dynamic:** Sequence/activity/state for **protocols, data flows**, and **quality scenarios** (e.g., failover).
* **Prose that removes ambiguity:** define **connector directions**, **payloads** (APIs, protocols, data types), and **assumptions/constraints** (e.g., thread model, latency budgets). [1], [2]
* **Quality attribute scenarios**: e.g., “**Availability 99.95%**: on DB failure, API recovers within **30 s** with no data loss.” Tie each scenario to **architectural tactics** (replication, retry/backoff, circuit breakers, etc.). [2]

---

## 7) Rapid practical drills (10–15 minutes each)

1. **Model picker:**
   Given: “Campus elevator controller; safety-critical; fixed regulatory spec; must deliver complete system; client is technically literate (facilities).”

   * **Answer:** Waterfall **+** V-model **+** **early prototyping** of safety interfaces; justify with **spec stability** and **acceptance testing mapping**. Note **change-management risks**. [3]

2. **Risk loop (Spiral):**
   List top 3 risks for “IoT smoke sensors over unreliable network,” pick one (network partitions), sketch **prototype** to measure MTBF/latency, and define **success threshold**. [3]

3. **Increment design:**
   Plan 3 increments for an **e-shop** (slides mention a business case): **(1)** catalog & auth, **(2)** cart & payments, **(3)** order tracking & returns. Show how you keep an **operational product** at each step and which **interfaces** must be stable from day 1. [3]

---

## 8) Common pitfalls to avoid

* Shipping a **prototype** (meant for learning) as production code. [3]
* Choosing Waterfall with a **non-literate** client or fluid requirements. [3]
* Claiming Incremental while making **architecture decisions** that **block future slices** (no extensibility). [3]
* Treating architecture as a **big-upfront design artifact** detached from **quality scenarios** and **team coordination**. [2]

---

## 9) What to memorize vs. what to *be able to argue*

**Memorize:** model names, **one-line essence**, 1–2 **key strengths**, 1–2 **key pitfalls**, **maintenance≈67%** fact, and the **canonical stage list**. [3], [4]
**Argue:** model selection **given a context**, mapping from **quality attributes → architectural tactics → lifecycle implications**, and why **right-weight** architecture beats both extremes. [2], [3], [4]

---

### References (IEEE-style)

- [1] **Lecture transcript**: “Lecture01_2025-08-27.merged.txt,” live class notes (course intro; project/assessment; lifecycle overview; Q&A), Aug. 27, 2025.
- [2] **Slides**: “Lecture01_CourseIntroduction.pdf,” *Based on ISR: Architectures for Software Systems* (architecture motivation, definitions, agile vs. architecture, right-weight design), Sept. 2023.
- [3] **Slides**: “Lecture01_Lifecycle_Models.pdf,” *Enterprise Software Systems Development — Lifecycle Models* (Build-and-Fix, Waterfall/V-model, Rapid Prototyping, Incremental/Evolution, Spiral, Synchronize-and-Stabilize, OO/Fountain; pros/cons and applicability), 2024.
- [4] **Slides (self-study)**: “Lecture01_SoftwareLifecycle.pdf,” *Architecture of Software Systems — Software Lifecycle* (stages, roles, economics, maintenance share, comparative model analysis), 2021.

[<kbd><br><- Return (PreMid)<br></kbd>](PreMid.md)
