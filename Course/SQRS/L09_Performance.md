# L09 — Performance Analysis Flashcards

**Source:** https://sqrbok.github.io/content/material/sqr/RQ_L09_PerformanceAnalysis.html

**Study notes:** https://sqrbok.github.io/content/material/sqr/SN_L09_PerformanceAnalysis.html

**Cards:** 17

> [!tip] Active recall
> Questions are copied verbatim from the pinned SQRBOK source. Answers are locally synthesized self-checks, not official model answers.

### Q1 — The business value of latency

**Card ID:** l09-performance-001

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L09_PerformanceAnalysis.html#q1-the-business-value-of-latency

> [!question] Question
> ### Q1: The business value of latency
>
> Google's experiments found that adding 100–400 ms of delay to search pages reduced searches per user by 0.2–0.6%. A shop processes 50,000 orders a day at an average of 80 USD, and an upgrade costing 200,000 USD a year would cut its response time by 800 ms.
>
> 1. Why can you not simply scale the Google result ("0.2–0.6% per 100–400 ms") to estimate the shop's revenue gain?
> 2. What would you measure in the shop itself to decide whether the upgrade pays off?

> [!answer]- Answer / self-check
> **No:** searches are not purchases, users and baselines differ, and the latency–conversion response need not be linear. The folklore “100 ms≈1% sales” is not a justified forecast. Measure the shop's own randomized/controlled change in conversion, revenue or contribution margin per visitor, tail latency and errors across representative traffic. Daily gross revenue is $4M, but the decision concerns **incremental benefit net of costs**, not a mechanically extrapolated percentage of gross revenue.

### Q2 — Why late fixes are expensive

**Card ID:** l09-performance-002

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L09_PerformanceAnalysis.html#q2-why-late-fixes-are-expensive

> [!question] Question
> ### Q2: Why late fixes are expensive
>
> Explain why a performance problem caused by an anti-pattern cannot be fixed by tuning. Give one example of a problem that a design review could have caught, and say what the redesign would be.

> [!answer]- Answer / self-check
> Design review can change architecture before code/data/dependencies harden. Production fixes can require schema/service redesign, migrations, compatibility work, capacity, incident mitigation, and retesting. Example: chatty synchronous fan-out identified in architecture can become batching/async early; after launch it may require API redesign across services and clients.

### Q3 — Little's law

**Card ID:** l09-performance-003

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L09_PerformanceAnalysis.html#q3-littles-law

> [!question] Question
> ### Q3: Little's law
>
> A Kubernetes deployment shows on average 250 active connections and a mean response time of 125 ms.
>
> 1. What is the throughput in requests per second?
> 2. The team wants a mean response time of 80 ms at the same throughput. How many requests will be in the system?
> 3. A cache cuts response time by 40%. At the same throughput, what happens to concurrency?

> [!answer]- Answer / self-check
> Little's Law N=X·R. X=250/0.125 = **2000 req/s**. At 80 ms, N=2000×0.080 = **160**. A 40% reduction from 125 ms gives R=75 ms, so N=2000×0.075 = **150** concurrent requests at the same throughput.

### Q4 — Averaging rates

**Card ID:** l09-performance-015

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L09_PerformanceAnalysis.html#q4-averaging-rates

> [!question] Question
> ### Q4: Averaging rates
>
> Two benchmark runs of the same workload achieve 40 and 60 requests per second. What is the average throughput, and why is it not 50? When would 50 be the right answer?

> [!answer]- Answer / self-check
> Let each run process W requests. Total rate = 2W/(W/40+W/60) = **48 requests/s**, the harmonic mean. **50** is correct for runs of **equal duration**, where the faster run completes more work. Choose the mean from total work / total elapsed time, not from habit.

### Q5 — Percentiles versus means

**Card ID:** l09-performance-004

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L09_PerformanceAnalysis.html#q5-percentiles-versus-means

> [!question] Question
> ### Q5: Percentiles versus means
>
> Two endpoints both report a mean response time of 500 ms.
>
> - Endpoint A: p50 = 450 ms, p90 = 550 ms, p99 = 600 ms.
> - Endpoint B: p50 = 100 ms, p90 = 200 ms, p99 = 8,000 ms.
>
> 1. Which endpoint serves most users better?
> 2. Which one violates a target of "p99 < 1,000 ms"?
> 3. Why can two endpoints with such different percentiles have the same mean?

