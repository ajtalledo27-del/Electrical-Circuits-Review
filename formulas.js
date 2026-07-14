/** Electrical Circuits 1 — 19 formulas */
window.CIRCUITS_FORMULAS = [
  {
    "id": "f-basic-01",
    "section": "basic",
    "secTitle": "Basic Concepts",
    "name": "Voltage",
    "formula": "V = W/Q  (volts = joules per coulomb)",
    "vars": [
      {
        "sym": "V",
        "desc": "Voltage / potential difference (V)"
      },
      {
        "sym": "W",
        "desc": "Work or energy (J)"
      },
      {
        "sym": "Q",
        "desc": "Charge (C)"
      }
    ],
    "notes": "Voltage is energy per unit charge.",
    "example": "1 V = 1 J/C"
  },
  {
    "id": "f-basic-02",
    "section": "basic",
    "secTitle": "Basic Concepts",
    "name": "Current",
    "formula": "I = Q/t  (amperes = coulombs per second)",
    "vars": [
      {
        "sym": "I",
        "desc": "Current (A)"
      },
      {
        "sym": "Q",
        "desc": "Charge (C)"
      },
      {
        "sym": "t",
        "desc": "Time (s)"
      }
    ],
    "notes": "Rate of charge flow.",
    "example": "1 A = 1 C/s through a cross-section."
  },
  {
    "id": "f-basic-03",
    "section": "basic",
    "secTitle": "Basic Concepts",
    "name": "Power",
    "formula": "P = V·I = I²R = V²/R",
    "vars": [
      {
        "sym": "P",
        "desc": "Power (W)"
      },
      {
        "sym": "V",
        "desc": "Voltage (V)"
      },
      {
        "sym": "I",
        "desc": "Current (A)"
      },
      {
        "sym": "R",
        "desc": "Resistance (Ω)"
      }
    ],
    "notes": "Instantaneous power in a resistor.",
    "example": "10 V, 2 A → P = 20 W"
  },
  {
    "id": "f-basic-04",
    "section": "basic",
    "secTitle": "Basic Concepts",
    "name": "Energy",
    "formula": "E = P·t = V·I·t",
    "vars": [
      {
        "sym": "E",
        "desc": "Energy (J or Wh)"
      },
      {
        "sym": "t",
        "desc": "Time (s)"
      }
    ],
    "notes": "Energy consumed over time.",
    "example": "100 W for 2 h → 200 Wh"
  },
  {
    "id": "f-ohm-01",
    "section": "ohm",
    "secTitle": "Ohm's Law",
    "name": "Ohm's Law",
    "formula": "V = I·R",
    "vars": [
      {
        "sym": "V",
        "desc": "Voltage across resistor"
      },
      {
        "sym": "I",
        "desc": "Current through resistor"
      },
      {
        "sym": "R",
        "desc": "Resistance (Ω)"
      }
    ],
    "notes": "Linear relation for ohmic resistors.",
    "example": "I = 2 A, R = 5 Ω → V = 10 V"
  },
  {
    "id": "f-ohm-02",
    "section": "ohm",
    "secTitle": "Ohm's Law",
    "name": "Conductance",
    "formula": "G = 1/R",
    "vars": [
      {
        "sym": "G",
        "desc": "Conductance (S = siemens)"
      },
      {
        "sym": "R",
        "desc": "Resistance (Ω)"
      }
    ],
    "notes": "Reciprocal of resistance.",
    "example": "R = 200 Ω → G = 0.005 S"
  },
  {
    "id": "f-ser-01",
    "section": "series",
    "secTitle": "Series Circuits",
    "name": "Series Resistance",
    "formula": "R_T = R₁ + R₂ + … + R_n",
    "vars": [
      {
        "sym": "R_T",
        "desc": "Total / equivalent resistance"
      },
      {
        "sym": "R_n",
        "desc": "Individual resistors"
      }
    ],
    "notes": "Same current through all series elements.",
    "example": "4 Ω + 6 Ω = 10 Ω"
  },
  {
    "id": "f-ser-02",
    "section": "series",
    "secTitle": "Series Circuits",
    "name": "Series Current",
    "formula": "I = I₁ = I₂ = … = I_n",
    "vars": [
      {
        "sym": "I",
        "desc": "Loop current (same everywhere)"
      }
    ],
    "notes": "Current is identical in a single series path.",
    "example": "3 A through each resistor in series."
  },
  {
    "id": "f-par-01",
    "section": "parallel",
    "secTitle": "Parallel Circuits",
    "name": "Parallel Resistance (two)",
    "formula": "1/R_T = 1/R₁ + 1/R₂",
    "vars": [
      {
        "sym": "R_T",
        "desc": "Equivalent resistance"
      }
    ],
    "notes": "Same voltage across parallel branches.",
    "example": "6 Ω ∥ 3 Ω → R_T = 2 Ω"
  },
  {
    "id": "f-par-02",
    "section": "parallel",
    "secTitle": "Parallel Circuits",
    "name": "Parallel Resistance (n resistors)",
    "formula": "1/R_T = Σ (1/R_i)",
    "vars": [
      {
        "sym": "R_i",
        "desc": "Each branch resistance"
      }
    ],
    "notes": "R_T is always less than smallest branch R.",
    "example": "Two 8 Ω in parallel → 4 Ω"
  },
  {
    "id": "f-par-03",
    "section": "parallel",
    "secTitle": "Parallel Circuits",
    "name": "Parallel Voltage",
    "formula": "V = V₁ = V₂ = … = V_n",
    "vars": [
      {
        "sym": "V",
        "desc": "Voltage across each branch"
      }
    ],
    "notes": "Branches share the same node pair.",
    "example": "12 V source → each branch has 12 V."
  },
  {
    "id": "f-kvl-01",
    "section": "kvl",
    "secTitle": "Kirchhoff's Voltage Law",
    "name": "KVL Statement",
    "formula": "Σ V_rise = Σ V_drop  (around any closed loop)",
    "vars": [
      {
        "sym": "V_rise",
        "desc": "Sources / EMF rises"
      },
      {
        "sym": "V_drop",
        "desc": "IR drops and opposing rises"
      }
    ],
    "notes": "Conservation of energy in a loop.",
    "example": "12 V source = sum of resistor drops in loop."
  },
  {
    "id": "f-kcl-01",
    "section": "kcl",
    "secTitle": "Kirchhoff's Current Law",
    "name": "KCL Statement",
    "formula": "Σ I_in = Σ I_out  (at any node)",
    "vars": [
      {
        "sym": "I_in",
        "desc": "Currents entering node"
      },
      {
        "sym": "I_out",
        "desc": "Currents leaving node"
      }
    ],
    "notes": "Conservation of charge.",
    "example": "3 A in, 1 A + 2 A out → balanced."
  },
  {
    "id": "f-mesh-01",
    "section": "mesh",
    "secTitle": "Mesh Analysis",
    "name": "Mesh Current Method",
    "formula": "Σ (I_mesh − I_adjacent) · R_loop + Σ E = 0",
    "vars": [
      {
        "sym": "I_mesh",
        "desc": "Assumed clockwise mesh current"
      },
      {
        "sym": "R_loop",
        "desc": "Resistors in that mesh path"
      }
    ],
    "notes": "Apply KVL to each independent mesh.",
    "example": "Two-mesh circuit → 2 simultaneous equations."
  },
  {
    "id": "f-nod-01",
    "section": "nodal",
    "secTitle": "Nodal Analysis",
    "name": "Nodal Voltage Method",
    "formula": "Σ (V_node − V_adj) / R + Σ I_source = 0",
    "vars": [
      {
        "sym": "V_node",
        "desc": "Unknown node voltage"
      },
      {
        "sym": "V_adj",
        "desc": "Adjacent node voltage (0 V if ground)"
      }
    ],
    "notes": "Apply KCL at each non-reference node.",
    "example": "Supernode used when voltage source between nodes."
  },
  {
    "id": "f-div-01",
    "section": "divider",
    "secTitle": "Voltage & Current Dividers",
    "name": "Voltage Divider",
    "formula": "V_x = V_T · R_x / (R₁ + R₂ + …)",
    "vars": [
      {
        "sym": "V_x",
        "desc": "Voltage across R_x"
      },
      {
        "sym": "V_T",
        "desc": "Total series voltage"
      }
    ],
    "notes": "Only for series-connected resistors.",
    "example": "R₁=1 kΩ, R₂=3 kΩ, V_T=8 V → V₁=2 V"
  },
  {
    "id": "f-div-02",
    "section": "divider",
    "secTitle": "Voltage & Current Dividers",
    "name": "Current Divider (two)",
    "formula": "I₁ = I_T · R₂ / (R₁ + R₂)",
    "vars": [
      {
        "sym": "I₁",
        "desc": "Current through R₁"
      },
      {
        "sym": "I_T",
        "desc": "Total parallel current"
      }
    ],
    "notes": "Inverse proportion to resistance.",
    "example": "I_T=6 A, R₁=2 Ω, R₂=4 Ω → I₁=4 A"
  },
  {
    "id": "f-wye-01",
    "section": "wye",
    "secTitle": "Wye-Delta & Bridges",
    "name": "Delta to Wye (R₁ opposite R_A)",
    "formula": "R_A = (R₁·R₂) / (R₁+R₂+R₃)",
    "vars": [
      {
        "sym": "R_A",
        "desc": "Wye leg opposite delta side R₁"
      }
    ],
    "notes": "Product of adjacent / sum of all three.",
    "example": "Equal delta R → wye R/3 each."
  },
  {
    "id": "f-wye-02",
    "section": "wye",
    "secTitle": "Wye-Delta & Bridges",
    "name": "Wheatstone Bridge Balance",
    "formula": "R₁/R₂ = R₃/R₄",
    "vars": [
      {
        "sym": "R₁…R₄",
        "desc": "Bridge arms"
      }
    ],
    "notes": "Galvanometer reads zero when balanced.",
    "example": "R₁=100, R₂=200, R₃=150 → R₄=300 Ω for balance."
  }
];
