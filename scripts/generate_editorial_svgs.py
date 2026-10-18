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


def section(num: str, label: str, hint: str, c: dict, mode: str = "dark") -> str:
    """Numbered header — numeral brightness matches locked WHOAMI/FLAGSHIP."""
    h = HERO_COLORS[mode]
    ghost = "#A8B8CC" if mode == "dark" else "#8A96AB"
    # Draw start after label; long labels (SYSTEM MAP) need more room.
    x_draw = 288 if len(label) >= 10 else 268
    return f'''<svg viewBox="0 0 1000 92" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Section {num} — {label}">
  <style>
    .mono {{ font-family:{MONO}; }}
    .draw {{ stroke-dasharray:760; stroke-dashoffset:0; }}
    .f {{ opacity:1; }}
    @keyframes d {{ from {{ stroke-dashoffset:760; }} to {{ stroke-dashoffset:0; }} }}
    @media (prefers-reduced-motion: no-preference) {{
      .draw {{ animation:d 1.3s cubic-bezier(.6,0,.2,1) .2s forwards; }}
    }}
  </style>
  <g class="f mono">
    <text x="48" y="68" font-size="52" fill="{ghost}">{num}</text>
    <text x="148" y="58" font-size="14" fill="{h['cyan']}" letter-spacing="6">{label}</text>
    <text x="952" y="58" font-size="11" fill="{h['muted']}" letter-spacing="2" text-anchor="end">{hint}</text>
  </g>
  <line class="draw" x1="{x_draw}" y1="53" x2="820" y2="53" stroke="{h['rule']}" stroke-width="1"/>
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


def system_map(c: dict, mode: str = "dark") -> str:
    """Compact CareerPilot-centered map — storytelling over flowchart density."""
    h = HERO_COLORS[mode]
    # Stronger fills than palette node/soft so map reads at full-page scale.
    if mode == "dark":
        node, soft = "#1A2A44", "#243652"
    else:
        node, soft = "#EEF2F8", "#E4EAF5"
    return f'''<svg viewBox="0 0 1000 420" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="System map — CareerPilot at the center of products, integrations, AI, and research">
  <style>{flagship_css(500)}</style>

  <text class="mono fade a1" x="48" y="28" fill="{h['muted']}" font-size="11" letter-spacing="3">HOW THE WORK CONNECTS</text>
  <text class="mono fade a1" x="952" y="28" fill="{h['muted']}" font-size="11" letter-spacing="2" text-anchor="end">FIG. 03</text>
  <line class="draw a1" x1="48" y1="40" x2="952" y2="40" stroke="{h['rule']}" stroke-width="1"/>

  <!-- Speaks: evidence · reliability · human control -->
  <line class="draw a2" x1="500" y1="130" x2="180" y2="200" stroke="{h['rule']}" stroke-width="1.25"/>
  <line class="draw a2" x1="500" y1="130" x2="820" y2="200" stroke="{h['rule']}" stroke-width="1.25"/>
  <line class="draw a3" x1="500" y1="190" x2="180" y2="300" stroke="{h['rule']}" stroke-width="1.25"/>
  <line class="draw a3" x1="500" y1="190" x2="820" y2="300" stroke="{h['rule']}" stroke-width="1.25"/>

  <g class="rise a2">
    <rect x="340" y="100" width="320" height="90" rx="2" fill="{soft}" stroke="{h['cyan']}" stroke-width="1.5"/>
    <text class="mono" x="500" y="136" fill="{h['cyan']}" font-size="12" letter-spacing="3" text-anchor="middle">FLAGSHIP</text>
    <text class="mono" x="500" y="164" fill="{h['ink']}" font-size="22" letter-spacing="-0.5" text-anchor="middle">CareerPilot</text>
    <text class="mono" x="500" y="186" fill="{h['muted']}" font-size="12" text-anchor="middle">evidence · workflow · human control</text>
  </g>

  <g class="rise a3">
    <rect x="48" y="210" width="264" height="72" rx="2" fill="{node}" stroke="{h['cyan']}" stroke-width="1.25"/>
    <text class="mono" x="180" y="240" fill="{h['cyan']}" font-size="11" letter-spacing="2" text-anchor="middle">PRODUCTS</text>
    <text class="mono" x="180" y="264" fill="{h['ink']}" font-size="13" text-anchor="middle">StrikeCaller · PagePulse</text>
  </g>
  <g class="rise a3">
    <rect x="688" y="210" width="264" height="72" rx="2" fill="{node}" stroke="{h['lavender']}" stroke-width="1.25"/>
    <text class="mono" x="820" y="240" fill="{h['lavender']}" font-size="11" letter-spacing="2" text-anchor="middle">AI EXPERIMENTATION</text>
    <text class="mono" x="820" y="264" fill="{h['ink']}" font-size="13" text-anchor="middle">R.E.A.C.T. · Minecraft AI Civ.</text>
  </g>
  <g class="rise a4">
    <rect x="48" y="310" width="264" height="72" rx="2" fill="{node}" stroke="{h['coral']}" stroke-width="1.25"/>
    <text class="mono" x="180" y="340" fill="{h['coral']}" font-size="11" letter-spacing="2" text-anchor="middle">INTEGRATIONS</text>
    <text class="mono" x="180" y="364" fill="{h['ink']}" font-size="13" text-anchor="middle">IntegrationLab · reliability</text>
  </g>
  <g class="rise a4">
    <rect x="688" y="310" width="264" height="72" rx="2" fill="{node}" stroke="{h['cyan']}" stroke-width="1.25"/>
    <text class="mono" x="820" y="340" fill="{h['cyan']}" font-size="11" letter-spacing="2" text-anchor="middle">QUANT RESEARCH</text>
    <text class="mono" x="820" y="364" fill="{h['ink']}" font-size="13" text-anchor="middle">EquityTrace · Banking</text>
  </g>

  <text class="mono fade a5" x="48" y="408" fill="{h['muted']}" font-size="12" letter-spacing="1.5">SHARED THREAD — inspectable data paths · careful interfaces · human final control</text>
