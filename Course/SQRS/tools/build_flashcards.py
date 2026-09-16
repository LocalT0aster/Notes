#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.14"
# dependencies = [
#   "markdown-it-py>=4.0.0,<5.0.0",
# ]
# ///
"""Build the SQRS HTML flashcard deck from the current Markdown decks.

Adapted from Course/SQRBOK/tools/build_flashcards.py on the `sqrbok` branch.
The original HTML study UI and grading/progress model are reused; only the
input adapter differs so it consumes Course/SQRS/L*.md callout cards.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Sequence

from markdown_it import MarkdownIt

MARKDOWN_RENDERER = MarkdownIt("commonmark", {"html": False}).enable("table")
CARD_HEADING_RE = re.compile(r"^###\s+(?P<label>Q\d+\s+—\s+.+?)\s*$")
SOURCE_RE = re.compile(r"^\*\*Source:\*\*\s+(?P<url>https?://\S+)\s*$")
QUESTION_MARKER = "> [!question] Question"
ANSWER_PREFIX = "> [!answer]-"
GITHUB_BASE = "https://github.com/LocalT0aster/Notes/blob/master/Course/SQRS/"


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
    parser.add_argument("--source", type=Path, required=True, help="Course/SQRS directory")
    parser.add_argument("--output", type=Path, help="HTML output path; defaults to SOURCE/flashcards.html")
    parser.add_argument("--json", type=Path, dest="json_output", help="Optional JSON output for inspection")
    return parser.parse_args()


def unquote_callout(lines: Sequence[str]) -> str:
    out: list[str] = []
    for line in lines:
        if line == ">":
            out.append("")
        elif line.startswith("> "):
            out.append(line[2:])
        elif line.startswith(">"):
            out.append(line[1:].lstrip())
        else:
            break
    return "\n".join(out).strip()


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def deck_topic(lines: Sequence[str], fallback: str) -> str:
    for line in lines:
        if line.startswith("# "):
            return re.sub(r"\s+Flashcards\s*$", "", line[2:].strip())
    return fallback


def deck_source(lines: Sequence[str]) -> str:
    for line in lines:
        match = SOURCE_RE.match(line)
        if match:
            return match.group("url")
    return ""


def parse_deck(path: Path, root: Path) -> list[Card]:
    lines = path.read_text(encoding="utf-8").splitlines()
    topic = deck_topic(lines, path.stem)
    source_url = deck_source(lines)
    cards: list[Card] = []
    starts = [i for i, line in enumerate(lines) if CARD_HEADING_RE.match(line)]

    for ordinal, start in enumerate(starts, 1):
        stop = starts[ordinal] if ordinal < len(starts) else len(lines)
        block = lines[start:stop]
        heading = CARD_HEADING_RE.match(block[0])
        assert heading is not None
        label = heading.group("label")

        try:
            q_marker = block.index(QUESTION_MARKER)
        except ValueError as exc:
            raise ValueError(f"{path}: {label}: missing question callout") from exc

        answer_marker = next((i for i, line in enumerate(block) if line.startswith(ANSWER_PREFIX)), None)
        if answer_marker is None:
            raise ValueError(f"{path}: {label}: missing answer callout")

        prompt = unquote_callout(block[q_marker + 1 : answer_marker])
        answer = unquote_callout(block[answer_marker + 1 :])
        if not prompt or not answer:
            raise ValueError(f"{path}: {label}: empty question or answer")

        rel = path.relative_to(root).as_posix()
        cards.append(
            Card(
                id=f"{slug(path.stem)}-{ordinal:03d}",
                topic=topic,
                section=topic,
                label=label,
                prompt=prompt,
                answer=answer,
                answer_kind="answer / self-check",
                source_path=rel,
                source_url=source_url,
                github_url=GITHUB_BASE + rel,
            )
        )
    return cards


def build_cards(source: Path) -> list[Card]:
    files = sorted(source.glob("L[0-9][0-9]_*.md"))
    if not files:
        raise SystemExit(f"No lecture decks found in {source}")
    cards: list[Card] = []
    for path in files:
        cards.extend(parse_deck(path, source))
    return cards


def markdown_to_html(text: str) -> str:
    return MARKDOWN_RENDERER.render(text)


def write_json(cards: Sequence[Card], output: Path) -> None:
    output.write_text(json.dumps([asdict(card) for card in cards], indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_static_html(cards: Sequence[Card], output: Path) -> None:
    payload = []
    for card in cards:
        data = asdict(card)
        data["prompt_html"] = markdown_to_html(card.prompt)
        data["answer_html"] = markdown_to_html(card.answer)
        payload.append(data)
    json_blob = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    html_doc = STATIC_HTML_TEMPLATE.replace("__CARD_DATA__", json_blob).replace("__CARD_COUNT__", str(len(cards)))
    output.write_text(html_doc, encoding="utf-8")


# Reused from the sqrbok branch generator; labels/storage key are scoped to SQRS.
STATIC_HTML_TEMPLATE = r'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SQRS Flashcards</title>
<style>
:root{font-family:Inter,ui-sans-serif,system-ui,sans-serif;color-scheme:light dark;--bg:#101216;--panel:#181b21;--muted:#9ca3af;--border:#30343d;--accent:#8ab4f8;--good:#76c893;--bad:#ff8585}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:#eef1f5;min-height:100vh}.wrap{max-width:980px;margin:auto;padding:22px}.top{display:flex;gap:12px;align-items:end;flex-wrap:wrap}.top h1{margin:0 auto 0 0;font-size:clamp(1.5rem,4vw,2.2rem)}.muted{color:var(--muted)}select,input,button{font:inherit;border:1px solid var(--border);border-radius:10px;background:var(--panel);color:inherit;padding:10px 12px}button{cursor:pointer}button:hover{border-color:var(--accent)}.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:9px;margin:16px 0}.stat{background:var(--panel);border:1px solid var(--border);padding:10px;border-radius:12px}.stat b{display:block;font-size:1.25rem}.filters{display:grid;grid-template-columns:2fr 1fr 1fr auto;gap:9px;margin:12px 0 18px}.card{min-height:390px;background:var(--panel);border:1px solid var(--border);border-radius:18px;padding:clamp(18px,4vw,34px);display:flex;flex-direction:column;box-shadow:0 16px 50px #0005}.card-meta{display:flex;align-items:start;gap:9px;margin-bottom:14px}.pill{align-self:flex-start;border:1px solid var(--border);border-radius:999px;padding:5px 9px;font-size:.82rem;color:var(--muted)}.origin{margin-left:auto;max-width:52%;overflow-wrap:anywhere;text-align:right;font-size:.72rem;line-height:1.35;color:var(--muted)}.content{font-size:clamp(1.08rem,2.2vw,1.35rem);line-height:1.55;flex:1}.content code{font-size:.9em}.answer{border-top:1px solid var(--border);padding-top:18px}.source{font-size:.85rem;color:var(--muted);margin-top:16px}.source a{color:var(--accent)}.controls{display:grid;grid-template-columns:repeat(4,1fr);gap:9px;margin-top:12px}.flip{width:100%;margin-top:12px}.hidden{display:none}.empty{text-align:center;padding:80px 20px;color:var(--muted)}.key{font-size:.75rem;color:var(--muted)}@media(max-width:700px){.filters{grid-template-columns:1fr 1fr}.filters input{grid-column:1/-1}.stats{grid-template-columns:1fr 1fr}.controls{grid-template-columns:1fr 1fr}.origin{max-width:62%}}
.content h1,.content h2,.content h3,.content h4,.content h5,.content h6{line-height:1.25;margin:1.2em 0 .55em}.content h1:first-child,.content h2:first-child,.content h3:first-child,.content h4:first-child,.content h5:first-child,.content h6:first-child{margin-top:0}.content p{margin:.8em 0}.content ul,.content ol{padding-left:1.45em}.content li+li{margin-top:.25em}.content table{border-collapse:collapse;display:block;max-width:100%;overflow-x:auto;margin:1em 0;font-size:.88em}.content th,.content td{border:1px solid var(--border);padding:.45em .6em;text-align:left;vertical-align:top}.content th{background:#242932}.content pre{overflow-x:auto;padding:.8em;border:1px solid var(--border);border-radius:8px;background:#0d0f13;font-size:.82em}.content blockquote{margin:1em 0;padding-left:1em;border-left:3px solid var(--accent);color:var(--muted)}.content a{color:var(--accent)}
</style>
</head><body><main class="wrap">
<div class="top"><div><h1>SQRS Flashcards</h1><div class="muted">__CARD_COUNT__ current-course revision cards · progress stays in this browser</div></div><button id="shuffle">Shuffle</button></div>
<div class="stats"><div class="stat"><span class="muted">Available</span><b id="available">0</b></div><div class="stat"><span class="muted">Due</span><b id="due">0</b></div><div class="stat"><span class="muted">New</span><b id="newCount">0</b></div><div class="stat"><span class="muted">Reviewed</span><b id="reviewed">0</b></div></div>
<div class="filters"><input id="search" placeholder="Search questions…"><select id="topic"><option value="">All topics</option></select><select id="mode"><option value="all">All</option><option value="due">Due</option><option value="new">New</option><option value="trouble">Trouble</option></select><button id="reset">Reset progress</button></div>
<section id="study"></section>
<p class="muted"><span class="key">Space</span> flip · <span class="key">1</span> Again · <span class="key">2</span> Hard · <span class="key">3</span> Good · <span class="key">4</span> Easy</p>
</main><script>
const cards=__CARD_DATA__;
const KEY='sqrs-progress-v1';
let progress=JSON.parse(localStorage.getItem(KEY)||'{}'), queue=[], index=0, revealed=false;
const $=id=>document.getElementById(id), now=()=>Date.now();
function save(){localStorage.setItem(KEY,JSON.stringify(progress));updateStats()}
function rec(c){return progress[c.id]||{reps:0,lapses:0,interval:0,due:0}}
function filtered(){const q=$('search').value.trim().toLowerCase(),t=$('topic').value,m=$('mode').value,n=now();return cards.filter(c=>{const r=rec(c);if(t&&c.topic!==t)return false;if(q&&!(`${c.prompt} ${c.topic} ${c.section}`.toLowerCase().includes(q)))return false;if(m==='due'&&!(r.reps>0&&r.due<=n))return false;if(m==='new'&&r.reps>0)return false;if(m==='trouble'&&r.lapses<1)return false;return true})}
function rebuild(keep=false){const current=keep&&queue[index]?.id;queue=filtered();index=Math.max(0,current?queue.findIndex(c=>c.id===current):0);if(index<0)index=0;revealed=false;render();updateStats()}
function updateStats(){const n=now();$('available').textContent=cards.length;$('due').textContent=cards.filter(c=>{const r=rec(c);return r.reps>0&&r.due<=n}).length;$('newCount').textContent=cards.filter(c=>rec(c).reps===0).length;$('reviewed').textContent=cards.filter(c=>rec(c).reps>0).length}
function render(){const host=$('study');if(!queue.length){host.innerHTML='<div class="empty">No cards match these filters.</div>';return}const c=queue[index%queue.length],r=rec(c);host.innerHTML=`<article class="card"><div class="card-meta"><span class="pill">${esc(c.topic)}</span><span class="origin">${esc(c.source_path)} · ${index+1}/${queue.length}</span></div><div class="content"><h2>${revealed?'Answer / cues':'Question'}</h2>${revealed?c.answer_html:c.prompt_html}</div>${revealed?`<div class="answer"><span class="pill">${esc(c.answer_kind)}</span><div class="source">${c.source_url?`<a href="${c.source_url}" target="_blank" rel="noopener">SQRBOK question set</a> · `:''}<a href="${c.github_url}" target="_blank" rel="noopener">course Markdown</a> · reviews: ${r.reps}, lapses: ${r.lapses}</div></div>`:''}</article><button class="flip" id="flip">${revealed?'Show question':'Reveal answer'} <span class="key">Space</span></button>${revealed?'<div class="controls"><button data-grade="again">Again <span class="key">1</span></button><button data-grade="hard">Hard <span class="key">2</span></button><button data-grade="good">Good <span class="key">3</span></button><button data-grade="easy">Easy <span class="key">4</span></button></div>':''}`;$('flip').onclick=flip;document.querySelectorAll('[data-grade]').forEach(b=>b.onclick=()=>grade(b.dataset.grade))}
function esc(s){const d=document.createElement('div');d.textContent=s;return d.innerHTML}
function flip(){revealed=!revealed;render()}
function grade(g){if(!queue.length)return;const c=queue[index%queue.length],r=rec(c),day=86400000;let interval=r.interval||0,lapses=r.lapses||0;if(g==='again'){interval=0;lapses++;r.due=now()+10*60*1000}else if(g==='hard'){interval=Math.max(1,Math.round(interval*1.2)||1);r.due=now()+interval*day}else if(g==='good'){interval=interval<=1?3:Math.max(3,Math.round(interval*2));r.due=now()+interval*day}else{interval=interval<=1?7:Math.max(7,Math.round(interval*3));r.due=now()+interval*day}progress[c.id]={reps:(r.reps||0)+1,lapses,interval,due:r.due,last:g};save();index=(index+1)%queue.length;revealed=false;render()}
function shuffle(){for(let i=queue.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[queue[i],queue[j]]=[queue[j],queue[i]]}index=0;revealed=false;render()}
[...new Set(cards.map(c=>c.topic))].forEach(t=>{const o=document.createElement('option');o.value=o.textContent=t;$('topic').appendChild(o)});
['search','topic','mode'].forEach(id=>$(id).addEventListener(id==='search'?'input':'change',()=>rebuild()));$('shuffle').onclick=shuffle;$('reset').onclick=()=>{if(confirm('Clear all SQRS review progress in this browser?')){progress={};save();rebuild()}};
document.addEventListener('keydown',e=>{if(e.target.matches('input,select'))return;if(e.code==='Space'){e.preventDefault();flip()}if(revealed&&['1','2','3','4'].includes(e.key))grade(({1:'again',2:'hard',3:'good',4:'easy'})[e.key])});rebuild();
</script></body></html>'''


def main() -> int:
    args = parse_args()
    source = args.source.resolve()
    cards = build_cards(source)
    output = (args.output or source / "flashcards.html").resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    write_static_html(cards, output)
    if args.json_output:
        write_json(cards, args.json_output.resolve())
    topics = len({card.topic for card in cards})
    print(f"Generated {len(cards)} cards across {topics} topics: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
