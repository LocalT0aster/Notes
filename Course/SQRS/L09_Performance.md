# L09 — Performance Analysis Flashcards

**Source:** https://sqrbok.github.io//content/material/sqr/RQ_L09_PerformanceAnalysis.html

**Cards:** 14

> [!tip] Active recall
> Answer every part before revealing the answer. For design/essay questions, the answer is a grading checklist: alternative designs can also be correct when justified.

### Q1 — Business impact of latency

> [!question] Question
> 50k orders/day at $80; latency improves 1.2s→0.4s for $200k/year. Use 100ms≈1% sales and critique the estimate.

> [!answer]- Answer / self-check
> Daily revenue = 50,000×$80 = $4M; annual ≈ **$1.46B**. 800 ms = eight 100-ms steps → heuristic **8%** uplift ≈ **$116.8M/year**, dwarfing $200k. But the heuristic is not causal/universal: conversion response may be nonlinear, baseline differs, order count may already include lost demand, seasonality/confounders matter, and infrastructure may affect more than latency.

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

### Q12 — Tail-latency amplification

> [!question] Question
> 80 shards; each has 0.5% slow probability. Compute query slow probability and tied-request effect.

> [!answer]- Answer / self-check
> At least one slow shard: 1−0.995^80 ≈ **33.0%**. If two independent replicas are raced for every subrequest, both slow probability = 0.005² = **0.0025%**; across 80, ≈ **0.20%** chance at least one remains slow. Full tied requests roughly **double subrequest traffic**. True hedging sends a backup only after a tail threshold, so overhead is near the fraction exceeding that threshold, not 100%.

### Q13 — Per-service latency budget

> [!question] Question
> End-to-end p99 budget 400ms; current 30+280+50=360. Can recommendation rise to 350ms?

> [!answer]- Answer / self-check
> Allocate budgets that sum to ≤400 with contingency, e.g. Gateway 40–50, Recommendation ~290–300, DB 50–60 ms. If Recommendation rises 280→350 with others unchanged, end-to-end ≈ **430 ms**, violating the SLO. Approve only if other components improve or the model's value justifies renegotiating the SLO/risk; latency budget is finite like an error budget.

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
