# FP-0002 V9-06D7C Services Hub Section Map v1

**Date:** 2026-07-05

| Section | V9 source | WP template-part | Data source | Fallback | Implemented | Deferred reason |
|---|---|---|---|---|---:|---|
| hero | hero-inner | services-hub/hero | ACF `services_hub_intro` + STATIC_FROM_V9 | static eyebrow/title | yes | — |
| service-groups | services-category-hub × N | services-hub/service-groups | SERVICE_CPT_QUERY | empty-state / omit | yes | — |
| service-card | hub `__service` | components/service-card | POST_FIELD + service ACF | omit text if empty | yes | — |
| rehabilitation-program | home-rehabilitation-program | services-hub/rehabilitation-program | STATIC_FROM_V9 | always render static | yes | — |
| founder-quote | founder-quote | — | — | — | no | no ACF; content migration |
| comfort | comfort | — | — | — | no | no ACF; content migration |
| faq | faq | services-hub/faq | ACF `services_hub_faq_items` | OMIT_IF_EMPTY | yes | — |
| final-form | final-form | components/final-form | home CTA ACF / defaults | generic copy | yes | live submit deferred |
| genotyping-hub | category-hub genotyping | — | SAFE_UNKNOWN | — | no | no Service CPT parent |
| category-gallery | gallery in hub | — | DEFER_CONTENT_MIGRATION | — | no | no ACF/media |

Machine-readable: `architecture/FP-0002-V9-06D7C-SERVICES-HUB-SECTION-MAP-v1.json`

## Result

PARTIAL (core wave complete; 4 V9 sections deferred)
