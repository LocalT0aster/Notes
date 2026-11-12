# L02 — Quality Measurement & Metrics Flashcards

**Source:** https://sqrbok.github.io/content/material/sqr/RQ_L2_Metrics.html

**Study notes:** https://sqrbok.github.io/content/material/sqr/SN_L2_Metrics.html

**Cards:** 20

> [!tip] Active recall
> Questions are copied verbatim from the pinned SQRBOK source. Answers are locally synthesized self-checks, not official model answers.

### Q1 — From Quality Model to Metric

**Card ID:** l02-metrics-012

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L2_Metrics.html#question-1-from-quality-model-to-metric

> [!question] Question
> ## Question 1: From Quality Model to Metric
>
> Explain the chain *factor → criterion → metric → value*, using McCall's model. Give one example that starts from **maintainability** and ends with a number computed on code.

> [!answer]- Answer / self-check
> Example: **Maintainability** → **Analyzability/Modifiability/Testability** → concrete measure such as mean change lead time, coupling, complexity, or automated-test execution/coverage relevant to that sub-characteristic. The hierarchy turns a broad quality concept into observable evidence.
> In McCall terms: **factor maintainability → criterion simplicity → metric cyclomatic complexity → value 4** for a specified function and counting rule. Distinguish a metric definition from its measured value.

### Q2 — Two Definitions of Measurement

**Card ID:** l02-metrics-001

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L2_Metrics.html#question-2-two-definitions-of-measurement

> [!question] Question
> ## Question 2: Two Definitions of Measurement
>
> State **Hubbard's** definition of measurement and **Sarle's**. What does each one stress?
>
> Hubbard argues that "everything is measurable". Apply his three-step argument to "developer happiness": what would you observe, and what would count as more or less of it?

> [!answer]- Answer / self-check
> Hubbard: **measurement is a quantitatively expressed reduction of uncertainty based on one or more observations**. Garvin's transcendent view treats quality as recognizable excellence that is hard to define. Hubbard challenges that stance: useful measurement need not be perfect; even partial quantitative evidence can reduce uncertainty.
> **Sarle:** assign numbers so their relationships reflect relationships in the measured attribute (representation condition). Hubbard's three steps: if it matters it is detectable; if detectable, observe more/less; amounts can be measured. For developer happiness, repeated surveys and retention/absence observations can reduce uncertainty, but proxies need validation and privacy-aware interpretation.

### Q3 — Entity, Attribute, Rule

**Card ID:** l02-metrics-013

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L2_Metrics.html#question-3-entity-attribute-rule

> [!question] Question
> ## Question 3: Entity, Attribute, Rule
>
> The metric "defects per KLOC of a release" is a ratio of two measurements. For each of the two (the defect count and the size), name the entity, the attribute and the counting rule you would need to write down.

> [!answer]- Answer / self-check
> For a specified release, **defects:** entity = release, attribute = confirmed defect count, rule = unique confirmed post-release defects within the first year, with severity/duplicate exclusions stated. **Size:** entity = that release's source, attribute = code size, rule = nonblank, noncomment physical lines of production code, with generated/test code exclusions stated. Divide the first by LOC/1000 only after fixing both rules.

### Q4 — Resolution, Accuracy, Precision

**Card ID:** l02-metrics-002

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L2_Metrics.html#question-4-resolution-accuracy-precision

> [!question] Question
> ## Question 4: Resolution, Accuracy, Precision
>
> Define **resolution**, **accuracy** and **precision**.
>
> a) A timing script reports 250 ms for a request that really takes 200 ms, on every run. Is the script accurate? Is it precise?
>
> b) A response-time log truncates every reading to whole seconds. Two requests took 200 ms and 800 ms. What does the log show, and which property is the problem?
>
> c) A complexity tool reports 10 for a function; your hand count gives 12. Before calling the tool inaccurate, what should you check?

> [!answer]- Answer / self-check
> - **Resolution:** smallest change the measurement can distinguish.
> - **Accuracy:** closeness to the true/reference value.
> - **Precision:** repeatability/consistency.
> The timer is **precise but inaccurate**. The log reports **0 seconds** for both: inadequate resolution. Before calling CC=10 inaccurate, check identical counting rules, e.g. whether Boolean operators count as decisions. If definitions and reference really agree, a repeatable wrong value is precise but inaccurate.

### Q5 — The Representation Condition

**Card ID:** l02-metrics-014

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L2_Metrics.html#question-5-the-representation-condition

> [!question] Question
> ## Question 5: The Representation Condition
>
> Lines of code satisfy the representation condition for one attribute and not for another. Name both attributes and explain the difference with an example.

