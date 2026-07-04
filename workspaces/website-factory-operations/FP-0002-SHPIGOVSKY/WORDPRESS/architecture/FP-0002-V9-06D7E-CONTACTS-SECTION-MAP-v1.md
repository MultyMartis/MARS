# FP-0002 V9-06D7E Contacts Section Map v1

**Date:** 2026-07-05  
**Task:** V9-06D7-E Contacts Template Source

| Section | V9 source | WP template-part | Data source | Fallback | Implemented | Deferred reason |
|---|---|---|---|---|---:|---|
| Breadcrumbs wrapper | kontakty.html | page-templates/contacts.php | POST_FIELD | skeleton partial | yes | derived trail V9-07+ |
| Contacts body | contacts-map-body.html | contacts/map-body.php | ACF + SITE_OPTION + POST | STATIC_FROM_V9 | yes | — |
| Location card | contacts-map-body.html | contacts/location-card.php | ACF + SITE_OPTION | STATIC_FROM_V9 | yes | map PNG media |
| Phone row | contacts-map-body.html | contacts/map-body.php | ACF + SITE_OPTION | OMIT_IF_EMPTY | yes | — |
| Messengers | contacts-map-body.html | contacts/map-body.php | ACF + SITE_OPTION | OMIT_IF_EMPTY | yes | — |
| Map figure | contacts-map-body.html | contacts/location-card.php | ACF + SITE_OPTION | OMIT_IF_EMPTY | partial | PNG assets; embed allowlist only |
| Rehabilitation steps | contacts-rehabilitation-steps.html | contacts/rehabilitation-steps.php | STATIC_FROM_V9 | SAFE_STATIC_FALLBACK | yes | — |
| CTA band | program-cta-band.html | components/program-cta-band.php | ACF + SITE_OPTION | STATIC_FROM_V9 | yes | live submit deferred |
| Support list | contacts-rehabilitation-steps.html | contacts/rehabilitation-steps.php | STATIC_FROM_V9 | SAFE_STATIC_FALLBACK | yes | — |
| Photo bleed | contacts-rehabilitation-steps.html | — | — | OMIT_IF_EMPTY | no | DEFER_CONTENT_MIGRATION |

**Result:** PASS
