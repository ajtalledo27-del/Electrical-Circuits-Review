# -*- coding: utf-8 -*-
"""Transcribe Electrical Circuits Part 1 & Part 2 videos in chunks; save incrementally."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VIDEOS = [
    {
        "key": "part1",
        "label": "Part 1",
        "paths": [
            Path(r"C:\Users\User\Downloads\ELECTRICAL_CIRCUITS_1_(PART_1)_(2).mp4"),
            ROOT / "materials" / "ELECTRICAL_CIRCUITS_1_(PART_1)_(2).mp4",
        ],
    },
    {
        "key": "part2",
        "label": "Part 2",
        "paths": [
            Path(r"C:\Users\User\Downloads\ELECTRICAL_CIRCUITS_1_(PART_2)_(2).mp4"),
            ROOT / "materials" / "ELECTRICAL_CIRCUITS_1_(PART_2)_(2).mp4",
        ],
    },
]
CHUNK_DIR = ROOT / "materials" / "chunks"
OUT_TXT = ROOT / "materials" / "transcript.txt"
OUT_JSON = ROOT / "materials" / "transcript.json"
CHUNK_SEC = 300  # 5 minutes per chunk


def resolve_video(paths: list[Path]) -> Path:
    for p in paths:
        if p.exists():
            return p
    raise FileNotFoundError(f"Video not found. Tried: {paths}")


def duration_seconds(video: Path) -> float:
    cmd = [
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", str(video),
    ]
    return float(subprocess.check_output(cmd, text=True).strip())


def extract_chunk(video: Path, start: float, dur: float, out: Path):
    out.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "ffmpeg", "-y", "-ss", str(start), "-i", str(video),
        "-t", str(dur), "-vn", "-acodec", "pcm_s16le", "-ar", "16000", "-ac", "1",
        str(out),
    ]
    subprocess.run(cmd, check=True, capture_output=True)


def load_progress() -> dict:
    if OUT_JSON.exists():
        try:
            return json.loads(OUT_JSON.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"parts": {}, "segments": []}


def save_progress(data: dict):
    OUT_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def transcribe_part(model, video: Path, part_key: str, part_label: str, time_offset: float, data: dict):
    part_state = data["parts"].get(part_key, {})
    start_at = part_state.get("done_at", 0.0)
    total = duration_seconds(video)
    chunk_i = int(start_at // CHUNK_SEC)

    print(f"\n=== {part_label}: {video.name} ({total/60:.1f} min, offset {time_offset/60:.1f} min) ===")

    while start_at < total - 1:
        end_at = min(start_at + CHUNK_SEC, total)
        dur = end_at - start_at
        wav = CHUNK_DIR / f"{part_key}_chunk_{chunk_i:04d}.wav"
        print(f"--- {part_label} chunk {chunk_i}: {start_at/60:.1f}–{end_at/60:.1f} min ---")
        if not wav.exists() or wav.stat().st_size < 1000:
            extract_chunk(video, start_at, dur, wav)

        segments, _ = model.transcribe(str(wav), language="en", beam_size=1, vad_filter=True)
        new_lines = []
        for seg in segments:
            text = seg.text.strip()
            if not text:
                continue
            entry = {
                "part": part_key,
                "partLabel": part_label,
                "start": round(time_offset + start_at + seg.start, 2),
                "end": round(time_offset + start_at + seg.end, 2),
                "localStart": round(start_at + seg.start, 2),
                "text": text,
            }
            data["segments"].append(entry)
            line = f"[{entry['start']:08.1f}s][{part_label}] {text}"
            new_lines.append(line)
            try:
                print(line)
            except UnicodeEncodeError:
                print(line.encode("ascii", errors="replace").decode("ascii"))

        with OUT_TXT.open("a", encoding="utf-8") as f:
            for ln in new_lines:
                f.write(ln + "\n")

        data["parts"][part_key] = {"done_at": end_at, "duration": total, "video": video.name}
        save_progress(data)
        print(f"Saved {len(data['segments'])} total segments")

        start_at = end_at
        chunk_i += 1
        wav.unlink(missing_ok=True)

    data["parts"][part_key]["complete"] = True
    save_progress(data)
    print(f"Finished {part_label}")


def transcribe():
    from faster_whisper import WhisperModel

    print("Loading whisper tiny (fast)...")
    model = WhisperModel("tiny", device="cpu", compute_type="int8")

    data = load_progress()
    if not data.get("segments"):
        if OUT_TXT.exists():
            OUT_TXT.unlink()
        data = {"parts": {}, "segments": []}

    offset = 0.0
    for spec in VIDEOS:
        video = resolve_video(spec["paths"])
        part_state = data["parts"].get(spec["key"], {})
        if part_state.get("complete"):
            print(f"Skipping {spec['label']} (already complete)")
            offset += part_state.get("duration", duration_seconds(video))
            continue
        transcribe_part(model, video, spec["key"], spec["label"], offset, data)
        offset += data["parts"][spec["key"]]["duration"]

    print(f"\nDone -> {OUT_TXT} ({len(data['segments'])} segments)")


if __name__ == "__main__":
    try:
        for spec in VIDEOS:
            resolve_video(spec["paths"])
    except FileNotFoundError as e:
        sys.exit(str(e))
    if OUT_TXT.exists() and OUT_TXT.stat().st_size == 0:
        OUT_TXT.unlink()
    transcribe()