> [!answer]- Answer / self-check
> Numerical relationships must preserve relationships in the attribute. Under a fixed counting rule, twice as many physical lines means twice that size. One feature can take 50 lines in one implementation and 500 in another; terseness, language and libraries change LOC without a proportional change in functionality, complexity or effort.

### Q6 — Relative and Absolute Numbers

**Card ID:** l02-metrics-015

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L2_Metrics.html#question-6-relative-and-absolute-numbers

> [!question] Question
> ## Question 6: Relative and Absolute Numbers
>
> A report says "production incidents rose by 100% this quarter". What two numbers would you ask for before reacting? Relate your answer to the 1995 contraceptive-pill warning.

> [!answer]- Answer / self-check
> Ask the original and new **counts**, denominator/exposure and comparable time windows: 1→2 differs from 1000→2000. The lecture's warning example doubled thrombosis risk from about **1/7000 to 2/7000**: +100% relative, but **+1/7000** absolute (about 0.014 percentage points). Report both.

### Q7 — Three Kinds of Pitfall

**Card ID:** l02-metrics-003

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L2_Metrics.html#question-7-three-kinds-of-pitfall

> [!question] Question
> ## Question 7: Three Kinds of Pitfall
>
> **Case:** A company mandates 80% line coverage for every release. After six months the report shows 88% overall: the UI has 6,000 lines at 95% coverage, the API 3,000 lines at 90%, and the payment module 1,000 lines at 40%. Production defects have not decreased, and developers say they write tests "to hit the number".
>
> Analyse the case as **bad statistics**, **bad decisions** and **bad incentives**: what went wrong under each heading?

> [!answer]- Answer / self-check
> - **Bad statistics:** coverage is treated as a direct proxy for effectiveness.
> - **Bad decisions:** the organization optimizes the proxy instead of defect risk / assertions / requirements.
> - **Bad incentives:** developers write tests only to cross the threshold (Goodhart-like gaming).
> A metric should inform a goal, not become the goal.
> In the source example, (6000×0.95 + 3000×0.90 + 1000×0.40)/10000 = **88%** masks a payment module at **40%**: aggregation hides the highest-risk weakness. The other two errors are substituting coverage for effectiveness and rewarding tests that hit lines without checking behavior.

### Q8 — McNamara Fallacy or Streetlight Effect?

**Card ID:** l02-metrics-004

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L2_Metrics.html#question-8-mcnamara-fallacy-or-streetlight-effect

> [!question] Question
> ## Question 8: McNamara Fallacy or Streetlight Effect?
>
> **Case:** A manager ranks developers by commits per week, lines added and tickets closed. Developer A scores high on all three. Developer B scores lower but mentors new hires and removes technical debt. Developer A is promoted.
>
> Which pitfall applies: the McNamara fallacy, the streetlight effect, or both? Justify your answer.

> [!answer]- Answer / self-check
> **Both can apply.** McNamara: decisions use only what is easily quantified and effectively assign zero value to hard-to-measure contributions. Streetlight effect: the manager measures what tools conveniently expose instead of what best represents performance/value.

### Q9 — Classify by Scale

**Card ID:** l02-metrics-005

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L2_Metrics.html#question-9-classify-by-scale

> [!question] Question
> ## Question 9: Classify by Scale
>
> Give the scale (nominal, ordinal, interval, ratio or absolute) of each field of a defect record, and one summary statistic that is meaningful for it:
>
> - component (UI, API, DB)
> - severity 1–4
> - date reported
> - hours to fix
> - number of open defects

> [!answer]- Answer / self-check
> - **Nominal:** categories only; e.g. defect type.
> - **Ordinal:** ordered categories; e.g. severity Low/Medium/High.
> - **Interval:** equal differences, no true zero; classic example temperature °C (software examples are rarer).
> - **Ratio:** equal intervals + true zero; e.g. LOC, elapsed time, defect count.
> The lecture distinguishes **absolute** counts (e.g. open defects, a fixed unit) from general ratio measurements. For defect-record fields: component → nominal/mode; severity → ordinal/median; date reported → interval/mean date; hours to fix → ratio/mean or median; number open → absolute/count arithmetic.
> Only use operations meaningful for the scale.

### Q10 — Is the Statement Meaningful?

**Card ID:** l02-metrics-016

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L2_Metrics.html#question-10-is-the-statement-meaningful

> [!question] Question
> ## Question 10: Is the Statement Meaningful?
>
> For each statement, say whether it is meaningful for its scale, and why:
>
> a) "The average severity of last month's defects was 2.7."
>
> b) "Task A took twice as long as task B" (effort in hours).
>
> c) "Today, at 20 °C, is twice as warm as yesterday at 10 °C."

