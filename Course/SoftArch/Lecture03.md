# Lecture 3 — Software Architectures (pre-midterm rehearsal)

> Sources this week: the live lecture transcript [1] and the **Software Architectures** slide deck [2]. No separate lab slides were provided; I’ve added short “lab-style drills” so you can rehearse anyway.

---

## 1) Client–Server foundations you must be fluent in

### 1.1 Open systems (why client–server scaled in the first place)

* **Core idea:** standardize interfaces so apps are *portable* and *interoperable*. This enabled cheap shared access to DBs over LAN and component “mix-and-match” without vendor lock-in. [2]
* **Exam verbs:** define *portability* vs *interoperability*; explain how “open systems” reduced coupling across OS/hardware. [2]

### 1.2 Roles and specializations (clients, servers, and their many hats)

* **Client =** requests services; **Server =** provides them. Typical servers: **telecom**, **compute**, **disk/file**, **DB**, etc. You’ll see these recur as you map quality attributes to components (e.g., add a **cache** or **encryption** server when latency or security is a driver). [2], [1]

### 1.3 File-server vs Database-server data processing

* **File-server:** ships whole files/blocks across the network; the client does heavy lifting.
* **DB-server (client–server DBMS):** pushes integrity constraints and query execution to the server; GUI and app code at the client; SQL is the standard interface. *Pro:* security, centralized admin; *Con:* server can become a bottleneck. [2]

### 1.4 RPC & hiding heterogeneity

* **Remote Procedure Call (RPC)** makes “ask the server” look like “call a function,” hiding byte ordering, address formats, protocol quirks. Consequence: you can **rebalance logic** (client ↔ server) without rewriting everything. [2]

---

## 2) Where to put the logic: PL/BL/AL and the three canonical splits

> Think in **three slices**: **Presentation (PL)**, **Business (BL)**, **Access (AL)**. Your exam answers should always make this explicit. [2]

* **“Rich/Thick client (RDA/Remote Data Access):** PL+BL on client, AL on server.

  * **Use when:** rich offline UX; compute at the edge; few clients.
  * **Trade-offs:** faster UI, but **change management pain** (update many clients). [2]

* **Thin client:** PL on client; BL+AL on server (often via stored procedures).

  * **Use when:** centralized governance, security & integrity dominate; browsers.
  * **Trade-offs:** **server load spikes**; you must scale vertically/horizontally. [2]

* **Application-Server (3-tier):** BL in a **separate middle tier**.

  * **Use when:** many clients, evolving business rules, need to offload DB.
  * **Trade-offs:** more moving parts, but **flexible BL** and better DB throughput. [2]

**DB-server internals you should name:**

* **Multiprocess** model (e.g., Oracle): one process per connection; simple isolation, higher memory.
* **Multithreaded** model (e.g., MS SQL Server, Sybase): one process, many threads; lower overhead, careful scheduling. [2]

**Lab-style drill (10′):** Given “call-center CRM with 1k agents + heavy reporting,” choose **3-tier**: browser PL, app-server BL (validation, workflows), DB AL (constraints; reporting offloaded to read replicas). Defend against **server bottleneck** by explaining horizontal scale at BL and read scaling at AL. Cite the PL/BL/AL placements explicitly. [2]

---

## 3) Web (Internet/Intranet) architectures: request flows & server-side extensions

### 3.1 Two-tier vs three-tier on the Web

* **Two-tier:** browser ↔ web server serving HTML.
* **Three-tier:** browser ↔ web server (+extensions) ↔ DB server. **Why it won:** less network traffic, component interchangeability, improved security. **Caveat:** HTTP statelessness complicates DB transactions—your design must plan sessions/transactions explicitly. [2]

### 3.2 What exactly happens (know the order)

1. Browser requests a page → 2) Web server handles static, forwards dynamic to an **extension** →
2. Extension transforms request → DB server → 4) DB returns result → 5) Extension renders response →
3. Web server returns to browser. [2]

### 3.3 Server-side extensions (enumerate!)

* **Regular CGI**, **Hybrid CGI**, **API-style extensions**. Rationale: reduce connect overhead, keep DB connections warm, and decouple web/DB vendors via **standard interfaces**. [2]

**Lab-style drill (8′):** Draw the 3-tier sequence above and annotate where **input validation** happens (BL), where **authorization** checks live (BL/edge), and where **referential integrity** sits (AL). [2]

---

## 4) Beyond single DBs: distributed, federated, integrated, and multi-DB

* **Integrated DB:** build a **global schema** over heterogeneous sources; transform global operations into local DBMS languages; central admin.
* **Federated DB:** similar goal but keeps stronger autonomy per site; heavy **global transaction management** + **network query optimization** concerns.
* **Multi-database:** preserves **local autonomy**; looser coupling, special access types; **no single global schema**.
* **Reality check:** these are powerful, but **efficiency is hard**—be ready to discuss trade-offs (latency, optimizer limits, failure modes). [2]

