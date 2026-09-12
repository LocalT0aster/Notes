#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.14"
# dependencies = [
#   "markdown-it-py>=4.0.0,<5.0.0",
# ]
# ///
"""Build SQRBOK flashcards from the upstream Markdown sources.

The builder intentionally does not synthesize authoritative answers.  It uses
embedded official/model answers when present and otherwise retrieves nearby
SQRBOK source-note sections as active-recall cues.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Sequence

from markdown_it import MarkdownIt

GITHUB_BASE = "https://github.com/sqrbok/sqrbok-preview/blob/main/"
SITE_BASE = "https://sqrbok.github.io/"
QUESTION_HEADING_RE = re.compile(
    r"^(?P<marks>#{2,6})\s+(?P<label>(?:Question\s*\d+|Q\s*\d+)\b.*)$",
    re.IGNORECASE,
)
HEADING_RE = re.compile(r"^(?P<marks>#{1,6})\s+(?P<title>.+?)\s*$")
NUMBERED_RE = re.compile(r"^(?P<indent>\s*)(?P<num>\d+)\.\s+(?P<text>\S.*)$")
FRONTMATTER_RE = re.compile(r"\A---\s*\n.*?\n---\s*(?:\n|\Z)", re.DOTALL)
DETAILS_RE = re.compile(
    r"<details(?:\s+[^>]*)?>\s*<summary>\s*Answer\s*</summary>(?P<body>.*?)</details>",
    re.IGNORECASE | re.DOTALL,
)
MODEL_ANSWER_RE = re.compile(r"\*\*Model Answer:\*\*\s*(?P<body>.*)", re.IGNORECASE | re.DOTALL)
CITE_RE = re.compile(r"\{%\s*(?:cite|bibliography)\b.*?%\}", re.IGNORECASE)
HTML_TAG_RE = re.compile(r"</?(?:details|summary)(?:\s+[^>]*)?>", re.IGNORECASE)
TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9_-]{2,}")
MARKDOWN_RENDERER = MarkdownIt("commonmark", {"html": False}).enable("table")

STOPWORDS = {
    "the", "and", "for", "that", "this", "with", "from", "into", "are", "was", "were",
    "what", "when", "where", "which", "why", "how", "can", "could", "should", "would", "will",
    "you", "your", "their", "they", "them", "then", "than", "has", "have", "had", "its", "not",
    "use", "using", "used", "about", "between", "each", "give", "explain", "describe", "define",
    "example", "examples", "software", "quality", "question", "questions", "following", "does",
    "also", "only", "more", "most", "such", "some", "any", "all", "one", "two", "three", "why",
}


@dataclass(frozen=True)
class RevisionSpec:
    path: str
    topic: str
    expected: int | None = None


@dataclass(frozen=True)
class NoteSection:
    title: str
    body: str
    source_path: str


@dataclass
class Card:
    id: str
    topic: str
    section: str
    label: str
    prompt: str
    answer: str
    answer_kind: str
    source_path: str
    source_url: str
    github_url: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True, help="sqrbok-preview checkout")
    parser.add_argument("--manifest", type=Path, required=True, help="source_manifest.json")
    parser.add_argument("--output-dir", type=Path, required=True, help="output directory")
    return parser.parse_args()


def read_manifest(path: Path) -> tuple[dict, dict[str, RevisionSpec]]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    specs = {
        item["path"]: RevisionSpec(item["path"], item.get("topic", stem_topic(item["path"])), item.get("expected"))
        for item in raw.get("revision_files", [])
    }
    return raw, specs


def stem_topic(relative_path: str) -> str:
    stem = Path(relative_path).stem
    stem = re.sub(r"^RQ[-_]?(?:[AL]\d+[-_]?)?", "", stem, flags=re.IGNORECASE)
    return re.sub(r"[-_]+", " ", stem).strip().title() or Path(relative_path).stem


def discover_revision_files(source: Path, specs: dict[str, RevisionSpec]) -> list[tuple[Path, RevisionSpec]]:
    content = source / "content"
    discovered: dict[str, Path] = {}
    for file in content.rglob("*.md"):
        rel = file.relative_to(source).as_posix()
        if file.name.lower().startswith("rq"):
            discovered[rel] = file
            continue
        head = file.read_text(encoding="utf-8", errors="replace")[:5000]
        if re.search(r"(?im)^(?:title:\s*[\"\']?.*revision\s+questions|#\s+.*revision\s+questions)", head):
            discovered[rel] = file

    # Preserve the handbook/manifest ordering first, then include newly added RQ pages.
    ordered_paths = [p for p in specs if p in discovered]
    ordered_paths.extend(sorted(p for p in discovered if p not in specs))
    return [(discovered[p], specs.get(p, RevisionSpec(p, stem_topic(p)))) for p in ordered_paths]


def strip_frontmatter(text: str) -> str:
    return FRONTMATTER_RE.sub("", text, count=1)


def clean_markdown(text: str) -> str:
    text = CITE_RE.sub("", text)
    text = HTML_TAG_RE.sub("", text)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = re.sub(r"(?m)^\s*---+\s*$", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def clean_prompt(text: str) -> str:
    text = DETAILS_RE.sub("", text)
    text = MODEL_ANSWER_RE.sub("", text)
    return clean_markdown(text)


def extract_embedded_answer(block: str) -> tuple[str | None, str | None]:
    details = DETAILS_RE.search(block)
    if details:
        return clean_markdown(details.group("body")), "official answer"
    model = MODEL_ANSWER_RE.search(block)
    if model:
        return clean_markdown(model.group("body")), "model answer"
    return None, None


def current_section(lines: Sequence[str], index: int) -> str:
    for i in range(index - 1, -1, -1):
        m = HEADING_RE.match(lines[i])
        if m and not QUESTION_HEADING_RE.match(lines[i]):
            title = clean_markdown(m.group("title"))
            if not re.match(r"^(?:practice\s+questions|sample\s+exam\s+questions)", title, re.IGNORECASE):
                return title
    return "Revision Questions"


def heading_cards(text: str) -> tuple[list[tuple[str, str, str, str | None, str | None]], set[int]]:
    """Return label, section, prompt, answer, answer-kind plus consumed line indexes."""
    lines = strip_frontmatter(text).splitlines()
    hits: list[tuple[int, re.Match[str]]] = []
    for i, line in enumerate(lines):
        match = QUESTION_HEADING_RE.match(line)
        if match:
            hits.append((i, match))

    cards: list[tuple[str, str, str, str | None, str | None]] = []
    consumed: set[int] = set()
    for hit_index, (start, match) in enumerate(hits):
        level = len(match.group("marks"))
        stop = len(lines)
        for j in range(start + 1, len(lines)):
            h = HEADING_RE.match(lines[j])
            if not h:
                continue
            if QUESTION_HEADING_RE.match(lines[j]):
                stop = j
                break
            if len(h.group("marks")) <= level:
                stop = j
                break

        label = clean_markdown(match.group("label"))
        block = "\n".join(lines[start + 1 : stop]).strip()
        answer, answer_kind = extract_embedded_answer(block)
        prompt_body = clean_prompt(block)

        # Sample-exam pages commonly put the actual prompt in italics on the line after
        # a generic "Question N" heading.  Keep both where the heading itself is descriptive.
        if re.fullmatch(r"(?:Question\s*\d+|Q\s*\d+)", label, re.IGNORECASE):
            prompt = prompt_body
        elif prompt_body:
            prompt = f"**{label}**\n\n{prompt_body}"
        else:
            prompt = label

        if prompt.strip():
            cards.append((label, current_section(lines, start), prompt.strip(), answer, answer_kind))
            consumed.update(range(start, stop))
    return cards, consumed


def looks_like_question(text: str) -> bool:
    s = clean_markdown(text).strip()
    if not s:
        return False
    if "?" in s:
        return True
    return bool(
        re.match(
            r"^(?:define|explain|describe|compare|contrast|calculate|compute|derive|identify|list|name|discuss|"
            r"give|provide|state|why|what|when|where|which|how|consider|suppose|assume|show|outline|interpret|"
            r"apply|build|given|you\s+have|for\s+each)\b",
            re.sub(r"^[*_`\s]+", "", s),
            re.IGNORECASE,
        )
    )


def numbered_cards(
    text: str, consumed: set[int]
) -> list[tuple[str, str, str, str | None, str | None]]:
    """Parse top-level numbered question lists used by Classification Tree / Process pages."""
    lines = strip_frontmatter(text).splitlines()
    cards: list[tuple[str, str, str, str | None, str | None]] = []
    i = 0
    while i < len(lines):
        if i in consumed:
            i += 1
            continue
        m = NUMBERED_RE.match(lines[i])
        if not m or m.group("indent"):
            i += 1
            continue

        section = current_section(lines, i)
        # Avoid treating bibliography, glossary and ordinary numbered prose as cards.
        if re.search(r"(?:reference|bibliograph|glossar|key\s+number|learning\s+objective|contents?)", section, re.I):
            i += 1
            continue

        start = i
        parts = [m.group("text")]
        i += 1
        while i < len(lines):
            if i in consumed:
                break
            if NUMBERED_RE.match(lines[i]) and not NUMBERED_RE.match(lines[i]).group("indent"):
                break
            h = HEADING_RE.match(lines[i])
            if h and len(h.group("marks")) <= 3:
                break
            # Preserve sub-bullets, formulae and wrapped prompt lines.
            parts.append(lines[i])
            i += 1

        raw = "\n".join(parts).strip()
        answer, answer_kind = extract_embedded_answer(raw)
        prompt = clean_prompt(raw)
        if looks_like_question(prompt):
            label = f"Q{m.group('num')}"
            cards.append((label, section, prompt, answer, answer_kind))
        if i == start:
            i += 1
    return cards


def parse_revision_questions(text: str) -> list[tuple[str, str, str, str | None, str | None]]:
    headings, consumed = heading_cards(text)
    numbered = numbered_cards(text, consumed)
    return headings + numbered


def split_note_sections(text: str, source_path: str) -> list[NoteSection]:
    body = strip_frontmatter(text)
    lines = body.splitlines()
    sections: list[NoteSection] = []
    title = Path(source_path).stem
    acc: list[str] = []

    def flush() -> None:
        nonlocal acc
        cleaned = clean_markdown("\n".join(acc))
        if cleaned and len(cleaned) >= 80:
            sections.append(NoteSection(title=title, body=cleaned, source_path=source_path))
        acc = []

    for line in lines:
        h = HEADING_RE.match(line)
        if h and len(h.group("marks")) <= 3:
            flush()
            title = clean_markdown(h.group("title"))
        else:
            acc.append(line)
    flush()
    return sections


def tokens(text: str) -> set[str]:
    return {tok for tok in TOKEN_RE.findall(text.lower()) if tok not in STOPWORDS}


def relevance_score(query_tokens: set[str], section: NoteSection) -> float:
    title_tokens = tokens(section.title)
    body_tokens = tokens(section.body)
    if not query_tokens:
        return 0.0
    title_hits = len(query_tokens & title_tokens)
    body_hits = len(query_tokens & body_tokens)
    return title_hits * 4.0 + body_hits / max(1.0, (len(body_tokens) / 120.0))


def sibling_note_sections(source_root: Path, revision_file: Path) -> list[NoteSection]:
    sections: list[NoteSection] = []
    for candidate in sorted(revision_file.parent.glob("*.md")):
        if candidate == revision_file or candidate.name.lower().startswith("rq"):
            continue
        rel = candidate.relative_to(source_root).as_posix()
        try:
            text = candidate.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        sections.extend(split_note_sections(text, rel))
    return sections


def truncate_markdown(text: str, limit: int = 1800) -> str:
    if len(text) <= limit:
        return text
    candidate = text[:limit]
    boundaries = [match.start() for match in re.finditer(r"\n\s*\n", candidate)]
    for boundary in reversed(boundaries):
        cut = candidate[:boundary].rstrip()
        # Do not leave a heading with none of its content behind.
        if cut and not re.match(r"^\s*#{1,6}\s+", cut.splitlines()[-1]):
            return cut + "\n\n…"

    # A line boundary is less ideal than a Markdown block boundary, but still
    # avoids splitting inline syntax such as bold headings.
    line_boundary = candidate.rfind("\n")
    cut = candidate[:line_boundary] if line_boundary > 0 else candidate
    return cut.rstrip() + "\n\n…"


def source_note_answer(prompt: str, sections: Sequence[NoteSection]) -> str:
    query = tokens(prompt)
    ranked = sorted(
        ((relevance_score(query, section), section) for section in sections),
        key=lambda pair: pair[0],
        reverse=True,
    )
    best = [(score, section) for score, section in ranked if score > 0][:2]
    if not best:
        return (
            "**Self-check (no embedded model answer):** Answer every part of the prompt aloud, define the key terms, "
            "justify the reasoning, and work any requested example/calculation. Then compare against the linked SQRBOK page."
        )

    chunks = [
        "**Relevant SQRBOK source notes — active-recall cue, not a model answer.**",
    ]
    for _, section in best:
        chunks.append(f"#### {section.title}\n\n{truncate_markdown(section.body)}")
    return "\n\n".join(chunks)


def live_url(relative_path: str) -> str:
    path = relative_path
    if path.startswith("content/"):
        path = path[len("content/") :]
    if path.endswith(".md"):
        path = path[:-3] + ".html"
    return SITE_BASE + path


def make_id(relative_path: str, ordinal: int) -> str:
    stem = re.sub(r"[^a-z0-9]+", "-", Path(relative_path).stem.lower()).strip("-")
    return f"{stem}-{ordinal:03d}"


def build_cards(source: Path, files: Sequence[tuple[Path, RevisionSpec]]) -> tuple[list[Card], dict[str, int]]:
    cards: list[Card] = []
    counts: dict[str, int] = {}
    for file, spec in files:
        rel = file.relative_to(source).as_posix()
        text = file.read_text(encoding="utf-8", errors="replace")
        parsed = parse_revision_questions(text)
        note_sections = sibling_note_sections(source, file)
        counts[rel] = len(parsed)
        for ordinal, (label, section, prompt, embedded, embedded_kind) in enumerate(parsed, 1):
            answer = embedded if embedded else source_note_answer(prompt, note_sections)
            kind = embedded_kind if embedded_kind else ("source notes" if note_sections else "self-check")
            cards.append(
                Card(
                    id=make_id(rel, ordinal),
                    topic=spec.topic,
                    section=section,
                    label=label,
                    prompt=prompt,
                    answer=answer,
                    answer_kind=kind,
                    source_path=rel,
                    source_url=live_url(rel),
                    github_url=GITHUB_BASE + rel,
                )
            )
    return cards, counts


def warn_snapshot(manifest: dict, specs: dict[str, RevisionSpec], counts: dict[str, int], total: int) -> None:
    expected_total = manifest.get("expected_total_questions")
    if isinstance(expected_total, int) and total != expected_total:
        print(
            f"warning: generated {total} cards; snapshot expected {expected_total}. "
            "Upstream may have changed or parsing needs review.",
            file=sys.stderr,
        )
    for path, spec in specs.items():
        if path not in counts:
            print(f"warning: manifest revision file missing from checkout: {path}", file=sys.stderr)
        elif spec.expected is not None and counts[path] != spec.expected:
            print(
                f"warning: {path}: generated {counts[path]} cards; snapshot expected {spec.expected}",
                file=sys.stderr,
            )


def quote_callout(text: str) -> str:
    return "\n".join("> " + line.rstrip() if line.strip() else ">" for line in text.splitlines())


def write_markdown(cards: Sequence[Card], output: Path) -> None:
    lines = [
        "# SQRBOK Flashcards",
        "",
        f"Generated from the SQRBOK source repository. **{len(cards)} cards.**",
        "",
        "> [!tip] Active recall",
        "> Answer the question aloud before opening the answer callout. Cards labelled `source notes` provide relevant handbook cues, not an official model answer.",
        "",
    ]
    by_topic: dict[str, list[Card]] = {}
    for card in cards:
        by_topic.setdefault(card.topic, []).append(card)

    index = 0
    for topic, topic_cards in by_topic.items():
        lines.extend([f"## {topic} ({len(topic_cards)})", ""])
        for card in topic_cards:
            index += 1
            lines.extend(
                [
                    f"### Card {index:03d} — {card.label}",
                    "",
                    "> [!question] Question",
                    quote_callout(card.prompt),
                    "",
                    f"> [!answer]- Reveal answer / cues — {card.answer_kind}",
                    quote_callout(card.answer),
                    "",
                    "> [!info]- Source",
                    f"> [SQRBOK handbook]({card.source_url}) · [source Markdown]({card.github_url})",
                    "",
                ]
            )
    output.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def tsv_cell(text: str) -> str:
    text = text.replace("\t", " ").replace("\r", "")
    return text.replace("\n", "<br>")


def write_tsv(cards: Sequence[Card], output: Path) -> None:
    rows = ["Front\tBack\tTags\tSource"]
    for card in cards:
        tags = " ".join(
            ["sqrbok", re.sub(r"[^a-z0-9]+", "-", card.topic.lower()).strip("-"), card.answer_kind.replace(" ", "-")]
        )
        rows.append(
            "\t".join(
                [
                    tsv_cell(card.prompt),
                    tsv_cell(card.answer),
                    tsv_cell(tags),
                    tsv_cell(card.source_url),
                ]
            )
        )
    output.write_text("\n".join(rows) + "\n", encoding="utf-8")


def write_json(cards: Sequence[Card], output: Path) -> None:
    output.write_text(json.dumps([asdict(card) for card in cards], indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def markdownish_to_html(text: str) -> str:
    """Render source Markdown without allowing source HTML into the deck."""
    return MARKDOWN_RENDERER.render(text)


def write_static_html(cards: Sequence[Card], output: Path) -> None:
    payload = []
    for card in cards:
        data = asdict(card)
        data["prompt_html"] = markdownish_to_html(card.prompt)
        data["answer_html"] = markdownish_to_html(card.answer)
        payload.append(data)
    json_blob = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    html_doc = STATIC_HTML_TEMPLATE.replace("__CARD_DATA__", json_blob).replace("__CARD_COUNT__", str(len(cards)))
    output.write_text(html_doc, encoding="utf-8")


STATIC_HTML_TEMPLATE = r'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SQRBOK Flashcards</title>
<style>
:root{font-family:Inter,ui-sans-serif,system-ui,sans-serif;color-scheme:light dark;--bg:#101216;--panel:#181b21;--muted:#9ca3af;--border:#30343d;--accent:#8ab4f8;--good:#76c893;--bad:#ff8585}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:#eef1f5;min-height:100vh}.wrap{max-width:980px;margin:auto;padding:22px}.top{display:flex;gap:12px;align-items:end;flex-wrap:wrap}.top h1{margin:0 auto 0 0;font-size:clamp(1.5rem,4vw,2.2rem)}.muted{color:var(--muted)}select,input,button{font:inherit;border:1px solid var(--border);border-radius:10px;background:var(--panel);color:inherit;padding:10px 12px}button{cursor:pointer}button:hover{border-color:var(--accent)}.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:9px;margin:16px 0}.stat{background:var(--panel);border:1px solid var(--border);padding:10px;border-radius:12px}.stat b{display:block;font-size:1.25rem}.filters{display:grid;grid-template-columns:2fr 1fr 1fr auto;gap:9px;margin:12px 0 18px}.card{min-height:390px;background:var(--panel);border:1px solid var(--border);border-radius:18px;padding:clamp(18px,4vw,34px);display:flex;flex-direction:column;box-shadow:0 16px 50px #0005}.card-meta{display:flex;align-items:start;gap:9px;margin-bottom:14px}.pill{align-self:flex-start;border:1px solid var(--border);border-radius:999px;padding:5px 9px;font-size:.82rem;color:var(--muted)}.origin{margin-left:auto;max-width:52%;overflow-wrap:anywhere;text-align:right;font-size:.72rem;line-height:1.35;color:var(--muted)}.content{font-size:clamp(1.08rem,2.2vw,1.35rem);line-height:1.55;flex:1}.content code{font-size:.9em}.answer{border-top:1px solid var(--border);padding-top:18px}.source{font-size:.85rem;color:var(--muted);margin-top:16px}.source a{color:var(--accent)}.controls{display:grid;grid-template-columns:repeat(4,1fr);gap:9px;margin-top:12px}.flip{width:100%;margin-top:12px}.hidden{display:none}.empty{text-align:center;padding:80px 20px;color:var(--muted)}.key{font-size:.75rem;color:var(--muted)}@media(max-width:700px){.filters{grid-template-columns:1fr 1fr}.filters input{grid-column:1/-1}.stats{grid-template-columns:1fr 1fr}.controls{grid-template-columns:1fr 1fr}.origin{max-width:62%}}
.content h1,.content h2,.content h3,.content h4,.content h5,.content h6{line-height:1.25;margin:1.2em 0 .55em}.content h1:first-child,.content h2:first-child,.content h3:first-child,.content h4:first-child,.content h5:first-child,.content h6:first-child{margin-top:0}.content p{margin:.8em 0}.content ul,.content ol{padding-left:1.45em}.content li+li{margin-top:.25em}.content table{border-collapse:collapse;display:block;max-width:100%;overflow-x:auto;margin:1em 0;font-size:.88em}.content th,.content td{border:1px solid var(--border);padding:.45em .6em;text-align:left;vertical-align:top}.content th{background:#242932}.content pre{overflow-x:auto;padding:.8em;border:1px solid var(--border);border-radius:8px;background:#0d0f13;font-size:.82em}.content blockquote{margin:1em 0;padding-left:1em;border-left:3px solid var(--accent);color:var(--muted)}.content a{color:var(--accent)}
</style>
</head><body><main class="wrap">
<div class="top"><div><h1>SQRBOK Flashcards</h1><div class="muted">__CARD_COUNT__ source-grounded revision cards · progress stays in this browser</div></div><button id="shuffle">Shuffle</button></div>
<div class="stats"><div class="stat"><span class="muted">Available</span><b id="available">0</b></div><div class="stat"><span class="muted">Due</span><b id="due">0</b></div><div class="stat"><span class="muted">New</span><b id="newCount">0</b></div><div class="stat"><span class="muted">Reviewed</span><b id="reviewed">0</b></div></div>
<div class="filters"><input id="search" placeholder="Search questions…"><select id="topic"><option value="">All topics</option></select><select id="mode"><option value="all">All</option><option value="due">Due</option><option value="new">New</option><option value="trouble">Trouble</option></select><button id="reset">Reset progress</button></div>
<section id="study"></section>
<p class="muted"><span class="key">Space</span> flip · <span class="key">1</span> Again · <span class="key">2</span> Hard · <span class="key">3</span> Good · <span class="key">4</span> Easy</p>
</main><script>
const cards=__CARD_DATA__;
const KEY='sqrbok-progress-v1';
let progress=JSON.parse(localStorage.getItem(KEY)||'{}'), queue=[], index=0, revealed=false;
const $=id=>document.getElementById(id), now=()=>Date.now();
function save(){localStorage.setItem(KEY,JSON.stringify(progress));updateStats()}
function rec(c){return progress[c.id]||{reps:0,lapses:0,interval:0,due:0}}
function filtered(){const q=$('search').value.trim().toLowerCase(),t=$('topic').value,m=$('mode').value,n=now();return cards.filter(c=>{const r=rec(c);if(t&&c.topic!==t)return false;if(q&&!(`${c.prompt} ${c.topic} ${c.section}`.toLowerCase().includes(q)))return false;if(m==='due'&&!(r.reps>0&&r.due<=n))return false;if(m==='new'&&r.reps>0)return false;if(m==='trouble'&&r.lapses<1)return false;return true})}
function rebuild(keep=false){const current=keep&&queue[index]?.id;queue=filtered();index=Math.max(0,current?queue.findIndex(c=>c.id===current):0);if(index<0)index=0;revealed=false;render();updateStats()}
function updateStats(){const n=now();$('available').textContent=cards.length;$('due').textContent=cards.filter(c=>{const r=rec(c);return r.reps>0&&r.due<=n}).length;$('newCount').textContent=cards.filter(c=>rec(c).reps===0).length;$('reviewed').textContent=cards.filter(c=>rec(c).reps>0).length}
function render(){const host=$('study');if(!queue.length){host.innerHTML='<div class="empty">No cards match these filters.</div>';return}const c=queue[index%queue.length],r=rec(c);host.innerHTML=`<article class="card"><div class="card-meta"><span class="pill">${esc(c.topic)}</span><span class="origin">${esc(c.source_path)} · ${index+1}/${queue.length}</span></div><div class="content"><h2>${revealed?'Answer / cues':'Question'}</h2>${revealed?c.answer_html:c.prompt_html}</div>${revealed?`<div class="answer"><span class="pill">${esc(c.answer_kind)}</span><div class="source"><a href="${c.source_url}" target="_blank" rel="noopener">SQRBOK handbook</a> · <a href="${c.github_url}" target="_blank" rel="noopener">source Markdown</a> · reviews: ${r.reps}, lapses: ${r.lapses}</div></div>`:''}</article><button class="flip" id="flip">${revealed?'Show question':'Reveal answer'} <span class="key">Space</span></button>${revealed?'<div class="controls"><button data-grade="again">Again <span class="key">1</span></button><button data-grade="hard">Hard <span class="key">2</span></button><button data-grade="good">Good <span class="key">3</span></button><button data-grade="easy">Easy <span class="key">4</span></button></div>':''}`;$('flip').onclick=flip;document.querySelectorAll('[data-grade]').forEach(b=>b.onclick=()=>grade(b.dataset.grade))}
function esc(s){const d=document.createElement('div');d.textContent=s;return d.innerHTML}
function flip(){revealed=!revealed;render()}
function grade(g){if(!queue.length)return;const c=queue[index%queue.length],r=rec(c),day=86400000;let interval=r.interval||0,lapses=r.lapses||0;if(g==='again'){interval=0;lapses++;r.due=now()+10*60*1000}else if(g==='hard'){interval=Math.max(1,Math.round(interval*1.2)||1);r.due=now()+interval*day}else if(g==='good'){interval=interval<=1?3:Math.max(3,Math.round(interval*2));r.due=now()+interval*day}else{interval=interval<=1?7:Math.max(7,Math.round(interval*3));r.due=now()+interval*day}progress[c.id]={reps:(r.reps||0)+1,lapses,interval,due:r.due,last:g};save();index=(index+1)%queue.length;revealed=false;render()}
function shuffle(){for(let i=queue.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[queue[i],queue[j]]=[queue[j],queue[i]]}index=0;revealed=false;render()}
[...new Set(cards.map(c=>c.topic))].forEach(t=>{const o=document.createElement('option');o.value=o.textContent=t;$('topic').appendChild(o)});
['search','topic','mode'].forEach(id=>$(id).addEventListener(id==='search'?'input':'change',()=>rebuild()));$('shuffle').onclick=shuffle;$('reset').onclick=()=>{if(confirm('Clear all SQRBOK review progress in this browser?')){progress={};save();rebuild()}};
document.addEventListener('keydown',e=>{if(e.target.matches('input,select'))return;if(e.code==='Space'){e.preventDefault();flip()}if(revealed&&['1','2','3','4'].includes(e.key))grade(({1:'again',2:'hard',3:'good',4:'easy'})[e.key])});rebuild();
</script></body></html>'''


def main() -> int:
    args = parse_args()
    source = args.source.resolve()
    if not (source / "content").is_dir():
        print(f"error: no SQRBOK content directory at {source / 'content'}", file=sys.stderr)
        return 2
    manifest, specs = read_manifest(args.manifest)
    files = discover_revision_files(source, specs)
    if not files:
        print("error: no revision-question Markdown files found", file=sys.stderr)
        return 2

    cards, counts = build_cards(source, files)
    warn_snapshot(manifest, specs, counts, len(cards))
    args.output_dir.mkdir(parents=True, exist_ok=True)
    write_markdown(cards, args.output_dir / "Flashcards.md")
    write_tsv(cards, args.output_dir / "flashcards.tsv")
    write_json(cards, args.output_dir / "flashcards.json")
    write_static_html(cards, args.output_dir / "flashcards.html")
    print(f"Generated {len(cards)} cards from {len(files)} revision files in {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
