# REPORT — M9.8.9-09B LIMIT LINK FORENSIC AFTER HOTFIX

**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** TEST — https://zpm.new-site.space/  
**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01`  
**Pass:** M9.8.9-09B (forensic only)  
**Date:** 2026-06-21  
**PRE-TASK:** Knowledge Map · Stable Checkpoint · site-passport · M9.8.9-09A hotfix report — read.  
**Mode:** FORENSIC ONLY — no code changes, no deploy, no commit.

**Artefacts:** `reports/m9.8.9-09b-work/` (`plain.html`, `filtered.html`, `filtered_limit50.html`, `ajax-filtered.html`, `main-live.js`, `forensic-results.json`, `m9.8.9-09b-forensic-probe.py`)

---

## 1. Reproduction

### Operator-reported scenario (confirmed logically + by live HTML)

| Step | Action | Expected | Actual |
|------|--------|----------|--------|
| 1 | Open **Столы** PLP (no query params) | Plain catalog | OK |
| 2 | Enable filter **`only_with_price`** (checkbox / switch in sidebar) | Filtered grid, URL gets `filters=only_with_price=1` | OK — AJAX path |
| 3 | Change **Показывать по** (e.g. 15 → 50) | Filter persists + new limit | **FAIL** — filter lost, only `limit` remains |

### Why HTTP-only QA in 09A missed this

09A QA tested **full page load** with `?filters=only_with_price=1` already in URL, then inspected limit hrefs. That path **passes** after the PHP hotfix.

Operator QA uses the **interaction path**: filter toggle via sidebar → AJAX → then limit click. That path **does not reload** the limit selector — stale hrefs from step 1 remain in DOM.

### Inverse scenario (works)

**limit → filter:** user sets limit in URL or via limit link first, then toggles filter. `updateBrowserUrl()` merges `filters` into existing `URLSearchParams(window.location.search)` — `limit` preserved. Confirmed in live `main.js` and 09A report.

---

## 2. Browser URL State

Target category: `/katalog/nejtralnoe-oborudovanie/stoly/`

| Stage | Browser URL (after action) | Notes |
|-------|---------------------------|-------|
| Initial load | `…/stoly` (no query) | Limit hrefs generated **without** `filters` |
| After filter toggle (AJAX) | `…/stoly?filters=only_with_price=1` | Set by `updateBrowserUrl()` via `history.replaceState` |
| After limit click (broken path) | `…/stoly?limit=50` | Full navigation via stale `<a href>` — **`filters` absent** |

**Evidence:** plain-page limit href for 50:

```
https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly?limit=50
```

No `filters=` in href. Clicking it navigates away from filtered URL state.

---

## 3. Actual Limit Hrefs

Live capture **2026-06-21** — block `.category__limit` / «Показывать по:».

### A) Plain page (initial load, no filters) — `plain.html`

| Label | href |
|-------|------|
| 15 (active) | `…/stoly?limit=15` |
| 25 | `…/stoly?limit=25` |
| 50 | `…/stoly?limit=50` |
| 100 | `…/stoly?limit=100` |

**`filters` present:** NO (all four links)

> Note: live values are **15 / 25 / 50 / 100** (not 30). Matches `$allowed_limits` in `category.php`.

### B) Full page load with filter in URL — `filtered.html`  
Request: `?filters=only_with_price=1`

| Label | href |
|-------|------|
| 15 (active) | `…/stoly?filters=only_with_price=1&limit=15` |
| 25 | `…/stoly?filters=only_with_price=1&limit=25` |
| 50 | `…/stoly?filters=only_with_price=1&limit=50` |
| 100 | `…/stoly?filters=only_with_price=1&limit=100` |

**`filters` present:** YES — **09A PHP fix is live and working on full page render**

### C) Post-AJAX DOM state (simulated) — what operator actually clicks

After filter toggle on plain page:

- **Browser URL:** `?filters=only_with_price=1` ✓
- **DOM limit menu:** still block **A** (plain hrefs without `filters`) ✗

Because `updateProducts()` does **not** replace `.category__limit` (see §6–§7).

---

## 4. Actual Sort Hrefs

Sort control on PLP is **not href-based**. Template uses `<button data-sort="sort=…&order=…">` inside `.category__sort`.

Live `main.js` click handler (~6800):

```javascript
const url = new URL(window.location.href);
const params = new URLSearchParams(sortData);
params.forEach((value, key) => { url.searchParams.set(key, value); });
window.location.href = url.toString();
```

| Control type | Uses href? | Reads current browser URL? | After filter toggle |
|--------------|------------|----------------------------|---------------------|
| Sort buttons | No | **Yes** (`window.location.href`) | **Works** — `filters` already in URL |
| Limit links | **Yes** (`<a href>`) | **No** — uses server-rendered href from initial load | **Broken** — stale href without `filters` |

Legacy PHP `$data['sorts']` href array exists in `category.php` but is **not used** by current twig toolbar (buttons only).

---

## 5. Actual Pagination Hrefs

### Plain page — `plain.html`

```
…/stoly?page=2
…/stoly?page=3
… (no filters)
```

### Filtered full page load — `filtered.html`

```
…/stoly?filters=only_with_price=1&page=2
…/stoly?filters=only_with_price=1&page=3
…
```

**`filters` present:** YES on filtered full load (09A PHP pagination fix confirmed live).

### After AJAX filter toggle

`updateProducts()` **replaces** `.pagination` from fetched HTML. Post-toggle pagination links **do** include `filters` (same as filtered full page response).

Pagination clicks are also intercepted (`initPaginationAJAX`) and merge `page` into current browser URL before re-fetch — secondary safety.

**Asymmetry:** pagination is refreshed after filter AJAX; **limit menu is not**.

---

## 6. Source Of Generated Links

| UI element | Generator | Template | Updated by AJAX? |
|------------|-----------|----------|------------------|
| Limit menu `<a href>` | **`category.php`** → `$data['limits'][]['href']` | `category.twig` — `{% for l in limits %}` inside `.category__limit` | **NO** |
| Sort buttons | Static markup + **JS** click handler | `category.twig` buttons | N/A (uses live URL) |
| Pagination | **`category.php`** → `Pagination` + `$data['pagination']` | rendered in category section | **YES** — `updateProducts()` replaces `.pagination` |
| Product grid | **`category.php`** + twig partials | `.category__grid` | **YES** — `updateProducts()` replaces innerHTML |
| Browser URL on filter change | **JS** `updateBrowserUrl()` | — | YES (history API) |

### PHP — limit href assembly (live, post-09A)

File: `catalog/controller/product/category.php` (patched in 09A)

```php
if (isset($this->request->get['filters'])) {
    $url .= '&filters=' . $this->request->get['filters'];
}
// …
'href' => $this->url->link('product/category', 'path=' . $this->request->get['path'] . $url . '&limit=' . $value)
```

**Proof filters in limit hrefs when request carries `filters`:** captured `filtered.html` and `ajax-filtered.html` (full HTML response to `?filters=only_with_price=1`).

### Twig — limit markup

```twig
<div class="category__limit">
  …
  {% for l in limits %}
  <a class="category__sort-item…" href="{{ l.href }}">{{ l.text }}</a>
  {% endfor %}