</svg>'''


def flagship_css(draw_len: int = 1000) -> str:
    """Fail-safe motion for unlocked sections.

    Resting CSS = final visible state (opacity:1, rules drawn).
    NEVER animate opacity/transform on content groups — tall README
    full-page captures and GitHub camo loads left lower SVGs invisible
    when rise/fade ran through opacity:0. Only stroke draw animates.
    """
    return f"""
    .mono {{ font-family:{MONO}; }}
    .draw {{ stroke-dasharray:{draw_len}; stroke-dashoffset:0; }}
    .rise,.fade,.row {{ opacity:1; }}
    @keyframes draw {{ from {{ stroke-dashoffset:{draw_len}; }} to {{ stroke-dashoffset:0; }} }}
    .a1{{animation-delay:.08s}} .a2{{animation-delay:.16s}} .a3{{animation-delay:.24s}}
    .a4{{animation-delay:.32s}} .a5{{animation-delay:.4s}} .a6{{animation-delay:.48s}}
    .r1{{animation-delay:.1s}} .r2{{animation-delay:.2s}} .r3{{animation-delay:.3s}}
    .r4{{animation-delay:.4s}} .r5{{animation-delay:.5s}}
    @media (prefers-reduced-motion: no-preference) {{
      .draw {{ animation:draw 1.1s cubic-bezier(.6,0,.2,1) forwards; }}
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
    @media (prefers-reduced-motion: no-preference) {{
      .draw {{ animation:d 1.3s cubic-bezier(.6,0,.2,1) .2s forwards; }}
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
    """Bottom rail under the screenshot — top pad so text doesn't kiss the image."""
    h = HERO_COLORS[mode]
    return f'''<svg viewBox="0 0 1000 88" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="CareerPilot screenshot frame bottom">
  <style>{flagship_css(904)}</style>
  <!-- Extra empty air under screenshot before rails (matches WHOAMI row breathing room) -->
  <line class="draw a1" x1="72" y1="40" x2="928" y2="40" stroke="{h['rule']}" stroke-width="1"/>
  <path class="fade a1" d="M48 40 V56 H64" stroke="{h['cyan']}" stroke-width="1.25" fill="none"/>
  <path class="fade a1" d="M952 40 V56 H936" stroke="{h['cyan']}" stroke-width="1.25" fill="none"/>
  <text class="mono fade a2" x="48" y="76" fill="{h['muted']}" font-size="11" letter-spacing="2.5">HUMAN CONTROLLED · NEVER AUTO-SUBMIT</text>
  <text class="mono fade a2" x="952" y="76" fill="{h['coral']}" font-size="11" letter-spacing="2" text-anchor="end">SOURCE VISIBLE</text>
