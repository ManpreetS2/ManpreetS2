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
    # Ghost numeral: slightly brighter for legibility, still secondary to title.
    ghost = "#A8B8CC" if mode == "dark" else "#8A96AB"
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
    h = HERO_COLORS[mode]
    # Line 3 uses subtitle (near-white in dark) for clearer contrast than muted.
    line3 = h["subtitle"]
    return f'''<svg viewBox="0 0 1000 236" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="About Manpreet Singh — builds end-to-end software; CS at De Anza, incoming SJSU Spring 2027">
  <style>{whoami_css()}</style>

  <text class="mono rise a1" x="48" y="32" font-size="16" fill="{h['ink']}">Building end-to-end software, from backend systems to user-facing products.</text>
  <text class="mono rise a2" x="48" y="60" font-size="16" fill="{h['ink']}">My projects span career tools, AI experimentation, and financial research.</text>
  <text class="mono rise a3" x="48" y="88" font-size="15" fill="{line3}">I care about clear interfaces, reliable systems, and results I can explain.</text>

  <line class="rise a4" x1="48" y1="116" x2="952" y2="116" stroke="{h['rule']}" stroke-width="1" opacity=".5"/>

  <text class="mono rise a4" x="48" y="148" font-size="11" fill="{h['muted']}" letter-spacing="2.5">FOCUS</text>
  <text class="mono rise a4" x="154" y="148" font-size="15" fill="{h['ink']}">Full-stack engineering · Applied AI · Quantitative research</text>

  <text class="mono rise a5" x="48" y="182" font-size="11" fill="{h['muted']}" letter-spacing="2.5">STATUS</text>
  <text class="mono rise a5" x="154" y="182" font-size="15" fill="{h['cyan']}">Seeking software engineering and solutions engineering internships</text>

  <text class="mono rise a6" x="48" y="216" font-size="11" fill="{h['muted']}" letter-spacing="2.5">EDUCATION</text>
  <text class="mono rise a6" x="154" y="216" font-size="15" fill="{h['ink']}">Computer Science · De Anza College → SJSU (Spring 2027)</text>
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


def flagship_css(draw_len: int = 1000) -> str:
    """CareerPilot motion: hero timings + whoami fail-safe resting visibility."""
    return f"""
    .mono {{ font-family:{MONO}; }}
    .draw {{ stroke-dasharray:{draw_len}; stroke-dashoffset:0; }}
    .rise,.fade,.row {{ opacity:1; }}
    @keyframes draw {{ from {{ stroke-dashoffset:{draw_len}; }} to {{ stroke-dashoffset:0; }} }}
    @keyframes rise {{ from {{ opacity:0; transform:translateY(8px); }} to {{ opacity:1; transform:translateY(0); }} }}
    @keyframes fade {{ from {{ opacity:0; }} to {{ opacity:1; }} }}
    .a1{{animation-delay:.1s}} .a2{{animation-delay:.25s}} .a3{{animation-delay:.4s}}
    .a4{{animation-delay:.55s}} .a5{{animation-delay:.7s}} .a6{{animation-delay:.85s}}
    .r1{{animation-delay:.2s}} .r2{{animation-delay:.35s}} .r3{{animation-delay:.5s}}
    @media (prefers-reduced-motion: no-preference) {{
      .draw {{ animation:draw 1.3s cubic-bezier(.6,0,.2,1) both; }}
      .rise {{ animation:rise .7s cubic-bezier(.2,.7,.2,1) both; }}
      .fade {{ animation:fade .65s ease both; }}
      .row {{ animation:rise .65s cubic-bezier(.2,.7,.2,1) both; }}
    }}
"""


def flagship_section(mode: str = "dark") -> str:
    """02 — FLAGSHIP header matching locked WHOAMI section geometry."""
    h = HERO_COLORS[mode]
    ghost = "#A8B8CC" if mode == "dark" else "#8A96AB"
    return f'''<svg viewBox="0 0 1000 92" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Section 02 — FLAGSHIP">
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
    <text x="48" y="68" font-size="52" fill="{ghost}">02</text>
    <text x="148" y="58" font-size="14" fill="{h['cyan']}" letter-spacing="6">FLAGSHIP</text>
    <text x="952" y="58" font-size="11" fill="{h['muted']}" letter-spacing="2" text-anchor="end">~/02-careerpilot</text>
  </g>
  <line class="draw" x1="288" y1="53" x2="820" y2="53" stroke="{h['rule']}" stroke-width="1"/>
