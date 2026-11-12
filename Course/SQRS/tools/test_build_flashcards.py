#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.14"
# dependencies = ["markdown-it-py>=4.0.0,<5.0.0"]
# ///
"""Check lecture coverage and completeness before publishing the SQRS deck."""

import json
from pathlib import Path
import tempfile
import unittest

import build_flashcards as builder

ROOT = Path(__file__).resolve().parents[1]


class CourseCoverageTest(unittest.TestCase):
    def test_all_lectures_have_complete_cards(self) -> None:
        cards = builder.build_cards(ROOT)
        self.assertEqual({f"L{i:02d}" for i in range(11)}, {c.source_path[:3] for c in cards})
        self.assertEqual(len(cards), len({c.id for c in cards}))
        for card in cards:
            self.assertTrue(card.prompt.strip(), card.id)
            self.assertTrue(card.answer.strip(), card.id)

    def test_missing_lecture_is_rejected(self) -> None:
        cards = builder.build_cards(ROOT)
        with self.assertRaisesRegex(ValueError, "L00_Intro_CICD"):
            builder.validate_coverage(ROOT, [c for c in cards if not c.source_path.startswith("L00_")])

    def test_missing_question_is_rejected(self) -> None:
        cards = builder.build_cards(ROOT)
        with self.assertRaisesRegex(ValueError, "L02_Metrics"):
            builder.validate_coverage(ROOT, [c for c in cards if c.id != "l02-metrics-020"])

    def test_html_contains_every_card_and_preserves_progress_ids(self) -> None:
        cards = builder.build_cards(ROOT)
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "flashcards.html"
            builder.write_static_html(cards, output)
            html = output.read_text(encoding="utf-8")
        payload = json.loads(html.split("const cards=", 1)[1].split(";\nconst KEY=", 1)[0])
        self.assertEqual([c.id for c in cards], [c["id"] for c in payload])
        self.assertIn("sqrs-progress-v1", html)
        self.assertIn("l01-quality-models-001", {c["id"] for c in payload})
        intro = [c for c in payload if c["source_path"].startswith("L00_")]
        self.assertEqual(15, len(intro))
        self.assertIn("<strong>", intro[0]["answer_html"])


if __name__ == "__main__":
    unittest.main()
