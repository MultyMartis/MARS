# REPORT — M9.8.9-09A FILTER LIMIT PERSISTENCE HOTFIX

**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** TEST — https://zpm.new-site.space/  
**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01`  
**Pass:** M9.8.9-09A  
**Date:** 2026-06-21  
**PRE-TASK:** Knowledge Map · Stable Checkpoint · site-passport · README — read. Forensic evidence: `reports/m9.8.9-09-work/` (live captures + `main-live.js`).

---

## 1. Root Cause Confirmation

### RC-1 — `updateBrowserUrl()` (JS)

**Confirmed.** `assets/js/main.js` rebuilt URL as `pathname + "?filters=" + stateText`, dropping `limit`, `sort`, `order`, `page` and any other query params.

Evidence: live capture `reports/m9.8.9-09-work/main-live.js` lines 4754–4758; Knowledge Map §7 documents preservation intent but live code did not implement it.

### RC-2 — URL generation in `category.php` (PHP)

**Confirmed.** Blocks building `$url` for **sort hrefs**, **limit hrefs**, and **pagination** included `filter`, `sort`, `order`, `limit` but **not** `filters`.

Evidence: forensic HTML `reports/m9.8.9-09-work/plp-stoly-filtered-live.html` — with `only_with_price` active, limit links were `?limit=50` without `filters=only_with_price=1`.

---

## 2. Changes Applied

| Layer | File | Change |
|-------|------|--------|
| JS | `assets/js/main.js` | `updateBrowserUrl()` — merge `filters` into existing `URLSearchParams(window.location.search)` |
| PHP | `catalog/controller/product/category.php` | Append `&filters=` in sort, limit, and pagination `$url` blocks |

**Not changed (per scope):** SQL, `product.php`, `getProducts()`, `getTotalProducts()`, `updateProducts()`, filter/price/category logic.

---

## 3. JS Fix

**Before:**

```javascript
const newUrl = stateText
  ? window.location.pathname + "?filters=" + stateText
  : window.location.pathname;
```

**After:**

```javascript
const params = new URLSearchParams(window.location.search);
if (stateText) {
  params.set("filters", stateText);
} else {
  params.delete("filters");
}
const query = params.toString();
const newUrl = query
  ? window.location.pathname + "?" + query
  : window.location.pathname;
