# L10 — Security Flashcards

**Source:** https://sqrbok.github.io//content/material/sqr/RQ_L10_Security.html

**Cards:** 12

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

### Q4 — Code review + fuzzing

> [!question] Question
> What does each technique catch, and how should a bank combine them?

> [!answer]- Answer / self-check
> Security-focused review is strong for **business logic, authorization, trust-boundary, crypto/API misuse** but can miss huge input spaces. Fuzzing is strong for **parser/input handling, memory safety, crashes/DoS** but may miss semantic fraud that does not crash. Use security checklists/assigned reviewers and threat-model references; fuzz critical transfer parsers/APIs with coverage guidance/sanitizers and realistic seeds. For fraud, logic review/threat modeling is central; for DoS/input corruption, fuzzing is central.

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

### Q6 — Threat-model method for GDPR healthcare

> [!question] Question
> Why is STRIDE alone insufficient, and what pragmatic mix should a small startup use?

> [!answer]- Answer / self-check
> STRIDE focuses technical security properties; GDPR also demands privacy threats such as **linkability, identifiability, detectability, disclosure, unawareness, non-compliance** (LINDDUN). A small team can build one DFD, run STRIDE on trust boundaries, then a focused LINDDUN pass on personal/health data and data lifecycle. Start at lightweight repeatable maturity (trained facilitator + checklist) and evolve toward threat models in design reviews and release cadence.

### Q7 — Saltzer–Schroeder principles and breaches

> [!question] Question
> Map major breaches to design principles; explain two in depth.

> [!answer]- Answer / self-check
> Mappings are not unique—justify causally. Reasonable examples: **Target → least privilege / separation of privilege** (vendor access should not reach payment network); **Equifax → complete mediation / secure maintenance** (vulnerable internet-facing component remained exploitable); **Heartbleed → fail-safe defaults/economy of mechanism** (unchecked length exposed memory); **SolarWinds → least common mechanism / trusted build-chain controls**; **WannaCry → least privilege + fail-safe network segmentation**; **Log4Shell → economy of mechanism / minimize ambient dangerous capability**. State the principle definition and how design would reduce blast radius.

### Q8 — Allowlist input validation

> [!question] Question
> Design validation for name/email/age; show why denylisting fails and explain an input chokepoint.

> [!answer]- Answer / self-check
> Allowlist by **type, canonical form, length, character set, and semantic range**: e.g. name normalized Unicode + bounded length; email parsed/canonicalized with bounded lengths; age integer within business range. Denylists miss encodings/Unicode/alternate syntax. **Canonicalize then validate**. An input chokepoint centralizes validation at a small trusted boundary so every downstream path receives normalized validated data and policy is not duplicated.

### Q9 — DevSecOps pipeline

> [!question] Question
> Place security checks from IDE to production within time budgets.

> [!answer]- Answer / self-check
> Example: IDE—lint/secret/SAST hints; pre-commit—secrets, formatting, fast SAST; CI build—SCA/SBOM, SAST, IaC/container scan; CI test—security unit/integration + fuzz subsets; staging/CD—DAST and policy/admission checks (long DAST async if ~14 min); production—runtime detection, WAF, dependency/vuln monitoring. Triage by severity/exploitability/ownership and baseline known false positives. Not all checks shift left because some require a running integrated system/real environment.

### Q10 — Software supply-chain attacks

> [!question] Question
> Explain dependency, build-infrastructure, and human vectors using Log4Shell, SolarWinds, and XZ; include SBOM value/limits.

> [!answer]- Answer / self-check
> - **Log4Shell:** vulnerable dependency capability reachable via attacker-controlled strings → patch/upgrade, SCA, egress/JNDI hardening; SBOM helps locate affected versions.
> - **SolarWinds:** build/update pipeline compromise shipped trusted malicious artifacts → hardened isolated builds, signing/provenance/reproducibility; SBOM alone may still list legitimate components and miss a compromised build process.
> - **XZ:** social-engineering/maintainer-trust attack inserted a backdoor into release artifacts/build path → maintainer governance, review, provenance, reproducible builds; SBOM helps inventory but not human intent.

### Q11 — CVSS base, temporal, environmental

> [!question] Question
> Explain 8.1→7.1→4.0 and decide emergency vs sprint patch; compare Log4Shell.

> [!answer]- Answer / self-check
> **Base** describes intrinsic exploit/impact; **Temporal** adjusts for exploit maturity/fix/report confidence; **Environmental** adjusts for local asset importance/controls. Here unproven exploit + official fix lower temporal risk, and public data + WAF lowers local impact. A next-sprint patch can be defensible if exposure/controls are verified and monitoring exists; emergency patch if exploit evidence/exposure changes. Log4Shell was more urgent because **AC:L vs AC:H** and **Scope Changed vs Unchanged** (plus rapid exploit weaponization and initially difficult remediation) made real-world exploitation far easier.

### Q12 — Three-horizon fintech remediation

> [!question] Question
> Prioritize SQLi, vulnerable Log4j, and missing auth threat model across immediate/quarter/year horizons.

> [!answer]- Answer / self-check
> **Immediate:** patch/mitigate internet-exposed known RCE Log4j and SQLi in parallel; if forced to order, prioritize the finding with active exploitability + greatest reachable blast radius. Disable vulnerable features/WAF rules/network egress as temporary controls; parameterize queries and add regression tests. **Quarter:** SCA/SBOM, SAST, secret scanning, fuzz/security tests, security-review checklist/ownership. **Year:** recurring STRIDE + privacy/risk modeling, supply-chain provenance/reproducible builds, secure design training, metrics and incident feedback. Missing threat model is a program gap: start now, mature continuously.
