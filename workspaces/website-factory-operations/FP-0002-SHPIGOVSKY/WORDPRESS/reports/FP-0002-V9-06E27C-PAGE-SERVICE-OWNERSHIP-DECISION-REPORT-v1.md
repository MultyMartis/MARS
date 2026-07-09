# REPORT — FP-0002 V9-06E27C PAGE SERVICE OWNERSHIP DECISION

**Project:** FP-0002 — Шпиговский  
**Wave:** V9-06E27C  
**Date:** 2026-07-10  
**Mode:** Read-only decision audit — no mutations  
**Baseline:** `d6caab422bc9301caf3f90631558b43e1c9e3bfb` (E27B ancestor PASS)  
**HEAD note:** Task executed at `52470afb8aff84db5b1aee881f31056b20780483` (baseline is ancestor; local/remote synced)

---

## 1. Safety preflight

| Check | Value |
|---|---|
| Volume | X: |
| Label | AI WS |
| Repository | `X:\AI MARS` |
| Branch | `mars/canonical-post-recovery` |
| Local HEAD | `52470afb8aff84db5b1aee881f31056b20780483` |
| Local short HEAD | `52470afb` |
| Remote HEAD | `52470afb8aff84db5b1aee881f31056b20780483` |
| Remote short HEAD | `52470afb` |
| Ahead | 0 |
| Behind | 0 |
| Foreign WIP | Present (unrelated; not staged) |
| Pre-existing staged files | None |
| E27B baseline ancestor check | PASS |
| **Result** | **PASS** |

## 2. Authorization and scope

| Item | Value |
|---|---|
| Operator authorization | YES — V9-06E27C Page Service Ownership Decision |
| Task mode | WORDPRESS READ-ONLY DECISION AUDIT |
| DB writes | 0 |
| Source changes | 0 |
| Runtime delivery | NO |
| Pages trashed/deleted | 0 |
| Pages drafted/unpublished | 0 |
| Service CPT changes | 0 |
| Menu changes | 0 |
| Redirects | 0 |
| Permalink changes | NO |
| Rewrite flush | NO |
| WPilot implementation | NO |
| Production migration | NO |
| Documentation/evidence writes | YES (E27C scope only) |
| **Result** | **PASS** |

## 3. Conflicted object inventory

| Object | Type | ID | Route/path | Status | Content state | Current role | Notes |
|---|---|---:|---|---|---|---|---|
| Зависимости | page | 6 | `/uslugi/zavisimosti/` | publish | legacy_generic_page_copy | shadow_legacy_page | Primary menu `#301`; 0 ACF |
| Психическое здоровье | page | 7 | `/uslugi/psihicheskoe-zdorovie/` | publish | legacy_generic_page_copy | shadow_legacy_page | No menu refs |
| Расстройства пищевого поведения | page | 8 | `/uslugi/rasstroystva-pischevogo-povedeniya/` | publish | legacy_generic_page_copy | shadow_legacy_page | No menu refs |
| Зависимости | service | 73 | `/uslugi/zavisimosti/` | publish | acf_template_managed | canonical_route_owner | 5 children; 75 meta |
| Психическое здоровье | service | 77 | `/uslugi/psihicheskoe-zdorovie/` | publish | acf_template_managed | canonical_route_owner | 6 children |
| Расстройства пищевого поведения | service | 84 | `/uslugi/rasstroystva-pischevogo-povedeniya/` | publish | acf_template_managed | canonical_route_owner | 3 children |
| Лечение алкогольной зависимости | service | 74 | `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | publish | template_fixture | service_leaf_child | Child of `#73` |
| Профилактический анализ | service | 75 | `/uslugi/zavisimosti/profilakticheskiy-analiz/` | publish | template_fixture | service_leaf_child | Child of `#73` |
| Наркотическая зависимость | service | 314 | `/uslugi/zavisimosti/narkoticheskaya-zavisimost/` | publish | skeleton_or_empty | service_leaf_child | Child of `#73` |
| Лекарственная зависимость | service | 315 | `/uslugi/zavisimosti/lekarstvennaya-zavisimost/` | publish | skeleton_or_empty | service_leaf_child | Child of `#73` |
| Поведенческие зависимости | service | 316 | `/uslugi/zavisimosti/povedencheskie-zavisimosti/` | publish | skeleton_or_empty | service_leaf_child | Child of `#73` |

Evidence: `validation/v9-06e27c-page-service-ownership-decision/conflicted-object-inventory.json`

## 4. Route ownership audit

