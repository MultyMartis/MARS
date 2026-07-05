# FP-0002 V9-06D9-C — Source Hero Repair

**Date:** 2026-07-05

## Files changed

| File | Change |
|------|--------|
| `assets/img/hero/hero-main.png` | Added from V9 static source (SHA256 `48CBA0B7…`) |
| `inc/home-helpers.php` | Added `shpigovsky_get_home_hero_image_fallback()` |
| `template-parts/home/hero.php` | Fallback wiring; dynamic width/height from fallback |

## Behavior

- ACF image URL resolved first via `shpigovsky_acf_image_url()`.
- If empty, theme reads bundled PNG from `SHPIGOVSKY_THEME_DIR/assets/img/hero/hero-main.png`.
- `hero__media` + `hero__image` rendered when either source provides URL.
- D4/D8 text fields (title, tagline, CTA) unchanged.

## Result

PASS — runtime hero media layer restored without DB writes.

**Evidence:** `validation/v9-06d9c-home-hero-parity-repair/source-hero-repair-result.json`