> [!answer]- Answer / self-check
> Most users see **B** as faster (p50/p90 far lower), but **B violates the p99 SLA badly** and has extreme tail latency; A is consistent and meets it. Reporting p90 instead of mean would prioritize B's common-case experience, which is why multiple percentiles—especially the SLO percentile—must be monitored.

### Q6 — Behavior under rising load

**Card ID:** l09-performance-005

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L09_PerformanceAnalysis.html#q6-behavior-under-rising-load

> [!question] Question
> ### Q6: Behavior under rising load
>
> Sketch utilization, throughput and response time against the number of users, and mark the light-load, heavy-load and buckle zones. For each zone, say what happens to each metric and to the user. What changes if the bottleneck resource is replaced by one twice as fast?

> [!answer]- Answer / self-check
> - **Light load:** U rises, X rises roughly linearly, R near baseline.
> - **Heavy load:** U approaches saturation, X gains slow, queues grow, R rises sharply.
> - **Buckle/retrograde:** contention/coherency causes X to flatten or fall while R explodes.
> A faster CPU shifts the saturation/buckle point right/up, but cannot remove non-CPU bottlenecks or coordination limits.

### Q7 — Amdahl's law

**Card ID:** l09-performance-006

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L09_PerformanceAnalysis.html#q7-amdahls-law

> [!question] Question
> ### Q7: Amdahl's law
>
> An application spends 45% of its time in database queries, 35% in business logic and 20% in network I/O. A new index makes queries 3 times faster.
>
> 1. What is the overall speedup?
> 2. What is the most you could gain from making queries infinitely fast?
> 3. If network I/O is also made 2 times faster, what is the combined speedup?

> [!answer]- Answer / self-check
> DB only: S=1/(0.55+0.45/3)=1/0.70=**1.43×**. Infinite DB speed: 1/0.55=**1.82×** max. DB 3× + network 2×: new fraction=0.45/3+0.35+0.20/2=0.60 → **1.67×**.

### Q8 — Amdahl or Gustafson?

**Card ID:** l09-performance-007

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L09_PerformanceAnalysis.html#q8-amdahl-or-gustafson

> [!question] Question
> ### Q8: Amdahl or Gustafson?
>
> A training pipeline loads data for 10 minutes (serial) and trains for 50 minutes on one GPU (parallel).
>
> 1. With 10 GPUs and the same data, how long does the pipeline take?
> 2. Under Gustafson's view (loading still takes 10 minutes), what could the team do with 10 GPUs in the original 60 minutes, and what is the scaled speedup?
> 3. Which view fits a team that wants better models rather than faster training runs?

> [!answer]- Answer / self-check
> Fixed problem (Amdahl): 10 + 50/10 = **15 min** idealized. Gustafson view: keep the 60-min wall-clock budget; after 10 min serial work, 10 GPUs provide **500 GPU-min** of parallel training—roughly a 10× larger parallel workload. Use Amdahl for fixed-size speedup; Gustafson when the problem grows with resources.
> The enlarged workload takes **510 minutes on one GPU**, so scaled speedup is **510/60=8.5×**, equivalently 10−9×(10/60). The model assumes the serial loading cost stays fixed.

### Q9 — Retrograde throughput

**Card ID:** l09-performance-008

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L09_PerformanceAnalysis.html#q9-retrograde-throughput

> [!question] Question
> ### Q9: Retrograde throughput
>
> A service cluster measures:
>
> | Instances | Throughput (req/s) |
> |---|---|
> | 1 | 100 |
> | 2 | 185 |
> | 4 | 330 |
> | 8 | 500 |
> | 16 | 450 |
> | 32 | 320 |
>
> 1. Which USL parameter, α or β, explains the decline beyond 8 instances?
> 2. What is physically happening in the cluster?
> 3. Propose one architectural change that would reduce that parameter.

> [!answer]- Answer / self-check
> A decline after a peak is the signature of **coherency/coordination cost β**, not just contention α. More replicas amplify shared-state synchronization, cache invalidation, locks, broadcasts, or cross-node coordination. Reduce shared/coherent state: partition/shard, decentralize coordination, batch, cache, or redesign the bottleneck. Adding instances alone worsens βN(N−1).

### Q10 — Name the anti-pattern

