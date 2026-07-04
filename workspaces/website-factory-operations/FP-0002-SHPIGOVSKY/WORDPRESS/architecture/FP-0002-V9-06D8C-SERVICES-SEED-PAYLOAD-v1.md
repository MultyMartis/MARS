# FP-0002 V9-06D8C Services Seed Payload v1

**Date:** 2026-07-05  
**Evidence:** `validation/v9-06d8c-services-mvp-content-seed/proposed-services-seed-payload.json`

---

## Payload summary

| Service | Field | Classification | Write |
|---:|---|---|---:|
| 74 | intro_text | STATIC_V9_CONTENT | yes |
| 74 | intro_note | STATIC_V9_CONTENT | yes |
| 74 | signs_items | STATIC_V9_CONTENT | yes |
| 74 | programme_items | STATIC_V9_CONTENT | yes |
| 74 | stages | STATIC_V9_CONTENT | yes |
| 74 | faq_items | LOCAL_MVP_PLACEHOLDER | yes |
| 73/77/84 | programme_items | STATIC_V9_CONTENT | yes |
| 73/77/84 | stages | STATIC_V9_CONTENT | yes |
| 73/77/84 | faq_items | LOCAL_MVP_PLACEHOLDER | yes |

All other allowlisted fields: **SKIP** (existing safe value, template fallback, or not rendered).

---

## Rollback

Pre-values captured in checkpoint `services-73-74-77-84-pre-values.json`.

---

## Result

**PASS** — 15 writable operations; 0 blocked
