#!/usr/bin/env python3
"""Build Electrical Circuits 1 (Part 1) — DC Circuits MCQ bank from lecture video content."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "circuits-dc-v1-2026"

SECTIONS = {
    "ohms-law": "Ohm's Law",
    "power": "Power & Ohm's Law",
    "series": "Series Circuits",
    "parallel": "Parallel Circuits",
    "series-parallel": "Series-Parallel & Req",
    "circuit-elements": "Circuit Elements & Sources",
    "networks": "Electrical Networks",
    "open-short": "Open & Short Circuits",
    "source-xform": "Source Transformation",
    "v-div": "Voltage Division",
    "k-laws": "Kirchhoff's Laws",
    "thevenin": "Thévenin's Theorem",
    "network-thms": "Network Theorems Overview",
}

LO_MAP = {
    "ohms-law": "t01",
    "power": "t02",
    "series": "t03",
    "parallel": "t04",
    "series-parallel": "t05",
    "circuit-elements": "t06",
    "networks": "t07",
    "open-short": "t08",
    "source-xform": "t09",
    "v-div": "t10",
    "k-laws": "t11",
    "thevenin": "t12",
    "network-thms": "t13",
}


def q(section, n, text, choices, ans, expl, level="Knowledge", refs=None):
    letters = "abcd"
    ch = [{"ltr": letters[i], "text": c} for i, c in enumerate(choices)]
    return {
        "id": f"{LO_MAP[section]}-{n:03d}",
        "lo": LO_MAP[section],
        "section": section,
        "secTitle": SECTIONS[section],
        "level": level,
        "type": "mcq",
        "text": text,
        "choices": ch,
        "ans": ans,
        "expl": expl,
        "refs": refs or [f"Electrical Circuits 1 (Part 1) — {SECTIONS[section]}"],
    }


def build():
    items = []

    # ---- Ohm's Law ----
    s, c = "ohms-law", 0
    def add(*a, **k):
        nonlocal c
        c += 1
        items.append(q(s, c, *a, **k))

    add(
        "According to Ohm's Law, current I in a circuit is:",
        [
            "Directly proportional to voltage and directly proportional to resistance",
            "Directly proportional to voltage and inversely proportional to resistance",
            "Inversely proportional to voltage and directly proportional to resistance",
            "Independent of both voltage and resistance",
        ],
        "b",
        "I is directly proportional to applied voltage V (or E) and inversely proportional to equivalent resistance R.",
    )
    add(
        "The basic form of Ohm's Law relating current, voltage, and resistance is:",
        ["I = VR", "I = V/R", "I = R/V", "I = V + R"],
        "b",
        "I = V/R. Rearrangements: V = IR and R = V/I.",
    )
    add(
        "In circuit analysis lecture notation, voltage may be represented as:",
        ["Only V", "Only E", "V or E", "Only emf without a symbol"],
        "c",
        "The lecture uses V or E for applied voltage.",
    )
    add(
        "If voltage across a fixed resistor doubles, the current:",
        ["Halves", "Doubles", "Stays the same", "Quadruples"],
        "b",
        "With R fixed, I ∝ V, so doubling V doubles I.",
        level="Application",
    )
    add(
        "If resistance is halved while voltage is held constant, current:",
        ["Halves", "Stays the same", "Doubles", "Becomes zero"],
        "c",
        "I = V/R; if R ↓ by 1/2, I ↑ by 2× (inverse relationship).",
        level="Application",
    )
    add(
        "Given V = 12 V and R = 4 Ω, the current is:",
        ["0.333 A", "3 A", "48 A", "8 A"],
        "b",
        "I = V/R = 12/4 = 3 A.",
        level="Application",
    )
    add(
        "Given I = 2 A and R = 10 Ω, the voltage across the resistor is:",
        ["5 V", "12 V", "20 V", "0.2 V"],
        "c",
        "V = IR = 2 × 10 = 20 V.",
        level="Application",
    )
    add(
        "Given V = 9 V and I = 3 A, the resistance is:",
        ["3 Ω", "12 Ω", "27 Ω", "0.33 Ω"],
        "a",
        "R = V/I = 9/3 = 3 Ω.",
        level="Application",
    )
    add(
        "Ohm's Law applies to which class of devices (within their linear region)?",
        [
            "Only superconductors",
            "Linear resistors obeying V ∝ I",
            "Only ideal diodes",
            "Only capacitors",
        ],
        "b",
        "Ohm's Law describes linear (ohmic) resistors where V is proportional to I.",
    )
    add(
        "The unit of resistance from Ohm's Law is:",
        ["Ampere", "Volt", "Ohm (Ω)", "Watt"],
        "c",
        "R = V/I has units volt/ampere = ohm.",
    )
    add(
        "When total (equivalent) resistance of a circuit increases with fixed supply voltage, total current:",
        ["Increases", "Decreases", "Is unchanged", "Becomes infinite"],
        "b",
        "I_total = V / R_eq; larger R_eq means smaller total current.",
        level="Application",
    )
    add(
        "Which equation is NOT a valid rearrangement of Ohm's Law?",
        ["V = IR", "R = V/I", "I = V/R", "V = I/R"],
        "d",
        "V = I/R is incorrect; correct is V = IR.",
    )
    add(
        "Current flowing 'in an electrical circuit' in the lecture definition of Ohm's Law refers to:",
        [
            "Displacement current in a capacitor only",
            "I flowing through the circuit equivalent resistance",
            "Only electron drift in superconductors",
            "Magnetic flux around a conductor",
        ],
        "b",
        "The definition states current I flowing in the circuit relative to applied voltage and equivalent R.",
    )
    add(
        "If R = 5 Ω and I = 0.4 A, voltage is:",
        ["2 V", "12.5 V", "1.25 V", "20 V"],
        "a",
        "V = IR = 5 × 0.4 = 2 V.",
        level="Application",
    )
    add(
        "A 100 Ω resistor carries 50 mA. The voltage drop is:",
        ["2 V", "5 V", "0.5 V", "20 V"],
        "b",
        "I = 0.05 A; V = 100 × 0.05 = 5 V.",
        level="Application",
    )

    # ---- Power ----
    s, c = "power", 0
    add(
        "Electrical power in terms of voltage and current is:",
        ["P = V/I", "P = VI", "P = V + I", "P = I/V"],
        "b",
        "Basic power equation: P = VI.",
    )
    add(
        "Incorporating Ohm's Law, power dissipated in a resistor can be written as:",
        ["P = I²R only", "P = V²/R only", "P = I²R and P = V²/R", "P = IR only"],
        "c",
        "From P = VI with V = IR: P = I²R; with I = V/R: P = V²/R.",
    )
    add(
        "Which trio correctly lists the power–Ohm forms used in the lecture?",
        [
            "P = VI, P = IR, P = VR",
            "P = VI, P = I²R, P = V²/R",
            "P = V/I, P = I/R, P = VR",
            "P = I/V, P = R/I², P = R/V²",
        ],
        "b",
        "Lecture boxes: P = VI, P = I²R, P = V²/R.",
    )
    add(
        "If voltage across a fixed resistor doubles, power becomes:",
        ["2×", "4×", "½×", "Unchanged"],
        "b",
        "P = V²/R ⇒ P ∝ V², so doubling V multiplies power by 4.",
        level="Application",
    )
    add(
        "If current through a fixed resistor doubles, power becomes:",
        ["2×", "4×", "½×", "Unchanged"],
        "b",
        "P = I²R ⇒ P ∝ I².",
        level="Application",
    )
    add(
        "A 12 V source across 6 Ω dissipates:",
        ["2 W", "72 W", "24 W", "0.5 W"],
        "c",
        "P = V²/R = 144/6 = 24 W (also P = VI with I = 2 A).",
        level="Application",
    )
    add(
        "A 2 A current through 5 Ω dissipates:",
        ["10 W", "20 W", "2.5 W", "40 W"],
        "b",
        "P = I²R = 4 × 5 = 20 W.",
        level="Application",
    )
    add(
        "When resistance is constant, the lecture notes emphasize that power is proportional to:",
        ["V only (linear)", "V²", "1/V", "√V"],
        "b",
        "Circled relation: P ∝ V² (for fixed R).",
    )
    add(
        "The ratio Po/Pi with the same RT in P = V²/R form simplifies to:",
        ["Vo/Vi", "(Vo/Vi)²", "Vi/Vo", "Vo · Vi"],
        "b",
        "Po/Pi = (Vo²/RT)/(Vi²/RT) = (Vo/Vi)².",
        level="Application",
    )
    add(
        "Unit of electrical power is:",
        ["Joule", "Watt", "Ohm", "Coulomb"],
        "b",
        "Power is measured in watts (W).",
    )
    add(
        "For P = V²/R, if R increases while V is fixed, power:",
        ["Increases", "Decreases", "Is unchanged", "Becomes infinite"],
        "b",
        "Larger R means less power for the same voltage.",
        level="Application",
    )
    add(
        "Total power PT when VT = 12 V and RT = 11 Ω is closest to:",
        ["1.09 W", "13.1 W", "132 W", "0.91 W"],
        "b",
        "PT = VT²/RT = 144/11 ≈ 13.09 W (Sample problem no. 4 style).",
        level="Application",
    )
    add(
        "Which statement is TRUE?",
        [
            "Power is always independent of resistance",
            "P = VI, P = I²R, and P = V²/R are consistent via Ohm's Law",
            "P = V²R is the correct Ohm form",
            "P = I/R² is a standard form",
        ],
        "b",
        "All three standard forms are linked through Ohm's Law.",
    )
    add(
        "A device draws 0.5 A from 24 V. Power is:",
        ["12 W", "48 W", "0.021 W", "24.5 W"],
        "a",
        "P = VI = 24 × 0.5 = 12 W.",
        level="Application",
    )

    # ---- Series ----
    s, c = "series", 0
    add(
        "In a series connection, total resistance RT equals:",
        [
            "The reciprocal sum of resistances",
            "The product of all resistances",
            "The sum of the resistances connected in series",
            "The smallest resistance only",
        ],
        "c",
        "RT = R1 + R2 + R3 + … + Rn.",
    )
    add(
        "The series resistance formula is:",
        [
            "1/RT = 1/R1 + 1/R2 + …",
            "RT = R1 + R2 + R3 + … + Rn",
            "RT = R1 · R2 · R3",
            "RT = (R1 + R2)/2",
        ],
        "b",
        "Lecture: RT = R1 + R2 + R3 + … Rn.",
    )
    add(
        "Current in a series circuit is:",
        [
            "Different in every resistor",
            "The same through every series element",
            "Always zero",
            "Proportional only to the largest R",
        ],
        "b",
        "One path ⇒ same current through each series element.",
    )
    add(
        "Voltage drops across series resistors:",
        [
            "Are always equal regardless of R",
            "Add up to the total applied voltage",
            "Cancel each other",
            "Are independent of current",
        ],
        "b",
        "By KVL, series voltage drops sum to the source voltage.",
    )
    add(
        "Three resistors 2 Ω, 3 Ω, and 5 Ω in series have RT =",
        ["0.97 Ω", "10 Ω", "30 Ω", "3.33 Ω"],
        "b",
        "RT = 2 + 3 + 5 = 10 Ω.",
        level="Application",
    )
    add(
        "A 12 V source feeds three equal series resistors. Each drops:",
        ["12 V", "4 V", "36 V", "0 V"],
        "b",
        "Equal resistors share voltage equally: 12/3 = 4 V each.",
        level="Application",
    )
    add(
        "Adding another resistor in series (fixed source voltage) causes total current to:",
        ["Increase", "Decrease", "Stay the same", "Reverse direction"],
        "b",
        "RT increases ⇒ I = V/RT decreases.",
        level="Application",
    )
    add(
        "Power in series resistors:",
        [
            "Is always identical in each resistor",
            "Is largest in the largest resistance (same I)",
            "Is largest in the smallest resistance (same I)",
            "Is zero in all resistors",
        ],
        "b",
        "Same I ⇒ P = I²R is largest for largest R.",
        level="Application",
    )
    add(
        "Series elements share a single:",
        ["Voltage only", "Current path", "Conductance path only", "Magnetic flux path"],
        "b",
        "Series means one common current path.",
    )
    add(
        "If one resistor opens in a series string, the circuit:",
        ["Continues with reduced R", "Carries maximum short-circuit current", "Stops conducting (open path)", "Becomes a parallel circuit"],
        "c",
        "An open anywhere in series breaks the only path.",
        level="Application",
    )
    add(
        "Four 1 kΩ resistors in series equal:",
        ["250 Ω", "1 kΩ", "4 kΩ", "4 Ω"],
        "c",
        "RT = 4 × 1 kΩ = 4 kΩ.",
        level="Application",
    )
    add(
        "Which is a property of series circuits?",
        [
            "Total R is less than the smallest R",
            "Total R is greater than any single R in the string",
            "Voltage is identical across every element",
            "Current divides inversely with R",
        ],
        "b",
        "RT = ΣR exceeds each individual resistance.",
    )
    add(
        "I_T through series R1=4 Ω and R2=8 Ω with 24 V is:",
        ["2 A", "3 A", "6 A", "12 A"],
        "a",
        "RT = 12 Ω; I = 24/12 = 2 A.",
        level="Application",
    )
    add(
        "In series, the largest resistor has the:",
        ["Smallest voltage drop", "Largest voltage drop (same I)", "Largest current", "Zero power"],
        "b",
        "V = IR with common I ⇒ largest R has largest V drop.",
        level="Application",
    )

    # ---- Parallel ----
    s, c = "parallel", 0
    add(
        "For parallel resistors, the lecture states that:",
        [
            "RT equals the sum of resistances",
            "The inverse of total R equals the sum of inverses of individual R",
            "RT equals the product of all R always",
            "RT equals the largest R",
        ],
        "b",
        "1/RT = 1/R1 + 1/R2 + 1/R3 + … + 1/Rn.",
    )
    add(
        "Two resistors in parallel formula is:",
        ["RT = R1 + R2", "RT = R1R2/(R1+R2)", "RT = (R1+R2)/R1R2", "RT = R1 − R2"],
        "b",
        "Product-over-sum: RT = R1R2/(R1+R2).",
    )
    add(
        "6 Ω and 3 Ω in parallel equal:",
        ["9 Ω", "2 Ω", "18 Ω", "4.5 Ω"],
        "b",
        "RT = 6·3/(6+3) = 18/9 = 2 Ω (as in Sample problem no. 1).",
        level="Application",
    )
    add(
        "Voltage across each branch of a parallel circuit is:",
        ["Proportional to each R", "The same across parallel branches", "Zero on the largest R", "Additive"],
        "b",
        "Parallel elements share the same voltage.",
    )
    add(
        "Current in parallel branches:",
        [
            "Is identical in every branch",
            "Divides among branches (larger share to smaller R)",
            "Flows in only one branch",
            "Is always zero",
        ],
        "b",
        "I divides; smaller R takes more current (I = V/R).",
    )
    add(
        "Total resistance of parallels is:",
        [
            "Always greater than the smallest branch R",
            "Always less than the smallest branch R",
            "Equal to the average of branch R",
            "Equal to the sum of branch R",
        ],
        "b",
        "Adding parallel paths lowers RT below the smallest R.",
    )
    add(
        "You need 1.25 kΩ using only 5 kΩ resistors. How many in parallel?",
        ["2", "3", "4", "5"],
        "c",
        "For n equal R: RT = R/n ⇒ 1.25 = 5/n ⇒ n = 4 (Sample problem no. 3).",
        level="Application",
    )
    add(
        "Four identical 8 Ω resistors in parallel give RT =",
        ["32 Ω", "2 Ω", "8 Ω", "4 Ω"],
        "b",
        "RT = 8/4 = 2 Ω.",
        level="Application",
    )
    add(
        "10 Ω || 15 Ω equals:",
        ["25 Ω", "6 Ω", "12.5 Ω", "5 Ω"],
        "b",
        "10·15/(10+15) = 150/25 = 6 Ω.",
        level="Application",
    )
    add(
        "If one parallel branch opens, total resistance:",
        ["Decreases", "Increases (fewer paths)", "Becomes zero", "Is unchanged always"],
        "b",
        "Removing a path increases RT.",
        level="Application",
    )
    add(
        "Conductance G = 1/R. Parallel conductances:",
        ["Subtract", "Add", "Multiply only", "Divide"],
        "b",
        "1/RT = Σ(1/Ri) means conductances add.",
    )
    add(
        "A 12 V source across paralleled 4 Ω and 6 Ω. Current in 4 Ω is:",
        ["1 A", "2 A", "3 A", "5 A"],
        "c",
        "I4 = 12/4 = 3 A.",
        level="Application",
    )
    add(
        "Which is TRUE for parallel circuits?",
        [
            "RT = R1 + R2 + … always",
            "Source voltage appears across each parallel branch",
            "Current is identical in every branch",
            "Opening one branch opens all branches",
        ],
        "b",
        "Common voltage across branches is a defining parallel property.",
    )
    add(
        "Two 10 Ω in parallel plus a series sense: RT of the pair alone is:",
        ["20 Ω", "5 Ω", "10 Ω", "100 Ω"],
        "b",
        "Equal parallels: RT = R/2 = 5 Ω.",
        level="Application",
    )

    # ---- Series-Parallel ----
    s, c = "series-parallel", 0
    add(
        "Simplifying a mixed network usually starts by:",
        [
            "Ignoring all parallel groups",
            "Combining obvious series and parallel groups step by step",
            "Assuming RT = 0",
            "Removing the voltage source permanently",
        ],
        "b",
        "Reduce parallel groups, then series chains, repeatedly.",
    )
    add(
        "Sample: (10 || 15) then + 5 Ω. RT is:",
        ["30 Ω", "11 Ω", "20 Ω", "7.5 Ω"],
        "b",
        "10||15 = 6; 6 + 5 = 11 Ω (Sample problem no. 4).",
        level="Application",
    )
    add(
        "With RT = 11 Ω and VT = 12 V, IT =",
        ["1 A exactly", "12/11 A", "132 A", "0.11 A"],
        "b",
        "IT = VT/RT = 12/11 A.",
        level="Application",
    )
    add(
        "Two resistors with series sum 10 Ω and parallel equivalent 2 Ω. The larger resistor is approximately:",
        ["2.764 Ω", "5 Ω", "7.236 Ω", "10 Ω"],
        "c",
        "Quadratic solution yields ~2.764 Ω and ~7.236 Ω (Sample problem no. 5).",
        level="Application",
    )
    add(
        "If R1 + R2 = 10 and R1R2/(R1+R2) = 2, then R1R2 =",
        ["2", "20", "12", "5"],
        "b",
        "R1R2 / 10 = 2 ⇒ R1R2 = 20.",
        level="Application",
    )
    add(
        "Req looking into a ladder/network of series-parallel resistors is found by:",
        [
            "Adding all resistor values blindly",
            "Successive reduction from far end toward the source terminals",
            "Using only the first resistor",
            "Setting all currents to zero permanently",
        ],
        "b",
        "Work from innermost parallel/series groups outward.",
    )
    add(
        "6 Ω || 4 Ω equals:",
        ["10 Ω", "2.4 Ω", "24 Ω", "5 Ω"],
        "b",
        "24/10 = 2.4 Ω (appears in Sample problem reductions).",
        level="Application",
    )
    add(
        "In Sample problem no. 1 style reduction, 6 || 3 first yields:",
        ["9 Ω", "2 Ω", "18 Ω", "4.5 Ω"],
        "b",
        "RT1 = 6·3/(6+3) = 2 Ω.",
        level="Application",
    )
    add(
        "A series-parallel circuit with several paths can have:",
        [
            "Only one unique current everywhere",
            "Different branch currents but one Req at the terminals",
            "No equivalent resistance",
            "Infinite Req always",
        ],
        "b",
        "Branch currents differ; terminals still see one Req.",
    )
    add(
        "When combining 5 Ω in series with (4 || 12), RT =",
        ["8 Ω", "21 Ω", "5.75 Ω", "9 Ω"],
        "a",
        "4||12 = 3; 5 + 3 = 8 Ω.",
        level="Application",
    )
    add(
        "Product-over-sum applies when:",
        [
            "Any two resistors regardless of connection",
            "Exactly two resistors in parallel",
            "Only series pairs",
            "Only three or more parallels",
        ],
        "b",
        "R1R2/(R1+R2) is the two-resistor parallel formula.",
    )
    add(
        "Increasing a series resistor that feeds a parallel bank:",
        ["Always lowers voltage across the bank", "Always raises bank voltage", "Never changes currents", "Shorts the bank"],
        "a",
        "More series drop reduces voltage available to the parallel group (fixed source).",
        level="Application",
    )
    add(
        "Which pair must be combined first in a typical ladder: far-end parallel, or source-side series alone?",
        [
            "Always source first only",
            "Usually innermost/far groupings that are pure series or parallel",
            "Never combine parallels",
            "Only after Thevenin",
        ],
        "b",
        "Reduce clear series/parallel groups from the far end inward.",
    )
    add(
        "Req between terminals is unchanged if you:",
        [
            "Add a short across the terminals",
            "Rearrange only with equivalent series-parallel reductions",
            "Open all paths",
            "Change source polarity alone always changes Req",
        ],
        "b",
        "Valid series-parallel reductions preserve terminal Req.",
    )

    # ---- Circuit Elements ----
    s, c = "circuit-elements", 0
    add(
        "An ideal independent source provides a specified voltage or current that is:",
        [
            "Controlled by another voltage or current",
            "Completely independent of other circuit elements",
            "Always zero",
            "Dependent on load only by definition",
        ],
        "b",
        "Lecture: ideal independent source is independent of other elements.",
    )
    add(
        "An ideal dependent (controlled) source has a source quantity that is:",
        [
            "Fixed forever and independent of the circuit",
            "Controlled by another voltage or current",
            "Always a short circuit",
            "Always an open circuit",
        ],
        "b",
        "Dependent sources are controlled by another V or I.",
    )
    add(
        "Which symbol typically denotes a dependent source?",
        [
            "A circle only",
            "A diamond (rhombus) symbol",
            "A zigzag only",
            "A ground triangle only",
        ],
        "b",
        "Dependent sources use diamond symbols; independents use circles.",
    )
    add(
        "A voltage source that stays fixed regardless of other elements is:",
        ["Dependent", "Ideal independent voltage source", "Passive resistor", "Short circuit"],
        "b",
        "Independent voltage source definition.",
    )
    add(
        "In Sample problem no. 9, 0.5 io represents:",
        [
            "An independent 0.5 A source",
            "A current-controlled current source (dependent)",
            "A resistor of 0.5 Ω",
            "Open-circuit voltage",
        ],
        "b",
        "Diamond CCCS labeled 0.5 io — dependent current source.",
        level="Application",
    )
    add(
        "Active elements can:",
        [
            "Only dissipate energy",
            "Deliver energy (sources)",
            "Never appear in DC circuits",
            "Only be resistors",
        ],
        "b",
        "Sources are active elements that can deliver energy.",
    )
    add(
        "A resistor is classified as a:",
        ["Active independent source", "Passive element", "Dependent voltage source", "Ideal short"],
        "b",
        "Resistors are passive dissipative elements.",
    )
    add(
        "Controlled sources are called dependent because:",
        [
            "They never appear in problems",
            "Their value depends on another circuit voltage or current",
            "They depend on room temperature only by definition",
            "They equal zero always",
        ],
        "b",
        "Control is from another V or I in the circuit.",
    )
    add(
        "Independent current source symbol is typically:",
        ["Diamond with arrow", "Circle with arrow", "Zigzag", "Battery only"],
        "b",
        "Independent current source: circle with arrow.",
    )
    add(
        "If a source value is written as 3 vx, it is:",
        ["Independent", "Voltage-controlled (dependent)", "Always 3 A", "A resistor"],
        "b",
        "Value depends on voltage vx ⇒ dependent source.",
        level="Application",
    )
    add(
        "Ideal sources are 'ideal' in the sense that:",
        [
            "They have zero and infinite internal resistance cases as assumed models",
            "They never obey circuit laws",
            "They produce heat only",
            "They cannot be drawn on schematics",
        ],
        "a",
        "Ideal models: independent V (zero series R), independent I (infinite parallel R).",
    )
    add(
        "Which is NOT an active source element?",
        ["Independent voltage source", "Dependent current source", "Ohmic resistor", "Independent current source"],
        "c",
        "Resistor is passive.",
    )

    # ---- Networks ----
    s, c = "networks", 0
    add(
        "In electrical networks, a branch represents:",
        [
            "Any closed path",
            "A single element such as a voltage source or a resistor",
            "Only junctions of three wires",
            "The ground symbol only",
        ],
        "b",
        "Branch = single element (source or resistor, etc.).",
    )
    add(
        "A node (junction) is:",
        [
            "Any closed path",
            "The point of connection between two or more branches",
            "A single resistor alone",
            "Only the battery negative terminal",
        ],
        "b",
        "Node/junction connects two or more branches.",
    )
    add(
        "A loop is:",
        ["A single element", "Any closed path in a circuit", "Only a parallel pair", "An open wire end"],
        "b",
        "Loop = any closed path.",
    )
    add(
        "A mesh is typically:",
        [
            "Any loop including all elements",
            "A loop that does not enclose other loops (window pane)",
            "A single node",
            "An open circuit",
        ],
        "b",
        "Mesh = elementary loop with no loops inside.",
    )
    add(
        "If three resistors meet at one point, that point is a:",
        ["Branch", "Node", "Only a mesh", "Short circuit always"],
        "b",
        "Connection of multiple branches = node.",
    )
    add(
        "Counting elements along one path without closing returns:",
        ["A loop", "Not a loop (open path)", "Always a mesh", "A short"],
        "b",
        "Loops must be closed paths.",
    )
    add(
        "Essential nodes usually have:",
        ["Exactly one branch", "Three or more branches", "Zero elements", "Only voltage labels"],
        "b",
        "Essential nodes join three or more branches.",
    )
    add(
        "A series connection of two resistors has how many essential nodes between them (internal)?",
        ["Many", "Often treated as a simple joining node of degree 2", "Infinite", "None exist in series"],
        "b",
        "Two-branch junctions are simple nodes; series string is one path.",
    )
    add(
        "Network topology language (branch/node/loop) is used mainly to:",
        [
            "Replace Ohm's Law",
            "Describe circuit structure for KCL/KVL and analysis methods",
            "Compute battery chemistry",
            "Define only AC machines",
        ],
        "b",
        "Supports systematic KCL/KVL / mesh / nodal analysis.",
    )
    add(
        "Which statement is correct?",
        [
            "Every loop is a mesh",
            "Every mesh is a loop, but not every loop is a mesh",
            "Nodes are closed paths",
            "Branches are always voltage sources",
        ],
        "b",
        "Meshes are special loops; loops may enclose multiple meshes.",
    )
    add(
        "A voltage source alone connected between two nodes counts as:",
        ["No element", "One branch", "Two loops automatically", "Only a dependent source"],
        "b",
        "A single element between nodes is one branch.",
    )
    add(
        "Closed path returning to the start without regard to enclosing others is a:",
        ["Node", "Loop", "Open circuit", "Conductance"],
        "b",
        "Definition of loop.",
    )

    # ---- Open & Short ----
    s, c = "open-short", 0
    add(
        "A SHORT CIRCUIT is a circuit element with resistance approaching:",
        ["Infinity", "Zero", "Exactly 1 Ω", "The source voltage"],
        "b",
        "Short: R → 0.",
    )
    add(
        "An OPEN CIRCUIT is a circuit element with resistance approaching:",
        ["Zero", "Infinity", "The load R only", "Negative resistance"],
        "b",
        "Open: R → ∞.",
    )
    add(
        "Ideal short-circuit voltage across its terminals is:",
        ["Equal to the source", "Zero", "Infinite", "Equal to I·Rload"],
        "b",
        "R → 0 ⇒ V = IR → 0 for finite I.",
    )
    add(
        "Ideal open-circuit current through it is:",
        ["Infinite", "Zero", "Equal to source short current", "V/R with R=0"],
        "b",
        "R → ∞ ⇒ I = V/R → 0.",
    )
    add(
        "Shorting a voltage source (ideally) is dangerous because current:",
        ["Becomes zero", "Can become extremely large (limited only by internal R)", "Reverses voltage forever safely", "Opens automatically always"],
        "b",
        "Near-zero load R draws huge current from a voltage source.",
        level="Application",
    )
    add(
        "An open switch in series with a lamp means the lamp:",
        ["Glows brighter", "Receives no current", "Sees a short", "Has R = 0"],
        "b",
        "Open breaks the series path ⇒ I = 0.",
        level="Application",
    )
    add(
        "To find RTh looking into terminals, independent voltage sources are typically replaced by:",
        ["Open circuits", "Short circuits", "Their rated voltage still", "Infinite current sources"],
        "b",
        "Deactivate independent V sources → short (ideal).",
        level="Application",
    )
    add(
        "To find RTh, independent current sources are replaced by:",
        ["Shorts", "Open circuits", "Their ampere value", "Voltage doubles"],
        "b",
        "Deactivate independent I sources → open.",
        level="Application",
    )
    add(
        "A wire drawn with negligible resistance between two nodes models:",
        ["An open", "A short between those nodes", "A 1 MΩ resistor", "A dependent source"],
        "b",
        "Connecting wire ≈ short (R ≈ 0).",
    )
    add(
        "Which pair is correct?",
        [
            "Short → ∞ Ω; Open → 0 Ω",
            "Short → 0 Ω; Open → ∞ Ω",
            "Both are 1 Ω",
            "Both are ∞ Ω",
        ],
        "b",
        "Lecture definitions.",
    )
    add(
        "If a resistor is shorted by a wire across it, that resistor:",
        ["Sees full voltage", "Is bypassed (essentially 0 V across it)", "Doubles current through itself", "Becomes open"],
        "b",
        "Short across R forces nearly 0 V; current takes short path.",
        level="Application",
    )
    add(
        "An open at the load terminals means the load current is:",
        ["Maximum", "Zero", "Source short-circuit current", "Undefined voltage only"],
        "b",
        "Open load ⇒ I_load = 0; Voc may appear.",
    )

    # ---- Source Transformation ----
    s, c = "source-xform", 0
    add(
        "Source transformation replaces a voltage source vs in series with R by:",
        [
            "A current source is in series with R",
            "A current source is in parallel with R (same R), or vice versa",
            "An open circuit only",
            "Removing R entirely",
        ],
        "b",
        "vs series R ↔ is parallel R with vs = is R.",
    )
    add(
        "The relationship used in source transformation is:",
        ["vs = is / R", "vs = is · R and is = vs / R", "vs = is + R", "vs = R − is"],
        "b",
        "Lecture: vs = is R ; is = vs/R.",
    )
    add(
        "A 12 V source in series with 4 Ω transforms to a current source of:",
        ["3 A in parallel with 4 Ω", "48 A in series with 4 Ω", "0.33 A in parallel with 4 Ω", "12 A in series with 4 Ω"],
        "a",
        "is = vs/R = 12/4 = 3 A parallel with 4 Ω.",
        level="Application",
    )
    add(
        "A 3 A source in parallel with 4 Ω transforms to:",
        ["0.75 V series with 4 Ω", "12 V series with 4 Ω", "3 V parallel with 4 Ω", "7 V series with 3 Ω"],
        "b",
        "vs = is R = 3 × 4 = 12 V series with 4 Ω (Sample problem no. 6).",
        level="Application",
    )
    add(
        "12 V series with 3 Ω transforms to:",
        ["4 A parallel with 3 Ω", "36 A parallel with 3 Ω", "0.25 A series with 3 Ω", "15 A parallel with 12 Ω"],
        "a",
        "is = 12/3 = 4 A || 3 Ω.",
        level="Application",
    )
    add(
        "Source transformation is valid when:",
        [
            "R is the resistor in series with V (or parallel with I) being transformed",
            "Any random resistor in another branch is used as R",
            "Only dependent sources exist",
            "The circuit has no resistors",
        ],
        "a",
        "R must be the companion resistor of that source pair.",
    )
    add(
        "After transformation, terminal behavior a–b is:",
        ["Different", "Equivalent (same i–v at a–b)", "Always shorted", "Always open"],
        "b",
        "Transformation preserves equivalence at the terminals.",
    )
    add(
        "You cannot transform a lone ideal voltage source with R = 0 because:",
        [
            "Ohm's Law forbids voltage",
            "is = vs/R would be undefined/infinite",
            "Current sources cannot exist",
            "KVL fails always",
        ],
        "b",
        "Needs finite series R for a finite equivalent is.",
        level="Application",
    )
    add(
        "Direction of the equivalent current source must match:",
        [
            "Arbitrary always",
            "Polarity of the voltage source (producing same open-circuit polarity)",
            "Opposite polarity always",
            "Ground direction only",
        ],
        "b",
        "Match polarity so Voc and Isc stay consistent.",
    )
    add(
        "Source transformation is often used to:",
        [
            "Avoid Ohm's Law",
            "Simplify circuits before mesh/nodal or series-parallel reduction",
            "Delete all KCL equations forever",
            "Convert AC to DC magnetically",
        ],
        "b",
        "A simplification tool (e.g., Sample problem no. 6).",
    )
    add(
        "vs = 24 V, R = 8 Ω → is =",
        ["3 A", "192 A", "0.33 A", "16 A"],
        "a",
        "is = 24/8 = 3 A.",
        level="Application",
    )
    add(
        "Which statement is FALSE?",
        [
            "vs series R ↔ is parallel R",
            "R stays the same value in the equivalent pair",
            "Dependent sources with controlling variables may need care / may not freely transform the same way",
            "R always becomes R/2 after every transform",
        ],
        "d",
        "R value is unchanged by the transformation pair.",
    )

    # ---- Voltage Division ----
    s, c = "v-div", 0
    add(
        "Voltage division occurs when resistors are connected in:",
        ["Parallel only", "Series", "Neither", "Only with current sources"],
        "b",
        "Lecture: voltage division occurs for series resistors.",
    )
    add(
        "For two series resistors, v1 equals:",
        ["R2/(R1+R2)·v", "R1/(R1+R2)·v", "R1·R2·v", "v/(R1+R2)"],
        "b",
        "v1 = [R1/(R1+R2)] v.",
    )
    add(
        "For two series resistors, v2 equals:",
        ["R1/(R1+R2)·v", "R2/(R1+R2)·v", "R1+R2", "(R1+R2)/R2 · v"],
        "b",
        "v2 = [R2/(R1+R2)] v.",
    )
    add(
        "The two-resistor voltage-divider equations in the lecture are noted as applicable for:",
        [
            "Any number of parallels",
            "Two resistors in series (that boxed form)",
            "Only capacitors",
            "Open circuits only",
        ],
        "b",
        "Slide note: voltage-divider equation shown is for TWO series resistors.",
    )
    add(
        "v = 12 V, R1 = 2 Ω, R2 = 4 Ω. Voltage across R1 is:",
        ["8 V", "4 V", "6 V", "12 V"],
        "b",
        "v1 = 2/(2+4)·12 = 4 V.",
        level="Application",
    )
    add(
        "In a series string, larger R gets:",
        ["Smaller voltage share", "Larger voltage share", "Zero share", "Equal share always"],
        "b",
        "Voltage divides proportional to R.",
        level="Application",
    )
    add(
        "Voltage divider with R1 = R2 yields across each:",
        ["0", "v/2", "v", "2v"],
        "b",
        "Equal series R ⇒ equal split.",
        level="Application",
    )
    add(
        "Current through series divider resistors is:",
        ["Different in each R", "The same I = v/(R1+R2)", "Infinite", "v·(R1+R2)"],
        "b",
        "One series current feeds both.",
    )
    add(
        "VTh via voltage divider across 4 Ω with 12 V and series 5 Ω + 1 Ω + 4 Ω is:",
        ["12 V", "4.8 V", "2.4 V", "6 V"],
        "b",
        "VTH = 12·4/(1+5+4) = 4.8 V (Sample problem no. 11).",
        level="Application",
    )
    add(
        "If a load is connected across one divider resistor, the simple unloaded divider formula:",
        [
            "Always remains exact",
            "Needs re-derivation because loading changes the equivalent",
            "Becomes Ohm's Law only for capacitors",
            "Forces R = 0",
        ],
        "b",
        "Loading parallels one resistor → recalculate.",
        level="Application",
    )
    add(
        "v1 + v2 for a two-resistor divider must equal:",
        ["0", "v (source)", "v/2", "IR only if open"],
        "b",
        "Series KVL: drops sum to applied v.",
    )
    add(
        "Select the correct divider expression for v across R2:",
        ["v · R1/(R1+R2)", "v · R2/(R1+R2)", "v · (R1+R2)/R2", "v · R1·R2"],
        "b",
        "Matches lecture formula for v2.",
    )

    # ---- Kirchhoff ----
    s, c = "k-laws", 0
    add(
        "Kirchhoff's Current Law (KCL) states that at a node:",
        [
            "Voltages sum to zero",
            "Algebraic sum of currents entering/leaving is zero",
            "Resistance is infinite",
            "Power is always maximum",
        ],
        "b",
        "KCL: Σ i = 0 at a node (conservation of charge).",
    )
    add(
        "Kirchhoff's Voltage Law (KVL) states that around a closed loop:",
        [
            "Currents are equal",
            "Algebraic sum of voltage rises/drops is zero",
            "R = 0 always",
            "Power sums to voltage",
        ],
        "b",
        "KVL: Σ v = 0 around a loop.",
    )
    add(
        "In Sample problem no. 10, equation i1 − i8Ω − i2 = 0 is:",
        ["KVL", "KCL at the top node", "Ohm's Law only", "Source transformation"],
        "b",
        "Currents meeting at a node: KCL.",
        level="Application",
    )
    add(
        "For the left mesh with 5 V, 2 Ω, 8 Ω, a KVL form used was:",
        ["−2i1 − 8i8Ω = −5", "i1 = 5 only", "2 + 8 = 5", "i1 − i2 = 5"],
        "a",
        "Lecture eq. 2: −2i1 − 8i8Ω = −5.",
        level="Application",
    )
    add(
        "Solving the Sample problem no. 10 system gave i8Ω =",
        ["1.5 A", "0.25 A", "1.25 A", "3 A"],
        "b",
        "Results: i1 = 1.5 A, i8Ω = 0.25 A, i2 = 1.25 A.",
        level="Application",
    )
    add(
        "Mesh analysis primarily applies:",
        ["KCL at every node only", "KVL to mesh currents", "Faraday's law only", "Maximum power only"],
        "b",
        "Mesh analysis writes KVL in terms of mesh currents.",
    )
    add(
        "Nodal analysis primarily applies:",
        ["KVL only to meshes", "KCL at essential nodes (with Ohm's Law)", "Gauss's law", "Only transformer turns"],
        "b",
        "Nodal: KCL + Ohm expressing branch currents via node voltages.",
    )
    add(
        "If you circle two window panes and write KVL, you are doing:",
        ["Nodal analysis", "Mesh (loop) analysis", "Open-circuit test only", "Average power only"],
        "b",
        "Mesh/loop analysis uses loop KVL.",
    )
    add(
        "In the 5 V / 3 V two-loop circuit, current through 8 Ω was found using:",
        [
            "Voltage division only on opens",
            "Simultaneous KCL + KVL equations",
            "Ignoring sources",
            "Setting all R = 1",
        ],
        "b",
        "System of 3 equations (KCL + two KVLs).",
        level="Application",
    )
    add(
        "Sign convention in KVL requires:",
        [
            "Ignoring polarities",
            "Consistent assignment of rises/drops around the oriented path",
            "Always positive resistors only",
            "Leaving sources out",
        ],
        "b",
        "Track +/− consistently around the loop.",
    )
    add(
        "KCL is based on conservation of:",
        ["Energy only", "Charge", "Flux only", "Temperature"],
        "b",
        "Charge conserved ⇒ currents balance at a node.",
    )
    add(
        "KVL is based on conservation of:",
        ["Charge", "Energy (around a conservative electrostatic path)", "Mass", "Momentum"],
        "b",
        "Electrostatic potential returns to start ⇒ Σv = 0.",
    )
    add(
        "Three currents into a node: 2 A, 3 A in, and i out. For KCL, i =",
        ["1 A", "5 A", "6 A", "0 A"],
        "b",
        "Σin = Σout ⇒ i = 5 A.",
        level="Application",
    )
    add(
        "Calculator hint MODE → [5] → [2] in the lecture refers to:",
        [
            "Complex mode",
            "Simultaneous linear equation solver (for the KCL/KVL system)",
            "Statistics only",
            "Base-n conversion",
        ],
        "b",
        "Used to solve the 3-variable system for Sample problem no. 10.",
        level="Application",
    )

    # ---- Thevenin ----
    s, c = "thevenin", 0
    add(
        "Thévenin's theorem replaces a linear network (seen from load terminals) by:",
        [
            "A current source only",
            "VTh in series with RTh",
            "RTh only",
            "Two voltage sources in parallel",
        ],
        "b",
        "Thévenin equivalent: VTh series RTh.",
    )
    add(
        "VTh is the:",
        [
            "Short-circuit current at the load terminals",
            "Open-circuit voltage at the load terminals",
            "Average of all source voltages",
            "Always 1 V",
        ],
        "b",
        "VTh = Voc with load removed.",
    )
    add(
        "RTh is found by:",
        [
            "Leaving all sources active and measuring only Voc",
            "Deactivating independent sources, then Req at the terminals",
            "Shorting the load and measuring only current forever",
            "Setting R = V/I with load attached only",
        ],
        "b",
        "Kill independent sources; find input resistance at terminals.",
    )
    add(
        "In Sample problem no. 11, RTh = 6||4 =",
        ["10 Ω", "2.4 Ω", "24 Ω", "1.5 Ω"],
        "b",
        "RTh = 6·4/(6+4) = 2.4 Ω (5+1 = 6 with sources killed).",
        level="Application",
    )
    add(
        "In Sample problem no. 11, VTh =",
        ["12 V", "4.8 V", "2.4 V", "0.8 V"],
        "b",
        "VTh = 12·4/(1+5+4) = 4.8 V.",
        level="Application",
    )
    add(
        "With VTh = 4.8 V, RTh = 2.4 Ω, RL = 0.8 Ω, load current I =",
        ["1.5 A", "6 A", "0.8 A", "2.4 A"],
        "a",
        "I = 4.8/(2.4+0.8) = 4.8/3.2 = 1.5 A.",
        level="Application",
    )
    add(
        "Sample problem no. 12 found VTh ≈",
        ["12 V", "30 V", "32 V", "2.5 V"],
        "b",
        "After reduction, VTh = 12 × 2.5 = 30 V.",
        level="Application",
    )
    add(
        "Once VTh and RTh are known, current in RL is:",
        ["I = VTh / RL only ignoring RTh", "I = VTh / (RTh + RL)", "I = RL / VTh", "I = (RTh + RL)/VTh"],
        "b",
        "Series circuit of VTh, RTh, RL.",
    )
    add(
        "Thévenin equivalents are most useful when:",
        [
            "You must never attach different loads",
            "You want to reuse analysis for varying load RL",
            "The circuit is nonlinear always",
            "There are no resistors",
        ],
        "b",
        "Change RL without redoing the whole network each time.",
    )
    add(
        "If RL → ∞ (open), voltage across load terminals approaches:",
        ["0", "VTh", "Isc · 0", "RTh only"],
        "b",
        "Open-circuit voltage is VTh.",
        level="Application",
    )
    add(
        "If RL → 0 (short), current approaches:",
        ["0", "VTh / RTh (= Isc)", "VTh · RTh", "Infinite always even if RTh > 0"],
        "b",
        "Isc = VTh/RTh.",
        level="Application",
    )
    add(
        "RTh = VTh / Isc is valid when:",
        [
            "The network is linear at those terminals",
            "Only for superconductors",
            "Never",
            "Only if RL = RTh",
        ],
        "a",
        "Alternative RTh method using Voc/Isc for linear circuits.",
    )
    add(
        "In the Thévenin process for Sample problem no. 11, load 0.8 Ω is:",
        [
            "Included when finding VTh (left connected)",
            "Removed to find Voc = VTh, then reattached to the equivalent",
            "Replaced by a short first for VTh",
            "Ignored forever",
        ],
        "b",
        "Remove load for Voc; reconnect to VTh–RTh model.",
        level="Application",
    )
    add(
        "Which is the Thévenin model topology?",
        [
            "Current source parallel with RTh only (that is Norton)",
            "Voltage source VTh series with RTh",
            "Two opens",
            "Only a single resistor equal to RL",
        ],
        "b",
        "Distinguish from Norton (is || R).",
    )

    # ---- Network theorems overview ----
    s, c = "network-thms", 0
    add(
        "Which set matches the lecture 'Network theorems' list?",
        [
            "Ohm, Faraday, Lenz, Ampere, Gauss",
            "Kirchhoff's Laws, Thévenin, Norton, Nodal Analysis, Superposition",
            "Only Fourier and Laplace",
            "Maxwell's equations only",
        ],
        "b",
        "Slide list: Kirchhoff, Thévenin, Norton, Nodal, Superposition.",
    )
    add(
        "Norton's theorem replaces a linear network by:",
        [
            "VTh series RTh",
            "IN parallel with RN (often RN = RTh)",
            "Only an open circuit",
            "A dependent source only",
        ],
        "b",
        "Norton: current source parallel with Norton resistance.",
    )
    add(
        "Superposition theorem applies to:",
        [
            "Nonlinear circuits with diodes always",
            "Linear circuits with multiple independent sources (one active at a time)",
            "Only magnetic circuits",
            "Only open circuits",
        ],
        "b",
        "Sum responses from each independent source separately (linear networks).",
    )
    add(
        "When using superposition, dependent sources are generally:",
        [
            "Always deactivated",
            "Left active (their controlling variables remain)",
            "Replaced by shorts always",
            "Converted to opens always",
        ],
        "b",
        "Do not deactivate dependent sources; they stay as elements responding to controls.",
    )
    add(
        "Norton current IN equals:",
        [
            "Open-circuit voltage",
            "Short-circuit current at the terminals",
            "Always VTh · RTh",
            "Zero always",
        ],
        "b",
        "IN = Isc; also IN = VTh/RTh.",
    )
    add(
        "Relation between Thévenin and Norton (same terminals) is:",
        [
            "Unrelated",
            "Same R, with VTh = IN · RTh",
            "RTh = 2 RN always",
            "Opposite polarity always only",
        ],
        "b",
        "Source transformation links VTh–RTh and IN–RN.",
    )
    add(
        "Nodal analysis is listed among network theorems/methods because it:",
        [
            "Replaces Ohm's Law",
            "Systematically uses KCL with node voltages as unknowns",
            "Only applies to open circuits",
            "Ignores resistors",
        ],
        "b",
        "Standard DC analysis method in the lecture outline.",
    )
    add(
        "Which method is best when many voltage sources share a ground and you want node voltages?",
        ["Mesh only always", "Nodal analysis", "Only voltage division on opens", "Ignoring KCL"],
        "b",
        "Nodal shines with node-to-reference voltages.",
    )
    add(
        "Which method is often convenient for planar circuits with many meshes and current unknowns?",
        ["Only Norton", "Mesh analysis", "Only Faraday", "Phasor RF only"],
        "b",
        "Mesh/KVL unknowns = mesh currents.",
    )
    add(
        "If two independent sources act in a linear resistor network, superposition says total response is:",
        [
            "Product of individual responses",
            "Sum of responses found with each source acting alone",
            "Difference always zero",
            "Maximum of the two responses only",
        ],
        "b",
        "Linearity ⇒ additivity.",
    )
    add(
        "Thévenin and Norton are most closely related by:",
        ["KCL only", "Source transformation", "Magnetic coupling only", "Open-circuit inductance"],
        "b",
        "They are source-transform pairs of the same R.",
    )
    add(
        "A goal of network theorems in DC Part 1 is to:",
        [
            "Avoid defining nodes",
            "Simplify analysis of linear circuits (especially with loads)",
            "Replace all resistors with sources",
            "Eliminate Ohm's Law",
        ],
        "b",
        "Tools for solving and simplifying DC networks.",
    )
    add(
        "Which is NOT on the lecture Network theorems overview slide?",
        ["Superposition Theorem", "Thévenin's Theorem", "Maxwell's equations", "Kirchhoff's Laws"],
        "c",
        "Overview listed Kirchhoff, Thévenin, Norton, Nodal, Superposition.",
    )
    add(
        "For maximum power transfer to RL from a Thévenin source, choose:",
        ["RL = 0", "RL = RTh", "RL → ∞ only", "RL = 2 RTh always only"],
        "b",
        "Classic result: RL = RTh for max power (linear DC).",
        level="Application",
    )

    # renumber per-section already via add(); fix global if section switched incorrectly
    # The add() above reuses nonlocal s,c — verified per block.

    # Fix: first section uses add before s reassignment issues — OK.

    # Rebuild ids cleanly in section order
    ordered = []
    counters = {k: 0 for k in SECTIONS}
    for it in items:
        sec = it["section"]
        counters[sec] += 1
        it["id"] = f"{LO_MAP[sec]}-{counters[sec]:03d}"
        ordered.append(it)
    return ordered


def main():
    questions = build()
    bank = {"version": VERSION, "questions": questions}
    (ROOT / "bank.json").write_text(json.dumps(bank, indent=2), encoding="utf-8")

    lines = [
        "/**",
        f" * Electrical Circuits 1 (Part 1) — Direct Current Circuits — {len(questions)} MCQ",
        " * Source: ELECTRICAL_CIRCUITS_1_(PART_1) lecture video",
        " */",
        f"window.CIRCUITS_DC_QB = {json.dumps(questions, indent=2)};",
        "",
    ]
    (ROOT / "questions.js").write_text("\n".join(lines), encoding="utf-8")

    manifest = {
        "version": VERSION,
        "banks": {
            "reviewer": {
                "label": "DC Circuits Reviewer",
                "file": "questions.js",
                "global": "CIRCUITS_DC_QB",
                "description": "Electrical Circuits 1 (Part 1) — Direct Current Circuits",
                "count": len(questions),
            }
        },
    }
    (ROOT / "banks-manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Wrote {len(questions)} questions -> bank.json, questions.js")
    for sec, title in SECTIONS.items():
        n = sum(1 for q in questions if q["section"] == sec)
        print(f"  {title}: {n}")


if __name__ == "__main__":
    main()
