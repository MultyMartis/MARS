# FP-0002 V6 ERRONEOUS SECTION ROLLBACK REVIEW

**Date:** 2026-06-22  
**Branch:** `mars/post-cycle8-live-tests`  
**HEAD before:** `1fcf3d29d2fcffa52ee5989ec39df010fea7b44f`  
**Checkpoint reference:** `caaf51e6979917fb3432295858bece8497fa5a04` (not reverted wholesale)

---

## Operator correction

`intro-programs` was implemented immediately after Hero, violating the operator-approved production order **Header → Hero → Footer**. The erroneous block was removed from the active build; artefacts archived as draft-only.

---

## Previous approved production order

```text
Header → Hero → Footer
```

Post-Hero content sections were **not** authorized at this stage.

---

## Erroneous implementation

| Item | Detail |
|------|--------|
| Block | `intro-programs` |
| Commit | `caaf51e` — SECTION-002 variable-first pilot |
| Problem | Implemented before Footer; claimed SECTION-002 production status |
| Active removal | HTML include, SCSS import, compiled CSS |

---

## Commit classification (`caaf51e`)

| File | Purpose | Keep | Remove from active build | Archive | Reason |
|------|---------|-----:|-------------------------:|--------:|--------|
| `src/pages/index.html` (intro include) | Active page | — | YES | — | INTRO_PROGRAMS_ACTIVE_REMOVE |
| `src/partials/sections/intro-programs.html` | Section HTML | — | YES | YES | INTRO_PROGRAMS_ACTIVE_REMOVE → archive |
| `src/scss/sections/_intro-programs.scss` | Section SCSS | — | YES | YES | INTRO_PROGRAMS_ACTIVE_REMOVE → archive |
| `src/scss/style.scss` (import) | Build chain | YES (minus import) | partial | — | FALSE_STATUS_CORRECT |
| `src/scss/base/_root.scss` | Foundation tokens | YES | partial | — | FACTORY_LAW_KEEP (operator-approved rhythm tokens retained) |
| `foundation/FP-0002-V6-SECTION-INVENTORY.md` | Registry | — | — | — | FALSE_STATUS_CORRECT |
| `foundation/FP-0002-V6-BLOCK-INVENTORY.md` | Registry | — | — | — | FALSE_STATUS_CORRECT |
| `foundation/FP-0002-V6-PRODUCTION-PIPELINE.md` | Pipeline | — | — | — | FALSE_STATUS_CORRECT |
| `specifications/section-002/*` | Draft spec | — | YES | YES | INTRO_PROGRAMS_DRAFT_ARCHIVE |
| `reviews/section-002/*` | Draft review/QA | — | YES | YES | INTRO_PROGRAMS_DRAFT_ARCHIVE |
| `logs/v6-*.log` | Append-only history | YES | — | — | LOG_APPEND_CORRECT |
| `logs/v6-violations.log` | Evidence | YES | — | — | FOUNDATION_VERIFICATION_KEEP |

---

## Files removed from active build

- `src/partials/sections/intro-programs.html` (moved to archive)
- `src/scss/sections/_intro-programs.scss` (moved to archive)
- `@@include('partials/sections/intro-programs.html')` from `src/pages/index.html`
- `@use 'sections/intro-programs'` from `src/scss/style.scss`

---

## Artefacts archived

Location: `archive/aborted-section-attempts/intro-programs/`

- `README.md` — DRAFT · NOT ACTIVE · NOT CANONICAL
- `src/partials/sections/intro-programs.html`
- `src/scss/sections/_intro-programs.scss`
- `specifications/` (former `section-002/`)
- `reviews/` (former `section-002/`)

---

## Tokens removed

| Token | Used outside intro-programs | Foundation-approved before caaf51e | Decision |
|-------|----------------------------:|----------------------------------:|----------|
| `--section-gap-same-bg` | NO | NO (PROPOSAL only) | REMOVED |
| `--text-stack-gap` | NO | NO (PROPOSAL only) | REMOVED |

---

## Tokens preserved

| Token | Decision |
|-------|----------|
| `--section-padding-compact` | KEEP — operator-approved Gate 2 |
| `--section-padding-standard` | KEEP — operator-approved Gate 2 |
| `--section-padding-large` | KEEP — operator-approved Gate 2 |
| `--heading-content-gap` | KEEP — operator-approved Gate 2 |
| `--grid-gap-standard` | KEEP — operator-approved Gate 2 |
| `--card-padding-standard` | KEEP — operator-approved Gate 2 |
| `--accordion-row-spacing` | KEEP — operator-approved Gate 2 |
| All Header/Hero/component/control tokens | KEEP — foundation |

---

## Foundation preserved

- Header HTML/SCSS
- Hero HTML/SCSS + asset
- Inter production typography (Google Fonts)
- Font Awesome Pro integration + `fa-search` nav item last
- `components/_button`, `components/_icon`
- CSS Variable First Law contract
- `container-main: 1220px`, `container-hero: 1360px`
- Hero intrinsic image ratio, content-sized CTA
- Header/Hero cleanup from pre-caaf51e commits

---

## CSS Variable First Law status

**ACTIVE.** The Variable-First implementation mechanics passed. The selected production target was wrong. The implementation was removed from the active build.

---

## Active page structure

```text
body
├── div.intro-section
│   ├── Header
│   └── Hero
├── main (empty)
└── p — FOOTER NOT STARTED
```

---

## Section inventory correction

- SECTION-001 — IMPLEMENTED · REVIEWED
- FOOTER — NEXT AUTHORIZED PRODUCTION TARGET
- SECTION-002+ content — NOT STARTED; intro-programs ABORTED ATTEMPT archived

---

## Block inventory correction

- CMP-001–CMP-003 — active IMPLEMENTED
- CMP-004–CMP-007 — NOT STARTED; draft archived only
- Footer — next active block

---

## Roadmap correction

```text
CURRENT IMPLEMENTED: Header, Hero
NEXT: Footer
NOT STARTED: Main content sections, Responsive, JavaScript, SECTION-003+
```

---

## Pipeline correction

Removed claim: `SECTION-002 Variable-First production pilot complete`.

Replaced with: Variable-First foundation verified on aborted noncanonical block attempt. Footer remains next production target.

---

## Build result

**SUCCESS** — `npm run build` @ 2026-06-22

---

## Compiled CSS audit

| Check | Result |
|-------|--------|
| `.intro-programs` in `dist/assets/css/style.css` | **NOT FOUND** |
| `intro-programs` in `dist/index.html` | **NOT FOUND** |
| `data-asset-required` in active HTML | **NOT FOUND** |

---

## Screenshot

`reviews/foundation/visual/FP-0002-V6-HEADER-HERO-FOOTER-PLACEHOLDER-RESTORED.png`

---

## JS lock

**NOT CHANGED** — `javascript_changed: false`

---

## Responsive lock

**NOT STARTED** — `responsive_layout_implemented: false`

---

## Next authorized target

**Footer** — no Footer HTML implemented in this correction task.

---

## Final verdict

**FP-0002 V6 FOOTER-FIRST ORDER — RESTORED**

```text
ERRONEOUS INTRO-PROGRAMS IMPLEMENTATION — REMOVED FROM ACTIVE BUILD
HEADER — PRESERVED
HERO — PRESERVED
FOOTER — NEXT AUTHORIZED TARGET
CSS VARIABLE FIRST LAW — ACTIVE
FOUNDATION VERIFICATION — PASSED
MAIN CONTENT SECTIONS — NOT STARTED
JS NOT CHANGED
RESPONSIVE NOT STARTED
```
