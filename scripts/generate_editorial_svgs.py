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


# ─── HERO (1000×400 — measured Sharann geometry; original identity/color) ─────

# Hero-only contrast (does not alter other section palettes).
HERO_COLORS = {
    "light": {
        "ink": "#0F1729",
        "subtitle": "#1A2438",
        "muted": "#3D4A5F",
        "dim": "#5A6578",
        "rule": "#B0BACC",
        "cyan": "#0B8F8A",
        "lavender": "#5F4F8F",
        "coral": "#B85040",
    },
    "dark": {
        # Near-white subtitle/meta for Sharann-like clarity on midnight navy.
        "ink": "#F4F7FC",
        "subtitle": "#EDF1F8",
        "muted": "#C5CEDC",
        "dim": "#A8B4C6",
        "rule": "#5A7190",
        "cyan": "#3DDBD9",
        "lavender": "#B8A9E8",
        "coral": "#E08A7A",
    },
}


def hero_css(draw_len: int = 1000) -> str:
    """Sharann timings/easing, GitHub-safe visibility.

    Resting CSS = completed visible state (rules drawn, text opaque).
    Animations run only under prefers-reduced-motion: no-preference, so
    reduced-motion / unsupported CSS never leave the hero blank.
    """
    return f"""
    .mono {{ font-family:{MONO}; }}
    .draw {{ stroke-dasharray:{draw_len}; stroke-dashoffset:0; }}
    .rise,.fade {{ opacity:1; }}
    @keyframes draw {{ from {{ stroke-dashoffset:{draw_len}; }} to {{ stroke-dashoffset:0; }} }}
    @keyframes rise {{ from {{ opacity:0; transform:translateY(12px); }} to {{ opacity:1; transform:translateY(0); }} }}
    @keyframes fade {{ from {{ opacity:0; }} to {{ opacity:1; }} }}
    .a1{{animation-delay:.2s}} .a2{{animation-delay:.5s}} .a3{{animation-delay:.9s}}
    .a4{{animation-delay:1.2s}} .a5{{animation-delay:1.4s}} .a6{{animation-delay:1.7s}}
    @media (prefers-reduced-motion: no-preference) {{
      .draw {{ animation:draw 1.4s cubic-bezier(.6,0,.2,1) both; }}
      .rise {{ animation:rise .9s cubic-bezier(.2,.7,.2,1) both; }}
      .fade {{ animation:fade .7s ease both; }}
    }}
"""


