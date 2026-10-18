#!/usr/bin/env python3
"""Generate light/dark editorial SVG assets for the profile README."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIGHT_DIR = ROOT / "assets/editorial/light"
DARK_DIR = ROOT / "assets/editorial/dark"

# Palette — deep midnight + cyan/teal + lavender + muted coral
LIGHT = {
    "ink": "#0F1729",
    "muted": "#4E596E",
    "dim": "#7A8499",
    "rule": "#B8C2D4",
    "ghost": "#C5CEE0",
    "cyan": "#0B8F8A",
    "lavender": "#5F4F8F",
    "coral": "#B85040",
    "soft": "#EEF2FA",
    "node": "#F5F7FC",
}

DARK = {
    "ink": "#E8EEF8",
    "muted": "#9AA6BB",
    "dim": "#7B879C",
    "rule": "#334866",
    "ghost": "#2A3D5C",
    "cyan": "#3DDBD9",
    "lavender": "#B8A9E8",
    "coral": "#E08A7A",
    "soft": "#152238",
    "node": "#121E33",
}

MONO = 'ui-monospace, "SFMono-Regular", "SF Mono", Menlo, Consolas, "Liberation Mono", monospace'
SANS = 'ui-sans-serif, "Segoe UI", Roboto, Helvetica, Arial, sans-serif'


def anim_block(draw_len: int = 1200) -> str:
    # Keep delays short so below-fold SVGs settle even if they load late.
    return f"""
    .mono {{ font-family: {MONO}; }}
    .sans {{ font-family: {SANS}; }}
    .draw {{ stroke-dasharray: {draw_len}; stroke-dashoffset: {draw_len}; animation: draw 1.2s cubic-bezier(.6,0,.2,1) forwards; }}
    @keyframes draw {{ to {{ stroke-dashoffset: 0; }} }}
    /* Opacity-only rise: transform on text nodes inside img SVGs often never completes. */
    .rise {{ opacity: 0; animation: rise .7s cubic-bezier(.2,.7,.2,1) forwards; }}
    @keyframes rise {{ from {{ opacity:0; }} to {{ opacity:1; }} }}
    .lift {{ opacity: 0; animation: lift .75s cubic-bezier(.2,.7,.2,1) forwards; }}
    @keyframes lift {{ from {{ opacity:0; transform: translateY(10px); }} to {{ opacity:1; transform: translateY(0); }} }}
    .fade {{ opacity: 0; animation: fade .6s ease forwards; }}
    @keyframes fade {{ to {{ opacity: 1; }} }}
    .pulse {{ animation: pulse 2.8s ease-in-out infinite; }}
    @keyframes pulse {{ 0%,100% {{ opacity: .55; }} 50% {{ opacity: 1; }} }}
    .travel {{ stroke-dasharray: 5 9; animation: travel 18s linear infinite; }}
    @keyframes travel {{ to {{ stroke-dashoffset: -280; }} }}
    .caret {{ animation: blink 1.05s steps(1,end) infinite; }}
    @keyframes blink {{ 0%,49% {{ opacity:1; }} 50%,100% {{ opacity:0; }} }}
    .a1{{animation-delay:.08s}} .a2{{animation-delay:.2s}} .a3{{animation-delay:.35s}}
    .a4{{animation-delay:.5s}} .a5{{animation-delay:.65s}} .a6{{animation-delay:.8s}}
    .a7{{animation-delay:.95s}} .d1{{animation-delay:.6s}} .d2{{animation-delay:1.1s}} .d3{{animation-delay:1.6s}}
    @media (prefers-reduced-motion: reduce) {{
      .draw,.rise,.lift,.fade,.pulse,.travel,.caret {{ animation: none !important; }}
      .draw {{ stroke-dashoffset: 0; }}
      .rise,.lift,.fade {{ opacity: 1; transform: none; }}
      .pulse {{ opacity: 1; }}
      .caret {{ opacity: 1; }}
    }}
