# REPORT — BZPM M9 Phase 2 Sink Profile

**Program:** BZPM Product Roadmap  
**Milestone:** M9 Filter Profile System — Phase 2  
**Category:** 80 — Моечные ванны  
**Environment:** https://zpm.new-site.space/ (**TEST only**)  
**Execution UTC:** 2026-06-14  
**Rollback source:** `SITE-002-STABLE-M8.3-BEFORE-M9-20260615-0159`  
**Phase 1 reference:** `SITE-002-M9-PHASE1-TABLES.md`  
**Deploy manifest:** `projects/ocpilot/sites/site-002/m9-phase2-sinks-work/backups/m9-phase2-deploy-20260614-195231.json`

**Production deploy:** NO  
**Git commit / push:** NO (default policy)  
**Phase 3:** NOT started

---

## Safety Check

### Pre-flight

| Check | Result |
| --- | --- |
| Stable baseline exists | **PASS** — `backups/stable-baselines/SITE-002-STABLE-M8.3-BEFORE-M9-20260615-0159/` + `SITE-002-STABLE-M8.3-BEFORE-M9.md` |
| M9 Phase 1 files exist | **PASS** — `m9-phase1-tables-work/patch/` + deployed manifest `m9-phase1-deploy-20260614-193725.json` |
| Rollback source documented | **PASS** — stable baseline + Phase 1 pre-deploy backups |
| TEST only | **PASS** — deploy target `zpm.new-site.space` |
| Risk gate | **PASS** — single new branch profile (80); profile 301 untouched; no cross-branch conflict |

### Category Scope

| Scope | Policy |
| --- | --- |
| **Active profile (new)** | `80` Моечные ванны + descendants via `oc_category_path` |
| **Preserved profile** | `301` Столы — **unchanged** (`301_stoly.php` byte-identical redeploy) |
| **Out of scope** | 322, 207, 79 root, subcategory overrides, M10 dynamic visibility, admin UI |
| **Legacy behaviour** | Non-profile PLPs (79 hub, 322, 207, …) keep M8.3 Wave 2 global pool |

### Attributes Visible (PRIMARY)

| Control | ID / source | Tier |
| --- | --- | --- |
| Цена | PLP commerce UI | PRIMARY |
| Наличие | PLP switches (`in_stock`, …) | PRIMARY |
| Длина | `oc_product.length` | PRIMARY |
| Ширина | `oc_product.width` | PRIMARY |
| Высота | `oc_product.height` | PRIMARY |
| Размер раковины (ДхШхВ, мм) | **29** | PRIMARY |
| Мойка | **23** | PRIMARY |
| Наличие борта | **25** | PRIMARY |

**Note:** «Количество секций» — **attribute absent in DB** (see UNKNOWN); not included. Tier mapping follows `BZPM-M9-FILTER-PROFILE-SYSTEM-v1.md` branch-80 classification (Отверстие 28, Конструкция 21, Материал 22 → SECONDARY per architecture, not task wishlist PRIMARY).

### Attributes Secondary

Collapsed section **«Дополнительные параметры»** (default closed; opens when a secondary filter is active):

| ID | Attribute |
| ---: | --- |
| 28 | Отверстие под смеситель |
| 47 | Конструкция борта |
| 18 | Высота борта (мм) |
| 33 | Тип опоры |
| 26 | Ножки |
| 21 | Конструкция |
| 31 | Регулируемость опоры по высоте (max мм) |
| 22 | Материал столешницы |
| 17 | В комплекте |

### Attributes Hidden

**Branch-specific (80):** 51 Конструкция полки · 112 Материал полки · 115 Усиление · 20 Макс. нагрузка  

**Global hidden** (`filter_profiles/global_hidden.php` — unchanged from Phase 1):

| Class | IDs |
| --- | --- |
| TEST guard | 16, 105–111 |
| SERVICE | 43, 48, 58, 102 |
| Packaging | 44–46, 52–54, 56, 57 |
| TECHNICAL | 12, 13, 27, 36, 34, 42 |
| Dead / duplicate | 14, 15, 32, 55, 103, 104 |

**Allowlist rule:** any attribute discovered in subtree but not in PRIMARY or SECONDARY lists → **HIDDEN** on profile PLPs (e.g. 49 Производитель, 38 Количество).

### Files To Modify