</svg>'''


def flagship_meta(c: dict, mode: str = "dark") -> str:
    """CareerPilot title block — brand-first, 48/952 grid, HERO_COLORS."""
    h = HERO_COLORS[mode]
    return f'''<svg viewBox="0 0 1000 188" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="CareerPilot — evidence-driven job search workspace">
  <style>{flagship_css(904)}</style>

  <line class="draw a1" x1="48" y1="24" x2="952" y2="24" stroke="{h['rule']}" stroke-width="1"/>
  <text class="mono fade a1" x="48" y="16" fill="{h['cyan']}" font-size="11" letter-spacing="3.2">FLAGSHIP · 02 / CAREERPILOT</text>
  <text class="mono fade a1" x="952" y="16" fill="{h['lavender']}" font-size="11" letter-spacing="2" text-anchor="end">LOCAL / SELF-HOSTABLE</text>

  <text class="mono rise a2" x="48" y="78" fill="{h['ink']}" font-size="44" letter-spacing="-1.5">CareerPilot</text>
  <text class="mono fade a3" x="48" y="114" fill="{h['subtitle']}" font-size="18">Evidence-driven job search workspace</text>
  <text class="mono fade a4" x="48" y="148" fill="{h['muted']}" font-size="14">Python · FastAPI · React · TypeScript · SQLite · Chrome Extension</text>

  <line class="draw a5" x1="48" y1="172" x2="952" y2="172" stroke="{h['rule']}" stroke-width="1"/>
  <text class="mono fade a5" x="48" y="186" fill="{h['dim']}" font-size="11" letter-spacing="2.5">PRODUCT VIEW  ▸  DISCOVER WORKSPACE</text>
  <text class="mono fade a5" x="952" y="186" fill="{h['dim']}" font-size="11" letter-spacing="2" text-anchor="end">FIG. 02</text>
</svg>'''


def flagship_frame(c: dict, mode: str = "dark") -> str:
    """Top rail / corner marks above the real product screenshot (48–952)."""
    h = HERO_COLORS[mode]
    return f'''<svg viewBox="0 0 1000 40" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="CareerPilot screenshot frame top">
  <style>{flagship_css(904)}</style>
  <!-- Corner ticks align screenshot to the editorial grid -->
  <path class="fade a1" d="M48 28 V12 H64" stroke="{h['cyan']}" stroke-width="1.25" fill="none"/>
  <path class="fade a1" d="M952 28 V12 H936" stroke="{h['cyan']}" stroke-width="1.25" fill="none"/>
  <line class="draw a1" x1="72" y1="12" x2="928" y2="12" stroke="{h['rule']}" stroke-width="1"/>
  <text class="mono fade a2" x="48" y="36" fill="{h['dim']}" font-size="11" letter-spacing="2.5">LIVE UI — DISCOVER</text>
  <text class="mono fade a2" x="952" y="36" fill="{h['muted']}" font-size="11" letter-spacing="2" text-anchor="end">REAL PRODUCT SCREENSHOT</text>
