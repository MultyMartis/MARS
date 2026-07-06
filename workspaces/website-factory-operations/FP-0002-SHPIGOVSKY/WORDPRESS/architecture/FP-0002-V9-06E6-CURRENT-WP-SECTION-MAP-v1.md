# FP-0002 V9-06E6 — Current WP Section Map

**Route:** `/uslugi/zavisimosti/`  
**Template:** `single-service.php` → `subdivision-stack.php`

## Before E6

| Order | Section | Source | Notes |
|------:|---------|--------|-------|
| 0 | hero | `inner-hero.php` | OK (E5) |
| 1 | subnav | `subnav.php` | OK |
| 2 | dependencies | `children.php` | Simplified markup |
| 3 | nature | `nature.php` | Copy drift |
| 4 | mid-cta | `mid-cta.php` | OK structure |
| 5 | program | `program.php` | No images/modifiers |
| 6–14 | stages…final-form | stack partials | Present; CSS not applied (body class) |

**Wrapper:** `article.shpigovsky-service--subdivision` (extra vs static)

## After E6

- Body class `page-service-subdivision-v1` applied
- No article wrapper
- Dependencies/program/nature/team-stats aligned to static V9 markup patterns

JSON: `validation/v9-06e6-service-subdivision-main-layout-repair/current-wp-section-map.json`