| Path | Action |
| --- | --- |
| `system/library/zpm/filter_profiles/80_moechnye_vanny.php` | **NEW** |
| `system/library/zpm/filter_profile_resolver.php` | **MODIFIED** — register branch 80 + `profile_file_map` |
| `system/library/zpm/filter_profiles/global_hidden.php` | unchanged (redeploy) |
| `system/library/zpm/filter_profiles/301_stoly.php` | unchanged (redeploy) |
| `catalog/model/catalog/product.php` | unchanged (redeploy) |
| `catalog/controller/product/category.php` | unchanged (redeploy) |
| `catalog/view/theme/default/template/sections/filterssidebar.twig` | unchanged (redeploy) |

Local patch tree: `projects/ocpilot/sites/site-002/m9-phase2-sinks-work/patch/`

### Rollback Method

1. Restore pre-Phase-2 resolver from `m9-phase2-sinks-work/backups/pre-m9-phase2-system__library__zpm__filter_profile_resolver.php` (Phase 1-only resolver).
2. Delete `system/library/zpm/filter_profiles/80_moechnye_vanny.php` on TEST host.
3. Clear `system/storage/cache/template/*` and `cache.category.attributes.*`.
4. Re-run M9 Phase 1 QA (`m9-phase1-qa.py`) to confirm profile 301 intact.

**Full rollback to M8.3:** use `SITE-002-STABLE-M8.3-BEFORE-M9-20260615-0159` baseline files + remove all M9 library files.

---

## Architecture

```
PLP category_id
       │
       ▼
FilterProfileResolver::resolveForCategory()
       │  (80 or descendant → 80_moechnye_vanny.php)
       │  (301 or descendant → 301_stoly.php)
       ▼
getAttributesByCategory($category_ids, $plp_category_id)
       │  Wave 2 STORE_ONLY still applies first
       ▼
applyProfileToAttributes() — allowlist + tier + sort
       │
       ▼
category.php → filter_groups (PRIMARY)
              → filter_secondary_groups (SECONDARY)
              → filter_profile_active flag
       │
       ▼
filterssidebar.twig — M9 profile layout (shared Phase 1 UI):
  Цена → Наличие → L/W/H → PRIMARY attrs → «Дополнительные параметры»
```

**Resolver change (Phase 2 only):** `$registered_branch_roots = [80, 301]`; `$profile_file_map` maps profile IDs to file names — no controller/template changes required.

**Cross-family separation:**

| Branch | Sink cluster 23/28/29 | Table cluster 51/112/115/20 |
| --- | --- | --- |
| 301 Столы | HIDDEN | PRIMARY / SECONDARY |
| 80 Моечные ванны | PRIMARY / SECONDARY | HIDDEN |

**Not implemented (by design):** M10 dynamic visibility · ROAD-004 subcategory overrides · root profile 79 · admin UI · profiles 322/207.

---

## Files Modified

### Deployed to TEST (7 files)

| Remote path | SHA256 (deployed) | Change |
| --- | --- | --- |
| `system/library/zpm/filter_profile_resolver.php` | `05d0cb12…` | **MODIFIED** |
| `system/library/zpm/filter_profiles/80_moechnye_vanny.php` | `7650df0b…` | **NEW** |
| `system/library/zpm/filter_profiles/global_hidden.php` | `63d146bc…` | unchanged |
| `system/library/zpm/filter_profiles/301_stoly.php` | `27b89d42…` | unchanged |
| `catalog/model/catalog/product.php` | `4dea6237…` | unchanged |
| `catalog/controller/product/category.php` | `20b71084…` | unchanged |
| `catalog/view/theme/default/template/sections/filterssidebar.twig` | `bcf9d1e9…` | unchanged |

### Repo artifacts (local)

| Path | Role |
| --- | --- |
| `m9-phase2-sinks-work/patch/` | Source patches |
| `m9-phase2-sinks-work/m9-phase2-deploy.py` | TEST FTP deploy |
| `m9-phase2-sinks-work/m9-phase2-qa.py` | Storefront QA |
| `qa/m9-phase2/m9-phase2-qa-result.json` | QA JSON |

---

## Visible Attributes

QA confirmed **8/8** PRIMARY markers on Моечные ванны PLP (SEO URL and `path=80`):

