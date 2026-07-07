# REPORT — FP-0002 V9-06E14 SERVICE ADMIN FIELDS + SERVICE TREE DEMO CONTENT REPAIR

**Wave:** V9-06E14  
**Date:** 2026-07-07  
**Baseline:** E13 @ `67248b3f` (ancestor PASS; HEAD `148696fc`)

## 1. Safety preflight

| Item | Value |
|---|---|
| Volume | X |
| Label | AI WS |
| Repository | `X:\AI MARS` |
| Branch | `mars/canonical-post-recovery` |
| Local HEAD | `148696fca496f17befcc2114b64a39e51aac1430` |
| Local short HEAD | `148696fc` |
| Remote HEAD | `148696fca496f17befcc2114b64a39e51aac1430` |
| Remote short HEAD | `148696fc` |
| Ahead | 0 |
| Behind | 0 |
| Foreign WIP | Present (unrelated; untouched) |
| Pre-existing staged files | None |
| E13 ancestor check | PASS |
| Result | **PASS** |

## 2. Authorization and scope

| Scope item | Result |
|---|---|
| Operator authorization | YES — V9-06E14 charter |
| Task mode | SCOPED SERVICE DATA / ADMIN REPAIR |
| DB checkpoint | YES |
| DB writes | YES — service tree + ACF mini-descriptions + demo seeds |
| Source/theme changes | YES — 2 files |
| Project plugin changes | YES — 1 file |
| Third-party plugin changes | 0 |
| ACF JSON changes | YES — 1 file |
| Runtime delivery | YES |
| Legal/reviews/menu/privacy | 0 |
| V9 src/dist changes | 0 |
| Result | **PASS** |

## 3. Baseline service/admin audit

| Area | Result | Notes |
|---|---|---|
| Hub query display mode | PASS | `services_hub_query_mode` on page 5; default `grouped_by_parent` |
| Hub card text source (before) | HARDCODED/V9 OVERRIDE | `shpigovsky_build_services_hub_child_card` used V9 map text directly, bypassing admin |
| Mini-description field | ABSENT | No `service_short_description` before E14 |
| Zavisimosti children | 3 publish | alcohol, profilakticheskiy, specialistam (76) |
| Canonical specialistam page | PASS publish | Page ID 15 `/o-centre/specialistam/` |
| Psych/eating layout | subdivision ACF | IDs 77, 84 — skeleton hero text before seed |

Evidence: `validation/v9-06e14-service-admin-fields-service-tree-demo-content-repair/baseline-service-admin-audit.json`

## 4. DB checkpoint

