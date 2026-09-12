#!/usr/bin/env python3
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