| Route | HTTP | WP queried object | Current owner | Menu owner | Conflict | Notes |
|---|---:|---|---|---|---|---|
| `/uslugi/` | 200 | page `#5` | page `#5` | — | none | Hub correct |
| `/uslugi/zavisimosti/` | 200 | service `#73` | service `#73` | page `#6` | **HIGH** | `postid-73` body class |
| `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | 200 | service `#74` | service `#74` | — | none | Alcohol leaf OK |
| `/uslugi/zavisimosti/profilakticheskiy-analiz/` | 200 | service `#75` | service `#75` | — | none | |
| `/uslugi/zavisimosti/specialistam/` | 404 | — | — | — | none | Static-only gap (separate) |
| `/uslugi/psihicheskoe-zdorovie/` | 200 | service `#77` | service `#77` | — | **HIGH** | Shadow page `#7` |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` | 200 | service `#84` | service `#84` | — | **HIGH** | Shadow page `#8` |

Evidence: `validation/v9-06e27c-page-service-ownership-decision/route-ownership-audit.json`

## 5. Menu ownership audit

| Menu | Item | Linked object | URL | Current route owner | Recommendation | Notes |
|---|---|---|---|---|---|---|
| Primary | `#301` Зависимости | page `#6` | `/uslugi/zavisimosti/` | service `#73` | MENU_RETARGET → `#73` | **Mismatch** |
| Footer | — | — | hardcoded URLs | service CPT | KEEP | Theme `navigation.php` |
| Legal | — | — | — | — | — | No conflict items |

Evidence: `validation/v9-06e27c-page-service-ownership-decision/menu-ownership-audit.json`

## 6. Static V9 / WP architecture comparison

| Route/object | Static V9 role | WP page | WP service CPT | Recommended owner | Notes |
|---|---|---|---|---|---|
| `/uslugi/zavisimosti/` | SERVICE_SUBDIVISION | `#6` shadow | `#73` | **service `#73`** | APPROVED_FULL in V9 |
| `/uslugi/psihicheskoe-zdorovie/` | SERVICE_SUBDIVISION | `#7` shadow | `#77` | **service `#77`** | PLACEHOLDER in V9 |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` | SERVICE_SUBDIVISION | `#8` shadow | `#84` | **service `#84`** | PLACEHOLDER in V9 |
| `/uslugi/` | SERVICES_HUB | `#5` | — | page `#5` | No conflict |

Evidence: `validation/v9-06e27c-page-service-ownership-decision/static-v9-wp-architecture-comparison.json`

## 7. Ownership options risk analysis

| Option | Description | Benefits | Risks | Verdict |
|---|---|---|---|---|
| A | Service CPT owns routes | Architecture + V9 + runtime + ACF alignment | Menu retarget before trash `#6` | **RECOMMENDED** |
| B | Page owns routes | Avoids menu retarget | Breaks `#73` tree; rewrite surgery | NOT_RECOMMENDED |
| C | Keep both temporarily | Defers writes | Admin confusion; blocks E28 QA | NOT_RECOMMENDED |

Evidence: `validation/v9-06e27c-page-service-ownership-decision/ownership-options-risk-analysis.json`

## 8. Recommended ownership decision

| Route/object | Recommended decision | Future action | Risk | Notes |
|---|---|---|---|---|
| `/uslugi/zavisimosti/` | RECOMMENDED_KEEP_SERVICE_CPT | Trash page `#6` in E27D | LOW after menu retarget | Menu `#301` retarget first |
| `/uslugi/psihicheskoe-zdorovie/` | RECOMMENDED_KEEP_SERVICE_CPT | Trash page `#7` in E27D | LOW | No menu conflict |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` | RECOMMENDED_KEEP_SERVICE_CPT | Trash page `#8` in E27D | LOW | No menu conflict |
| Service `#73/#77/#84` | MUST_NOT_TOUCH (keep) | Preserve | — | Canonical owners |
| Post `#750`, pages `#3/#4/#19` | MUST_NOT_TOUCH | — | — | Protected |

Evidence: `validation/v9-06e27c-page-service-ownership-decision/recommended-ownership-decision.json`

## 9. Proposed E27D implementation plan

| Step | Future action | Object IDs | Safety | Validation |
|---:|---|---|---|---|
| 1 | DB checkpoint | — | mysqldump + SHA256 | checkpoint JSON |
| 2 | Retarget Primary menu | `#301` → service `#73` | single meta update | menu + route probe |
| 3 | Pre-trash validation | `#301`, `#73` | read-only | alignment PASS |
| 4 | Trash legacy pages | `#6`, `#7`, `#8` | trash only | status = trash |
| 5 | Route validation | `#73`, `#74`, `#75`, `#77`, `#84` | HTTP probe | 200 expected |