> [!answer]- Answer / self-check
> **Ordinal severity:** a mean assumes equal category spacing, which the scale alone does not justify; median/category counts are safer. **Effort hours:** a ratio scale with a true zero, so twice the time is meaningful. **Celsius:** interval scale with arbitrary zero; converting to Fahrenheit destroys the 2× relationship, so “twice as warm” is not meaningful.

### Q11 — Story Points

**Card ID:** l02-metrics-017

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L2_Metrics.html#question-11-story-points

> [!question] Question
> ## Question 11: Story Points
>
> In one company's data, the median hours spent were 21, 52, 64, 100 and 111 for stories of 1, 2, 3, 5 and 8 points. If story points were a ratio scale, what medians would you expect from the 1-point median? Where does the data agree with a ratio scale, and where not? Would you sum story points into a velocity? State your assumption.

> [!answer]- Answer / self-check
> Predicted **21/42/63/105/168 hours**. Three and five points are close; two is about 24% higher; eight is far below prediction. Summation treats points as additive ratio-like quantities; state and validate that assumption within the team. Do not infer universal hours/point or compare team velocities as though the units were identical.

### Q12 — Mean or Median?

**Card ID:** l02-metrics-006

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L2_Metrics.html#question-12-mean-or-median

> [!question] Question
> ## Question 12: Mean or Median?
>
> Nine bugs took 1 hour each to fix and one took 100 hours. Compute the mean and the median. Which describes a typical fix, and which number would you report for response times?

> [!answer]- Answer / self-check
> Mean is useful for roughly symmetric quantitative data; median is robust for skew/outlier-heavy data. Mean = (9×1+100)/10 = **10.9 h**. Median = **1 h**, which better represents the typical fix in this sample.
> For response times report median **and a high percentile** such as p95/p99, along with the window and sample size. A median alone hides slow users; a mean remains useful for totals/resource accounting.

### Q13 — Confounding by Size

**Card ID:** l02-metrics-007

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L2_Metrics.html#question-13-confounding-by-size

> [!question] Question
> ## Question 13: Confounding by Size
>
> What is a **confounding variable**? Draw the three-arrow diagram for class size, a class metric such as CBO, and fault-proneness.
>
> El Emam and colleagues found that after controlling for class size, none of the CK metrics in one system remained associated with faults. What does this imply for a team that plans to reduce faults by reducing CBO?

> [!answer]- Answer / self-check
> A confounder affects both predictor and outcome: **size → CBO**, **size → faults**, while **CBO → faults** is the hypothesis. The notes distinguish two studies: in one C++ system **no CK metric** remained associated after size control; in another, **4 of 24 OO metrics** remained associated, with two coupling metrics improving prediction. Reducing CBO alone is therefore not established as a causal way to reduce faults; evaluate locally with size controlled.

### Q14 — GQM

**Card ID:** l02-metrics-008

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L2_Metrics.html#question-14-gqm

> [!question] Question
> ## Question 14: GQM
>
> Apply **Goal–Question–Metric** to the goal "reduce the number of defects that reach production". Write the goal with all five parts (object, purpose, quality focus, viewpoint, context), give two questions, and at least one metric for each question.

> [!answer]- Answer / self-check
> Example:
> - **Goal:** improve maintainability for the development team in the current maintenance context.
> - **Questions:** Which modules are hard to understand/change? Where is coupling/complexity concentrated? How long do changes take?
> - **Metrics:** cyclomatic complexity, coupling, change lead time, defect escape after changes, review/rework rates.
> Metrics must answer the questions that operationalize the goal.
> For escaped defects: **analyse the release process** (object), **to improve** (purpose) **production defect escape** (focus), **from the service owner's view** (viewpoint), **for this team's monthly releases** (context). Questions: how many defects escape, and which gate missed them? Metrics: confirmed post-release defects per release/severity and fraction by earliest missed detection stage, with stable counting windows.

### Q15 — Operational Definitions

**Card ID:** l02-metrics-011

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L2_Metrics.html#question-15-operational-definitions

> [!question] Question
> ## Question 15: Operational Definitions
>
> Team A reports 15 defects per KLOC; Team B reports 8. Before concluding that Team B writes better code, list the operational-definition questions you must ask, and say which of Park's two criteria each question protects.

> [!answer]- Answer / self-check
> Ensure **communication** and **repeatability**. Define what counts as a defect (severity, duplicate handling, source), when it is counted (opened/confirmed/fixed), what code is in KLOC (generated/tests/comments?), counting method (physical/logical LOC), time window, and product/version. Otherwise the rates are not comparable.

### Q16 — Cyclomatic Complexity

**Card ID:** l02-metrics-018

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L2_Metrics.html#question-16-cyclomatic-complexity

