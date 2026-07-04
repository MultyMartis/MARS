# FP-0002 V9-06D8B Home ACF Field Allowlist v1

**Page:** Home (ID 4, front page)  
**Field group:** `group_fp02_page_home`  
**Date:** 2026-07-05

## Writable (applied)

| Field | Key | Type | Source | Classification |
|---|---|---|---|---|
| `home_advantages` | `field_fp02_home_advantages` | repeater | V9 `home-feature-grid.html` | STATIC_V9_CONTENT |
| `home_faq_items` | `field_fp02_home_faq_items` | repeater | V9 `faq.html` items 2–6 | LOCAL_MVP_PLACEHOLDER |

## Attempted — retained D4 value

| Field | Reason |
|---|---|
| `home_hero_slides` | D4 minimal seed already populated; `update_field` returned false when normalizing text; existing title/text acceptable |

## Skipped

| Field | Skip reason |
|---|---|
| `home_cta_title`, `home_cta_text` | EXISTING_SAFE_VALUE (D4 seed matches V9/fallback) |
| `home_service_nav_items` | CPT accordion primary path; D4 seed present |
| `home_intro_bands` | SKIP_NOT_RENDERED (not in D7-B `front-page.php`) |
| `home_reviews_teaser` | DO_NOT_SEED (no invented reviews) |
| `home_blog_teaser_enabled` | SKIP_DEFER_AFTER_MVP (no posts) |
| `home_gallery_media` | SKIP_MEDIA_REQUIRED |

Evidence: `validation/v9-06d8b-home-content-seed/home-acf-field-allowlist.json`
