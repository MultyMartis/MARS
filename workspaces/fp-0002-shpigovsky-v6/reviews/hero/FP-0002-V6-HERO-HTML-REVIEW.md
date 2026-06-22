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

hero_html_status: READY_FOR_OPERATOR_REVIEW
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
├── div.hero__media[data-safe-unknown=hero-media-asset][role=img]
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

- Implementation spec binds hero photo to `container-bleed-media` / CSS background on `hero__media`.
- No discrete hero photo raster was confirmed in `INCOMING/` (search covered all subfolders; only composite `HOME-PAGE-FULL-MOCKUP.jpg` and PDF/FIG assets present).
- Media layer created as empty `div.hero__media` with `data-safe-unknown="hero-media-asset"`.
- No `<img>`, `<picture>`, or `background-image` in HTML/SCSS.

---

## Asset binding

| Field | Value |
|-------|-------|
| Expected role | GROUP-09 full-bleed hero photo |
| Search scope | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/` |
| Confirmed asset | **None** |
| Copied to `src/img/hero/` | **No** |
| SHA-256 | **N/A** |
| Specification binding | `hero_media_binding.asset_status: NOT_CONFIRMED` |

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
| Media placeholder | `role="img"` + `aria-label` on `hero__media` until asset bound |
| CTA | Native `<button>` with visible label |
| Panel content order | Tagline before title (matches visual hierarchy) |

---

## SAFE UNKNOWN

| ID | Item | DOM marker |
|----|------|------------|
| SU-S001-018 | CTA action / href | `data-safe-unknown="hero-consultation-action"` |
| Hero media asset | No confirmed INCOMING photo | `data-safe-unknown="hero-media-asset"` |
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
FP-0002 V6 HERO HTML — PARTIAL
CONTENT OR ASSET BINDING REQUIRES REVIEW
HEADER DESKTOP — UNCHANGED
HERO SCSS NOT AUTHORIZED
```

**Reason for PARTIAL:** Hero HTML structure and confirmed text groups are complete; discrete hero photo asset not found in `INCOMING/` — media layer remains `SAFE UNKNOWN` pending operator asset delivery or extraction approval.
