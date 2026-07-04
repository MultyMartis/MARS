# FP-0002 V9-06D8D Services Hub ACF Field Allowlist v1

**Page ID:** 5 (`/uslugi/`)  
**Field group:** `group_fp02_page_services_hub`  
**Verdict:** PASS

## Authorized writes

| Field | Key | Type | Write |
|---|---|---|---|
| `services_hub_intro` | `field_fp02_services_hub_intro` | textarea | YES |
| `services_hub_faq_items` | `field_fp02_services_hub_faq_items` | repeater | YES |

## Forbidden in D8-D

- `services_hub_query_mode` — DEVELOPER_ONLY
- `services_hub_show_placeholders` — DEVELOPER_ONLY
- `post_title`, `post_content`
- Home / Service CPT / Contacts / options
- Media uploads

## Inventory

| Field | Field key | Type | Old | Source | D7-C | Decision | Risk | Result |
|---|---|---|---|---|---:|---|---|---|
| `services_hub_intro` | `field_fp02_services_hub_intro` | textarea | populated | V9_STATIC_SOURCE | True | WRITE | LOW | CONFIRMED |
| `services_hub_query_mode` | `field_fp02_services_hub_query_mode` | select | populated | EXISTING_ACF_VALUE | False | SKIP | LOW | CONFIRMED |
| `services_hub_show_placeholders` | `field_fp02_services_hub_show_placeholders` | true_false | populated | EXISTING_ACF_VALUE | False | SKIP | LOW | CONFIRMED |
| `services_hub_faq_items` | `field_fp02_services_hub_faq_items` | repeater | empty | V9_STATIC_SOURCE | True | WRITE | LOW_MVP_PLACEHOLDER | CONFIRMED |

Writable count: **2** · Skipped: **2**
