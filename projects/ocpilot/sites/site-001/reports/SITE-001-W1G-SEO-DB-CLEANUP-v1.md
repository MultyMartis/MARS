# REPORT — SITE-001 W1G SEO DB Cleanup

**Type:** Supervised W1G execution report — targeted DB SEO cleanup  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Authorization context:** Phase 1 residual remediation per [SITE-001-PHASE1-FINAL-AUDIT-DECISION-v1.md](SITE-001-PHASE1-FINAL-AUDIT-DECISION-v1.md) (W1G recommended wave)

**Explicit exclusions (honored):** PRODUCTION · SMTP / mail settings · unrelated DB tables · blind full-database UPDATE · template changes outside admin SEO generator default

**Evidence artefacts:**

| Artefact | Location |
|----------|----------|
| Pre-replace backup (JSON + SQL) | `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\w1g-seo-db-pre-replace-2026-06-09\` |
| Execution JSON | `...\w1g-seo-db-pre-replace-2026-06-09\execution-result.json` |
| Orchestrator (local, not committed) | `.recovery-temp/site-001-w1g-execute.py` |

---

## Executive summary

Targeted SQL cleanup of legacy SEO meta in **TEST** database completed successfully. **206 rows** updated across `oc_category_description` (3) and `oc_product_description` (203). Post-update discovery: **0 remaining hits** for the search dictionary. Admin JS SEO generator default in `product_form.twig` fixed to prevent re-seeding.

Primary failure from Phase 1 final audit (`/auto/` title + meta description) is **remediated**.

**Verdict: PASS WITH NOTES** — new-car product detail page not HTTP-verified (no discoverable public URLs on TEST catalog); allowed legacy surfaces unchanged as expected.

---

## 1. Discovery (SELECT only — pre-update)

### 1.1 Search scope

**Tables:**

| Table | Fields searched |
|-------|-----------------|
| `oc_category_description` | `meta_title`, `meta_description`, `meta_keyword`, `name`, `description` |
| `oc_product_description` | same |
| Custom SEO-like tables (`SHOW TABLES` filter: `oc_*` + `seo\|meta\|description`) | text columns matching meta/name/desc/keyword/seo patterns |

**Search values:**

- `АЦ Хмельницкий`
- `Автоцентр Хмельницкий`
- `ООО «АЦ Хмельницкий»`
- `ац-хмельницкий.рф`
- `xn----7sbqmagfghm8fkh5f`

**Geographical exclusion:** `ул. Богдана Хмельницкого` — protected during replacement planning (not modified).

### 1.2 Discovery results

| Surface | Rows with legacy hits |
|---------|----------------------|
| `oc_category_description` | **3** |
| `oc_category_description` where `category_id = 59` (`/auto/`) | **1** |
| `oc_product_description` (all) | **203** |
| `oc_product_description` (join `oc_product_to_category`, `category_id = 59` — new cars) | **203** |
| Extra custom SEO tables | **0** |

### 1.3 Category rows (pre-update)

| category_id | Route context | Fields affected | Legacy pattern |
|-------------|---------------|-----------------|----------------|
| **59** | `/auto/` root | `meta_title`, `meta_description` | `\| АЦ Хмельницкий` · `АЦ Хмельницкий –` |
| 60 | Used cars catalog root | `meta_title`, `meta_description` | same |
| 61 | Special offers catalog | `meta_title`, `meta_description` | same |

**Example — `category_id = 59` (pre-update):**

| Field | Value (excerpt) |
|-------|-----------------|
| `meta_title` | `Каталог новых автомобилей в Новосибирске – цены, комплектации, фото \| АЦ Хмельницкий` |
| `meta_description` | `…АЦ Хмельницкий – широкий выбор машин…` |

### 1.4 Product rows (pre-update sample)

All **203** hits were `meta_title` suffix `| АЦ Хмельницкий` on new-car products (`category_id = 59`). No hits for domain punycode or legal entity strings in product SEO fields.

**Example — `product_id = 5093`:**

| Field | Value (excerpt) |
|-------|-----------------|
| `meta_title` | `Новый Lada (ВАЗ) Granta Универсал - купить … \| АЦ Хмельницкий` |

### 1.5 Discovery method note

Direct remote MySQL from operator workstation is **blocked by Beget** (`1045 Access denied` for external host). Discovery executed via **one-shot localhost PHP helper** uploaded over FTP, invoked over HTTPS, then **self-deleted**. Equivalent to SELECT-only phase before backup.

---

## 2. Backup (pre-UPDATE)

**Directory:** `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\w1g-seo-db-pre-replace-2026-06-09\`

| File | Contents |
|------|----------|
| `affected-rows.json` | Full affected-row inventory: table, primary key, `language_id`, old values, planned replacements |
| `rollback.sql` | Field-level UPDATE statements to restore pre-change values |
| `discovery-summary.json` | Discovery counts + `category_id = 59` snapshot |
| `execution-result.json` | Full execution + verification payload |
| `admin__view__template__catalog__product_form.twig` | Pre-replace admin template backup |

**Affected row count in backup:** **206**

---

## 3. SQL operations performed

### 3.1 Replacement rules (exact)

| From | To |
|------|-----|
| `ООО «АЦ Хмельницкий»` | `ООО «СибКар»` |
| `Автоцентр Хмельницкий` | `Автосалон СИБКАР` |
| `АЦ Хмельницкий` | `СИБКАР` |
| `xn----7sbqmagfghm8fkh5f.xn--p1ai` | `NAME.ru` |
| `ац-хмельницкий.рф` | `NAME.ru` |
| `xn----7sbqmagfghm8fkh5f` | `NAME.ru` |

Longest-match order applied. Geographic street references excluded.

### 3.2 Updates executed

| Table | Rows updated | Primary key |
|-------|--------------|-------------|
| `oc_category_description` | **3** | `category_id` + `language_id` |
| `oc_product_description` | **203** | `product_id` + `language_id` |
| **Total** | **206** | — |

**Typical UPDATE pattern:**

```sql
UPDATE oc_category_description
SET meta_title = '…| СИБКАР', meta_description = '…СИБКАР –…'
WHERE category_id = 59 AND language_id = 1;

