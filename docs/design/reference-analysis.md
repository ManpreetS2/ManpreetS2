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

---

# Sharann WHOAMI — Reference Analysis

Source inspected (2026-10-18):
- Light: `assets/whoami.svg`
- Dark: `assets/dark/whoami.svg`
- Section header: `assets/s01.svg` / `assets/dark/s01.svg`

Personal bio text is **not** reused. Measured composition only.

## Canvas

| Property | Value |
|----------|--------|
| `viewBox` | `0 0 1000 236` |
| Aspect ratio | ≈ 4.24 : 1 |
| Content left | **48** |
| Content right | **952** |
| Label column | **x=48** |
| Value column | **x=154** |

No background fill, cards, icons, or diagrams.

## Vertical rhythm (y positions)

| Element | y | Size | Fill role |
|---------|---|------|-----------|
| Intro line 1 | **32** | 16 | bone (primary) |
| Intro line 2 | **60** | 16 | bone |
| Intro line 3 | **88** | 15 | muted |
| Dividing rule | **116** | 1px, opacity **0.5** | rule, `48→952` |
| FOCUS label / value | **148** | 11 / 15 | muted / bone |
| STATUS label / value | **182** | 11 / 15 | muted / **accent** |
| CLUBS label / value | **216** | 11 / 15 | muted / bone |

### Measured gaps

| From → To | Δy |
|-----------|-----|
| Line1 → Line2 | 28 |
| Line2 → Line3 | 28 |
| Line3 → rule | 28 |
| Rule → FOCUS | 32 |
| FOCUS → STATUS | 34 |
| STATUS → CLUBS | 34 |
| Last baseline → canvas bottom | 20 |

Labels use `letter-spacing="2.5"`. Values are plain mono at 15px. Structure: **3 short intros → one fine rule → 3 metadata rows**.

## Section header (s01)

| Property | Value |
|----------|--------|
| `viewBox` | `0 0 1000 92` |
| Ghost numeral `01` | x=48, y=68, size **52** |
| Title `WHOAMI` | x=128, y=58, size **14**, tracking **6** |
| Path hint | x=952, y=58, size **11**, tracking **2**, end-anchored |
| Draw rule | y=**53**, x1=**248** → x2=**831** |

## Animation (whoami body)

| Class | Resting (ref) | Motion | Duration | Easing |
|-------|---------------|--------|----------|--------|
| `.rise` | `opacity: 0` | → 1 + `translateY(8px→0)` | **0.7s** | `cubic-bezier(.2,.7,.2,1)` |

Delays: `.a1` 0.1s · `.a2` 0.2s · `.a3` 0.35s · `.a4` 0.5s · `.a5` 0.65s · `.a6` 0.8s.

`prefers-reduced-motion: reduce` → `animation: none; opacity: 1`.

## Principles to match (ours)

1. Same **48 / 952** margins as the approved hero.
2. Same **HERO_COLORS** and mono stack so the block continues the hero.
3. Same fail-safe motion pattern as the hero (resting = visible; animate under `no-preference`), with whoami-scale rise (0.7s / 8px) and compact delays.
4. Three intros + hairline rule + FOCUS / STATUS / EDUCATION rows (EDUCATION replaces reference CLUBS).
5. Dedicated **390-wide** mobile composition (not a scaled desktop SVG).
6. Copy must not repeat locked hero phrases.