"""


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)}")


def hero(c: dict, mode: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 420" fill="none" role="img" aria-labelledby="title desc">
  <title id="title">Manpreet Singh — software engineering, AI systems, and fintech</title>
  <desc id="desc">Animated editorial hero for Manpreet Singh's developer portfolio.</desc>
  <defs>
    <linearGradient id="nameGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{c['cyan']}"/>
      <stop offset="0.55" stop-color="{c['lavender']}"/>
      <stop offset="1" stop-color="{c['coral']}"/>
    </linearGradient>
    <radialGradient id="glow" cx="78%" cy="42%" r="42%">
      <stop offset="0" stop-color="{c['cyan']}" stop-opacity=".16"/>
      <stop offset="0.55" stop-color="{c['lavender']}" stop-opacity=".08"/>
      <stop offset="1" stop-color="{c['cyan']}" stop-opacity="0"/>
    </radialGradient>
    <style>{anim_block()}</style>
  </defs>

  <rect width="1200" height="420" fill="transparent"/>
  <ellipse cx="920" cy="180" rx="320" ry="220" fill="url(#glow)"/>

  <line class="draw a1" x1="48" y1="56" x2="1152" y2="56" stroke="{c['rule']}" stroke-width="1"/>
  <g class="fade a1 mono">
    <text x="48" y="40" fill="{c['muted']}" font-size="12" letter-spacing="3.2">MS / ENGINEERING PORTFOLIO</text>
    <text x="1152" y="40" fill="{c['muted']}" font-size="12" letter-spacing="3.2" text-anchor="end">EST. IN CURIOSITY</text>
  </g>

  <g class="fade a2 mono">
    <text x="48" y="108" fill="{c['cyan']}" font-size="15" letter-spacing="4.5">HELLO, I'M</text>
  </g>
  <g class="lift a3">
    <text class="sans" x="46" y="188" fill="{c['ink']}" font-size="74" font-weight="700" letter-spacing="-2.8">MANPREET</text>
    <text class="sans" x="46" y="268" fill="url(#nameGrad)" font-size="74" font-weight="700" letter-spacing="-2.8">SINGH</text>
    <rect class="caret" x="318" y="216" width="4" height="48" rx="1" fill="{c['cyan']}"/>
  </g>

  <g class="fade a4 mono">
    <text x="48" y="308" fill="{c['muted']}" font-size="16">Software · AI systems · Fintech tooling</text>
  </g>
  <g class="fade a5 mono">
    <text x="48" y="338" fill="{c['dim']}" font-size="13" letter-spacing="1.2">focus ▸</text>
    <text x="118" y="338" fill="{c['ink']}" font-size="13" letter-spacing=".3">evidence-backed products · reliable systems · human oversight</text>
  </g>

  <!-- Signal panel -->
  <g class="fade a4" transform="translate(780 96)">
    <rect x="0" y="0" width="340" height="210" rx="10" fill="{c['node']}" stroke="{c['rule']}" stroke-width="1"/>
    <text class="mono" x="18" y="28" fill="{c['dim']}" font-size="11" letter-spacing="2.5">SYSTEM TRACE / 001</text>
    <path class="travel" d="M40 78 H120 M180 78 H260 M150 110 V148" stroke="{c['cyan']}" stroke-width="1.6" fill="none" opacity=".85"/>
    <g class="pulse">
      <rect x="28" y="58" width="92" height="42" rx="7" fill="{c['soft']}" stroke="{c['cyan']}" stroke-opacity=".45"/>
      <text class="mono" x="40" y="76" fill="{c['cyan']}" font-size="10" letter-spacing="1">01 INPUT</text>
      <text class="mono" x="40" y="92" fill="{c['ink']}" font-size="13" font-weight="600">observe</text>
    </g>
    <g class="pulse d1">
      <rect x="138" y="58" width="92" height="42" rx="7" fill="{c['soft']}" stroke="{c['lavender']}" stroke-opacity=".55"/>
      <text class="mono" x="150" y="76" fill="{c['lavender']}" font-size="10" letter-spacing="1">02 VERIFY</text>
      <text class="mono" x="150" y="92" fill="{c['ink']}" font-size="13" font-weight="600">ground</text>
    </g>
    <g class="pulse d2">
      <rect x="248" y="58" width="72" height="42" rx="7" fill="{c['soft']}" stroke="{c['coral']}" stroke-opacity=".5"/>
      <text class="mono" x="258" y="76" fill="{c['coral']}" font-size="10" letter-spacing="1">03 OUT</text>
      <text class="mono" x="258" y="92" fill="{c['ink']}" font-size="13" font-weight="600">deliver</text>
    </g>
    <circle class="pulse d3" cx="150" cy="158" r="5" fill="{c['cyan']}"/>
    <text class="mono" x="164" y="162" fill="{c['ink']}" font-size="13">traceable state</text>
    <text class="mono" x="18" y="194" fill="{c['dim']}" font-size="10" letter-spacing="1.4">BUILT TO BE UNDERSTOOD</text>
    <text class="mono" x="322" y="194" fill="{c['dim']}" font-size="10" letter-spacing="1.4" text-anchor="end">LOCAL-FIRST</text>
  </g>

  <line class="draw a5" x1="48" y1="368" x2="1152" y2="368" stroke="{c['rule']}" stroke-width="1"/>
  <g class="fade a6 mono">
    <text x="48" y="396" fill="{c['muted']}" font-size="12" letter-spacing="1.6">DE ANZA COLLEGE  →  SAN JOSÉ STATE UNIVERSITY / SPRING 2027</text>
    <text x="1152" y="396" fill="{c['muted']}" font-size="12" letter-spacing="1.6" text-anchor="end">github.com/ManpreetS2</text>
  </g>
</svg>
<!-- mode:{mode} -->'''


def section(num: str, label: str, path_hint: str, c: dict, mode: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 88" fill="none" role="img" aria-label="Section {num} — {label}">
  <defs><style>{anim_block(820)}</style></defs>
  <g class="fade a1 mono">
    <text x="48" y="64" fill="{c['ghost']}" font-size="48" font-weight="600">{num}</text>
    <text x="138" y="54" fill="{c['cyan']}" font-size="14" letter-spacing="5.5">{label}</text>
    <text x="1152" y="54" fill="{c['dim']}" font-size="11" letter-spacing="2" text-anchor="end">{path_hint}</text>
  </g>
  <line class="draw a2" x1="268" y1="48" x2="980" y2="48" stroke="{c['rule']}" stroke-width="1"/>
</svg>
<!-- mode:{mode} -->'''


def whoami(c: dict, mode: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 240" fill="none" role="img" aria-labelledby="t d">
  <title id="t">About Manpreet Singh</title>
  <desc id="d">Concise bio, focus areas, status, and education.</desc>
  <defs><style>{anim_block()}</style></defs>
  <text class="mono rise a1" x="48" y="36" fill="{c['ink']}" font-size="16">Computer Science @ De Anza College · Incoming San José State University, Spring 2027.</text>
  <text class="mono rise a2" x="48" y="68" fill="{c['ink']}" font-size="16">I build practical software, AI-powered tools, and systems designed around reliability.</text>
  <text class="mono rise a3" x="48" y="100" fill="{c['muted']}" font-size="15">Prefer products where claims stay grounded in evidence and humans keep final control.</text>

  <line class="fade a4" x1="48" y1="128" x2="1152" y2="128" stroke="{c['rule']}" stroke-width="1"/>

  <text class="mono rise a4" x="48" y="164" fill="{c['dim']}" font-size="11" letter-spacing="2.8">FOCUS</text>
  <text class="mono rise a4" x="148" y="164" fill="{c['ink']}" font-size="15">Full-stack systems · Explainable AI tooling · Fintech research · Local-first apps</text>

  <text class="mono rise a5" x="48" y="196" fill="{c['dim']}" font-size="11" letter-spacing="2.8">STATUS</text>
  <text class="mono rise a5" x="148" y="196" fill="{c['cyan']}" font-size="15">Open to software engineering, solutions engineering, and technical internships</text>

  <text class="mono rise a6" x="48" y="228" fill="{c['dim']}" font-size="11" letter-spacing="2.8">EDU</text>
  <text class="mono rise a6" x="148" y="228" fill="{c['ink']}" font-size="15">De Anza College → San José State University / Spring 2027</text>
</svg>
<!-- mode:{mode} -->'''


def featured_meta(c: dict, mode: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 118" fill="none" role="img" aria-label="CareerPilot featured project meta">
  <defs><style>{anim_block()}</style></defs>
  <g class="rise a1">
    <text class="mono" x="48" y="28" fill="{c['cyan']}" font-size="12" letter-spacing="3.2">FLAGSHIP · CAREERPILOT</text>
    <text class="sans" x="48" y="62" fill="{c['ink']}" font-size="28" font-weight="700" letter-spacing="-0.6">Evidence-driven job search workspace</text>
    <text class="mono" x="48" y="92" fill="{c['muted']}" font-size="14">Python · FastAPI · React · TypeScript · SQLite · Chrome Extension</text>
    <text class="mono" x="1152" y="28" fill="{c['dim']}" font-size="11" letter-spacing="2" text-anchor="end">LOCAL / SELF-HOSTABLE</text>
  </g>
  <line class="draw a2" x1="48" y1="110" x2="1152" y2="110" stroke="{c['rule']}" stroke-width="1"/>
</svg>
<!-- mode:{mode} -->'''


def featured_points(c: dict, mode: str) -> str:
    # Editorial rows scale better than four cards when GitHub shrinks the SVG on mobile.
    rows = [
        ("01 / PROFILE", c["cyan"], "Grounded résumé → candidate profile with traceable claims", "a1"),
        ("02 / MATCH", c["lavender"], "Explainable Fit scores — missing evidence stays a gap, not a yes", "a2"),
        ("03 / WORKFLOW", c["coral"], "Discover → analyze → prepare → track with human-approved drafts", "a3"),
        ("04 / EXTENSION", c["cyan"], "Assists Greenhouse and Lever fills — never auto-submits applications", "a4"),
    ]
    body = []
    y = 28
    for label, color, text, delay in rows:
        body.append(
            f'<text class="mono rise {delay}" x="48" y="{y}" fill="{color}" font-size="12" letter-spacing="2">{label}</text>'
            f'<text class="mono rise {delay}" x="220" y="{y}" fill="{c["ink"]}" font-size="15">{text}</text>'
        )
        y += 34
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 148" fill="none" role="img" aria-label="CareerPilot capabilities">
  <defs><style>{anim_block()}</style></defs>
  <line x1="200" y1="8" x2="200" y2="140" stroke="{c['rule']}" stroke-width="1" opacity=".75"/>
  {''.join(body)}
</svg>
<!-- mode:{mode} -->'''


def toolkit(c: dict, mode: str) -> str:
    rows = [
        ("LANGUAGES", "Python · TypeScript · Java · JavaScript · SQL", "a1"),
        ("FRAMEWORKS", "FastAPI · React · Node.js · JavaFX", "a2"),
        ("DATA", "PostgreSQL · SQLite · DuckDB · SQLAlchemy", "a3"),
        ("TOOLING", "Git · Docker · GitHub Actions · pytest · Vitest · Playwright · JUnit", "a4"),
    ]
    body = []
    y = 32
    for label, value, delay in rows:
        body.append(
            f'<text class="mono rise {delay}" x="48" y="{y}" fill="{c["dim"]}" font-size="12" letter-spacing="2.2">{label}</text>'
            f'<text class="mono rise {delay}" x="188" y="{y}" fill="{c["ink"]}" font-size="15">{value}</text>'
        )
        y += 36
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 168" fill="none" role="img" aria-label="Technical toolkit">
  <defs><style>{anim_block()}</style></defs>
  <line x1="168" y1="8" x2="168" y2="156" stroke="{c['rule']}" stroke-width="1" opacity=".7"/>
  {''.join(body)}
</svg>
<!-- mode:{mode} -->'''


def more_projects(c: dict, mode: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 140" fill="none" role="img" aria-label="Additional projects">
  <defs><style>{anim_block()}</style></defs>
  <text class="mono fade a1" x="48" y="28" fill="{c['dim']}" font-size="11" letter-spacing="2.8">ALSO BUILT</text>
  <text class="mono rise a2" x="48" y="58" fill="{c['ink']}" font-size="14">StrikeCaller — spoken boxing / Muay Thai training coach</text>
  <text class="mono rise a3" x="48" y="84" fill="{c['ink']}" font-size="14">PagePulse — webpage monitoring that filters noise from factual change</text>
  <text class="mono rise a4" x="48" y="110" fill="{c['ink']}" font-size="14">Java Banking System — JavaFX desktop banking with atomic transfers</text>
  <text class="mono rise a5" x="48" y="136" fill="{c['ink']}" font-size="14">System Down Simulator — incident-response strategy browser game</text>
</svg>
<!-- mode:{mode} -->'''


def footer(c: dict, mode: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 96" fill="none" role="img" aria-label="Footer">
  <defs><style>{anim_block()}</style></defs>
  <line class="draw a1" x1="48" y1="24" x2="1152" y2="24" stroke="{c['rule']}" stroke-width="1"/>
  <g class="fade a2 mono">
    <text x="48" y="56" fill="{c['muted']}" font-size="13" letter-spacing="1.4">Open to software engineering, solutions engineering, and technical internship opportunities.</text>
    <text x="48" y="82" fill="{c['dim']}" font-size="12" letter-spacing="2">MANPREET SINGH  ·  BUILDING TRACEABLE SYSTEMS</text>
    <circle class="pulse" cx="1128" cy="56" r="5" fill="{c['cyan']}"/>
    <text x="1114" y="82" fill="{c['cyan']}" font-size="11" letter-spacing="2" text-anchor="end">AVAILABLE</text>
  </g>
</svg>
<!-- mode:{mode} -->'''


def social(c: dict, mode: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 56" fill="none" role="img" aria-label="Social links row">
  <defs><style>{anim_block()}</style></defs>
  <g class="fade a1 mono">
    <text x="48" y="34" fill="{c['dim']}" font-size="12" letter-spacing="2.5">CONNECT</text>
    <text x="160" y="34" fill="{c['cyan']}" font-size="13" letter-spacing="1.5">LINKEDIN</text>
    <text x="280" y="34" fill="{c['rule']}" font-size="13">/</text>
    <text x="300" y="34" fill="{c['lavender']}" font-size="13" letter-spacing="1.5">EMAIL</text>
    <text x="380" y="34" fill="{c['rule']}" font-size="13">/</text>
    <text x="400" y="34" fill="{c['coral']}" font-size="13" letter-spacing="1.5">REPOSITORIES</text>
    <text x="1152" y="34" fill="{c['dim']}" font-size="12" letter-spacing="2" text-anchor="end">BAY AREA, CA</text>
  </g>
</svg>
<!-- mode:{mode} -->'''


def main() -> None:
    sections = [
        ("s01", "01", "WHOAMI", "~/01-whoami"),
        ("s02", "02", "FEATURED WORK", "~/02-featured"),
        ("s03", "03", "SELECTED PROJECTS", "~/03-projects"),
        ("s04", "04", "TOOLKIT", "~/04-toolkit"),
    ]

    for mode, colors, out in (("light", LIGHT, LIGHT_DIR), ("dark", DARK, DARK_DIR)):
        write(out / "hero.svg", hero(colors, mode))
        write(out / "whoami.svg", whoami(colors, mode))
        write(out / "featured-meta.svg", featured_meta(colors, mode))
        write(out / "featured-points.svg", featured_points(colors, mode))
        write(out / "toolkit.svg", toolkit(colors, mode))
        write(out / "footer.svg", footer(colors, mode))
        for name, num, label, hint in sections:
            write(out / f"{name}.svg", section(num, label, hint, colors, mode))


if __name__ == "__main__":
    main()
