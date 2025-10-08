# Labs Pack (Weeks 1–6) — Topics & Exam-Ready Explanations

*This is the labs companion to your 6-part pre-midterm set. I’m extracting the core topics from each lab deck and translating them into practical, exam-facing guidance. Dates below follow the files (order slightly diverges from the initial plan; I note where that happens).*

---

## Lab Week 1 — Course intro, team & case study setup (Aug 27, 2025)

### What the lab established

* **Project frame:** form **3–5 person** teams and pick **one case study** for the entire course. Once chosen, both are final. [L1]
* **Assessment cadence & weights:** attendance **15%**, lab assignments **30%** (each lab up to **2 points**: **1** core + **1** extra Q), midterm **15%**, final exam **40%**. Late labs without justification: **–50%**. All labs due **before the exam**. [L1]
* **12-week lab roadmap:** from case/topic selection → requirements → model/method choice → use cases → **detailed class diagram & architecture** → dynamics → test/maint plan → documentation. [L1]

### Why this matters for the midterm

* You’ll be asked to **justify choices** (model, methodology, architecture) using the **same artifacts** the labs require. Knowing the required **deliverables** and **grading criteria** lets you align your answers with how the course evaluates you.

**Quick check:** Can you articulate your team’s **case-study boundary** in 2–3 sentences and list the 3 most critical **quality attributes** you’ll protect? (You’ll use those in Weeks 3, 5, 6.)

**Source:** [L1]

---

## Lab Week 2 — Requirements elicitation (Sept 3, 2025)

### Topics & moves to master

* **Question types:** **open-ended** vs **closed-ended**; when to use which (open to explore; closed to pin specifics). [L2]
* **Elicitation structure:**

  1. Understand the **problem** and **domain** (become part of it).
  2. Elicit **success metrics** (these become **quality attributes** you’ll later make verifiable).
  3. Surface **constraints**: business rules, time/resources, budget, regulatory, technology. [L2]
* **Deliverable:** **≥15 well-formulated questions** that reveal **goals**, **boundaries/constraints**, **functionality**, **quality attributes**. [L2]

### Exam-facing explanation

* On the midterm, when given a vague brief, lead with **3–5 elicitation questions** that target **success metrics** (“What would count as a good launch? Which uptime/latency targets matter?”) and **hard constraints** (“Any regulated data? deployment windows?”). Then show how those answers map to **NFRs** and **architecture constraints** later.

**Source:** [L2]

---

## Lab Week 3 — List of requirements (ToR), prioritization, constraints (Sept 10, 2025)

### Topics & standards to apply

* **Why requirements:** reduce ambiguity, enable testing/acceptance, anchor scope/schedule, **guide architecture**. [L3]
* **FR vs NFR** basics. [L3]
* **Characteristics of good requirements:** atomic, achievable, cohesive, complete, current, independent, modifiable, traceable, unambiguous, **verifiable**, necessary. (Memorize this “A-list”.) [L3]
* **Worked rewrites:** examples turning vague FR/NFR into **testable** statements (e.g., availability with a window and measurement method; auth latency with **p95/p99** targets). [L3]
* **Prioritization:** **MoSCoW** (Must/Should/Could/Won’t) + rationale. [L3]
* **Architecture constraints:** capture the **“box you’re designing inside”** (legacy compatibility, budget, skills, tech stacks, compliance). [L3]
* **Deliverable:** a **ToR** containing **prioritized FR table**, **prioritized NFR table**, and a **list of architecture constraints**. [L3]

### Exam-facing explanation

* Expect prompts like “rewrite this requirement to be verifiable.” Use the **pattern**: *action + measurable threshold + scope/window + how measured*. For constraints, explicitly state **implications** (e.g., “must run on X DB” ⇒ affects **AL** design and **scalability** options).

**Source:** [L3]

---

## Lab Week 4 — Use-Case Diagram (Sept 17, 2025)

> Note: The initial plan had “choosing model/methodology” earlier, but the actual file order shows **Use Cases in Week 4**. I follow the files.

### Topics & minimum bar

* **Purpose:** depict functionality from **user perspective**; identify **actors**, **system boundary**, **use cases**, **packages**. [L4]
* **Relationships:** **association**, **generalization**, **include**, **extend**—know when each applies. [L4]
* **Workflow example:** stepwise table (main path + alt/failure paths). [L4]
* **Task constraints:** diagram must show **≥3 actors**, **≥2 system components**, **≥10 use cases**, and include **all four relationship types**. Tools: Draw.io / PlantUML / StarUML. [L4]

### Exam-facing explanation

* When asked to “sketch use-cases,” always:

  1. Draw the **system boundary** box;
  2. Place **actors** (including external systems);
  3. Use **include** for reusable flows (e.g., “Authenticate user”), **extend** for optional/exceptional behavior (“Apply coupon” if condition met);
  4. Pair the diagram with **one short scenario** (main + alt) to remove ambiguity.

**Source:** [L4]

---

## Lab Week 5 — Choosing a lifecycle model & development methodology (Sept 24, 2025)

### Topics & decision logic

