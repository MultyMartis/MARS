# FP-0002 V9-06D8A Site Options Seed Payload Resume v1

**Date:** 2026-07-05  
**Classification:** LOCAL_MVP_PLACEHOLDER (all writable values)

---

## Writable payload (11 fields)

Values traced to `workspaces/fp-0002-shpigovsky-v9/src/` — not operator-confirmed production data.

| Field | Source | Classification | Write |
|---|---|---|---:|
| organisation_name | V9 static head/header/footer | LOCAL_MVP_PLACEHOLDER | yes |
| phone_primary | V9 header/footer/contacts | LOCAL_MVP_PLACEHOLDER | yes |
| phone_secondary | V9 header/footer | LOCAL_MVP_PLACEHOLDER | yes |
| site_email | V9 footer/contacts | LOCAL_MVP_PLACEHOLDER | yes |
| site_address | V9 header chrome (2 lines) | LOCAL_MVP_PLACEHOLDER | yes |
| opening_hours | V9 footer/contacts variant | LOCAL_MVP_PLACEHOLDER | yes |
| default_callback_title | V9 header modal title | LOCAL_MVP_PLACEHOLDER | yes |
| default_button_label | V9 header/footer buttons | LOCAL_MVP_PLACEHOLDER | yes |
| default_secondary_button_label | V9 footer appointment | LOCAL_MVP_PLACEHOLDER | yes |
| global_cta_title | V9 final-form default | LOCAL_MVP_PLACEHOLDER | yes |
| global_cta_text | V9 usluga-konechnaya final-form | LOCAL_MVP_PLACEHOLDER | yes |

## Skipped (5 fields)

| Field | Reason |
|---|---|
| map_link | OPERATOR_SUPPLIED_REQUIRED |
| social_links | OPERATOR_SUPPLIED_REQUIRED |
| legal_org_identifiers | OPERATOR_SUPPLIED_REQUIRED |
| default_callback_text | DO_NOT_SEED |
| default_consent_text_reference | DO_NOT_SEED |

Evidence: `validation/v9-06d8a-site-options-seed/proposed-site-options-seed-payload-resume.json`
