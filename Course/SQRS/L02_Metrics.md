# L02 — Quality Measurement & Metrics Flashcards

**Source:** https://sqrbok.github.io/content/material/sqr/RQ_L2_Metrics.html

**Cards:** 20

> [!tip] Active recall
> Answer every part before revealing the answer. For design/essay questions, the answer is a grading checklist: alternative designs can also be correct when justified.

### Q1 — Hubbard measurement vs transcendent quality

> [!question] Question
> State Hubbard's definition of measurement and contrast it with Garvin's transcendent view.

> [!answer]- Answer / self-check
> Hubbard: **measurement is a quantitatively expressed reduction of uncertainty based on one or more observations**. Garvin's transcendent view treats quality as recognizable excellence that is hard to define. Hubbard challenges that stance: useful measurement need not be perfect; even partial quantitative evidence can reduce uncertainty.
> **Sarle:** assign numbers so their relationships reflect relationships in the measured attribute (representation condition). Hubbard's three steps: if it matters it is detectable; if detectable, observe more/less; amounts can be measured. For developer happiness, repeated surveys and retention/absence observations can reduce uncertainty, but proxies need validation and privacy-aware interpretation.

### Q2 — Resolution, accuracy, precision

> [!question] Question
> Define resolution, accuracy, and precision. A timing tool always reports 250 ms for 200 ms; a log truncates 200 and 800 ms to whole seconds; a CC tool reports 10 against a hand count of 12. Diagnose each.

> [!answer]- Answer / self-check
> - **Resolution:** smallest change the measurement can distinguish.
> - **Accuracy:** closeness to the true/reference value.
> - **Precision:** repeatability/consistency.
> The timer is **precise but inaccurate**. The log reports **0 seconds** for both: inadequate resolution. Before calling CC=10 inaccurate, check identical counting rules, e.g. whether Boolean operators count as decisions. If definitions and reference really agree, a repeatable wrong value is precise but inaccurate.

### Q3 — Three metric dangers

> [!question] Question
> Analyze an 80% coverage mandate that produces 85% coverage but no defect reduction using bad statistics, bad decisions, and bad incentives.

> [!answer]- Answer / self-check
> - **Bad statistics:** coverage is treated as a direct proxy for effectiveness.
> - **Bad decisions:** the organization optimizes the proxy instead of defect risk / assertions / requirements.
> - **Bad incentives:** developers write tests only to cross the threshold (Goodhart-like gaming).
> A metric should inform a goal, not become the goal.
> In the source example, (6000×0.95 + 3000×0.90 + 1000×0.40)/10000 = **88%** masks a payment module at **40%**: aggregation hides the highest-risk weakness. The other two errors are substituting coverage for effectiveness and rewarding tests that hit lines without checking behavior.

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
> The lecture distinguishes **absolute** counts (e.g. open defects, a fixed unit) from general ratio measurements. For defect-record fields: component → nominal/mode; severity → ordinal/median; date reported → interval/mean date; hours to fix → ratio/mean or median; number open → absolute/count arithmetic.
> Only use operations meaningful for the scale.

### Q6 — Mean vs median

> [!question] Question
> When should mean vs median be used? For nine 1-hour fixes and one 100-hour fix, calculate both.

> [!answer]- Answer / self-check
> Mean is useful for roughly symmetric quantitative data; median is robust for skew/outlier-heavy data. Mean = (9×1+100)/10 = **10.9 h**. Median = **1 h**, which better represents the typical fix in this sample.
> For response times report median **and a high percentile** such as p95/p99, along with the window and sample size. A median alone hides slow users; a mean remains useful for totals/resource accounting.

### Q7 — Confounding variables

> [!question] Question
> Define a confounder and explain the class-size confounding result in OO metrics research.

> [!answer]- Answer / self-check
> A confounder affects both predictor and outcome: **size → CBO**, **size → faults**, while **CBO → faults** is the hypothesis. The notes distinguish two studies: in one C++ system **no CK metric** remained associated after size control; in another, **4 of 24 OO metrics** remained associated, with two coupling metrics improving prediction. Reducing CBO alone is therefore not established as a causal way to reduce faults; evaluate locally with size controlled.

### Q8 — Goal–Question–Metric (GQM)

> [!question] Question
> Apply GQM to “Improve maintainability of the codebase.”

> [!answer]- Answer / self-check
> Example:
> - **Goal:** improve maintainability for the development team in the current maintenance context.
> - **Questions:** Which modules are hard to understand/change? Where is coupling/complexity concentrated? How long do changes take?
> - **Metrics:** cyclomatic complexity, coupling, change lead time, defect escape after changes, review/rework rates.
> Metrics must answer the questions that operationalize the goal.
> For escaped defects: **analyse the release process** (object), **to improve** (purpose) **production defect escape** (focus), **from the service owner's view** (viewpoint), **for this team's monthly releases** (context). Questions: how many defects escape, and which gate missed them? Metrics: confirmed post-release defects per release/severity and fraction by earliest missed detection stage, with stable counting windows.

### Q9 — Maintainability Index

> [!question] Question
> Explain MI, then compute Halstead volume and normalized MI for n₁=7, n₂=12, N₁=9, N₂=18, CC=6, LLOC=11, no comments. Give Visual Studio and radon bands.