</svg>'''


def flagship_points(c: dict, mode: str = "dark") -> str:
    h = HERO_COLORS[mode]
    # Exact brief copy. Extra top pad so rows don't collide with screenshot frame.
    rows = [
        ("01 / FIT", h["cyan"], [
            "Explainable job matching grounded in actual resume and job-posting evidence.",
        ]),
        ("02 / WORKFLOW", h["lavender"], [
            "Discover, analyze, prepare, and track applications in one workspace.",
        ]),
        ("03 / EXTENSION", h["coral"], [
            "Human-controlled Chrome assistance for supported job applications.",
            "Never automatic submission.",
        ]),
    ]
    parts = []
    y = 48  # air under frame-bottom (frame already carries the screenshot gap)
    for i, (lab, col, lines) in enumerate(rows):
        texts = [f'<text x="48" y="{y}" fill="{col}" font-size="12" letter-spacing="2.5">{lab}</text>']
        y += 26
        for line in lines:
            texts.append(f'<text x="48" y="{y}" fill="{h["ink"]}" font-size="15">{line}</text>')
            y += 26
        parts.append(f'''<g class="row r{i+1} mono">
    {''.join(texts)}
    <line x1="48" y1="{y + 8}" x2="952" y2="{y + 8}" stroke="{h['rule']}" stroke-width="1" opacity=".55"/>
  </g>''')
        y += 40
    return f'''<svg viewBox="0 0 1000 {y + 16}" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="CareerPilot engineering highlights">
  <style>{flagship_css(904)}</style>
  <text class="mono fade a1" x="48" y="22" fill="{h['muted']}" font-size="11" letter-spacing="3">THREE ENGINEERING HIGHLIGHTS</text>
  {''.join(parts)}
</svg>'''


def flagship_link_chip(label: str, accent: str, mode: str = "dark", width: int = 160) -> str:
    h = HERO_COLORS[mode]
    return f'''<svg viewBox="0 0 {width} 34" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{label}">
  <style>.mono {{ font-family:{MONO}; }}</style>
  <rect x="0.5" y="0.5" width="{width - 1}" height="33" stroke="{h['rule']}" fill="none"/>
  <line x1="0" y1="33" x2="{width}" y2="33" stroke="{accent}" stroke-width="1.5"/>
  <text class="mono" x="{width / 2}" y="22" fill="{h['ink']}" font-size="11" letter-spacing="1.8" text-anchor="middle">{label}</text>
