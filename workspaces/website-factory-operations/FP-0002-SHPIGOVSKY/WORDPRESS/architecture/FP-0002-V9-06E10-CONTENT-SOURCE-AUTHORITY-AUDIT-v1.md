# FP-0002 V9-06E10 Content Source Authority Audit v1

**Evidence JSON:** `validation/v9-06e10-full-backup-wp-port-root-cause-audit/content-source-authority-audit.json`

## Content mutation paths

1. **`inc/v9-static-content.php`** — static copy as PHP arrays (E8); authoritative for alcohol/hub but not HTML-faithful render path
2. **ACF service fields** — D8-C seed on CPT #74 can override fallbacks via `get_field()` in partials
3. **`inc/service-helpers.php`** — variant routing, subnav, programme image fallbacks
4. **`inc/home-fallbacks.php`** — demo FAQ text on Home
5. **`inc/reviews-helpers.php`** — OPTIONS mode replaces static slider content
6. **CPT titles/excerpts** — used when ACF/static empty

## Alcohol leaf route

| Field | Expected V9 | Current source | Drift risk |
|-------|-------------|----------------|------------|
| Hero | static hero block | ACF + `inner-hero.php` alcohol fallbacks | medium |
| Intro/bordered/approach | static leaf partials | `v9-static-content.php` | low |
| Signs | static signs partial | ACF `signs` or fallback | **high** |
| Program | static fixture lorem | `v9-static-content.php` demo | low (fixture) |
| Reviews | static 10 slides | ACF fp02-reviews OPTIONS | medium |
| FAQ | static faq partial | ACF `faq_items` | medium |

## Recommendation

Use **EXACT_V9** static for all non-operator fields. ACF should be **OPERATOR_REAL_CONTENT** overlay only, never silent mutation of V9 copy.
