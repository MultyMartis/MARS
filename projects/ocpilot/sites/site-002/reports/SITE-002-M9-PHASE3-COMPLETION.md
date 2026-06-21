# REPORT — BZPM M9 Phase 3 Completion

**Program:** BZPM Product Roadmap  
**Milestone:** M9 Filter Profile System — Phase 3  
**Environment:** https://zpm.new-site.space/ (**TEST only**)  
**Execution UTC:** 2026-06-15  
**Authority:** `BZPM-M9-FILTER-PROFILE-SYSTEM-v1.md` · `SITE-002-M9-PHASE1-TABLES.md` · `SITE-002-M9-PHASE2-SINKS.md` · `SITE-002-STABLE-M8.3-BEFORE-M9-20260615-0159`  
**Deploy manifest:** `projects/ocpilot/sites/site-002/m9-phase3-remaining-work/backups/m9-phase3-deploy-20260614-200051.json`  
**Safety check:** `projects/ocpilot/sites/site-002/m9-phase3-remaining-work/M9-PHASE3-SAFETY-CHECK.md`

**Production deploy:** NO  
**Git commit / push:** NO (default policy)  
**M10:** NOT started

---

## Pre-flight

| Check | Result |
| --- | --- |
| Stable baseline | **PASS** — `backups/stable-baselines/SITE-002-STABLE-M8.3-BEFORE-M9-20260615-0159/` + `SITE-002-STABLE-M8.3-BEFORE-M9.md` |
| M9 Phase 1 | **PASS** — `m9-phase1-tables-work/patch/` + `SITE-002-M9-PHASE1-TABLES.md` |
| M9 Phase 2 | **PASS** — `m9-phase2-sinks-work/patch/` + `SITE-002-M9-PHASE2-SINKS.md` |
| TEST only | **PASS** — target `zpm.new-site.space` |
| Risk gate | **PASS** — see Safety Check |

---

## Safety Check

Full document: `m9-phase3-remaining-work/M9-PHASE3-SAFETY-CHECK.md`

| Section | Summary |
| --- | --- |
| **Active categories** | 322 (11 SKU), 207 (23 SKU), 326 (3 SKU) — profiles implemented |
| **Empty categories** | 83 Полки, 86 Стеллажи, 85 Тележки — **0 active SKU** — document-only, no profile files |
| **Visible (PRIMARY)** | 322: dims + 51, 20 · 207: dims + 21 · 326: dims + commerce only |
| **Secondary** | 322: 10 attrs in «Дополнительные параметры» · 207: 34 Страна производства · 326: none |
| **Hidden** | Global list unchanged; branch-specific sink/table attrs excluded per M9 architecture |
| **Files to modify** | 3 new profiles + resolver update; controller/template unchanged |
| **Rollback** | Pre-Phase-3 resolver backup + delete 3 new profile files |

**Risk gate:** PASS — no blockers detected.

---

## Profiles Created

| File | category_id | SHA256 (deployed) |
| --- | ---: | --- |
| `322_podtovarniki.php` | 322 | `87e3c4ed…` |
| `207_zonty.php` | 207 | `8a33cc1c…` |
| `326_telezhki.php` | 326 | `f98cbf90…` |

**Resolver update:** `filter_profile_resolver.php` — registered branch roots `[80, 207, 301, 322, 326]`; `isHiddenAttribute()` allows branch PRIMARY/SECONDARY to override global hidden (INH-04 — attr 34 on zonty).

Local patch tree: `projects/ocpilot/sites/site-002/m9-phase3-remaining-work/patch/`

---

## Active Categories Covered

| category_id | Branch | Profile | QA |
| --- | ---: | --- | --- |
| 301 | Столы | Phase 1 — unchanged | **PASS** regression |
| 80 | Моечные ванны | Phase 2 — unchanged | **PASS** regression |
| 322 | Подтоварники и подставки | **NEW** | **PASS** |
| 207 | Зонты вытяжные | **NEW** | **PASS** |
| 326 | Тележки сервировочные | **NEW** (dims-only) | **PASS** |

**Category isolation verified:** sink cluster absent on 301/322/207/326; table attrs absent on 80/207/326; packaging/SERVICE/TECHNICAL markers absent on all profile PLPs checked.

---

## Empty Categories Deferred

| category_id | Name | Active SKU | Action |
| --- | ---: | --- | --- |
| 83 | Полки | 0 | Spec-only in M9 architecture — activate on first SKU import |
| 86 | Стеллажи | 0 | Spec-only — activate on first SKU import |
| 85 | Тележки | 0 | Inherit legacy pool until populated |

Planned commercial attribute sets documented in `BZPM-M9-FILTER-PROFILE-SYSTEM-v1.md` § Polki / Stellazhi — no PHP profile files created.

---

## Files Modified

### Deployed to TEST (10 files)

| Remote path | Change |
| --- | --- |
| `system/library/zpm/filter_profile_resolver.php` | **MODIFIED** |
| `system/library/zpm/filter_profiles/322_podtovarniki.php` | **NEW** |
| `system/library/zpm/filter_profiles/207_zonty.php` | **NEW** |
| `system/library/zpm/filter_profiles/326_telezhki.php` | **NEW** |
| `system/library/zpm/filter_profiles/global_hidden.php` | unchanged (redeploy) |
| `system/library/zpm/filter_profiles/301_stoly.php` | unchanged (redeploy) |
| `system/library/zpm/filter_profiles/80_moechnye_vanny.php` | unchanged (redeploy) |
| `catalog/model/catalog/product.php` | unchanged (redeploy) |
| `catalog/controller/product/category.php` | unchanged (redeploy) |
| `catalog/view/theme/default/template/sections/filterssidebar.twig` | unchanged (redeploy) |

