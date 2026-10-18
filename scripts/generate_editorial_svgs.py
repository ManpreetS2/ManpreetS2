#!/usr/bin/env python3
"""Generate light/dark editorial SVG assets for the profile README.

Animation safety: never set opacity:0 (or undrawn strokes) as the element's
resting CSS. Put the hidden start state only in @keyframes with
animation-fill-mode: both. If the animation never runs, content stays visible.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIGHT_DIR = ROOT / "assets/editorial/light"
DARK_DIR = ROOT / "assets/editorial/dark"

LIGHT = {
    "ink": "#0F1729",
    "muted": "#4E596E",
    "dim": "#6E7890",
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
    "rule": "#3A4F6C",
    "ghost": "#314864",
    "cyan": "#3DDBD9",
    "lavender": "#B8A9E8",
    "coral": "#E08A7A",
    "soft": "#152238",
    "node": "#121E33",
}

MONO = 'ui-monospace, "SFMono-Regular", "SF Mono", Menlo, Consolas, "Liberation Mono", monospace'
SANS = 'ui-sans-serif, "Segoe UI", Roboto, Helvetica, Arial, sans-serif'


def anim_block(draw_len: int = 1200) -> str:
    # Fail-safe: resting CSS is always the final visible state.
    # Animations only attach under prefers-reduced-motion: no-preference.
    # If <img> SVG animation is skipped, content stays visible.
    return f"""
    .mono {{ font-family: {MONO}; }}
    .sans {{ font-family: {SANS}; }}
    .draw {{ stroke-dasharray: {draw_len}; stroke-dashoffset: 0; }}
    .rise,.lift,.fade {{ opacity: 1; }}
    .pulse,.caret {{ opacity: 1; }}
    .travel {{ stroke-dasharray: 5 9; }}
    @keyframes draw {{
      from {{ stroke-dashoffset: {draw_len}; }}
      to {{ stroke-dashoffset: 0; }}
    }}
    @keyframes rise {{
      from {{ opacity: 0; }}
      to {{ opacity: 1; }}
    }}
    @keyframes lift {{
      from {{ opacity: 0; transform: translateY(8px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}
    @keyframes fade {{
      from {{ opacity: 0; }}
      to {{ opacity: 1; }}
    }}
    @keyframes pulse {{
      0%,100% {{ opacity: .55; }}
      50% {{ opacity: 1; }}
    }}
    @keyframes travel {{ to {{ stroke-dashoffset: -280; }} }}
    @keyframes blink {{
      0%,49% {{ opacity: 1; }}
      50%,100% {{ opacity: 0; }}
    }}
    .a1{{animation-delay:.05s}} .a2{{animation-delay:.15s}} .a3{{animation-delay:.28s}}
    .a4{{animation-delay:.4s}} .a5{{animation-delay:.52s}} .a6{{animation-delay:.64s}}
    .d1{{animation-delay:.5s}} .d2{{animation-delay:.95s}} .d3{{animation-delay:1.4s}}
    @media (prefers-reduced-motion: no-preference) {{
      .draw {{ animation: draw 1.1s cubic-bezier(.6,0,.2,1) both; }}
      .rise {{ animation: rise .6s cubic-bezier(.2,.7,.2,1) both; }}
      .lift {{ animation: lift .65s cubic-bezier(.2,.7,.2,1) both; }}
      .fade {{ animation: fade .5s ease both; }}
      .pulse {{ animation: pulse 2.8s ease-in-out infinite; }}
      .travel {{ animation: travel 18s linear infinite; }}
      .caret {{ animation: blink 1.05s steps(1,end) infinite; }}
    }}
"""


def static_style() -> str:
    """No entrance animations — always-visible content for section SVGs."""
    return f"""
    .mono {{ font-family: {MONO}; }}
    .sans {{ font-family: {SANS}; }}
    .pulse {{ opacity: 1; }}
    @keyframes pulse {{
      0%,100% {{ opacity: .55; }}
      50% {{ opacity: 1; }}
    }}
    @media (prefers-reduced-motion: no-preference) {{
      .pulse {{ animation: pulse 2.8s ease-in-out infinite; }}
    }}
"""


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)}")


def hero(c: dict, mode: str) -> str:
    # Stacked composition: readable when scaled to ~390px (name ~28px, labels ~7–8px+).
    # Dense bio/metadata lives in Markdown for true mobile readability.
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 560" fill="none" role="img" aria-labelledby="title desc">
  <title id="title">Manpreet Singh — software engineering, AI systems, and fintech</title>
  <desc id="desc">Animated editorial hero for Manpreet Singh's developer portfolio.</desc>
  <defs>
    <linearGradient id="nameGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{c['cyan']}"/>
      <stop offset=".55" stop-color="{c['lavender']}"/>
      <stop offset="1" stop-color="{c['coral']}"/>
    </linearGradient>
    <radialGradient id="glow" cx="70%" cy="28%" r="48%">
      <stop offset="0" stop-color="{c['cyan']}" stop-opacity=".18"/>
      <stop offset=".55" stop-color="{c['lavender']}" stop-opacity=".08"/>
      <stop offset="1" stop-color="{c['cyan']}" stop-opacity="0"/>
    </radialGradient>
    <style>{anim_block()}</style>
  </defs>

  <rect width="1200" height="560" fill="transparent"/>
  <ellipse cx="860" cy="150" rx="380" ry="220" fill="url(#glow)"/>

  <line class="draw a1" x1="48" y1="58" x2="1152" y2="58" stroke="{c['rule']}" stroke-width="1.25"/>
  <g class="fade a1 mono">
    <text x="48" y="40" fill="{c['muted']}" font-size="18" letter-spacing="3.4">MS / ENGINEERING PORTFOLIO</text>
    <text x="1152" y="40" fill="{c['muted']}" font-size="18" letter-spacing="3.4" text-anchor="end">EST. IN CURIOSITY</text>
  </g>

  <g class="fade a2 mono">
    <text x="48" y="118" fill="{c['cyan']}" font-size="20" letter-spacing="5">HELLO, I'M</text>
  </g>
  <g class="lift a3">
    <text class="sans" x="44" y="198" fill="{c['ink']}" font-size="86" font-weight="700" letter-spacing="-3.2">MANPREET</text>
    <text class="sans" x="44" y="288" fill="url(#nameGrad)" font-size="86" font-weight="700" letter-spacing="-3.2">SINGH</text>
    <rect class="caret" x="368" y="232" width="5" height="56" rx="1.5" fill="{c['cyan']}"/>
  </g>

  <g class="fade a4 mono">
    <text x="48" y="334" fill="{c['muted']}" font-size="22">Software · AI systems · Fintech tooling</text>
  </g>

  <!-- Full-width signal strip (stacks cleanly on narrow viewports) -->
  <g class="fade a5" transform="translate(48 360)">
    <rect x="0" y="0" width="1104" height="118" rx="8" fill="{c['node']}" stroke="{c['rule']}" stroke-width="1"/>
    <text class="mono" x="28" y="32" fill="{c['dim']}" font-size="14" letter-spacing="2.4">SYSTEM TRACE / 001</text>
    <path class="travel" d="M40 72 H210 M320 72 H490 M600 72 H770" stroke="{c['cyan']}" stroke-width="1.8" fill="none" opacity=".85"/>
    <g class="pulse">
      <rect x="28" y="50" width="168" height="48" rx="6" fill="{c['soft']}" stroke="{c['cyan']}" stroke-opacity=".5"/>
      <text class="mono" x="44" y="70" fill="{c['cyan']}" font-size="12" letter-spacing="1.2">01 INPUT</text>
      <text class="mono" x="44" y="90" fill="{c['ink']}" font-size="16" font-weight="600">observe</text>
    </g>
    <g class="pulse d1">
      <rect x="308" y="50" width="168" height="48" rx="6" fill="{c['soft']}" stroke="{c['lavender']}" stroke-opacity=".55"/>
      <text class="mono" x="324" y="70" fill="{c['lavender']}" font-size="12" letter-spacing="1.2">02 VERIFY</text>
      <text class="mono" x="324" y="90" fill="{c['ink']}" font-size="16" font-weight="600">ground</text>
    </g>
    <g class="pulse d2">
      <rect x="588" y="50" width="168" height="48" rx="6" fill="{c['soft']}" stroke="{c['coral']}" stroke-opacity=".5"/>
      <text class="mono" x="604" y="70" fill="{c['coral']}" font-size="12" letter-spacing="1.2">03 OUTPUT</text>
      <text class="mono" x="604" y="90" fill="{c['ink']}" font-size="16" font-weight="600">deliver</text>
    </g>
    <circle class="pulse d3" cx="860" cy="74" r="6" fill="{c['cyan']}"/>
    <text class="mono" x="878" y="80" fill="{c['ink']}" font-size="16">traceable state · local-first</text>
  </g>

  <line class="draw a6" x1="48" y1="508" x2="1152" y2="508" stroke="{c['rule']}" stroke-width="1.25"/>
  <g class="fade a6 mono">
    <text x="48" y="540" fill="{c['muted']}" font-size="16" letter-spacing="1.4">DE ANZA COLLEGE → SAN JOSÉ STATE UNIVERSITY / SPRING 2027</text>
    <text x="1152" y="540" fill="{c['muted']}" font-size="16" letter-spacing="1.4" text-anchor="end">github.com/ManpreetS2</text>
  </g>
</svg>
<!-- mode:{mode} -->'''


def section(num: str, label: str, path_hint: str, c: dict, mode: str) -> str:
    # Static — always visible. Larger type for ~390px readability.
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 110" fill="none" role="img" aria-label="Section {num} — {label}">
  <defs><style>{static_style()}</style></defs>
  <g class="mono">
    <text x="48" y="78" fill="{c['ghost']}" font-size="64" font-weight="600">{num}</text>
    <text x="168" y="64" fill="{c['cyan']}" font-size="20" letter-spacing="5">{label}</text>
    <text x="1152" y="64" fill="{c['dim']}" font-size="15" letter-spacing="2" text-anchor="end">{path_hint}</text>
  </g>
  <line x1="320" y1="58" x2="960" y2="58" stroke="{c['rule']}" stroke-width="1.25"/>
</svg>
<!-- mode:{mode} -->'''


def featured_meta(c: dict, mode: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 150" fill="none" role="img" aria-label="CareerPilot featured project meta">
  <defs><style>{static_style()}</style></defs>
  <g>
    <text class="mono" x="48" y="34" fill="{c['cyan']}" font-size="16" letter-spacing="3.4">FLAGSHIP · 02 / CAREERPILOT</text>
    <text class="sans" x="48" y="82" fill="{c['ink']}" font-size="36" font-weight="700" letter-spacing="-0.8">Evidence-driven job search workspace</text>
    <text class="mono" x="48" y="118" fill="{c['muted']}" font-size="17">Python · FastAPI · React · TypeScript · SQLite · Chrome Extension</text>
    <text class="mono" x="1152" y="34" fill="{c['lavender']}" font-size="14" letter-spacing="2" text-anchor="end">LOCAL / SELF-HOSTABLE</text>
  </g>
  <line x1="48" y1="140" x2="1152" y2="140" stroke="{c['rule']}" stroke-width="1.25"/>
</svg>
<!-- mode:{mode} -->'''


def featured_points(c: dict, mode: str) -> str:
    # Three labels — static. Full sentences in Markdown for mobile readability.
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 72" fill="none" role="img" aria-label="CareerPilot highlights — Fit, workflow, extension">
  <defs><style>{static_style()}</style></defs>
  <line x1="48" y1="20" x2="1152" y2="20" stroke="{c['rule']}" stroke-width="1"/>
  <g class="mono">
    <text x="48" y="50" fill="{c['cyan']}" font-size="17" letter-spacing="2.2">01 / FIT</text>
    <text x="200" y="50" fill="{c['rule']}" font-size="17">·</text>
    <text x="230" y="50" fill="{c['lavender']}" font-size="17" letter-spacing="2.2">02 / WORKFLOW</text>
    <text x="470" y="50" fill="{c['rule']}" font-size="17">·</text>
    <text x="500" y="50" fill="{c['coral']}" font-size="17" letter-spacing="2.2">03 / EXTENSION</text>
    <text x="1152" y="50" fill="{c['dim']}" font-size="14" letter-spacing="2" text-anchor="end">HUMAN SUBMITS</text>
  </g>
</svg>
<!-- mode:{mode} -->'''


def toolkit(c: dict, mode: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 64" fill="none" role="img" aria-label="Toolkit accent">
  <defs><style>{static_style()}</style></defs>
  <line x1="48" y1="20" x2="1152" y2="20" stroke="{c['rule']}" stroke-width="1"/>
  <g class="mono">
    <text x="48" y="48" fill="{c['dim']}" font-size="15" letter-spacing="2.2">LANGUAGES</text>
    <text x="220" y="48" fill="{c['rule']}" font-size="15">·</text>
    <text x="250" y="48" fill="{c['dim']}" font-size="15" letter-spacing="2.2">FRAMEWORKS</text>
    <text x="450" y="48" fill="{c['rule']}" font-size="15">·</text>
    <text x="480" y="48" fill="{c['dim']}" font-size="15" letter-spacing="2.2">DATA</text>
    <text x="580" y="48" fill="{c['rule']}" font-size="15">·</text>
    <text x="610" y="48" fill="{c['dim']}" font-size="15" letter-spacing="2.2">TOOLING</text>
    <text x="1152" y="48" fill="{c['cyan']}" font-size="14" letter-spacing="2" text-anchor="end">PRACTICAL STACK</text>
  </g>
</svg>
<!-- mode:{mode} -->'''


def footer(c: dict, mode: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 160" fill="none" role="img" aria-label="Closing sign-off">
  <defs>
    <linearGradient id="fg" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{c['cyan']}"/>
      <stop offset="1" stop-color="{c['lavender']}"/>
    </linearGradient>
    <style>{static_style()}</style>
  </defs>
  <line x1="48" y1="28" x2="1152" y2="28" stroke="{c['rule']}" stroke-width="1.25"/>
  <text class="sans" x="48" y="78" fill="{c['ink']}" font-size="28" font-weight="700" letter-spacing="-0.4">Building systems you can trace.</text>
  <g class="mono">
    <text x="48" y="112" fill="{c['muted']}" font-size="16">Open to software engineering, solutions engineering, and technical internships.</text>
    <text x="48" y="142" fill="url(#fg)" font-size="15" letter-spacing="2.4">MANPREET SINGH</text>
    <circle class="pulse" cx="1088" cy="100" r="6" fill="{c['cyan']}"/>
    <text x="1074" y="142" fill="{c['cyan']}" font-size="14" letter-spacing="2.5" text-anchor="end">AVAILABLE</text>
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
        write(out / "featured-meta.svg", featured_meta(colors, mode))
        write(out / "featured-points.svg", featured_points(colors, mode))
        write(out / "toolkit.svg", toolkit(colors, mode))
        write(out / "footer.svg", footer(colors, mode))
        for name, num, label, hint in sections:
            write(out / f"{name}.svg", section(num, label, hint, colors, mode))

    # Remove dense whoami SVG — content moved to Markdown for mobile readability.
    for d in (LIGHT_DIR, DARK_DIR):
        p = d / "whoami.svg"
        if p.exists():
            p.unlink()
            print(f"removed {p.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
