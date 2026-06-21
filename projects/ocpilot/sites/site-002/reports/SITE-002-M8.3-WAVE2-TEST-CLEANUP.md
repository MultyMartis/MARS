# REPORT — BZPM M8.3 Wave 2 Packaging & Service Cleanup

**Program:** BZPM Product Roadmap · ROAD-002  
**Environment:** https://zpm.new-site.space/ (TEST only)  
**Authority:** `BZPM-M8.2-CLEANUP-SPECIFICATION-v1.md` · `BZPM-M8.1-ATTRIBUTE-INVENTORY-v1.md` · Wave 1 Report  
**Execution UTC:** 2026-06-15  
**Git:** no commit · no push · no production deploy

---

## Pre-flight

| Check | Result |
| --- | --- |
| Git status | Branch `mars/post-cycle8-live-tests`; unrelated modified files elsewhere; SITE-002 Wave 2 work **untracked** |
| Scope | TEST storefront filter layer only |
| Wave 1 gate | TEST attrs cleared; product 3071 inactive |
| Production | Not touched |

### SITE-002 / BZPM files (this task)

**Created (untracked):**

- `projects/ocpilot/sites/site-002/m8.3-wave2-cleanup-work/` — audit, deploy, QA, safety check, patch, backups
- `projects/ocpilot/sites/site-002/qa/m8.3-wave2/m8.3-wave2-qa-result.json`
- `projects/ocpilot/sites/site-002/reports/SITE-002-M8.3-WAVE2-TEST-CLEANUP.md` *(this file)*

**Deployed to TEST (FTP):**

- `system/library/zpm/attribute_filter_visibility.php` *(new)*
- `catalog/model/catalog/product.php` *(patched `getAttributesByCategory()`)*

---

## TASK 1 — Wave 2 Attribute List

Source: M8.1 baseline (`.recovery-temp/bzpm-m8.1-audit.json`, audit UTC 2026-06-14). SKU = active products with non-empty value.

### PACKAGING

| ID | Название | SKU Count | Текущее использование (pre-Wave 2) |
| ---: | --- | ---: | --- |
| 44 | Длина в упаковке (мм) | 531 | В фильтре PLP (dynamic sidebar) |
| 45 | Ширина в упаковке (мм) | 531 | В фильтре PLP |
| 46 | Высота в упаковке (мм) | 531 | В фильтре PLP |
| 52 | Упаковка (Длина, мм) | 29 | В фильтре PLP (legacy import plane) |
| 53 | Упаковка (Ширина, мм) | 29 | В фильтре PLP |
| 54 | Упаковка (Высота, мм) | 29 | В фильтре PLP |
| 56 | Упаковка (Объем, м. куб.) | 535 | В фильтре PLP |
| 57 | Вес (нетто, кг) | 28 | В фильтре PLP |

### SERVICE

| ID | Название | SKU Count | Текущее использование (pre-Wave 2) |
| ---: | --- | ---: | --- |
| 43 | Дополнительные сведения | 974 | В фильтре PLP — highest noise on Столы (419 branch fill) |
| 48 | Комплект поставки | 111 | В фильтре PLP |
| 58 | Комплект отгрузки | 47 | В фильтре PLP |

### TECHNICAL (Wave 2 listed — **not hidden in this deploy**)

| ID | Название | SKU Count | Текущее использование |
| ---: | --- | ---: | --- |
| 12 | Габариты нетто (мм) | 54 | В фильтре PLP — deferred per task scope |
| 27 | Обвязка | 7 | В фильтре PLP |
| 34 | Страна производства | 55 | В фильтре PLP |
| 36 | Обвязка | 17 | В фильтре PLP |
| 42 | Стандарт | 367 | В фильтре PLP |

---

## Safety Check

Full document: `m8.3-wave2-cleanup-work/M8.3-WAVE2-SAFETY-CHECK.md`

| Section | Summary |
| --- | --- |
| Attributes To Hide | 11 IDs — PACKAGING 44–46, 52–54, 56–57 + SERVICE 43, 48, 58 |
| Attributes To Keep | All COMMERCIAL + REVIEW + physical dims |
| Attributes To Review | TECHNICAL 12/27/34/36/42 (next wave); SERVICE 43 junk audit |
| Impacted Categories | Neutral 79 subtree — Столы, Моечные ванны, Подтоварники, Зонты |
| Rollback Method | Restore pre-deploy `product.php`; delete visibility lib; flush attribute cache |
| Data loss risk | **None** — STORE_ONLY filter exclusion only |

---

## Attributes Hidden

Implemented via `AttributeFilterVisibility::isStoreOnly()` in `getAttributesByCategory()`:

| Class | IDs | Filter |
| --- | --- | --- |
| PACKAGING | 44, 45, 46, 52, 53, 54, 56, 57 | **Removed from sidebar** |
| SERVICE | 43, 48, 58 | **Removed from sidebar** |

