# REPORT — BZPM M8.3 Wave 1 TEST Cleanup

**Program:** BZPM Product Roadmap · ROAD-002  
**Environment:** https://zpm.new-site.space/ (TEST only)  
**Authority:** `BZPM-M8.2-CLEANUP-SPECIFICATION-v1.md` · `BZPM-M8.1-ATTRIBUTE-INVENTORY-v1.md`  
**Execution UTC:** 2026-06-15  
**Git:** no commit · no push · no production deploy

---

## Pre-flight

| Check | Result |
| --- | --- |
| Git status | Branch `mars/post-cycle8-live-tests`; many unrelated modified files; SITE-002 work dirs untracked |
| Scope | SITE-002 + BZPM roadmap docs only |
| Production | Not touched |

---

## TASK 1 — Product 3071

**Live state (pre-cleanup):**

| Field | Value |
| --- | --- |
| product_id | 3071 |
| model | СПБ-С-10/6 |
| status | **1** (active) |
| name | Стол производственный СПБ-С-10/6 (1000х600х850) … (содержит «ТЕ…» / TEST в имени) |
| oc_product L/W/H | 1.0 / 1.0 / 1.0 м |
| weight | 4.0 кг |
| category | **306** — Столы СТАНДАРТ-600 с полкой-решеткой |
| storefront PLP | Участвовал в фильтрах Neutral / Столы (TEST attrs в sidebar) |

**M8.2 decision:** HIDE → cleanup → KEEP (или DELETE позже если подтверждён мусор)

**Реализация Wave 1:** **HIDE** — `status=0`. Товар и категорийные связи сохранены в БД. PDP → 404 на TEST (ожидаемо для inactive).

**Миграция L/W/H (105–107):** поля `oc_product` уже заполнены; M8.2 допускает migrate «если empty» — **overwrite не выполнялся** (строго по спецификации).

---

## TASK 2 — TEST Attribute Definitions

| ID | Name | Active products (pre) | In filter (pre) | Safe delete? | Wave 1 action |
| ---: | --- | ---: | --- | --- | --- |
| 16 | Параметр | 0 | No | **Yes** | **DELETE** |
| 105 | шир ТЕСТ | 1 (3071) | Yes | **Yes** (after value strip) | **DELETE** |
| 106 | выс ТЕСТ | 1 | Yes | **Yes** | **DELETE** |
| 107 | дл ТЕСТ | 1 | Yes | **Yes** | **DELETE** |
| 108 | марка стали ТЕСТ | 1 | Yes | **Yes** (единственный SKU hidden) | **DELETE** |
| 109 | толщина столешницы ТЕСТ | 1 | Yes | **Yes** | **DELETE** |
| 111 | толщина материала ног ТЕСТ | 1 | Yes | **Yes** | **DELETE** |

**Post-cleanup DB:** `oc_attribute` count for IDs 16,105–111 = **0**. TEST defs в фильтре не остались.

**Сохранён (вне TEST scope):** attr **110** «Тип покрытия» — COMMERCIAL, 1 value на inactive 3071.

---

## TASK 3 — TEST Values

| Product | Attr | Value | M8.2 | Wave 1 |
| --- | ---: | --- | --- | --- |
| 3071 | 105 | 0,6 | DELETE after migrate | **DELETE** (migrate L/W/H skipped — fields filled) |
| 3071 | 106 | 0,85 | DELETE after migrate | **DELETE** |
| 3071 | 107 | 1 | DELETE after migrate | **DELETE** |
| 3071 | 108 | 430 | DELETE after migrate / REVIEW | **DELETE** (backup in pre-cleanup JSON) |
| 3071 | 109 | 0,7 | DELETE after migrate / REVIEW | **DELETE** (backup) |
| 3071 | 111 | 1,5 | DELETE after migrate / REVIEW | **DELETE** (backup) |

**False positives (KEEP per M8.2):** категории 189/193/194 (тесто-*), option values, manufacturers, native `oc_filter` (empty).

