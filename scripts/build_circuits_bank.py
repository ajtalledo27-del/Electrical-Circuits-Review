# -*- coding: utf-8 -*-
"""Build Electrical Circuits 1 — questions.js, formulas.js, bank.json."""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_JS = ROOT / "questions.js"
OUT_FORM = ROOT / "formulas.js"
OUT_JSON = ROOT / "bank.json"
VERSION = "circuits1-v1-2026"

SECTIONS = {
    "basic": "Basic Concepts",
    "ohm": "Ohm's Law",
    "series": "Series Circuits",
    "parallel": "Parallel Circuits",
    "kvl": "Kirchhoff's Voltage Law",
    "kcl": "Kirchhoff's Current Law",
    "mesh": "Mesh Analysis",
    "nodal": "Nodal Analysis",
    "divider": "Voltage & Current Dividers",
    "wye": "Wye-Delta & Bridges",
}


def _mcq(qid, lo, text, correct, wrong, expl="", refs=None, level="Application"):
    letters = ["a", "b", "c", "d"]
    opts = [correct, wrong[0], wrong[1], wrong[2]]
    rng = random.Random(qid)
    rng.shuffle(opts)
    ans = letters[opts.index(correct)]
    return {
        "id": qid,
        "lo": lo,
        "section": lo,
        "secTitle": SECTIONS[lo],
        "level": level,
        "type": "mcq",
        "text": text,
        "choices": [{"ltr": letters[i], "text": opts[i]} for i in range(4)],
        "ans": ans,
        "expl": expl,
        "refs": refs or ["Electrical Circuits 1"],
    }


