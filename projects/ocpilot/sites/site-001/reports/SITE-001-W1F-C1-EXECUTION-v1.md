# REPORT — SITE-001 W1F-C1 Execution

**Type:** Supervised W1F-C1 execution report — YML feeds + `robots.txt` remediation  
**Date:** 2026-06-08  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Authorization context:** W1F remediation wave C per [SITE-001-W1F-LEGACY-SWEEP-v1.md](SITE-001-W1F-LEGACY-SWEEP-v1.md) · [SITE-001-W1-WRITE-CHARTER-v1.md](SITE-001-W1-WRITE-CHARTER-v1.md)  
**Prior waves:** W1A **PASS** · W1B **PASS** · W1C **PASS** · W1D **PASS WITH NOTES**

**Binding inputs:**

| Document | Role |
|----------|------|
| [SITE-001-W1F-LEGACY-SWEEP-v1.md](SITE-001-W1F-LEGACY-SWEEP-v1.md) | Pre-execution legacy inventory — YML + robots flagged CRITICAL/HIGH |
| [SITE-001-W1D-EXECUTION-v1.md](SITE-001-W1D-EXECUTION-v1.md) | Prior grep artefact; robots deferred to W1F-C |
| [SITE-001-W1C-EXECUTION-v1.md](SITE-001-W1C-EXECUTION-v1.md) | Controller meta pattern; geographic exception policy |
| [SITE-001-W1-WRITE-CHARTER-v1.md](SITE-001-W1-WRITE-CHARTER-v1.md) | TEST-only write authorization |
| [SITE-001-W1-ROLLBACK-PLAN-v1.md](SITE-001-W1-ROLLBACK-PLAN-v1.md) | T1 wave rollback reference |

**Explicit exclusions (honored):** SMTP · `config_email` · `config_mail_smtp_username` · production domains · legal pages · product templates · admin UI · `backup_yml/` copies.

**Production:** **NOT TOUCHED**

**Evidence artefact (local, not in git):** `.recovery-temp/site-001-w1f-c1-result.json` · `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\w1f-c1-pre-replace-2026-06-08\`

---

## Executive summary

W1F-C1 scoped remediation **complete** on TEST. Active YML generators (`yml.php`, `ymlnew.php`) and `robots.txt` updated; static export files regenerated. Post-change verification shows **zero** legacy brand/domain hits in shop-level YML metadata and `robots.txt` directives.

**Verdict:** **PASS WITH NOTES** — see §9.

---

## Authorization confirmation

| Gate | Status | Notes |
|------|--------|-------|
| Environment = TEST only | **PASS** | `https://sibcar.new-site.space/` confirmed |
| Scope = YML + robots only | **PASS** | 3 files modified; SMTP/admin/legal untouched |
| Pre-W1 backup (C-08) | **PASS** | Operator-confirmed 2026-06-08 (Beget) |
| Wave-specific backup | **PASS** | 3 files backed up before edit (§2) |
| Write approver | **PASS** | **Андрей** per [project-access-brief.md](../project-access-brief.md) |

---

## 1. Discovery

Pre-modification inventory of all YML/robots surfaces.

### 1.1 File inventory

| File path | Role | Source of values | Current output (pre-change) |
|-----------|------|------------------|----------------------------|
| `catalog/controller/product/yml.php` | Used-stock YML generator | Hardcoded shop block lines 55–57 | `<name>АЦ «Хмельницкий»</name>` · `<company>ООО «АЦ Хмельницкий»</company>` · `<url>https://ац-хмельницкий.рф/</url>` |
| `catalog/controller/product/ymlnew.php` | New-stock YML generator | Hardcoded shop block lines 55–57 | Same legacy shop block as `yml.php` |
| `data/yandex-bu.xml` | Static export (used) | Written by `yml.php` on route hit | Mirrors controller legacy shop block |
| `data/yandex.xml` | Static export (new) | Written by `ymlnew.php` on route hit | Mirrors controller legacy shop block |
| `catalog/controller/product/backup_yml/yml.php` | Inactive backup copy | Hardcoded strings | Same legacy shop block — **not in W1F-C1 scope** |
| `catalog/controller/product/backup_yml/ymlnew.php` | Inactive backup copy | Hardcoded strings | Same legacy shop block — **not in W1F-C1 scope** |
| `robots.txt` | SEO crawler directives | Static file at web root | `Host: xn----7sbqmagfghm8fkh5f.xn--p1ai` · `Sitemap: https://xn----7sbqmagfghm8fkh5f.xn--p1ai/index.php?route=extension/feed/google_sitemap` |

