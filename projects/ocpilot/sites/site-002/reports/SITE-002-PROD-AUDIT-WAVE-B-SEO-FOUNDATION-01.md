# REPORT — SITE-002 Audit Wave B SEO Foundation

**Operation:** `SITE-002-PROD-AUDIT-WAVE-B-SEO-FOUNDATION-01`  
**OCPilot run:** 4.243  
**Date:** 2026-07-10  
**Environment:** https://bzpm.ru/ (Production — controlled sitemap + scoped DB patch)  
**Baseline before:** `SITE-002-STABLE-PROD-CRON-RUN-REPORTS-DURATION-FIX-01`  
**Checkpoint after:** `SITE-002-STABLE-PROD-AUDIT-WAVE-B-SEO-FOUNDATION-01`

---

## 1. Scope

Controlled production SEO foundation cleanup after Run 4.241 Full Tech SEO Audit and Run 4.242 Redirect Hygiene.

| Target | Intent |
|--------|--------|
| **AUDIT-007** | Remove 7 legacy `index.php?route=information/...` URLs from sitemap |
| **AUDIT-004** | Resolve duplicate SEO keywords `compare-products`, `wishlist` |
| **AUDIT-010** | Reclassify duplicate title groups after Run 4.242 |
| **AUDIT-002** | Add canonical `/contact` to sitemap (optional, included) |

**Allowed:** HTTP GET, read-only DB SELECT, scoped DB DELETE after backup, exact sitemap controller FTP upload, rollback bundle, docs.  
**Forbidden:** category/product content edits, `/contact` slug change, `/kontakty` implementation, import/monitor, admin saves, header/footer/Yandex changes.

---

## 2. Pre-flight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume X: label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD | `5a4a5537` |
| Staged changes before task | **none** |
| Foreign WIP | Present — excluded from commit |

---

## 3. Target audit issues

| ID | Before | After |
|----|--------|-------|
| AUDIT-007 | 7 legacy information URLs in sitemap | **fixed** — 0 legacy URLs |
| AUDIT-004 | 2 duplicate keyword groups (`compare-products`, `wishlist`) | **fixed** — redundant rows removed |
| AUDIT-010 | 3 duplicate title groups (homepage/index.php; Lari flat/nested) | **partially resolved** — Run 4.242 closed homepage + Lari pairs; content/meta duplicates deferred |
| AUDIT-002 | `/contact` not in sitemap | **fixed** — `/contact` now emitted |

---

## 4. Before snapshot

| Signal | Value |
|--------|-------|
| Sitemap URLs | **1408** |
| Legacy `index.php?route=information/...` | **7** |
| `/contact` in sitemap | **no** |
| `/kontakty` in sitemap | **no** |
| Flat Lari in sitemap | **0** |
| Nested Lari in sitemap | **7** |
| Public `БЗПМ` (seed URLs) | **0** |

**Exact 7 legacy sitemap URLs:**

1. `information_id=11` → pretty `/guarantee`
2. `information_id=10` → pretty `/dealers`
3. `information_id=13` → (legacy CMS row; migrated route in seo_url set)
4. `information_id=12` → (legacy CMS row; migrated route in seo_url set)
5. `information_id=14` → pretty `/custom-equipment`
6. `information_id=9` → pretty `/payment-methods`
7. `information_id=6` → pretty `/delivery`

Root cause: `google_sitemap.php` called `$this->url->link('information/information', 'information_id=N')` for CMS rows whose SEO URLs were migrated to dedicated `information/*` controllers — `url->link` could not resolve pretty paths.

Evidence: Storage `deployments/SITE-002-PROD-AUDIT-WAVE-B-SEO-FOUNDATION-01/sitemap-before/`, `http-before/`

---

## 5. DB discovery

| Metric | Value |
|--------|-------|
| Active categories | 224 |
| Active products | 1170 |
| Active information pages | 13 |
| Duplicate keywords (global) | 2 (`compare-products`, `wishlist`) |

**compare-products / wishlist duplicates:**

| seo_url_id | query | keyword | Classification |
|------------|-------|---------|----------------|
| 850 | `product/compare` | compare-products | **kept** (owner) |
| 928 | `product/compare` | compare-products | **deleted** (identical redundant) |
| 857 | `account/wishlist` | wishlist | **kept** (owner) |
| 927 | `account/wishlist` | wishlist | **deleted** (identical redundant) |

Both duplicate groups were **identical redundant rows** (same query/keyword/store/lang) — safe scoped DELETE after backup. Service routes remain; `/compare-products` and `/wishlist` are non-indexable technical pages (robots.txt / noindex policy unchanged).

**Contact route:** `information/contact` → keyword `contact` (seo_url_id 846) — eligible for sitemap inclusion via route-based emission.

Evidence: Storage `db-readonly/`

---

## 6. Source authority

| Remote path | Role | Will modify |
|-------------|------|-------------|
| `/public_html/catalog/controller/extension/feed/google_sitemap.php` | Sitemap feed controller | **yes** |
| `seo_url.php` | SEO startup | no (reference) |
| `seo_pro.php` | SEO Pro startup | no (reference) |

Patch strategy: emit all distinct `information/*` routes from `oc_seo_url`; skip migrated legacy `information_id` rows (6, 9, 10, 11, 12, 13, 14); fallback emit remaining `information_id=N` pages that still have active seo_url rows.

---

## 7. Patch plan and rollback

1. **Sitemap controller patch** — route-based information URL emission + migrated-id skip + `/contact` via `information/contact` route.
2. **DB cleanup** — DELETE seo_url_id **928**, **927** after scoped JSON backup.

Rollback:

