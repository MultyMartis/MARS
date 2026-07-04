# FP-0002 V9-06D8B Home Content Source Map v1

**Date:** 2026-07-05

| Section | V9 reference | Target field(s) | Seed decision | Reason |
|---|---|---|---|---|
| Hero | `src/partials/sections/hero.html` | `home_hero_slides` | RETAIN D4 | Title/tagline already seeded; image MEDIA_REQUIRED |
| Feature grid | `src/partials/sections/home-feature-grid.html` | `home_advantages` | WRITE | Six cards traceable; section now visible |
| Treatment/prevention | Service CPT + theme static | `home_service_nav_items` | SKIP | CPT query drives accordion |
| Rehabilitation program | Static in theme partial | — | NO ACF | Hardcoded D7-B |
| Gallery | `src/partials/sections/home-gallery.html` | `home_gallery_media` | SKIP_MEDIA | No upload authorized |
| Articles teaser | `src/partials/sections/home-articles.html` | `home_blog_teaser_enabled` | SKIP | No published posts |
| FAQ | `src/partials/sections/faq.html` | `home_faq_items` | WRITE | V9 Q2–6 technical placeholders; Q1 lorem skipped |
| Final form / CTA | `src/partials/sections/final-form.html` | `home_cta_title`, `home_cta_text` | SKIP | D4 + D8-A global options cover CTA |
| Recovery intro | `src/partials/sections/home-recovery-intro.html` | `home_intro_bands` | SKIP_NOT_RENDERED | Not wired in D7-B home orchestration |
| Reviews | `src/partials/sections/reviews.html` | `home_reviews_teaser` | DO_NOT_SEED | Do not invent reviews |

Evidence: `validation/v9-06d8b-home-content-seed/home-content-source-map.json`
