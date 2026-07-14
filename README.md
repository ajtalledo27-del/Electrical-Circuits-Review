# Electrical Circuits 1 — Reviewer, Formula Bank & Lecture Text

**Live:** https://ajtalledo27-del.github.io/Electrical-Circuits-Review/

Offline reviewer for **Electrical Circuits 1 (Parts 1 & 2)** — DC circuits, Ohm's law, KVL/KCL, mesh & nodal analysis.

**Source lectures:**
- `ELECTRICAL_CIRCUITS_1_(PART_1)_(2).mp4`
- `ELECTRICAL_CIRCUITS_1_(PART_2)_(2).mp4`

## App sections

| Section | Description |
|---------|-------------|
| **📝 Lecture Text** | Full transcript from Part 1 & Part 2 videos (3,751 lines) |
| **📐 Formula Bank** | 19 compiled formulas with variables & examples |
| **📖 Reviewer** | MCQs with solutions |
| **🎯 Quiz Bee** | Timed practice + dashboard |

## Question bank

| Bank | Source | Items |
|------|--------|------:|
| **Circuits 1** | Video lectures + standard EC1 coverage | 37 |

## Topics

| Section | Focus |
|---------|--------|
| Basic Concepts | Voltage, current, power, energy |
| Ohm's Law | V = IR, conductance |
| Series & Parallel | Equivalent resistance, current/voltage rules |
| KVL & KCL | Loop and node laws |
| Mesh & Nodal Analysis | Systematic circuit analysis |
| Dividers & Wye-Delta | Voltage/current dividers, bridge balance |

## Regenerate all text from videos

```bash
python scripts/transcribe_video.py
python scripts/build_lecture_notes.py
python scripts/build_circuits_bank.py
python scripts/patch_index.py
```

Videos stay in `materials/` locally (too large for GitHub). **Lecture text** is committed as `lecture-notes.js` + `materials/transcript.txt`.

## Deploy

Push to `main` — GitHub Pages is already enabled on this repo.

```powershell
cd C:\Users\User\Electrical-Circuits-Review
git add -A
git commit -m "Update"
git push
```
