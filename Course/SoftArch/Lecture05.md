# Lecture 5 — Object-Oriented Design (OOD) & Detailed OO Design

*Pre-midterm rehearsal digest with exam-grade depth*

> Sources this week: the live lecture transcript [1], the **OOD** slide deck (principles, approaches, architectural design) [2], and the **Detailed OOD** slide deck (detailed class diagrams, dynamics, project testing) [3]. No separate lab slides were provided; I’ve added targeted “lab-style drills” so you can rehearse the exam moves.

---

## 0) What this week actually covers (so you study the right things)

* **Bridge from analysis to buildable design.** You start with **use-case scenarios** and finish with **detailed class/interaction/state diagrams** and a **detailed design spec** (interfaces, algorithms, data structures). [1]–[3]
* **Principles to apply everywhere:** **modularity, high cohesion, low coupling**, with explicit **traceability** from requirements → use cases → classes → interactions/states. [2], [3]

**Midterm value:** you’ll be asked to **choose/design** artifacts that make implementation unambiguous (who calls whom, in what order, with what signatures). OOD is where you prove that. [1]

---

## 1) OOD principles you must name and use

* **Modularity** — split the system into manageable, independently understandable pieces. Helps localize defects and reduces change ripple. [2]
* **Cohesion** — how tightly responsibilities inside a module fit together. Prefer **functional/informational cohesion**; avoid “grab-bag” modules. [2]
* **Coupling** — how much modules rely on one another. Lower is safer. Avoid **content/shared/control coupling**; move toward **data coupling** (clean interfaces, narrow parameter sets). [2]

**Exam cue:** given a muddled “God class,” show a refactor plan that **raises cohesion** and **reduces coupling**, and say **which dependencies move across which interfaces**. [2]

---

## 2) Design approaches (know the comparison, pick OOD deliberately)

* **AOD (Action-Oriented)** — decomposes **processing steps** (DFD, transaction analysis). Useful to understand flows; **risk**: can produce brittle module boundaries. [2]
* **DOD (Data-Oriented/Jackson)** — structures mirror data; largely historical. [2]
* **OOD (Object-Oriented)** — equal attention to **data + behavior**; targets **high cohesion, low coupling** with **classes/objects** and **interactions**. This is the **default** for the course. [2]

**How to answer**: “We adopt OOD; AOD/DFD will support early flow understanding, but modules are decided by **domain objects & collaborations**, not just steps.” [2]

---

## 3) The OOD workflow (ordered, with deliverables)

> **From OOA to OOD**: you **refine** analysis results into build-ready design artifacts. [2], [3]

1. **Interaction diagrams** for key scenarios — **sequence** (or collaboration; they’re isomorphic). Purpose: **ordering of calls** and **who calls whom**. Include nominal + alternate paths (e.g., login success/failure). [1]–[3]
2. **Detailed class diagrams** — expand the preliminary model to **full signatures**: names, attributes (types, defaults), operations (params, types), **visibility** (public/protected/private), **associations** (with **multiplicity/cardinality**), **inheritance**, and **aggregation/composition**. [1], [3]
3. **Client–object (hierarchical) diagrams** — capture invocation/control structure where useful. [2]
4. **Detailed design spec** — **Interfaces** (constructors/methods with types), **Algorithms** (NL/pseudocode), **Data structures** (class/static/locals; representation choices). This is what programmers code from (often as **skeletal class files** + comments). [3]

**Why this order matters:** class diagrams alone don’t show **call order**; sequence diagrams alone don’t lock **contracts**. You need both. [1]

---

## 4) Class modeling that won’t get you marked down

### 4.1 Noun extraction → preliminary class list

* Parse the **problem statement and use-case scenarios**; list nouns; **filter out**: abstractions (“time” if not first-class), out-of-scope entities, and **attributes masquerading as classes** (e.g., “client name” → attribute of `Client`). [1], [2], [3]

### 4.2 UML class diagram essentials (what graders expect to *see*)

* **Three compartments:** *Name* / *Attributes* / *Operations*.
* **Relations:**

  * **Inheritance** (arrow to superclass).
  * **Association** with **named roles** and **multiplicities** (1, 0..1, 1..*, 0..*).
  * **Aggregation/Composition** for part–whole; reserve for real lifecycles.
  * (Slides also mention a “method-call relation”; keep that semantic in **sequence** diagrams; don’t overload class diagrams.) [1], [3]

### 4.3 Detail level for the midterm

* **Attributes:** names, **types**, **visibility**, and defaults if fixed by policy.
* **Operations:** **signatures** (param names/types, return types), **visibility**.
* **Contracts:** pre/post conditions may be *brief prose* if it locks ambiguous behavior. [1], [3]

**Pitfall:** flipping terminology (“user” vs “client”) across artifacts → **traceability breaks**; marks off. Keep names consistent end-to-end. [1]

---

## 5) Dynamic modeling done right

### 5.1 Sequence (or collaboration) diagrams — make order explicit

* Show **lifelines** (object instances), **messages** (sync/async), **self-calls**, and **alt** fragments for alternate flows (e.g., DB down, invalid password).
* Use them when a use-case leaves call order ambiguous or multiple outcomes exist. [1]
* Collaboration diagrams are **isomorphic** to sequence diagrams; pick one (sequence is usually clearer for ordering). [1], [2]