</div>
```

Source: `m9.8.5-products-per-page-work/category.twig` (same structure on live).

### JS — filter toggle chain (live `main.js`)

1. `initChecks` / `initSwitches` → `change` → `updateBrowserUrl(form)`
2. `updateBrowserUrl` → merges `filters` into `URLSearchParams(window.location.search)` → `replaceState` → `debouncedUpdate(root)`
3. `debouncedUpdate` → `updateProducts(root)`
4. `updateProducts` fetch uses current URL params + form state, parses response, replaces:
   - `.category__grid` ✓
   - `.pagination` ✓
   - **`.category__limit` — NOT touched** ✗

Limit dropdown JS (~6820) only toggles menu open/close — **no href rewrite**, no click intercept.

---

## 7. Root Cause

### RC-09B-1 — Stale limit hrefs after AJAX filter (PRIMARY)

**Proven chain:**

```
filter checkbox change
  → updateBrowserUrl()          // URL gets ?filters=…  ✓
  → debouncedUpdate()
  → updateProducts()
       → fetch( pathname + ?filters=… )
       → replace .category__grid   ✓
       → replace .pagination      ✓  (new links include filters)
       → .category__limit UNCHANGED ✗  (still plain-page hrefs ?limit=N only)
  → user clicks limit link
       → full navigation to ?limit=N   (no filters)
       → filter lost
