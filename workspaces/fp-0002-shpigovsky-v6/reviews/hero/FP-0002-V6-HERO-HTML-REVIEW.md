# FP-0002 V6 HERO HTML REVIEW

**Date:** 2026-06-22  
**Workspace:** `workspaces/fp-0002-shpigovsky-v6/`  
**Checkpoint before:** `59b7e92b2805c2faca1c7f64f5b89fc466a8665c`  
**Gate:** Hero HTML structure only — `hero_html_status: READY_FOR_OPERATOR_REVIEW`

---

## Source authority

| Field | Value |
|-------|-------|
| Visual SSOT | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/HOME-PAGE-FULL-MOCKUP.jpg` |
| SHA-256 | `cdd1d5bcc512b617dcf93efa97af88cf4ad99a0895cfc27a63c07bc704945290` |
| Text / hero crops | `specifications/section-001/evidence/03-hero-content-area.jpg` |
| Forbidden sources | FIG, PDF, v1–v5, legacy workspaces — not used |

---

## Specification authority

| Document | Status |
|----------|--------|
| `FP-0002-V6-SECTION-001-SPECIFICATION.json` | `section_001_specification_status: APPROVED` |
| `FP-0002-V6-SECTION-001-GROUP-DECOMPOSITION.md` | SECTION-001-GROUP-02 groups applied |
| `FP-0002-V6-SECTION-001-LAYOUT-SPEC.md` | Composite zone model preserved |
| `FP-0002-V6-SECTION-001-IMPLEMENTATION-SPECIFICATION.md` | Hero groups only — no SCSS |
| `FP-0002-V6-STYLE-FOUNDATION.json` | `site_wide_style_foundation_approved: true` |

---

## Authorization

```text
header_html_status: APPROVED
header_scss_status: APPROVED
header_desktop_status: APPROVED
header_js_authorized: false
header_responsive_authorized: false

hero_html_status: APPROVED
hero_html_authorized: true
hero_scss_authorized: false
hero_js_authorized: false
hero_responsive_authorized: false

implementation_authorized: false
```

---

## SECTION-001 composite structure

```text
div.intro-section
├── header.site-header          (SECTION-001-GROUP-01)
└── section.hero                (SECTION-001-GROUP-02)
```

Header and Hero are internal groups within one composite wrapper — not independent major sections.

`Y=174` is not used as HTML, CSS, or layout boundary.

---

## Hero DOM outline

```text
section.hero
├── div.hero__media
│   └── img.hero__image[src=assets/img/hero/hero-main.png][aria-hidden=true]
└── div.hero__container
    ├── div.hero__panel
    │   └── div.hero__content
    │       ├── p.hero__tagline
    │       └── h1.hero__title
    └── div.hero__actions
        └── button.hero__button[type=button][data-safe-unknown=hero-consultation-action]