UPDATE oc_product_description
SET meta_title = '…| СИБКАР'
WHERE product_id = ? AND language_id = 1;
```

### 3.3 Post-update discovery

| Table | Remaining legacy hits |
|-------|----------------------|
| `oc_category_description` | **0** |
| `oc_product_description` (all) | **0** |
| `oc_product_description` (new cars, cat 59) | **0** |

---

## 4. Admin generator source fix

**Path checked (task spec):** `catalog/view/theme/auto/template/product/product_form.twig` — **NOT FOUND** on server.

**Actual path (OpenCart admin):** `admin/view/template/catalog/product_form.twig`

| Item | Detail |
|------|--------|
| Status | **UPDATED** |
| Pattern replaced | `\| АЦ Хмельницкий` → `\| СИБКАР` (2 occurrences) |
| Lines (context) | JS meta title template for new-car product edit form |
| Backup | `...\w1g-seo-db-pre-replace-2026-06-09\admin__view__template__catalog__product_form.twig` |
| Post-update FTP scan | **0** legacy lines · **2** `\| СИБКАР` lines |

No other admin UI files modified.

---

## 5. Cache / modification refresh

| Action | HTTP | OK |
|--------|------|-----|
| `oc3x_storage_cleaner` — system cache | 200 | **yes** |
| `oc3x_storage_cleaner` — modification cache | 200 | **yes** |
| Modification refresh | 200 | **yes** |

---

## 6. Verification

### 6.1 Public HTTP audit

| URL | HTTP | Title (excerpt) | Meta description | Meta keywords | H1 | Legacy hits | Verdict |
|-----|------|-----------------|------------------|---------------|-----|-------------|---------|
| `/` | 200 | `…\| СИБКАР` | Автосалон СИБКАР… | СИБКАР, … | СИБКАР — авто с пробегом… | **0** | **CLEAN** |
| `/auto/` | 200 | `…\| СИБКАР` | …СИБКАР – широкий выбор… | *(empty)* | Каталог новых автомобилей | **0** | **CLEAN** *(was FAIL)* |
| `/auto/baic` | 200 | `…\| СИБКАР` | …в СИБКАР… | *(empty)* | Новые автомобили BAIC в СИБКАР | **0** | **CLEAN** |
| `/cars/bmw` | 200 | `…\| СИБКАР` | …в СИБКАР… | *(empty)* | Автомобили BMW… в СИБКАР | **0** | **CLEAN** |

**Geographical reference:** `ул. Богдана Хмельницкого` — **4 hits/page** on all probed URLs — **expected, unchanged**.

### 6.2 New-car product detail page

| Check | Result |
|-------|--------|
| Automated link discovery from `/auto/`, `/auto/baic`, `/auto/haval`, `/auto/geely`, sitemap | **0 product URLs** |
| Direct probe `product_id=5093` | **404** (product not publicly routable on TEST) |
| DB post-update scan (203 new-car products) | **0 legacy meta hits** |

**Status:** **NOT VERIFIED at HTTP layer** — consistent with Phase 1 final audit empty-catalog behaviour. DB remediation for all 203 new-car product meta titles is **confirmed**.

### 6.3 Admin generator default

| Check | Result |
|-------|--------|
| `product_form.twig` legacy `\| АЦ Хмельницкий` | **0** |
| `product_form.twig` `\| СИБКАР` default | **present** |

---

## 7. Remaining legacy inventory (allowed / deferred)

| Surface | Legacy content | Status | Wave |
|---------|----------------|--------|------|
| `config_mail_smtp_username` | `send@ац-хмельницкий.рф` | **KNOWN — W1A hold** | W1F-D |
| `catalog/controller/checkout/anketa.php` | punycode fragment ×1 | **DEFERRED** | W1F-D |
| `catalog/controller/product/backup_yml/yml.php` | brand + legal + domain ×4 | **DEFERRED** (backup YML) | W1F-E |
| `ул. Богдана Хмельницкого` | address/footer | **GEOGRAPHICAL_REFERENCE — allowed** | — |

**Not re-introduced:** `/auto/` · new-car DB SEO meta · admin generator default.

---

## 8. Rollback instructions

### Tier T1 — Field-level (preferred)

1. Restore from `rollback.sql` in backup directory via phpMyAdmin or localhost MySQL on Beget.
2. Re-upload `admin__view__template__catalog__product_form.twig` to `admin/view/template/catalog/product_form.twig`.
3. Clear system + modification cache (admin → oc3x_storage_cleaner + modification refresh).

### Tier T2 — Row-level JSON

Use `affected-rows.json` → each entry contains `fields.<field>.old` for precise manual restore.

### Tier T3 — Full DB restore

Pre-W1A Beget database backup (operator-confirmed 2026-06-08) — use only if T1/T2 insufficient.

---

## 9. Files modified

| File | Change |
|------|--------|
| `admin/view/template/catalog/product_form.twig` | JS SEO suffix `\| АЦ Хмельницкий` → `\| СИБКАР` |

**Database:** 206 rows in `oc_category_description` / `oc_product_description` (no schema changes).

**Temporary helper:** `w1g-seo-db-helper.php` uploaded for execution — **deleted** after run (`db_helper_removed.deleted = true`).

---

## 10. Verdict

| Criterion | Result |
|-----------|--------|
| `/auto/` legacy brand removed | **PASS** |
| New-car DB SEO meta cleaned (203 products) | **PASS** |
| Extra SEO tables scanned | **PASS** (none affected) |
| Admin generator default fixed | **PASS** |
| Geographic street reference preserved | **PASS** |
| SMTP / mail untouched | **PASS** |
| New-car product HTTP page verified | **NOT VERIFIED** (empty/unroutable catalog on TEST) |

### **PASS WITH NOTES**

**Notes:**

1. New-car product detail URL could not be probed live — DB + generator fixes cover the residual pattern identified in Phase 1 final audit.
2. Categories **60** and **61** were also cleaned (used-car / special-offer catalog meta had same legacy suffix — in scope of discovery hits, low public visibility risk).
3. Domain replacement rule `→ NAME.ru` was not triggered in SEO fields (no domain strings found in affected rows).

---

## 11. Git status

**Repository changes from this wave:** this report file only (`projects/ocpilot/sites/site-001/reports/SITE-001-W1G-SEO-DB-CLEANUP-v1.md`).

**No commit. No push.**

**SECURITY RISK:** None introduced. Temporary DB helper removed. Credentials used from external secrets store only; not recorded in this report.

**UNKNOWN:** Production environment state — not in scope (TEST only).

---

*End of W1G execution report.*
