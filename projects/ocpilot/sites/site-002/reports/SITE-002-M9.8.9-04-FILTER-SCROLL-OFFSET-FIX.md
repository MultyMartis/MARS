# REPORT — M9.8.9-04 FILTER SCROLL OFFSET FIX

**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01`  
**Environment:** https://zpm.new-site.space/  
**Date:** 2026-06-19  
**Status:** **DEPLOYED + QA PASS**

---

## Authority confirmation

| Item | Value |
|------|-------|
| Knowledge Map | [knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) |
| Stable checkpoint | [baselines/SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01.md](../baselines/SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01.md) |
| Authority state | **`SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01`** — confirmed |

---

## 1. Root Source

| Item | Detail |
|------|--------|
| **File** | `assets/js/main.js` (live FTP) |
| **Function** | `updateProducts(root)` inside filters IIFE `(function () { ... })();` |
| **Trigger** | After successful filter/pagination AJAX fetch — grid + pagination DOM swap |
| **Prior scroll call** | `grid.scrollIntoView({ behavior: 'smooth', block: 'start' })` on `.category__grid` |

**Problem:** `scrollIntoView` on the inner grid scrolled to the product grid block (mid-section), ignoring sticky header offset and skipping the top of `section.category`.

---

## 2. Scroll Logic Before (audit)

| # | Finding |
|---|---------|
| 1 | **Where scroll happens:** `updateProducts()` → `.then(html => { ... })` after grid/pagination update |
| 2 | **Target element:** `.category__grid` (inner product grid) |
| 3 | **Offset:** **none** — native `scrollIntoView({ block: 'start' })` |
| 4 | **Smooth scroll:** **yes** — `behavior: 'smooth'` |
| 5 | **Multiple handlers:** **one** filter-scroll handler in `updateProducts`; other `scrollIntoView` usages elsewhere (form errors, PDP) — **not** filter-related |

**Existing offset patterns in project (reused):**

- PDP: `scrollToProductContentMain()` — `window.scrollTo` + measured offset (100 mobile / 140 desktop)
- CSS token: `--header-posotopn-and-size: 140px` in `style.css`
- Sticky header bars: `[data-header-sticky]` / `[data-header-mobilebar]`
- Scroll lock: `body.is-scroll-locked` + `body.style.top` (filter mobile drawer)

---

## 3. Scroll Logic After

Added inside filters IIFE (before `updateProducts`):

| Function | Role |
|----------|------|
| `getPageScrollOffset()` | Measures sticky header bar height; fallback `--header-posotopn-and-size`; last resort 100/140 (PDP pattern) |
| `getPageScrollTop()` | Reads scroll position including `is-scroll-locked` state |
| `scrollToCategorySection()` | Target: `.page--category section.category` → `section.category`; closes mobile filter drawer if open; `window.scrollTo({ behavior: 'smooth' })` with header offset |

**Replacement in `updateProducts`:**

```diff
- grid.scrollIntoView({ behavior: 'smooth', block: 'start' });
+ scrollToCategorySection();
```

**Mobile:** if filter offcanvas is open (`is-filter-open`), clicks `[data-filter-close]` before scroll so `unlockScroll()` restores page scroll and smooth scroll works.

---

## 4. Files Changed

| Path | Action |
|------|--------|
| **Live FTP** `assets/js/main.js` | **patched + deployed** |
| `reports/m9.8.9-04-work/live-capture/assets__js__main.js` | pre-deploy capture |
| `reports/m9.8.9-04-work/assets__js__main.js.patched` | patched work copy |
| `backups/main.js.pre-m9.8.9-04-filter-scroll-offset.bak` | rollback backup |
| `reports/m9.8.9-04-work/manifest-pre-20260619-111745.json` | pre-deploy manifest |
| `reports/m9.8.9-04-work/manifest-post-20260619-111745.json` | post-deploy manifest (initial) |
| `reports/m9.8.9-04-work/m9.8.9-04-deploy-run.py` | deploy script |
| `reports/m9.8.9-04-work/m9.8.9-04-qa-run.py` | QA script |
| `reports/m9.8.9-04-work/qa-results.json` | QA evidence |
| `reports/SITE-002-M9.8.9-04-FILTER-SCROLL-OFFSET-FIX.md` | this report |

**Not changed:** PHP, SQL, filter profiles, price logic, pagination, PDP, megamenu, overlay CSS.

### Deploy hashes

| Phase | SHA-256 |
|-------|---------|
| Pre (live capture) | `a1759eead063fa9616266507da39a27c4c870a947aa24532aa3a7db0d37e2cd9` |
| Post (final live) | `c74c9c1dc993a0e7acb5189bd71d1885b93bd46c3e5ee155aa80411c15d5f5d2` |

---

## 5. QA Results

**Script:** `reports/m9.8.9-04-work/m9.8.9-04-qa-run.py`  
**Result:** `qa_pass: true` — all 4 categories × desktop + mobile

| Category | Desktop offset | Mobile offset | AJAX | JS errors |
|----------|----------------|---------------|------|-----------|
| Столы | section.top ≈ 131 (expected 131) | section.top ≈ 90 (expected 90) | OK | none |
| Моечные ванны | section.top ≈ 131 | section.top ≈ 90 | OK | none |
| Подтоварники | section.top ≈ 131 | section.top ≈ 90 | OK | none |
| Тележки | section.top ≈ 131 | section.top ≈ 90 | OK | none |

**Live JS checks:** `scrollToCategorySection` present, `getPageScrollOffset` present, `grid.scrollIntoView` absent from filter update path.

---

## 6. Rollback

1. Upload backup → live:

   `backups/main.js.pre-m9.8.9-04-filter-scroll-offset.bak` → `assets/js/main.js`

2. No Twig cache clear required (JS-only change).

3. Verify: filter apply restores `grid.scrollIntoView` behavior.

---

## Git

- **Commit:** NO  
- **Push:** NO