```

---

## Hero group mapping

| GROUP-ID | Name | DOM element |
|----------|------|-------------|
| GROUP-09 | Hero photo | `div.hero__media` |
| GROUP-10 | Frosted overlay panel | `div.hero__panel` |
| GROUP-11 | Hero tagline | `p.hero__tagline` |
| GROUP-12 | Hero display title | `h1.hero__title` |
| GROUP-13 | Hero CTA | `button.hero__button` in `div.hero__actions` |

---

## Media layer decision

- Hero photo bound via decorative `<img>` inside `div.hero__media` per operator FIG media exception.
- Asset source: FIG embedded raster `image 13030403` — byte-for-byte copy to `src/img/hero/hero-main.png`.
- No `background-image` in HTML/SCSS.
- FIG not used for layout geometry.

---

## Asset binding

| Field | Value |
|-------|-------|
| Expected role | GROUP-09 full-bleed hero photo |
| Confirmed asset | `src/img/hero/hero-main.png` |
| SHA-256 | `48cba0b7509915e3e2cedb1c5239ff594b9070a5908fc937e345c8517af0bea1` |
| Specification binding | `hero_media_binding.asset_status: CONFIRMED` |

---

## Text extraction

| Element | Source | Text |
|---------|--------|------|
| Tagline | `evidence/03-hero-content-area.jpg` | Центр профилактики и лечения зависимостей |
| Display title | GROUP-12 / task authority | Шпиговский дом |
| CTA label | GROUP-13 / probe evidence | ЗАПИСАТЬСЯ НА КОНСУЛЬТАЦИЮ |

Tagline confirmed from evidence crop — not guessed. Russian typography: `и&nbsp;лечения`.

---

## CTA semantics

- Control: `<button type="button">` — not `<a href="#">`.
- `data-safe-unknown="hero-consultation-action"` — no action implemented.
- Label matches observed JPG text exactly.

---

## Accessibility

| Item | Status |
|------|--------|
| Single `h1` on page | Yes — `hero__title` |
| Media placeholder | Decorative `img` with `aria-hidden="true"` and empty `alt` |
| CTA | Native `<button>` with visible label |
| Panel content order | Tagline before title (matches visual hierarchy) |

---

## SAFE UNKNOWN

| ID | Item | DOM marker |
|----|------|------------|
| SU-S001-018 | CTA action / href | `data-safe-unknown="hero-consultation-action"` |
| SU-S001-003 | Frosted panel radius | Deferred to SCSS gate |
| SU-S001-004 | Photo top corner radius | Deferred to SCSS gate |

---

## Header lock confirmation

| Path | Modified |
|------|----------|
| `src/partials/layout/header.html` | **No** |
| `src/scss/layout/_header.scss` | **No** |
| Header assets (`src/img/branding/`, social, search) | **No** |
| Header geometry (`site-header__container` 1220px / 40px inline / 18px top) | **Unchanged** |

---

## Hero SCSS lock confirmation

| Item | Status |
|------|--------|
| `_hero.scss` | **Not created** |
| Hero import in `style.scss` | **Not added** |
| Inline styles on hero nodes | **None** |
| Forbidden values (`174px`, `904px`, `1138px`) | **Absent from HTML** |

---

## JS lock confirmation

| Path | Modified |
|------|----------|
| `src/js/main.js` | **No** |

No modal, slider, parallax, or CTA behavior added.

---

## Build result

`npm run build` — see task report (expected: Build succeeded).

`dist/` generated locally — not committed.

---

## Final verdict

```text
FP-0002 V6 HERO HTML — APPROVED
HERO MEDIA ASSET — CONFIRMED AND BOUND
HEADER DESKTOP — UNCHANGED
HERO SCSS READY FOR OPERATOR AUTHORIZATION
```

**Reason:** Hero HTML structure and confirmed text groups are complete; original Hero photo extracted from FIG per operator exception and bound in HTML.

---

## FIG asset exception

Operator authorized narrow FIG read for **Hero media asset extraction only**. FIG was not used for layout, geometry, typography, or colors. Visual authority remains JPG mockup SHA `cdd1d5bcc512b617dcf93efa97af88cf4ad99a0895cfc27a63c07bc704945290`.

---

## Original Hero asset

| Field | Value |
|-------|-------|
| FIG embedded hash | `52431f9977e354192c7f56fe9d5503bdc6374fbb` |
| FIG node | `image 13030403` (`1:916`) |
| V6 path | `src/img/hero/hero-main.png` |
| Format | PNG |
| Dimensions | 2230 × 1246 px |
| Bytes | 3,809,988 |

---

## Asset SHA-256

```text
48cba0b7509915e3e2cedb1c5239ff594b9070a5908fc937e345c8517af0bea1
```

Source and destination SHA-256 match (byte-for-byte copy, no transformation).

---

## Visual match

| Check | Result |
|-------|--------|
| Classification | **EXACT HERO SOURCE** |
| Building / tower / trees | Matches SECTION-001-GROUP-02 Hero scene in JPG |
| Text in raster | **None** |
| CTA in raster | **None** |
| Frosted panel in raster | **None** |
| Comparison artefact | `reviews/hero/assets/FP-0002-V6-HERO-FIG-ASSET-COMPARISON.png` |
| Extraction report | `reviews/hero/assets/FP-0002-V6-HERO-FIG-ASSET-EXTRACTION.md` |

Rejected alternate: `de219c6e…` (`image 219`, 860×204) — header decorative strip, not Hero photo.

---

## Media binding

```html
<div class="hero__media">
  <img class="hero__image" src="assets/img/hero/hero-main.png" alt="" aria-hidden="true">
</div>
```

Gulp path: `src/img/hero/hero-main.png` → `dist/assets/img/hero/hero-main.png`.

`data-safe-unknown="hero-media-asset"` **removed** — asset confirmed.

---

## Remaining SAFE UNKNOWN

| ID | Item | DOM marker |
|----|------|------------|
| SU-S001-018 | CTA action / href | `data-safe-unknown="hero-consultation-action"` |
| SU-S001-003 | Frosted panel radius | Deferred to SCSS gate |
| SU-S001-004 | Photo top corner radius | Deferred to SCSS gate |