</svg>'''


def flagship_frame_bottom(c: dict, mode: str = "dark") -> str:
    """Bottom rail under the screenshot — matching width / corners."""
    h = HERO_COLORS[mode]
    return f'''<svg viewBox="0 0 1000 40" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="CareerPilot screenshot frame bottom">
  <style>{flagship_css(904)}</style>
  <line class="draw a1" x1="72" y1="10" x2="928" y2="10" stroke="{h['rule']}" stroke-width="1"/>
  <path class="fade a1" d="M48 10 V26 H64" stroke="{h['cyan']}" stroke-width="1.25" fill="none"/>
  <path class="fade a1" d="M952 10 V26 H936" stroke="{h['cyan']}" stroke-width="1.25" fill="none"/>
  <text class="mono fade a2" x="48" y="36" fill="{h['dim']}" font-size="11" letter-spacing="2.5">HUMAN CONTROLLED · NEVER AUTO-SUBMIT</text>
  <text class="mono fade a2" x="952" y="36" fill="{h['coral']}" font-size="11" letter-spacing="2" text-anchor="end">SOURCE VISIBLE</text>
</svg>'''


def flagship_points(c: dict, mode: str = "dark") -> str:
    h = HERO_COLORS[mode]
    rows = [
        ("01 / FIT", h["cyan"], "Explainable job matching grounded in resume evidence"),
        ("02 / WORKFLOW", h["lavender"], "Discover, analyze, prepare, and track applications"),
        ("03 / EXTENSION", h["coral"], "Human-controlled browser assistance, never automatic submission"),
    ]
    parts = []
    y = 40
    for i, (lab, col, txt) in enumerate(rows):
        parts.append(f'''<g class="row r{i+1} mono">
    <text x="48" y="{y}" fill="{col}" font-size="13" letter-spacing="2.5">{lab}</text>
    <text x="220" y="{y}" fill="{h['ink']}" font-size="15">{txt}</text>
    <line x1="48" y1="{y + 18}" x2="952" y2="{y + 18}" stroke="{h['rule']}" stroke-width="1" opacity=".55"/>
  </g>''')
        y += 52
    return f'''<svg viewBox="0 0 1000 200" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="CareerPilot engineering highlights">
  <style>{flagship_css(904)}</style>
  <text class="mono fade a1" x="48" y="18" fill="{h['dim']}" font-size="11" letter-spacing="3">THREE ENGINEERING HIGHLIGHTS</text>
  {''.join(parts)}
</svg>'''


def flagship_cta(mode: str = "dark") -> str:
    """Minimal repo CTA label (wrapped in HTML <a> in README)."""
    h = HERO_COLORS[mode]
    return f'''<svg viewBox="0 0 280 36" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Open CareerPilot repository">
  <style>.mono {{ font-family:{MONO}; }}</style>
  <rect x="0.5" y="0.5" width="279" height="35" stroke="{h['rule']}" fill="none"/>
  <line x1="0" y1="35" x2="280" y2="35" stroke="{h['cyan']}" stroke-width="1.5"/>
  <text class="mono" x="16" y="23" fill="{h['ink']}" font-size="12" letter-spacing="2">OPEN CAREERPILOT  →</text>
</svg>'''


def social_link(label: str, accent: str, mode: str = "dark", mobile: bool = False) -> str:
    """Minimal monospace link chip — cyan / lavender / coral accents."""
    h = HERO_COLORS[mode]
    if mobile:
        w, fs, ls, pad_y = 118, 11, 1.5, 22
        vb_h = 32
    else:
        w, fs, ls, pad_y = 148, 12, 2.2, 24
        vb_h = 34
    return f'''<svg viewBox="0 0 {w} {vb_h}" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{label}">
  <style>.mono {{ font-family:{MONO}; }}</style>
  <rect x="0.5" y="0.5" width="{w - 1}" height="{vb_h - 1}" stroke="{h['rule']}" fill="none"/>
  <line x1="0" y1="{vb_h}" x2="{w}" y2="{vb_h}" stroke="{accent}" stroke-width="1.5"/>
  <text class="mono" x="{w / 2}" y="{pad_y}" fill="{h['ink']}" font-size="{fs}" letter-spacing="{ls}" text-anchor="middle">{label}</text>