> [!question] Question
> ## Question 16: Cyclomatic Complexity
>
> Give two counts for this function: the cyclomatic complexity from its control-flow graph (decisions + 1, with `and` drawn as part of one decision), and what `radon cc` would report. Explain the difference:
>
> ```python
> def shipping(order):
>     if order.total > 100 and order.country == "RU":
>         return 0
>     for item in order.items:
>         if item.fragile:
>             return 15
>     return 5
> ```
>
> What do the SEI risk bands say about the result?

> [!answer]- Answer / self-check
> Three decisions (outer if, loop, inner if) +1 gives **4**. Radon additionally counts `and`, yielding **5**, rank **A**. Both are in the lecture's **SEI low-risk 1–10** band. Neither number proves the function correct or maintainable; agree the CFG convention before comparing tools.

### Q17 — Halstead and the Maintainability Index

**Card ID:** l02-metrics-009

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L2_Metrics.html#question-17-halstead-and-the-maintainability-index

> [!question] Question
> ## Question 17: Halstead and the Maintainability Index
>
> A file holds one function, with *n₁* = 7, *n₂* = 12, *N₁* = 9, *N₂* = 18, cyclomatic complexity 6, 11 logical lines of code and no comments. Compute its Halstead volume and its Maintainability Index on the 0–100 scale. Which colour band does it fall into in Visual Studio, and which radon rank? Name two reasons two tools may report different MIs for the same function.

> [!answer]- Answer / self-check
> HV = Halstead Volume, CC = cyclomatic complexity, LOC = size. Higher complexity/volume/size reduce the index. MI is useful as a comparative indicator, not ground truth: variants differ by tool, it mixes correlated size/complexity measures, thresholds are context-dependent, and a single score hides causes.
> Vocabulary n=7+12=19; length N=9+18=27; **V=N log₂n≈114.69**. Raw index = 171−5.2 ln(V)−0.23×6−16.2 ln(11)≈**106.11**; normalized **MI=max(0, raw×100/171)≈62.06**. Visual Studio **green**; radon MI rank **A** (20–100; B 10–<20; C <10). These are not radon's cyclomatic-complexity letter bands. Tool differences include LOC definitions, decision counting, comment terms and per-file aggregation.

### Q18 — CK Metrics

**Card ID:** l02-metrics-010

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L2_Metrics.html#question-18-ck-metrics

> [!question] Question
> ## Question 18: CK Metrics
>
> List the six **Chidamber–Kemerer** metrics and what each counts. For a class with four methods, one superclass (`object`), no subclasses, calls to two other classes, and no class that uses it, give WMC (unit weights), DIT, NOC and CBO.
>
> Why is a fixed threshold such as "CBO above 14 is bad", taken from another system, unreliable?

> [!answer]- Answer / self-check
> **WMC:** sum of method weights/complexities; **DIT:** inheritance depth; **NOC:** immediate subclasses; **CBO:** other classes used or using this class under the stated rule; **RFC:** own methods plus directly called methods; **LCOM:** non-sharing method pairs minus attribute-sharing pairs, floored at zero (original variant). Here **WMC=4, DIT=1** (`object` depth 0), **NOC=0, CBO=2** (exclude root inheritance from this coupling count). A threshold borrowed from another system may reflect its size/distribution rather than validated fault risk in yours.

### Q19 — Accuracy on Rare Defects

**Card ID:** l02-metrics-019

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L2_Metrics.html#question-19-accuracy-on-rare-defects

> [!question] Question
> ## Question 19: Accuracy on Rare Defects
>
> A system has 1,000 classes, 10 of them faulty. Predictor X flags no class. Predictor Y flags 100 classes, including all 10 faulty ones. Compute accuracy, precision and recall for both (what happens to precision when nothing is flagged?). Which predictor is more useful, and what does this say about a paper that reports only accuracy?

> [!answer]- Answer / self-check
> **X:** TP=0, FP=0, FN=10, TN=990; accuracy **99%**, precision **undefined (0/0)**, recall **0%**. **Y:** TP=10, FP=90, FN=0, TN=900; accuracy **91%**, precision **10%**, recall **100%**. Y finds all faulty classes but requires triage; usefulness depends on inspection cost. Accuracy alone rewards the useless majority-class predictor.

### Q20 — Metrics for Generated Code

**Card ID:** l02-metrics-020

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L2_Metrics.html#question-20-metrics-for-generated-code

> [!question] Question
> ## Question 20: Metrics for Generated Code
>
> GPT-4's solutions to 72 tasks passed more tests than human solutions but had higher cyclomatic complexity. What does this say about measuring a code generator with a single metric?

> [!answer]- Answer / self-check
> Correctness on the sampled tests and structural complexity are different dimensions. One metric cannot establish overall quality: assess functional behavior, robustness/security, maintainability and task context together. The reported sample does not show all generated code is better, or that complexity has no cost.
