# Pre-Midterm Header — Lectures & Labs Overview (Weeks 1–6)

> Each row links to your weekly digest. For exam prep, scan this first, then dive into the linked file.

## Lectures (Weeks 1–5)

> **Note:** **10 Sep 2025 — no lecture** (department scheduling); the next lecture was on 17 Sep.

| Week | Date (2025)    | File                               | Theme                               | General topics (exam-relevant)                                                                                                                                                                                                                                                |
| ---- | -------------- | ---------------------------------- | ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | Wed **Aug 27** | [Lecture01.md](./Lecture01.md) [1] | **Course Intro & Lifecycle Models** | Course mechanics & grading; what “software architecture” is; lifecycle stages; models to contrast: *Build-and-Fix, Waterfall (+V), Rapid Prototyping, Incremental/Evolutionary, Spiral, Synchronize-and-Stabilize, OO/Fountain*; how model choice ties to quality attributes. |
| 2    | Wed **Sep 3**  | [Lecture02.md](./Lecture02.md) [2] | **Development Methodologies**       | RUP (phases, milestones, disciplines); MSF (team/process model, Stabilize nuance); Scrum (roles, events, artifacts, empirical control); XP (values, 12 practices, spikes/TDD/CI); how to pick & tailor a method to a chosen lifecycle model.                                  |
| —    | **Sep 10**     | —                                  | **No lecture**                      | (Keep labs moving; requirements work continues.)                                                                                                                                                                                                                              |
| 3    | Wed **Sep 17** | [Lecture03.md](./Lecture03.md) [3] | **Software Architectures**          | Open systems; client/server internals; **PL/BL/AL** splits (thick/thin/3-tier); RPC; web 2-tier vs 3-tier and server-side extensions; DB server models; integrated/federated/multi-DB; grid systems; how to make diagrams actionable; quality trade-offs.                     |
| 4    | Wed **Sep 24** | [Lecture04.md](./Lecture04.md) [4] | **.NET Platform & OOA**             | .NET as **vision/model/platform/toolkit**; CLR→MSIL→JIT; assemblies, CLS/CTS, BCL, ADO.NET, ASP.NET; component programming; **OOA**: use-cases & scenarios, noun extraction & class modeling, dynamic models (sequence/state).                                                |
| 5    | Wed **Oct 1**  | [Lecture05.md](./Lecture05.md) [5] | **OO Design & Detailed OOD**        | Modularity, cohesion, coupling; OOD workflow (**sequence → detailed class diagrams → state**); signatures/visibility/cardinality; detailed design spec (interfaces, algorithms, data structures); V&V/traceability of the design.                                             |

## Labs (Weeks 1–6)

| Week | Date (2025)    | File                                 | Focus                                     | What you produce / practice (for the midterm)                                                                                                                                                                        |
| ---- | -------------- | ------------------------------------ | ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | Wed **Aug 27** | [LabsPreMid.md](./LabsPreMid.md) [6] | **Intro & setup**                         | Form team + pick one case study; understand grading & cadence; define project boundary and initial quality drivers.                                                                                                  |
| 2    | Wed **Sep 3**  | ↑ same                               | **Requirements Elicitation**              | ≥15 elicitation questions; surface goals, constraints, success metrics; turn them into measurable NFRs later.                                                                                                        |
| 3    | Wed **Sep 10** | ↑ same                               | **ToR: FR/NFR & Prioritization**          | FR/NFR tables with **verifiable** wording; MoSCoW prioritization; architecture constraints (tech/compliance/legacy).                                                                                                 |
| 4    | Wed **Sep 17** | ↑ same                               | **Use-Case Diagram**                      | System boundary, ≥3 actors, ≥10 use-cases; relationships (**include/extend/generalization**); one short main/alt scenario.                                                                                           |
| 5    | Wed **Sep 24** | ↑ same                               | **Choose Model & Method**                 | Pick a lifecycle model + methodology; justify with context, risks, qualities, artifacts, cadence; mitigation of known pitfalls.                                                                                      |
| 6    | Wed **Oct 1**  | ↑ same                               | **Detailed Class Diagram & Architecture** | ≥10 classes with attributes/methods/visibility; cardinalities & ≥4 relation types; note parameter directionality; finalize PL/BL/AL placement coherent with your chosen model/method; (midterm logistics announced). |

---

### File references (IEEE-style)

[1] **Lecture01.md** — *Course Introduction & Lifecycle Models*, 27 Aug 2025.
[2] **Lecture02.md** — *Development Methodologies (RUP, MSF, Scrum, XP)*, 3 Sep 2025.
[3] **Lecture03.md** — *Software Architectures (client/server, web tiers, DB models, grids)*, 17 Sep 2025.
[4] **Lecture04.md** — *.NET Platform & Object-Oriented Analysis*, 24 Sep 2025.
[5] **Lecture05.md** — *Object-Oriented Design & Detailed OOD*, 1 Oct 2025.
[6] **LabsPreMid.md** — *Labs Pack (Weeks 1–6): setup, elicitation, ToR, use-cases, model/method, class diagram & architecture*, 27 Aug–1 Oct 2025.

[<kbd><br><- Return (SoftArch)<br></kbd>](SoftArch.md)
