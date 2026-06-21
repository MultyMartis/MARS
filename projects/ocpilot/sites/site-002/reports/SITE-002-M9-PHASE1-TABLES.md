# REPORT — BZPM M9 Phase 1 Tables Profile

**Program:** BZPM Product Roadmap  
**Milestone:** M9 Filter Profile System — Phase 1  
**Category:** 301 — Столы  
**Environment:** https://zpm.new-site.space/ (**TEST only**)  
**Execution UTC:** 2026-06-14  
**Rollback source:** `SITE-002-STABLE-M8.3-BEFORE-M9-20260615-0159`  
**Deploy manifest:** `projects/ocpilot/sites/site-002/m9-phase1-tables-work/backups/m9-phase1-deploy-20260614-193725.json`

**Production deploy:** NO  
**Git commit / push:** NO (default policy)

---

## Safety Check

### Pre-flight

| Check | Result |
| --- | --- |
| Stable baseline exists | **PASS** — `projects/ocpilot/sites/site-002/backups/stable-baselines/SITE-002-STABLE-M8.3-BEFORE-M9-20260615-0159/` + manifest |
| Rollback source documented | **PASS** — `SITE-002-STABLE-M8.3-BEFORE-M9.md` |
| TEST only | **PASS** — deploy target `zpm.new-site.space`; no production paths |
| Risk gate | **PASS** — single branch profile (301); other categories unchanged |

### Category Scope

| Scope | Policy |
| --- | --- |
| **Active profile** | `301` Столы + descendants via `oc_category_path` |
| **Out of scope** | 80, 322, 207, 79 root, subcategory overrides, M10 dynamic visibility |
| **Legacy behaviour** | All non-301 PLPs keep M8.3 Wave 2 global pool + `AttributeFilterVisibility` |

### Attributes Visible (PRIMARY)

| Control | ID / source | Tier |
| --- | --- | --- |
| Цена | PLP commerce UI | PRIMARY |
| Наличие | PLP switches (`in_stock`, …) | PRIMARY |
| Длина | `oc_product.length` | PRIMARY |
| Ширина | `oc_product.width` | PRIMARY |
| Высота | `oc_product.height` | PRIMARY |
| Материал столешницы | **22** | PRIMARY |
| Конструкция полки | **51** | PRIMARY |
| Тип опоры | **33** | PRIMARY |
| Макс. нагрузка (до, кг) | **20** | PRIMARY |
| Наличие борта | **25** | PRIMARY |

### Attributes Secondary

Collapsed section **«Дополнительные параметры»** (default closed; opens when a secondary filter is active):

| ID | Attribute |
| ---: | --- |
| 21 | Конструкция |
| 112 | Материал полки |
| 26 | Ножки |
| 31 | Регулируемость опоры по высоте (max мм) |
| 115 | Усиление |
| 18 | Высота борта (мм) |
| 47 | Конструкция борта |

### Attributes Hidden

**Branch-specific (301):** 23 Мойка · 28 Отверстие под смеситель · 29 Размер раковины  

**Global hidden** (`filter_profiles/global_hidden.php` — packaging, SERVICE, TEST guard, TECHNICAL, dead defs):

| Class | IDs |
| --- | --- |
| TEST guard | 16, 105–111 |
| SERVICE | 43, 48, 58, 102 |
| Packaging | 44–46, 52–54, 56, 57 |
| TECHNICAL | 12, 13, 27, 36, 34, 42 |
| Dead / duplicate | 14, 15, 32, 55, 103, 104 |

**Allowlist rule:** any attribute discovered in subtree but not in PRIMARY or SECONDARY lists → **HIDDEN** on profile PLPs.

### Files To Modify

| Path | Action |
| --- | --- |
| `system/library/zpm/filter_profile_resolver.php` | **NEW** |
| `system/library/zpm/filter_profiles/global_hidden.php` | **NEW** |
| `system/library/zpm/filter_profiles/301_stoly.php` | **NEW** |
| `catalog/model/catalog/product.php` | Profile hook in `getAttributesByCategory()` |
| `catalog/controller/product/category.php` | PRIMARY / SECONDARY split + template flags |
| `catalog/view/theme/default/template/sections/filterssidebar.twig` | M9 layout branch for profile PLPs |

Local patch tree: `projects/ocpilot/sites/site-002/m9-phase1-tables-work/patch/`

### Rollback Method

1. Restore files from `SITE-002-STABLE-M8.3-BEFORE-M9-20260615-0159/files/` (or pre-deploy backups under `m9-phase1-tables-work/backups/pre-m9-phase1-*`).
2. Delete new M9 files on server: `filter_profile_resolver.php`, `filter_profiles/*`.
3. Clear `system/storage/cache/template/*` and `cache.category.attributes.*`.
4. Verify QA pattern from stable baseline report.

---

## Architecture

```
PLP category_id
       │
       ▼
FilterProfileResolver::resolveForCategory()
       │  (301 or descendant → load 301_stoly.php)
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
filterssidebar.twig — profile layout:
  Цена → Наличие → L/W/H → PRIMARY attrs → «Дополнительные параметры»
```

