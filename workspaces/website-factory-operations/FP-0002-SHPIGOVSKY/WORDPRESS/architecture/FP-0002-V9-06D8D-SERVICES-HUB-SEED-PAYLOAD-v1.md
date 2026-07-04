# FP-0002 V9-06D8D Services Hub Seed Payload v1

**Target:** Page #5 only  
**Writable operations:** 2

| Field | Proposed state | Source | Classification | Write | Skip reason |
|---|---|---|---|---:|---|
| `services_hub_intro` | Зависимость, тревога, нарушение пищевого поведения — у каждого из этих состояний | V9_STATIC_SOURCE | STATIC_V9_CONTENT | yes | — |
| `services_hub_query_mode` | unchanged/skip | EXISTING_ACF_VALUE | SKIP_DO_NOT_SEED | no | SKIP_DO_NOT_SEED |
| `services_hub_show_placeholders` | unchanged/skip | EXISTING_ACF_VALUE | SKIP_DO_NOT_SEED | no | SKIP_DO_NOT_SEED |
| `services_hub_faq_items` | repeater[5 rows] | V9_STATIC_SOURCE | LOCAL_MVP_PLACEHOLDER | yes | — |