### Repo artifacts (local)

| Path | Role |
| --- | --- |
| `m9-phase3-remaining-work/patch/` | Source patches |
| `m9-phase3-remaining-work/M9-PHASE3-SAFETY-CHECK.md` | Pre-deploy safety report |
| `m9-phase3-remaining-work/m9-phase3-deploy.py` | TEST FTP deploy |
| `m9-phase3-remaining-work/m9-phase3-qa.py` | Storefront QA |
| `qa/m9-phase3/m9-phase3-qa-result.json` | QA JSON |

---

## QA Results

**Summary:** 12 pass · 0 fail · 0 unknown  
**Full JSON:** `projects/ocpilot/sites/site-002/qa/m9-phase3/m9-phase3-qa-result.json`

| ID | URL | Result |
| --- | --- | --- |
| QA-01 | `/katalog/nejtralnoe-oborudovanie/stoly/` | **PASS** — profile 301 regression, primary 10/10 |
| QA-02 | `/katalog/nejtralnoe-oborudovanie/moechnye-vanny/` | **PASS** — profile 80 regression, primary 8/8 |
| QA-03 | `/katalog/nejtralnoe-oborudovanie/podtovarniki-i-podstavki/` | **PASS** — primary 7/7, secondary section, no hidden hits |
| QA-04 | `path=322` | **PASS** — same |
| QA-05 | `/katalog/nejtralnoe-oborudovanie/zonty-vytyazhnye/` | **PASS** — primary 6/6, secondary «Страна производства» |
| QA-06 | `path=207` | **PASS** — same |
| QA-07 | `/katalog/nejtralnoe-oborudovanie/telezhki-servirovochnye/` | **PASS** — dims-only profile, primary 5/5, «Стандарт» absent |
| QA-08 | `path=326` | **PASS** — same |
| QA-09 | Reference podtovarnik PDP | **PASS** — HTTP 200 |
| QA-10 | Reference telezhka PDP | **PASS** — HTTP 200 |
| QA-11 | Reference table PDP | **PASS** — HTTP 200 |
| QA-12 | Reference sink PDP | **PASS** — HTTP 200 |

PHP warnings/notices: **none detected** on checked URLs.

---

## Rollback Procedure

### Fast rollback (revert Phase 3 only)

1. Upload `m9-phase3-remaining-work/backups/pre-m9-phase3-system__library__zpm__filter_profile_resolver.php` → live resolver (Phase 2 version).
2. Delete on TEST host: `322_podtovarniki.php`, `207_zonty.php`, `326_telezhki.php`.
3. Flush Twig + attribute caches.
4. Re-run `m9-phase2-qa.py` — expect 7/7 pass.

### Full rollback (M8.3 stable)

Restore baseline from `SITE-002-STABLE-M8.3-BEFORE-M9-20260615-0159`, remove all M9 library files, flush caches, run Wave 2 QA.

---

## M9 Completion Status

| M9 scope item | Status |
| --- | --- |
| Profile resolver + schema | **Done** — 5 branch profiles on TEST |
| Populated neutral branches (80, 301, 322, 207, 326) | **Done** — all on TEST with QA pass |
| Empty branches (83, 86, 85) | **Deferred** — documented, no implementation |
| Root profile 79 (`hidden_global` as inherit base) | **Pending** — global list exists; not wired as root inherit |
| Deprecate `AttributeFilterVisibility` on non-profile PLPs | **Pending** |
| Subcategory overrides (ROAD-004) | **Not started** — architecture Phase 3 item |
| M10 dynamic visibility hooks | **Not started** |
| M11 groups UI / accordion render | **Not started** |

**M9 branch profile coverage for active Neutral Equipment SKU:** **complete on TEST** for all populated target branches per M8.1 matrix.

---

## M10 Readiness

| Prerequisite | Status |
| --- | --- |
| Static allowlist profiles on all populated branches | **Ready** |
| PRIMARY / SECONDARY split in template | **Ready** — shared Phase 1 UI |
| Profile isolation verified | **Ready** — no cross-family contamination in QA |
| `dynamic_visibility` hook contract | **Not implemented** — M10 charter required |
| Root profile 79 absorption of Wave 2 hide | **Recommended before M10** — reduces dual hide paths |

**Recommendation:** operator sign-off on TEST behaviour for 322/207/326; M10 may proceed with DV-02…DV-07 runtime rules on existing profile allowlists. **Do not start M10 in this task.**

---

## UNKNOWN / SECURITY

| Signal | Detail |
| --- | --- |
| **UNKNOWN** | Live SKU counts post-Wave-2 — M8.1 baseline (322=11, 207=23, 326=3) used; not re-audited on deploy day |
| **UNKNOWN** | Attribute cache on host empty at flush (0 cleared) — same as Phase 1/2 |
| **NOTE** | REVIEW attrs 19/24/30 on 322 included in SECONDARY allowlist; M10 DV-06 may hide when fill < threshold |
| **SECURITY** | FTP credentials in deploy scripts match prior operator pattern — not stored in this report |

**M10:** NOT started (per task charter).