</svg>'''


def flagship_cta(mode: str = "dark") -> str:
    """Repo CTA — kept for compatibility; README also uses showcase/CI chips."""
    return flagship_link_chip("OPEN REPOSITORY  →", HERO_COLORS[mode]["cyan"], mode, 220)


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


def write_unlocked() -> None:
    """Regenerate everything EXCEPT locked hero / WHOAMI / s01."""
    for mode in ("dark", "light"):
        h = HERO_COLORS[mode]
        c = PALETTE[mode]
        d = OUT[("desktop", mode)]
        m = OUT[("mobile", mode)]

        # Social
        write(d / "link-linkedin.svg", social_link("LINKEDIN", h["cyan"], mode))
        write(d / "link-email.svg", social_link("EMAIL", h["lavender"], mode))
        write(d / "link-repos.svg", social_link("REPOSITORIES", h["coral"], mode))
        write(d / "link-github.svg", social_link("GITHUB", h["coral"], mode))
        write(m / "link-linkedin.svg", social_link("LINKEDIN", h["cyan"], mode, mobile=True))
        write(m / "link-email.svg", social_link("EMAIL", h["lavender"], mode, mobile=True))
        write(m / "link-repos.svg", social_link("REPOS", h["coral"], mode, mobile=True))
        write(m / "link-github.svg", social_link("GITHUB", h["coral"], mode, mobile=True))

        # 02 Flagship
        write(d / "s02.svg", flagship_section(mode))
        write(d / "flagship-meta.svg", flagship_meta(c, mode))
        write(d / "flagship-frame.svg", flagship_frame(c, mode))
        write(d / "flagship-frame-bottom.svg", flagship_frame_bottom(c, mode))
        write(d / "flagship-points.svg", flagship_points(c, mode))
        write(d / "flagship-cta.svg", flagship_cta(mode))
        write(d / "link-showcase.svg", flagship_link_chip("ARCHITECTURE", h["lavender"], mode, 170))
        write(d / "link-ci.svg", flagship_link_chip("CI WORKFLOW", h["coral"], mode, 150))
        write(d / "link-proj-01.svg", flagship_link_chip("01 INTEGRATIONLAB", h["cyan"], mode, 190))
        write(d / "link-proj-02.svg", flagship_link_chip("02 R.E.A.C.T.", h["lavender"], mode, 150))
        write(d / "link-proj-03.svg", flagship_link_chip("03 EQUITYTRACE", h["cyan"], mode, 160))
        write(d / "link-proj-04.svg", flagship_link_chip("04 MINECRAFT AI", h["coral"], mode, 170))
        write(m / "s02.svg", flagship_section_mobile(mode))
        write(m / "flagship-meta.svg", flagship_meta_mobile(c, mode))
        write(m / "flagship-frame.svg", flagship_frame_mobile(c, mode))
        write(m / "flagship-frame-bottom.svg", flagship_frame_bottom_mobile(c, mode))
        write(m / "flagship-points.svg", flagship_points_mobile(c, mode))
        write(m / "flagship-cta.svg", flagship_cta_mobile(mode))
        write(m / "link-showcase.svg", flagship_link_chip("ARCHITECTURE", h["lavender"], mode, 140))
        write(m / "link-ci.svg", flagship_link_chip("CI", h["coral"], mode, 90))
        write(m / "link-proj-01.svg", flagship_link_chip("01 LAB", h["cyan"], mode, 100))
        write(m / "link-proj-02.svg", flagship_link_chip("02 REACT", h["lavender"], mode, 110))
        write(m / "link-proj-03.svg", flagship_link_chip("03 EQUITY", h["cyan"], mode, 110))
        write(m / "link-proj-04.svg", flagship_link_chip("04 MINECRAFT", h["coral"], mode, 130))

        # 03 Projects · 04 System map · 05 Toolkit · footer
        write(d / "s03.svg", section("03", "PROJECTS", "~/03-projects", c, mode))
        write(d / "projects.svg", projects_dir(c, mode))
        write(d / "s04.svg", section("04", "SYSTEM MAP", "~/04-map", c, mode))
        write(d / "system-map.svg", system_map(c, mode))
        write(d / "s05.svg", section("05", "TOOLKIT", "~/05-toolkit", c, mode))
        write(d / "toolkit.svg", toolkit(c, mode))
        write(d / "footer.svg", footer(c, mode))

        write(m / "s03.svg", section_mobile("03", "PROJECTS", "~/03", c, mode))
        write(m / "projects.svg", projects_mobile(c, mode))
        write(m / "s04.svg", section_mobile("04", "SYSTEM MAP", "~/04", c, mode))
        write(m / "system-map.svg", system_map_mobile(c, mode))
        write(m / "s05.svg", section_mobile("05", "TOOLKIT", "~/05", c, mode))
        write(m / "toolkit.svg", toolkit_mobile(c, mode))
        write(m / "footer.svg", footer_mobile(c, mode))


def _project_motif(kind: str, x: float, y: float, accent: str, rule: str, ink: str, dim: str) -> str:
    """Small editorial glyph in the right column — not a card, not dominating art."""
    # Frame
    out = [
        f'<rect x="{x}" y="{y}" width="148" height="72" fill="none" stroke="{rule}" stroke-width="1"/>',
        f'<line x1="{x}" y1="{y + 72}" x2="{x + 148}" y2="{y + 72}" stroke="{accent}" stroke-width="1.5"/>',
    ]
    if kind == "console":
        # Terminal / evidence console
        out += [
            f'<rect x="{x + 14}" y="{y + 14}" width="120" height="44" fill="none" stroke="{accent}" stroke-width="1"/>',
            f'<text class="mono" x="{x + 22}" y="{y + 32}" fill="{accent}" font-size="9">▸ audit</text>',
            f'<text class="mono" x="{x + 22}" y="{y + 46}" fill="{dim}" font-size="9">retry · store</text>',
        ]
    elif kind == "research":
        # Two comparison bars
        out += [
            f'<rect x="{x + 28}" y="{y + 22}" width="18" height="36" fill="{accent}" opacity=".35"/>',
            f'<rect x="{x + 56}" y="{y + 34}" width="18" height="24" fill="{accent}" opacity=".7"/>',
            f'<rect x="{x + 84}" y="{y + 18}" width="18" height="40" fill="{accent}"/>',
            f'<text class="mono" x="{x + 74}" y="{y + 14}" fill="{dim}" font-size="8" text-anchor="middle">A / B</text>',
        ]
    elif kind == "chart":
        # Point-in-time sparkline + axis
        out += [
            f'<polyline fill="none" stroke="{accent}" stroke-width="1.5" points="{x+18},{y+50} {x+40},{y+40} {x+62},{y+44} {x+84},{y+28} {x+106},{y+32} {x+128},{y+20}"/>',
            f'<line x1="{x + 18}" y1="{y + 56}" x2="{x + 130}" y2="{y + 56}" stroke="{rule}"/>',
            f'<text class="mono" x="{x + 74}" y="{y + 16}" fill="{dim}" font-size="8" text-anchor="middle">SEC → factors</text>',
        ]
    else:  # agents / cube
        out += [
            f'<path d="M{x+74} {y+16} L{x+110} {y+34} L{x+74} {y+52} L{x+38} {y+34} Z" fill="none" stroke="{accent}" stroke-width="1.25"/>',
            f'<path d="M{x+74} {y+34} L{x+110} {y+34} M{x+74} {y+34} L{x+38} {y+34} M{x+74} {y+34} L{x+74} {y+52}" stroke="{accent}" stroke-width="1" opacity=".7"/>',
            f'<text class="mono" x="{x + 74}" y="{y + 66}" fill="{dim}" font-size="8" text-anchor="middle">agents</text>',
        ]
    return "\n    ".join(out)


def projects_dir(c: dict, mode: str = "dark") -> str:
    """Sharann-style editorial directory with restrained right-column motifs."""
    h = HERO_COLORS[mode]
    items = [
        (
            "01 / INTEGRATIONLAB",
            [
                "Self-hosted console for understanding API and webhook failures",
                "through recorded evidence, retry handling, and auditable observations.",
            ],
            "FASTAPI · POSTGRESQL · REACT · DOCKER",
            "PRODUCT",
            h["cyan"],
            "console",
        ),
        (
            "02 / R.E.A.C.T.",
            [
                "Research infrastructure for comparing language-model controller",
                "revisions with and without numerical reward feedback.",
            ],
            "PYTHON · SIMULATION · RESEARCH PROTOTYPE",
            "ILLUSTRATIVE",
            h["lavender"],
            "research",
        ),
        (
            "03 / EQUITYTRACE",
            [
                "Point-in-time financial research based on SEC filings,",
                "transparent factors, and reproducible backtesting.",
            ],
            "PYTHON · SEC XBRL · DUCKDB",
            "ILLUSTRATIVE",
            h["cyan"],
            "chart",
        ),
        (
            "04 / MINECRAFT AI CIVILIZATION",
            [
                "Multi-agent research prototype exploring persistent identities,",
                "memories, planning, and real actions in a shared Minecraft world.",
                "Complete autonomous multi-agent simulation still under development.",
            ],
            "TYPESCRIPT · MINEFLAYER · SQLITE",
            "IN DEVELOPMENT",
            h["coral"],
            "agents",
        ),
    ]
    parts = []
    y = 16
    for i, (title, lines, meta, note, accent, motif) in enumerate(items):
        motif_y = y + 18
        block = [f'<text x="48" y="{y + 22}" fill="{h["ink"]}" font-size="16" letter-spacing=".5">{title}</text>']
        block.append(f'<text x="780" y="{y + 14}" fill="{h["dim"]}" font-size="9" letter-spacing="1.2" text-anchor="end">{note}</text>')
        yy = y + 48
        for line in lines:
            block.append(f'<text x="48" y="{yy}" fill="{h["muted"]}" font-size="14">{line}</text>')
            yy += 22
        block.append(f'<text x="48" y="{yy + 6}" fill="{accent}" font-size="12" letter-spacing=".3">{meta}</text>')
        block.append(_project_motif(motif, 804, motif_y, accent, h["rule"], h["ink"], h["dim"]))
        yy = max(yy + 28, motif_y + 84)
        block.append(f'<line x1="48" y1="{yy}" x2="952" y2="{yy}" stroke="{h["rule"]}" stroke-width="1"/>')
        parts.append(f'<g class="row r{i+1} mono">{"".join(block)}</g>')
        y = yy + 20
    y += 8
    return f'''<svg viewBox="0 0 1000 {y + 24}" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Selected projects directory">
  <style>{flagship_css(904)}</style>
  {''.join(parts)}
  <text class="mono fade a5" x="48" y="{y + 16}" fill="{h['dim']}" font-size="12" letter-spacing="1.2">ALSO — StrikeCaller · PagePulse · Java Banking System · System Down Simulator</text>