**Per-offer URLs in YML:** Dynamic — built from OpenCart `config_url` / product SEO paths; pre-change already used **TEST hostname** (`https://sibcar.new-site.space/...`). Only shop-level `<url>` was legacy.

### 1.2 Sitemap path discovery (TEST)

| Path | HTTP | Content-Type | Notes |
|------|------|--------------|-------|
| `/sitemap.xml` | **200** | `application/xml` | **Active** sitemap on TEST |
| `/index.php?route=extension/feed/google_sitemap` | **200** | `application/xml` | OC extension route — also valid |
| `/sitemap_index.xml` | 404 | — | Not present |

**Decision:** Legacy `robots.txt` pointed to off-TEST `google_sitemap` route on punycode production host. TEST has live `/sitemap.xml`. Replacement uses TEST placeholder `https://NAME.ru/sitemap.xml` per URL policy — **not** production domain.

### 1.3 Live HTTP pre-change verification

| Surface | URL | Legacy in shop block |
|---------|-----|----------------------|
| Used YML export | `/data/yandex-bu.xml` | **YES** — name / company / url |
| New YML export | `/data/yandex.xml` | **YES** — name / company / url |
| YML generator route (used) | `/index.php?route=product/yml` | Route returns minimal response; static file is authoritative export |
| YML generator route (new) | `/index.php?route=product/ymlnew` | Same |
| robots.txt | `/robots.txt` | **YES** — Host + Sitemap legacy punycode |

---

## 2. Backup

