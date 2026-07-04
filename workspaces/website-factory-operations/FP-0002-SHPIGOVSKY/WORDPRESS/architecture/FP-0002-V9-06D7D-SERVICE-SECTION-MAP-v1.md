# FP-0002 V9-06D7D Service Section Map v1

**Date:** 2026-07-05

| Section | V9 source | WP template-part | Data source | Fallback | Implemented | Deferred reason |
|---|---|---|---|---|:---:|---|
| inner-hero | services-inner-hero-v2 | service/inner-hero | ACF_SERVICE_FIELD | POST_FIELD + STATIC_FROM_V9 | yes | |
| subnav | internal-page-nav | service/subnav | POST_FIELD | STATIC_FROM_V9 anchors | yes | |
| children | services-category-section-v2 | service/children | SERVICE_CPT_QUERY | OMIT_IF_EMPTY | yes | |
| intro | service-leaf-intro-v1 | service/intro | ACF_SERVICE_FIELD | POST_FIELD | yes | |
| mid-cta | program-cta-band | service/mid-cta | ACF_SERVICE_FIELD | SITE_OPTION | yes | |
| signs | service-leaf-signs-v1 | service/signs | ACF_SERVICE_FIELD | OMIT_IF_EMPTY | yes | |
| program | services-program-v2 | service/program | ACF_SERVICE_FIELD | STATIC_FROM_V9 | yes | |
| stages | service-leaf-stages-v1 | service/stages | ACF_SERVICE_FIELD | OMIT_IF_EMPTY | yes | |
| faq | faq | service/faq | ACF_SERVICE_FIELD | OMIT_IF_EMPTY | yes | |
| final-form | final-form | components/final-form | SITE_OPTION | STATIC_FROM_V9 | yes | |
| nature | service-subdivision-nature-v1 | — | DEFER_CONTENT_MIGRATION | omit | no | No ACF field |
| comfort | comfort | service/comfort | DEFER_CONTENT_MIGRATION | omit | no | Shared block wave |
| specialists | specialists | — | DEFER_CONTENT_MIGRATION | omit | no | Shared block wave |

JSON: [FP-0002-V9-06D7D-SERVICE-SECTION-MAP-v1.json](FP-0002-V9-06D7D-SERVICE-SECTION-MAP-v1.json)

## Result

PARTIAL — core wave complete; shared V9 blocks deferred