| Item | Result | Notes |
|---|---|---|
| Checkpoint path | PASS | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e14-service-admin-fields-service-tree-demo-content-repair-pre-20260707T104328Z\` |
| Full dump | PASS | `mars_wp_fp0002.sql` |
| Service rows snapshot | PASS | `service-posts-before.json` |
| Postmeta snapshot | PASS | `service-postmeta-before.json` |
| Restore instructions | PASS | `RESTORE.md` |
| Result | **PASS** |

## 5. Repair plan

| Component | Planned repair | Safety |
|---|---|---|
| Mini-description field | `service_short_description` / `Мини-описание` on all services | ACF local group only |
| Hub rendering | ACF → V9 → DEMO in grouped + flat | No query mode preference change |
| Remove `/uslugi/zavisimosti/specialistam/` | `wp_trash_post(76)` | Page 15 protected |
| New demo leaves | 314–316 under parent 73 | DEMO classified |
| Child order | profilakticheskiy last (menu_order 50) | metadata only |
| Psych/eating demo | subdivision confirmed + hero/intro seed | DEMO, not exact V9 page claim |

## 6. Service mini-description admin field

| Field | Location | Result | Notes |
|---|---|---|---|
| `service_short_description` | `group_fp02_service_layout_hero` / all `service` CPT | PASS | Label `Мини-описание`; textarea; instructions for `/uslugi/` cards |

## 7. Services hub mini-description rendering

| Mode | Source | Result | Notes |
|---|---|---|---|
| Grouped by parent | ACF `service_short_description` → V9 → DEMO | PASS | Seeded alcohol EXACT_V9 text visible |
| Flat | Same resolver | PASS | Parent + child cards use admin field |

## 8. Service mini-description seed

| Service | Status | Notes |
|---|---|---|
| Alcohol (74) | EXACT_V9 | V9 hub child copy seeded |
| New narcotic/medicine/behavioral (314–316) | PRESERVED / EXACT_V9 mini | V9 authority text for mini; page body DEMO |
| Profilakticheskiy (75) | DEMO | Explicit DEMO mini text |
| Psych/eating children | DEMO | V9 fixture lorem classified DEMO |
| Subdivision parents | DEMO | Flat-mode card text |

Full table: `service-mini-description-seed-result.json`

## 9. Dependencies service tree repair

| Item | Before | After | Result |
|---|---|---|---|
| `/uslugi/zavisimosti/specialistam/` service 76 | publish | trash | PASS |
| `/o-centre/specialistam/` page 15 | publish | publish | UNAFFECTED |
| `narkoticheskaya-zavisimost` | missing | ID 314 publish | PASS |
| `lekarstvennaya-zavisimost` | missing | ID 315 publish | PASS |
| `povedencheskie-zavisimosti` | missing | ID 316 publish | PASS |
| Child order | specialistam last | profilakticheskiy last | PASS |

Order: alcohol 10 → narcotic 20 → medicine 30 → behavioral 40 → profilakticheskiy 50.

## 10. New dependency demo leaf pages

| Page | Route | Parent | Content status | Result |
|---|---|---|---|---|
| Наркотическая зависимость | `/uslugi/zavisimosti/narkoticheskaya-zavisimost/` | 73 | DEMO | PASS |
| Лекарственная зависимость | `/uslugi/zavisimosti/lekarstvennaya-zavisimost/` | 73 | DEMO | PASS |
| Поведенческие зависимости | `/uslugi/zavisimosti/povedencheskie-zavisimosti/` | 73 | DEMO | PASS |

Layout: `placeholder` → leaf stack. Hero/intro/note seeded as DEMO.

## 11. Psych/eating subdivision demo setup

| Route | Template/layout | Content status | Result | Notes |
|---|---|---|---|---|
| `/uslugi/psihicheskoe-zdorovie/` | subdivision | DEMO | PASS | V9 group intro/lead seeded to hero/intro |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` | subdivision | DEMO | PASS | Same pattern |

## 12. Runtime delivery

| File | Delivered | Result |
|---|---:|---|
| `theme/shpigovsky/inc/services-hub-helpers.php` | YES | PASS |
| `theme/shpigovsky/inc/v9-static-content.php` | YES | PASS |
| `plugins/shpigovsky-core/src/Fields/FieldGroups.php` | YES | PASS |
| `acf-json/group_fp02_service_layout_hero.json` | YES | PASS |

Evidence: `runtime-delivery-result.json`

## 13. Post-repair validation

| Route/check | Result | Notes |
|---|---|---|
| Required routes HTTP 200 | PASS | 9/9 including new leaves |
| `/uslugi/zavisimosti/specialistam/` | PASS | HTTP 404 |
| `/o-centre/specialistam/` | PASS | HTTP 200 |
| Regression `/`, `/kontakty/`, `/otzyvy/`, legal | PASS | HTTP 200 |
| Alcohol leaf | PASS | HTTP 200 (no E13 regression) |
| Hub grouped + flat mini-descriptions | PASS | See rendering JSON |
| Admin data | PASS | 17 mini-descriptions seeded |

## 14. Screenshots