- Re-upload `source-before/public_html__catalog__controller__extension__feed__google_sitemap.php`
- Run `rollback/db-rollback-plan.sql` to reinsert deleted seo_url rows

Evidence: Storage `patch/`, `rollback/`

---

## 8. Dry-run gates

All gates **G1–G14 PASS**. See Storage `manifests/dry-run-gates.json`.

---

## 9. Controlled mutation

| Action | Result |
|--------|--------|
| FTP upload `google_sitemap.php` | **done** — SHA verified match |
| DB DELETE seo_url 928, 927 | **done** — backup in `db-backup-scoped/` |
| Cache clear | **not required** (dynamic sitemap) |

Upload SHA: `0117315108d8c9829c4b0a9c3263adcbcb283cbebe40dd11eb36c6c5d252178a`

---

## 10. After verification

| Signal | Before | After |
|--------|--------|-------|
| Sitemap URLs | 1408 | **1409** (+1 `/contact`; −7 legacy +7 pretty corporate routes net +1) |
| Legacy information URLs | 7 | **0** |
| `/contact` in sitemap | no | **yes** |
| `/kontakty` in sitemap | no | **no** |
| Categories/products in sitemap | present | **present** |
| Nested Lari URLs | 7 | **7** |
| Duplicate sitemap URLs | 0 | **0** |

Pretty information URLs now in sitemap include: `/about`, `/contact`, `/custom-equipment`, `/dealers`, `/delivery`, `/guarantee`, `/payment-methods`.

Evidence: Storage `sitemap-after/`, `verification/after-sitemap-verification.md`

---

## 11. Regression verification

16 bounded URLs checked — **0 failures**, **0** HTTP 500, **0** public `БЗПМ`.

- `/index.php` → **301** `/`
- Flat Lari → **301** nested
- `/contact` → **200**, canonical `/contact`
- `/kontakty` → **404** (accepted)

Evidence: Storage `verification/regression.json`

---

## 12. Audit issue status update

| ID | Status | Evidence |
|----|--------|----------|
| AUDIT-007 | **fixed** | 0 legacy information URLs in sitemap after |
| AUDIT-004 | **fixed** | Duplicate rows 928/927 removed; owners 850/857 retained |
| AUDIT-010 | **partially resolved** | Homepage/index.php + Lari pairs closed in Run 4.242; meta/title content wave deferred |
| AUDIT-002 | **fixed** | `/contact` present in sitemap |

---

## 13. Production mutation summary

| Action | Count |
|--------|-------|
| Remote uploads | **1** |
| Remote overwrites | **1** (`google_sitemap.php`) |
| Remote deletes | **0** |
| FTP writes | **1** |
| FTP reads/listings | **4** |
| FTP downloads | **4** |
| Admin saves | **0** |
| DB SELECTs | **7** |
| DB direct writes | **1** (DELETE 2 rows) |
| DB backup rows | **2** |
| Mail sends | **0** |
| Form submits | **0** |
| Import runs triggered | **0** |
| Monitor runs triggered | **0** |
| Product data changes | **0** |
| Category data changes | **0** |
| SEO URL changes | **2** rows deleted |
| Redirect changes | **0** |
| Sitemap file changes | **1** |
| Robots changes | **0** |
| llms.txt changes | **0** |
| Header/footer changes | **0** |
| Cache clears | **0** |
| public БЗПМ introduced | **no** |

---

## 14. Storage artefacts

```
X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-AUDIT-WAVE-B-SEO-FOUNDATION-01\
├── sitemap-before/  sitemap-after/
├── http-before/     http-after/
├── db-readonly/     db-backup-scoped/
├── source-before/   source-after/
├── patch/           rollback/
├── verification/    manifests/  logs/  reports/
```

Checkpoint storage: `production/baselines/SITE-002-STABLE-PROD-AUDIT-WAVE-B-SEO-FOUNDATION-01/`

---

## 15. Authority updates

Updated in-repo (this commit):

- `projects/ocpilot/OCPILOT-STATE.md`
- `projects/ocpilot/OPERATIONAL-INDEX.md` (Run 4.243)
- `projects/ocpilot/sites/site-002/production-profile.md`
- `projects/ocpilot/sites/site-002/site-passport.md`
- `projects/ocpilot/sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md`
- `projects/ocpilot/sites/site-002/tools/README.md`
- `projects/ocpilot/sites/site-002/baselines/SITE-002-STABLE-PROD-AUDIT-WAVE-B-SEO-FOUNDATION-01.md`

---

## 16. Git status

Selective commit of report, tool, patched sitemap mirror, checkpoint, and authority docs only. Storage artefacts **not** committed (policy).

---

## 17. SAFE UNKNOWN / blockers

- **Post-1C import verification (Run 4.240):** still pending next scheduled import — unrelated to this wave.
- **AUDIT-010 remaining title/description duplicates:** require separate content/meta wave; not in scope.
- **AUDIT-011 missing alt bulk:** deferred.

---

## 18. Final verdict

**SITE-002 AUDIT WAVE B SEO FOUNDATION COMPLETE — SITEMAP AND SEO DUPLICATES CLEANED**

Sitemap now emits canonical pretty URLs for corporate information pages and `/contact`. Legacy `index.php?route=information/...` entries removed. Redundant `compare-products`/`wishlist` SEO URL duplicates cleaned with scoped backup. Regression passed. `/contact` canonical unchanged. `/kontakty` 404 accepted.

---

## 19. Next task recommendation

1. **Await next scheduled 1C import** — close Run 4.240 verification (passive).
2. **Wave E — Information pages meta** — AUDIT-008/009 (missing meta/H1 on edge pages).
3. **Wave F — Polish** — AUDIT-011 alt text bulk (prioritized sampling).
