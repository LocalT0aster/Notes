# Lecture 4 — .NET Platform & Object-Oriented Analysis (OOA)

*Pre-midterm rehearsal digest with exam-ready depth*

> Sources this week: the live lecture transcript [1], **.NET** slide deck [2], and **OOA** slide deck [3]. I call out what to memorize vs. what to be able to argue, plus short lab-style drills so you can rehearse without extra materials.

---

## 0) What this week is actually about (so you study the right things)

* Part A: **Microsoft .NET as an architecture platform**—how its **components, connectors, and layers** implement the ideas from earlier architecture lectures: **assemblies, CLR/JIT, CLS/CTS, BCL, ADO.NET, ASP.NET, Windows/Web Forms, Web services**, and **component programming**. Expect “**place this quality attribute—where in .NET?**” style questions. [1], [2]
* Part B: **OOA (Object-Oriented Analysis)**—how to go from requirements to **use-case diagrams & scenarios → class diagrams (noun extraction & filtering) → dynamic models (state & sequence)**. Expect “**given a brief, sketch the minimal correct set of diagrams and explain why**.” [1], [3]

---

## 1) .NET in four lenses you must name and contrast

**Vision.** Easier deployment in a global/Internet context; emphasis on **software as a service**, better **interoperability**, **security**, and **usability**. Architectural theme: standard interfaces + component reuse. [1], [2]

**Computational model.** **Component approach** over an OO base; **unified type system** (“everything is an object” in practice) with data + metadata; hierarchical namespaces and assemblies. [2]

**Technological platform.** **Multi-language** (many languages compile to the same intermediate form), **Web-service technologies** for interoperability, unified APIs, alignment with modern standards. [2]

**Toolkit.** **CLR (virtual machine) + compilers → MSIL → JIT → native** with **the same class libraries and services across languages**; Visual Studio as the integrating IDE. [1], [2]

**Exam cue:** If a prompt says “explain .NET as *vision vs model vs platform vs toolkit*,” hit one bullet from each of the four boxes above.

---

## 2) The CLR pipeline & why architects care