| Screenshot | Captured | Result |
|---|---:|---|
| runtime-uslugi-grouped-mini-descriptions-e14.png | YES | PASS |
| runtime-uslugi-flat-mini-descriptions-e14.png | YES | PASS |
| runtime-zavisimosti-children-order-e14.png | YES | PASS |
| runtime-new-narcotic-demo-leaf-e14.png | YES | PASS |
| runtime-new-medicine-demo-leaf-e14.png | YES | PASS |
| runtime-new-behavioral-demo-leaf-e14.png | YES | PASS |
| runtime-psych-subdivision-demo-e14.png | YES | PASS |
| runtime-eating-subdivision-demo-e14.png | YES | PASS |
| runtime-alcohol-leaf-regression-e14.png | YES | PASS |
| runtime-o-centre-specialistam-regression-e14.png | YES | PASS |
| admin-service-mini-description-field-e14.png | NO | PARTIAL — admin auth not automated |

**10/10** frontend screenshots PASS.

## 15. Final service content/demo inventory

See `final-service-content-demo-inventory.json` — **COMPLETE** (17 active services + trashed 76 recorded).

## 16. No-scope-drift

All scope boundaries respected. Third-party plugins untouched. V9 src/dist unchanged. Rewrite flush not performed. **PASS**

## 17. Documentation changes

| File | Action | Reason |
|---|---|---|
| `reports/FP-0002-V9-06E14-...-REPORT-v1.md` | created | Wave report |
| `architecture/FP-0002-V9-06E14-*.md` | created | E14 architecture pack |
| `validation/v9-06e14-.../*.json` + screenshots | created | Evidence |
| `WORDPRESS/README.md` | updated | Phase status |
| `WORDPRESS/SOURCE-AUTHORITY.md` | updated | E14 authority note |
| `PROJECT-STATUS.md` | updated | Project phase |

## 18. Git checkpoint

Staged only E14 allowlisted source, ACF JSON, docs, validation evidence (no helpers/DB dumps/runtime).

## 19. Final verdict

**PASS**

V9-06E14 Service Admin Fields + Service Tree Demo Content Repair: **COMPLETE**

| Sub-verdict | Status |
|---|---|
| Service mini-description field | PASS |
| Services hub grouped mode | PASS |
| Services hub flat mode | PASS |
| Dependencies tree | PASS |
| Specialistam service removal | PASS |
| Canonical /o-centre/specialistam | UNAFFECTED |
| New dependency demo leaves | PASS |
| Psych/eating subdivision demo | PASS |
| Final inventory | COMPLETE |
| Hero/alcohol/accepted regression | PASS |
| No-scope-drift | PASS |

**Recommended next phase:** `CREATE_V9_06E15_OPERATOR_SERVICE_TREE_VISUAL_QA_TASK`

## 20. Recommended next action

**CREATE_V9_06E15_OPERATOR_SERVICE_TREE_VISUAL_QA_TASK**

## 21. Final safety statement

Target folder: `X:\AI MARS`

V9-06E14 Service Admin Fields + Service Tree Demo Content Repair performed: **YES**

DB checkpoint: **YES**

DB writes: **46**

Source/theme changes: **2**

Project plugin changes: **1**

Third-party plugin changes: **0**

ACF JSON changes: **1**

Runtime delivery: **YES**

ACF value writes: **40**

Native content writes: **6**

Legal text writes: **0**

Reviews data writes: **0**

Media uploads: **0**

Attachment creation: **0**

Service tree writes: **6**

Menu writes: **0**

Privacy setting writes: **0**

Rewrite flush performed: **NO**

OCPilot writes: **0**

Production migration performed: **NO**

Canonical /o-centre/specialistam affected: **NO**

Hero system regression: **NO**

Alcohol leaf regression: **NO**

Accepted pages regression: **NO**

V9 source changed: **NO**

V9 dist changed: **NO**

DB dump committed: **NO**

Runtime snapshot committed: **NO**

Helper/temp committed: **NO**

Secrets committed: **0**
