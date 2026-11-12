# L10 — Security Flashcards

**Source:** https://sqrbok.github.io/content/material/sqr/RQ_L10_Security.html

**Cards:** 14

> [!tip] Active recall
> Answer every part before revealing the answer. For design/essay questions, the answer is a grading checklist: alternative designs can also be correct when justified.

### Q1 — Fault–error–failure for SQL injection

> [!question] Question
> Trace SQL injection and a normal apostrophe bug through fault→error→failure. What changes in the security case?

> [!answer]- Answer / self-check
> Shared **fault:** constructing SQL with untrusted string concatenation instead of parameterization. Normal bug: apostrophe produces malformed query (**error/internal invalid command**) → exception/wrong service (**failure**). Attack: adversarial input changes query semantics (**error: unauthorized query state**) → unauthorized access/data change (**security failure**). Security adds an intelligent adversary exploiting the same defect, so likelihood/blast radius differ.

### Q2 — SAST vs threat modeling first

> [!question] Question
> Use McGraw's 50/50 idea and Avizienis's four means to reason about a startup's first investment.

> [!answer]- Answer / self-check
> Only one leaves a major blind spot: automated code tools mainly find **implementation bugs**, threat modeling finds **design flaws**. A defensible startup-first choice is lightweight threat modeling for auth/data/trust boundaries because design flaws are expensive to retrofit, then automate SAST immediately after; alternatively SAST can be first when code churn and zero automation dominate. Map means: prevention→secure design/training; tolerance→sandboxing/least privilege/fail-safe recovery; removal→SAST/testing/patching; forecasting→risk/threat/vulnerability analysis.

### Q3 — Pick one security tool under CI constraints

> [!question] Question
> Compare SAST, DAST, and SCA for 5 deployments/day and 30% tool effectiveness.

> [!answer]- Answer / self-check
> - **SAST:** early/custom-code reach but high false-positive triage; usually fits build/PR.
> - **DAST:** realistic runtime findings/low FP but ~14 min cited overhead → ~70 min/day if serial across five deploys; run asynchronously/nightly or on staging.
> - **SCA:** low friction and excellent known-dependency CVEs, but no custom-code/design coverage.
> ~30% effectiveness means no tool is a complete security program. Pick based on dominant exposure and complement it with review/threat modeling.
> **Effective vulnerability ≠ true positive:** a real finding can be irrelevant, duplicate or not worth fixing in that context. Thus 30% actionable/effective results does **not** imply a measured 70% false-positive rate. Include triage cost and reachable risk, not just scan runtime, in the decision.

### Q4 — Code review + fuzzing

> [!question] Question
> What does each technique catch, and how should a bank combine them?

> [!answer]- Answer / self-check
> Security-focused review is strong for **business logic, authorization, trust-boundary, crypto/API misuse** but can miss huge input spaces. Fuzzing is strong for **parser/input handling, memory safety, crashes/DoS** but may miss semantic fraud that does not crash. Use security checklists/assigned reviewers and threat-model references; fuzz critical transfer parsers/APIs with coverage guidance/sanitizers and realistic seeds. For fraud, logic review/threat modeling is central; for DoS/input corruption, fuzzing is central.
> The source reports fewer than 1% of review comments concerned security, with **81.3% of raised security defects fixed when a concrete fix was proposed**. Write an actionable comment identifying the unsafe path, consequence and a specific remediation/test rather than “security issue?”. This is study evidence, not a universal fix probability.

### Q5 — Apply STRIDE

> [!question] Question
> Give one web-banking threat per STRIDE category with a target and mitigation.

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

### Q6 — Threat-model method for GDPR healthcare

> [!question] Question
> Why is STRIDE alone insufficient, and what pragmatic mix should a small startup use?

