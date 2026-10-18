# Sharann Hero — Reference Analysis

Source inspected (2026-10-18):
- https://github.com/Sharann-del/Sharann-del
- Light: `assets/header-v1.svg`
- Dark: `assets/dark/header-v1.svg`

Personal content, name, and artwork are **not** reused. Only measured composition and layout principles inform our hero.

## Canvas

| Property | Value |
|----------|--------|
| `viewBox` | `0 0 1000 400` |
| Aspect ratio | 2.5 : 1 |
| Content left edge | **48** (name slightly inset at **46**) |
| Content right edge | **952** (`text-anchor="end"`) |
| Usable width | 904 |

No background fill in the SVG — page theme shows through. No diagrams, cards, badges, or side graphics in the hero.

## Vertical rhythm (y positions)

| Element | y | Notes |
|---------|---|--------|
| Top metadata baseline | **44** | Left + right |
| Top horizontal rule | **58** | `x1=48` → `x2=952`, `stroke-width=1` |
| Name baseline | **176** | Large monospace display |
| Subtitle baseline | **214** | Role line |
| Focus row | **274** | `focus  ▸` + interests |
| Status / open-to row | **300** | Single line |
| Bottom horizontal rule | **342** | Same span as top rule |
| Footer tags baseline | **374** | Category chips + school years |

### Measured gaps

| From → To | Δy |
|-----------|-----|
| Top meta → top rule | 14 |
| Top rule → name | **118** (dominant whitespace above name) |
| Name → subtitle | 38 |
| Subtitle → focus | **60** |
| Focus → open-to | 26 |
| Open-to → bottom rule | 42 |
| Bottom rule → footer | 32 |
| Footer → canvas bottom | 26 |

## Typography

| Role | Family | Size | Letter-spacing | Weight | Color token |
|------|--------|------|----------------|--------|-------------|
| Top meta | ui-monospace stack | **11** | **3.5** | regular | `--muted` |
| **Name** | **same mono stack** | **72** | **-2** | regular (no bold) | `--bone` |
| Subtitle | mono | **19** | default | regular | `--muted` |
| Focus label + body | mono | **12.5** | **1** | regular | label `--dim`, body `--accent` |
| Open-to | mono | **12.5** | **1** | regular | `--dim` |
| Footer tags | mono | **11.5** | **3** | regular | `--muted` (dots `--accent`) |

Font stack exactly:
`ui-monospace, "SFMono-Regular", "SF Mono", Menlo, Consolas, "Liberation Mono", monospace`

**Critical:** The name is monospace at 72px — not a sans display face. That is the primary typographic signal.

## Horizontal alignment

- Single left column; no right-side diagram.
- Top meta: left `PORTFOLIO — INDEX Nº 001`, right location string.
- Focus label at `x=48`, focus body at `x=128` (label width ≈ 80).
- Footer: left-aligned category tags separated by `·` at fixed x positions; education right-aligned at `x=952`.

## Color hierarchy (reference)

Monochrome editorial. Approximate roles:

| Token | Light file | Dark file (hardcoded override) |
|-------|------------|--------------------------------|
| `--bone` (name) | `#444444` → dark media `#DDDDDD` | forced `#FFFFFF` |
| `--rule` | `#C0C0C0` | `#FFFFFF` / dark media `#444444` |
| `--muted` | `#888888` | `#FFFFFF` / `#777777` |
| `--dim` | `#AAAAAA` | `#FFFFFF` / `#666666` |
| `--accent` | `#555555` | `#FFFFFF` / `#AAAAAA` |

Our adaptation keeps this hierarchy but maps tokens to a DIMFLIX-inspired palette (midnight navy page, cyan primary, muted lavender secondary, restrained coral) without gradients or glow.

## Animation

| Class | Resting | Animation | Duration | Easing | Fill |
|-------|---------|-----------|----------|--------|------|
| `.draw` | `stroke-dashoffset: 1000` (hidden) | → `0` | **1.4s** | `cubic-bezier(.6,0,.2,1)` | `forwards` |
| `.rise` | `opacity: 0` | → 1 + `translateY(12px→0)` | **0.9s** | `cubic-bezier(.2,.7,.2,1)` | `forwards` |
| `.fade` | `opacity: 0` | → 1 | **0.7s** | `ease` | `forwards` |

Stagger delays:

| Class | Delay |
|-------|-------|
| `.a1` | 0.2s |
| `.a2` | 0.5s |
| `.a3` | 0.9s |
| `.a4` | 1.2s |
| `.a5` | 1.4s |
| `.a6` | 1.7s |

Sequence: top rule + meta → name rise → subtitle → focus → open-to + bottom rule → footer tags. Total ≈ **2.4s** to settle.

`prefers-reduced-motion: reduce`: animations disabled; `.draw` offset 0; `.rise`/`.fade` opacity 1.

(Reference also defines a `.rot` rotator unused in the visible hero markup.)

## Composition principles to match

1. **1000×400** canvas, margins **48 / 952**.
2. **Two hairline rules** framing the block; rules *draw in*.
3. **Name dominates** — 72px mono, large empty band above it.
4. **No side graphics** in the hero.
5. **All-mono editorial voice**; tight tracking on meta/footer; negative tracking on name.
6. **Four content bands below the name:** subtitle → focus → status → footer tags.
7. **Fast, ordered reveals**; reduced-motion shows final state.

## Deliberate identity differences (ours)

| Aspect | Reference | Ours |
|--------|-----------|------|
| Name / copy | Sharann’s personal text | Manpreet Singh + his focus/edu/status |
| Color | Near-monochrome | Cyan / lavender / coral accents on same hierarchy |
| Files | CSS variables + dark overrides | Hardcoded light/dark fills (camo-safe) |
| Mobile asset | Same SVG scaled | Same 1000×400 composition (scaled at 390px) |