**Примечание:** значение `0,6` встречается у packaging attr **56** на других SKU — не TEST contamination.

---

## TASK 4 — Migration Plan (108–111, no transfer executed)

| Attr ID | TEST field | Current value (3071) | Target field | Status |
| ---: | --- | --- | --- | --- |
| 108 | марка стали ТЕСТ | 430 | **REVIEW** — нет канонического commercial attr; кандидаты: STORE_ONLY note (43) или будущий technical attr | Plan only |
| 109 | толщина столешницы ТЕСТ | 0,7 | **REVIEW** — нет twin; attr 22 = материал, не толщина | Plan only |
| 110 | Тип покрытия | оцинкованный | **KEEP** attr 110 (COMMERCIAL, не TEST) | No migration |
| 111 | толщина материала ног ТЕСТ | 1,5 | **REVIEW** — нет канонического attr | Plan only |

Значения 108/109/111 сохранены в backup-файле до DELETE.

---

## Safety Check

### Objects To Modify

- `oc_product` product_id **3071** — `status` 1 → 0

### Objects To Delete

- `oc_product_attribute` rows: 3071 × (105, 106, 107, 108, 109, 111) — **6 rows**
- `oc_attribute_description` + `oc_attribute`: IDs **16, 105–109, 111** — **7 defs**

### Objects To Keep

- Product 3071 record (inactive), categories, commercial attrs on 3071 (**110** и прочие non-TEST)
- Packaging / Commercial / Service attrs (вне scope)
- Categories 189/193/194 (false positives)
- Filter profiles, UI, megamenu — не тронуты

### Migration Required

- **105–107:** не требуется (поля `oc_product` уже заполнены)
- **108–111:** план подготовлен; перенос **не выполнялся** (по заданию)

### Rollback Method

1. Restore from `m8.3-wave1-pre-cleanup-20260614-182952.json`:
   - `UPDATE oc_product SET status=1 WHERE product_id=3071`
   - Re-insert `oc_attribute` / `oc_attribute_description` / `oc_product_attribute` from backup
2. Flush OpenCart file cache: `storage/cache/cache.category.attributes.*` (см. cache-flush helper pattern)
3. Beget global backup (operator tier) — вне scope агента

**Risk assessment:** низкий для Wave 1 — единственный активный TEST SKU; backup создан; commercial attr 110 сохранён.

---

## Objects Modified

| Object | Change |
| --- | --- |
| `oc_product` #3071 | `status` → 0 |

## Objects Deleted

| Object | Count |
| --- | ---: |
| TEST `oc_product_attribute` values | 6 |
| TEST `oc_attribute` definitions | 7 (16 + 105–109 + 111) |

## Objects Preserved

- Product 3071 (inactive, with attr 110 «Тип покрытия» = оцинкованный)
- All non-TEST catalog data (609→608 active under Neutral after hide)
- Packaging / Service / Commercial attribute registry (unchanged)

## Migration Decisions

- Dimensional TEST values: no overwrite of `oc_product` (already filled per M8.2 «if empty» rule)
- Steel/thickness TEST values: deleted with backup; migration deferred to operator REVIEW

## Deploy Status

| Step | Status |
| --- | --- |
| DB cleanup (TEST `polygonws_zpm`) | **Done** |
| OpenCart file cache flush (`storage/cache/cache.category.attributes.*`) | **Done** (11 cache files) |
| Twig template cache | Empty / no files |
| FTP code deploy | **Not required** (DB-only Wave 1) |
| One-shot cache helper | Uploaded + self-deleted |
| Production | **Not deployed** |

## QA Results

| Check | URL | Result |
| --- | --- | --- |
| QA-01 | `/katalog` | **PASS** — no TEST markers |
| QA-02 | `/katalog/nejtralnoe-oborudovanie` | **PASS** — no TEST in filter sidebar |
| QA-03 | PLP Столы (path=301) | **PASS** |
| QA-04 | PLP Моечные ванны (path=80) | **PASS** |
| QA-05 | PDP product_id=3071 | **404** — hidden (expected) |
| QA-06 | PDP product_id=1 | 404 — reference SKU not valid (SAFE UNKNOWN) |
| PDP reference | SPKB-18/7-ВЛ5 SEO URL | **200** — storefront OK |