> [!answer]- Answer / self-check
> STRIDE focuses technical security properties; GDPR also demands privacy threats such as **linkability, identifiability, detectability, disclosure, unawareness, non-compliance** (LINDDUN). A small team can build one DFD, run STRIDE on trust boundaries, then a focused LINDDUN pass on personal/health data and data lifecycle. Start at lightweight repeatable maturity (trained facilitator + checklist) and evolve toward threat models in design reviews and release cadence.
> LINDDUN also includes **non-repudiation as a privacy threat** (loss of plausible deniability). The reported field maturity **level 1/ad hoc** and roughly **69 hours/project** warn that facilitation, scope and iteration need planned effort; they do not prescribe a fixed 69-hour budget for this startup. Avoid an elaborate PASTA program the three-person team cannot sustain.

### Q7 — Saltzer–Schroeder principles and breaches

> [!question] Question
> Map major breaches to design principles; explain two in depth.

> [!answer]- Answer / self-check
> Mappings are not unique—justify causally. Reasonable examples: **Target → least privilege / separation of privilege** (vendor access should not reach payment network); **Equifax → complete mediation / secure maintenance** (vulnerable internet-facing component remained exploitable); **Heartbleed → fail-safe defaults/economy of mechanism** (unchecked length exposed memory); **SolarWinds → least common mechanism / trusted build-chain controls**; **WannaCry → least privilege + fail-safe network segmentation**; **Log4Shell → economy of mechanism / minimize ambient dangerous capability**. State the principle definition and how design would reduce blast radius.
> Distinguish the eight principles from **SD3** (secure by design, by default, in deployment). For the source's direct readings: Equifax/WannaCry → **secure in deployment** (unpatched services); Log4Shell → **secure by default** (dangerous lookup enabled); SolarWinds → **separation of privilege** (independent build/change approval); Target → **least privilege**. Heartbleed supports economy of mechanism or secure-by-default, with reasons. Do not relabel generic “patching” as complete mediation without explaining the missing access check.

### Q8 — Allowlist input validation

> [!question] Question
> Design validation for name/email/age; show why denylisting fails and explain an input chokepoint.

> [!answer]- Answer / self-check
> Allowlist by **type, canonical form, length, character set, and semantic range**: e.g. name normalized Unicode + bounded length; email parsed/canonicalized with bounded lengths; age integer within business range. Denylists miss encodings/Unicode/alternate syntax. **Canonicalize then validate**. An input chokepoint centralizes validation at a small trusted boundary so every downstream path receives normalized validated data and policy is not duplicated.
> Example policy: name 1–80 permitted normalized characters; email parsed with a 254-character limit; age an integer (not a Boolean/string) in 0–130. Blocking only quotes/brackets still accepts invalid **age −100**, and a filter-before-decode can miss `%27 OR 1=1 --` or double-encoded `%2527`. Decode according to one consistent boundary contract, validate the resulting form, and still use parameterized SQL; validation is not a substitute for safe query construction.

### Q9 — DevSecOps pipeline

> [!question] Question
> Place security checks from IDE to production within time budgets.

> [!answer]- Answer / self-check
> Example: IDE—lint/secret/SAST hints; pre-commit—secrets, formatting, fast SAST; CI build—SCA/SBOM, SAST, IaC/container scan; CI test—security unit/integration + fuzz subsets; staging/CD—DAST and policy/admission checks (long DAST async if ~14 min); production—runtime detection, WAF, dependency/vuln monitoring. Triage by severity/exploitability/ownership and baseline known false positives. Not all checks shift left because some require a running integrated system/real environment.
> Fit measured budgets: IDE instant; pre-commit <30 s; build <5 min; test <15 min (the cited DAST job was **14 min 6 s**, best parallel/asynchronous); deploy <2 min; operate continuously. **Bandit `-ll` is a severity filter**, retaining medium/high regardless of confidence and letting low-severity findings through. Add a secrets scanner and appropriate review for low-severity hardcoded credentials.

### Q10 — Software supply-chain attacks

> [!question] Question
> Explain dependency, build-infrastructure, and human vectors using Log4Shell, SolarWinds, and XZ; include SBOM value/limits.