**Card ID:** l09-performance-009

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L09_PerformanceAnalysis.html#q10-name-the-anti-pattern

> [!question] Question
> ### Q10: Name the anti-pattern
>
> For each case, name the anti-pattern and propose a fix.
>
> 1. An endpoint fetches 100 user ids with one query, then each profile with a separate query; it takes 3 s.
> 2. An `OrderController` class computes every order itself: it asks the cart for each item, each item for its price, and the stock component for each item's availability, then applies the discounts. An order of 20 items takes about 60 calls. After your fix, how many calls does the controller make, and where has the work gone?
> 3. A service creates and discards a database connection object on every request, and garbage-collection pauses cause 2 s spikes.

> [!answer]- Answer / self-check
> - 1 + 100 queries → **N+1 query / chatty I/O**; fix with join/batch/prefetch.
> - One service owns unrelated critical work → **god service / serialized bottleneck**; split or isolate queues/resources, use async boundaries.
> - Create/destroy connections per request → **resource churn/no pooling**; use connection pooling/reuse and bounded lifecycle.
> For the source's controller that fetches price/discount/stock for 20 items (**60 calls**), the **God Class** remedy is to put behavior next to its data: call **`cart.total()` once** and let cart/items do their work. That does not magically remove all internal work; it removes controller-level chat and misplaced responsibilities.

### Q11 — How performance bugs are found

**Card ID:** l09-performance-010

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L09_PerformanceAnalysis.html#q11-how-performance-bugs-are-found

> [!question] Question
> ### Q11: How performance bugs are found
>
> Studies found that 33.9–57.3% of performance bugs were discovered by reasoning about code and only 5.5–10.4% with a profiler.
>
> 1. Why does a profiler find so few of them?
> 2. How would you change your team's code review to catch more?

> [!answer]- Answer / self-check
> Profilers expose where time/resources are spent **under the exercised workload**; they do not tell you that the workload model/API usage/architecture is conceptually wrong. The lecture cites many bugs from misunderstanding workload/API (~67%) and only ~5–10% discovered by profiling, while **code review/inspection** finds a much larger share (~33–57%). Review performance assumptions and API complexity explicitly.

### Q12 — Performance budget

**Card ID:** l09-performance-016

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L09_PerformanceAnalysis.html#q12-performance-budget

> [!question] Question
> ### Q12: Performance budget
>
> Explain what a performance budget allocates, how it is tracked during development, and why it is cheaper than load testing alone.

> [!answer]- Answer / self-check
> Allocate the end-to-end response-time/resource target among components, with headroom. Measure/model each component during development and fail meaningful performance regression gates when budgets are exceeded. Discovering a costly interaction while design can change is cheaper than waiting for an integrated load test to expose an architectural bottleneck. Budgeting complements realistic load testing; it does not replace it.

### Q13 — A test strategy for a ticket sale

**Card ID:** l09-performance-011

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L09_PerformanceAnalysis.html#q13-a-test-strategy-for-a-ticket-sale

> [!question] Question
> ### Q13: A test strategy for a ticket sale
>
> A concert ticket platform normally has 5,000 concurrent users; at the moment sales open it expects 200,000 within 60 seconds, for a two-hour sale.
>
> 1. Which of the six test types would you run, and in what order? Where does a spike test fit?
> 2. Which metrics would you monitor, and what targets would you write?
> 3. What does a realistic workload mean here?
> 4. What risk remains if you run only a load test and skip stress and soak tests?

> [!answer]- Answer / self-check
> Sequence a **baseline/smoke → load at 5k → spike to 200k → stress beyond expected peak → scalability/capacity tests → soak/endurance** at sustained realistic traffic. Monitor p50/p95/p99 latency, throughput, errors, saturation (CPU/memory/DB/queues), retries/timeouts, GC, cache hit, dependency SLOs. Realism includes arrival burst shape, transaction mix, think time, hot inventory, auth/payment dependencies.
> The lecture's six named types are **baseline, smoke, load, stress, soak, isolation**; spike is a stress variant, isolation diagnoses one repeated transaction. Write agreed targets, e.g. purchase p99<2 s and failed purchases<0.1% at the specified arrival/peak profile. Model the two-hour sale and recovery, not just the peak count. Skipping stress hides collapse/recovery behavior; skipping soak hides leaks/exhaustion.