**Lab-style drill (12′):** For “national e-gov + regional DBs,” propose **federation** with a **lightweight global schema** for citizen identity objects; list two risks (global deadlocks, inconsistent statistics) and one mitigation (bounded, asynchronous ETL for reporting). [2]

---

## 5) Grid systems (what they are and when *not* to use them)

* **Definition:** a **global distributed compute fabric** (thousands→millions of PCs on fiber networks) rivaling supercomputers by parallelizing problems and aggregating results. Used in **CERN**, bio/medicine imaging, geophysics, etc. [2]
* **Why grids emerged:** supercomputers are expensive and scale poorly; many scientific/analytics tasks are **embarrassingly parallel**. [2]
* **Numbers to quote:** information flow on the order of **~100 MB/s sustained for ~10 years** in exemplar projects. [2]
* **Constraints:** requires **very fast backbones**, partitionable tasks, and careful **result aggregation**; otherwise it *underperforms*. [1], [2]

**Lab-style drill (7′):** Given “password brute force” vs “OLTP banking,” justify why grids fit the former (parallelizable keyspace) and are wrong for the latter (strong ACID, low-latency coordination). [1]

---

## 6) Making architecture useful (not just pretty diagrams)

> The transcript spends time showing **bad architecture pictures** and *why they fail*. Use these to guide your own artifacts. [1]

* **Always provide a legend and prose.** Readers must know what a **box** (component) and **arrow** (control? data? sync/async?) mean. Without this, diagrams are **non-actionable**. [1]
* **Show both static and dynamic views.** Static “components & connectors” ≠ runtime message flows; pair diagrams with a sequence/activity view where it matters. [1]
* **Avoid “architecture astronautics.”** Stay connected to **business goals** and **quality attributes** (availability, performance, security, modifiability, usability, portability). [1]
* **Trade-offs are real.** E.g., **security vs performance** (more locks on the “door” slow access). You must **prioritize** qualities and **justify** sacrifices. [1]
* **Refactoring is not a silver bullet.** If partitioning is wrong (client/server split, missing middle tier, no load balancer), “refactor later” may mean **redesign from scratch**. [1]
* **Methodologies help, but won’t say when architecture is “done.”** Use **drivers** (top quality goals) to decide when the architecture is *stable enough* for construction. [1]

**Exam pattern to practice:**

1. **Drivers:** list top 3 system qualities (ranked).
2. **Partitioning:** where do PL/BL/AL live; any specialized servers (cache, auth)?
3. **Mechanisms:** RPC? async messaging? server-side extension type?
4. **Consequences:** what gets better/worse; fallback options if demand doubles. [1], [2]

---

## 7) Architectures you can *name and sketch* in <60 seconds

* **2-tier vs 3-tier client–server** with PL/BL/AL placements. [2]
* **Thick vs thin client** (what moves when BL moves). [2]
* **DB server models:** multi-process vs multi-threaded (plus examples). [2]
* **Web three-tier flow** (six steps). [2]
* **Integrated / Federated / Multi-DB** (one-line definitions and their pain points). [2]
* **Grid** vs **Supercomputer** (parallelism vs monolith; cost & scalability). [2]

---

## 8) Quick-fire rehearsal prompts (write 4–6 line answers)

1. **Why did open systems matter for DB-backed apps on LANs?** Include portability/interoperability and SQL as a de-facto standard. [2]
2. **Pick thick or thin for a medical imaging viewer at hospitals.** Defend against bandwidth limits and privacy constraints; say where BL sits. [2]
3. **Explain RPC to a junior.** Show how it hides heterogeneity and enables rebalance of logic. [2]
4. **When would you *not* choose a federated DB?** Talk about global transactions and optimizer complexity. [2]
5. **Show a concrete security↔performance trade-off** you would bake into your design (e.g., token revalidation interval, encryption at rest with CPU cost). [1]

---

## 9) Common pitfalls (don’t do these in the midterm)

* Diagrams with **no legend** or **ambiguous arrows**. [1]
* Choosing thin client without **capacity planning** for the server tier. [2]
* Shipping a CGI-only stack that **reconnects per request** under load. [2]
* Declaring “we’ll grid it” when the problem is **not** parallelizable. [2]
* Promising “we’ll refactor into 3-tier later” when the data model and session handling are already baked into a thick client. [1]

---

### References (IEEE-style)

[1] **Lecture transcript**: “Lecture03_2025-09-17.txt,” live class notes (client/thin/thick/app-server; grid; quality attributes; diagram pitfalls; architecture vs business alignment), Sept. 17, 2025.
[2] **Slides**: “Lecture03_SoftwareArchitectures.pdf,” *Architecture of Software Systems — Lecture 5: Software Architectures* (open systems; client–server DBMS; RPC; PL/BL/AL; 2-tier/3-tier web flows; server-side extensions; DB server models; integrated/federated/multi-DB; grid systems), HSE University, 2021.

[<kbd><br><- Return (PreMid)<br></kbd>](PreMid.md)
