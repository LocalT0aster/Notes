# L10 — Security Flashcards

**Source:** https://sqrbok.github.io/content/material/sqr/RQ_L10_Security.html

**Study notes:** https://sqrbok.github.io/content/material/sqr/SN_L10_Security.html

**Cards:** 13

> [!tip] Active recall
> Questions are copied verbatim from the pinned SQRBOK source. Answers are locally synthesized self-checks, not official model answers.

### Q1 — Fault, Error, Failure in Security

**Card ID:** l10-security-001

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L10_Security.html#q1-fault-error-failure-in-security

> [!question] Question
> ### Q1: Fault, Error, Failure in Security
>
> A junior developer writes a login query using string concatenation instead of a parameterised query. An attacker submits `alice' --` as the user name and any password.
>
> 1. Trace the **fault → error → failure** chain for this attack. Name each stage precisely and say which CIA properties fail, and why.
> 2. Trace the chain again for a customer named **O'Brien** who simply logs in. What is different about the activation, the error and the failure?
> 3. Both cases share one fault and one fix. Why does the fault count as a **vulnerability**, although O'Brien's failed login on its own is only an accidental reliability failure?

> [!answer]- Answer / self-check
> Shared **fault:** constructing SQL with untrusted string concatenation instead of parameterization. Normal bug: apostrophe produces malformed query (**error/internal invalid command**) → exception/wrong service (**failure**). Attack: adversarial input changes query semantics (**error: unauthorized query state**) → unauthorized access/data change (**security failure**). Security adds an intelligent adversary exploiting the same defect, so likelihood/blast radius differ.

### Q2 — Detecting vs Preventing — The CTO's Dilemma

**Card ID:** l10-security-002

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L10_Security.html#q2-detecting-vs-preventing--the-ctos-dilemma

> [!question] Question
> ### Q2: Detecting vs Preventing — The CTO's Dilemma
>
> A start-up CTO with a 20-person team and a small budget asks: "Should we invest in static analysis tools or in threat modeling first?" You know:
>
> - McGraw's estimate: about half of security problems are implementation **bugs**, about half are design **flaws**.
> - IBM's 2024 survey (figures given here, not in the study notes): an average breach costs **USD 4.88 million** and is found after **194 days**.
> - Avizienis's **four means**: fault prevention, fault tolerance, fault removal, fault forecasting.
>
> (a) Using McGraw's estimate, explain why investing in only one approach leaves roughly half of the problems unaddressed.
>
> (b) If the team deploys daily and can pick only one to start with, which do you recommend? Justify.
>
> (c) Map each of the four means to a concrete security practice. Under which means do static analysis and threat modeling fall?

> [!answer]- Answer / self-check
> Only one leaves a major blind spot: automated code tools mainly find **implementation bugs**, threat modeling finds **design flaws**. A defensible startup-first choice is lightweight threat modeling for auth/data/trust boundaries because design flaws are expensive to retrofit, then automate SAST immediately after; alternatively SAST can be first when code churn and zero automation dominate. Map means: prevention→secure design/training; tolerance→sandboxing/least privilege/fail-safe recovery; removal→SAST/testing/patching; forecasting→risk/threat/vulnerability analysis.

### Q3 — Tool Selection Under Constraints

**Card ID:** l10-security-003

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L10_Security.html#q3-tool-selection-under-constraints