```

All existing params (`limit`, `sort`, `order`, `page`, etc.) are preserved; only `filters` is updated or removed.

---

## 4. PHP Fix

Added to three `$url` assembly blocks (sorts, limits, pagination):

```php
if (isset($this->request->get['filters'])) {
    $url .= '&filters=' . $this->request->get['filters'];
}
```

Sort UI on PLP uses client-side `data-sort` handlers that already merge into `window.location.href` — no PHP change required for sort buttons. PHP sort `$data['sorts']` array (legacy hrefs) also receives `filters` for consistency.

---

## 5. QA Matrix

Target category: **Столы** — `/katalog/nejtralnoe-oborudovanie/stoly/`

| # | Scenario | Method | Result |
|---|----------|--------|--------|
| S1 | `limit=50` + `only_with_price` coexist | HTTP GET `?filters=only_with_price=1&limit=50` | **PASS** — checkbox checked, 50 cards, both params in URL |
| S2 | `only_with_price` → limit=50 link | HTTP — inspect + fetch limit href | **PASS** — href `?filters=only_with_price=1&limit=50`, filter persists on navigation |
| S3 | `only_with_price` → sort price ASC | HTTP GET `?filters=only_with_price=1&sort=p.price&order=ASC` | **PASS** — filter checked, sort params present |
| S4 | `only_with_price` → page 2 | HTTP GET + pagination link inspect | **PASS** — page-2 links include `filters=only_with_price=1` |
| S5 | Full combo | HTTP GET all five params | **PASS** — `filters`, `limit`, `sort`, `order`, `page` together |

**Probe artefact:** `reports/m9.8.9-09a-work/qa-results.json` — `all_pass: true`

**Operator browser QA still recommended for:**

- S1 **interaction path**: set limit=50 in UI → toggle `only_with_price` (JS `updateBrowserUrl` + AJAX) — HTTP cannot simulate checkbox AJAX chain.
- Pagination “load more” / mobile filter shell edge cases.

---

## 6. Before / After

| State | Before | After |
|-------|--------|-------|
| Toggle filter at `?limit=50` | URL → `?filters=only_with_price=1` (limit lost) | URL → `?limit=50&filters=only_with_price=1` |
| Limit link with active filter | `?limit=50` | `?filters=only_with_price=1&limit=50` |
| Pagination page 2 with filter | `?limit=50&page=2` | `?filters=only_with_price=1&limit=50&page=2` |
| Sort (JS) with filter in URL | Already preserved via `URL` API | Unchanged — still works |

---

## 7. Deploy Verification

| Step | Status |
|------|--------|
| FTP live capture | **OK** — `reports/m9.8.9-09a-work/live-capture/` |
| Backup | **OK** — `backups/main.js.pre-m9.8.9-09a-filter-limit-persistence.bak`, `backups/category.php.pre-m9.8.9-09a-filter-limit-persistence.bak` |
| Patch + upload | **OK** |
| SHA256 verify (post-upload re-download) | **OK** — see manifest |
| Twig cache clear | Attempted — `twig_cache_cleared: []` (empty dir or no files) |

**Manifest:** `reports/m9.8.9-09a-work/manifest-post-20260621-104243.json`

| File | SHA256 (pre) | SHA256 (post) | deploy_ok |
|------|--------------|---------------|-----------|
| `assets/js/main.js` | `fda2ef8c…cf6f` | `3e25fabe…843d0` | true |
| `catalog/controller/product/category.php` | `b4594c74…9036` | `7e5221b7…424e6` | true |

---

## 8. Rollback

1. Restore from backups:
   - `backups/main.js.pre-m9.8.9-09a-filter-limit-persistence.bak` → `assets/js/main.js`
   - `backups/category.php.pre-m9.8.9-09a-filter-limit-persistence.bak` → `catalog/controller/product/category.php`
2. Clear Twig template cache on server.
3. Re-verify PLP filter/limit interaction on Столы.

Full Beget backup remains disaster-recovery authority per checkpoint.

---

## 9. Changed Files

**Live (deployed):**

- `assets/js/main.js`
- `catalog/controller/product/category.php`

**Repo (artefacts, not git-committed):**

- `reports/m9.8.9-09a-work/m9.8.9-09a-deploy-run.py`
- `reports/m9.8.9-09a-work/m9.8.9-09a-qa-probe.py`
- `reports/m9.8.9-09a-work/live-capture/*`
- `reports/m9.8.9-09a-work/assets__js__main.js.patched`
- `reports/m9.8.9-09a-work/catalog__controller__product__category.php.patched`
- `reports/m9.8.9-09a-work/manifest-pre-20260621-104243.json`
- `reports/m9.8.9-09a-work/manifest-post-20260621-104243.json`
- `reports/m9.8.9-09a-work/qa-results.json`
- `backups/main.js.pre-m9.8.9-09a-filter-limit-persistence.bak`
- `backups/category.php.pre-m9.8.9-09a-filter-limit-persistence.bak`

---

## 10. Risks / SAFE UNKNOWN

| Item | Status |
|------|--------|
| **JS S1 click-path** (limit UI → toggle filter) | Deployed code verified; **operator browser QA pending** for AJAX interaction |
| **`filters` encoding** in PHP `$url` | Uses raw `$this->request->get['filters']` — same pattern as pagination `str_replace` for `%3B`; no new encoding layer added |
| **Breadcrumb / hub `$url` blocks** | Not patched — out of QA scope; may still drop `filters` on breadcrumb navigation |
| **Forensic report file** `REPORT M9.8.9-09 FILTER LIMIT PERSISTENCE FORENSIC` | **Not found as standalone doc in repo** — root causes taken from task brief + `m9.8.9-09-work` captures |
| **Git commit/push** | **Not performed** (per task) |

---

**Status:** Deploy complete · HTTP QA **all_pass** · awaiting operator browser QA.