* **Model vs methodology:** model = **process/order of phases**; methodology = **how teams work** (roles, artifacts, practices). [L5]
* **Models to compare:** **Build-and-Fix**, **Waterfall**, **Incremental**, **Spiral**, **Rapid Prototyping** (not standalone). Pros/cons summarized (e.g., Spiral = risk-driven but demands risk expertise; Incremental = early ROI but needs open architecture). [L5]
* **Methodologies:** **RUP** (tailorable, architecture-centric), **Scrum** (empirical, lightweight artifacts), **XP** (quality via TDD, CI, pair programming). With advantages/disadvantages grid. [L5]
* **Selection questions (Rockwood):** team size/competence; product size/complexity; management style; org-wide vs project processes; requirement stability; traceability/compliance needs. [L5]
* **Deliverable:** pick **one model** and **one methodology** for your project, and **justify** across: product type, scale, team size/competence, bureaucracy, artifacts needed, technical factors. [L5]

### Exam-facing explanation

* Use the **decision template**: *Context → Primary qualities/risks → Lifecycle model (why) → Methodology (why) → Artifacts & cadence → Known pitfalls + mitigations*. Concrete example: **Incremental + Scrum** for early value with changing requirements; **Waterfall(+prototyping) + RUP-ish artifacts** for stable specs & compliance.

**Source:** [L5]

---

## Lab Week 6 — Detailed Class Diagram & Final Architecture Choice (Oct 1, 2025)

### Topics to nail

* **Midterm logistics (FYI):** **Oct 8, 2025, 14:30–15:30**, closed-book, covers **Weeks 1 → current**; rooms posted **Oct 7** on Telegram. (Plan your revision timeline.) [L6]
* **UML Class theory:** class, attributes, methods; **visibility** (`+`/`-`/`#`/`~`); **parameter directionality** (in/out/inout) and how different languages express it. [L6]
* **Relationships:** **association** (don’t duplicate as fields), **cardinality** (1, 0..1, 1..*, 0..*), **inheritance/generalization**, **realization** (interface→impl), **dependency** (use without ownership), **aggregation vs composition** (lifecycle & ownership). [L6]
* **Task constraints (strict):** **≥10 classes**; each with **name, attributes, methods with parameters & visibility**; **≥4 relation types** used; **cardinality on all associations**; **≥1** explicit **parameter directionality** example. [L6]
* **Architecture choice (final, with justification):** tie your class design to **PL/BL/AL placement** and chosen **model/methodology**; call out quality tactics (e.g., caching, auth). [L6]

### Exam-facing explanation

* Class diagrams **without** cardinalities/visibility lose points; include them.
* Don’t misuse composition—reserve it for **shared lifecycle** (e.g., `Order` owns its `OrderLine`s).
* Add a short **sequence diagram** for one critical flow to lock call order (even if not required here, it helps you defend design questions).

**Source:** [L6]

---

## Cross-lab “glue” (how these feed your midterm answers)

1. **Traceability chain you can recite & demonstrate:**
   *Elicited Qs (W2) → ToR with prioritized FR/NFR & constraints (W3) → Use-Case Diagram + scenarios (W4) → Lifecycle model + methodology (W5) → Detailed Class Diagram + Architecture placement (W6)*. Use this chain to structure any long-form answer.

2. **Quality attributes are first-class:** define **measurable** NFRs (W3) and keep pointing to **where** you realize them in the design/architecture (W6).

3. **Right-weight documentation:** build exactly the artifacts the labs ask for—examiners grade to this rubric.

---

## Speed-drill checklist (10–15 min per lab theme)

* **W2:** Write **5** elicitation Qs that produce **measurable** NFRs and **3** that expose constraints.
* **W3:** Rewrite one vague FR and one vague NFR into verifiable specs; place **3** items into MoSCoW with a one-line business rationale each.
* **W4:** Sketch a use-case boundary box with **3 actors, 10 use cases, include/extend/generalization**, and one short main+alt scenario.
* **W5:** Pick model+method for your case study; defend with **team competence, requirement stability, compliance**.
* **W6:** Draw a **10-class** diagram with **4 relation types** and **cardinalities**; add one **in/out** parameter and a 6-message **sequence** for a critical flow.

---

## References (IEEE-style)

[L1] **Lab deck**: “Lab Week 1 (Introduction to SA).pdf,” *Software Architecture Labs — Introduction, team & case selection; lab grading & plan*, Aug. 27, 2025.
[L2] **Lab deck**: “Lab Week 2 (Requirements Gathering).pdf,” *Requirements elicitation—question types, elicitation structure, constraints; deliverable: ≥15 questions*, Sept. 3, 2025.
[L3] **Lab deck**: “Lab Week 3 (List of Requirements).pdf,” *ToR: FR/NFR quality criteria, MoSCoW prioritization, architecture constraints; worked rewrites*, Sept. 10, 2025.
[L4] **Lab deck**: “Lab Week 4 (Use Case Diagram).pdf,” *UML use-case components & relationships; workflow examples; deliverable requirements*, Sept. 17, 2025.
[L5] **Lab deck**: “Lab Week 5 Choosing a model and methodology.pdf,” *Lifecycle models vs. methodologies; comparative analysis; selection questions; justification task*, Sept. 24, 2025.
[L6] **Lab deck**: “Lab Week 6.pdf,” *Detailed class diagram & final architecture choice; UML relationships, visibility, parameter directionality; midterm announcement*, Oct. 1, 2025.

[<kbd><br><- Return (PreMid)<br></kbd>](PreMid.md)