**Post-cache-flush:** stale `category.attributes.*` cache was root cause of PLP TEST markers after DB delete.

## Remaining TEST Contamination

| Item | Status |
| --- | --- |
| TEST attr defs 16, 105–111 | **Cleared** |
| TEST values on active SKUs | **Cleared** |
| Active product with TEST in name | **Cleared** (3071 inactive) |
| «ТЕСТ» in product name on 3071 | **Remains in DB** on inactive SKU — optional rename in Wave 2+ |
| 4 unknown attribute IDs (60 vs 56) | **SAFE UNKNOWN** — unchanged |
| Packaging / SERVICE filter noise | **Out of Wave 1 scope** (M8.3 Wave 2) |

## Risks

| ID | Risk | Mitigation |
| --- | --- | --- |
| R1 | Stale OC file cache after DB delete | Resolved — flush `storage/cache/` |
| R2 | Loss of steel/thickness QA values on 3071 | Backup JSON; product inactive |
| R3 | `oc_product` width/height may not match real dims (1/1 vs 0.6/0.85) | Not changed per M8.2; operator REVIEW if 3071 reactivated |

## Recommended Next Step

1. Operator: confirm product 3071 fate (rename + reactivate vs permanent DELETE).
2. **M8.3 Wave 2** — SERVICE/packaging filter hide (per M8.2, not M9 deploy).
3. Classify 4 missing attribute IDs before Wave 3 dead-def DELETE.

---

## Changed files (agent workspace)

**Created:**

- `projects/ocpilot/sites/site-002/m8.3-wave1-cleanup-work/m8.3-wave1-audit.py`
- `projects/ocpilot/sites/site-002/m8.3-wave1-cleanup-work/m8.3-wave1-cleanup.py`
- `projects/ocpilot/sites/site-002/m8.3-wave1-cleanup-work/m8.3-wave1-cache-clear.py`
- `projects/ocpilot/sites/site-002/m8.3-wave1-cleanup-work/m8.3-wave1-cache-flush.php` (ephemeral on host — self-deleted)
- `projects/ocpilot/sites/site-002/m8.3-wave1-cleanup-work/m8.3-wave1-cache-flush-deploy.py`
- `projects/ocpilot/sites/site-002/m8.3-wave1-cleanup-work/m8.3-wave1-qa.py`
- `projects/ocpilot/sites/site-002/m8.3-wave1-cleanup-work/m8.3-wave1-verify-db.py`
- `projects/ocpilot/sites/site-002/m8.3-wave1-cleanup-work/backups/m8.3-wave1-pre-cleanup-20260614-182952.json`
- `projects/ocpilot/sites/site-002/m8.3-wave1-cleanup-work/m8.3-wave1-cleanup-result-20260614-183001.json`
- `projects/ocpilot/sites/site-002/m8.3-wave1-cleanup-work/m8.3-wave1-audit-result.json`
- `projects/ocpilot/sites/site-002/qa/m8.3-wave1/m8.3-wave1-qa-result.json`
- `projects/ocpilot/sites/site-002/reports/SITE-002-M8.3-WAVE1-TEST-CLEANUP.md` *(this file)*

**Modified:** none in tracked git paths (new untracked work dir only)

## Git status

No commit. No push. SITE-002 `m8.3-wave1-cleanup-work/` — untracked.

## UNKNOWN / SECURITY RISK

- **UNKNOWN:** Exact full product name of 3071 (truncated in PMA export) — substring TEST inferred from M8.1 + search.
- **UNKNOWN:** Whether 3071 should be permanently deleted vs kept inactive.
- **SECURITY RISK:** DB/FTP credentials used from existing OCPilot recovery patterns — not written to report; ephemeral cache-flush PHP self-deleted on host.

---

*M8.3 Wave 1 complete. Stopped per instruction — no commit, no push, no production.*
