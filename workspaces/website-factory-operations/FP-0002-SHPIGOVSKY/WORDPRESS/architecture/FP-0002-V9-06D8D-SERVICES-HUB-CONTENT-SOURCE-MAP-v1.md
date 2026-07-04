# FP-0002 V9-06D8D Services Hub Content Source Map v1

Traceable V9/static sources only. No invented medical claims.

| Section | V9/source reference | Target field(s) | Seed decision | Reason |
|---|---|---|---|---|
| hero tagline | src/pages/uslugi-v2.html heroLead | services_hub_intro | WRITE_IF_DIFFERENT | V9 hero lead; D4 may have partial intro |
| service groups/cards | CPT hierarchy + D7-C template | — | SKIP | SERVICE_CPT_DERIVED_SKIP — not manual ACF |
| programme/rehabilitation | services-program-v2.html theme fallback | — | SKIP | STATIC_FALLBACK_ALREADY_IN_TEMPLATE |
| faq | src/partials/sections/faq.html items 2–6 | services_hub_faq_items | WRITE | LOCAL_MVP_PLACEHOLDER; section omitted when empty |
| final-form/CTA | final-form.html + D8-A options | — | SKIP | Site options + template fallback |
| founder-quote/comfort/genotyping/galleries | uslugi-v2 deferred blocks | — | SKIP | SKIP_DEFER_AFTER_MVP / not rendered D7-C |
| query mode / placeholders | EXISTING_ACF_VALUE | services_hub_query_mode, services_hub_show_placeholders | SKIP | DEVELOPER_ONLY |
