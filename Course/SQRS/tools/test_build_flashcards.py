#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.14"
# dependencies = ["markdown-it-py>=4.0.0,<5.0.0"]
# ///
"""Check lecture coverage and completeness before publishing the SQRS deck."""

import json
from dataclasses import replace
from pathlib import Path
import tempfile
import unittest

import build_flashcards as builder

ROOT = Path(__file__).resolve().parents[1]


class CourseCoverageTest(unittest.TestCase):
    def test_coverage_question_keeps_original_premise_and_subquestions(self) -> None:
        card = next(c for c in builder.build_cards(ROOT) if c.id == "l00-intro-cicd-013")
        self.assertEqual(
            "## Question 13: Coverage\n\n"
            "A coverage report shows 37% statement coverage.\n\n"
            "1. What does the remaining 63% tell you about the code?\n"
            "2. Give two reasons why 100% statement coverage still does not show the code is correct.",
            card.prompt,
        )

    def test_all_lectures_have_complete_cards(self) -> None:
        cards = builder.build_cards(ROOT)
        self.assertEqual(236, len(cards))
        self.assertEqual({f"L{i:02d}" for i in range(11)}, {c.source_path[:3] for c in cards})
        self.assertEqual(len(cards), len({c.id for c in cards}))
        for card in cards:
            self.assertTrue(card.prompt.strip(), card.id)
            self.assertTrue(card.answer.strip(), card.id)

    def test_paraphrased_question_is_rejected(self) -> None:
        cards = builder.build_cards(ROOT)
        changed = [
            replace(card, prompt="What does the other 63% mean?")
            if card.id == "l00-intro-cicd-013" else card
            for card in cards
        ]
        with self.assertRaisesRegex(ValueError, "Q13 differs from the original"):
            builder.validate_fidelity(ROOT, changed)

    def test_coverage_source_link_points_to_exact_question(self) -> None:
        card = next(c for c in builder.build_cards(ROOT) if c.id == "l00-intro-cicd-013")
        self.assertEqual(13, card.question_number)
        self.assertEqual(
            "https://sqrbok.github.io/content/material/sqr/RQ_L00_Intro_CICD.html#question-13-coverage",
            card.source_url,
        )

    def test_source_parser_keeps_tables_and_code_but_not_later_sections(self) -> None:
        text = (
            "## Question 1: Example\n\nRead this scenario.\n\n"
            "| Input | Output |\n|---|---|\n| 1 | 2 |\n\n"
            "```text\n## Question 99: Not a question\n```\n\n"
            "1. Explain the result.\n\n---\n\n## Topics Covered\n\nNot a prompt.\n"
        )
        questions = builder.parse_original_questions(text)
        self.assertEqual(1, len(questions))
        self.assertEqual(text.split("\n\n---", 1)[0], questions[0].prompt)

    def test_html_keeps_subscripts_and_escapes_other_source_html(self) -> None:
        rendered = builder.markdown_to_html("R<sub>c</sub> <script>alert(1)</script>")
        self.assertIn("R<sub>c</sub>", rendered)
        self.assertNotIn("<script>", rendered)

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
        self.assertEqual([c.prompt for c in cards], [c["prompt"] for c in payload])
        self.assertIn("sqrs-progress-v1", html)
        self.assertIn("l01-quality-models-001", {c["id"] for c in payload})
        intro = [c for c in payload if c["source_path"].startswith("L00_")]
        self.assertEqual(15, len(intro))
        self.assertIn("<strong>", intro[0]["answer_html"])
        diagram = next(c for c in payload if c["source_path"].startswith("L10_") and c["question_number"] == 6)
        self.assertIn("data:image/svg+xml;base64,", diagram["prompt_html"])


if __name__ == "__main__":
    unittest.main()
