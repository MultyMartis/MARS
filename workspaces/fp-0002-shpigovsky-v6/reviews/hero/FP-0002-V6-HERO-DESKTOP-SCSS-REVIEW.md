# FP-0002 V6 HERO DESKTOP SCSS REVIEW

**Date:** 2026-06-22  
**Workspace:** `workspaces/fp-0002-shpigovsky-v6/`  
**Checkpoint before:** `d446468d9bde44905e1af092f4e6dddc66fa4552`  
**Gate:** Hero desktop SCSS + SECTION-001 visual QA

---

## Source authority

| Field | Value |
|-------|-------|
| Visual SSOT | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/HOME-PAGE-FULL-MOCKUP.jpg` |
| SHA-256 | `cdd1d5bcc512b617dcf93efa97af88cf4ad99a0895cfc27a63c07bc704945290` |
| Hero media asset | `src/img/hero/hero-main.png` (FIG extraction exception — media only) |
| Forbidden | FIG/PDF layout, v1–v5, legacy workspaces |

---

## Authorization

```text
header_html_status: APPROVED
header_scss_status: APPROVED
header_desktop_status: APPROVED

hero_html_status: APPROVED
hero_media_status: SOURCE_ASSET_FOUND
hero_scss_authorized: true
hero_scss_status: READY_FOR_OPERATOR_VISUAL_REVIEW

section_001_desktop_status: READY_FOR_OPERATOR_VISUAL_REVIEW
implementation_authorized: false
```

---

## Original Hero asset

| Field | Value |
|-------|-------|
| Path | `src/img/hero/hero-main.png` |
| SHA-256 | `48cba0b7509915e3e2cedb1c5239ff594b9070a5908fc937e345c8517af0bea1` |
| Natural size | 2230×1246 |
| Transform | NONE — `object-fit: cover` in CSS only |

---

## SCSS files

| File | Role |
|------|------|
| `src/scss/sections/_hero.scss` | Hero desktop styles (created) |
| `src/scss/style.scss` | `@use 'sections/hero';` import added |

Header SCSS untouched.

---

## SECTION-001 relationship

```text
div.intro-section
├── header.site-header     (SECTION-001-GROUP-01) — APPROVED, unchanged
└── section.hero           (SECTION-001-GROUP-02) — styled
```

No fixed SECTION-001 height. Header natural height + Hero media geometry compose the desktop band.

---

## Hero outer geometry

| Measure | JPG @ 1398px | Rendered | Delta | Status |
|---------|--------------|----------|-------|--------|
| Left inset | 18px | 18px padding-inline | 0 | PASS |
| Right inset | 19px | 18px padding-inline | 1px | ACCEPTABLE |
| Visual width | 1361px | 1362px (1398−36) | 1px | ACCEPTABLE |
| Top (page Y) | photo ~174 | hero y≈186 (header natural) | +12px | ACCEPTABLE — header locked |
| Media height | 729px crop | 728px | 1px | PASS |
| Corner radius | ~20px observed | 20px | 0 | PASS |

Hero is wider than `container-main` (1220px) but inset within page — **BP-S001-HERO-001**.

---

## Media geometry

| Token | Value | Classification |
|-------|-------|----------------|
| `$hero-media-inset-inline` | 18px | JPG observed |
| `$hero-media-height` | 728px | `HERO_MEDIA_COMPONENT_GEOMETRY` |
| `$hero-media-radius` | 20px | block proposal |

---

## Object fit and position

| Property | Value |
|----------|-------|
| `object-fit` | `cover` |
| `object-position` | `36% 58%` |

**Evidence:** PIL downscaled crop MAE sweep vs JPG hero crop (18,174)–(1379,903).  
**Reason:** Centers white tower / dome; preserves right tree and entrance.  
**Confidence:** MEDIUM

---

## Corner radius

| Element | Observed | Production | Confidence |
|---------|----------|------------|------------|
| Hero media | soft large corners | 20px | MEDIUM |
| Frosted panel | large rounded rect | 20px | MEDIUM |

---

## Content layering

```text
.hero (relative)
├── .hero__media (z implicit 0)
└── .hero__container (absolute inset 0, flex column end-aligned)
    ├── .hero__panel
    └── .hero__actions → .hero__button
