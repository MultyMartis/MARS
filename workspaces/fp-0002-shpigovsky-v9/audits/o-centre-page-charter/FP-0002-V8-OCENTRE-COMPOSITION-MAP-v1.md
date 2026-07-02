# FP-0002 V8 O-Centre Composition Map v1

**Date:** 2026-06-29

| Order | Block | Implementation source | Reuse mode | Parameters/content | New source required |
|---:|---|---|---|---:|
| 0 | Header | `partials/layout/header.html` | DIRECT_REUSE | active nav none for O-Centre | 0 |
| 1 | OC-B01 Hero | `partials/sections/services-inner-hero-v2.html` | REUSE_WITH_CONTENT_PARAMETERS | eyebrow, H1, lead, CTA source, hero image | 0 |
| 2 | OC-B02 Nav | `partials/components/internal-page-nav.html` | REUSE_WITH_CONTENT_PARAMETERS | breadcrumbs, subnav listHtml | 0 |
| 3 | OC-B03 Who we are | **NEW** narrative partial (BLK-036) | GENUINELY_UNIQUE | institutional copy C-OC-WHO-* | 1 |
| 4 | OC-B04 Who we treat | `services-category-section-v2.html` OR NEW variant | REUSE_WITH_EXISTING_FUNCTIONAL_MODIFIER | heading, bodyHtml, galleryHtml, hideCta | 0–1 |
| 5 | OC-B05 Steps | `home-rehabilitation-requirements.html` OR `service-leaf-stages-v1.html` | SIMILAR — pick after PDF | steps copy | 0 |
| 6 | OC-B06 Program | `services-program-v2.html` | REUSE_WITH_CONTENT_PARAMETERS | program items, links | 0 |
| 7 | OC-B07 CTA band | `partials/components/program-cta-band.html` | DIRECT_REUSE | guest visit copy | 0 |
| 8 | OC-B08–B09 Narrative + founder | NEW (037/038) + `founder-quote.html` | MIXED | founder params; narrative copy missing | 1 |
| 9 | OC-B10 Comfort | `partials/sections/comfort.html` | DIRECT_REUSE | heading/lead (defaults OK) | 0 |
| 10 | OC-B11 Specialists | `partials/sections/specialists.html` | DIRECT_REUSE | headingId, headingText | 0 |
| 11 | OC-B12 Reviews | `partials/sections/reviews.html` | DIRECT_REUSE | section modifiers | 0 |
| 12 | OC-B13 FAQ | `partials/sections/faq.html` | DIRECT_REUSE | heading; optional About FAQ subset | 0 |
| 13 | Footer | `partials/layout/footer.html` | DIRECT_REUSE | — | 0 |
| 14 | Modal | `partials/components/modal-consultation.html` | DIRECT_REUSE | — | 0 |

**Proposed page file:** `src/pages/o-centre.html` → `dist/o-centre.html` (production folder `/o-centre/` later).

**Explicitly excluded:** `home-gallery.html`, `home-staff-photo.html`, Home hero `hero.html`.
