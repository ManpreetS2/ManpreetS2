#!/usr/bin/env python3
"""
Generate Manpreet Singh profile SVG suite.

Design principles (from studying Sharann-del, adapted with color):
- Almost all content lives in purpose-built SVGs, not Markdown cards
- Fixed editorial margins on a 1000-wide canvas (48–952)
- Monospace editorial voice + strong display type in hero/flagship
- Numbered section identities (01–05) as ghost numerals
- Meaningful system-map geometry, not decoration
- Separate light/dark files with hardcoded colors (camo-safe)
- Mobile variants (390-wide) with larger type / stacked layouts
- Fail-safe motion: resting CSS = final visible state; animate only
  under prefers-reduced-motion: no-preference
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = {
    ("desktop", "light"): ROOT / "assets/editorial/light",
    ("desktop", "dark"): ROOT / "assets/editorial/dark",
    ("mobile", "light"): ROOT / "assets/editorial/mobile/light",
    ("mobile", "dark"): ROOT / "assets/editorial/mobile/dark",
}

PALETTE = {
    "light": {
        "ink": "#0F1729",
        "muted": "#4E596E",
        "dim": "#6E7890",
        "rule": "#B8C2D4",
        "ghost": "#C5CEE0",
        "cyan": "#0B8F8A",
        "lavender": "#5F4F8F",
        "coral": "#B85040",
        "node": "#F0F4FA",
        "soft": "#E4EAF5",
    },
    "dark": {
        "ink": "#E8EEF8",
        "muted": "#8A96AB",
        "dim": "#6A768C",
        "rule": "#3A4F6C",
        "ghost": "#2A3D5C",
        "cyan": "#3DDBD9",
        "lavender": "#B8A9E8",
        "coral": "#E08A7A",
        "node": "#121E33",
        "soft": "#1A2740",
    },
}

MONO = 'ui-monospace,"SFMono-Regular","SF Mono",Menlo,Consolas,"Liberation Mono",monospace'
SANS = 'ui-sans-serif,"Segoe UI",Roboto,Helvetica,Arial,sans-serif'


def css(c: dict, draw_len: int = 1000, animate: bool = True) -> str:
    """Hardcoded palette + fail-safe animation block."""
    anim = ""
    if animate:
        anim = f"""
    .draw {{ stroke-dasharray:{draw_len}; stroke-dashoffset:0; }}
    .rise,.fade,.pop,.row {{ opacity:1; }}
    .flow {{ stroke-dasharray:3 9; opacity:.35; }}
    .pulse {{ opacity:1; }}
    .caret {{ opacity:1; }}
    @keyframes draw {{ from {{ stroke-dashoffset:{draw_len}; }} to {{ stroke-dashoffset:0; }} }}
    @keyframes rise {{ from {{ opacity:0; }} to {{ opacity:1; }} }}
    @keyframes fade {{ from {{ opacity:0; }} to {{ opacity:1; }} }}
    @keyframes pop {{ from {{ opacity:0; }} to {{ opacity:1; }} }}
    @keyframes march {{ to {{ stroke-dashoffset:-12; }} }}
    @keyframes pulse {{ 0%,100% {{ opacity:.55; }} 50% {{ opacity:1; }} }}
    @keyframes blink {{ 0%,49% {{ opacity:1; }} 50%,100% {{ opacity:0; }} }}
    .a1{{animation-delay:.08s}}.a2{{animation-delay:.2s}}.a3{{animation-delay:.35s}}
    .a4{{animation-delay:.5s}}.a5{{animation-delay:.65s}}.a6{{animation-delay:.8s}}
    .w1{{animation-delay:.15s}}.w2{{animation-delay:.28s}}.w3{{animation-delay:.4s}}
    .w4{{animation-delay:.52s}}.w5{{animation-delay:.64s}}.w6{{animation-delay:.76s}}
    .p0{{animation-delay:.1s}}.p1{{animation-delay:.45s}}.p2{{animation-delay:.55s}}
    .p3{{animation-delay:.65s}}.p4{{animation-delay:.75s}}.p5{{animation-delay:.85s}}
    .p6{{animation-delay:.95s}}.p7{{animation-delay:1.05s}}.p8{{animation-delay:1.15s}}
    .r1{{animation-delay:.05s}}.r2{{animation-delay:.12s}}.r3{{animation-delay:.19s}}
    .r4{{animation-delay:.26s}}.r5{{animation-delay:.33s}}
    /* forwards (not both): resting CSS stays visible if animation is
       delayed, paused offscreen, or unsupported — critical for GitHub. */
    @media (prefers-reduced-motion:no-preference) {{
      .draw {{ animation:draw 1.2s cubic-bezier(.6,0,.2,1) forwards; }}
      .rise {{ animation:rise .65s cubic-bezier(.2,.7,.2,1) forwards; }}
      .fade {{ animation:fade .55s ease forwards; }}
      .pop {{ animation:pop .65s cubic-bezier(.2,.7,.2,1) forwards; }}
      .row {{ animation:rise .5s cubic-bezier(.2,.7,.2,1) forwards; }}
      .flow {{ animation:march 1.4s linear infinite; }}
      .pulse {{ animation:pulse 2.6s ease-in-out infinite; }}
      .caret {{ animation:blink 1.05s steps(1,end) infinite; }}
    }}
"""
    return f"""
    .mono {{ font-family:{MONO}; }}
    .sans {{ font-family:{SANS}; }}
    {anim}
