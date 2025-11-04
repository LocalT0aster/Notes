# Lecture 2 — Development Methodologies (RUP, MSF, Scrum, XP, Agile)

> Sources this week: the live lecture transcript [1] and the “Development Methodologies” slide deck [2]. No lab slides were provided for Week 2; I’ll flag lab-style drills where appropriate so you can still rehearse.

---

## 0) First principles (model vs. methodology)

* **Pick a lifecycle model first, then a methodology** to support/realize it. A model shapes *when* and *how often* you iterate; a methodology adds **roles, artifacts, and practices** that operationalize the work. [1], [2]
* Most methodologies are **process frameworks** (tailorable) **and** **sets of best practices**. Exam trick: you’re expected to scale them **down** for small teams and **up** for enterprise contexts. [1], [2]

**What to be able to do on the midterm:**
Explain which model fits a scenario (risk, domain knowledge, client literacy), then justify a methodology **and** the specific artifacts you’d produce.

---

## 1) RUP — Rational Unified Process

### Essence

* **Iterative**, **architecture-centric**, **use-case–driven**. [2]
* A tailorable **process framework** + **best practices** (manage requirements, iterative dev, component architecture, visual modeling, quality monitoring, change management). [2]

### Phases, iterations, milestones

* **Phases**: *Inception* (what we build), *Elaboration* (how we’ll build; stabilize architecture), *Construction* (build & test), *Transition* (acceptance/deployment). [2]
* **Iterations** exist inside phases; RUP names key milestones such as **Lifecycle Objectives**, **Lifecycle Architecture**, **Initial Operational Capability**, **Product Release**. [2]

### Disciplines, roles, artifacts

* Work streams like **business modeling, requirements, analysis & design, implementation, test, deployment, configuration/change mgmt** run across iterations. [2]
* **Role → tasks → artifact** pattern (e.g., *Designer* “analyzes use case” → “designs use case” → produces **Use-Case Realization**, guided by **templates** and **tool manuals** such as Rational Rose). [2]

### How RUP maps to lifecycle *models*

* **Cascade/Waterfall within RUP**: single iteration when scope is small and well-understood.
* **Incremental within RUP**: multiple development iterations; requires stable architecture and known risks.
* **Evolutionary within RUP**: for new/uncertain domains or inexperienced teams (earlier risk attack, prototyping). [2]

### Ideology & exam pitfalls

* “Attack main risks early,” “Executable architecture early,” “Adapt from day one.” [2]
* Pitfalls: treating RUP as **rigid** (it’s tailorable), or ignoring the **architecture-centric** requirement.
* **What to sketch**: a timeline annotated with phases, iterations, and which **disciplines** are “thick” in each. [2]

**Lab-style drill:**
Given a brief (“payment gateway add-on to a mature e-shop”), pick **RUP incremental**, list 2–3 iterations, specify artifacts per iteration (use-case refinements, component diagram deltas, test cases). Defend why **Elaboration** finishes when the architecture is *stable enough*. [2]

---

## 2) MSF — Microsoft Solution Framework

### Essence

* **Integrated approach** with **Agile** and **Formal** instantiations; **not** a lifecycle model by itself. Comes with **team model**, **process model**, **management disciplines**, and is implemented in Microsoft toolchains. [2]

### Principles and team model

* Principles: **client partnership, open communication, shared vision, quality every day, flexibility, implementation habit, value focus**. [2]
* **Team of equals** with clear responsibility areas; ensure **all stakeholder interests** are represented (UX, operations, security, etc.). [2]

**Roles/areas (v4.0):** *Program Mgmt, Product Mgmt, Development, Testing, User Experience, Release/Operations,* and **Architecture** (explicit in v4.0). Some role combinations are **possible**, others **not recommended** (know the idea, not the entire matrix). [2]

### Process model (stages + control points)

* **Envision → Plan → Develop → Stabilize → Deploy** with control gates: *vision/boundaries approved*, *plans approved*, *release readiness approved*, *deployment complete*. [2]

**The “Stabilize” nuance (high-yield exam point):**

* MSF runs extensive **integration + automated testing** across many **candidate builds** to select a stable release. Outside Microsoft, teams **often stall** here (quality rises but **no new features**); misuse leads to schedule drag. [1]

### Trade-offs & use-outside-Microsoft

* Strong for **product groups with mature automation**; **harder** to apply verbatim elsewhere. If you cite MSF, show **how** you’ll avoid stabilisation sinkholes (e.g., Definition of Done, capped test matrices). [1], [2]

**Lab-style drill:**
You inherit a service with flaky releases. Propose **MSF-like** staging with a *short* Stabilize window, explicit **release readiness checklist**, and **contradiction (triple-constraint) matrix**: if resources drop, you either **move the date** or **descope** features. [2]

---

## 3) Scrum — Adaptive Project Management

### Core idea

* Use **empirical process control** when the problem **cannot be fully defined upfront**; maximize responsiveness through short, time-boxed cycles. [2]

### Mechanics