</svg>'''


def write_social_and_flagship() -> None:
    """Regenerate ONLY social links + CareerPilot assets. Hero/WHOAMI locked."""
    for mode in ("dark", "light"):
        h = HERO_COLORS[mode]
        d = OUT[("desktop", mode)]
        m = OUT[("mobile", mode)]
        # Social chips
        write(d / "link-linkedin.svg", social_link("LINKEDIN", h["cyan"], mode))
        write(d / "link-email.svg", social_link("EMAIL", h["lavender"], mode))
        write(d / "link-repos.svg", social_link("REPOSITORIES", h["coral"], mode))
        write(m / "link-linkedin.svg", social_link("LINKEDIN", h["cyan"], mode, mobile=True))
        write(m / "link-email.svg", social_link("EMAIL", h["lavender"], mode, mobile=True))
        write(m / "link-repos.svg", social_link("REPOS", h["coral"], mode, mobile=True))
        # Flagship (palette arg unused; colors from HERO_COLORS)
        c = PALETTE[mode]
        write(d / "s02.svg", flagship_section(mode))
        write(d / "flagship-meta.svg", flagship_meta(c, mode))
        write(d / "flagship-frame.svg", flagship_frame(c, mode))
        write(d / "flagship-frame-bottom.svg", flagship_frame_bottom(c, mode))
        write(d / "flagship-points.svg", flagship_points(c, mode))
        write(d / "flagship-cta.svg", flagship_cta(mode))
        write(m / "s02.svg", flagship_section_mobile(mode))
        write(m / "flagship-meta.svg", flagship_meta_mobile(c, mode))
        write(m / "flagship-frame.svg", flagship_frame_mobile(c, mode))
        write(m / "flagship-frame-bottom.svg", flagship_frame_bottom_mobile(c, mode))
        write(m / "flagship-points.svg", flagship_points_mobile(c, mode))
        write(m / "flagship-cta.svg", flagship_cta_mobile(mode))


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
    ghost = "#A8B8CC" if mode == "dark" else "#8A96AB"
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
    line3 = h["subtitle"]
    return f'''<svg viewBox="0 0 390 492" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="About Manpreet Singh">
  <style>{whoami_css()}</style>

  <text class="mono rise a1" x="20" y="28" font-size="14" fill="{h['ink']}">Building end-to-end software,</text>
  <text class="mono rise a1" x="20" y="48" font-size="14" fill="{h['ink']}">from backend systems to</text>
  <text class="mono rise a1" x="20" y="68" font-size="14" fill="{h['ink']}">user-facing products.</text>
  <text class="mono rise a2" x="20" y="100" font-size="13" fill="{h['ink']}">My projects span career tools,</text>
  <text class="mono rise a2" x="20" y="120" font-size="13" fill="{h['ink']}">AI experimentation, and</text>
  <text class="mono rise a2" x="20" y="140" font-size="13" fill="{h['ink']}">financial research.</text>
  <text class="mono rise a3" x="20" y="172" font-size="13" fill="{line3}">I care about clear interfaces,</text>
  <text class="mono rise a3" x="20" y="192" font-size="13" fill="{line3}">reliable systems, and results</text>
  <text class="mono rise a3" x="20" y="212" font-size="13" fill="{line3}">I can explain.</text>

  <line class="rise a4" x1="20" y1="236" x2="370" y2="236" stroke="{h['rule']}" stroke-width="1" opacity=".5"/>

  <text class="mono rise a4" x="20" y="268" font-size="11" fill="{h['muted']}" letter-spacing="2.5">FOCUS</text>
  <text class="mono rise a4" x="20" y="290" font-size="13" fill="{h['ink']}">Full-stack engineering · Applied AI</text>
  <text class="mono rise a4" x="20" y="310" font-size="13" fill="{h['ink']}">Quantitative research</text>

  <text class="mono rise a5" x="20" y="346" font-size="11" fill="{h['muted']}" letter-spacing="2.5">STATUS</text>
  <text class="mono rise a5" x="20" y="368" font-size="13" fill="{h['cyan']}">Seeking software engineering and</text>
  <text class="mono rise a5" x="20" y="388" font-size="13" fill="{h['cyan']}">solutions engineering internships</text>

  <text class="mono rise a6" x="20" y="424" font-size="11" fill="{h['muted']}" letter-spacing="2.5">EDUCATION</text>
  <text class="mono rise a6" x="20" y="446" font-size="13" fill="{h['ink']}">Computer Science · De Anza College</text>
  <text class="mono rise a6" x="20" y="466" font-size="13" fill="{h['ink']}">→ SJSU (Spring 2027)</text>
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