**Future-ready:** resolver registers branch roots `[301]`; new profiles add files `80.php`, `322.php`, `207.php` and extend `$registered_branch_roots` — no rewrite of controller/template contract.

**Not implemented (by design):** M10 dynamic visibility · ROAD-004 subcategory overrides · root profile 79 · admin UI · deprecation of `AttributeFilterVisibility` on non-profile categories.

---

## Files Modified

### Deployed to TEST (6 files)

| Remote path | SHA256 (deployed) |
| --- | --- |
| `system/library/zpm/filter_profile_resolver.php` | `178a81aa…` |
| `system/library/zpm/filter_profiles/global_hidden.php` | `63d146bc…` |
| `system/library/zpm/filter_profiles/301_stoly.php` | `27b89d42…` |
| `catalog/model/catalog/product.php` | `4dea6237…` |
| `catalog/controller/product/category.php` | `20b71084…` |
| `catalog/view/theme/default/template/sections/filterssidebar.twig` | `bcf9d1e9…` |

### Repo artifacts (local)

| Path | Role |
| --- | --- |
| `m9-phase1-tables-work/patch/` | Source patches |
| `m9-phase1-tables-work/m9-phase1-deploy.py` | TEST FTP deploy |
| `m9-phase1-tables-work/m9-phase1-qa.py` | Storefront QA |
| `qa/m9-phase1/m9-phase1-qa-result.json` | QA JSON |

---

## Visible Attributes

See **Safety Check → Attributes Visible**. QA confirmed **10/10** PRIMARY markers on Столы PLP (both SEO URL and `path=301`).

---

## Secondary Attributes

See **Safety Check → Attributes Secondary**. QA confirmed section title **«Дополнительные параметры»** present and collapsed by default; inner groups: Конструкция, Материал полки, Ножки, Регулируемость опоры (+ Усиление, bort detail attrs when filled).

---

## Hidden Attributes

See **Safety Check → Attributes Hidden**. QA **hidden_hits=[]** on Столы PLP — sink cluster, packaging, SERVICE, TECHNICAL markers absent from filter sidebar.

---

## QA Results

**Summary:** 5 pass · 0 fail · 0 unknown  
**Full JSON:** `projects/ocpilot/sites/site-002/qa/m9-phase1/m9-phase1-qa-result.json`

| ID | URL | Result |
| --- | --- | --- |
| QA-01 | `/katalog/nejtralnoe-oborudovanie/stoly/` | **PASS** — primary 10/10, secondary section, no hidden hits |
| QA-02 | `/index.php?route=product/category&path=301` | **PASS** — same |
| QA-03 | `/katalog/nejtralnoe-oborudovanie` | **PASS** — HTTP 200 |
| QA-04 | `path=80` Моечные ванны | **PASS** — no regression (legacy pool) |
| QA-05 | Reference PDP SPKB-18/7-ВЛ5 | **PASS** — HTTP 200, no PHP errors |

PHP warnings/notices: **none detected** on checked URLs.

---

## Rollback Procedure

### Fast rollback (M8.3 stable)

1. Upload baseline files from `backups/stable-baselines/SITE-002-STABLE-M8.3-BEFORE-M9-20260615-0159/files/` for the 2 modified baseline files + remove 3 new M9 library files.
2. Flush Twig + attribute caches (see stable baseline report §Rollback Instruction).
3. Re-run Wave 2 QA pattern (`m8.3-wave2-qa.py`).

### Pre-M9 deploy snapshot (this task)

Pre-deploy copies: `m9-phase1-tables-work/backups/pre-m9-phase1-*` (product.php, category.php, filterssidebar.twig).

---

## M9 Phase 2 Readiness

| Item | Status |
| --- | --- |
| Profile resolver + schema | **Ready** — extend with profiles 80, 322, 207 |
| Root profile 79 (`hidden_global` absorption) | **Pending** — global list exists but not wired as root inherit |
| Deprecate `AttributeFilterVisibility` duplicate | **Pending** — kept as safety net for non-profile PLPs |
| Branch QA matrix (80, 322, 207) | **Not started** — Phase 2 scope |
| Subcategory overrides (ROAD-004) | **Not started** — Phase 3 |
| M10 dynamic visibility hooks | **Not started** |

**Recommendation:** operator sign-off on Столы TEST behaviour, then Phase 2 slice = profile **80** Моечные ванны (validates cross-family separation).

---

## UNKNOWN / SECURITY

| Signal | Detail |
| --- | --- |
| **UNKNOWN** | Attribute cache files on host were empty at deploy flush (0 cleared) — may indicate no prior cache or different cache path |
| **SECURITY** | FTP credentials in deploy scripts match prior M8.3 operator pattern — not stored in this report |
| **NOTE** | `AttributeFilterVisibility` retained; global hidden duplicated in profile layer for 301 branch only |

**Phase 2:** NOT started (per task charter).
