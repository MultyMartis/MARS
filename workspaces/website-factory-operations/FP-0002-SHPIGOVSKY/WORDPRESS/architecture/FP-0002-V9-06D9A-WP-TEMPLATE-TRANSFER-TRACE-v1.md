# FP-0002 V9-06D9A WP Template Transfer Trace v1

**Date:** 2026-07-05  
**Evidence:** `validation/v9-06d9a-visual-parity-audit/wp-template-transfer-trace.json`

| V9 section/partial | WP template/partial | Code exists | Data exists | Rendered | Root cause | Repair |
|--------------------|---------------------|------------:|------------:|---------:|------------|--------|
| hero | template-parts/home/hero.php | yes | no | yes (degraded) | ACF image not seeded | D9-C |
| home-recovery-intro | — | no | no | no | Not ported D7-B | D9-D |
| founder-quote | — | no | no | no | Not ported | D9-D |
| home-treatment-prevention | treatment-prevention.php | yes | partial | yes | Media gaps | D9-E |
| home-gallery | gallery.php | yes | no | no | ACF empty | D9-D |
| home-feature-grid | feature-grid.php | yes | yes | yes | OK | — |
| home-rehabilitation-program | rehabilitation-program.php | yes | partial | yes | Image gaps | D9-E |
| reviews | — | no | no | no | Not ported | D9-D |
| specialists | — | no | no | no | Not ported | D9-D |
| home-articles | articles-teaser.php | yes | no | no | No posts | D9-D |
| faq | faq.php | yes | yes | yes | OK | — |
| final-form | components/final-form.php | yes | yes | yes | OK | — |
| @font-face Inter | assets/css/v9-style.css | yes | n/a | broken | Root path 404 | D9-B |

## Orchestration file

`front-page.php` calls 7 home partials + final-form. Twelve additional V9 sections have no template-parts.

## Result

Template trace complete. Primary gaps: **missing partials** + **empty ACF/media** + **font CSS paths**.
