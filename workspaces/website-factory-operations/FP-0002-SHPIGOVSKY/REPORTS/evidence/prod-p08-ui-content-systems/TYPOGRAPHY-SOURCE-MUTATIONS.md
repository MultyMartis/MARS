# TYPOGRAPHY-SOURCE-MUTATIONS

**Wave:** PROD-P08 UI content systems — theme source typography  
**Date:** 2026-08-14  
**Scope:** Hardcoded Russian user-facing strings in FP-0002 theme PHP sources only  
**Path root:** `WORDPRESS/theme/shpigovsky/inc/`

## Rules applied

- Unicode NBSP `U+00A0` (not `&nbsp;`) inside PHP quoted strings for plain / `esc_html` contexts
- Short prepositions/conjunctions: в, и, на, с, к, о, у, от, по, из, за, до, об, со, ко, во
- Initials + surname patterns when present
- Numbers + units: года, лет, мин, %
- NBSP before existing em/en dashes (meaning preserved; no copy rewrite)
- Converted legacy `&nbsp;` / `&mdash;` / `&ndash;` entities in these strings to Unicode
- Skipped: URLs, slugs, asset paths, field keys, English technical strings, comments, P07 helpers (`services-hub-helpers.php`, `service-general-helpers.php` not edited)
- Russian «» quotes: already correct in scope; no quote rewrite

## Files changed

| File | Strings changed (approx.) | Unicode NBSP after | Notes |
|------|---------------------------:|-------------------:|-------|
| `v9-static-content.php` | 59 | 204 | 1 legacy `&nbsp;` converted; hub/leaf/program/signs/stages copy |
| `home-fallbacks.php` | 53 | 175 | 170 legacy `&nbsp;` → Unicode; + prep/dash polish |
| `institutional-about-v9-content.php` | 38 | 134 | About hub narrative / approach / infrastructure |
| `reusable-blocks-helpers.php` | 23 | 51 | Fallback UI strings only (`__()`, defaults, founder quote fallbacks, rehab copy) |
| `contacts-helpers.php` | 20 | 46 | Hours, locations labels/alts, intro, rehab steps/support, CTA chrome |

**Total approximate string mutations:** 193  
**Total Unicode NBSP characters in mutated files after:** 610  
**Entity `&nbsp;` remaining in these five files:** 0

## Not changed

- `services-hub-helpers.php` / `service-general-helpers.php` (explicitly out of scope)
- Logic, ACF field keys, context slugs (`fp02-block-*`), `home_url()` paths, map/asset paths
- Meaning / rephrasing of copy

## Tooling evidence (local)

- Script: `REPORTS/evidence/prod-p08-ui-content-systems/_p08_typo_nbsp_source.py`
- Verify helper: `REPORTS/evidence/prod-p08-ui-content-systems/_p08_typo_verify.py`