def flagship_section_mobile(mode: str = "dark") -> str:
    h = HERO_COLORS[mode]
    ghost = "#A8B8CC" if mode == "dark" else "#8A96AB"
    return f'''<svg viewBox="0 0 390 72" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Section 02 — FLAGSHIP">
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
    <text x="20" y="52" font-size="36" fill="{ghost}">02</text>
    <text x="78" y="42" font-size="13" fill="{h['cyan']}" letter-spacing="3">FLAGSHIP</text>
    <text x="370" y="42" font-size="10" fill="{h['muted']}" text-anchor="end">~/02</text>
  </g>
  <line class="draw" x1="78" y1="54" x2="300" y2="54" stroke="{h['rule']}" stroke-width="1"/>
</svg>'''


def flagship_meta_mobile(c: dict, mode: str = "dark") -> str:
    h = HERO_COLORS[mode]
    return f'''<svg viewBox="0 0 390 168" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="CareerPilot">
  <style>{flagship_css(350)}</style>
  <line class="draw a1" x1="20" y1="20" x2="370" y2="20" stroke="{h['rule']}" stroke-width="1"/>
  <text class="mono fade a1" x="20" y="14" fill="{h['cyan']}" font-size="11" letter-spacing="2">FLAGSHIP · 02</text>
  <text class="mono rise a2" x="20" y="58" fill="{h['ink']}" font-size="28" letter-spacing="-0.5">CareerPilot</text>
  <text class="mono fade a3" x="20" y="88" fill="{h['subtitle']}" font-size="14">Evidence-driven job search</text>
  <text class="mono fade a3" x="20" y="108" fill="{h['subtitle']}" font-size="14">workspace</text>
  <text class="mono fade a4" x="20" y="136" fill="{h['muted']}" font-size="12">Python · FastAPI · React</text>
  <text class="mono fade a4" x="20" y="156" fill="{h['muted']}" font-size="12">TypeScript · SQLite · Extension</text>
</svg>'''


def flagship_frame_mobile(c: dict, mode: str = "dark") -> str:
    h = HERO_COLORS[mode]
    return f'''<svg viewBox="0 0 390 36" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Screenshot frame top">
  <style>{flagship_css(350)}</style>
  <path class="fade a1" d="M20 24 V10 H32" stroke="{h['cyan']}" stroke-width="1.25" fill="none"/>
  <path class="fade a1" d="M370 24 V10 H358" stroke="{h['cyan']}" stroke-width="1.25" fill="none"/>
  <line class="draw a1" x1="38" y1="10" x2="352" y2="10" stroke="{h['rule']}" stroke-width="1"/>
  <text class="mono fade a2" x="20" y="32" fill="{h['dim']}" font-size="10" letter-spacing="1.5">LIVE UI — DISCOVER</text>
</svg>'''


def flagship_frame_bottom_mobile(c: dict, mode: str = "dark") -> str:
    h = HERO_COLORS[mode]
    return f'''<svg viewBox="0 0 390 36" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Screenshot frame bottom">
  <style>{flagship_css(350)}</style>
  <line class="draw a1" x1="38" y1="8" x2="352" y2="8" stroke="{h['rule']}" stroke-width="1"/>
  <path class="fade a1" d="M20 8 V22 H32" stroke="{h['cyan']}" stroke-width="1.25" fill="none"/>
  <path class="fade a1" d="M370 8 V22 H358" stroke="{h['cyan']}" stroke-width="1.25" fill="none"/>
  <text class="mono fade a2" x="20" y="32" fill="{h['dim']}" font-size="10" letter-spacing="1.2">HUMAN CONTROLLED</text>
</svg>'''


