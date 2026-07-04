# FP-0002 V9-06D8A Site Options Seed Payload v1

**Date:** 2026-07-05  
**Task:** V9-06D8-A Site Options Seed  
**Status:** PLANNED — apply blocked by DB gate

---

## Scope

Options page `fp02-site-settings` only. Eleven fields writable from V9 static; five skipped.

## Writable payload (LOCAL_MVP_PLACEHOLDER from V9 static)

| Field | Proposed value (summary) | V9 source |
|---|---|---|
| `organisation_name` | Шпиговский дом | `head.html` og:site_name |
| `phone_primary` | 8 (925) 183-64-64 | header, footer, kontakty |
| `phone_secondary` | 8 (995) 023-92-26 | header, footer |
| `site_email` | Info@shpigovsky.ru | footer, kontakty |
| `site_address` | Москва, / Московская область (2 lines) | header chrome |
| `opening_hours` | пн-пт: 09:00-19:00 / сб-вс: 09:00-20:00 | kontakty + footer (header hours differ — documented) |
| `default_callback_title` | Заказать звонок | header modal |
| `default_button_label` | Заказать звонок | header/footer CTA |
| `default_secondary_button_label` | Записаться | footer appointment |
| `global_cta_title` | Остались вопросы? | final-form default |
| `global_cta_text` | Опишите вашу ситуацию… | usluga-konechnaya-v1 final-form |

## Skipped fields

| Field | Reason |
|---|---|
| `map_link` | OPERATOR_SUPPLIED — V9 uses PNG maps only |
| `social_links` | OPERATOR_SUPPLIED — V9 href="#" placeholders |
| `legal_org_identifiers` | OPERATOR_SUPPLIED — privacy has demo placeholders |
| `default_callback_text` | DO_NOT_SEED — no stable modal body in V9 |
| `default_consent_text_reference` | DO_NOT_SEED — deferred legal review |

## Classification note

V9 contact phone/email values are **traceable static brand copy**, not invented by this task. They remain **LOCAL_MVP_PLACEHOLDER** until operator confirms production values.

## Evidence

`validation/v9-06d8a-site-options-seed/proposed-site-options-seed-payload.json`
