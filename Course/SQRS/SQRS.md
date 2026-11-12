# SQRS — Software Quality & Reliability

Flashcards synthesized from all eleven SQRBOK lecture revision-question sets, **L00–L10**. Each lecture is separate for selective revision in Obsidian.

## Interactive deck

- [HTML flashcards](https://html-preview.github.io/?url=https://github.com/LocalT0aster/Notes/blob/master/Course/SQRS/flashcards.html) — search, lecture filters, shuffle, keyboard grading, and local review progress.

Rebuild it from the Markdown decks with the `uv` generator adapted from the repository's `sqrbok` branch:

```bash
uv run --script tools/build_flashcards.py --source .
uv run --script tools/test_build_flashcards.py
```

## Decks

- [L00 — Course Introduction & CI/CD](L00_Intro_CICD.md) — 15
- [L01 — Quality Models](L01_Quality_Models.md) — 18
- [L02 — Quality Measurement & Metrics](L02_Metrics.md) — 20
- [L03 — Verification Methods](L03_Verification.md) — 16
- [L04 — Adequacy Criteria / Coverage](L04_Coverage.md) — 32
- [L05 — Input Domain Testing](L05_Domain.md) — 26
- [L06 — Random Testing](L06_Random.md) — 34
- [L07 — Exploratory Testing & Operational Profiles](L07_Exploratory_OP.md) — 30
- [L08 — Software Reliability](L08_Reliability.md) — 17
- [L09 — Performance Analysis](L09_Performance.md) — 17
- [L10 — Security](L10_Security.md) — 14

**Total: 239 cards.**

## Coverage and source version

Checked against SQRBOK revision questions and study notes at commit [`506d4f5`](https://github.com/sqrbok/sqrbok-preview/tree/506d4f5ba880cfb21311e12069510df5c2a71b80/content/material/sqr) on **2026-11-12**. The source course index lists L00–L10. This is lecture-revision coverage, not every page of the wider SQRBOK/QAM handbook.

[`source_manifest.json`](source_manifest.json) records each revision set and its question-to-local-card mapping: entry 1 in `question_cards` maps upstream Q1, entry 2 maps upstream Q2, and so on. Existing local card numbers/IDs are retained; they need not match upstream question numbers after upstream revisions. Some source questions span multiple cards, and the deck retains an additional prevention/tolerance card. The 236 upstream questions are represented by 239 local cards.

The builder checks every expected lecture, parsed/declared card counts, consecutive local numbering and valid mappings before generating HTML. The tests check L00 inclusion and complete HTML serialization. These are structural checks; they do not verify the factual accuracy or completeness of an answer. When upstream changes, compare both the question text and the linked study notes before updating the mapping—equal counts alone can hide changed topics.

The November coverage repair adds L00, supplements six other lecture decks and revises L06's guided-testing/seed questions. It also updates stale examples such as the test-pyramid ratios, N-version failure figures and CVSS calculations. Existing browser review records remain attached to their card IDs; revised cards may deserve another review.

## Usage

Answer each card before opening its collapsed answer callout. Numerical cards include worked results; design/essay cards use a grading checklist so reasonable alternatives remain possible.

> [!note]
> These are study answers/cues synthesized from SQRBOK, not official model answers. For exact empirical figures, standards wording, or lecture-specific claims, use the source linked at the top of each deck.