```

**Concrete DOM proof:**

| Source file | limit=50 href |
|-------------|---------------|
| `plain.html` (initial + post-AJAX DOM) | `…/stoly?limit=50` |
| `filtered.html` (server would render) | `…/stoly?filters=only_with_price=1&limit=50` |

Server **already returns correct limit links** in AJAX response (`ajax-filtered.html`), but JS **never applies them** to the toolbar.

### RC-09B-2 — 09A scope gap (CONFIRMED, not regression)

09A fixed:

| Layer | Fix | Covers filter→limit via AJAX? |
|-------|-----|-------------------------------|
| PHP `category.php` | append `filters` to sort/limit/pagination `$url` | Only on **full page render** |
| JS `updateBrowserUrl()` | preserve query params when setting `filters` | Fixes **limit→filter** and URL bar after filter toggle |
| JS `updateProducts()` | — | **Not updated** — omits limit toolbar refresh |

09A HTTP QA S2 validated **direct GET** `?filters=only_with_price=1` → limit hrefs. That does **not** exercise AJAX partial DOM update.

### What is NOT the cause (ruled out by live evidence)

| Hypothesis | Verdict |
|------------|---------|
| 09A PHP not deployed | **Ruled out** — `filtered.html` limit hrefs include `filters` |
| 09A JS `updateBrowserUrl` not deployed | **Ruled out** — live `main.js` has merged-params version |
| Limit uses different PHP branch | **Ruled out** — same `$data['limits']` block; twig `{% for l in limits %}` |
| JS rewrites limit hrefs incorrectly | **Ruled out** — limit JS only opens/closes menu |
| Sort/pagination same bug for filter→limit | **Sort ruled out** (URL merge at click). **Pagination ruled out** (DOM replaced after AJAX) |

---

## 8. Recommended Fix

**Forensic recommendation only — NOT implemented in this pass.**

### Option A (minimal, mirrors pagination) — preferred

In `updateProducts()`, after parsing AJAX HTML response, also replace limit menu from fetched doc:

```javascript
const newLimitMenu = doc.querySelector('.category__limit [data-limit-menu]');
const oldLimitMenu = document.querySelector('.category__limit [data-limit-menu]');
if (newLimitMenu && oldLimitMenu) {
  oldLimitMenu.innerHTML = newLimitMenu.innerHTML;
  // optionally sync active button text from doc
}
```

Server already emits correct hrefs when `filters` is in fetch URL — no PHP change required.

### Option B — JS limit handler (mirror sort)

Replace limit `<a href>` navigation with click handler that sets `limit` on `new URL(window.location.href)` then navigates or calls `updateProducts`. More invasive; duplicates sort pattern.

### Option C — replace entire toolbar block

Replace `.category__toolbar` (or sort+limit cluster) from AJAX response. Broader refresh; verify sort button state.

### QA after fix

Must test **interaction matrix**, not only direct URL loads:

| # | Scenario | Method |
|---|----------|--------|
| Q1 | plain → toggle filter → click limit 50 | **Browser** |
| Q2 | plain → toggle filter → inspect limit href in DOM | DevTools |
| Q3 | `?limit=50` → toggle filter | Browser (regression) |
| Q4 | filter → sort → limit | Browser combo |

---

## 9. Risks

| Risk | Level | Notes |
|------|-------|-------|
| Deploy Option A without QA | Medium | Must not break limit→filter or plain load |
| Only fixing PHP again | **No effect** on this bug | PHP already correct on full render |
| `getFullFilterUrl()` still drops non-filter params | Low | Copy-link feature; separate from limit menu; still has `fullPath + "?filters="` pattern |
| Breadcrumb / subcategory chips with stale params | Low | Out of 09B scope; chips on page may carry unrelated `limit=` |
| Pagination «Показать ещё» `data-next` | Low | Updated with pagination block — includes filters after AJAX |

---

## 10. Changed Files

**Forensic pass — no live or repo source changes.**

| File | Action |
|------|--------|
| `reports/SITE-002-M9.8.9-09B-LIMIT-LINK-FORENSIC-AFTER-HOTFIX.md` | **Created** — this report |
| `reports/m9.8.9-09b-work/m9.8.9-09b-forensic-probe.py` | **Created** — live capture script |
| `reports/m9.8.9-09b-work/plain.html` | **Created** — live HTML capture |
| `reports/m9.8.9-09b-work/filtered.html` | **Created** — live HTML `?filters=only_with_price=1` |
| `reports/m9.8.9-09b-work/filtered_limit50.html` | **Created** — combo URL capture |
| `reports/m9.8.9-09b-work/ajax-filtered.html` | **Created** — fetch response snapshot |
| `reports/m9.8.9-09b-work/main-live.js` | **Created** — live JS capture |
| `reports/m9.8.9-09b-work/forensic-results.json` | **Created** — structured probe output |

**Not changed:** `assets/js/main.js`, `catalog/controller/product/category.php`, twig, deploy state.

---

## Summary

| Question | Answer |
|----------|--------|
| Does 09A PHP fix work on live? | **Yes** — limit hrefs include `filters` when page loaded with `?filters=…` |
| Why filter→limit still breaks? | **AJAX partial update** refreshes grid + pagination but **leaves `.category__limit` hrefs from initial plain load** |
| Where filters are lost | **Click** on stale `<a href="…?limit=N">` — full navigation without `filters` |
| Proof type | Live HTML captures + live `main.js` + `updateProducts()` DOM scope |

**Status:** Root cause identified with live evidence. Ready for targeted hotfix (Option A) in a separate implementation pass.

**SAFE UNKNOWN:** Whether mobile filter shell uses a separate limit control — not observed on desktop capture; desktop toolbar path proven broken.