</svg>'''


def toolkit(c: dict, mode: str = "dark") -> str:
    """Sharann stack geometry with exact brief groups."""
    h = HERO_COLORS[mode]
    rows = [
        ("LANGUAGES", "Python · TypeScript · Java · JavaScript · SQL"),
        ("BACKEND", "FastAPI · Node.js · REST APIs"),
        ("FRONTEND", "React · JavaFX"),
        ("DATA", "PostgreSQL · SQLite · DuckDB"),
        ("TOOLING", "Git · Docker · GitHub Actions · pytest · Vitest · Playwright · JUnit"),
    ]
    parts = []
    for i, (lab, val) in enumerate(rows):
        y = 30 + i * 34
        parts.append(f'''<text class="mono rise a{min(i+1,6)}" x="48" y="{y}" fill="{h['muted']}" font-size="12" letter-spacing="2">{lab}</text>
  <text class="mono rise a{min(i+1,6)}" x="168" y="{y}" fill="{h['ink']}" font-size="15">{val}</text>''')
    return f'''<svg viewBox="0 0 1000 200" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Technical toolkit">
  <style>{flagship_css(200)}</style>
  <line x1="148" y1="8" x2="148" y2="188" stroke="{h['rule']}" stroke-width="1"/>
  {''.join(parts)}