def formulas():
    return [
        {"id": "f-basic-01", "section": "basic", "secTitle": "Basic Concepts", "name": "Voltage", "formula": "V = W/Q  (volts = joules per coulomb)", "vars": [{"sym": "V", "desc": "Voltage / potential difference (V)"}, {"sym": "W", "desc": "Work or energy (J)"}, {"sym": "Q", "desc": "Charge (C)"}], "notes": "Voltage is energy per unit charge.", "example": "1 V = 1 J/C"},
        {"id": "f-basic-02", "section": "basic", "secTitle": "Basic Concepts", "name": "Current", "formula": "I = Q/t  (amperes = coulombs per second)", "vars": [{"sym": "I", "desc": "Current (A)"}, {"sym": "Q", "desc": "Charge (C)"}, {"sym": "t", "desc": "Time (s)"}], "notes": "Rate of charge flow.", "example": "1 A = 1 C/s through a cross-section."},
        {"id": "f-basic-03", "section": "basic", "secTitle": "Basic Concepts", "name": "Power", "formula": "P = V·I = I²R = V²/R", "vars": [{"sym": "P", "desc": "Power (W)"}, {"sym": "V", "desc": "Voltage (V)"}, {"sym": "I", "desc": "Current (A)"}, {"sym": "R", "desc": "Resistance (Ω)"}], "notes": "Instantaneous power in a resistor.", "example": "10 V, 2 A → P = 20 W"},
        {"id": "f-basic-04", "section": "basic", "secTitle": "Basic Concepts", "name": "Energy", "formula": "E = P·t = V·I·t", "vars": [{"sym": "E", "desc": "Energy (J or Wh)"}, {"sym": "t", "desc": "Time (s)"}], "notes": "Energy consumed over time.", "example": "100 W for 2 h → 200 Wh"},
        {"id": "f-ohm-01", "section": "ohm", "secTitle": "Ohm's Law", "name": "Ohm's Law", "formula": "V = I·R", "vars": [{"sym": "V", "desc": "Voltage across resistor"}, {"sym": "I", "desc": "Current through resistor"}, {"sym": "R", "desc": "Resistance (Ω)"}], "notes": "Linear relation for ohmic resistors.", "example": "I = 2 A, R = 5 Ω → V = 10 V"},
        {"id": "f-ohm-02", "section": "ohm", "secTitle": "Ohm's Law", "name": "Conductance", "formula": "G = 1/R", "vars": [{"sym": "G", "desc": "Conductance (S = siemens)"}, {"sym": "R", "desc": "Resistance (Ω)"}], "notes": "Reciprocal of resistance.", "example": "R = 200 Ω → G = 0.005 S"},
        {"id": "f-ser-01", "section": "series", "secTitle": "Series Circuits", "name": "Series Resistance", "formula": "R_T = R₁ + R₂ + … + R_n", "vars": [{"sym": "R_T", "desc": "Total / equivalent resistance"}, {"sym": "R_n", "desc": "Individual resistors"}], "notes": "Same current through all series elements.", "example": "4 Ω + 6 Ω = 10 Ω"},
        {"id": "f-ser-02", "section": "series", "secTitle": "Series Circuits", "name": "Series Current", "formula": "I = I₁ = I₂ = … = I_n", "vars": [{"sym": "I", "desc": "Loop current (same everywhere)"}], "notes": "Current is identical in a single series path.", "example": "3 A through each resistor in series."},
        {"id": "f-par-01", "section": "parallel", "secTitle": "Parallel Circuits", "name": "Parallel Resistance (two)", "formula": "1/R_T = 1/R₁ + 1/R₂", "vars": [{"sym": "R_T", "desc": "Equivalent resistance"}], "notes": "Same voltage across parallel branches.", "example": "6 Ω ∥ 3 Ω → R_T = 2 Ω"},
        {"id": "f-par-02", "section": "parallel", "secTitle": "Parallel Circuits", "name": "Parallel Resistance (n resistors)", "formula": "1/R_T = Σ (1/R_i)", "vars": [{"sym": "R_i", "desc": "Each branch resistance"}], "notes": "R_T is always less than smallest branch R.", "example": "Two 8 Ω in parallel → 4 Ω"},
        {"id": "f-par-03", "section": "parallel", "secTitle": "Parallel Circuits", "name": "Parallel Voltage", "formula": "V = V₁ = V₂ = … = V_n", "vars": [{"sym": "V", "desc": "Voltage across each branch"}], "notes": "Branches share the same node pair.", "example": "12 V source → each branch has 12 V."},
        {"id": "f-kvl-01", "section": "kvl", "secTitle": "Kirchhoff's Voltage Law", "name": "KVL Statement", "formula": "Σ V_rise = Σ V_drop  (around any closed loop)", "vars": [{"sym": "V_rise", "desc": "Sources / EMF rises"}, {"sym": "V_drop", "desc": "IR drops and opposing rises"}], "notes": "Conservation of energy in a loop.", "example": "12 V source = sum of resistor drops in loop."},
        {"id": "f-kcl-01", "section": "kcl", "secTitle": "Kirchhoff's Current Law", "name": "KCL Statement", "formula": "Σ I_in = Σ I_out  (at any node)", "vars": [{"sym": "I_in", "desc": "Currents entering node"}, {"sym": "I_out", "desc": "Currents leaving node"}], "notes": "Conservation of charge.", "example": "3 A in, 1 A + 2 A out → balanced."},
        {"id": "f-mesh-01", "section": "mesh", "secTitle": "Mesh Analysis", "name": "Mesh Current Method", "formula": "Σ (I_mesh − I_adjacent) · R_loop + Σ E = 0", "vars": [{"sym": "I_mesh", "desc": "Assumed clockwise mesh current"}, {"sym": "R_loop", "desc": "Resistors in that mesh path"}], "notes": "Apply KVL to each independent mesh.", "example": "Two-mesh circuit → 2 simultaneous equations."},
        {"id": "f-nod-01", "section": "nodal", "secTitle": "Nodal Analysis", "name": "Nodal Voltage Method", "formula": "Σ (V_node − V_adj) / R + Σ I_source = 0", "vars": [{"sym": "V_node", "desc": "Unknown node voltage"}, {"sym": "V_adj", "desc": "Adjacent node voltage (0 V if ground)"}], "notes": "Apply KCL at each non-reference node.", "example": "Supernode used when voltage source between nodes."},
        {"id": "f-div-01", "section": "divider", "secTitle": "Voltage & Current Dividers", "name": "Voltage Divider", "formula": "V_x = V_T · R_x / (R₁ + R₂ + …)", "vars": [{"sym": "V_x", "desc": "Voltage across R_x"}, {"sym": "V_T", "desc": "Total series voltage"}], "notes": "Only for series-connected resistors.", "example": "R₁=1 kΩ, R₂=3 kΩ, V_T=8 V → V₁=2 V"},
        {"id": "f-div-02", "section": "divider", "secTitle": "Voltage & Current Dividers", "name": "Current Divider (two)", "formula": "I₁ = I_T · R₂ / (R₁ + R₂)", "vars": [{"sym": "I₁", "desc": "Current through R₁"}, {"sym": "I_T", "desc": "Total parallel current"}], "notes": "Inverse proportion to resistance.", "example": "I_T=6 A, R₁=2 Ω, R₂=4 Ω → I₁=4 A"},
        {"id": "f-wye-01", "section": "wye", "secTitle": "Wye-Delta & Bridges", "name": "Delta to Wye (R₁ opposite R_A)", "formula": "R_A = (R₁·R₂) / (R₁+R₂+R₃)", "vars": [{"sym": "R_A", "desc": "Wye leg opposite delta side R₁"}], "notes": "Product of adjacent / sum of all three.", "example": "Equal delta R → wye R/3 each."},
        {"id": "f-wye-02", "section": "wye", "secTitle": "Wye-Delta & Bridges", "name": "Wheatstone Bridge Balance", "formula": "R₁/R₂ = R₃/R₄", "vars": [{"sym": "R₁…R₄", "desc": "Bridge arms"}], "notes": "Galvanometer reads zero when balanced.", "example": "R₁=100, R₂=200, R₃=150 → R₄=300 Ω for balance."},
    ]


