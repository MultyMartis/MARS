# FP-0002 V9-06D8G ACF Content Integrity Audit v1

**Date:** 2026-07-05  
**Evidence:** `validation/v9-06d8g-post-seed-qa/acf-content-integrity-audit.json`

Read-only audit across D8-A…D8-E seeded scopes. No DB/ACF writes during D8-G.

---

## Scope summary

| Scope | Seeded fields checked | Skipped fields checked | Result |
|---|---|---:|---|
| D8-A Site Options | 11 | 5 | PASS |
| D8-B Home #4 | 2 + hero retained | 3 media/deferred | PASS |
| D8-C Services 73/74/77/84 | programme/stages/FAQ (+74 intro/signs) | hero_lead D4 retained | PASS |
| D8-D Hub #5 | intro + FAQ | developer fields unchanged | PASS |
| D8-E Contacts #20 | intro, address, blocks | map/messengers skipped | PASS |

---

## Notable classifications

| Field | Classification | Note |
|---|---|---|
| Site options phone/email | LOCAL_MVP_PLACEHOLDER | D8-A seeded |
| home_advantages / home_faq_items | STATIC_V9_CONTENT | D8-B seeded |
| home_hero_slides | EXISTING_SAFE_VALUE | D4 minimal seed retained |
| Service 74 signs/programme/FAQ | STATIC_V9_CONTENT | D8-C MVP seed |
| services_hub_intro/FAQ | STATIC_V9_CONTENT | D8-D seeded |
| contacts_form_intro/blocks | STATIC_V9_CONTENT | D8-E seeded |
| hero_lead (services) | EXISTING_SAFE_VALUE | Pre-D8-C D4 values; not cleared by D8-C |
| contacts_phones | EXISTING_SAFE_VALUE | D8-E skipped; canonical phones in Options |
| map_link / social_links | SKIPPED_EXPECTED | Operator deferred |

---

## Result

**PASS** — no unexpected empty seeded fields; no D8-wave mutations to skipped scopes during D8-G.