Evidence: `validation/v9-06e27c-page-service-ownership-decision/proposed-e27d-implementation-plan.json`

## 10. Evidence

| Evidence | Captured | Result | Notes |
|---|---:|---|---|
| DB read-only inventory | YES | PASS | pymysql |
| HTTP route probe (10 routes) | YES | PASS | body-class markers |
| Menu ownership query | YES | PASS | Primary conflict found |
| ServicePermalinks source | YES | PASS | rewrite `top` priority |
| Static V9 manifest compare | YES | PASS | v9-route-manifest.json |
| E27A/E27B prior validation | YES | PASS | dependency baseline |
| WP admin screenshots | NO | PARTIAL | HTTP/DB sufficient |

Evidence: `validation/v9-06e27c-page-service-ownership-decision/evidence-result.json`

## 11. No-mutation validation

| Check | Before | After | Result | Notes |
|---|---|---|---|---|
| Page `#6` status/modified | publish / 2026-07-02 | unchanged | PASS | |
| Page `#7` status/modified | publish / 2026-07-02 | unchanged | PASS | |
| Page `#8` status/modified | publish / 2026-07-02 | unchanged | PASS | |
| Service `#73` status/modified | publish / 2026-07-04 | unchanged | PASS | |
| Menu checksum | `550eea2a…` | identical | PASS | |
| Options snapshot | unchanged | unchanged | PASS | |
| DB writes | 0 | 0 | PASS | |

Evidence: `validation/v9-06e27c-page-service-ownership-decision/no-mutation-validation.json`

## 12. Final E27C decision contract

| Item | Final state | Notes |
|---|---|---|
| Conflict diagnosis | Pages `#6/#7/#8` shadow service CPT | DB duplicates |
| Current route owner | service `#73/#77/#84` | HTTP confirmed |
| Current menu owner | page `#6` on Primary only | Mismatch |
| Recommended owner | service CPT | Option A |
| Must not touch yet | `#3,#4,#5,#19,#750,#73` tree | Protected |
| Operator decision | Approve E27D execution | |
| Next task | E27D implementation | |
| E27C verdict | PASS | |

Evidence: `validation/v9-06e27c-page-service-ownership-decision/final-e27c-ownership-decision-contract.json`

## 13. Documentation changes

| File | Action | Reason |
|---|---|---|
| `reports/FP-0002-V9-06E27C-PAGE-SERVICE-OWNERSHIP-DECISION-REPORT-v1.md` | created | Task report |
| `architecture/FP-0002-V9-06E27C-*.md` (9 files) | created | Decision package |
| `validation/v9-06e27c-page-service-ownership-decision/*.json` (12 files) | created | Evidence |
| `WORDPRESS/README.md` | updated | E27C status |
| `WORDPRESS/SOURCE-AUTHORITY.md` | updated | E27C status |
| `FP-0002-SHPIGOVSKY/PROJECT-STATUS.md` | updated | E27C status |

## 14. Git checkpoint

*(Completed after staging — see commit section in agent log)*

## 15. Final verdict

**PASS**

V9-06E27C Page Service Ownership Decision: **COMPLETE**

Read-only discipline: **PASS**

Conflicted object inventory: **PASS**

Route ownership audit: **PASS**

Menu ownership audit: **PASS**

Architecture comparison: **PASS**

Ownership recommendation: **PASS**

Proposed E27D plan: **PASS**

No mutation: **PASS**

No-scope-drift: **PASS**

Recommended next phase: **CREATE_V9_06E27D_PAGE_SERVICE_OWNERSHIP_IMPLEMENTATION_TASK**

## 16. Recommended next action

**CREATE_V9_06E27D_PAGE_SERVICE_OWNERSHIP_IMPLEMENTATION_TASK**

## 17. Final safety statement

Target folder:
X:\AI MARS

V9-06E27C Page Service Ownership Decision performed:
YES

DB writes:
0

Source changes:
0

Runtime delivery:
NO

Pages trashed/deleted:
0

Pages drafted/unpublished:
0

Service CPT changes:
0

Menu changes:
0

Redirects:
0

Permalink changes:
NO

Rewrite flush performed:
NO

WPilot implementation:
NO

Production migration performed:
NO

Protected pages #3/#4/#6/#7/#8/#19 preserved:
YES

Demo post #750 preserved:
YES

Service CPT #73 preserved:
YES

V9 source changed:
NO

V9 dist changed:
NO

DB dump committed:
NO

Backup payload committed:
NO

Runtime snapshot committed:
NO

Helper/temp committed:
NO

Secrets committed:
0
