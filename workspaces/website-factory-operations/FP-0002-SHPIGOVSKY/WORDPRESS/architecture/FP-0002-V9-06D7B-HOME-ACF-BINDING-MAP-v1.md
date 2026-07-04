# FP-0002 V9-06D7B Home ACF Binding Map v1

**Date:** 2026-07-05

ACF group: `group_fp02_page_home` (read-only; JSON not modified in D7-B)

| Section | ACF fields | Data source class | Empty behavior | ACF unavailable |
|---|---|---|---|---|
| hero | home_hero_slides | ACF_HOME_FIELD + POST_FIELD | blogname + static tagline; omit image | Same fallbacks |
| feature-grid | home_advantages | ACF_HOME_FIELD | OMIT_IF_EMPTY | OMIT |
| treatment-prevention | home_service_nav_items (fallback) | QUERY_DYNAMIC + ACF | OMIT if no CPT groups and no nav rows | Query only if CPT exists |
| rehabilitation-program | — | STATIC_FROM_V9 | Always renders abbreviated static structure | Same |
| gallery | home_gallery_media | ACF_HOME_FIELD | OMIT_IF_EMPTY | OMIT |
| articles-teaser | home_blog_teaser_enabled | ACF + QUERY_DYNAMIC | OMIT if disabled or no posts | OMIT |
| faq | home_faq_items | ACF_HOME_FIELD | OMIT_IF_EMPTY | OMIT |
| final-form | home_cta_title, home_cta_text | ACF + SITE_OPTION | i18n defaults | i18n defaults |

Unused home fields in D7-B: `home_intro_bands`, `home_reviews_teaser` — reserved for deferred partials.

Evidence: `validation/v9-06d7b-home-template-source/home-acf-binding-inventory.json`

## Result

COMPLETE