* **Compilation:** `C# / VB / C++ / F# / … → compiler → assembly (DLL/EXE) with metadata → CLR JIT → native`. Assemblies are **self-describing** (types, versioning, dependencies). [1], [2]
* **Execution domains:** **Managed code** (with runtime services) vs **unmanaged code** (e.g., unsafe pointer blocks), plus **code-access/role-based security** knobs. [1], [2]
* **CLS/CTS:** Common Language Specification/Type System = **type & behavior contract** enabling **inter-language composition** (e.g., VB handles exceptions from C#). Architectural payoff: choose language per concern without sacrificing integration. [2]

**What to memorize:** the compile→MSIL→JIT chain; what an **assembly** is (and why metadata matters). [2]

---

## 3) The .NET stack as a layered architecture (map qualities to layers)

From bottom to top (architect’s view) [1], [2]:

1. **OS services** (Windows family emphasized in slides).
2. **CLR services** (GC, type system, security, threading, JIT).
3. **Base Class Library (BCL)** (collections, I/O, crypto, threading, globalization…).
4. **Data & XML** (**ADO.NET**, XML APIs).
5. **UI & Web** (**Windows Forms**, **ASP.NET**: Web Forms, Web Services).
6. **Your components** (assemblies) written in multiple languages, normalized by **CLS**.

**Where qualities live:**

* **Security:** CLR enforcement + BCL crypto + ASP.NET pipeline.
* **Performance:** JIT + efficient BCL + caching in ASP.NET + data access patterns in ADO.NET.
* **Modifiability:** **Assemblies + versioning + interfaces**; swap components with stable contracts.
* **Interoperability:** Web-service stack (**HTTP/XML/SOAP/UDDI/WSDL** per slides) + language neutrality. [2]

**Exam trap:** Saying “.NET is only C#.” Correct stance: **multi-language to the same runtime & libraries**. [1], [2]

---

## 4) Web & distributed: how .NET renders client–server decisions concrete

* **Types of Internet apps:**

  * **Web applications** (ASP.NET, browser client).
  * **Distributed apps** using **XML Web Services** (standards-first) or **.NET Remoting** (MS-specific). [2]
* **Why this matters for architectures:** lets you **place PL/BL/AL** cleanly (Presentation in Web/Win Forms, Business in service layer, Access via ADO.NET), matching the **2-tier/3-tier** patterns from Week 3. [1], [2]

**Drill (5′):** Given “call-center CRM with 1000 agents,” place **PL=browser, BL=ASP.NET services, AL=ADO.NET/DB**. State 1 concrete **security** control (e.g., token lifetime) and 1 **performance** tactic (e.g., output caching), and name the stack layer where each lives. [2]

---

## 5) Component programming in .NET (contrast with OO)

* **Component** = **deployable, replaceable unit** (bigger than a class; can contain many classes; versioned; language-agnostic; used across boundaries). [2]
* **COM/ActiveX** vs **Java Beans** (slides’ historical contrast): both component models; COM is language-neutral with binary contracts; Beans are Java-centric. .NET subsumes this with **assemblies + metadata + CLS**. [2]

**Pitfalls/limits called out in slides:** higher resource needs; uneven maturity of certain language toolchains; Windows-centric ecosystem (mitigations exist, but treat as a design constraint). [2], [1]

---

## 6) OOA overview—what artifacts you must produce (and in which order)

The **requirements spec is a contract**. Free-text is accessible but **ambiguous**; combine NL with **semi-formal notations**. [3]

**Structural analysis recap (pre-OO tools)** you may still need:

* **DFD** (levels 0/1… for data flows), **process logic** (decision trees; control-flow diagrams), **data dictionaries**, **I/O specs** (valid & invalid inputs, expected outputs). [3]

**OOA proper = three strands** (slides’ framing) [3]:

1. **Use-case modeling** (roles, system boundary, UML use-case diagram, **NL scenarios** including abnormal paths).
2. **Class modeling** (**noun extraction → filter → class (object) diagram** with attributes/methods/relations).
3. **Dynamic modeling** (**state diagrams** for object lifecycles; **sequence diagrams** for interactions).

**Exam cue:** if a question says “walk from requirements to design,” your ordered answer is **use-cases → classes → dynamics** (with structural tools as supportive checks). [3]

---

## 7) Use-case modeling (what “complete enough” looks like)

* **Actors (roles)**: users (novice/expert), admins, **external systems** (DB, remote services), integrators/maintainers. [3]
* **Diagram**: named **actors** (stick figures) outside a **system boundary** (rectangle), **use-cases** (ovals) inside; connect actors to use-cases; optional **<<uses>> / <<extends>>** relations. [3]
* **Scenarios** (the real meat): write **concise NL** with **main flow** and **extensions**, plus **pre-/post-conditions**. Slides’ example shows a catalog browsing case with DB failures handled explicitly. [1], [3]

**What graders look for:** coverage of **abnormal events**; clear linkage from **roles → actions**; **consistent naming**. Missing abnormal flows = red flag. [3]

---

## 8) Class modeling—turn text into structure (without overfitting)

* **Noun extraction:** list all nouns from the requirements/use-case text. [1], [3]
* **Filter** out: (1) **too abstract** (e.g., “time” if not first-class), (2) **out of scope**, (3) **attributes disguised as nouns** (“client name” → attribute of `Client`). [1], [3]
* **Class diagram (UML):** 3 compartments = **name / attributes / methods**; show **associations** (with multiplicities), and **inheritance** (arrow from subclass to superclass). Start coarse; refine later in design. [3]
* **Object diagram:** early stage may show **classes & relationships only**; detailed attributes/methods often finalize in design. [3]

**Drill (10′):** From a “login + browse catalog + view product” brief, propose classes (`User`, `Session`, `Product`, `Catalog`, `DBGateway`), mark one association each with multiplicity, and justify **why `product name` is an attribute but `Product` is a class**. [3]

---

## 9) Dynamic modeling—when states and messages matter

* **State diagrams (STD):** finite-state view per class: `Stopped/Playing/Paused`-style examples appear in slides; transitions are **<state> & <event> & <guard> ⇒ <new state>**. Use these when object behavior depends on history. [3]
* **Sequence diagrams:** show **lifelines** and **messages** (e.g., **login** then **SQL query** through a service to DB). Use these to verify that your **use-case flow** is realistic under your **architecture choice** (e.g., 3-tier). [3]

**Drill (8′):** Draw a minimal sequence for *Login*: `Browser → AuthController → UserRepo → DB`, include an **alt** fragment for **invalid password**, and note at which point you set a **session token** (architecture tie-in). [3]

---

## 10) Putting it together—architecture ↔ process ↔ artifacts

* **Traceability chain you should demonstrate on the midterm:**
  **Requirement → Use-case (incl. failures) → Classes (filtered nouns) → Dynamics (state/sequence) → Placement on .NET layers (PL/BL/AL)**.
* **Right-weighting:** don’t drown in diagrams; pick the **minimum set that kills risk** (unclear roles? do use-cases; lifecycle heavy? add STDs). [1], [3]

---

## 11) Common mistakes (high-yield to avoid)

* **.NET**: treating it as “just C# and WinForms”; ignoring **assemblies/metadata/versioning**; hand-waving where a quality attribute lives (security/perf belong to **specific** layers). [1], [2]
* **OOA**: skipping **abnormal flows** in scenarios; turning every noun into a class; drawing UML without **multiplicities** or **system boundary**; mixing **design detail** prematurely into analysis. [3]

---

## 12) Memorize vs. Argue

**Memorize (flash-card level):**

* **CLR pipeline** (source → MSIL/assembly → JIT → native); **what an assembly is**; **CLS/CTS purpose**; names of **ADO.NET / ASP.NET / BCL / Windows Forms**. [2]
* **Use-case diagram elements**, scenario structure (main + extensions + pre/post); **filtering rules** for noun extraction; what **STD** and **sequence** capture. [3]

**Be ready to argue:**

* Given a brief, **place PL/BL/AL** on the .NET stack and tie **one quality** to a **layered mechanism** (e.g., cache, token validation). [1], [2]
* Justify your **diagram set**: “I chose use-cases + sequence because the risk is interaction flow, not state explosion,” etc. [3]

---

## 13) One-page practice set (for a 30-min self-rehearsal)

1. **Explain .NET as vision/model/platform/toolkit** in ≤6 sentences, mapping one **quality attribute** to a **specific layer**. [1], [2]
2. **Draw a use-case** for “Guest checkout” with one **extension** path for “payment fails,” and write a 6–8 line scenario. [3]
3. **Noun-extract** that scenario; filter to 5–7 classes; sketch a class diagram with at least two multiplicities. [3]
4. **Sequence** the successful path; note which call crosses **BL↔AL** and how you’d implement it in **ADO.NET**. [2], [3]

---

### References (IEEE-style)

- [1] **Lecture transcript**: “Lecture04_2025-09-24.merged.txt,” live class notes (.NET overview; CLR/assemblies; service orientation; OOA workflow from use-cases to classes to dynamics), Sept. 24, 2025.
- [2] **Slides**: “Lecture04_.NET.pdf,” *Software Architectures — Introduction to Microsoft .NET* (vision/model/platform/toolkit; CLR/CLS/CTS; assemblies & metadata; BCL/ADO.NET/ASP.NET; Windows/Web Forms; Web services; component programming; pros/cons), HSE University.
- [3] **Slides**: “Lecture04_OOA.pdf,” *Architecture of Software Systems — OO Analysis & Requirements Specification* (DFD/logic/data dictionaries/I-O specs; OOA vs structural; use-case modeling—roles, diagrams, scenarios; class modeling—noun extraction & filtering; dynamic modeling—state & sequence; lab: build DFD/STD/ER), HSE University.

[<kbd><br><- Return (PreMid)<br></kbd>](PreMid.md)