def hero_desktop(c: dict, mode: str = "dark") -> str:
    # Geometry locked to Sharann header-v1. Contrast from HERO_COLORS[mode].
    h = HERO_COLORS[mode]
    return f'''<svg viewBox="0 0 1000 400" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Manpreet Singh — software engineering, AI systems, fintech">
  <style>{hero_css(1000)}</style>

  <line class="draw a1" x1="48" y1="58" x2="952" y2="58" stroke="{h['rule']}" stroke-width="1"/>
  <g class="fade a1">
    <text class="mono" fill="{h['muted']}" x="48" y="44" font-size="11" letter-spacing="3.5">PORTFOLIO — INDEX Nº 001</text>
    <text class="mono" fill="{h['muted']}" x="952" y="44" font-size="11" letter-spacing="3.5" text-anchor="end">BAY AREA, CA</text>
  </g>

  <g class="rise a2">
    <text fill="{h['ink']}" class="mono" x="46" y="176" font-size="72" letter-spacing="-2">Manpreet Singh</text>
  </g>
  <g class="fade a3">
    <text fill="{h['subtitle']}" class="mono" x="48" y="214" font-size="19">Software Engineering · AI Systems · Fintech</text>
  </g>

  <g class="fade a4">
    <text fill="{h['dim']}" class="mono" x="48" y="274" font-size="12.5" letter-spacing="1">focus  ▸</text>
    <text fill="{h['cyan']}" class="mono" x="128" y="274" font-size="12.5" letter-spacing="1">evidence-first products · reliable backends · reproducible research</text>
  </g>
  <g class="fade a5">
    <text fill="{h['dim']}" class="mono" x="48" y="300" font-size="12.5" letter-spacing="1">open to software engineering and solutions engineering internships</text>
  </g>

  <line class="draw a5" x1="48" y1="342" x2="952" y2="342" stroke="{h['rule']}" stroke-width="1"/>
  <g class="fade a6">
    <text fill="{h['cyan']}" class="mono" x="48" y="374" font-size="11.5" letter-spacing="3">BUILD</text>
    <text fill="{h['lavender']}" class="mono" x="128" y="374" font-size="11.5">·</text>
    <text fill="{h['lavender']}" class="mono" x="152" y="374" font-size="11.5" letter-spacing="3">TEST</text>
    <text fill="{h['coral']}" class="mono" x="228" y="374" font-size="11.5">·</text>
    <text fill="{h['coral']}" class="mono" x="252" y="374" font-size="11.5" letter-spacing="3">SHIP</text>
    <text fill="{h['muted']}" class="mono" x="952" y="374" font-size="11.5" letter-spacing="3" text-anchor="end">DE ANZA → SJSU / 2027</text>
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


def whoami_css() -> str:
    """Whoami motion: Sharann whoami rise (0.7s / 8px) + hero fail-safe visibility.
    Resting = final visible; animate only under prefers-reduced-motion: no-preference.
    """
    return f"""
    .mono {{ font-family:{MONO}; }}
    .rise {{ opacity:1; }}
    @keyframes rise {{ from {{ opacity:0; transform:translateY(8px); }} to {{ opacity:1; transform:translateY(0); }} }}
    .a1{{animation-delay:.1s}} .a2{{animation-delay:.2s}} .a3{{animation-delay:.35s}}
    .a4{{animation-delay:.5s}} .a5{{animation-delay:.65s}} .a6{{animation-delay:.8s}}
    @media (prefers-reduced-motion: no-preference) {{
      .rise {{ animation:rise .7s cubic-bezier(.2,.7,.2,1) both; }}
    }}
"""


def whoami_section(mode: str = "dark") -> str:
    """01 — WHOAMI header using locked hero colors (section 01 only)."""
    h = HERO_COLORS[mode]
    ghost = "#2A3D5C" if mode == "dark" else "#C5CEE0"
    return f'''<svg viewBox="0 0 1000 92" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Section 01 — WHOAMI">
  <style>
    .mono {{ font-family:{MONO}; }}
    .draw {{ stroke-dasharray:760; stroke-dashoffset:0; }}
    .f {{ opacity:1; }}
    @keyframes d {{ from {{ stroke-dashoffset:760; }} to {{ stroke-dashoffset:0; }} }}
    @keyframes f {{ from {{ opacity:0; }} to {{ opacity:1; }} }}
    @media (prefers-reduced-motion: no-preference) {{
      .draw {{ animation:d 1.3s cubic-bezier(.6,0,.2,1) .2s both; }}
      .f {{ animation:f .8s ease .1s both; }}
    }}
  </style>
  <g class="f mono">
    <text x="48" y="68" font-size="52" fill="{ghost}">01</text>
    <text x="128" y="58" font-size="14" fill="{h['cyan']}" letter-spacing="6">WHOAMI</text>
    <text x="952" y="58" font-size="11" fill="{h['muted']}" letter-spacing="2" text-anchor="end">~/01-whoami</text>
  </g>
  <line class="draw" x1="248" y1="53" x2="831" y2="53" stroke="{h['rule']}" stroke-width="1"/>
</svg>'''


def whoami(c: dict, mode: str = "dark") -> str:
    # Geometry locked to Sharann whoami (1000×236). Colors from HERO_COLORS.
    # Copy deliberately avoids locked hero phrases.
    h = HERO_COLORS[mode]
    return f'''<svg viewBox="0 0 1000 236" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="About Manpreet Singh — CS at De Anza, incoming SJSU Spring 2027">
  <style>{whoami_css()}</style>

  <text class="mono rise a1" x="48" y="32" font-size="16" fill="{h['ink']}">CS student at De Anza College, incoming San José State University, Spring 2027.</text>
  <text class="mono rise a2" x="48" y="60" font-size="16" fill="{h['ink']}">building software, AI-assisted products, and fintech research tools end to end.</text>
  <text class="mono rise a3" x="48" y="88" font-size="15" fill="{h['muted']}">drawn to work where the data path stays inspectable and the interface stays honest.</text>

  <line class="rise a4" x1="48" y1="116" x2="952" y2="116" stroke="{h['rule']}" stroke-width="1" opacity=".5"/>

  <text class="mono rise a4" x="48" y="148" font-size="11" fill="{h['muted']}" letter-spacing="2.5">FOCUS</text>
  <text class="mono rise a4" x="154" y="148" font-size="15" fill="{h['ink']}">Product systems · Applied ML tooling · Markets &amp; research software</text>

  <text class="mono rise a5" x="48" y="182" font-size="11" fill="{h['muted']}" letter-spacing="2.5">STATUS</text>
  <text class="mono rise a5" x="154" y="182" font-size="15" fill="{h['cyan']}">looking for teams that ship careful, inspectable software</text>

  <text class="mono rise a6" x="48" y="216" font-size="11" fill="{h['muted']}" letter-spacing="2.5">EDUCATION</text>
  <text class="mono rise a6" x="154" y="216" font-size="15" fill="{h['ink']}">Computer Science — De Anza College, then San José State University (Spring 2027)</text>
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