</svg>'''


def footer(c: dict, mode: str = "dark") -> str:
    """Minimal closing — no hero repeat, no counters. Static status mark."""
    h = HERO_COLORS[mode]
    return f'''<svg viewBox="0 0 1000 110" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Manpreet Singh — open to software engineering internships">
  <style>{flagship_css(904)}</style>
  <line class="draw a1" x1="48" y1="20" x2="952" y2="20" stroke="{h['rule']}" stroke-width="1"/>
  <circle cx="60" cy="56" r="4" fill="{h['cyan']}"/>
  <text class="mono fade a2" x="82" y="52" fill="{h['ink']}" font-size="14" letter-spacing="2.5">MANPREET SINGH</text>
  <text class="mono fade a2" x="82" y="74" fill="{h['muted']}" font-size="13">Open to software engineering and solutions engineering internships</text>
  <text class="mono fade a3" x="952" y="62" fill="{h['muted']}" font-size="12" letter-spacing="1.5" text-anchor="end">BAY AREA · DE ANZA → SJSU / 2027</text>
  <line class="draw a4" x1="48" y1="96" x2="952" y2="96" stroke="{h['rule']}" stroke-width="1"/>
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


def flagship_section_mobile(mode: str = "dark") -> str:
    h = HERO_COLORS[mode]
    ghost = "#A8B8CC" if mode == "dark" else "#8A96AB"
    return f'''<svg viewBox="0 0 390 72" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Section 02 — FLAGSHIP">
  <style>
    .mono {{ font-family:{MONO}; }}
    .draw {{ stroke-dasharray:300; stroke-dashoffset:0; }}
    .f {{ opacity:1; }}
    @keyframes d {{ from {{ stroke-dashoffset:300; }} to {{ stroke-dashoffset:0; }} }}
    @media (prefers-reduced-motion: no-preference) {{
      .draw {{ animation:d 1.1s cubic-bezier(.6,0,.2,1) .15s forwards; }}
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
    return f'''<svg viewBox="0 0 390 72" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Screenshot frame bottom">
  <style>{flagship_css(350)}</style>
  <line class="draw a1" x1="38" y1="34" x2="352" y2="34" stroke="{h['rule']}" stroke-width="1"/>
  <path class="fade a1" d="M20 34 V48 H32" stroke="{h['cyan']}" stroke-width="1.25" fill="none"/>
  <path class="fade a1" d="M370 34 V48 H358" stroke="{h['cyan']}" stroke-width="1.25" fill="none"/>
  <text class="mono fade a2" x="20" y="64" fill="{h['muted']}" font-size="10" letter-spacing="1.2">HUMAN CONTROLLED</text>
</svg>'''


def flagship_points_mobile(c: dict, mode: str = "dark") -> str:
    h = HERO_COLORS[mode]
    return f'''<svg viewBox="0 0 390 380" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="CareerPilot highlights">
  <style>{flagship_css(350)}</style>
  <text class="mono fade a1" x="20" y="28" fill="{h['muted']}" font-size="11" letter-spacing="2">HIGHLIGHTS</text>
  <g class="row r1 mono">
    <text x="20" y="64" fill="{h['cyan']}" font-size="12" letter-spacing="2">01 / FIT</text>
    <text x="20" y="90" fill="{h['ink']}" font-size="13">Explainable job matching grounded</text>
    <text x="20" y="112" fill="{h['ink']}" font-size="13">in actual resume and posting evidence.</text>
  </g>
  <line x1="20" y1="132" x2="370" y2="132" stroke="{h['rule']}" opacity=".55"/>
  <g class="row r2 mono">
    <text x="20" y="164" fill="{h['lavender']}" font-size="12" letter-spacing="2">02 / WORKFLOW</text>
    <text x="20" y="190" fill="{h['ink']}" font-size="13">Discover, analyze, prepare, and track</text>
    <text x="20" y="212" fill="{h['ink']}" font-size="13">applications in one workspace.</text>
  </g>
  <line x1="20" y1="232" x2="370" y2="232" stroke="{h['rule']}" opacity=".55"/>
  <g class="row r3 mono">
    <text x="20" y="264" fill="{h['coral']}" font-size="12" letter-spacing="2">03 / EXTENSION</text>
    <text x="20" y="290" fill="{h['ink']}" font-size="13">Human-controlled Chrome assistance</text>
    <text x="20" y="312" fill="{h['ink']}" font-size="13">for supported job applications.</text>
    <text x="20" y="334" fill="{h['ink']}" font-size="13">Never automatic submission.</text>
  </g>
