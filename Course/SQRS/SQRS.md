# SQRS — Software Quality & Reliability

Original questions from all eleven SQRBOK lecture revision-question sets, **L00–L10**, paired with locally synthesized self-check answers. Each lecture is separate for selective revision in Obsidian.

## Interactive deck

- [HTML flashcards](https://html-preview.github.io/?url=https://github.com/LocalT0aster/Notes/blob/master/Course/SQRS/flashcards.html) — search, lecture filters, shuffle, keyboard grading, and local review progress.

Rebuild it from the Markdown decks with the `uv` generator adapted from the repository's `sqrbok` branch:

```bash
uv run --script tools/build_flashcards.py --source .
uv run --script tools/test_build_flashcards.py
```

Restore question fronts verbatim from the checked-in source snapshots (offline):

```bash
uv run --script tools/sync_questions.py
```

Use `--fetch` to re-download the pinned source revision and verify exact heading anchors on the published pages. No fetching is needed to build, test or study offline. When upstream changes, review the source revision and mappings deliberately rather than rewriting questions by hand.

## Decks

- [L00 — Course Introduction & CI/CD](L00_Intro_CICD.md) — 15
- [L01 — Quality Models](L01_Quality_Models.md) — 18
- [L02 — Quality Measurement & Metrics](L02_Metrics.md) — 20
- [L03 — Verification Methods](L03_Verification.md) — 16
- [L04 — Adequacy Criteria / Coverage](L04_Coverage.md) — 32
- [L05 — Input Domain Testing](L05_Domain.md) — 26
- [L06 — Random Testing](L06_Random.md) — 34
- [L07 — Exploratory Testing & Operational Profiles](L07_Exploratory_OP.md) — 30
- [L08 — Software Reliability](L08_Reliability.md) — 15
- [L09 — Performance Analysis](L09_Performance.md) — 17
- [L10 — Security](L10_Security.md) — 13

**Total: 236 cards — one per original question.**

## Coverage and source version

Checked against SQRBOK revision questions and study notes at commit [`506d4f5`](https://github.com/sqrbok/sqrbok-preview/tree/506d4f5ba880cfb21311e12069510df5c2a71b80/content/material/sqr) on **2026-11-12**. The source course index lists L00–L10. This is lecture-revision coverage, not every page of the wider SQRBOK/QAM handbook.

The unmodified revision files and the security-question diagram are checked into [`sources/`](sources/README.md). [`source_manifest.json`](source_manifest.json) records their SHA-256 checksums, stable review IDs and exact published question anchors. Original question sections—including headings, scenarios, figures, subquestions, code and tables—are copied without paraphrasing. Only inter-question dividers are omitted.

The builder checks lecture coverage, counts, source checksums, **exact question-text equality**, stable IDs and exact source URLs before generating HTML. An edited or shortened front fails the build. Tests specifically cover L00 Q13's 37% premise, source-section boundaries, complete serialization and offline image embedding. These checks protect question fidelity; they do not establish the factual accuracy or completeness of locally authored answers.

The earlier 239-card deck paraphrased questions, split two source questions and included one supplemental question. It is replaced by 236 source-ordered questions. Split self-check answers are combined; the extra prevention/tolerance note is retained in [`Supplementary.md`](Supplementary.md). Retained questions keep their previous review IDs even where the displayed question number changed; three redundant/supplemental IDs are retired without clearing browser storage. Revised questions may deserve another review.

Source-label example: **`L00_Intro_CICD.md · Q13 · Review 5/15`**. **Q13** is the original question number; the linked label opens that exact question. **Review 5/15** is its position in the current filtered/shuffled queue, not its source number.

## Usage

Answer each card before opening its collapsed answer callout. Numerical cards include worked results; design/essay cards use a grading checklist so reasonable alternatives remain possible.

> [!note]
> These are study answers/cues synthesized from SQRBOK, not official model answers. For exact empirical figures, standards wording, or lecture-specific claims, use the source linked at the top of each deck.
