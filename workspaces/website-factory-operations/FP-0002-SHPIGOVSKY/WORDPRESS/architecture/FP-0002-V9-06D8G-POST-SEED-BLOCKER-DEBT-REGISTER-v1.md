# FP-0002 V9-06D8G Post-Seed Blocker Debt Register v1

**Date:** 2026-07-05  
**Evidence:** `validation/v9-06d8g-post-seed-qa/post-seed-blocker-debt-register.json`

---

## Register

| Item | Class | Blocks visual review | Blocks production | Owner / action |
|---|---|---:|---:|---|
| Map URL missing | OPERATOR_DATA_REQUIRED | no | yes | Operator + options/contacts fields |
| Messenger/social URLs missing | OPERATOR_DATA_REQUIRED | no | yes | Operator fills social_links |
| Legal identifiers missing | OPERATOR_DATA_REQUIRED | no | yes | Legal review |
| Hero/service/gallery media missing | MEDIA_REQUIRED | no | yes | Separate media upload wave |
| FAQ technical placeholder copy | CONTENT_REVIEW | no | no | Olga copy review |
| Service 74 medical copy review | CONTENT_REVIEW | no | yes | Clinical operator |
| English ACF labels/help | ADMIN_UX_DEBT | no | no | D8-F Admin UX Repair |
| Developer-only fields visible | ADMIN_UX_DEBT | no | no | D8-F hide/explain |
| Genotyping/founder/comfort/specialists/reviews | DEFER_AFTER_MVP | no | no | Post-MVP shared blocks |
| Page 6 / Service 73 path collision | TECH_DEBT_NON_BLOCKING | no | no | Path cleanup later |

---

## Blockers before operator visual review

**None** — all seven routes HTTP 200; seeded sections render; gaps are expected debt.

---

## Result

**COMPLETE**