"""


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)}")


# ─── DESKTOP (1000-wide, Sharann geometry) ───────────────────────────────────

def hero_desktop(c: dict) -> str:
    # Distinctive animated graphic: evidence → systems → control pipeline
    # representing full-stack, AI, and fintech interests (right plane).
    return f'''<svg viewBox="0 0 1000 440" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Manpreet Singh — software engineering, AI systems, fintech">
  <defs>
    <style>{css(c, 1000)}</style>
  </defs>
  <line class="draw a1" x1="48" y1="56" x2="952" y2="56" stroke="{c['rule']}" stroke-width="1"/>
  <g class="fade a1 mono">
    <text x="48" y="40" fill="{c['muted']}" font-size="11" letter-spacing="3.5">PORTFOLIO — INDEX Nº 001</text>
    <text x="952" y="40" fill="{c['muted']}" font-size="11" letter-spacing="3.5" text-anchor="end">BAY AREA, CA</text>
  </g>
  <g class="fade a2 mono"><text x="48" y="108" fill="{c['cyan']}" font-size="14" letter-spacing="4">HELLO, I'M</text></g>
  <g class="rise a3">
    <text class="sans" x="46" y="178" fill="{c['ink']}" font-size="64" font-weight="700" letter-spacing="-2.2">Manpreet Singh</text>
    <rect class="caret" x="528" y="134" width="3" height="46" rx="1" fill="{c['cyan']}"/>
  </g>
  <g class="fade a4 mono">
    <text x="48" y="216" fill="{c['muted']}" font-size="16">Software · AI systems · Fintech tooling</text>
  </g>
  <g class="fade a5 mono">
    <text x="48" y="262" fill="{c['dim']}" font-size="12" letter-spacing="1">focus  ▸</text>
    <text x="120" y="262" fill="{c['ink']}" font-size="12">evidence-backed products · reliable workflows · human control</text>
  </g>
  <g class="fade a5 mono">
    <text x="48" y="288" fill="{c['dim']}" font-size="12" letter-spacing="1">open to software engineering · solutions engineering · internships</text>
  </g>

  <!-- interest diagram (animated line art) -->
  <g aria-hidden="true">
    <line class="draw w1" x1="720" y1="120" x2="820" y2="170" stroke="{c['rule']}" stroke-width="1"/>
    <line class="draw w2" x1="920" y1="120" x2="820" y2="170" stroke="{c['rule']}" stroke-width="1"/>
    <line class="draw w3" x1="820" y1="200" x2="760" y2="260" stroke="{c['rule']}" stroke-width="1"/>
    <line class="draw w4" x1="820" y1="200" x2="880" y2="260" stroke="{c['rule']}" stroke-width="1"/>
    <line class="draw w5" x1="820" y1="200" x2="820" y2="300" stroke="{c['cyan']}" stroke-width="1.2"/>
    <line class="flow" x1="720" y1="120" x2="820" y2="170" stroke="{c['cyan']}"/>
    <line class="flow" x1="920" y1="120" x2="820" y2="170" stroke="{c['lavender']}"/>
    <line class="flow" x1="820" y1="200" x2="760" y2="260" stroke="{c['coral']}"/>
    <line class="flow" x1="820" y1="200" x2="880" y2="260" stroke="{c['cyan']}"/>
    <line class="flow" x1="820" y1="200" x2="820" y2="300" stroke="{c['lavender']}"/>
    <g class="pop p1">
      <rect x="668" y="96" width="104" height="36" rx="2" fill="{c['node']}" stroke="{c['cyan']}" stroke-opacity=".55"/>
      <text class="mono" x="715" y="118" fill="{c['ink']}" font-size="11" text-anchor="middle">EVIDENCE</text>
    </g>
    <g class="pop p2">
      <rect x="868" y="96" width="104" height="36" rx="2" fill="{c['node']}" stroke="{c['lavender']}" stroke-opacity=".55"/>
      <text class="mono" x="920" y="118" fill="{c['ink']}" font-size="11" text-anchor="middle">MODELS</text>
    </g>
    <g class="pop p0">
      <rect x="770" y="160" width="100" height="44" rx="2" fill="{c['soft']}" stroke="{c['rule']}"/>
      <text class="mono" x="820" y="180" fill="{c['ink']}" font-size="11" text-anchor="middle">SYSTEMS</text>
      <text class="mono" x="820" y="196" fill="{c['muted']}" font-size="9" text-anchor="middle">compose · verify</text>
    </g>
    <g class="pop p3">
      <rect x="708" y="250" width="104" height="36" rx="2" fill="{c['node']}" stroke="{c['coral']}" stroke-opacity=".5"/>
      <text class="mono" x="760" y="272" fill="{c['ink']}" font-size="11" text-anchor="middle">PRODUCTS</text>
    </g>
    <g class="pop p4">
      <rect x="828" y="250" width="104" height="36" rx="2" fill="{c['node']}" stroke="{c['cyan']}" stroke-opacity=".5"/>
      <text class="mono" x="880" y="272" fill="{c['ink']}" font-size="11" text-anchor="middle">FINTECH</text>
    </g>
    <g class="pop p5">
      <rect x="758" y="300" width="124" height="36" rx="2" fill="{c['node']}" stroke="{c['lavender']}"/>
      <text class="mono" x="820" y="322" fill="{c['lavender']}" font-size="11" text-anchor="middle">HUMAN CONTROL</text>
    </g>
  </g>

  <line class="draw a6" x1="48" y1="356" x2="952" y2="356" stroke="{c['rule']}" stroke-width="1"/>
  <g class="fade a6 mono">
    <text x="48" y="388" fill="{c['cyan']}" font-size="11" letter-spacing="2.5">FULL-STACK SYSTEMS</text>
    <text x="250" y="388" fill="{c['rule']}" font-size="11">·</text>
    <text x="272" y="388" fill="{c['lavender']}" font-size="11" letter-spacing="2.5">EXPLAINABLE AI</text>
    <text x="458" y="388" fill="{c['rule']}" font-size="11">·</text>
    <text x="480" y="388" fill="{c['coral']}" font-size="11" letter-spacing="2.5">FINTECH RESEARCH</text>
    <text x="952" y="388" fill="{c['muted']}" font-size="11" letter-spacing="2" text-anchor="end">DE ANZA → SJSU / 2027</text>
  </g>
  <g class="fade a6 mono">
    <text x="48" y="420" fill="{c['dim']}" font-size="11" letter-spacing="2">github.com/ManpreetS2</text>
  </g>
</svg>'''


def section(num: str, label: str, hint: str, c: dict) -> str:
    return f'''<svg viewBox="0 0 1000 92" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Section {num} — {label}">
  <defs><style>{css(c, 760)}</style></defs>
  <g class="fade a1 mono">
    <text x="48" y="68" fill="{c['ghost']}" font-size="52" font-weight="600">{num}</text>
    <text x="148" y="56" fill="{c['cyan']}" font-size="14" letter-spacing="5.5">{label}</text>
    <text x="952" y="56" fill="{c['dim']}" font-size="11" letter-spacing="2" text-anchor="end">{hint}</text>
  </g>
  <line class="draw a2" x1="268" y1="50" x2="820" y2="50" stroke="{c['rule']}" stroke-width="1"/>
</svg>'''


def whoami(c: dict) -> str:
    return f'''<svg viewBox="0 0 1000 250" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="About Manpreet Singh">
  <defs><style>{css(c)}</style></defs>
  <text class="mono rise a1" x="48" y="36" fill="{c['ink']}" font-size="16">Computer Science @ De Anza College · Incoming San José State University, Spring 2027.</text>
  <text class="mono rise a2" x="48" y="66" fill="{c['ink']}" font-size="16">I build practical software, AI-powered tools, and systems designed around reliability.</text>
  <text class="mono rise a3" x="48" y="96" fill="{c['muted']}" font-size="15">Prefer products where claims stay grounded in evidence and humans keep final control.</text>
  <line class="fade a4" x1="48" y1="126" x2="952" y2="126" stroke="{c['rule']}" stroke-width="1" opacity=".7"/>
  <text class="mono rise a4" x="48" y="160" fill="{c['dim']}" font-size="11" letter-spacing="2.5">FOCUS</text>
  <text class="mono rise a4" x="148" y="160" fill="{c['ink']}" font-size="15">Full-stack systems · Explainable AI tooling · Fintech research · Local-first apps</text>
  <text class="mono rise a5" x="48" y="194" fill="{c['dim']}" font-size="11" letter-spacing="2.5">STATUS</text>
  <text class="mono rise a5" x="148" y="194" fill="{c['cyan']}" font-size="15">Open to software engineering, solutions engineering, and technical internships</text>
  <text class="mono rise a6" x="48" y="228" fill="{c['dim']}" font-size="11" letter-spacing="2.5">EDU</text>
  <text class="mono rise a6" x="148" y="228" fill="{c['ink']}" font-size="15">De Anza College → San José State University / Spring 2027</text>
</svg>'''


def system_map(c: dict) -> str:
    # Meaningful relationships: CareerPilot bridges products↔evidence↔control;
    # IntegrationLab shares evidence patterns; R.E.A.C.T./Minecraft share AI;
    # EquityTrace/Banking share quantitative rigor.
    return f'''<svg viewBox="0 0 1000 660" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="System map of Manpreet Singh's engineering work">
  <defs>
    <style>{css(c, 600)}</style>
    <mask id="cut" maskUnits="userSpaceOnUse" x="0" y="0" width="1000" height="660">
      <rect width="1000" height="660" fill="white"/>
      <rect x="395" y="248" width="210" height="64" fill="black"/>
      <rect x="110" y="110" width="180" height="56" fill="black"/>
      <rect x="48" y="186" width="150" height="44" fill="black"/>
      <rect x="210" y="186" width="150" height="44" fill="black"/>
      <rect x="710" y="110" width="180" height="56" fill="black"/>
      <rect x="690" y="186" width="240" height="44" fill="black"/>
      <rect x="110" y="380" width="180" height="56" fill="black"/>
      <rect x="100" y="452" width="210" height="44" fill="black"/>
      <rect x="710" y="380" width="180" height="56" fill="black"/>
      <rect x="720" y="452" width="190" height="44" fill="black"/>
      <rect x="370" y="500" width="260" height="56" fill="black"/>
    </mask>
  </defs>
  <line x1="48" y1="36" x2="952" y2="36" stroke="{c['rule']}"/>
  <text class="mono fade a1" x="48" y="24" fill="{c['muted']}" font-size="11" letter-spacing="3.2">SYSTEM MAP — HOW THE WORK CONNECTS</text>
  <text class="mono fade a1" x="952" y="24" fill="{c['muted']}" font-size="11" letter-spacing="3.2" text-anchor="end">FIG. 01</text>

  <g mask="url(#cut)">
    <line class="draw w1" x1="420" y1="248" x2="245" y2="166" stroke="{c['rule']}" stroke-width="1"/>
    <line class="draw w2" x1="580" y1="248" x2="755" y2="166" stroke="{c['rule']}" stroke-width="1"/>
    <line class="draw w3" x1="420" y1="312" x2="245" y2="380" stroke="{c['rule']}" stroke-width="1"/>
    <line class="draw w4" x1="580" y1="312" x2="755" y2="380" stroke="{c['rule']}" stroke-width="1"/>
    <line class="draw w5" x1="500" y1="312" x2="500" y2="500" stroke="{c['cyan']}" stroke-width="1.3"/>
    <line class="draw w6" x1="200" y1="166" x2="123" y2="186" stroke="{c['rule']}" stroke-width="1"/>
    <line class="draw w6" x1="200" y1="166" x2="285" y2="186" stroke="{c['rule']}" stroke-width="1"/>
    <line class="draw w6" x1="800" y1="166" x2="810" y2="186" stroke="{c['rule']}" stroke-width="1"/>
    <line class="draw w6" x1="200" y1="436" x2="205" y2="452" stroke="{c['rule']}" stroke-width="1"/>
    <line class="draw w6" x1="800" y1="436" x2="815" y2="452" stroke="{c['rule']}" stroke-width="1"/>
    <line class="flow" x1="420" y1="248" x2="245" y2="166" stroke="{c['cyan']}"/>
    <line class="flow" x1="580" y1="248" x2="755" y2="166" stroke="{c['lavender']}"/>
    <line class="flow" x1="420" y1="312" x2="245" y2="380" stroke="{c['coral']}"/>
    <line class="flow" x1="580" y1="312" x2="755" y2="380" stroke="{c['cyan']}"/>
    <line class="flow" x1="500" y1="312" x2="500" y2="500" stroke="{c['lavender']}"/>
  </g>

  <text class="mono pop p1" x="200" y="92" fill="{c['cyan']}" font-size="10" letter-spacing="2.5" text-anchor="middle">FULL-STACK PRODUCTS</text>
  <text class="mono pop p2" x="800" y="92" fill="{c['lavender']}" font-size="10" letter-spacing="2.5" text-anchor="middle">AI EXPERIMENTATION</text>
  <text class="mono pop p3" x="200" y="548" fill="{c['coral']}" font-size="10" letter-spacing="2.5" text-anchor="middle">RELIABLE INTEGRATIONS</text>
  <text class="mono pop p4" x="800" y="548" fill="{c['cyan']}" font-size="10" letter-spacing="2.5" text-anchor="middle">QUANTITATIVE RESEARCH</text>
  <text class="mono pop p5" x="500" y="590" fill="{c['lavender']}" font-size="10" letter-spacing="2.5" text-anchor="middle">FLAGSHIP HUB · CAREERPILOT</text>

  <g class="pop p0">
    <rect x="395" y="248" width="210" height="64" rx="2" fill="{c['node']}" stroke="{c['rule']}"/>
    <text class="mono" x="500" y="276" fill="{c['ink']}" font-size="13" letter-spacing="2" text-anchor="middle">MANPREET.SYS</text>
    <text class="mono" x="500" y="296" fill="{c['muted']}" font-size="9" letter-spacing=".5" text-anchor="middle">evidence → systems → control</text>
  </g>

  <g class="pop p1">
    <rect x="110" y="110" width="180" height="56" rx="2" fill="{c['node']}" stroke="{c['cyan']}" stroke-opacity=".55"/>
    <text class="mono" x="200" y="134" fill="{c['ink']}" font-size="12" text-anchor="middle">CareerPilot</text>
    <text class="mono" x="200" y="152" fill="{c['muted']}" font-size="9" text-anchor="middle">job search · Fit · extension</text>
  </g>
  <g class="pop p1">
    <rect x="48" y="186" width="150" height="44" rx="2" fill="{c['node']}" stroke="{c['rule']}"/>
    <text class="mono" x="123" y="206" fill="{c['ink']}" font-size="11" text-anchor="middle">StrikeCaller</text>
    <text class="mono" x="123" y="222" fill="{c['dim']}" font-size="9" text-anchor="middle">spoken coaching</text>
  </g>
  <g class="pop p1">
    <rect x="210" y="186" width="150" height="44" rx="2" fill="{c['node']}" stroke="{c['rule']}"/>
    <text class="mono" x="285" y="206" fill="{c['ink']}" font-size="11" text-anchor="middle">PagePulse</text>
    <text class="mono" x="285" y="222" fill="{c['dim']}" font-size="9" text-anchor="middle">change evidence</text>
  </g>

  <g class="pop p2">
    <rect x="710" y="110" width="180" height="56" rx="2" fill="{c['node']}" stroke="{c['lavender']}" stroke-opacity=".6"/>
    <text class="mono" x="800" y="134" fill="{c['ink']}" font-size="12" text-anchor="middle">R.E.A.C.T.</text>
    <text class="mono" x="800" y="152" fill="{c['muted']}" font-size="9" text-anchor="middle">reward · controllers</text>
  </g>
  <g class="pop p2">
    <rect x="690" y="186" width="240" height="44" rx="2" fill="{c['node']}" stroke="{c['rule']}"/>
    <text class="mono" x="810" y="206" fill="{c['ink']}" font-size="11" text-anchor="middle">Minecraft AI Civilization</text>
    <text class="mono" x="810" y="222" fill="{c['dim']}" font-size="9" text-anchor="middle">multi-agent simulation</text>
  </g>

  <g class="pop p3">
    <rect x="110" y="380" width="180" height="56" rx="2" fill="{c['node']}" stroke="{c['coral']}" stroke-opacity=".55"/>
    <text class="mono" x="200" y="404" fill="{c['ink']}" font-size="12" text-anchor="middle">IntegrationLab</text>
    <text class="mono" x="200" y="422" fill="{c['muted']}" font-size="9" text-anchor="middle">webhooks · evidence store</text>
  </g>
  <g class="pop p3">
    <rect x="100" y="452" width="210" height="44" rx="2" fill="{c['node']}" stroke="{c['rule']}"/>
    <text class="mono" x="205" y="472" fill="{c['ink']}" font-size="11" text-anchor="middle">System Down Simulator</text>
    <text class="mono" x="205" y="488" fill="{c['dim']}" font-size="9" text-anchor="middle">incident response game</text>
  </g>

  <g class="pop p4">
    <rect x="710" y="380" width="180" height="56" rx="2" fill="{c['node']}" stroke="{c['cyan']}" stroke-opacity=".5"/>
    <text class="mono" x="800" y="404" fill="{c['ink']}" font-size="12" text-anchor="middle">EquityTrace</text>
    <text class="mono" x="800" y="422" fill="{c['muted']}" font-size="9" text-anchor="middle">SEC filings · factors</text>
  </g>
  <g class="pop p4">
    <rect x="720" y="452" width="190" height="44" rx="2" fill="{c['node']}" stroke="{c['rule']}"/>
    <text class="mono" x="815" y="472" fill="{c['ink']}" font-size="11" text-anchor="middle">Java Banking System</text>
    <text class="mono" x="815" y="488" fill="{c['dim']}" font-size="9" text-anchor="middle">atomic transfers</text>
  </g>

  <g class="pop p5">
    <rect x="370" y="500" width="260" height="56" rx="2" fill="{c['soft']}" stroke="{c['lavender']}"/>
    <text class="mono" x="500" y="524" fill="{c['lavender']}" font-size="12" letter-spacing="1" text-anchor="middle">CareerPilot hub</text>
    <text class="mono" x="500" y="542" fill="{c['muted']}" font-size="9" text-anchor="middle">products ↔ evidence ↔ human control</text>
  </g>

  <line x1="48" y1="620" x2="952" y2="620" stroke="{c['rule']}"/>
  <text class="mono" x="48" y="644" fill="{c['dim']}" font-size="10" letter-spacing="1.5">WIRES — SHARED IDEAS · EVIDENCE PATTERNS · CONTROL LOOPS</text>
  <text class="mono" x="952" y="644" fill="{c['dim']}" font-size="10" letter-spacing="2" text-anchor="end">ORIGINAL DIAGRAM</text>
</svg>'''


def flagship_meta(c: dict) -> str:
    return f'''<svg viewBox="0 0 1000 200" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="CareerPilot flagship meta">
  <defs><style>{css(c)}</style></defs>
  <line class="draw a1" x1="48" y1="28" x2="952" y2="28" stroke="{c['rule']}" stroke-width="1"/>
  <text class="mono fade a1" x="48" y="18" fill="{c['cyan']}" font-size="12" letter-spacing="3.2">FLAGSHIP · CAREERPILOT</text>
  <text class="mono fade a1" x="952" y="18" fill="{c['lavender']}" font-size="11" letter-spacing="2" text-anchor="end">LOCAL / SELF-HOSTABLE</text>
  <text class="sans rise a2" x="48" y="78" fill="{c['ink']}" font-size="36" font-weight="700" letter-spacing="-1">Evidence-driven job search</text>
  <text class="sans rise a2" x="48" y="118" fill="{c['ink']}" font-size="36" font-weight="700" letter-spacing="-1">workspace</text>
  <text class="mono fade a3" x="48" y="152" fill="{c['muted']}" font-size="14">Python · FastAPI · React · TypeScript · SQLite · Chrome Extension</text>
  <text class="mono fade a4" x="48" y="178" fill="{c['dim']}" font-size="12">Grounded profiles · deterministic Fit · human-approved applications</text>
  <g class="fade a4 mono">
    <text x="700" y="78" fill="{c['dim']}" font-size="10" letter-spacing="2">STACK TRACE</text>
    <text x="700" y="102" fill="{c['cyan']}" font-size="12">01  Fit engine</text>
    <text x="700" y="124" fill="{c['lavender']}" font-size="12">02  Search workflow</text>
    <text x="700" y="146" fill="{c['coral']}" font-size="12">03  Chrome assist</text>
  </g>
  <line class="draw a4" x1="48" y1="192" x2="952" y2="192" stroke="{c['rule']}" stroke-width="1"/>
</svg>'''


def flagship_frame(c: dict) -> str:
    """Thin editorial frame placed above the real product screenshot."""
    return f'''<svg viewBox="0 0 1000 36" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="CareerPilot product screenshot label">
  <defs><style>{css(c, 400, animate=False)}</style></defs>
  <text class="mono" x="48" y="22" fill="{c['dim']}" font-size="11" letter-spacing="2.5">PRODUCT SCREENSHOT — DISCOVER WORKSPACE</text>
  <text class="mono" x="952" y="22" fill="{c['muted']}" font-size="11" letter-spacing="2" text-anchor="end">LIVE UI</text>
</svg>'''


def flagship_points(c: dict) -> str:
    rows = [
        ("01 / FIT", c["cyan"], "Explainable, evidence-based Fit scoring grounded in resume and posting text"),
        ("02 / WORKFLOW", c["lavender"], "Complete job-search loop: discover → analyze → prepare → track"),
        ("03 / EXTENSION", c["coral"], "Human-controlled Chrome extension that assists fills and never submits"),
    ]
    parts = []
    y = 36
    for i, (lab, col, txt) in enumerate(rows):
        delay = f"r{i+1}"
        parts.append(f'''<g class="row {delay} mono">
    <text x="48" y="{y}" fill="{col}" font-size="14" letter-spacing="2.5">{lab}</text>
    <text x="230" y="{y}" fill="{c['ink']}" font-size="15">{txt}</text>
    <line x1="48" y1="{y+20}" x2="952" y2="{y+20}" stroke="{c['rule']}" stroke-width="1" opacity=".55"/>
  </g>''')
        y += 56
    return f'''<svg viewBox="0 0 1000 220" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="CareerPilot three engineering highlights">
  <defs><style>{css(c)}</style></defs>
  <text class="mono fade a1" x="48" y="18" fill="{c['dim']}" font-size="11" letter-spacing="3">THREE ENGINEERING HIGHLIGHTS</text>
  {''.join(parts)}
</svg>'''


def projects_dir(c: dict) -> str:
    items = [
        (
            "01 / INTEGRATIONLAB",
            "Self-hosted console for diagnosing API and webhook failures",
            "with stored evidence, signed webhooks, and retry handling.",
            "FASTAPI · POSTGRESQL · REACT · DOCKER",
            "PRODUCT SCREENSHOT",
        ),
        (
            "02 / R.E.A.C.T.",
            "Research prototype: does numerical reward feedback change",
            "language-model controller revisions in a physics simulator?",
            "PYTHON · LUNARLANDER · RESEARCH PROTOTYPE",
            "CONCEPT ART",
        ),
        (
            "03 / EQUITYTRACE",
            "Point-in-time stock research from SEC filings, auditable",
            "financial factors, and transparent portfolio backtesting.",
            "PYTHON · SEC XBRL · DUCKDB",
            "CONCEPT ART",
        ),
        (
            "04 / MINECRAFT AI CIVILIZATION",
            "Multi-agent simulation with persistent memory, planning,",
            "and actions inside a shared Minecraft world — in development.",
            "TYPESCRIPT · MINEFLAYER · SQLITE",
            "CONCEPT ART",
        ),
    ]
    parts = []
    y0 = 20
    for i, (title, line1, line2, meta, note) in enumerate(items):
        y = y0 + i * 130
        delay = f"r{i+1}"
        accent = c["cyan"] if i % 2 == 0 else c["lavender"]
        parts.append(f'''<g class="row {delay} mono">
    <text x="48" y="{y + 24}" fill="{c['ink']}" font-size="17" font-weight="700" letter-spacing=".6">{title}</text>
    <text x="952" y="{y + 24}" fill="{c['dim']}" font-size="10" letter-spacing="1.5" text-anchor="end">{note}</text>
    <text x="48" y="{y + 52}" fill="{c['muted']}" font-size="13">{line1}</text>
    <text x="48" y="{y + 72}" fill="{c['muted']}" font-size="13">{line2}</text>
    <text x="48" y="{y + 96}" fill="{accent}" font-size="11" letter-spacing=".4">{meta}</text>
    <line x1="48" y1="{y + 114}" x2="952" y2="{y + 114}" stroke="{c['rule']}" stroke-width="1"/>
  </g>''')
    return f'''<svg viewBox="0 0 1000 580" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Selected projects directory">
  <defs><style>{css(c)}</style></defs>
  {''.join(parts)}
  <text class="mono fade a5" x="48" y="560" fill="{c['dim']}" font-size="12" letter-spacing="1.2">ALSO · StrikeCaller · PagePulse · Java Banking System · System Down Simulator</text>
</svg>'''


def toolkit(c: dict) -> str:
    rows = [
        ("LANGUAGES", "Python · TypeScript · Java · JavaScript · SQL"),
        ("FRAMEWORKS", "FastAPI · React · Node.js · JavaFX"),
        ("DATA", "PostgreSQL · SQLite · DuckDB · SQLAlchemy"),
        ("TOOLING", "Git · Docker · GitHub Actions · pytest · Vitest · Playwright · JUnit"),
    ]
    parts = []
    for i, (lab, val) in enumerate(rows):
        y = 32 + i * 36
        parts.append(f'''<text class="mono rise a{i+1}" x="48" y="{y}" fill="{c['dim']}" font-size="12" letter-spacing="2">{lab}</text>
  <text class="mono rise a{i+1}" x="188" y="{y}" fill="{c['ink']}" font-size="15">{val}</text>''')
    return f'''<svg viewBox="0 0 1000 180" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Technical toolkit">
  <defs><style>{css(c)}</style></defs>
  <line x1="168" y1="8" x2="168" y2="168" stroke="{c['rule']}" stroke-width="1" opacity=".55"/>
  {''.join(parts)}
</svg>'''


def footer(c: dict) -> str:
    return f'''<svg viewBox="0 0 1000 120" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Status — available">
  <defs><style>{css(c)}</style></defs>
  <line class="draw a1" x1="48" y1="24" x2="952" y2="24" stroke="{c['rule']}" stroke-width="1"/>
  <circle class="pulse" cx="60" cy="64" r="4" fill="{c['cyan']}"/>
  <text class="mono fade a2" x="82" y="60" fill="{c['ink']}" font-size="12" letter-spacing="3">STATUS — AVAILABLE</text>
  <text class="mono fade a2" x="82" y="82" fill="{c['muted']}" font-size="12" letter-spacing="1">building traceable systems · open to internships</text>
  <text class="mono fade a3" x="952" y="70" fill="{c['muted']}" font-size="13" text-anchor="end">Manpreet Singh  ·  github.com/ManpreetS2</text>
</svg>'''


# ─── MOBILE (390-wide, larger type, stacked) ─────────────────────────────────

def hero_mobile(c: dict) -> str:
    return f'''<svg viewBox="0 0 390 520" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Manpreet Singh">
  <defs><style>{css(c, 340)}</style></defs>
  <line class="draw a1" x1="20" y1="40" x2="370" y2="40" stroke="{c['rule']}"/>
  <text class="mono fade a1" x="20" y="28" fill="{c['muted']}" font-size="11" letter-spacing="2">MS / PORTFOLIO</text>
  <text class="mono fade a2" x="20" y="78" fill="{c['cyan']}" font-size="13" letter-spacing="3">HELLO, I'M</text>
  <text class="sans rise a3" x="18" y="130" fill="{c['ink']}" font-size="36" font-weight="700" letter-spacing="-1.2">Manpreet</text>
  <text class="sans rise a3" x="18" y="176" fill="{c['ink']}" font-size="36" font-weight="700" letter-spacing="-1.2">Singh</text>
  <text class="mono fade a4" x="20" y="210" fill="{c['muted']}" font-size="14">Software · AI · Fintech</text>
  <text class="mono fade a5" x="20" y="244" fill="{c['ink']}" font-size="13">evidence-backed products</text>
  <text class="mono fade a5" x="20" y="266" fill="{c['ink']}" font-size="13">reliable workflows</text>
  <text class="mono fade a5" x="20" y="288" fill="{c['ink']}" font-size="13">human-in-the-loop systems</text>
  <!-- compact interest diagram -->
  <line class="draw w1" x1="60" y1="330" x2="195" y2="360" stroke="{c['rule']}"/>
  <line class="draw w2" x1="330" y1="330" x2="195" y2="360" stroke="{c['rule']}"/>
  <line class="draw w3" x1="195" y1="380" x2="195" y2="420" stroke="{c['cyan']}"/>
  <g class="pop p1"><rect x="20" y="310" width="80" height="28" rx="2" fill="{c['node']}" stroke="{c['cyan']}" stroke-opacity=".5"/>
    <text class="mono" x="60" y="328" fill="{c['ink']}" font-size="10" text-anchor="middle">EVIDENCE</text></g>
  <g class="pop p2"><rect x="290" y="310" width="80" height="28" rx="2" fill="{c['node']}" stroke="{c['lavender']}" stroke-opacity=".5"/>
    <text class="mono" x="330" y="328" fill="{c['ink']}" font-size="10" text-anchor="middle">MODELS</text></g>
  <g class="pop p0"><rect x="145" y="348" width="100" height="32" rx="2" fill="{c['soft']}" stroke="{c['rule']}"/>
    <text class="mono" x="195" y="368" fill="{c['ink']}" font-size="11" text-anchor="middle">SYSTEMS</text></g>
  <g class="pop p5"><rect x="130" y="420" width="130" height="28" rx="2" fill="{c['node']}" stroke="{c['lavender']}"/>
    <text class="mono" x="195" y="438" fill="{c['lavender']}" font-size="10" text-anchor="middle">HUMAN CONTROL</text></g>
  <line class="draw a6" x1="20" y1="468" x2="370" y2="468" stroke="{c['rule']}"/>
  <text class="mono fade a6" x="20" y="492" fill="{c['cyan']}" font-size="11" letter-spacing="1">FULL-STACK · AI · FINTECH</text>
  <text class="mono fade a6" x="20" y="512" fill="{c['dim']}" font-size="11">De Anza → SJSU / 2027 · open to internships</text>
</svg>'''


def whoami_mobile(c: dict) -> str:
    return f'''<svg viewBox="0 0 390 320" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="About Manpreet">
  <defs><style>{css(c)}</style></defs>
  <text class="mono rise a1" x="20" y="28" fill="{c['ink']}" font-size="14">CS @ De Anza College</text>
  <text class="mono rise a1" x="20" y="50" fill="{c['ink']}" font-size="14">Incoming SJSU, Spring 2027</text>
  <text class="mono rise a2" x="20" y="86" fill="{c['muted']}" font-size="13">Practical software, AI tools,</text>
  <text class="mono rise a2" x="20" y="106" fill="{c['muted']}" font-size="13">and reliable systems.</text>
  <text class="mono rise a3" x="20" y="136" fill="{c['dim']}" font-size="13">Evidence first. Humans in control.</text>
  <line x1="20" y1="160" x2="370" y2="160" stroke="{c['rule']}"/>
  <text class="mono rise a4" x="20" y="190" fill="{c['dim']}" font-size="11" letter-spacing="2">FOCUS</text>
  <text class="mono rise a4" x="20" y="212" fill="{c['ink']}" font-size="13">Full-stack · Explainable AI</text>
  <text class="mono rise a4" x="20" y="232" fill="{c['ink']}" font-size="13">Fintech research · Local-first</text>
  <text class="mono rise a5" x="20" y="262" fill="{c['dim']}" font-size="11" letter-spacing="2">STATUS</text>
  <text class="mono rise a5" x="20" y="284" fill="{c['cyan']}" font-size="13">Open to SE / solutions / internships</text>
  <text class="mono rise a6" x="20" y="310" fill="{c['dim']}" font-size="12">EDU · De Anza → SJSU / 2027</text>
</svg>'''


def system_map_mobile(c: dict) -> str:
    return f'''<svg viewBox="0 0 390 520" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="System map mobile">
  <defs><style>{css(c, 400)}</style></defs>
  <text class="mono fade a1" x="20" y="24" fill="{c['muted']}" font-size="11" letter-spacing="2">SYSTEM MAP</text>
  <g class="pop p0">
    <rect x="70" y="48" width="250" height="52" rx="2" fill="{c['node']}" stroke="{c['rule']}"/>
    <text class="mono" x="195" y="72" fill="{c['ink']}" font-size="13" letter-spacing="1" text-anchor="middle">MANPREET.SYS</text>
    <text class="mono" x="195" y="90" fill="{c['muted']}" font-size="10" text-anchor="middle">evidence → systems → control</text>
  </g>
  <line class="draw w1" x1="195" y1="100" x2="195" y2="470" stroke="{c['rule']}"/>
  <g class="pop p1"><rect x="40" y="120" width="310" height="48" rx="2" fill="{c['node']}" stroke="{c['cyan']}" stroke-opacity=".5"/>
    <text class="mono" x="56" y="142" fill="{c['cyan']}" font-size="11">PRODUCTS</text>
    <text class="mono" x="56" y="160" fill="{c['ink']}" font-size="12">CareerPilot · StrikeCaller · PagePulse</text></g>
  <g class="pop p2"><rect x="40" y="184" width="310" height="48" rx="2" fill="{c['node']}" stroke="{c['lavender']}" stroke-opacity=".55"/>
    <text class="mono" x="56" y="206" fill="{c['lavender']}" font-size="11">AI EXPERIMENTATION</text>
    <text class="mono" x="56" y="224" fill="{c['ink']}" font-size="12">R.E.A.C.T. · Minecraft AI Civ.</text></g>
  <g class="pop p3"><rect x="40" y="248" width="310" height="48" rx="2" fill="{c['node']}" stroke="{c['coral']}" stroke-opacity=".5"/>
    <text class="mono" x="56" y="270" fill="{c['coral']}" font-size="11">RELIABLE INTEGRATIONS</text>
    <text class="mono" x="56" y="288" fill="{c['ink']}" font-size="12">IntegrationLab · System Down</text></g>
  <g class="pop p4"><rect x="40" y="312" width="310" height="48" rx="2" fill="{c['node']}" stroke="{c['cyan']}" stroke-opacity=".45"/>
    <text class="mono" x="56" y="334" fill="{c['cyan']}" font-size="11">QUANTITATIVE RESEARCH</text>
    <text class="mono" x="56" y="352" fill="{c['ink']}" font-size="12">EquityTrace · Java Banking</text></g>
  <g class="pop p5"><rect x="40" y="390" width="310" height="56" rx="2" fill="{c['soft']}" stroke="{c['lavender']}"/>
    <text class="mono" x="56" y="416" fill="{c['lavender']}" font-size="12">FLAGSHIP HUB</text>
    <text class="mono" x="56" y="436" fill="{c['muted']}" font-size="12">CareerPilot ties products ↔ evidence</text></g>
  <text class="mono fade a6" x="20" y="480" fill="{c['dim']}" font-size="11">shared ideas and dependencies</text>
</svg>'''


def flagship_meta_mobile(c: dict) -> str:
    return f'''<svg viewBox="0 0 390 150" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="CareerPilot">
  <defs><style>{css(c)}</style></defs>
  <text class="mono fade a1" x="20" y="28" fill="{c['cyan']}" font-size="12" letter-spacing="2">FLAGSHIP · CAREERPILOT</text>
  <text class="sans rise a2" x="20" y="68" fill="{c['ink']}" font-size="22" font-weight="700">Evidence-driven</text>
  <text class="sans rise a2" x="20" y="96" fill="{c['ink']}" font-size="22" font-weight="700">job search workspace</text>
  <text class="mono fade a3" x="20" y="128" fill="{c['muted']}" font-size="12">Python · FastAPI · React · SQLite</text>
</svg>'''


def flagship_frame_mobile(c: dict) -> str:
    return f'''<svg viewBox="0 0 390 32" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Screenshot label">
  <defs><style>{css(c, 200, animate=False)}</style></defs>
  <text class="mono" x="20" y="20" fill="{c['dim']}" font-size="11" letter-spacing="1.5">PRODUCT SCREENSHOT</text>
</svg>'''


def flagship_points_mobile(c: dict) -> str:
    return f'''<svg viewBox="0 0 390 200" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="CareerPilot highlights">
  <defs><style>{css(c)}</style></defs>
  <g class="row r1 mono">
    <text x="20" y="28" fill="{c['cyan']}" font-size="13" letter-spacing="2">01 / FIT</text>
    <text x="20" y="50" fill="{c['ink']}" font-size="13">Explainable, evidence-based Fit</text>
    <text x="20" y="68" fill="{c['ink']}" font-size="13">scoring from resume + posting text</text>
  </g>
  <line x1="20" y1="84" x2="370" y2="84" stroke="{c['rule']}"/>
  <g class="row r2 mono">
    <text x="20" y="110" fill="{c['lavender']}" font-size="13" letter-spacing="2">02 / WORKFLOW</text>
    <text x="20" y="132" fill="{c['ink']}" font-size="13">Discover → analyze → prepare → track</text>
  </g>
  <line x1="20" y1="148" x2="370" y2="148" stroke="{c['rule']}"/>
  <g class="row r3 mono">
    <text x="20" y="174" fill="{c['coral']}" font-size="13" letter-spacing="2">03 / EXTENSION</text>
    <text x="20" y="196" fill="{c['ink']}" font-size="13">Assists fills · never auto-submits</text>
  </g>
</svg>'''


def projects_mobile(c: dict) -> str:
    items = [
        ("01 / INTEGRATIONLAB", "API/webhook failure console with stored evidence.", "FASTAPI · POSTGRES · REACT"),
        ("02 / R.E.A.C.T.", "Reward feedback vs controller revisions (prototype).", "PYTHON · RESEARCH"),
        ("03 / EQUITYTRACE", "SEC filings → factors → transparent backtests.", "PYTHON · XBRL · DUCKDB"),
        ("04 / MINECRAFT AI CIV.", "Multi-agent sim with memory and planning.", "TYPESCRIPT · MINEFLAYER"),
    ]
    parts = []
    for i, (t, d, m) in enumerate(items):
        y = 16 + i * 100
        parts.append(f'''<g class="row r{i+1} mono" transform="translate(0 {y})">
    <text x="20" y="20" fill="{c['ink']}" font-size="14" font-weight="700">{t}</text>
    <text x="20" y="44" fill="{c['muted']}" font-size="12">{d}</text>
    <text x="20" y="66" fill="{c['cyan']}" font-size="11">{m}</text>
    <line x1="20" y1="82" x2="370" y2="82" stroke="{c['rule']}"/>
  </g>''')
    return f'''<svg viewBox="0 0 390 460" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Selected projects">
  <defs><style>{css(c)}</style></defs>
  {''.join(parts)}
  <text class="mono" x="20" y="440" fill="{c['dim']}" font-size="11">ALSO · StrikeCaller · PagePulse · Banking · System Down</text>
</svg>'''


def toolkit_mobile(c: dict) -> str:
    return f'''<svg viewBox="0 0 390 220" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Toolkit">
  <defs><style>{css(c)}</style></defs>
  <text class="mono rise a1" x="20" y="28" fill="{c['dim']}" font-size="11" letter-spacing="2">LANGUAGES</text>
  <text class="mono rise a1" x="20" y="50" fill="{c['ink']}" font-size="13">Python · TypeScript · Java · JS · SQL</text>
  <text class="mono rise a2" x="20" y="84" fill="{c['dim']}" font-size="11" letter-spacing="2">FRAMEWORKS</text>
  <text class="mono rise a2" x="20" y="106" fill="{c['ink']}" font-size="13">FastAPI · React · Node.js · JavaFX</text>
  <text class="mono rise a3" x="20" y="140" fill="{c['dim']}" font-size="11" letter-spacing="2">DATA</text>
  <text class="mono rise a3" x="20" y="162" fill="{c['ink']}" font-size="13">PostgreSQL · SQLite · DuckDB</text>
  <text class="mono rise a4" x="20" y="196" fill="{c['dim']}" font-size="11" letter-spacing="2">TOOLING</text>
  <text class="mono rise a4" x="20" y="218" fill="{c['ink']}" font-size="13">Git · Docker · Actions · pytest · Vitest</text>
</svg>'''


def footer_mobile(c: dict) -> str:
    return f'''<svg viewBox="0 0 390 110" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Footer">
  <defs><style>{css(c)}</style></defs>
  <line class="draw a1" x1="20" y1="20" x2="370" y2="20" stroke="{c['rule']}"/>
  <circle class="pulse" cx="28" cy="48" r="4" fill="{c['cyan']}"/>
  <text class="mono fade a2" x="44" y="52" fill="{c['ink']}" font-size="12" letter-spacing="2">AVAILABLE</text>
  <text class="mono fade a2" x="20" y="80" fill="{c['muted']}" font-size="12">building traceable systems</text>
  <text class="mono fade a3" x="20" y="102" fill="{c['dim']}" font-size="11">Manpreet Singh</text>
</svg>'''


def section_mobile(num: str, label: str, hint: str, c: dict) -> str:
    return f'''<svg viewBox="0 0 390 72" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Section {num}">
  <defs><style>{css(c, 300)}</style></defs>
  <g class="fade a1 mono">
    <text x="20" y="52" fill="{c['ghost']}" font-size="36" font-weight="600">{num}</text>
    <text x="78" y="42" fill="{c['cyan']}" font-size="13" letter-spacing="3">{label}</text>
  </g>
  <line class="draw a2" x1="78" y1="54" x2="300" y2="54" stroke="{c['rule']}"/>
  <text class="mono fade a2" x="370" y="42" fill="{c['dim']}" font-size="10" text-anchor="end">{hint}</text>
</svg>'''


def main() -> None:
    sections = [
        ("s01", "01", "WHOAMI", "~/01-whoami"),
        ("s02", "02", "SYSTEM MAP", "~/02-map"),
        ("s03", "03", "FLAGSHIP", "~/03-careerpilot"),
        ("s04", "04", "PROJECTS", "~/04-projects"),
        ("s05", "05", "TOOLKIT", "~/05-toolkit"),
    ]

    for mode, c in PALETTE.items():
        d = OUT[("desktop", mode)]
        write(d / "hero.svg", hero_desktop(c))
        write(d / "whoami.svg", whoami(c))
        write(d / "system-map.svg", system_map(c))
        write(d / "flagship-meta.svg", flagship_meta(c))
        write(d / "flagship-frame.svg", flagship_frame(c))
        write(d / "flagship-points.svg", flagship_points(c))
        write(d / "projects.svg", projects_dir(c))
        write(d / "toolkit.svg", toolkit(c))
        write(d / "footer.svg", footer(c))
        for name, num, label, hint in sections:
            write(d / f"{name}.svg", section(num, label, hint, c))

        m = OUT[("mobile", mode)]
        write(m / "hero.svg", hero_mobile(c))
        write(m / "whoami.svg", whoami_mobile(c))
        write(m / "system-map.svg", system_map_mobile(c))
        write(m / "flagship-meta.svg", flagship_meta_mobile(c))
        write(m / "flagship-frame.svg", flagship_frame_mobile(c))
        write(m / "flagship-points.svg", flagship_points_mobile(c))
        write(m / "projects.svg", projects_mobile(c))
        write(m / "toolkit.svg", toolkit_mobile(c))
        write(m / "footer.svg", footer_mobile(c))
        for name, num, label, hint in sections:
            write(m / f"{name}.svg", section_mobile(num, label, hint, c))


if __name__ == "__main__":
    main()