def flagship_points_mobile(c: dict, mode: str = "dark") -> str:
    h = HERO_COLORS[mode]
    return f'''<svg viewBox="0 0 390 272" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="CareerPilot highlights">
  <style>{flagship_css(350)}</style>
  <text class="mono fade a1" x="20" y="18" fill="{h['dim']}" font-size="11" letter-spacing="2">HIGHLIGHTS</text>
  <g class="row r1 mono">
    <text x="20" y="48" fill="{h['cyan']}" font-size="12" letter-spacing="2">01 / FIT</text>
    <text x="20" y="70" fill="{h['ink']}" font-size="13">Explainable job matching</text>
    <text x="20" y="90" fill="{h['ink']}" font-size="13">grounded in resume evidence</text>
  </g>
  <line x1="20" y1="106" x2="370" y2="106" stroke="{h['rule']}" opacity=".55"/>
  <g class="row r2 mono">
    <text x="20" y="132" fill="{h['lavender']}" font-size="12" letter-spacing="2">02 / WORKFLOW</text>
    <text x="20" y="154" fill="{h['ink']}" font-size="13">Discover, analyze, prepare,</text>
    <text x="20" y="174" fill="{h['ink']}" font-size="13">and track applications</text>
  </g>
  <line x1="20" y1="190" x2="370" y2="190" stroke="{h['rule']}" opacity=".55"/>
  <g class="row r3 mono">
    <text x="20" y="216" fill="{h['coral']}" font-size="12" letter-spacing="2">03 / EXTENSION</text>
    <text x="20" y="238" fill="{h['ink']}" font-size="13">Human-controlled assistance,</text>
    <text x="20" y="258" fill="{h['ink']}" font-size="13">never automatic submission</text>
  </g>
</svg>'''


