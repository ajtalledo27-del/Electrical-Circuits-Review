# -*- coding: utf-8 -*-
"""Build lecture-notes.js from transcript.json (Part 1 + Part 2 combined)."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSCRIPT = ROOT / "materials" / "transcript.txt"
TRANSCRIPT_JSON = ROOT / "materials" / "transcript.json"
OUT_JS = ROOT / "lecture-notes.js"


def load_segments():
    if TRANSCRIPT_JSON.exists():
        data = json.loads(TRANSCRIPT_JSON.read_text(encoding="utf-8"))
        if isinstance(data, dict) and "segments" in data:
            return data["segments"]
        if isinstance(data, list):
            return data
    if not TRANSCRIPT.exists():
        return []
    segs = []
    for line in TRANSCRIPT.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\[(\d+\.\d+)s\]\[(Part \d+)\]\s*(.+)", line)
        if m:
            segs.append({
                "start": float(m.group(1)),
                "partLabel": m.group(2),
                "text": m.group(3).strip(),
            })
        else:
            m2 = re.match(r"\[(\d+\.\d+)s\]\s*(.+)", line)
            if m2:
                segs.append({"start": float(m2.group(1)), "text": m2.group(2).strip()})
    return segs


def fmt_time(sec: float) -> str:
    m, s = divmod(int(sec), 60)
    h, m = divmod(m, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def group_segments(segments, gap=45):
    if not segments:
        return []
    blocks = []
    cur = {
        "start": segments[0]["start"],
        "part": segments[0].get("partLabel", ""),
        "lines": [segments[0]["text"]],
    }
    prev_end = segments[0].get("end", segments[0]["start"] + 5)
    for seg in segments[1:]:
        start = seg["start"]
        part_changed = seg.get("partLabel") and seg.get("partLabel") != cur.get("part")
        if (start - prev_end > gap or part_changed) and cur["lines"]:
            blocks.append(cur)
            cur = {"start": start, "part": seg.get("partLabel", ""), "lines": []}
        cur["lines"].append(seg["text"])
        prev_end = seg.get("end", start + 5)
    if cur["lines"]:
        blocks.append(cur)
    return blocks


def extract_formula_lines(segments):
    keys = re.compile(
        r"(ohm|kirchhoff|kvl|kcl|voltage|current|resistance|power|watt|"
        r"series|parallel|mesh|nodal|divider|delta|wye|capacitor|inductor|"
        r"V\s*=|I\s*=|R\s*=|P\s*=|E\s*=|\bR_T\b|\bG\s*=)",
        re.I,
    )
    found = []
    seen = set()
    for seg in segments:
        t = seg["text"]
        if keys.search(t) and t.lower() not in seen:
            seen.add(t.lower())
            found.append({"time": seg["start"], "text": t})
    return found


def build():
    segments = load_segments()
    blocks = group_segments(segments)
    formulas_found = extract_formula_lines(segments)

    notes = []
    for i, blk in enumerate(blocks):
        title = f"Section {i + 1}"
        if blk.get("part"):
            title = f"{blk['part']} — {title}"
        notes.append({
            "id": f"note-{i+1:03d}",
            "time": fmt_time(blk["start"]),
            "start": blk["start"],
            "part": blk.get("part", ""),
            "title": title,
            "text": " ".join(blk["lines"]),
            "paragraphs": blk["lines"],
        })

    payload = {
        "title": "Electrical Circuits 1 — Full Lecture Text (Parts 1 & 2)",
        "source": "ELECTRICAL_CIRCUITS_1_(PART_1)_(2).mp4 + ELECTRICAL_CIRCUITS_1_(PART_2)_(2).mp4",
        "segmentCount": len(segments),
        "blockCount": len(notes),
        "notes": notes,
        "formulaMentions": formulas_found,
    }
    if not notes:
        payload["status"] = "Transcript not ready yet. Run: python scripts/transcribe_video.py"

    OUT_JS.write_text(
        "/** Auto-generated from video transcripts */\nwindow.CIRCUITS_LECTURE = "
        + json.dumps(payload, ensure_ascii=False, indent=2)
        + ";\n",
        encoding="utf-8",
    )
    print(f"Built lecture-notes.js: {len(segments)} segments, {len(notes)} blocks, {len(formulas_found)} formula lines")


if __name__ == "__main__":
    build()