**Backup location:** `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\w1f-c1-pre-replace-2026-06-08\`  
**Manifest:** `BACKUP-MANIFEST.json`

| # | Original path | Timestamp (UTC) | Size (bytes) | SHA-256 prefix | Backup file |
|---|---------------|-----------------|--------------|----------------|-------------|
| 1 | `catalog/controller/product/yml.php` | 2026-06-08T14:16:29Z | 8 358 | `8ce81438237c0c04` | `catalog__controller__product__yml.php` |
| 2 | `catalog/controller/product/ymlnew.php` | 2026-06-08T14:16:31Z | 8 912 | `4cb8fdb59b3c0bb6` | `catalog__controller__product__ymlnew.php` |
| 3 | `robots.txt` | 2026-06-08T14:16:33Z | 5 331 | `b50784a4181b63ac` | `robots.txt` |

**Backup status:** **COMPLETE** — no overwrite before backup.

---

## 3. Files modified

| # | Remote path | Method |
|---|-------------|--------|
| 1 | `catalog/controller/product/yml.php` | FTP string replacement + upload |
| 2 | `catalog/controller/product/ymlnew.php` | FTP string replacement + upload |
| 3 | `robots.txt` | FTP string replacement + upload |

**Not modified (per scope):**

| Path | Reason |
|------|--------|
| `catalog/controller/product/backup_yml/*` | Inactive copies — deferred W1F-E |
| `data/yandex*.xml` | Regenerated via generator routes post-controller edit |
| Admin settings / SMTP keys | Explicit exclusion |
| Product templates / legal pages | Explicit exclusion |

---

## 4. Exact replacements

### 4.1 YML controllers (`yml.php`, `ymlnew.php`)

| File | From | To | Count |
|------|------|-----|-------|
| `yml.php` / `ymlnew.php` | `АЦ «Хмельницкий»` | `СИБКАР` | 1 each |
| `yml.php` / `ymlnew.php` | `ООО «АЦ Хмельницкий»` | `ООО «СибКар»` | 1 each |
| `yml.php` / `ymlnew.php` | `https://ац-хмельницкий.рф/` | `https://NAME.ru/` | 1 each |

**Note:** Controllers did not contain `Автоцентр Хмельницкий` or punycode URL variants in shop block — only the three strings above.

### 4.2 `robots.txt`

| From | To | Count |
|------|-----|-------|
| `Host: xn----7sbqmagfghm8fkh5f.xn--p1ai` | `Host: NAME.ru` | 1 |
| `Sitemap: https://xn----7sbqmagfghm8fkh5f.xn--p1ai/index.php?route=extension/feed/google_sitemap` | `Sitemap: https://NAME.ru/sitemap.xml` | 1 |

**URL policy:** `NAME.ru` is a **TEST placeholder** — not a production domain. Documented for operator replacement before go-live.

### 4.3 YML regeneration

| Route | HTTP | Bytes | Effect |
|-------|------|-------|--------|
| `/index.php?route=product/yml` | 200 | 125 | Rewrote `data/yandex-bu.xml` |
| `/index.php?route=product/ymlnew` | 200 | 119 | Rewrote `data/yandex.xml` |

---

## 5. Cache operations

| Action | Method | Result |
|--------|--------|--------|
| System cache | oc3x_storage_cleaner `clearcache` key=system | **OK** |
| Modification cache | oc3x_storage_cleaner `clearcache` key=modification | **OK** |
| Modification refresh | `marketplace/modification/refresh` | **OK** — HTTP 200 |

**Not touched:** SMTP settings · mail config · image cache (not required for this wave).

---

## 6. Verification

### 6.1 Post-audit table

| Surface | Before | After | Result |
|---------|--------|-------|--------|
| YML `<name>` (shop) | `АЦ «Хмельницкий»` | `СИБКАР` | **PASS** |
| YML `<company>` | `ООО «АЦ Хмельницкий»` | `ООО «СибКар»` | **PASS** |
| YML `<url>` (shop) | `https://ац-хмельницкий.рф/` | `https://NAME.ru/` | **PASS** |
| `data/yandex-bu.xml` shop block | Legacy (all three fields) | СИБКАР / ООО «СибКар» / NAME.ru | **PASS** |
| `data/yandex.xml` shop block | Legacy (all three fields) | СИБКАР / ООО «СибКар» / NAME.ru | **PASS** |
| `robots.txt` Host | `xn----7sbqmagfghm8fkh5f.xn--p1ai` | `NAME.ru` | **PASS** |
| `robots.txt` Sitemap | Legacy punycode `google_sitemap` URL | `https://NAME.ru/sitemap.xml` | **PASS** |
| Legacy grep in YML exports | Hits: АЦ / ООО / punycode / Cyrillic domain | **0 hits** | **PASS** |
| Legacy grep in `robots.txt` | `xn----7sbqmagfghm8fkh5f` present | **0 hits** | **PASS** |
| Per-offer YML URLs | `https://sibcar.new-site.space/...` | Unchanged (TEST hostname) | **PASS** — expected |
| SMTP `config_mail_smtp_username` | `send@ац-хмельницкий.рф` *(W1A hold)* | Unchanged | **PASS** — exclusion honored |

### 6.2 Live probe summary

| Check | URL | Result |
|-------|-----|--------|
| robots Host | `https://sibcar.new-site.space/robots.txt` | `Host: NAME.ru` |
| robots Sitemap | same | `Sitemap: https://NAME.ru/sitemap.xml` |
| YML used export | `/data/yandex-bu.xml` | shop block clean; no legacy terms |
| YML new export | `/data/yandex.xml` | shop block clean; no legacy terms |

**Forbidden strings absent in generated feeds:** `АЦ Хмельницкий` · `Автоцентр Хмельницкий` · `ООО «АЦ Хмельницкий»` · `xn----7sbqmagfghm8fkh5f`

---

## 7. Remaining Legacy Inventory

*Inventory only — not fixed in W1F-C1.*

| Surface | Finding | Severity | Recommended wave |
|---------|---------|----------|------------------|
| `catalog/controller/product/backup_yml/yml.php` | Legacy shop block (inactive copy) | LOW | **W1F-E** |
| `catalog/controller/product/backup_yml/ymlnew.php` | Legacy shop block (inactive copy) | LOW | **W1F-E** |
| `catalog/controller/product/product.php` | `АЦ Хмельницкий` in SEO title/description | HIGH | **W1F-A** |
| `catalog/controller/product/category.php` | `АЦ Хмельницкий` in SEO title/description | HIGH | **W1F-A** |
| `catalog/view/theme/auto/template/product/productnew.twig` | `АЦ Хмельницкий` in visible copy | HIGH | **W1F-A** |
| `admin/view/template/catalog/product_form.twig` | JS SEO title template `\| АЦ Хмельницкий` | MEDIUM | **W1F-E** |
| `catalog/controller/checkout/anketa.php` | `send@xn----7sbqmagfghm8fkh5f.xn--p1ai` | CRITICAL | **W1F-D** |
| `config_mail_smtp_username` | `send@ац-хмельницкий.рф` *(W1A unchanged)* | CRITICAL | **W1F-D** |
| `/privacy-policy` | Legacy brand + `ац-хмельницкий.рф` in body | HIGH | **W1F-B** |
| `/user-agreement` | Legacy brand + `ац-хмельницкий.рф` in body | HIGH | **W1F-B** |
| `/autocredit` | Legacy brand + domain refs | HIGH | **W1F-B** |
| `/tradein` | Legacy brand refs | HIGH | **W1F-B** |

**Geographic exception (unchanged):** `ул. Богдана Хмельницкого` — not brand; excluded.

---

## 8. Risks

| ID | Risk | Severity | Status |
|----|------|----------|--------|
| R-W1F-C1-01 | `NAME.ru` is placeholder — aggregators/crawlers will not resolve until production DNS | **Medium** | **Accepted** — TEST policy; operator must substitute real domain pre-go-live |
| R-W1F-C1-02 | `backup_yml/` copies still contain legacy strings | **Low** | **Open** — W1F-E; inactive routes today |
| R-W1F-C1-03 | SMTP identity still legacy (`config_mail_smtp_username`, `anketa.php`) | **CRITICAL** | **Open** — W1F-D; explicitly out of scope |
| R-W1F-C1-04 | Product/legal SEO surfaces still show legacy brand at scale | **HIGH** | **Open** — W1F-A / W1F-B |
| R-W1F-C1-05 | YML generator HTTP routes return minimal body; reliance on static `/data/*.xml` for verification | **Low** | **Accepted** — static files confirmed post-regeneration |

---

## 9. Rollback impact

| Tier | W1F-C1 rollback action | Impact |
|------|------------------------|--------|
| **T1** | Restore 3 files from `w1f-c1-pre-replace-2026-06-08` via FTP; re-hit YML routes to regenerate XML | YML shop metadata + robots revert to legacy; W1A/B/C/D changes **unaffected** |
| **T2** | Full TEST restore from pre-W1 Beget backup | Reverts all W1 changes |

**Rollback required:** **NO**

---

## 10. Verdict

### **PASS WITH NOTES**

W1F-C1 scoped objectives **met** on TEST:

- Active YML generators remediated (2 controllers).
- Static exports `data/yandex-bu.xml` and `data/yandex.xml` regenerated with СИБКАР branding.
- `robots.txt` Host/Sitemap updated to TEST placeholder `NAME.ru`.
- Modification + system cache cleared; modifications refreshed.
- SMTP, mail settings, legal pages, product templates, admin UI **untouched**.
- Zero legacy brand/domain hits in post-change YML shop block and `robots.txt`.

**Notes:**

1. `NAME.ru` and `https://NAME.ru/sitemap.xml` are **TEST placeholders** — replace with attested production domain before launch.
2. Sitemap path chosen as `/sitemap.xml` because TEST returns HTTP 200 at that path (legacy robots used OC `google_sitemap` route on production punycode host).
3. `backup_yml/` inactive copies retain legacy strings — cleanup deferred to W1F-E.
4. Per-offer product URLs in YML remain on TEST hostname — correct for current environment.

**Production:** **NOT TOUCHED**

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-08 | **EXECUTED** — W1F-C1 YML + robots remediation on TEST; 3 files; backup + cache clear + YML regeneration |

*SITE-001 W1F-C1 Execution v1 — TEST only; no commit; no push.*