### 5.2 State transition diagrams (STD) — when history matters

* Use for objects whose behavior **depends on state** (classic example: **Player** with *Stopped/Playing/Paused*; also **Order**: *Placed → Paid → Shipped → Delivered/Cancelled*).
* **Elements:** states (rounded rectangles with **name** and **entry actions**), **transitions** with labels/guards, **initial** (solid dot) and optional **final** state. Include **reflexive** transitions when actions don’t change state (e.g., pressing “Play” while already *Playing*). [1], [3]

**Grader perspective:** If your class has lifecycle-dependent rules, an STD earns points because it prevents contradictory sequences the sequence diagram can’t easily forbid. [1], [3]

---

## 6) Detailed design spec (what devs need on day one)

* **Interfaces:** full method/constructor signatures aligned with class diagrams (names/types/visibility). [3]
* **Algorithms:** NL or pseudocode sufficient to implement (e.g., search strategy, error handling). Avoid “TBD”; choose concrete tactics. [1], [3]
* **Data structures:** chosen representations (arrays vs lists/trees/maps; persistence gateway types). Note **defaults** and **size/precision** constraints where relevant. [1], [3]

**Skeptical check:** If two competent devs could implement **different behaviors** from your spec, it’s **under-specified**. Add sequence/STD or tighten pre/post conditions. [1]

---

## 7) Project testing (design review) before coding: V&V of the design

* **Verification & Validation at design time:**

  * **Verify**: design satisfies **stated requirements** (coverage/traceability).
  * **Validate**: design is **coherent/consistent** (no contradictions; realistic call orders; signatures match). [1]
* **Traceability review:** walk from each **verb/noun** in requirements → **use case** → **class/operation** → **sequence/state** element. Document inconsistencies and fixes in a **review report**. [1], [3]

**Heuristic:** if a requirement verb (“log in”) lacks a **use case**, or the use case lacks a **class operation**, you will bleed time in implementation. Fix it now. [1]

---

## 8) What to memorize vs. what to argue

**Memorize (short list):**

* Definitions of **modularity, cohesion (types), coupling (types)**. [2]
* **Order of OOD workflow** and **what each artifact contributes**. [2], [3]
* **UML basics** (class compartments, association with multiplicities, inheritance symbols; sequence diagram components; STD elements). [3]

**Be ready to argue:**

* **Which diagrams** you choose for a given risk (ambiguous order → sequence; lifecycle rules → STD; data shape uncertainty → ER add-on). [1], [3]
* **Why a design achieves high cohesion/low coupling**, and what you changed to get there. [2]
* **Interface choices** (signatures & data structures) that serve target qualities (performance, security, modifiability). [1], [3]

---

## 9) Common mistakes (and quick fixes)

* **Only class diagrams** → devs guess call order. **Fix:** add sequence diagrams for hot paths. [1]
* **Inconsistent naming** (“User” vs “Client”) across artifacts → broken traceability. **Fix:** global rename + review. [1]
* **Over-using composition/aggregation** without lifecycle meaning. **Fix:** demote to association unless destruction semantics require comp/agg. [3]
* **“We’ll pick a data structure later.”** **Fix:** pick now, justify (e.g., `List` for append-heavy, `Map` for keyed access). [1]

---

## 10) Lab-style drills (10–15 min each)

1. **Login flow (ambiguity on order).**
   Produce a **sequence diagram** for `Browser → AuthController → UserRepo → DB`. Include an **alt** fragment for invalid password; show the **session token** creation point. Then list the **method signatures** you would commit (names/params/returns). [1], [3]

2. **Order lifecycle (stateful object).**
   Draw an **STD** for `Order` with *Placed, Paid, Shipped, Delivered, Cancelled*. Include at least one **guarded** transition (e.g., `Cancel` only if `!Shipped`). Map each transition to a **method** on `Order`. [1], [3]

3. **Cohesion & coupling triage.**
   Given a “Manager” class that logs, validates, queries, and emails: split into **cohesive** classes; define **interfaces** that reduce coupling (e.g., `IEmailGateway`, `IValidator`, `IRepository`). Provide **signatures**. [2], [3]

---

### References (IEEE-style)

[1] **Lecture transcript**: “Lecture05_2025-10-01.merged.txt,” live class notes (need for sequence/collaboration diagrams; detailing class diagrams with types/visibility; cardinality/modality; STDs; V&V/traceability; interfaces/algorithms/data structures), Oct. 1, 2025.
[2] **Slides**: “Lecture05_ООD.pdf,” *Architecture of Software Systems — Lecture 3: Object-Oriented Design* (principles—modularity, cohesion, coupling; AOD/DOD/OOD; architectural design order; interaction diagrams; class modeling; project testing), HSE University, 2021.
[3] **Slides**: “Lecture05_Detailed_ООD.pdf,” *Architecture of Software Systems — Lecture 4: Detailed OO Design* (detailed class diagrams; interaction/state diagrams; detailed design spec—interfaces/algorithms/data structures; project testing and review), HSE University, 2021.

[<kbd><br><- Return (PreMid)<br></kbd>](PreMid.md)
