#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.14"
# dependencies = ["markdown-it-py>=4.0.0,<5.0.0"]
# ///
"""Copy pinned upstream question sections into the Markdown decks verbatim.

Self-check answers remain locally authored. Normal synchronization is offline;
--fetch downloads the revision sources at the manifest's immutable commit.
"""

from __future__ import annotations

import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.request import urlopen

import build_flashcards as builder


class QuestionAnchors(HTMLParser):
    """Read the published heading IDs instead of guessing a slug algorithm."""

    def __init__(self) -> None:
        super().__init__()
        self.anchors: dict[int, str] = {}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag not in {"h2", "h3", "h4", "h5", "h6"}:
            return
        identity = dict(attrs).get("id", "") or ""
        match = re.match(r"^(?:question-|q)(\d+)(?:-|$)", identity)
        if match:
            number = int(match[1])
            if number in self.anchors:
                raise ValueError(f"Duplicate source question anchor: {identity}")
            self.anchors[number] = identity


def quote_callout(text: str) -> str:
    return "\n".join("> " + line if line else ">" for line in text.split("\n"))


def synchronize(root: Path, fetch: bool = False) -> None:
    manifest_path = root / "source_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    snapshots = root / "sources"
    snapshots.mkdir(exist_ok=True)
    base = f"https://raw.githubusercontent.com/sqrbok/sqrbok-preview/{manifest['source_version']}/content/material/sqr/"
    rendered: dict[Path, str] = {}
    supplementary: list[builder.Card] = []
    assets: set[str] = set()
    for deck in manifest["decks"]:
        snapshot = snapshots / deck["revision_file"]
        raw = urlopen(base + deck["revision_file"], timeout=30).read() if fetch else snapshot.read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        if deck.get("source_sha256", digest) != digest:
            raise ValueError(f"{snapshot.name}: fetched source differs from pinned snapshot")
        text = raw.decode("utf-8")
        originals = builder.parse_original_questions(text)
        if len(originals) != len(deck["question_cards"]):
            raise ValueError(f"{snapshot.name}: review mappings before accepting changed question counts")
        source_url = f"https://sqrbok.github.io/content/material/sqr/{snapshot.stem}.html"
        if fetch:
            parser = QuestionAnchors()
            parser.feed(urlopen(source_url, timeout=30).read().decode("utf-8"))
            if sorted(parser.anchors) != [question.number for question in originals]:
                raise ValueError(f"{source_url}: published question numbering differs from pinned source")
            anchors = [parser.anchors[question.number] for question in originals]
        else:
            anchors = deck["question_anchors"]
        for name in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text):
            if name != Path(name).name or not name.endswith(".svg"):
                raise ValueError(f"Unsupported source image: {name}")
            assets.add(name)

        path = root / deck["path"]
        previous = builder.parse_deck(path, root)
        used = {number for numbers in deck["question_cards"] for number in numbers}
        supplementary.extend(card for number, card in enumerate(previous, 1) if number not in used)
        topic = previous[0].topic
        study_file = "SN" + deck["revision_file"][2:]
        lines = [
            f"# {topic} Flashcards", "",
            f"**Source:** {source_url}", "",
            f"**Study notes:** https://sqrbok.github.io/content/material/sqr/{Path(study_file).stem}.html", "",
            f"**Cards:** {len(originals)}", "",
            "> [!tip] Active recall",
            "> Questions are copied verbatim from the pinned SQRBOK source. Answers are locally synthesized self-checks, not official model answers.", "",
        ]
        ids: list[str] = []
        for original, mapped in zip(originals, deck["question_cards"], strict=True):
            answers = [previous[number - 1] for number in mapped]
            identity = answers[0].id
            ids.append(identity)
            answer = "\n\n".join(card.answer for card in answers)
            lines.extend([
                f"### Q{original.number} — {original.title}", "",
                f"**Card ID:** {identity}", "",
                f"**Source question:** {source_url}#{anchors[original.number - 1]}", "",
                builder.QUESTION_MARKER, quote_callout(original.prompt), "",
                "> [!answer]- Answer / self-check", quote_callout(answer), "",
            ])
        rendered[path] = "\n".join(lines).rstrip() + "\n"
        deck.update({
            "cards": len(originals), "source_sha256": digest, "card_ids": ids,
            "question_anchors": anchors,
            "question_cards": [[question.number] for question in originals],
        })
        rendered[snapshot] = text

    asset_hashes: dict[str, str] = {}
    asset_data: dict[Path, bytes] = {}
    for name in sorted(assets):
        asset = snapshots / name
        raw = urlopen(base + name, timeout=30).read() if fetch else asset.read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        if manifest.get("assets", {}).get(name, digest) != digest:
            raise ValueError(f"{name}: fetched asset differs from pinned snapshot")
        asset_hashes[name] = digest
        asset_data[asset] = raw
    manifest["assets"] = asset_hashes
    manifest["scope"] = "One verbatim card per SQR L00–L10 revision question; answers are local synthesized self-checks, not official answers."
    rendered[manifest_path] = json.dumps(manifest, indent=2, ensure_ascii=False) + "\n"
    if supplementary:
        lines = ["# Supplementary SQRS self-checks", "", "Locally authored material without a corresponding original revision question; not included in the source-question deck.", ""]
        for card in supplementary:
            lines.extend([f"## {card.topic}: {card.label}", "", card.prompt, "", card.answer, ""])
        rendered[root / "Supplementary.md"] = "\n".join(lines)
    for path, contents in rendered.items():
        path.write_text(contents, encoding="utf-8")
    for path, contents in asset_data.items():
        path.write_bytes(contents)
    cards = builder.build_cards(root)
    builder.write_static_html(cards, root / "flashcards.html", root)
    print(f"Synchronized {len(cards)} verbatim questions across {len(manifest['decks'])} lectures")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--fetch", action="store_true", help="Fetch sources at the pinned manifest commit")
    args = parser.parse_args()
    synchronize(args.source.resolve(), args.fetch)


if __name__ == "__main__":
    main()