* **Live Product Backlog** prioritized by value; **Sprints** (short, fixed-time iterations); **Daily Scrum** (yesterday/today/blockers); **Sprint Planning**, **Review**, **Retrospective**. [2]
* **Roles**: *Product Owner* (backlog/value), *Scrum Master* (process & impediments, often 50% developer), *Scrum Team* (no titles beyond “member”). [2]
* **Artifacts**: Product/Release **backlogs**, **Sprint backlog**, **burndown** (iteration task chart), plus change/config mgmt. [2]
* **Lifecycle framing** (slides’ phrasing): **Pre-game (planning & architecture)** → **Game (development: double-shot, review, correction)** → **Post-game (release)**. [2]

### Strengths vs. risks

- Transparency, client co-creation, frequent working increments, strong team learning.
- Minimal formal docs outside management; architecture can be **under-elaborated** if teams chase short-term velocity only. [2]

**Lab-style drill:**
Turn vague stakeholder wishes into a **backlog** (story + acceptance criteria). Plan a 2-week sprint: pick top items, define **DoD** with demo conditions, and outline the **review**. Show one **risk** you’ll spike early.

---

## 4) XP — eXtreme Programming

### Origins & values

* Originated by **Kent Beck**, **Ward Cunningham**, **Ron Jeffries** (C3 project); values: **Communication, Simplicity, Feedback, Courage, Respect**. [2]

### Principles & 12 practices (know the names + intent)

* **Timely feedback**, **implied simplicity**, **incremental change**, **embrace change**. [2]
* Practices include **Planning Game**, **Small Releases**, **System Metaphor**, **Simple Design**, **Test-First/Advanced Testing**, **Refactoring**, **Pair Programming**, **Collective Code Ownership**, **Continuous Integration**, **40-hour week**, **On-site Customer**, **Coding Standards**. [2]

### Lifecycle & roles

* Flow: **Study/Spike → Release Planning → Iterations (tests & programming) → Release → Support**, with **acceptance tests written by the customer**. Roles include **Customer**, **Programmer**, **Tester**, **Coach/Mentor**. [2]

### Strengths vs. risks

* Bakes quality in (TDD/CI), real customer feedback, measurable cadence.
* Heavy reliance on oral communication; **practices work best together**; **little formal design notation**; **simple design** can mean **insufficient architectural elaboration**. [2]

**Lab-style drill:**
For a risky algorithmic part, plan an **Architectural Spike**; write a **failing test first**, define a “**small release**” boundary, and state the **refactoring** you expect once the spike informs the design.

---

## 5) Choosing methodology for a scenario (decision cheats)

| When you see…                                               | Prefer…                                         | Justify with…                                                         |
| ----------------------------------------------------------- | ----------------------------------------------- | --------------------------------------------------------------------- |
| **Stable requirements, literate client, one-shot delivery** | **RUP (cascade-ish)**                           | Traceability, clear milestones, acceptance mapping. [2]               |
| **Known domain, want early value**                          | **RUP (incremental)** or **Scrum**              | Shippable increments + architecture sustained across iterations. [2]  |
| **New domain, high uncertainty, team green**                | **RUP (evolutionary)** + **Scrum**/XP practices | Risk-first learning, spikes, evolving reqs. [2]                       |
| **Product org with strong automation**                      | **MSF (Agile or Formal)**                       | Team model covers all stakeholder qualities; gated stabilization. [2] |

**Exam stance template (use this even if rushed):**

* **Context** (domain knowledge, risk, client literacy, delivery cadence) → **primary quality attributes** → **model** → **methodology** → **artifacts & roles** → **known pitfalls + mitigations**. [1], [2]

---

## 6) Quick-fire rehearsal prompts

1. **Explain “architecture-centric” in RUP** and list the **evidence artifacts** you’d expect by the **Lifecycle Architecture** milestone. [2]
2. **MSF Stabilize**: why does it exist, and how would you **time-box** it outside Microsoft to avoid “quality with no features”? [1], [2]
3. Convert a vague feature (“better search”) into **Scrum items** with **acceptance criteria** and a **demo plan**. [2]
4. In XP, defend **Pair Programming + TDD** to a skeptical PM who wants velocity this sprint. Tie it to **defect prevention** and **safe refactoring**. [2]

---

## 7) Common mistakes to avoid (the “gotchas”)

* Treating RUP as fixed, not **tailorable**; skipping **executable architecture** in Elaboration. [2]
* Doing Scrum with **demo-able UI only** but no **quality bar** (no DoD), causing hidden debt. [2]
* Copying MSF’s **Stabilize** stage **without** automation capacity. [1]
* Doing XP “à la carte”; many of its benefits appear when **practices reinforce each other**. [2]

---

### References (IEEE-style)

- [1] **Lecture transcript**: “Lecture02_2025-09-03.merged.txt,” live class notes (RUP, MSF, Scrum/Agile overview; pitfalls; MSF stabilization nuance), Sept. 3, 2025.
- [2] **Slides**: “Lecture02_DevMethodologies.pdf,” *Software System Architecture — Lecture 4: Software System Development Methodologies* (RUP essence/iterations/disciplines; MSF team & process model; Scrum/XP values, roles, artifacts, pros/cons), HSE University, 2025.

[<kbd><br><- Return (PreMid)<br></kbd>](PreMid.md)