def questions():
    Q = _mcq
    return [
        Q("q-basic-01", "basic", "The SI unit of electric current is:", "Ampere", ("Volt", "Ohm", "Watt"), "Current is charge per unit time."),
        Q("q-basic-02", "basic", "Power dissipated in a resistor equals:", "P = V·I", ("P = V/I", "P = I/R", "P = V·R"), "Basic power relation."),
        Q("q-basic-03", "basic", "1 kilowatt-hour (kWh) is a unit of:", "Energy", ("Power", "Current", "Resistance"), "kWh = energy."),
        Q("q-basic-04", "basic", "If 5 C passes a point in 2 s, current is:", "2.5 A", ("10 A", "0.4 A", "7 A"), "I = Q/t = 5/2."),
        Q("q-ohm-01", "ohm", "A 10 Ω resistor carries 3 A. Voltage across it is:", "30 V", ("3.33 V", "13 V", "0.3 V"), "V = IR."),
        Q("q-ohm-02", "ohm", "Doubling resistance while current stays constant:", "Doubles voltage", ("Halves voltage", "Quarters power", "No change"), "V ∝ R."),
        Q("q-ohm-03", "ohm", "Conductance of 250 Ω is:", "0.004 S", ("250 S", "4 S", "0.25 S"), "G = 1/R."),
        Q("q-ser-01", "series", "Three resistors 2 Ω, 3 Ω, 5 Ω in series have R_T:", "10 Ω", ("1 Ω", "0.83 Ω", "30 Ω"), "Add in series."),
        Q("q-ser-02", "series", "In a series circuit, current is:", "The same through all elements", ("Split equally always", "Zero everywhere", "Largest at the source only"), "Series current rule."),
        Q("q-ser-03", "series", "Largest voltage drop in series occurs across:", "Largest resistance (same I)", ("Smallest R", "Always the first R", "Always equal"), "V = IR."),
        Q("q-par-01", "parallel", "Two 12 Ω resistors in parallel have R_T:", "6 Ω", ("24 Ω", "12 Ω", "3 Ω"), "1/6 = 1/12+1/12."),
        Q("q-par-02", "parallel", "Parallel equivalent resistance is always:", "Less than the smallest branch R", ("Greater than largest R", "Equal to average", "Infinite"), "Parallel reduces R."),
        Q("q-par-03", "parallel", "Voltage across parallel branches is:", "Equal to the source voltage", ("Divided by number of branches", "Always zero", "Sum of drops"), "Parallel voltage rule."),
        Q("q-kvl-01", "kvl", "Kirchhoff's Voltage Law is based on:", "Conservation of energy", ("Conservation of charge only", "Ohm's law only", "Magnetic flux"), "Energy balance in loop."),
        Q("q-kvl-02", "kvl", "Traversing a resistor against conventional current:", "Counts as a voltage rise", ("Counts as a drop", "Is ignored", "Violates KVL"), "Polarity convention."),
        Q("q-kcl-01", "kcl", "At a junction, algebraic sum of currents:", "Equals zero", ("Equals source voltage", "Equals total R", "Is always positive"), "ΣI = 0 at node."),
        Q("q-kcl-02", "kcl", "KCL applies to:", "Any node or junction", ("Only ground node", "Only voltage sources", "Only capacitors"), "Charge conservation."),
        Q("q-mesh-01", "mesh", "Mesh analysis assigns:", "Circulating mesh currents", ("Node voltages only", "Only source currents", "Capacitance values"), "Mesh current method."),
        Q("q-mesh-02", "mesh", "Number of independent mesh equations equals:", "Number of independent meshes", ("Number of nodes", "Number of resistors", "Always 1"), "One KVL per mesh."),
        Q("q-nod-01", "nodal", "Nodal analysis unknowns are:", "Node voltages relative to reference", ("Mesh currents only", "Power only", "Charge only"), "Nodal method."),
        Q("q-nod-02", "nodal", "Reference node is typically at:", "0 V (ground)", ("Highest voltage", "Floating potential", "Source terminal only"), "Ground reference."),
        Q("q-div-01", "divider", "Voltage divider with R₁=2 kΩ, R₂=6 kΩ, V_T=16 V gives V₁:", "4 V", ("12 V", "8 V", "2 V"), "V₁ = 16×2/8."),
        Q("q-div-02", "divider", "Current divider: larger branch resistance gets:", "Smaller share of total current", ("Larger share", "All current", "No current"), "I ∝ 1/R."),
        Q("q-wye-01", "wye", "Balanced Wheatstone bridge (R₁/R₂ = R₃/R₄) means:", "No current through galvanometer", ("Maximum power transfer always", "All resistors equal required", "Bridge is open circuit"), "Balance condition."),
        Q("q-wye-02", "wye", "Three equal resistors R in delta convert to wye each:", "R/3", ("3R", "R", "R/2"), "Symmetric conversion."),
        Q("q-basic-05", "basic", "Energy used by a 60 W bulb in 30 minutes is:", "30 Wh", ("60 Wh", "1800 Wh", "2 Wh"), "E = P×t = 0.5 h × 60 W."),
        Q("q-ohm-04", "ohm", "12 V across 4 Ω draws current:", "3 A", ("48 A", "0.33 A", "16 A"), "I = V/R."),
        Q("q-ser-04", "series", "Two resistors in series with 24 V source: R₁=8 Ω, R₂=16 Ω. Current is:", "1 A", ("2 A", "0.5 A", "24 A"), "I = 24/24."),
        Q("q-par-04", "parallel", "4 Ω and 12 Ω in parallel: total current at 24 V is:", "8 A", ("6 A", "2 A", "24 A"), "R_T=3 Ω, I=8 A."),
        Q("q-kvl-03", "kvl", "Sum of voltage drops around a closed loop equals:", "Sum of voltage rises", ("Zero always without sources", "Total resistance", "Total current"), "KVL balance."),
        Q("q-kcl-03", "kcl", "5 A enters a node; 2 A and 1 A leave on two branches. Third branch carries:", "2 A leaving", ("2 A entering", "8 A leaving", "0 A"), "5 = 2+1+2."),
        Q("q-div-03", "divider", "Voltage divider cannot be used to find branch voltage in:", "A parallel network without series pair", ("Series pair", "Two-resistor string", "Potentiometer"), "Needs series path."),
        Q("q-mesh-03", "mesh", "Shared resistor between two meshes appears in:", "Both mesh equations with appropriate signs", ("Neither equation", "Only one mesh", "KCL only"), "Coupling in meshes."),
        Q("q-nod-03", "nodal", "A supernode is used when:", "A voltage source connects two non-reference nodes", ("Only resistors exist", "Bridge is balanced", "No ground exists"), "Supernode technique."),
        Q("q-basic-06", "basic", "Resistance is defined as:", "R = V/I", ("R = I/V always for any device", "R = P·I", "R = Q/t"), "Ohmic definition."),
        Q("q-par-05", "parallel", "Three identical R in parallel: R_T equals:", "R/3", ("3R", "R", "R²"), "n equal: R/n."),
        Q("q-wye-03", "wye", "Purpose of delta-wye transformation:", "Simplify networks for analysis", ("Measure frequency only", "Eliminate all resistors", "Convert AC to DC"), "Network reduction."),
    ]


def build():
    qs = questions()
    fs = formulas()
    bank = {"version": VERSION, "questions": qs, "formulas": fs}
    OUT_JSON.write_text(json.dumps(bank, ensure_ascii=False, indent=2), encoding="utf-8")
    OUT_JS.write_text(
        "/** Electrical Circuits 1 — %d MCQ */\nwindow.CIRCUITS_QB = %s;\n"
        % (len(qs), json.dumps(qs, ensure_ascii=False, indent=2)),
        encoding="utf-8",
    )
    OUT_FORM.write_text(
        "/** Electrical Circuits 1 — %d formulas */\nwindow.CIRCUITS_FORMULAS = %s;\n"
        % (len(fs), json.dumps(fs, ensure_ascii=False, indent=2)),
        encoding="utf-8",
    )
    print(f"Built {len(qs)} questions, {len(fs)} formulas")


if __name__ == "__main__":
    build()
