# SQRBOK — Software Quality & Reliability

Retake-focused integration of the [SQRBOK handbook](https://sqrbok.github.io/) into this notes vault.

## Study entry points

- [Interactive flashcards](flashcards.html) — shuffle, topic filters, keyboard grading, and local progress.
- [Generated Markdown deck](Flashcards.md) — plugin-free Obsidian cards with collapsible answers/source notes.
- [Anki import](flashcards.tsv) — generated tab-separated `Front / Back / Tags / Source` data.
- [Source manifest](source_manifest.json) — linked revision files and expected counts.
- `source/` — SQRBOK source repository when the submodule is initialized.

## Build / refresh

From the repository root:

```bash
bash Course/SQRBOK/sync.sh
```

This initializes/updates `sqrbok/sqrbok-preview` and regenerates all decks from every revision-question Markdown file it discovers. The parser also checks the current known snapshot: **423 cards across 20 linked revision files**. If upstream adds questions or files, they are included automatically and the count warning tells you the snapshot changed.

The generator is a self-contained `uv` script and declares Python `>=3.14`; `uv` provisions a compatible interpreter automatically. Run its regression tests with:

```bash
uv run --script Course/SQRBOK/tools/test_build_flashcards.py
```

## Flashcard philosophy

The original questions are mostly oral/explanatory exam prompts. The deck therefore keeps each original question intact rather than breaking it into trivia fragments. The back side uses, in priority order:

1. an official answer embedded in the SQRBOK revision page;
2. a model answer embedded in that page; or
3. the most relevant source-note sections from sibling SQRBOK Markdown files, selected by lexical relevance.

That third form is intentionally labelled **source notes**, not a definitive model answer. It reduces hallucination risk and makes the cards useful for active recall: answer aloud first, then reveal the source-grounded cues.

## Attribution

SQRBOK — Software Quality and Reliability Body of Knowledge, source: <https://github.com/sqrbok/sqrbok-preview>, live handbook: <https://sqrbok.github.io/>. The upstream project is licensed under **CC BY 4.0**. Generated/adapted study material in this folder preserves source links and attribution.
