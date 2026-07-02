# FP-0002 V8 O-Centre Implementation Manifest v1

**Date:** 2026-06-29
**HEAD at start:** `f17287372927531cf70d6a2dd0b1b8c28ac79e1e`
**Branch:** `mars/canonical-post-recovery`

| Page block | Source/component | Action | Files | Risk |
|---|---|---|---|---|
| OC-B01 Hero | `services-inner-hero-v2.html` | REUSE_WITH_CONTENT_PARAMETERS | `src/pages/o-centre.html` | LOW |
| OC-B02 Subnav | `internal-page-nav.html` | REUSE_WITH_CONTENT_PARAMETERS | `src/pages/o-centre.html` | LOW |
| OC-B03 Institutional narrative | `institutional-narrative.html` | CREATE_UNIQUE_PARTIAL | `src/partials/sections/institutional-narrative.html`, `src/scss/style.scss` | MEDIUM |
| OC-B04 Who we treat | `services-category-section-v2.html` | REUSE_WITH_MODIFIER `--o-centre-who-we-treat` | `src/pages/o-centre.html`, `src/scss/style.scss` | LOW |
| OC-B06 Approach | `program-approach-band` (inline, leaf-approach pattern) | PAGE_INLINE_FUNCTION_BASED | `src/pages/o-centre.html`, `src/scss/style.scss` | MEDIUM |
| OC-B06 Program | `services-program-v2.html` | REUSE_WITH_CONTENT_PARAMETERS | `src/pages/o-centre.html`, `src/scss/style.scss` | LOW |
| OC-B07 Mid CTA | `program-cta-band.html` | REUSE | `src/pages/o-centre.html` | LOW |
| OC-B09 Founder quote | `founder-quote.html` | DIRECT_REUSE | `src/pages/o-centre.html` | LOW |
| OC-B08 Infrastructure | `infrastructure-narrative.html` | CREATE_UNIQUE_PARTIAL | `src/partials/sections/infrastructure-narrative.html`, `src/scss/style.scss` | HIGH |
| OC-B07b Guest CTA | `program-cta-band.html` | REUSE (second instance) | `src/pages/o-centre.html` | LOW |
| OC-B11 Specialists | `specialists.html` | REUSE `#specialists` | `src/pages/o-centre.html` | LOW |
| OC-B12 Reviews | `reviews.html` | REUSE `#reviews` | `src/pages/o-centre.html` | LOW |
| OC-B13 Final form | `final-form.html` | REUSE (no FAQ) | `src/pages/o-centre.html` | LOW |

## Shared modifier

- `services-program-v2.html`: optional `lead` via `@@if (lead !== '')` — existing consumers unchanged.

## JS

`main.js changes expected: 0`

## Protected files

Home, services pages, header, footer, modal, main.js, assets — not modified.

Machine-readable: `data/FP-0002-V8-OCENTRE-IMPLEMENTATION-MANIFEST.json`