> [!answer]- Answer / self-check
> - **Log4Shell:** vulnerable dependency capability reachable via attacker-controlled strings → patch/upgrade, SCA, egress/JNDI hardening; SBOM helps locate affected versions.
> - **SolarWinds:** build/update pipeline compromise shipped trusted malicious artifacts → hardened isolated builds, signing/provenance/reproducibility; SBOM alone may still list legitimate components and miss a compromised build process.
> - **XZ:** social-engineering/maintainer-trust attack inserted a backdoor into release artifacts/build path → maintainer governance, review, provenance, reproducible builds; SBOM helps inventory but not human intent.

### Q11 — CVSS base, temporal, environmental

> [!question] Question
> For CVSS v3.1 `AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H` (base 8.1), compute temporal with E:P, RL:T, RC:C, then environmental with CR/IR/AR:L and unchanged base metrics. Compare Log4Shell's publication-time temporal score and decide patch urgency.

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

### Q12 — Three-horizon fintech remediation

> [!question] Question
> Prioritize SQLi, vulnerable Log4j, and missing auth threat model across immediate/quarter/year horizons.

> [!answer]- Answer / self-check
> **Immediate:** patch/mitigate internet-exposed known RCE Log4j and SQLi in parallel; if forced to order, prioritize the finding with active exploitability + greatest reachable blast radius. Disable vulnerable features/WAF rules/network egress as temporary controls; parameterize queries and add regression tests. **Quarter:** SCA/SBOM, SAST, secret scanning, fuzz/security tests, security-review checklist/ownership. **Year:** recurring STRIDE + privacy/risk modeling, supply-chain provenance/reproducible builds, secure design training, metrics and incident feedback. Missing threat model is a program gap: start now, mature continuously.
> The fintech SQLi has **A:H** because multiple SQL statements can delete tables and stop service; the shop example's A:N assumed only the attacker's query failed. Restrict network access to exposed endpoints until fixed. SAST/exploit regression tests address SQL construction, SCA/SBOM identifies the vulnerable Log4j version; neither substitutes for an auth design threat model. Include independent maintainer review for the human vector and isolated, verifiable build provenance for infrastructure compromise.

### Q13 — Penetration testing phases and limits

> [!question] Question
> Name NIST's four phases. Where does written approval belong? Classify login with a default admin password, explain post-exploitation and interpret a clean one-week report.

> [!answer]- Answer / self-check
> **Planning:** scope, rules and written authorization before activity. **Discovery:** collect information and identify possible weaknesses. **Attack:** exploit one, such as logging into admin with the default password, and explore further findings. **Reporting:** document evidence, impact and fixes throughout and at completion. **Post-exploitation** asks what access enables next (data access, lateral movement, persistence) within the agreed scope. No critical findings means none found in that sampled scope/time, not proof of no vulnerabilities.

### Q14 — SQUARE and testable security requirements

> [!question] Question
> Apply SQUARE steps 2–4 to an exam-submission feature: assets/goals, misuse case and highest risk. Turn it into a testable requirement and CI test. Would RQCODE `check()`/`enforce()` fit?

> [!answer]- Answer / self-check
> **Goals/assets:** protect answer confidentiality and submission/grade integrity. **Artefacts/misuse case:** DFD plus a student changing another student's stored answer by substituting its submission ID. **Risk:** unauthorized answer modification has high integrity impact; rank likelihood/exposure explicitly.
> **Requirement:** on every submission-update request, the service shall authorize the authenticated owner and the server-side exam window before any write; unauthorized or late attempts shall be rejected without changing data. Test in CI with two accounts, swapped IDs and before/at/after deadline cases; assert both denial and unchanged stored answers, plus a valid positive case.
> SQUARE's full sequence: definitions → goals → artefacts → risks → elicitation technique → requirements → categorization → prioritization → inspection. **RQCODE** suits checkable/enforceable configuration such as a security setting; this stateful authorization/time behavior needs application context and integration tests, rather than only inspecting/remediating a setting.
