# Frontend Structure Analysis v1 — zakaz v5

**Workspace:** `workspaces/triumph-manipulator-landing-v5/`  
**Build:** Gulp → `dist/index.html` (index-only baseline per audit)

## Stack signals

| Layer | Pattern |
|-------|---------|
| HTML | Gulp `@@include` partials |
| CSS | SCSS — `_v5-hero-extensions.scss`, v5-page01 overrides, legacy v4 sections still in bundle |
| JS | Form handler, modals (`scripts-v5-page01.html`) |
| Assets | `hero-bg-final.jpg` (2560×1440), `second-screen-index-baseline.jpg` |
| Page marker | `body[data-page-type="ppc-zakaz-manip"]` |

## Partial reuse model

| Section | Partial source |
|---------|----------------|
| Hero, specs, tasks, steps, pricing, FAQ | `v5-ppc/zakaz/*` |
| Trust, B2B, proof strip, footer, header | `v5-page01/*` (shared with 5-ton page01 family) |

**Calibration insight:** Master hot route **shares** trust/B2B/footer with capability page01 kit — good for consistency; risk if B2B copy assumes capability-only intent.

## Hero technical structure

- Background: `<img class="first-screen__bg-media">` + `.first-screen__overlay` (gradients)
- Hero content: `.hero--v5` grid — **no** machine cutout image inside hero column (reduces clutter vs old v4 hero visual note)
- Specs: icon + label list (Font Awesome), not dl table

## Factory hardening findings (referenced)

From `v5-production-hardening-audit-v1.md`:

| Finding | Severity | Calibration impact |
|---------|----------|-------------------|
| Hero img dimensions fixed to 2560×1440 | was High | CLS risk mitigated in current index.html |
| `data-form-handler="mock"` on some forms | Critical | Launch blocker — outside calibration doc fix |
| Dual hero background in `_base.scss` | Medium | Technical debt; PPC override OK |
| Google Fonts external | Warn | file:// preview risk |

## Section anchors

| ID | Section |
|----|---------|
| `#hero` | Hero |
| `#specs` | Machine showcase |
| `#tasks` | Allowed / denied (in tasks partial) |
| `#contacts` | Footer form |

Nav labels from header partial — align with 5-ton handoff pattern (Параметры, Задачи, etc.).

## What Factory did without ORCA pack

- `hero--v5` grid + inline form pattern
- Operational `hero-proof--v5` strip
- Cargo cards as buttons with `data-cta-source` telemetry hooks (attributes only — **not** analytics product)
- Separated bg media layer for PPC pages

These must become **explicit pack fields** for the other 11 routes.