Цена · Наличие · Длина · Ширина · Высота · Размер раковины · Мойка · Наличие борта.

M9 profile layout confirmed: dimensions render **before** attribute groups and **before** «Дополнительные параметры».

---

## Secondary Attributes

QA confirmed section **«Дополнительные параметры»** present and collapsed by default. Inner groups detected: Отверстие под смеситель, Конструкция борта, Ножки, Конструкция, Материал столешницы (when filled).

---

## Hidden Attributes

QA **hidden_hits=[]** on Моечные ванны PLP — table attrs (Конструкция полки, Макс. нагрузка, …), packaging, SERVICE, TECHNICAL absent from filter sidebar.

Столы regression: sink cluster (Мойка, Отверстие, Размер раковины) remains **absent** on `path=301` — profiles do not conflict.

---

## QA Results

**Summary:** 7 pass · 0 fail · 0 unknown  
**Full JSON:** `projects/ocpilot/sites/site-002/qa/m9-phase2/m9-phase2-qa-result.json`

| ID | URL | Result |
| --- | --- | --- |
| QA-01 | `/katalog/nejtralnoe-oborudovanie/moechnye-vanny/` | **PASS** — primary 8/8, secondary section, profile layout, no hidden hits |
| QA-02 | `/index.php?route=product/category&path=80` | **PASS** — same |
| QA-03 | `/katalog/nejtralnoe-oborudovanie/stoly/` | **PASS** — primary 10/10, profile 301 regression OK |
| QA-04 | `/index.php?route=product/category&path=301` | **PASS** — same |
| QA-05 | `/katalog/nejtralnoe-oborudovanie` | **PASS** — HTTP 200 (legacy pool) |
| QA-06 | Reference sink PDP VMC-P3-2-500 | **PASS** — HTTP 200, no PHP errors |
| QA-07 | Reference table PDP SPKB-18/7-ВЛ5 | **PASS** — HTTP 200, no PHP errors |

PHP warnings/notices: **none detected** on checked URLs.

---

## Rollback Procedure

### Fast rollback (revert Phase 2 only)

1. Upload `pre-m9-phase2-system__library__zpm__filter_profile_resolver.php` → live `filter_profile_resolver.php`.
2. Delete `80_moechnye_vanny.php` on TEST host.
3. Flush Twig + attribute caches.
4. Re-run `m9-phase1-qa.py` — expect 5/5 pass on Phase 1 matrix.

### Full rollback (M8.3 stable)

Same as Phase 1 report: restore baseline files from `SITE-002-STABLE-M8.3-BEFORE-M9-20260615-0159`, remove all M9 library files, flush caches, run Wave 2 QA.

---

## M9 Phase 3 Readiness

| Item | Status |
| --- | --- |
| Profiles 80 + 301 on TEST | **Done** — cross-family separation verified |
| Profile resolver multi-branch | **Ready** — extend `profile_file_map` for 322, 207 |
| Root profile 79 (`hidden_global` absorption) | **Pending** — global list exists but not wired as root inherit |
| Deprecate `AttributeFilterVisibility` duplicate | **Pending** — kept for non-profile PLPs |
| Branch QA matrix (322, 207) | **Not started** — remaining Phase 2 slices per roadmap |
| Subcategory overrides (ROAD-004) | **Not started** — Phase 3 |
| M10 dynamic visibility hooks | **Not started** |

**Recommendation:** operator sign-off on Моечные ванны TEST behaviour; next slice = profile **322** Подтоварники or **207** Зонты (same resolver pattern).

---

## UNKNOWN / SECURITY

| Signal | Detail |
| --- | --- |
| **UNKNOWN** | «Количество секций» filter — attribute **does not exist** in `oc_attribute` registry; cannot be profiled until created + filled (see `SITE-002-WAVE-1B-HERO-ATTRIBUTE-STRATEGY-v1.md`) |
| **UNKNOWN** | Attribute cache files on host empty at deploy flush (0 cleared) — same as Phase 1 |
| **SECURITY** | FTP credentials in deploy scripts match prior operator pattern — not stored in this report |
| **NOTE** | Task wishlist placed Отверстие/Конструкция/Материал in PRIMARY; implementation follows **M9 architecture** tier table (SECONDARY) — matches Phase 1 pattern fidelity to authority doc |

**Phase 3:** NOT started (per task charter).