</svg>'''


def flagship_cta_mobile(mode: str = "dark") -> str:
    return flagship_link_chip("OPEN REPOSITORY  →", HERO_COLORS[mode]["cyan"], mode, 200)


def system_map_mobile(c: dict, mode: str = "dark") -> str:
    h = HERO_COLORS[mode]
    if mode == "dark":
        node, soft = "#1A2A44", "#243652"
    else:
        node, soft = "#EEF2F8", "#E4EAF5"
    return f'''<svg viewBox="0 0 390 380" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="System map mobile">
  <style>{flagship_css(350)}</style>
  <text class="mono fade a1" x="20" y="24" fill="{h['muted']}" font-size="11" letter-spacing="2">HOW WORK CONNECTS</text>
  <g class="rise a2">
    <rect x="20" y="40" width="350" height="70" rx="2" fill="{soft}" stroke="{h['cyan']}" stroke-width="1.5"/>
    <text class="mono" x="195" y="68" fill="{h['cyan']}" font-size="11" letter-spacing="2" text-anchor="middle">FLAGSHIP</text>
    <text class="mono" x="195" y="94" fill="{h['ink']}" font-size="18" text-anchor="middle">CareerPilot</text>
  </g>
  <g class="rise a3"><rect x="20" y="128" width="350" height="48" rx="2" fill="{node}" stroke="{h['cyan']}" stroke-width="1.25"/>
    <text class="mono" x="36" y="148" fill="{h['cyan']}" font-size="11">PRODUCTS</text>
    <text class="mono" x="36" y="166" fill="{h['ink']}" font-size="12">StrikeCaller · PagePulse</text></g>
  <g class="rise a3"><rect x="20" y="188" width="350" height="48" rx="2" fill="{node}" stroke="{h['lavender']}" stroke-width="1.25"/>
    <text class="mono" x="36" y="208" fill="{h['lavender']}" font-size="11">AI EXPERIMENTATION</text>
    <text class="mono" x="36" y="226" fill="{h['ink']}" font-size="12">R.E.A.C.T. · Minecraft AI Civ.</text></g>
  <g class="rise a4"><rect x="20" y="248" width="350" height="48" rx="2" fill="{node}" stroke="{h['coral']}" stroke-width="1.25"/>
    <text class="mono" x="36" y="268" fill="{h['coral']}" font-size="11">INTEGRATIONS</text>
    <text class="mono" x="36" y="286" fill="{h['ink']}" font-size="12">IntegrationLab · reliability</text></g>
  <g class="rise a4"><rect x="20" y="308" width="350" height="48" rx="2" fill="{node}" stroke="{h['cyan']}" stroke-width="1.25"/>
    <text class="mono" x="36" y="328" fill="{h['cyan']}" font-size="11">QUANT RESEARCH</text>
    <text class="mono" x="36" y="346" fill="{h['ink']}" font-size="12">EquityTrace · Banking</text></g>
</svg>'''


def projects_mobile(c: dict, mode: str = "dark") -> str:
    h = HERO_COLORS[mode]
    items = [
        ("01 / INTEGRATIONLAB", ["API/webhook failure console with", "recorded evidence and retries."], "FASTAPI · POSTGRES · REACT", "PRODUCT", h["cyan"], "console"),
        ("02 / R.E.A.C.T.", ["Compare LM controller revisions", "with/without reward feedback."], "PYTHON · RESEARCH", "ILLUSTRATIVE", h["lavender"], "research"),
        ("03 / EQUITYTRACE", ["SEC filings, transparent factors,", "reproducible backtesting."], "PYTHON · XBRL · DUCKDB", "ILLUSTRATIVE", h["cyan"], "chart"),
        ("04 / MINECRAFT AI CIV.", ["Multi-agent identities, memory,", "planning — still in development."], "TYPESCRIPT · MINEFLAYER", "IN DEV", h["coral"], "agents"),
    ]
    parts = []
    y = 12
    for i, (t, lines, m, note, accent, motif) in enumerate(items):
        block = [f'<text x="20" y="{y + 18}" fill="{h["ink"]}" font-size="14">{t}</text>']
        block.append(f'<text x="370" y="{y + 18}" fill="{h["dim"]}" font-size="10" text-anchor="end">{note}</text>')
        yy = y + 40
        for line in lines:
            block.append(f'<text x="20" y="{yy}" fill="{h["muted"]}" font-size="12">{line}</text>')
            yy += 18
        block.append(f'<text x="20" y="{yy + 4}" fill="{accent}" font-size="11">{m}</text>')
        # Compact motif under meta
        my = yy + 14
        block.append(f'<rect x="20" y="{my}" width="100" height="28" fill="none" stroke="{h["rule"]}"/>')
        block.append(f'<line x1="20" y1="{my + 28}" x2="120" y2="{my + 28}" stroke="{accent}" stroke-width="1.5"/>')
        block.append(f'<text x="28" y="{my + 18}" fill="{accent}" font-size="10">{motif}</text>')
        yy = my + 40
        block.append(f'<line x1="20" y1="{yy}" x2="370" y2="{yy}" stroke="{h["rule"]}"/>')
        parts.append(f'<g class="row r{i+1} mono">{"".join(block)}</g>')
        y = yy + 14
    return f'''<svg viewBox="0 0 390 {y + 30}" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Selected projects">
  <style>{flagship_css(350)}</style>
  {''.join(parts)}
  <text class="mono" x="20" y="{y + 18}" fill="{h['dim']}" font-size="11">ALSO · StrikeCaller · PagePulse · Banking · System Down</text>
