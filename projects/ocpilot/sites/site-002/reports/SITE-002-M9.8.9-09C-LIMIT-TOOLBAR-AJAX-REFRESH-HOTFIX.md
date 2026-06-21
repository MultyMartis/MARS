# REPORT — M9.8.9-09C LIMIT TOOLBAR AJAX REFRESH HOTFIX

**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01`  
**Date:** 2026-06-21  
**Target:** https://zpm.new-site.space/ — PLP «Столы»  
**PRE-TASK RULE:** Knowledge Map + Commercial Trust baseline + 09B forensic + site-passport — read and applied.

---

## 1. Root Cause

09B proved PHP (post-09A) already emits correct limit `<a href>` values with `filters` when the fetch URL includes filters. The remaining bug was **client-side partial DOM update**:

| Step | Behavior |
|------|----------|
| User loads plain PLP | `.category__limit` hrefs = `?limit=N` only |
| User toggles filter | `updateProducts()` fetches full page with `?filters=…` |
| AJAX response | Server HTML contains limit hrefs **with** `filters` |
| `updateProducts()` before fix | Replaced `.category__grid` + `.pagination` only |
| Stale DOM | `.category__limit` kept initial plain-page hrefs |
| User clicks limit | Full navigation via stale `?limit=N` → **filters dropped** |

**Root cause:** `updateProducts()` did not refresh the limit toolbar from the AJAX HTML response.

---

## 2. JS Change

### `updateProducts(root)` — limit toolbar refresh

After grid + pagination replacement, parse response and swap limit block:

```javascript
const oldLimit = document.querySelector(".category__limit");
const newLimit = doc.querySelector(".category__limit");
if (newLimit && oldLimit) {
  oldLimit.outerHTML = newLimit.outerHTML;
  initCategoryLimitMenu();
}
```

### `initCategoryLimitMenu()` — new reusable init

Extracted from the one-shot limit IIFE. Re-binds the toggle button (via `cloneNode`) after DOM replacement so the dropdown still opens post-AJAX.

### Limit close-on-outside — delegated listener

Replaced stale-closure document listener with a delegated handler that queries `.category__limit` on each click — survives limit DOM refresh.

### Unchanged behavior

- Grid innerHTML replacement  
- Pagination outerHTML replacement / insert / remove  
- `scrollToCategorySection()`  
- `initPaginationAJAX(root)` after update  
- Filter form state, `updateBrowserUrl`, debounced fetch URL construction  
- Sort, page, limit URL params preserved in fetch (09A)

---

## 3. Files Changed

| File | Action |
|------|--------|
| **Live** `assets/js/main.js` | **Patched + deployed** |
| `backups/main.js.pre-m9.8.9-09c-limit-ajax-refresh.bak` | Pre-deploy backup |
| `reports/m9.8.9-09c-work/live-capture/assets__js__main.js` | FTP pre-capture |
| `reports/m9.8.9-09c-work/assets__js__main.js.patched` | Patched work copy |
| `reports/m9.8.9-09c-work/m9.8.9-09c-deploy-run.py` | Deploy script |
| `reports/m9.8.9-09c-work/m9.8.9-09c-qa-probe.py` | Automated QA probe |
| `reports/m9.8.9-09c-work/qa-results.json` | Probe output |
| `reports/m9.8.9-09c-work/manifest-pre-20260621-113652.json` | Pre-deploy manifest |
| `reports/m9.8.9-09c-work/manifest-post-20260621-113652.json` | Post-deploy manifest + SHA verify |

**Not changed:** PHP, SQL, `category.php`, `product.php`, `filterssidebar.twig`, `style.css`, commercial trust block.

### Deploy verification

| Field | Value |
|-------|-------|
| SHA256 pre | `3e25fabebd954399ece49cd31bc352f15752f82aabb28b711585a457656843d0` |
| SHA256 post | `3ab098c786099c24e3ccf33e852b0aacc2d66089e81830e2b48af97db3920dbe` |
| Size delta | 201522 → 202482 (+960 B) |
| FTP verify | **OK** (`deploy_ok: true`) |
| Twig cache | Cleared (empty dir / no files listed) |

---

## 4. QA Results

### Automated (server-side + live JS) — PASS

Probe: `reports/m9.8.9-09c-work/qa-results.json`

| Check | Result |
|-------|--------|
| Plain PLP limit hrefs — no `filters` | PASS |
| Filtered PLP limit hrefs include `filters=only_with_price=1` | PASS |
| Combo URL limit hrefs preserve filters + sort | PASS |
| Live JS contains `initCategoryLimitMenu` | PASS |
| Live JS contains `oldLimit.outerHTML = newLimit.outerHTML` | PASS |
| Live JS contains delegated close-on-outside | PASS |

### Browser matrix — **PENDING operator**

Per task: interaction scenarios require manual browser QA after deploy.

| # | Scenario | Expected | Status |
|---|----------|----------|--------|
| **Q1** | `only_with_price` → limit 50 | URL: `filters=only_with_price=1` + `limit=50`; filter not reset | **PENDING** |
| **Q2** | attr filter → limit 50 | `filters` preserved | **PENDING** |
| **Q3** | limit=50 → filter → sort ASC → page 2 | `filters`, `limit`, `sort`, `order`, `page` all preserved | **PENDING** |
| **Q4** | Limit dropdown opens after filter AJAX | Menu toggles; no JS errors | **PENDING** |
| **Q5** | Active limit label correct after filter AJAX | Button text matches selected limit | **PENDING** |
| **Q6** | Pagination after filter AJAX | Page links work; params preserved | **PENDING** |

**SAFE UNKNOWN:** Mobile filter shell separate limit control — not probed; desktop toolbar path is the proven failure mode from 09B.

---

## 5. Before / After

| Aspect | Before (09A + 09B state) | After (09C) |
|--------|--------------------------|-------------|
| PHP limit hrefs with filters | Correct on full page load | Unchanged |
| Limit hrefs after filter AJAX | **Stale** (plain-load hrefs) | **Refreshed** from AJAX HTML |
| Filter → limit click | Drops `filters` | Expected: keeps `filters` (browser QA pending) |
| Limit dropdown after AJAX | Worked (old node) but wrong hrefs | Re-inited on fresh node |
| Pagination after filter | Correct (already refreshed) | Unchanged |

---

## 6. Rollback

1. Restore from backup:
   - `backups/main.js.pre-m9.8.9-09c-limit-ajax-refresh.bak` → live `assets/js/main.js`
2. Or re-deploy pre-patch capture:
   - `reports/m9.8.9-09c-work/live-capture/assets__js__main.js`
3. Clear Twig template cache after rollback.
4. Full hosting restore via Beget backup if needed.

Pre-deploy SHA256: `3e25fabebd954399ece49cd31bc352f15752f82aabb28b711585a457656843d0`

---

## 7. Risks

| Risk | Level | Mitigation |
|------|-------|------------|
| Limit toggle broken after AJAX | Low | `initCategoryLimitMenu()` re-bind + delegated doc click |
| Duplicate document listeners | Low | Single delegated close handler; toggle uses cloneNode |
| Sort/limit mutual close regression | Low | Same sort-close logic preserved in init |
| Deploy without browser QA | Medium | Operator matrix Q1–Q6 required before closing bug |
| Mobile limit path | Low | **SAFE UNKNOWN** — desktop path fixed; verify if mobile differs |

---

## Git

- **Commit:** NO  
- **Push:** NO  

---

**Status:** Deploy complete; SHA verified. Automated server/JS checks PASS. **Awaiting operator browser QA** on Столы scenarios Q1–Q6.