### Q14 — Reading a run

**Card ID:** l09-performance-017

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L09_PerformanceAnalysis.html#q14-reading-a-run

> [!question] Question
> ### Q14: Reading a run
>
> During a soak test at constant load, the response time rises slowly but steadily for four hours. What is the likely cause, and what would you look at next?

> [!answer]- Answer / self-check
> Suspect accumulating state or resource exhaustion: memory/connection/thread leaks, unbounded caches/queues or garbage-collection pressure. Correlate latency with heap/RSS, allocation/GC, open handles/connections, queue depth, database locks and throughput; confirm the arrival mix actually stayed stable. A trend is evidence to investigate, not proof of a memory leak.

### Q15 — Tail amplification

**Card ID:** l09-performance-012

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L09_PerformanceAnalysis.html#q15-tail-amplification

> [!question] Question
> ### Q15: Tail amplification
>
> A search query fans out to 80 shards; each shard is slow (over 200 ms) on 0.5% of requests, independently.
>
> 1. What share of queries hits at least one slow shard?
> 2. With hedged requests, a sub-request is slow only if both the original and its copy are slow. If the two are independent, what is the new probability per sub-request, and for the whole query?
> 3. Why does Dean and Barroso's advice to send the copy only after the 95th-percentile expected latency keep the extra load to about 5%?

> [!answer]- Answer / self-check
> At least one slow shard: 1−0.995^80 ≈ **33.0%**. If two independent replicas are raced for every subrequest, both slow probability = 0.005² = **0.0025%**; across 80, ≈ **0.20%** chance at least one remains slow. Full tied requests roughly **double subrequest traffic**. True hedging sends a backup only after a tail threshold, so overhead is near the fraction exceeding that threshold, not 100%.
> Sending a backup after the expected **p95** latency affects about **5%** of originals, so extra requests are about 5%, assuming that latency distribution remains valid. Correlation or overload weakens the independent-copy calculation.

### Q16 — Per-service budgets

**Card ID:** l09-performance-013

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L09_PerformanceAnalysis.html#q16-per-service-budgets

> [!question] Question
> ### Q16: Per-service budgets
>
> A chain of three services has an end-to-end target of p99 < 400 ms. Measured p99s are: gateway 30 ms, recommendation 280 ms, database 50 ms.
>
> 1. Propose a per-service budget.
> 2. The recommendation team wants a new model that raises its p99 to 350 ms. Should it be approved, and what would have to change elsewhere?
> 3. Why is adding the per-service p99s only an approximation of the chain's p99?

> [!answer]- Answer / self-check
> Allocate budgets that sum to ≤400 with contingency, e.g. Gateway 40–50, Recommendation ~290–300, DB 50–60 ms. If Recommendation rises 280→350 with others unchanged, end-to-end ≈ **430 ms**, violating the SLO. Approve only if other components improve or the model's value justifies renegotiating the SLO/risk; latency budget is finite like an error budget.
> Summing marginal p99s is a **budgeting approximation, not the chain's measured p99 or a guarantee**: the slowest 1% need not be the same requests, and correlation changes the sum's distribution. Verify end-to-end percentiles on traces under representative load before approval.

### Q17 — Classical and cloud performance engineering

**Card ID:** l09-performance-014

**Source question:** https://sqrbok.github.io/content/material/sqr/RQ_L09_PerformanceAnalysis.html#q17-classical-and-cloud-performance-engineering

> [!question] Question
> ### Q17: Classical and cloud performance engineering
>
> Map each classical concept to its cloud-native counterpart: the performance budget per component, tracking the budget during development, accepting some degradation, and queuing models. Explain why Little's law and queuing still apply to microservices.

> [!answer]- Answer / self-check
> - Component performance budget → **per-service latency/resource SLO budget**.
> - Budget tracking → **observability, dashboards, SLO/burn monitoring**.
> - Explicit risk acceptance → **error/performance budgets**.
> - Planned PE effort → **continuous performance engineering/capacity work**.
> - Queueing models → **capacity/autoscaling/queue models**.
> Cloud changes scale/tooling, not utilization, queues, contention, latency propagation, or finite-resource laws.
> Tracking also means **performance regression gates in CI**, not only dashboards. Little's law still relates average arrivals/completions, latency and in-flight work for a stable service boundary.