> [!question] Question
> ### Q3: Tool Selection Under Constraints
>
> Your team deploys **5 times per day**. The budget allows **one** tool:
>
> | Tool | Strength | Weakness |
> |------|----------|----------|
> | SAST | Finds bugs early, points to the line | False positives are unavoidable (Rice's theorem) |
> | DAST | Tests the running application, proves exploitability | One job took about 14 minutes in Rangnau et al.'s pipeline; finds only what it reaches |
> | SCA | Finds known vulnerabilities in dependencies | Cannot find bugs in your own code |
>
> 1. For each tool, describe its practical effect on a 5-per-day deployment cycle. Which causes the least friction?
> 2. Practitioners in Rajapakse et al.'s study report that only about **30% of scan results are effective vulnerabilities**. Why is this not the same as a 70% false-positive rate, and how does it change your cost-benefit analysis?
> 3. Make a recommendation. Under what circumstances would you change it?

> [!answer]- Answer / self-check
> - **SAST:** early/custom-code reach but high false-positive triage; usually fits build/PR.
> - **DAST:** realistic runtime findings/low FP but ~14 min cited overhead → ~70 min/day if serial across five deploys; run asynchronously/nightly or on staging.
> - **SCA:** low friction and excellent known-dependency CVEs, but no custom-code/design coverage.
> ~30% effectiveness means no tool is a complete security program. Pick based on dominant exposure and complement it with review/threat modeling.
> **Effective vulnerability ≠ true positive:** a real finding can be irrelevant, duplicate or not worth fixing in that context. Thus 30% actionable/effective results does **not** imply a measured 70% false-positive rate. Include triage cost and reachable risk, not just scan runtime, in the decision.

### Q4 — Code Review and Fuzzing — A Combined Strategy

**Card ID:** l10-security-004

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L10_Security.html#q4-code-review-and-fuzzing--a-combined-strategy

> [!question] Question
> ### Q4: Code Review and Fuzzing — A Combined Strategy
>
> You design the security testing strategy for a **banking application** that processes wire transfers. Yu et al. found that **fewer than 1%** of review comments concern security, but that developers fix **81.3%** of security defects when the reviewer proposes a specific fix.
>
> (a) Which kinds of vulnerability does **code review** catch well, and which does it miss? (Think: logic and concurrency versus input-handling edge cases.)
>
> (b) Which kinds does **fuzzing** catch well, and which does it miss? (Think: crashes and memory errors versus business-logic bypasses.)
>
> (c) Given Yu et al.'s result, how should a reviewer phrase a security comment so that it gets fixed, and where would you aim the fuzzer?
>
> (d) For this bank, which technique matters more against **fraud**, and which against **denial of service**?

> [!answer]- Answer / self-check
> Security-focused review is strong for **business logic, authorization, trust-boundary, crypto/API misuse** but can miss huge input spaces. Fuzzing is strong for **parser/input handling, memory safety, crashes/DoS** but may miss semantic fraud that does not crash. Use security checklists/assigned reviewers and threat-model references; fuzz critical transfer parsers/APIs with coverage guidance/sanitizers and realistic seeds. For fraud, logic review/threat modeling is central; for DoS/input corruption, fuzzing is central.
> The source reports fewer than 1% of review comments concerned security, with **81.3% of raised security defects fixed when a concrete fix was proposed**. Write an actionable comment identifying the unsafe path, consequence and a specific remediation/test rather than “security issue?”. This is study evidence, not a universal fix probability.

### Q5 — Penetration Testing

**Card ID:** l10-security-013

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L10_Security.html#q5-penetration-testing

> [!question] Question
> ### Q5: Penetration Testing
>
> A shop hires an external team for a one-week penetration test of its staging system.
>
> (a) Name the four NIST phases and say what happens in each. In which phase must written approval exist, and why?
>
> (b) The testers log in to an admin panel with its default password. Which phase is this (planning, discovery, attack or reporting), and what does Weidman's **post-exploitation** add to the report?
>
> (c) The final report lists no critical findings. What may the shop conclude, and what may it not? (Hint: what did one week of testing actually sample?)

> [!answer]- Answer / self-check
> **Planning:** scope, rules and written authorization before activity. **Discovery:** collect information and identify possible weaknesses. **Attack:** exploit one, such as logging into admin with the default password, and explore further findings. **Reporting:** document evidence, impact and fixes throughout and at completion. **Post-exploitation** asks what access enables next (data access, lateral movement, persistence) within the agreed scope. No critical findings means none found in that sampled scope/time, not proof of no vulnerabilities.

### Q6 — STRIDE Application

**Card ID:** l10-security-005

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L10_Security.html#q6-stride-application

> [!question] Question
> ### Q6: STRIDE Application
>
> Consider this simplified data flow diagram of an online bank. Rectangles are external entities, ovals processes, the open boxes data stores, and labelled arrows data flows; everything inside the dashed box runs on the bank's servers, and its edge is the trust boundary.
>
> ![Bank DFD: User sends credentials to the Login page process, which passes them to the Auth service process; Auth service writes sessions to the Session store and looks up the Account DB; Admin logs in to the Admin panel process, which updates the Account DB](rq-l10-bank-dfd.svg)
>
> 1. Using **STRIDE-per-element**, identify **six threats**, one per STRIDE category. For each, state the threat, the DFD element it targets (external entity, process, data store or data flow) and one mitigation.
> 2. Check your list against the per-element rule: which letters can apply to the *User* external entity, and which to the *Account DB* data store?
> 3. Scandariato et al. measured a recall of **36%** for STRIDE. What kinds of threat might your six miss, and which complementary techniques would raise recall?

> [!answer]- Answer / self-check
> Example set:
> - **S**poofing: stolen session impersonates user → MFA/session binding.
> - **T**ampering: modify request/account data → integrity checks + authorization.
> - **R**epudiation: admin denies transfer → tamper-evident audit log.
> - **I**nformation disclosure: session/account data leak → encryption + access control.
> - **D**oS: flood Auth Service → rate limits/circuit breakers/capacity controls.
> - **E**levation: normal user reaches Admin Panel → deny-by-default RBAC.
> STRIDE recall is incomplete; add insider, side-channel, and supply-chain analysis.
> Per-element targets: **User external entity: S/R; Account DB store: T/I/D** (R when used as a log); processes can receive all six, flows T/I/D. Put spoofing on the element whose identity is faked, e.g. User; tampering/disclosure on the affected flow or store; repudiation on an accountable actor/log; DoS/elevation on the relevant process. The study's **36% recall** is not a guarantee that six examples cover the design: add abuse cases, attack trees, expert review and focused testing.

### Q7 — Method Selection for a Healthcare Portal

**Card ID:** l10-security-006

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L10_Security.html#q7-method-selection-for-a-healthcare-portal

> [!question] Question
> ### Q7: Method Selection for a Healthcare Portal
>
> A healthcare start-up builds a **patient portal** that must comply with data-protection law. It has three developers, no security team and six months to launch.
>
> | Method | Focus | Effort |
> |--------|-------|--------|
> | STRIDE | Security threats per DFD element | Medium |
> | PASTA | Risk-centred, seven stages, attack simulation | High |
> | LINDDUN | Privacy threats such as linkability and identifiability | Medium |
>
> (a) Why is STRIDE alone not enough here? Which threats does LINDDUN prompt for that STRIDE does not?
>
> (b) Propose a pragmatic combination and justify it.
>
> (c) Yskout et al. place threat modeling as a field at **level 1, ad hoc**, with about **69 hours** per project. What does this tell the start-up about the effort to plan and about what tools and guidance to expect?

> [!answer]- Answer / self-check
> STRIDE focuses technical security properties; GDPR also demands privacy threats such as **linkability, identifiability, detectability, disclosure, unawareness, non-compliance** (LINDDUN). A small team can build one DFD, run STRIDE on trust boundaries, then a focused LINDDUN pass on personal/health data and data lifecycle. Start at lightweight repeatable maturity (trained facilitator + checklist) and evolve toward threat models in design reviews and release cadence.
> LINDDUN also includes **non-repudiation as a privacy threat** (loss of plausible deniability). The reported field maturity **level 1/ad hoc** and roughly **69 hours/project** warn that facilitation, scope and iteration need planned effort; they do not prescribe a fixed 69-hour budget for this startup. Avoid an elaborate PASTA program the three-person team cannot sustain.

### Q8 — CVSS Analysis — Prioritising Patches

**Card ID:** l10-security-011

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L10_Security.html#q8-cvss-analysis--prioritising-patches

> [!question] Question
> ### Q8: CVSS Analysis — Prioritising Patches
>
> A published CVE in the web framework you use has:
>
> - **Base score 8.1 (High):** `AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H`
> - **Temporal metrics:** proof-of-concept exploit code exists (E:P), a temporary fix is available (RL:T), the report is confirmed (RC:C)
> - **Environmental metrics:** the component handles only public data and sits behind a rate-limiting proxy, so the organisation sets CR:L, IR:L and AR:L and leaves the base metrics unmodified
>
> (a) Using the weights in the study notes, compute the temporal score. Show the rounding.
>
> (b) Compute the environmental score: MISS, Modified Impact, the rounded sum with Exploitability (compute it yourself from the base vector), and the final rounding after applying the temporal weights.
>
> (c) Explain what each metric group tells you and why the score falls from 8.1 through the temporal value to the environmental value.
>
> (d) Patch immediately, or schedule for the next sprint? Justify.
>
> (e) Log4Shell scored 10.0 with `AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H`. Identify the **two base metrics** that differ from the vector above and explain what each means. Then, starting from this S:C base score of 10.0, state Log4Shell's exploit code maturity (E), remediation level (RL) and report confidence (RC) at CVE publication, using the study notes, compute its temporal score, and explain how these changed the urgency.

> [!answer]- Answer / self-check
> **Base** describes intrinsic severity; **temporal** adjusts exploit maturity/fix/report confidence; **environmental** adjusts local requirements and modified metrics. Round **up** to one decimal, not to nearest.
> - Temporal = roundup(8.1×0.94×0.96×1) = **7.4**.
> - MISS = 1−(1−0.5×0.56)³ = **0.626752** (below the 0.915 cap).
> - Modified impact = 6.42×MISS = **4.023748**.
> - Exploitability = 8.22×0.85×0.44×0.85×0.85 = **2.221167**.
> - Inner roundup of impact+exploitability = roundup(6.244915) = **6.3**.
> - Environmental = roundup(6.3×0.94×0.96) = **5.7**.
> The rate-limiting proxy does not itself alter weights here; low CR/IR/AR are given assumptions. Confirm them rather than assuming public data makes integrity/availability unimportant. CVSS is severity, not a complete risk estimate; schedule versus emergency depends on exposure, exploitation and business impact.
> Log4Shell differs at **AC:L** and **S:C**. Given its published base 10.0, E:H=1, RL:O=0.95 (2.15.0 fix available), RC:C=1 at publication: temporal **9.5**. Easy exploitation and wide reach justify urgent action; later fixes and knowledge evolved.

### Q9 — Principle Mapping — A Judgement

**Card ID:** l10-security-007

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L10_Security.html#q9-principle-mapping--a-judgement

> [!question] Question
> ### Q9: Principle Mapping — A Judgement
>
> For each incident, name the one principle (where the study notes give two or more readings, as for Heartbleed, any of them is accepted with reasons) you think was most directly violated, using the eight Saltzer and Schroeder principles or, where none fits, an SD3 commitment (study notes §7). "Validate all input" is a practice, not one of the eight:
>
> | Incident | Year | Your reading |
> |----------|------|--------------|
> | Heartbleed | 2014 | ? |
> | Equifax | 2017 | ? |
> | WannaCry | 2017 | ? |
> | Log4Shell | 2021 | ? (hint: was the risky lookup feature on or off by default?) |
> | SolarWinds | 2020 | ? (hint: who could change the build, and what checked them?) |
> | Target | 2013 | ? (hint: what could a contractor's account reach?) |
>
> Then, for **two** incidents of your choice:
>
> (a) Describe the technical fault.
>
> (b) State your principle, its definition, and why it fits.
>
> (c) Give a second defensible reading and argue which one you prefer.

> [!answer]- Answer / self-check
> Mappings are not unique—justify causally. Reasonable examples: **Target → least privilege / separation of privilege** (vendor access should not reach payment network); **Equifax → complete mediation / secure maintenance** (vulnerable internet-facing component remained exploitable); **Heartbleed → fail-safe defaults/economy of mechanism** (unchecked length exposed memory); **SolarWinds → least common mechanism / trusted build-chain controls**; **WannaCry → least privilege + fail-safe network segmentation**; **Log4Shell → economy of mechanism / minimize ambient dangerous capability**. State the principle definition and how design would reduce blast radius.
> Distinguish the eight principles from **SD3** (secure by design, by default, in deployment). For the source's direct readings: Equifax/WannaCry → **secure in deployment** (unpatched services); Log4Shell → **secure by default** (dangerous lookup enabled); SolarWinds → **separation of privilege** (independent build/change approval); Target → **least privilege**. Heartbleed supports economy of mechanism or secure-by-default, with reasons. Do not relabel generic “patching” as complete mediation without explaining the missing access check.

### Q10 — Input Validation — "All Input Is Evil"

**Card ID:** l10-security-008

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L10_Security.html#q10-input-validation--all-input-is-evil

> [!question] Question
> ### Q10: Input Validation — "All Input Is Evil"
>
> A REST endpoint accepts:
>
> ```json
> {
>   "user_name": "Alice",
>   "email": "alice@example.com",
>   "age": 25
> }
> ```
>
> 1. Design an **allowlist** validation for each field: allowed characters, length limits, format and type checks.
> 2. A colleague proposes a **blocklist** of `<`, `>`, `'` and `"`. Give a concrete input that defeats it.
> 3. *Canonicalising* means decoding input into one standard form before checking it: a filter that blocks apostrophes passes the attack payload `%27 OR 1=1 --`, whose `%27` is decoded into `'` afterwards. Why must validation run after decoding, and give one more example of an encoding that could slip past?
> 4. What is an **input chokepoint**, and why does validating in one place reduce risk?

> [!answer]- Answer / self-check
> Allowlist by **type, canonical form, length, character set, and semantic range**: e.g. name normalized Unicode + bounded length; email parsed/canonicalized with bounded lengths; age integer within business range. Denylists miss encodings/Unicode/alternate syntax. **Canonicalize then validate**. An input chokepoint centralizes validation at a small trusted boundary so every downstream path receives normalized validated data and policy is not duplicated.
> Example policy: name 1–80 permitted normalized characters; email parsed with a 254-character limit; age an integer (not a Boolean/string) in 0–130. Blocking only quotes/brackets still accepts invalid **age −100**, and a filter-before-decode can miss `%27 OR 1=1 --` or double-encoded `%2527`. Decode according to one consistent boundary contract, validate the resulting form, and still use parameterized SQL; validation is not a substitute for safe query construction.

### Q11 — Pipeline Design

**Card ID:** l10-security-009

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L10_Security.html#q11-pipeline-design

> [!question] Question
> ### Q11: Pipeline Design
>
> You are the DevSecOps engineer for 12 microservices built with GitHub Actions and deployed to Kubernetes. Fill in which checks run at each stage and stay within the time budget:
>
> | Stage | Checks | Time budget |
> |-------|--------|-------------|
> | IDE | ? | Instant |
> | Pre-commit | ? | < 30 s |
> | Build | ? | < 5 min |
> | Test | ? | < 15 min |
> | Deploy | ? | < 2 min |
> | Operate | ? | Continuous |
>
> (a) Where does DAST go, given that one job took 14 minutes 6 seconds in Rangnau et al.'s pipeline, and how do you keep it from blocking deployments?
>
> (b) Your Bandit gate uses `-ll` (a Bandit severity threshold). Which findings does it let through, and what do you add to cover them?
>
> (c) Why can't all security testing move left into the IDE?

> [!answer]- Answer / self-check
> Example: IDE—lint/secret/SAST hints; pre-commit—secrets, formatting, fast SAST; CI build—SCA/SBOM, SAST, IaC/container scan; CI test—security unit/integration + fuzz subsets; staging/CD—DAST and policy/admission checks (long DAST async if ~14 min); production—runtime detection, WAF, dependency/vuln monitoring. Triage by severity/exploitability/ownership and baseline known false positives. Not all checks shift left because some require a running integrated system/real environment.
> Fit measured budgets: IDE instant; pre-commit <30 s; build <5 min; test <15 min (the cited DAST job was **14 min 6 s**, best parallel/asynchronous); deploy <2 min; operate continuously. **Bandit `-ll` is a severity filter**, retaining medium/high regardless of confidence and letting low-severity findings through. Add a secrets scanner and appropriate review for low-severity hardcoded credentials.

### Q12 — Supply Chain and Remediation Plan

**Card ID:** l10-security-010

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L10_Security.html#q12-supply-chain-and-remediation-plan

> [!question] Question
> ### Q12: Supply Chain and Remediation Plan
>
> You are the security architect of a fintech company that processes about USD 2 million a day. A penetration test reports:
>
> 1. **SQL injection** in the payment API, CVSS 9.8 (`AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`): three endpoints build queries from strings, and the database accepts several statements per call, so an attacker can also delete tables. Compare this vector with the shop example, scored 9.1 in §6 of the study notes: why A:H here and A:N there?
> 2. A **Log4j 2.14.1** dependency in the logging service, with a public exploit for Log4Shell.
> 3. **No threat model** for authentication and authorization.
>
> (a) **This week:** which finding do you fix first and why (CVSS, exploit availability, blast radius, how much of the system an exploit can reach)? Until the code fix ships, how would you reduce who can reach the vulnerable endpoint?
>
> (b) **This quarter:** which pipeline checks would have caught findings 1 and 2 automatically? Which supply chain vector does finding 2 belong to, and how would an SBOM have helped?
>
> (c) **This year:** choose a threat modeling method and say where in the delivery cycle it runs (study notes §5 and §8) and add one control for each of the other two supply chain vectors, using SolarWinds and XZ Utils as examples.

> [!answer]- Answer / self-check
> - **Log4Shell:** vulnerable dependency capability reachable via attacker-controlled strings → patch/upgrade, SCA, egress/JNDI hardening; SBOM helps locate affected versions.
> - **SolarWinds:** build/update pipeline compromise shipped trusted malicious artifacts → hardened isolated builds, signing/provenance/reproducibility; SBOM alone may still list legitimate components and miss a compromised build process.
> - **XZ:** social-engineering/maintainer-trust attack inserted a backdoor into release artifacts/build path → maintainer governance, review, provenance, reproducible builds; SBOM helps inventory but not human intent.
>
> **Immediate:** patch/mitigate internet-exposed known RCE Log4j and SQLi in parallel; if forced to order, prioritize the finding with active exploitability + greatest reachable blast radius. Disable vulnerable features/WAF rules/network egress as temporary controls; parameterize queries and add regression tests. **Quarter:** SCA/SBOM, SAST, secret scanning, fuzz/security tests, security-review checklist/ownership. **Year:** recurring STRIDE + privacy/risk modeling, supply-chain provenance/reproducible builds, secure design training, metrics and incident feedback. Missing threat model is a program gap: start now, mature continuously.
> The fintech SQLi has **A:H** because multiple SQL statements can delete tables and stop service; the shop example's A:N assumed only the attacker's query failed. Restrict network access to exposed endpoints until fixed. SAST/exploit regression tests address SQL construction, SCA/SBOM identifies the vulnerable Log4j version; neither substitutes for an auth design threat model. Include independent maintainer review for the human vector and isolated, verifiable build provenance for infrastructure compromise.

### Q13 — Security Requirements

**Card ID:** l10-security-014

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L10_Security.html#q13-security-requirements

> [!question] Question
> ### Q13: Security Requirements
>
> A university builds an online exam system. Students log in, see their exam during a fixed window, and submit answers; teachers grade.
>
> SQUARE's nine steps are: (1) agree on definitions; (2) identify security goals; (3) develop artefacts such as architecture diagrams, use and misuse cases, and attack trees; (4) assess risks; (5) select an elicitation technique; (6) elicit the security requirements; (7) categorise them; (8) prioritise them; (9) inspect them. A **misuse case** describes, next to a normal use case, how an attacker would abuse the same function.
>
> (a) Walk through steps 2 to 4 for the submission feature: name two assets and goals, write one misuse case, and state the risk you would rank highest.
>
> (b) Turn that misuse case into one testable security requirement, and describe the automated test that would check it on every build.
>
> (c) **RQCODE** expresses requirements as code with `check()` and `enforce()`. Which kinds of requirement does this suit well, and why would your requirement from (b) be harder to express that way?

> [!answer]- Answer / self-check
> **Goals/assets:** protect answer confidentiality and submission/grade integrity. **Artefacts/misuse case:** DFD plus a student changing another student's stored answer by substituting its submission ID. **Risk:** unauthorized answer modification has high integrity impact; rank likelihood/exposure explicitly.
> **Requirement:** on every submission-update request, the service shall authorize the authenticated owner and the server-side exam window before any write; unauthorized or late attempts shall be rejected without changing data. Test in CI with two accounts, swapped IDs and before/at/after deadline cases; assert both denial and unchanged stored answers, plus a valid positive case.
> SQUARE's full sequence: definitions → goals → artefacts → risks → elicitation technique → requirements → categorization → prioritization → inspection. **RQCODE** suits checkable/enforceable configuration such as a security setting; this stateful authorization/time behavior needs application context and integration tests, rather than only inspecting/remediating a setting.