> [!answer]- Answer / self-check
> HV = Halstead Volume, CC = cyclomatic complexity, LOC = size. Higher complexity/volume/size reduce the index. MI is useful as a comparative indicator, not ground truth: variants differ by tool, it mixes correlated size/complexity measures, thresholds are context-dependent, and a single score hides causes.
> Vocabulary n=7+12=19; length N=9+18=27; **V=N log₂n≈114.69**. Raw index = 171−5.2 ln(V)−0.23×6−16.2 ln(11)≈**106.11**; normalized **MI=max(0, raw×100/171)≈62.06**. Visual Studio **green**; radon MI rank **A** (20–100; B 10–<20; C <10). These are not radon's cyclomatic-complexity letter bands. Tool differences include LOC definitions, decision counting, comment terms and per-file aggregation.

### Q10 — CK object-oriented metrics

> [!question] Question
> Name all six CK metrics and their counting rules. For four unit-weight methods, only superclass `object`, no children and two used classes with no incoming users, compute WMC, DIT, NOC and CBO. Why distrust a borrowed CBO>14 threshold?

> [!answer]- Answer / self-check
> **WMC:** sum of method weights/complexities; **DIT:** inheritance depth; **NOC:** immediate subclasses; **CBO:** other classes used or using this class under the stated rule; **RFC:** own methods plus directly called methods; **LCOM:** non-sharing method pairs minus attribute-sharing pairs, floored at zero (original variant). Here **WMC=4, DIT=1** (`object` depth 0), **NOC=0, CBO=2** (exclude root inheritance from this coupling count). A threshold borrowed from another system may reflect its size/distribution rather than validated fault risk in yours.

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
> In McCall terms: **factor maintainability → criterion simplicity → metric cyclomatic complexity → value 4** for a specified function and counting rule. Distinguish a metric definition from its measured value.

### Q13 — Entity, attribute and counting rule

> [!question] Question
> Decompose defects/KLOC into two measurements. Name the entity, attribute and rule for each.

> [!answer]- Answer / self-check
> For a specified release, **defects:** entity = release, attribute = confirmed defect count, rule = unique confirmed post-release defects within the first year, with severity/duplicate exclusions stated. **Size:** entity = that release's source, attribute = code size, rule = nonblank, noncomment physical lines of production code, with generated/test code exclusions stated. Divide the first by LOC/1000 only after fixing both rules.

### Q14 — Representation condition

> [!question] Question
> Why does LOC represent physical code size but not necessarily functionality, complexity or effort?

> [!answer]- Answer / self-check
> Numerical relationships must preserve relationships in the attribute. Under a fixed counting rule, twice as many physical lines means twice that size. One feature can take 50 lines in one implementation and 500 in another; terseness, language and libraries change LOC without a proportional change in functionality, complexity or effort.

### Q15 — Relative versus absolute risk

> [!question] Question
> Incidents rose 100%. What must you ask? Relate it to the 1995 pill warning.

> [!answer]- Answer / self-check
> Ask the original and new **counts**, denominator/exposure and comparable time windows: 1→2 differs from 1000→2000. The lecture's warning example doubled thrombosis risk from about **1/7000 to 2/7000**: +100% relative, but **+1/7000** absolute (about 0.014 percentage points). Report both.

### Q16 — Meaningful arithmetic on scales

> [!question] Question
> Is mean severity 2.7 meaningful? Twice the hours? Twice as warm at 20°C versus 10°C?

> [!answer]- Answer / self-check
> **Ordinal severity:** a mean assumes equal category spacing, which the scale alone does not justify; median/category counts are safer. **Effort hours:** a ratio scale with a true zero, so twice the time is meaningful. **Celsius:** interval scale with arbitrary zero; converting to Fahrenheit destroys the 2× relationship, so “twice as warm” is not meaningful.

### Q17 — Story-point scale assumptions

> [!question] Question
> Observed medians for 1/2/3/5/8 points are 21/52/64/100/111 hours. What would a ratio scale predict from 1 point? Would you sum points into velocity?

> [!answer]- Answer / self-check
> Predicted **21/42/63/105/168 hours**. Three and five points are close; two is about 24% higher; eight is far below prediction. Summation treats points as additive ratio-like quantities; state and validate that assumption within the team. Do not infer universal hours/point or compare team velocities as though the units were identical.

### Q18 — Cyclomatic counting conventions

> [!question] Question
> A shipping function has `if total>100 and country=="RU"`, then a `for` loop containing `if item.fragile`. Compute decisions+1 when `and` is part of one decision, then radon's count and the SEI risk band.

> [!answer]- Answer / self-check
> Three decisions (outer if, loop, inner if) +1 gives **4**. Radon additionally counts `and`, yielding **5**, rank **A**. Both are in the lecture's **SEI low-risk 1–10** band. Neither number proves the function correct or maintainable; agree the CFG convention before comparing tools.

### Q19 — Accuracy with rare defects

> [!question] Question
> Of 1000 classes, 10 are faulty. X flags none; Y flags 100 including all faulty classes. Compute accuracy, precision and recall; which helps find faults?

> [!answer]- Answer / self-check
> **X:** TP=0, FP=0, FN=10, TN=990; accuracy **99%**, precision **undefined (0/0)**, recall **0%**. **Y:** TP=10, FP=90, FN=0, TN=900; accuracy **91%**, precision **10%**, recall **100%**. Y finds all faulty classes but requires triage; usefulness depends on inspection cost. Accuracy alone rewards the useless majority-class predictor.

### Q20 — Metrics for generated code

> [!question] Question
> GPT-4 solutions to 72 tasks passed more tests but had higher cyclomatic complexity than human solutions. What follows for evaluating generators?

> [!answer]- Answer / self-check
> Correctness on the sampled tests and structural complexity are different dimensions. One metric cannot establish overall quality: assess functional behavior, robustness/security, maintainability and task context together. The reported sample does not show all generated code is better, or that complexity has no cost.
