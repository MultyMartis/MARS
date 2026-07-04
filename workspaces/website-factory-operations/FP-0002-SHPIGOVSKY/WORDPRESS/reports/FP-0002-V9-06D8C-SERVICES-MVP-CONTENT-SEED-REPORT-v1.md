# FP-0002 V9-06D8C Services MVP Content Seed Report v1

**Date:** 2026-07-05  
**Task:** V9-06D8-C Services MVP Content Seed  
**Verdict:** PASS  
**Operator authorization:** YES

---

## Executive summary

Service CPT objects **73 / 74 / 77 / 84** received MVP ACF content under the exact D8-C allowlist. **15 field writes** across four services: priority service **74** received intro/signs/programme/stages/FAQ; parent services **73 / 77 / 84** received shared programme/stages/FAQ blocks from traceable V9 static source. DB checkpoint created. Dry-run PASS. Seven-route smoke ALL_200. Service 74 alcohol-special regression PASS. Visual smoke PASS. Zero runtime/source/home/hub/contacts/options writes. Local helper used but **not committed**.

---

## Preflight

| Check | Result |
|---|---|
| Volume X: / AI WS | PASS |
| Branch mars/canonical-post-recovery | PASS |
| Local HEAD | `4e95a80aa68377aacf8fa19a8cacff29c19b3719` |
| Remote HEAD | `4e95a80aa68377aacf8fa19a8cacff29c19b3719` |
| Ahead / Behind | 0 / 0 |
| Foreign WIP | Present unstaged — not staged |
| Strict HEAD gate | PASS |

---

## Apply summary

| Item | Result |
|---|---|
| DB checkpoint | PASS — `v9-06d8c-services-mvp-content-seed-pre-20260704-205431` |
| Dry-run | PASS — SAFE_TO_APPLY_EXACT_SERVICE_ACF_ALLOWLIST |
| Services attempted | 73, 74, 77, 84 |
| Fields updated | 15 |
| Fields skipped | 25 (CTA fallbacks, hero_lead retained, layout/media forbidden) |
| Errors | 0 |
| Route smoke | ALL_200 (7/7) |
| Service 74 regression | PASS |
| Scope drift | PASS |
| Visual smoke | PASS |

---

## Service 74 (priority)

| Field | Action | Source |
|---|---|---|
| intro_text | Cleared D4 placeholder | EXISTING_ACF_VALUE |
| intro_note | Seeded | V9 `service-leaf-intro-v1.html` |
| signs_items | 9 rows seeded | V9 `service-leaf-signs-v1.html` |
| programme_items | 4 rows seeded | V9 programme titles |
| stages | 4 rows seeded | V9 `service-leaf-stages-v1.html` |
| faq_items | 5 rows seeded | V9 `faq.html` items 2–6 (LOCAL_MVP_PLACEHOLDER) |
| hero_lead | Skipped | Already matches V9 |

---

## Services 73 / 77 / 84

Each received `programme_items`, `stages`, `faq_items` (same shared traceable blocks). Hero/intro/signs/CTA skipped per allowlist and safe-source rules.

---

## Skipped (all services)

- `hero_media` — MEDIA_REQUIRED  
- `service_layout_variant` — forbidden on 74  
- `hero_eyebrow`, `hero_title_override`, `hero_cta_*` — not in D8-C allowlist  
- `cta_*` — STATIC_FALLBACK_ALREADY_IN_TEMPLATE + D8-A options  
- Subdivision hero/intro — V9 lorem; D4 minimal retained  

---

## Evidence

- `validation/v9-06d8c-services-mvp-content-seed/`
- Checkpoint: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06d8c-services-mvp-content-seed-pre-20260704-205431\`

---

## Next step

**CREATE_V9_06D8D_SERVICES_HUB_CONTENT_SEED_TASK**