def flagship_cta_mobile(mode: str = "dark") -> str:
    h = HERO_COLORS[mode]
    return f'''<svg viewBox="0 0 240 34" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Open CareerPilot repository">
  <style>.mono {{ font-family:{MONO}; }}</style>
  <rect x="0.5" y="0.5" width="239" height="33" stroke="{h['rule']}" fill="none"/>
  <line x1="0" y1="33" x2="240" y2="33" stroke="{h['cyan']}" stroke-width="1.5"/>
  <text class="mono" x="14" y="22" fill="{h['ink']}" font-size="11" letter-spacing="1.5">OPEN CAREERPILOT  →</text>
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


def renumber_system_map_headers() -> None:
    """SYSTEM MAP becomes 03 after CareerPilot moves to 02 — numeral/hint only."""
    replacements = [
        (OUT[("desktop", "dark")] / "s03.svg", "#2A3D5C", "03", "SYSTEM MAP", "~/03-map"),
        (OUT[("desktop", "light")] / "s03.svg", "#C5CEE0", "03", "SYSTEM MAP", "~/03-map"),
        (OUT[("mobile", "dark")] / "s03.svg", None, "03", "SYSTEM MAP", "~/03"),
        (OUT[("mobile", "light")] / "s03.svg", None, "03", "SYSTEM MAP", "~/03"),
    ]
    # Start from current SYSTEM MAP header (s02), rewrite as s03 with new numeral.
    for mode in ("dark", "light"):
        src = OUT[("desktop", mode)] / "s02.svg"
        dst = OUT[("desktop", mode)] / "s03.svg"
        text = src.read_text(encoding="utf-8")
        text = text.replace("Section 02 — SYSTEM MAP", "Section 03 — SYSTEM MAP")
        text = text.replace(">02</text>", ">03</text>")
        text = text.replace("~/02-map", "~/03-map")
        # Keep original SYSTEM MAP styling; only numeral/path change.
        # If s02 was already overwritten as FLAGSHIP, fall back to regenerating via section().
        if "SYSTEM MAP" not in text:
            c = PALETTE[mode]
            text = section("03", "SYSTEM MAP", "~/03-map", c)
        dst.write_text(text if text.endswith("\n") else text + "\n", encoding="utf-8")
        print(f"wrote {dst.relative_to(ROOT)}")

        msrc = OUT[("mobile", mode)] / "s02.svg"
        mdst = OUT[("mobile", mode)] / "s03.svg"
        mtext = msrc.read_text(encoding="utf-8")
        mtext = mtext.replace("Section 02", "Section 03")
        mtext = mtext.replace(">02</text>", ">03</text>")
        mtext = mtext.replace("~/02", "~/03")
        if "SYSTEM MAP" not in mtext and "SYSTEM" not in mtext:
            c = PALETTE[mode]
            mtext = section_mobile("03", "SYSTEM MAP", "~/03", c)
        else:
            # Mobile s02 may say SYSTEM MAP in label text
            mtext = mtext.replace("FLAGSHIP", "SYSTEM MAP") if "FLAGSHIP" in mtext else mtext
        mdst.write_text(mtext if mtext.endswith("\n") else mtext + "\n", encoding="utf-8")
        print(f"wrote {mdst.relative_to(ROOT)}")


def main() -> None:
    """Full suite generator. Prefer write_social_and_flagship() for locked passes."""
    sections = [
        ("s01", "01", "WHOAMI", "~/01-whoami"),
        ("s02", "02", "FLAGSHIP", "~/02-careerpilot"),
        ("s03", "03", "SYSTEM MAP", "~/03-map"),
        ("s04", "04", "PROJECTS", "~/04-projects"),
        ("s05", "05", "TOOLKIT", "~/05-toolkit"),
    ]

    for mode, c in PALETTE.items():
        d = OUT[("desktop", mode)]
        write(d / "hero.svg", hero_desktop(c, mode))
        write(d / "whoami.svg", whoami(c, mode))
        write(d / "system-map.svg", system_map(c))
        write(d / "flagship-meta.svg", flagship_meta(c, mode))
        write(d / "flagship-frame.svg", flagship_frame(c, mode))
        write(d / "flagship-frame-bottom.svg", flagship_frame_bottom(c, mode))
        write(d / "flagship-points.svg", flagship_points(c, mode))
        write(d / "flagship-cta.svg", flagship_cta(mode))
        write(d / "projects.svg", projects_dir(c))
        write(d / "toolkit.svg", toolkit(c))
        write(d / "footer.svg", footer(c))
        for name, num, label, hint in sections:
            if name == "s01":
                write(d / "s01.svg", whoami_section(mode))
            elif name == "s02":
                write(d / "s02.svg", flagship_section(mode))
            else:
                write(d / f"{name}.svg", section(num, label, hint, c))

        m = OUT[("mobile", mode)]
        write(m / "hero.svg", hero_mobile(c, mode))
        write(m / "whoami.svg", whoami_mobile(c, mode))
        write(m / "system-map.svg", system_map_mobile(c))
        write(m / "flagship-meta.svg", flagship_meta_mobile(c, mode))
        write(m / "flagship-frame.svg", flagship_frame_mobile(c, mode))
        write(m / "flagship-frame-bottom.svg", flagship_frame_bottom_mobile(c, mode))
        write(m / "flagship-points.svg", flagship_points_mobile(c, mode))
        write(m / "flagship-cta.svg", flagship_cta_mobile(mode))
        write(m / "projects.svg", projects_mobile(c))
        write(m / "toolkit.svg", toolkit_mobile(c))
        write(m / "footer.svg", footer_mobile(c))
        for name, num, label, hint in sections:
            if name == "s01":
                write(m / "s01.svg", whoami_section_mobile(mode))
            elif name == "s02":
                write(m / "s02.svg", flagship_section_mobile(mode))
            else:
                write(m / f"{name}.svg", section_mobile(num, label, hint, c))


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--social-flagship":
        # Copy SYSTEM MAP headers to s03 with new numeral BEFORE overwriting s02.
        renumber_system_map_headers()
        write_social_and_flagship()
    else:
        main()
