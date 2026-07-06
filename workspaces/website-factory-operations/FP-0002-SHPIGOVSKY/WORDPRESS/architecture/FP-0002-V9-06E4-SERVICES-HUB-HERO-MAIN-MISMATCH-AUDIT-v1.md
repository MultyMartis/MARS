# FP-0002 V9-06E4 Services Hub Hero/Main Mismatch Audit

**Date:** 2026-07-06

## Root cause

`template-parts/services-hub/hero.php` renders **home-style** `hero hero--inner` without media. Static V9 authority (`uslugi-v2.html`) requires `services-inner-hero-v2` with `services-hero.webp`.

## Answers

| Question | Answer |
|----------|--------|
| Which template renders `/uslugi/`? | `page-templates/services-hub.php` (correct assignment) |
| Why Home hero? | Hub hero partial hardcoded to inner hero pattern — not ACF fallback |
| Hardcoded? | **Yes** — `services-hub/hero.php` |
| Static hero type | `services-inner-hero-v2` |
| Asset missing? | **No** — `services-hero.webp` in theme; **not wired** |
| Main wrapper drift? | **Yes** — `page-uslugi` vs `page-uslugi-v2__main` |

## E5 files

- `template-parts/services-hub/hero.php`
- `page-templates/services-hub.php`
- `template-parts/services-hub/service-groups.php` (section-v2 alignment)
- `inc/services-hub-helpers.php` (body class)

Evidence JSON: `validation/v9-06e4-services-layout-shared-bg-visual-reconciliation-audit/services-hub-hero-main-mismatch-audit.json`
