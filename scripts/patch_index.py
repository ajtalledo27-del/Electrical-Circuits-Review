# -*- coding: utf-8 -*-
"""Patch index.html for Electrical Circuits 1 reviewer + Formula Bank + Lecture Text."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
html = (ROOT / "index.html").read_text(encoding="utf-8")

# Theme: electric blue / amber
html = re.sub(r"#00695c", "#1565c0", html)
html = re.sub(r"#004d40", "#0d47a1", html)
html = re.sub(r"#00796b", "#1976d2", html)
html = re.sub(r"#80cbc4", "#90caf9", html)
html = re.sub(r"#b2dfdb", "#bbdefb", html)
html = re.sub(r"#e0f2f1", "#e3f2fd", html)
html = re.sub(r"#f1f8f6", "#e8f4fd", html)
html = re.sub(r"#1b5e20", "#e65100", html)
html = re.sub(r"#2e7d32", "#ef6c00", html)
html = re.sub(r"#a5d6a7", "#ffcc80", html)
html = html.replace('content="#00695c"', 'content="#1565c0"')

html = html.replace(
    "<title>Engineering Economy Part 1 — Reviewer, Formula Bank &amp; Quiz</title>",
    "<title>Electrical Circuits 1 — Reviewer, Formula Bank &amp; Quiz</title>",
)
html = html.replace(
    'content="Engineering Economy Part 1 reviewer — interest, annuities, depreciation, PW/AW/IRR/B-C, formula bank and quiz bee"',
    'content="Electrical Circuits 1 reviewer — Ohm\'s law, KVL, KCL, series/parallel, mesh & nodal analysis, formula bank and quiz bee"',
)
html = html.replace('apple-mobile-web-app-title" content="EngEcon"', 'apple-mobile-web-app-title" content="Circuits"')
html = html.replace("📐 EngEcon Navigation", "⚡ Circuits Navigation")
html = html.replace('<span class="mode-badge">📐 ENG ECON</span>', '<span class="mode-badge">⚡ CIRCUITS 1</span>')

html = re.sub(
    r'<ul id="toc-materials"[^>]*>.*?</ul>',
    '''<ul id="toc-materials" style="list-style:none;padding:6px 0">
<li class="gh"><a href="#">LECTURE VIDEOS</a></li>
<li><a href="materials/ELECTRICAL_CIRCUITS_1_(PART_1)_(2).mp4" target="_blank" rel="noopener">📹 Part 1 Video (MP4)</a></li>
<li><a href="materials/ELECTRICAL_CIRCUITS_1_(PART_2)_(2).mp4" target="_blank" rel="noopener">📹 Part 2 Video (MP4)</a></li>
</ul>''',
    html,
    count=1,
    flags=re.DOTALL,
)

html = html.replace("EngEcon Part 1", "Circuits 1")
html = html.replace(
    'id="bank-desc">Engineering Economy Part 1 — MCQs, compiled <strong>Formula Bank</strong>, and lecture video. Use sidebar to jump between topics and formulas.</p>',
    'id="bank-desc">Electrical Circuits 1 (Parts 1 &amp; 2) — MCQs, compiled <strong>Formula Bank</strong>, and full lecture transcript. Use sidebar to jump between topics and formulas.</p>',
)
html = html.replace('<div class="sn" id="topic-count">8</div>', '<div class="sn" id="topic-count">10</div>')

html = html.replace("<h1>📐 Engineering Economy Part 1</h1>", "<h1>⚡ Electrical Circuits 1</h1>")
html = html.replace(
    '<p class="sub"><strong>Engineering Economy Part 1</strong> — interest, annuities, gradients, depreciation, and project evaluation. Includes a searchable <strong>Formula Bank</strong>.</p>',
    '<p class="sub"><strong>Electrical Circuits 1</strong> — Ohm\'s law, series &amp; parallel circuits, KVL, KCL, mesh &amp; nodal analysis. Includes <strong>Formula Bank</strong> and full lecture text from Parts 1 &amp; 2.</p>',
)
html = html.replace(
    '<p>Browse MCQs with solutions tied to formulas and factor tables.</p>',
    '<p>Browse MCQs with solutions tied to circuit laws and analysis methods.</p>',
)
html = html.replace(
    '<p>Compiled formulas — interest, annuities, depreciation, PW, AW, IRR, B/C — with variables and examples.</p>',
    '<p>Compiled formulas — Ohm\'s law, KVL, KCL, dividers, mesh/nodal — with variables and examples.</p>',
)
html = html.replace(
    '<span class="tag" style="background:#004d40;color:#80cbc4">Quick Reference</span>',
    '<span class="tag" style="background:#0d47a1;color:#90caf9">Quick Reference</span>',
)
html = html.replace(
    '<p>Full transcript copied from the Part 1 video — searchable, section by section.</p>',
    '<p>Full transcript from Parts 1 &amp; 2 — searchable, section by section with timestamps.</p>',
)

html = html.replace("window.ENGECON_QB", "window.CIRCUITS_QB")
html = html.replace("window.ENGECON_FORMULAS", "window.CIRCUITS_FORMULAS")
html = html.replace("window.ENGECON_LECTURE", "window.CIRCUITS_LECTURE")
html = html.replace("'engecon_board'", "'circuits_board'")
html = html.replace("'engecon_dark'", "'circuits_dark'")
html = html.replace("'engecon_active_bank'", "'circuits_active_bank'")

old_bank = """var ACTIVE_BANK='reviewer';
var LOADED_BANKS={reviewer:true};
var FORMULA_VIEW=false;
var LECTURE_VIEW=false;
var BANK_DEFS={
  reviewer:{
    label:'Circuits 1',
    short:'EngEcon',
    desc:'Engineering Economy Part 1 — video lecture + formula bank + MCQs.',
    global:'ENGECON_QB',
    file:null,
    groups:[
      {grp:'Fundamentals',sids:['tvm','interest','effective','pwfw']},
      {grp:'Series & Assets',sids:['annuity','gradient','depreciation']},
      {grp:'Evaluation',sids:['eval']}
    ],
    order:['tvm','interest','effective','pwfw','annuity','gradient','depreciation','eval']
  }
};"""

new_bank = """var ACTIVE_BANK='reviewer';
var LOADED_BANKS={reviewer:true};
var FORMULA_VIEW=false;
var LECTURE_VIEW=false;
var BANK_DEFS={
  reviewer:{
    label:'Circuits 1',
    short:'Circuits',
    desc:'Electrical Circuits 1 — Parts 1 & 2 video lectures + formula bank + MCQs.',
    global:'CIRCUITS_QB',
    file:null,
    groups:[
      {grp:'Fundamentals',sids:['basic','ohm','series','parallel']},
      {grp:'Circuit Laws',sids:['kvl','kcl','mesh','nodal']},
      {grp:'Advanced',sids:['divider','wye']}
    ],
    order:['basic','ohm','series','parallel','kvl','kcl','mesh','nodal','divider','wye']
  }
};"""

html = html.replace(old_bank, new_bank)

html = html.replace(
    "if(bd)bd.innerHTML='📝 <strong>Lecture Text</strong> — full transcript from the Part 1 video. Search filters lines below.';",
    "if(bd)bd.innerHTML='📝 <strong>Lecture Text</strong> — full transcript from Parts 1 & 2. Search filters lines below.';",
)
html = html.replace(
    "if(bd)bd.innerHTML='📐 <strong>Formula Bank</strong> — compiled Engineering Economy Part 1 formulas. Click any card to expand. Search filters MCQs in Reviewer mode.';",
    "if(bd)bd.innerHTML='📐 <strong>Formula Bank</strong> — compiled Electrical Circuits 1 formulas. Click any card to expand. Search filters in current view.';",
)
html = html.replace(
    "if(el){el.scrollIntoView({behavior:'smooth',block:'start'});el.style.outline='2px solid #00796b';}",
    "if(el){el.scrollIntoView({behavior:'smooth',block:'start'});el.style.outline='2px solid #1976d2';}",
)

html = html.replace(
    "function getFormulas(){return window.ENGECON_FORMULAS||[];}",
    "function getFormulas(){return window.CIRCUITS_FORMULAS||[];}",
)
html = html.replace(
    "var data=window.ENGECON_LECTURE||{};",
    "var data=window.CIRCUITS_LECTURE||{};",
)

html = html.replace(
    "if(localStorage.getItem('engecon_dark')==='1') document.body.classList.add('dark');",
    "if(localStorage.getItem('circuits_dark')==='1') document.body.classList.add('dark');",
)
html = html.replace(
    "var savedBank=localStorage.getItem('engecon_active_bank');",
    "var savedBank=localStorage.getItem('circuits_active_bank');",
)

html = html.replace("⚖️ EngEcon Part 1", "⚡ Circuits 1")

(ROOT / "index.html").write_text(html, encoding="utf-8")
print("Patched index.html for Electrical Circuits 1")