**DB:** all `oc_product_attribute` rows **preserved**.  
**PDP:** unchanged — packaging/SERVICE may still appear in specifications block.  
**Import / 1C:** not touched.

---

## Attributes Preserved

- All COMMERCIAL filter attrs (Конструкция, Тип опоры, Материал столешницы, Макс. нагрузка, …)
- All REVIEW attrs (19, 24, 30, 50, 110, 113, 114)
- TECHNICAL still visible in filter (12, 27, 34, 36, 42) — out of Wave 2 impl scope
- `oc_product` length / width / height / weight filters
- Price, availability, subcategory filters

---

## Filter Impact

**Before (M8.1 / post-Wave 1):** Столы PLP exposed up to **6 packaging attrs + SERVICE 43** in top filter noise.

**After Wave 2:** PLP sidebar on tested categories shows **commercial attrs only** for packaging/SERVICE plane; filter panel materially cleaner.

**Mechanism:** Code-layer STORE_ONLY — not M9 profiles, not DB changes. Interim bridge until M9 Filter Profile System.

---

## QA Results

| Check | URL | Result |
| --- | --- | --- |
| QA-01 | `/katalog/nejtralnoe-oborudovanie` | **PASS** — no packaging/SERVICE in page filter markers |
| QA-02 | PLP Столы (`path=301`) | **PASS** — packaging_hits=[], service_hits=[], commercial present |
| QA-03 | PLP Моечные ванны (`path=80`) | **PASS** |
| QA-04 | PLP Подтоварники (`path=322`) | **PASS** |
| QA-05 | PLP Зонты (`path=207`) | **PASS** |
| QA-06 | PDP SPKB-18/7-ВЛ5 | **PASS** — HTTP 200, no PHP errors, specs block present |
| PHP errors | All PLP + PDP | **None detected** |

Artifact: `qa/m8.3-wave2/m8.3-wave2-qa-result.json`

---

## Rollback Procedure

1. FTP restore `backups/pre-m8.3-wave2-catalog__model__catalog__product.php` → `catalog/model/catalog/product.php`
2. FTP delete `system/library/zpm/attribute_filter_visibility.php`
3. Run cache flush pattern from Wave 1 (`m8.3-wave1-cache-clear.py` or delete `cache.category.attributes.*`)
4. Re-QA Столы PLP — packaging attrs should reappear

Deploy manifest: `m8.3-wave2-cleanup-work/backups/m8.3-wave2-deploy-20260614-184547.json`

---

## Remaining REVIEW Attributes

Unchanged — still in filter where filled (M9 operator decision):

| ID | Name | SKU (M8.1) |
| ---: | --- | ---: |
| 19 | Количество уровней направляющих | 3 |
| 24 | Назначение секции | 4 |
| 30 | Размер секции | 3 |
| 50 | Тип крепления | 1 |
| 110 | Тип покрытия | 1 |
| 113 | Шаг регулировки полки (мм) | 1 |
| 114 | Количество полок (шт) | 1 |

---

## M9 Readiness Status

| Criterion | Status |
| --- | --- |
| Wave 1 TEST cleanup | **Done** |
| Wave 2 packaging/SERVICE filter hide | **Done (TEST)** |
| TECHNICAL filter noise (12, 27, 34, 36, 42) | **Remaining** — M8.2 step 2.4 or M9 |
| Dead attr DELETE (Wave 3) | **Not started** |
| M9 Filter Profile System deploy | **Not started** — design may proceed in parallel |

**Assessment:** Filter is **significantly cleaner** after Wave 2 on TEST. M9 implementation can proceed after operator confirms TEST QA; TECHNICAL hide and Wave 3 dead-def cleanup remain optional pre-M9 hygiene.

---

## Deploy Status

| Step | Status |
| --- | --- |
| Live capture `product.php` | Done |
| Patch + visibility library | Done |
| FTP deploy TEST | **Done** (2 files) |
| Pre-deploy backup | `pre-m8.3-wave2-catalog__model__catalog__product.php` |
| Attribute cache flush | 0 files found (cache empty or alternate path) |
| DB changes | **None** |
| Production | **Not deployed** |

---

## Git status

No commit. No push. Wave 2 work directory untracked under `projects/ocpilot/sites/site-002/`.

---

## UNKNOWN / SECURITY RISK

- **UNKNOWN:** Live post-Wave-2 SKU counts — M8.1 baseline used; PMA complex subqueries returned empty in this session.
- **UNKNOWN:** Whether TECHNICAL attrs 12/42 still visible on Столы is acceptable until M9 — expected per scoped Wave 2.
- **SECURITY RISK:** FTP/DB credentials used from existing OCPilot patterns — not written to committed artifacts; deploy scripts stay local/untracked.

---

*M8.3 Wave 2 complete on TEST. Stopped per instruction — no commit, no push, no production.*
