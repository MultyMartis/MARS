# HomeGateway v4.ai — background and environment philosophy v0.1

**Статус:** **DRAFT** · **PLANNING** · Lane B  
**Назначение:** канон **фонового слоя** — atmospheric environment, не wallpaper; allowed/forbidden directions.

**Не является:** image assets, WebGL implementation, video loops.

**Связанные:** [depth-and-z-layer-system-v0.1.md](depth-and-z-layer-system-v0.1.md) (layers 0–1) · [lighting-and-depth-atmosphere-v0.1.md](lighting-and-depth-atmosphere-v0.1.md) · [visual-direction-exploration-pack-v0.1.md](visual-direction-exploration-pack-v0.1.md)

---

## Canonical assertion

> **HG background is NOT wallpaper.**  
> **HG background IS** atmospheric environment layer — ambient spatial depth and operational atmosphere.

The background is the **room** the cockpit sits in — not a poster behind a dashboard.

---

## What the environment layer does

| Function | Description |
|----------|-------------|
| **Spatial depth** | 2–3 planes: base tone → mid geometry → faint light |
| **Calm-control** | Stays P3 — never competes with P1 `main_area` |
| **Station identity** | Distinguishes HG from flat SaaS gray |
| **Theme anchor** | Dark = immersive volume; light = tactical daylight |

---

## Allowed directions

| Direction | Guidelines |
|-----------|------------|
| **Subtle gradients** | Deep navy → charcoal (dark); cool gray steps (light); low contrast |
| **Volumetric darkness** | Soft falloff; corners slightly deeper — «cockpit bay» |
| **Ambient geometry** | Lines, arcs, hex hints, grid — **large scale, low opacity** |
| **Faint structural lighting** | Directional wash suggesting overhead instrument light |
| **Restrained particles/noise** | Static grain or ultra-slow drift; 60s+ period if animated |
| **Soft parallax** | Optional ultra-slow shift between depth planes — `pointer-events: none` |
| **Layered environmental depth** | Parallax optional; never fast |

All elements on **layer 0–1** per [depth-and-z-layer-system-v0.1.md](depth-and-z-layer-system-v0.1.md) — non-interactive.

---

## Forbidden directions

| Forbidden | Why |
|-----------|-----|
| **Starscape / space wallpaper** | Literal sci-fi scene; breaks operational realism |
| **Spaceship windows** | Movie prop; distracts foveal attention |
| **Literal sci-fi scenes** | Narrative wallpaper ≠ operator tool |
| **Aggressive animation** | Fatigue; breaks calm-control |
| **Gamer wallpapers** | RGB, action art, franchise skins |
| **RGB environments** | Color belongs to signals, not room |
| **Busy tessellation** | Honeycomb spam, matrix rain |
| **Brand hero photography** | Marketing site, not cockpit |
| **Video loops** | Performance + distraction — not v0.1 |

---

## Background vs content relationship

```text
Layer 0–1  Environment (calm, P3)
Layer 2+   Shell + instruments (P1–P2)
Layer 4+   Overlays (focused work)
```

| Rule | Detail |
|------|--------|
| Contrast budget | Background luminance **below** glass block text stack |
| Motion budget | Background motion ≤ ambient charter ([motion-atmosphere-v0.1.md](motion-atmosphere-v0.1.md)) |
| Focus mode | Environment may dim slightly; never disappear into white void |

---

## Dark theme environment (primary)

| Quality | Direction |
|---------|-----------|
| **Mood** | Immersive cockpit bay — night operations |
| **Base** | Deep navy / charcoal (`--hg-bg`) |
| **Depth** | Volumetric dark + faint cool accent wash |
| **Geometry** | Sparse; suggests structure without blueprint clutter |

Default operator session — **dark is primary immersive cockpit**.

---

## Light theme environment (alternate)

| Quality | Direction |
|---------|-----------|
| **Mood** | Tactical daylight — clear scan |
| **Base** | Cool gray / off-white |
| **Depth** | Lighter volumetric steps; geometry even subtler |
| **Signals** | Desaturated vs dark; contrast maintained |

Light is **operational clarity**, not consumer bright mode.

---

## Parallax and motion (environment only)

| Allowed | Forbidden |
|---------|-----------|
| 60s+ period drift | Fast starfields |
| Static noise texture | Hologram scanlines |
| Optional 1–2px shift on resize | Scroll-linked aggressive parallax |

Respects `prefers-reduced-motion` — static fallback.

---

## Relationship to viewport

[viewport-and-scroll-philosophy-v0.1.md](viewport-and-scroll-philosophy-v0.1.md): environment **fixed to viewport** — does not scroll with `main_area` content.

---

## Implementation notes (Phase 3–4, non-binding)

| Approach | Tradeoff |
|----------|----------|
| CSS gradients + pseudo-elements | Lightweight; preferred v0.1 |
| SVG large-scale geometry | Crisp at 2K |
| Canvas/WebGL atmosphere | **Defer** — complexity, perf |

**SAFE UNKNOWN:** illustration vs pure CSS — operator choice at static MVP.

---

## Anti-patterns (environment-specific)

| Symptom | Detection | Mitigation |
|---------|-----------|------------|
| «Cool wallpaper» test | Screenshot looks like art without UI | Remove narrative imagery |
| Competing contrast | Text hard on bg without glass | Lower bg luminance |
| Motion distraction | Eye drawn to bg during work | Slow or static |

See also [visual-anti-patterns-v0.1.md](visual-anti-patterns-v0.1.md).

---

## SAFE UNKNOWN

- Starfield **micro** dots at 2% opacity — borderline; operator review if used.
- Per-mode background variants — likely unified environment first.
- Mobile background simplification — TBD.

---

*Last updated: 2026-05-24 — Background and environment philosophy.*
