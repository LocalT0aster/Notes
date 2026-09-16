# L02 — Quality Measurement & Metrics Flashcards

**Source:** https://sqrbok.github.io//content/material/sqr/RQ_L2_Metrics.html

**Cards:** 12

> [!tip] Active recall
> Answer every part before revealing the answer. For design/essay questions, the answer is a grading checklist: alternative designs can also be correct when justified.

### Q1 — Hubbard measurement vs transcendent quality

> [!question] Question
> State Hubbard's definition of measurement and contrast it with Garvin's transcendent view.

> [!answer]- Answer / self-check
> Hubbard: **measurement is a quantitatively expressed reduction of uncertainty based on one or more observations**. Garvin's transcendent view treats quality as recognizable excellence that is hard to define. Hubbard challenges that stance: useful measurement need not be perfect; even partial quantitative evidence can reduce uncertainty.

### Q2 — Resolution, accuracy, precision

> [!question] Question
> Define resolution, accuracy, and precision. A tool always reports CC=10 while the correct value is 12—what is it?

> [!answer]- Answer / self-check
> - **Resolution:** smallest change the measurement can distinguish.
> - **Accuracy:** closeness to the true/reference value.
> - **Precision:** repeatability/consistency.
> The tool is **precise but inaccurate** if it repeatedly reports 10.

### Q3 — Three metric dangers

> [!question] Question
> Analyze an 80% coverage mandate that produces 85% coverage but no defect reduction using bad statistics, bad decisions, and bad incentives.

> [!answer]- Answer / self-check
> - **Bad statistics:** coverage is treated as a direct proxy for effectiveness.
> - **Bad decisions:** the organization optimizes the proxy instead of defect risk / assertions / requirements.
> - **Bad incentives:** developers write tests only to cross the threshold (Goodhart-like gaming).
> A metric should inform a goal, not become the goal.

### Q4 — McNamara fallacy and streetlight effect

> [!question] Question
> A manager promotes the developer with more commits/LOC/closed bugs while ignoring mentoring, architecture, and debt reduction. Which fallacies apply?

> [!answer]- Answer / self-check
> **Both can apply.** McNamara: decisions use only what is easily quantified and effectively assign zero value to hard-to-measure contributions. Streetlight effect: the manager measures what tools conveniently expose instead of what best represents performance/value.

### Q5 — NOIR scales

> [!question] Question
> Explain Nominal, Ordinal, Interval, and Ratio scales with software examples.

> [!answer]- Answer / self-check
> - **Nominal:** categories only; e.g. defect type.
> - **Ordinal:** ordered categories; e.g. severity Low/Medium/High.
> - **Interval:** equal differences, no true zero; classic example temperature °C (software examples are rarer).
> - **Ratio:** equal intervals + true zero; e.g. LOC, elapsed time, defect count.
> Only use operations meaningful for the scale.

### Q6 — Mean vs median

> [!question] Question
> When should mean vs median be used? For nine 1-hour fixes and one 100-hour fix, calculate both.

> [!answer]- Answer / self-check
> Mean is useful for roughly symmetric quantitative data; median is robust for skew/outlier-heavy data. Mean = (9×1+100)/10 = **10.9 h**. Median = **1 h**, which better represents the typical fix in this sample.

### Q7 — Confounding variables

> [!question] Question
> Define a confounder and explain the class-size confounding result in OO metrics research.

> [!answer]- Answer / self-check
> A confounder affects both the proposed predictor and the outcome, creating/magnifying an apparent relationship. Large classes tend to have higher OO metric values **and** more defects. After controlling for class size, many metric–defect associations shrink; the lecture notes that only **4 of 24** commonly used OO metrics remained useful in that study.

### Q8 — Goal–Question–Metric (GQM)

> [!question] Question
> Apply GQM to “Improve maintainability of the codebase.”

> [!answer]- Answer / self-check
> Example:
> - **Goal:** improve maintainability for the development team in the current maintenance context.
> - **Questions:** Which modules are hard to understand/change? Where is coupling/complexity concentrated? How long do changes take?
> - **Metrics:** cyclomatic complexity, coupling, change lead time, defect escape after changes, review/rework rates.
> Metrics must answer the questions that operationalize the goal.

### Q9 — Maintainability Index

> [!question] Question
> Explain MI = 171 − 5.2 ln(HV) − 0.23 CC − 16.2 ln(LOC), its inputs, and limitations.

> [!answer]- Answer / self-check
> HV = Halstead Volume, CC = cyclomatic complexity, LOC = size. Higher complexity/volume/size reduce the index. MI is useful as a comparative indicator, not ground truth: variants differ by tool, it mixes correlated size/complexity measures, thresholds are context-dependent, and a single score hides causes.

### Q10 — CK object-oriented metrics

> [!question] Question
> Name five CK metrics and explain what a high value suggests.

> [!answer]- Answer / self-check
> Canonical CK metrics include **WMC** (many/complex methods), **DIT** (deep inheritance), **NOC** (many children), **CBO** (high coupling), **RFC** (large response set), and **LCOM** (low cohesion when high). The question asks for five; know at least five plus the direction/interpretation.

### Q11 — Operational definitions

> [!question] Question
> Before comparing 15 vs 8 defects/KLOC, what must be operationally defined?

> [!answer]- Answer / self-check
> Ensure **communication** and **repeatability**. Define what counts as a defect (severity, duplicate handling, source), when it is counted (opened/confirmed/fixed), what code is in KLOC (generated/tests/comments?), counting method (physical/logical LOC), time window, and product/version. Otherwise the rates are not comparable.

### Q12 — From quality model to measure

> [!question] Question
> Explain Characteristic → Sub-characteristic → Measure with a maintainability example.

> [!answer]- Answer / self-check
> Example: **Maintainability** → **Analyzability/Modifiability/Testability** → concrete measure such as mean change lead time, coupling, complexity, or automated-test execution/coverage relevant to that sub-characteristic. The hierarchy turns a broad quality concept into observable evidence.
