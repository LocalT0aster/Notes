#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.14"
# dependencies = [
#   "markdown-it-py>=4.0.0,<5.0.0",
# ]
# ///
"""Regression tests for SQRBOK revision-question extraction."""

from __future__ import annotations

import unittest
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import build_flashcards as builder


SQRBOK_ROOT = HERE.parent
SOURCE = SQRBOK_ROOT / "source"
MANIFEST = SQRBOK_ROOT / "source_manifest.json"


class RevisionQuestionExtractionTest(unittest.TestCase):
    def test_markdown_renderer_handles_source_blocks_safely(self) -> None:
        rendered = builder.markdownish_to_html(
            "#### Quality views\n\n"
            "| View | Meaning |\n"
            "| --- | --- |\n"
            "| **User** | `fit for purpose` |\n\n"
            "- first point\n"
            "- [source link](https://sqrbok.github.io/)\n\n"
            "```text\nexample\n```\n\n"
            "<script>alert('unsafe')</script>"
        )

        self.assertIn("<h4>Quality views</h4>", rendered)
        self.assertIn("<table>", rendered)
        self.assertIn("<strong>User</strong>", rendered)
        self.assertIn("<code>fit for purpose</code>", rendered)
        self.assertIn("<ul>", rendered)
        self.assertIn('<a href="https://sqrbok.github.io/">source link</a>', rendered)
        self.assertIn("<pre><code", rendered)
        self.assertIn("&lt;script&gt;", rendered)
        self.assertNotIn("<script>", rendered)

    def test_manifest_snapshot_counts(self) -> None:
        """Every numbered/heading question in the pinned source becomes a card."""
        manifest, specs = builder.read_manifest(MANIFEST)
        files = builder.discover_revision_files(SOURCE, specs)
        cards, counts = builder.build_cards(SOURCE, files)

        self.assertEqual(manifest["expected_total_questions"], len(cards))
        self.assertEqual(
            {path: spec.expected for path, spec in specs.items() if spec.expected is not None},
            counts,
        )

    def test_directive_style_numbered_questions_are_retained(self) -> None:
        cases = [
            "Given this specification, identify relevant aspects and classes.",
            "Apply the PDCA cycle to reduce bug escape rate.",
            "Build a classification tree for an ATM withdrawal function.",
            "You have an abstract test specification. Provide valid concrete cases.",
            "For each filter, describe one mitigation strategy.",
        ]

        for prompt in cases:
            with self.subTest(prompt=prompt):
                self.assertTrue(builder.looks_like_question(prompt))


if __name__ == "__main__":
    unittest.main()
