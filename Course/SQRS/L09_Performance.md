# L09 — Performance Analysis Flashcards

**Source:** https://sqrbok.github.io/content/material/sqr/RQ_L09_PerformanceAnalysis.html

**Cards:** 17

> [!tip] Active recall
> Answer every part before revealing the answer. For design/essay questions, the answer is a grading checklist: alternative designs can also be correct when justified.

### Q1 — Business impact of latency

> [!question] Question
> A shop has 50k orders/day at $80; an $200k/year upgrade cuts latency by 800 ms. Can Google's 0.2–0.6% fewer searches after 100–400 ms delay predict the shop's revenue gain? What should it measure?

> [!answer]- Answer / self-check
> **No:** searches are not purchases, users and baselines differ, and the latency–conversion response need not be linear. The folklore “100 ms≈1% sales” is not a justified forecast. Measure the shop's own randomized/controlled change in conversion, revenue or contribution margin per visitor, tail latency and errors across representative traffic. Daily gross revenue is $4M, but the decision concerns **incremental benefit net of costs**, not a mechanically extrapolated percentage of gross revenue.

### Q2 — Performance engineering vs late testing

> [!question] Question
> Why are design-time performance fixes much cheaper than production discoveries?

> [!answer]- Answer / self-check
> Design review can change architecture before code/data/dependencies harden. Production fixes can require schema/service redesign, migrations, compatibility work, capacity, incident mitigation, and retesting. Example: chatty synchronous fan-out identified in architecture can become batching/async early; after launch it may require API redesign across services and clients.

### Q3 — Little's Law

> [!question] Question
> N=250 active connections, R=125ms. Compute throughput; then N at R=80ms with same X; then effect of 40% lower R.

> [!answer]- Answer / self-check
> Little's Law N=X·R. X=250/0.125 = **2000 req/s**. At 80 ms, N=2000×0.080 = **160**. A 40% reduction from 125 ms gives R=75 ms, so N=2000×0.075 = **150** concurrent requests at the same throughput.

### Q4 — Percentiles vs averages

> [!question] Question
> Two endpoints both average 500ms; A p50/90/99=450/550/600, B=100/200/8000. Interpret UX and SLA p99<1000.

> [!answer]- Answer / self-check
> Most users see **B** as faster (p50/p90 far lower), but **B violates the p99 SLA badly** and has extreme tail latency; A is consistent and meets it. Reporting p90 instead of mean would prioritize B's common-case experience, which is why multiple percentiles—especially the SLO percentile—must be monitored.

### Q5 — Hockey-stick performance curve

> [!question] Question
> Explain utilization U, throughput X, and response time R across light, heavy, and buckle zones; what does faster CPU do?

> [!answer]- Answer / self-check
> - **Light load:** U rises, X rises roughly linearly, R near baseline.
> - **Heavy load:** U approaches saturation, X gains slow, queues grow, R rises sharply.
> - **Buckle/retrograde:** contention/coherency causes X to flatten or fall while R explodes.
> A faster CPU shifts the saturation/buckle point right/up, but cannot remove non-CPU bottlenecks or coordination limits.

### Q6 — Amdahl optimization

> [!question] Question
> 45% DB sped 3×; compute speedup, max if DB infinite, and combined with 20% network sped 2×.

> [!answer]- Answer / self-check
> DB only: S=1/(0.55+0.45/3)=1/0.70=**1.43×**. Infinite DB speed: 1/0.55=**1.82×** max. DB 3× + network 2×: new fraction=0.45/3+0.35+0.20/2=0.60 → **1.67×**.

### Q7 — Amdahl vs Gustafson

> [!question] Question
> 10 min serial loading + 50 min parallel training on 1 GPU. What happens with 10 GPUs and which law fits scale-up?

> [!answer]- Answer / self-check
> Fixed problem (Amdahl): 10 + 50/10 = **15 min** idealized. Gustafson view: keep the 60-min wall-clock budget; after 10 min serial work, 10 GPUs provide **500 GPU-min** of parallel training—roughly a 10× larger parallel workload. Use Amdahl for fixed-size speedup; Gustafson when the problem grows with resources.
> The enlarged workload takes **510 minutes on one GPU**, so scaled speedup is **510/60=8.5×**, equivalently 10−9×(10/60). The model assumes the serial loading cost stays fixed.

### Q8 — USL and retrograde throughput

> [!question] Question
> Throughput rises to 8 instances then falls at 16/32. Which USL term is implicated and what should change?

> [!answer]- Answer / self-check
> A decline after a peak is the signature of **coherency/coordination cost β**, not just contention α. More replicas amplify shared-state synchronization, cache invalidation, locks, broadcasts, or cross-node coordination. Reduce shared/coherent state: partition/shard, decentralize coordination, batch, cache, or redesign the bottleneck. Adding instances alone worsens βN(N−1).

### Q9 — Performance anti-patterns

> [!question] Question
> Identify and fix three scenarios: 100 per-user DB calls, giant OrderService, per-request DB connection construction.

> [!answer]- Answer / self-check
> - 1 + 100 queries → **N+1 query / chatty I/O**; fix with join/batch/prefetch.
> - One service owns unrelated critical work → **god service / serialized bottleneck**; split or isolate queues/resources, use async boundaries.
> - Create/destroy connections per request → **resource churn/no pooling**; use connection pooling/reuse and bounded lifecycle.
> For the source's controller that fetches price/discount/stock for 20 items (**60 calls**), the **God Class** remedy is to put behavior next to its data: call **`cart.total()` once** and let cart/items do their work. That does not magically remove all internal work; it removes controller-level chat and misplaced responsibilities.

