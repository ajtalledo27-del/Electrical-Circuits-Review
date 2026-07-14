# Electrical Circuits 1 — Reviewer & Quiz Bee (DC Part 1)

Offline reviewer for **Electrical Circuits 1 (Part 1) — Direct Current Circuits**

**Source lecture:** `ELECTRICAL_CIRCUITS_1_(PART_1)_(2).mp4`

## Question bank

| Bank | Source | Items |
|------|--------|------:|
| **DC Circuits Reviewer** | Electrical Circuits 1 (Part 1) lecture video | 173 |

## Topics (filter in Quiz Bee or browse by section)

| Topic | Focus | Items (approx.) |
|-------|--------|------:|
| **1 — Ohm's Law** | I = V/R, proportionality | 15 |
| **2 — Power & Ohm's Law** | P = VI, I²R, V²/R | 14 |
| **3 — Series Circuits** | RT = ΣR, same current | 14 |
| **4 — Parallel Circuits** | 1/RT = Σ(1/R), same voltage | 14 |
| **5 — Series-Parallel & Req** | Reduction + sample problems | 14 |
| **6 — Circuit Elements & Sources** | Independent / dependent sources | 12 |
| **7 — Electrical Networks** | Branch, node, loop | 12 |
| **8 — Open & Short Circuits** | R → 0 / R → ∞ | 12 |
| **9 — Source Transformation** | vs series R ↔ is ∥ R | 12 |
| **10 — Voltage Division** | Series divider formulas | 12 |
| **11 — Kirchhoff's Laws** | KCL, KVL, mesh systems | 14 |
| **12 — Thévenin's Theorem** | VTh, RTh, load current | 14 |
| **13 — Network Theorems Overview** | Norton, superposition, nodal | 14 |

Key lecture slides are in `materials/` and linked in the app sidebar. MCQs include definitions plus worked-sample values from the video (e.g. parallel Req, sample problems 3–12, Thévenin 4.8 V / 2.4 Ω / 1.5 A).

## Features

- **Reviewer** — Browse questions with answers, rationales, and references
- **Quiz Bee** — Timer, spaced repetition, confidence tracking, bookmarks
- **Dashboard** — Topic mastery radar, accuracy breakdown, quiz history
- **PWA** — Installable for offline use

## Regenerate bank

```bash
python scripts/build_circuits_bank.py
```

## Deploy

Push to `main`, enable GitHub Pages (root). Hard-refresh after updates (`circuits-dc-v1-2026`).

```powershell
cd C:\Users\User\Electrical-Circuits-Review
.\scripts\push-to-github.bat
```