def hero_mobile(c: dict, mode: str = "dark") -> str:
    """Narrow (~390) composition — not a scaled desktop SVG.
    Same editorial language/animation; larger type; simplified secondary meta.
    """
    h = HERO_COLORS[mode]
    return f'''<svg viewBox="0 0 390 460" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Manpreet Singh — software engineering, AI systems, fintech">
  <style>{hero_css(340)}</style>

  <line class="draw a1" x1="20" y1="44" x2="370" y2="44" stroke="{h['rule']}" stroke-width="1"/>
  <g class="fade a1">
    <text class="mono" fill="{h['muted']}" x="20" y="30" font-size="11" letter-spacing="2">PORTFOLIO — Nº 001</text>
    <text class="mono" fill="{h['muted']}" x="370" y="30" font-size="11" letter-spacing="2" text-anchor="end">BAY AREA</text>
  </g>

  <g class="rise a2">
    <text fill="{h['ink']}" class="mono" x="18" y="118" font-size="40" letter-spacing="-1.5">Manpreet</text>
    <text fill="{h['ink']}" class="mono" x="18" y="164" font-size="40" letter-spacing="-1.5">Singh</text>
  </g>
  <g class="fade a3">
    <text fill="{h['subtitle']}" class="mono" x="20" y="206" font-size="15">Software Engineering</text>
    <text fill="{h['subtitle']}" class="mono" x="20" y="228" font-size="15">AI Systems · Fintech</text>
  </g>

  <g class="fade a4">
    <text fill="{h['dim']}" class="mono" x="20" y="270" font-size="12" letter-spacing="1">focus  ▸</text>
    <text fill="{h['cyan']}" class="mono" x="20" y="292" font-size="12">evidence-first products</text>
    <text fill="{h['cyan']}" class="mono" x="20" y="310" font-size="12">reliable backends</text>
    <text fill="{h['cyan']}" class="mono" x="20" y="328" font-size="12">reproducible research</text>
  </g>
  <g class="fade a5">
    <text fill="{h['dim']}" class="mono" x="20" y="360" font-size="12">open to SE and solutions</text>
    <text fill="{h['dim']}" class="mono" x="20" y="378" font-size="12">engineering internships</text>
  </g>

  <line class="draw a5" x1="20" y1="400" x2="370" y2="400" stroke="{h['rule']}" stroke-width="1"/>
  <g class="fade a6">
    <text fill="{h['cyan']}" class="mono" x="20" y="428" font-size="12" letter-spacing="2">BUILD</text>
    <text fill="{h['lavender']}" class="mono" x="90" y="428" font-size="12">·</text>
    <text fill="{h['lavender']}" class="mono" x="110" y="428" font-size="12" letter-spacing="2">TEST</text>
    <text fill="{h['coral']}" class="mono" x="172" y="428" font-size="12">·</text>
    <text fill="{h['coral']}" class="mono" x="192" y="428" font-size="12" letter-spacing="2">SHIP</text>
    <text fill="{h['muted']}" class="mono" x="20" y="450" font-size="11" letter-spacing="1.5">DE ANZA → SJSU / 2027</text>
  </g>
</svg>'''


def whoami_section_mobile(mode: str = "dark") -> str:
    h = HERO_COLORS[mode]
    ghost = "#2A3D5C" if mode == "dark" else "#C5CEE0"
    return f'''<svg viewBox="0 0 390 72" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Section 01 — WHOAMI">
  <style>
    .mono {{ font-family:{MONO}; }}
    .draw {{ stroke-dasharray:300; stroke-dashoffset:0; }}
    .f {{ opacity:1; }}
    @keyframes d {{ from {{ stroke-dashoffset:300; }} to {{ stroke-dashoffset:0; }} }}
    @keyframes f {{ from {{ opacity:0; }} to {{ opacity:1; }} }}
    @media (prefers-reduced-motion: no-preference) {{
      .draw {{ animation:d 1.1s cubic-bezier(.6,0,.2,1) .15s both; }}
      .f {{ animation:f .7s ease .1s both; }}
    }}
  </style>
  <g class="f mono">
    <text x="20" y="52" font-size="36" fill="{ghost}">01</text>
    <text x="78" y="42" font-size="13" fill="{h['cyan']}" letter-spacing="3">WHOAMI</text>
    <text x="370" y="42" font-size="10" fill="{h['muted']}" text-anchor="end">~/01</text>
  </g>
  <line class="draw" x1="78" y1="54" x2="300" y2="54" stroke="{h['rule']}" stroke-width="1"/>
</svg>'''