### Q10 — How performance bugs are discovered

> [!question] Question
> Why does profiling find only a small share of performance bugs, and what finds more?

> [!answer]- Answer / self-check
> Profilers expose where time/resources are spent **under the exercised workload**; they do not tell you that the workload model/API usage/architecture is conceptually wrong. The lecture cites many bugs from misunderstanding workload/API (~67%) and only ~5–10% discovered by profiling, while **code review/inspection** finds a much larger share (~33–57%). Review performance assumptions and API complexity explicitly.

### Q11 — Ticket-sale performance test strategy

> [!question] Question
> Design testing for 5k normal users and a 200k-user 60s spike.

> [!answer]- Answer / self-check
> Sequence a **baseline/smoke → load at 5k → spike to 200k → stress beyond expected peak → scalability/capacity tests → soak/endurance** at sustained realistic traffic. Monitor p50/p95/p99 latency, throughput, errors, saturation (CPU/memory/DB/queues), retries/timeouts, GC, cache hit, dependency SLOs. Realism includes arrival burst shape, transaction mix, think time, hot inventory, auth/payment dependencies.
> The lecture's six named types are **baseline, smoke, load, stress, soak, isolation**; spike is a stress variant, isolation diagnoses one repeated transaction. Write agreed targets, e.g. purchase p99<2 s and failed purchases<0.1% at the specified arrival/peak profile. Model the two-hour sale and recovery, not just the peak count. Skipping stress hides collapse/recovery behavior; skipping soak hides leaks/exhaustion.

### Q12 — Tail-latency amplification

> [!question] Question
> 80 shards; each has 0.5% slow probability. Compute query slow probability and tied-request effect.

> [!answer]- Answer / self-check
> At least one slow shard: 1−0.995^80 ≈ **33.0%**. If two independent replicas are raced for every subrequest, both slow probability = 0.005² = **0.0025%**; across 80, ≈ **0.20%** chance at least one remains slow. Full tied requests roughly **double subrequest traffic**. True hedging sends a backup only after a tail threshold, so overhead is near the fraction exceeding that threshold, not 100%.
> Sending a backup after the expected **p95** latency affects about **5%** of originals, so extra requests are about 5%, assuming that latency distribution remains valid. Correlation or overload weakens the independent-copy calculation.

### Q13 — Per-service latency budget

> [!question] Question
> End-to-end p99 budget 400ms; current 30+280+50=360. Can recommendation rise to 350ms?

> [!answer]- Answer / self-check
> Allocate budgets that sum to ≤400 with contingency, e.g. Gateway 40–50, Recommendation ~290–300, DB 50–60 ms. If Recommendation rises 280→350 with others unchanged, end-to-end ≈ **430 ms**, violating the SLO. Approve only if other components improve or the model's value justifies renegotiating the SLO/risk; latency budget is finite like an error budget.
> Summing marginal p99s is a **budgeting approximation, not the chain's measured p99 or a guarantee**: the slowest 1% need not be the same requests, and correlation changes the sum's distribution. Verify end-to-end percentiles on traces under representative load before approval.

### Q14 — Classical PE → cloud-native

> [!question] Question
> Map classical performance-engineering concepts to cloud-native practice and explain “physics hasn't changed.”

> [!answer]- Answer / self-check
> - Component performance budget → **per-service latency/resource SLO budget**.
> - Budget tracking → **observability, dashboards, SLO/burn monitoring**.
> - Explicit risk acceptance → **error/performance budgets**.
> - Planned PE effort → **continuous performance engineering/capacity work**.
> - Queueing models → **capacity/autoscaling/queue models**.
> Cloud changes scale/tooling, not utilization, queues, contention, latency propagation, or finite-resource laws.
> Tracking also means **performance regression gates in CI**, not only dashboards. Little's law still relates average arrivals/completions, latency and in-flight work for a stable service boundary.

### Q15 — Average equal-work rates

> [!question] Question
> Equal-work benchmark runs reach 40 and 60 requests/s. What is their combined average, and when is 50 correct?

> [!answer]- Answer / self-check
> Let each run process W requests. Total rate = 2W/(W/40+W/60) = **48 requests/s**, the harmonic mean. **50** is correct for runs of **equal duration**, where the faster run completes more work. Choose the mean from total work / total elapsed time, not from habit.

### Q16 — Design-time performance budgets

> [!question] Question
> What does a performance budget allocate, how is it tracked, and why is load testing alone insufficient?

> [!answer]- Answer / self-check
> Allocate the end-to-end response-time/resource target among components, with headroom. Measure/model each component during development and fail meaningful performance regression gates when budgets are exceeded. Discovering a costly interaction while design can change is cheaper than waiting for an integrated load test to expose an architectural bottleneck. Budgeting complements realistic load testing; it does not replace it.

### Q17 — Rising latency during a soak test

> [!question] Question
> At constant load, latency climbs steadily for four hours. What do you suspect and inspect next?

> [!answer]- Answer / self-check
> Suspect accumulating state or resource exhaustion: memory/connection/thread leaks, unbounded caches/queues or garbage-collection pressure. Correlate latency with heap/RSS, allocation/GC, open handles/connections, queue depth, database locks and throughput; confirm the arrival mix actually stayed stable. A trend is evidence to investigate, not proof of a memory leak.