</svg>'''


def toolkit_mobile(c: dict, mode: str = "dark") -> str:
    h = HERO_COLORS[mode]
    return f'''<svg viewBox="0 0 390 286" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Toolkit">
  <style>{flagship_css(200)}</style>
  <text class="mono rise a1" x="20" y="28" fill="{h['muted']}" font-size="11" letter-spacing="2">LANGUAGES</text>
  <text class="mono rise a1" x="20" y="50" fill="{h['ink']}" font-size="13">Python · TypeScript · Java · JS · SQL</text>
  <text class="mono rise a2" x="20" y="84" fill="{h['muted']}" font-size="11" letter-spacing="2">BACKEND</text>
  <text class="mono rise a2" x="20" y="106" fill="{h['ink']}" font-size="13">FastAPI · Node.js · REST APIs</text>
  <text class="mono rise a3" x="20" y="140" fill="{h['muted']}" font-size="11" letter-spacing="2">FRONTEND</text>
  <text class="mono rise a3" x="20" y="162" fill="{h['ink']}" font-size="13">React · JavaFX</text>
  <text class="mono rise a4" x="20" y="196" fill="{h['muted']}" font-size="11" letter-spacing="2">DATA</text>
  <text class="mono rise a4" x="20" y="218" fill="{h['ink']}" font-size="13">PostgreSQL · SQLite · DuckDB</text>
  <text class="mono rise a5" x="20" y="252" fill="{h['muted']}" font-size="11" letter-spacing="2">TOOLING</text>
  <text class="mono rise a5" x="20" y="274" fill="{h['ink']}" font-size="13">Git · Docker · Actions · pytest · Vitest · JUnit</text>
</svg>'''


def footer_mobile(c: dict, mode: str = "dark") -> str:
    h = HERO_COLORS[mode]
    return f'''<svg viewBox="0 0 390 130" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Footer">
  <style>{flagship_css(350)}</style>
  <line class="draw a1" x1="20" y1="16" x2="370" y2="16" stroke="{h['rule']}"/>
  <circle cx="28" cy="44" r="4" fill="{h['cyan']}"/>
  <text class="mono fade a2" x="44" y="48" fill="{h['ink']}" font-size="13" letter-spacing="2">MANPREET SINGH</text>
  <text class="mono fade a2" x="20" y="78" fill="{h['muted']}" font-size="12">Open to SE &amp; solutions</text>
  <text class="mono fade a2" x="20" y="98" fill="{h['muted']}" font-size="12">engineering internships</text>
  <text class="mono fade a3" x="20" y="122" fill="{h['muted']}" font-size="11">Bay Area · De Anza → SJSU / 2027</text>
</svg>'''


def section_mobile(num: str, label: str, hint: str, c: dict, mode: str = "dark") -> str:
    h = HERO_COLORS[mode]
    ghost = "#A8B8CC" if mode == "dark" else "#8A96AB"
    return f'''<svg viewBox="0 0 390 72" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Section {num}">
  <style>
    .mono {{ font-family:{MONO}; }}
    .draw {{ stroke-dasharray:300; stroke-dashoffset:0; }}
    .f {{ opacity:1; }}
    @keyframes d {{ from {{ stroke-dashoffset:300; }} to {{ stroke-dashoffset:0; }} }}
    @media (prefers-reduced-motion: no-preference) {{
      .draw {{ animation:d 1.1s cubic-bezier(.6,0,.2,1) .15s forwards; }}
    }}
  </style>
  <g class="f mono">
    <text x="20" y="52" font-size="36" fill="{ghost}">{num}</text>
    <text x="78" y="42" font-size="13" fill="{h['cyan']}" letter-spacing="3">{label}</text>
    <text x="370" y="42" font-size="10" fill="{h['muted']}" text-anchor="end">{hint}</text>
  </g>
  <line class="draw" x1="78" y1="54" x2="300" y2="54" stroke="{h['rule']}" stroke-width="1"/>
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
    """Default: write unlocked sections only (hero/WHOAMI stay locked)."""
    write_unlocked()


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--all-including-locked":
        # Dangerous: rewrites hero/WHOAMI. Only for full rebuilds.
        for mode, c in PALETTE.items():
            d = OUT[("desktop", mode)]
            m = OUT[("mobile", mode)]
            write(d / "hero.svg", hero_desktop(c, mode))
            write(d / "whoami.svg", whoami(c, mode))
            write(d / "s01.svg", whoami_section(mode))
            write(m / "hero.svg", hero_mobile(c, mode))
            write(m / "whoami.svg", whoami_mobile(c, mode))
            write(m / "s01.svg", whoami_section_mobile(mode))
    write_unlocked()