```

No global `z-index` scale required.

---

## Frosted panel

| Measure | JPG | Production |
|---------|-----|------------|
| Width | ~600px (x 400–1000) | 600px |
| Padding | visual ~25/40 | 25px / 40px |
| Position | lower-middle | flex-end + 66px bottom offset |
| Background | semi-white over photo | `rgba(255,255,255,0.24)` |
| Blur | visible | `backdrop-filter: blur(12px)` + fallback |
| Border | light edge | `1px solid rgba(255,255,255,0.35)` |
| Radius | large | 20px |

---

## Typography

| Role | Size | Weight | Line-height | Align | Confidence |
|------|------|--------|-------------|-------|------------|
| Tagline | 16px | 400 | 1.25 | center | MEDIUM |
| H1 display | 40px | 400 | 1.15 | center | MEDIUM |
| CTA label | 13px | 500 | 1 | center | MEDIUM |

**Font-family:** SAFE UNKNOWN — system stack; serif/display deviation documented, not blocking.

---

## Colors

| Role | Sample (JPG) | Selected | Confidence |
|------|--------------|----------|------------|
| Inverse text | white on overlay | `#fff` | HIGH |
| Panel surface | blended frosted | `rgba(255,255,255,0.24)` | MEDIUM |
| CTA accent | center median `149,47,43` | `rgb(149,47,43)` | MEDIUM |
| Page background | unchanged | foundation block token | PASS |

---

## CTA geometry

| Measure | JPG | Rendered | Status |
|---------|-----|----------|--------|
| Width | 297px | 297px | PASS |
| Height | 45px | 45px | PASS (EX-S001-001) |
| Radius | pill | 22px | PASS |
| Center X | ~705 | ~679 | ACCEPTABLE |
| Center Y (in media) | ~641 | ~639 | PASS |
| Gap to panel | ~12px | 12px gap | PASS |

Family: **FAM-BTN-HERO-PRIMARY** — not header outline CTA.

---

## Foundation bindings

| Token | Used for |
|-------|----------|
| `$color-page-background` | page wash (unchanged) |
| OL-01 gaps | 12px panel–CTA, 15px tagline–title |

---

## Block-level values

See `FP-0002-V6-SECTION-001-SOURCE-TO-TOKEN-MAP.md` — BP-S001-HERO-001…007.

---

## Exact geometry exceptions

| ID | Value | Reason |
|----|-------|--------|
| EX-S001-001 | CTA height 45px | probe `hero_red_button` |
| HERO_MEDIA_COMPONENT_GEOMETRY | media height 728px | JPG photo band |
| object-position | 36% 58% | crop alignment |

---

## Build result

```text
npm run build — SUCCESS (2026-06-22)
```

---

## Screenshot evidence

| Artefact | Path |
|----------|------|
| SECTION-001 | `reviews/section-001/visual/FP-0002-V6-SECTION-001-DESKTOP-RENDER-01.png` |
| Hero | `reviews/hero/visual/FP-0002-V6-HERO-DESKTOP-RENDER-01.png` |
| Metrics | `reviews/hero/_qa-hero-metrics.json` |
| Script | `reviews/hero/_hero-visual-qa.py` |

**Viewport:** 1398×950 (SECTION-001 crop compares Y 0–904).

---

## Visual comparison

| Metric | JPG observed | Rendered | Delta | Status |
|--------|--------------|----------|-------|--------|
| Hero left edge | x 18 | 18px inset | 0 | PASS |
| Hero right edge | x 1378 | 18px inset | ~1px | ACCEPTABLE |
| Hero media height | 729px | 728px | 1px | PASS |
| Tower/dome crop | centered building | aligned | visual | ACCEPTABLE |
| Panel center X | ~700 | ~700 | 0 | PASS |
| Panel opacity/blur | frosted | 0.24 + blur 12px | visual | ACCEPTABLE |
| Tagline/H1 stack | centered white | centered white | visual | ACCEPTABLE |
| CTA color | dark red | rgb(149,47,43) | JPEG variance | ACCEPTABLE |
| SECTION-001 MAE | — | 47.02 | — | ACCEPTABLE (fonts/header drift) |
| Hero crop MAE | — | 59.12 | — | ACCEPTABLE (JPEG + font) |

---

## Correction pass

**One pass executed:** comment sanitization (`174` removed from SCSS comment). No Hero geometry changes — no REVISE-only metrics required adjustment beyond initial JPG-derived values.

---

## Remaining deviations

1. Header rendered height ~186px vs JPG nav band ~174px (+12px hero drop) — **header locked**.  
2. Display serif font not loaded — H1 uses system stack.  
3. MAE elevated by JPEG compression and missing webfont.

---

## SAFE UNKNOWN

| Item | Status |
|------|--------|
| Hero display font-family | SAFE UNKNOWN |
| Exact panel blur perception | MEDIUM confidence |
| Site-wide HEX approval for CTA red | block proposal only |

---

## Header lock confirmation

`git diff` — no changes to `header.html`, `_header.scss`, header SVG assets.

---

## JS lock confirmation

`src/js/main.js` — unchanged (zero skeleton).

---

## Responsive lock confirmation

No `@media` in `_hero.scss`. Desktop only.

---

## Final verdict

## READY FOR OPERATOR VISUAL REVIEW

Hero desktop styled and compared with JPG. Header approved and unchanged.