def whoami_mobile(c: dict, mode: str = "dark") -> str:
    h = HERO_COLORS[mode]
    return f'''<svg viewBox="0 0 390 400" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="About Manpreet Singh">
  <style>{whoami_css()}</style>

  <text class="mono rise a1" x="20" y="28" font-size="14" fill="{h['ink']}">CS student at De Anza College,</text>
  <text class="mono rise a1" x="20" y="48" font-size="14" fill="{h['ink']}">incoming SJSU, Spring 2027.</text>
  <text class="mono rise a2" x="20" y="80" font-size="13" fill="{h['ink']}">building software, AI-assisted</text>
  <text class="mono rise a2" x="20" y="100" font-size="13" fill="{h['ink']}">products, and fintech research tools.</text>
  <text class="mono rise a3" x="20" y="132" font-size="13" fill="{h['muted']}">inspectable data paths.</text>
  <text class="mono rise a3" x="20" y="152" font-size="13" fill="{h['muted']}">honest interfaces.</text>

  <line class="rise a4" x1="20" y1="176" x2="370" y2="176" stroke="{h['rule']}" stroke-width="1" opacity=".5"/>

  <text class="mono rise a4" x="20" y="208" font-size="11" fill="{h['muted']}" letter-spacing="2.5">FOCUS</text>
  <text class="mono rise a4" x="20" y="230" font-size="13" fill="{h['ink']}">Product systems · Applied ML</text>
  <text class="mono rise a4" x="20" y="250" font-size="13" fill="{h['ink']}">Markets &amp; research software</text>

  <text class="mono rise a5" x="20" y="286" font-size="11" fill="{h['muted']}" letter-spacing="2.5">STATUS</text>
  <text class="mono rise a5" x="20" y="308" font-size="13" fill="{h['cyan']}">looking for teams that ship</text>
  <text class="mono rise a5" x="20" y="328" font-size="13" fill="{h['cyan']}">careful, inspectable software</text>

  <text class="mono rise a6" x="20" y="364" font-size="11" fill="{h['muted']}" letter-spacing="2.5">EDUCATION</text>
  <text class="mono rise a6" x="20" y="386" font-size="13" fill="{h['ink']}">CS — De Anza, then SJSU (2027)</text>
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
        write(d / "hero.svg", hero_desktop(c, mode))
        write(d / "whoami.svg", whoami(c, mode))
        write(d / "system-map.svg", system_map(c))
        write(d / "flagship-meta.svg", flagship_meta(c))
        write(d / "flagship-frame.svg", flagship_frame(c))
        write(d / "flagship-points.svg", flagship_points(c))
        write(d / "projects.svg", projects_dir(c))
        write(d / "toolkit.svg", toolkit(c))
        write(d / "footer.svg", footer(c))
        for name, num, label, hint in sections:
            if name == "s01":
                write(d / "s01.svg", whoami_section(mode))
            else:
                write(d / f"{name}.svg", section(num, label, hint, c))

        m = OUT[("mobile", mode)]
        write(m / "hero.svg", hero_mobile(c, mode))
        write(m / "whoami.svg", whoami_mobile(c, mode))
        write(m / "system-map.svg", system_map_mobile(c))
        write(m / "flagship-meta.svg", flagship_meta_mobile(c))
        write(m / "flagship-frame.svg", flagship_frame_mobile(c))
        write(m / "flagship-points.svg", flagship_points_mobile(c))
        write(m / "projects.svg", projects_mobile(c))
        write(m / "toolkit.svg", toolkit_mobile(c))
        write(m / "footer.svg", footer_mobile(c))
        for name, num, label, hint in sections:
            if name == "s01":
                write(m / "s01.svg", whoami_section_mobile(mode))
            else:
                write(m / f"{name}.svg", section_mobile(num, label, hint, c))


if __name__ == "__main__":
    main()
