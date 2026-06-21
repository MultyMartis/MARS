# REPORT — M9.8.9-04A FILTER SCROLL OFFSET TUNING

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
| Prior pass | [SITE-002-M9.8.9-04-FILTER-SCROLL-OFFSET-FIX.md](SITE-002-M9.8.9-04-FILTER-SCROLL-OFFSET-FIX.md) |

---

## 1. Previous Offset

| Viewport | Source | Value |
|----------|--------|-------|
| Desktop | `getPageScrollOffset()` — measured `[data-header-sticky]` | **≈ 131px** |
| Mobile | `getPageScrollOffset()` — measured `[data-header-mobilebar]` | **≈ 90px** |
| Fallback | CSS `--header-posotopn-and-size` / PDP pattern | 140 / 100 |

**Formula (unchanged):**

```javascript
targetTop = target.getBoundingClientRect().top + scrollTop - offset;
```

Sticky header on catalog PLP appears later than on PDP; large measured offset created excessive gap above `section.category`.

---

## 2. New Offset

| Viewport | Value |
|----------|-------|
| Desktop | **15px** (fixed) |
| Mobile | **15px** (fixed) |

**Change in `scrollToCategorySection()` only:**

```diff
-    var offset = getPageScrollOffset();
+    var offset = 15;
```

**Preserved:**

- Target: `.page--category section.category` → `section.category`
- `behavior: 'smooth'`
- Mobile filter close via `[data-filter-close]` when `is-filter-open`
- `getPageScrollOffset()`, `getPageScrollTop()` helpers (architecture intact)
- AJAX filter flow in `updateProducts()` — still calls `scrollToCategorySection()`

**Not changed:** PHP, SQL, filters, sticky header logic, overlay system.

---

## 3. Files Changed

| Path | Action |
|------|--------|
| **Live FTP** `assets/js/main.js` | **patched + deployed** |
| `reports/m9.8.9-04a-work/live-capture/assets__js__main.js` | pre-deploy capture |
| `reports/m9.8.9-04a-work/assets__js__main.js.patched` | patched work copy |
| `backups/main.js.pre-m9.8.9-04a-filter-scroll-offset-tuning.bak` | rollback backup |
| `reports/m9.8.9-04a-work/manifest-pre-20260619-115007.json` | pre-deploy manifest |
| `reports/m9.8.9-04a-work/manifest-post-20260619-115007.json` | post-deploy manifest |
| `reports/m9.8.9-04a-work/m9.8.9-04a-deploy-run.py` | deploy script |
| `reports/m9.8.9-04a-work/m9.8.9-04a-qa-run.py` | QA script |
| `reports/m9.8.9-04a-work/qa-results.json` | QA evidence |
| `reports/SITE-002-M9.8.9-04A-FILTER-SCROLL-OFFSET-TUNING.md` | this report |

### Deploy hashes

| Phase | SHA-256 |
|-------|---------|
| Pre (M9.8.9-04 live) | `c74c9c1dc993a0e7acb5189bd71d1885b93bd46c3e5ee155aa80411c15d5f5d2` |
| Post (M9.8.9-04A) | `bbf85222ef9790d95d402385661b5a4751ba51da20c4dad52530edce89605d38` |

---

## 4. QA Results

**Run:** 2026-06-19T11:50:20Z · **QA_PASS: true**

| Category | Desktop `section_top` | Mobile `section_top` | AJAX | JS errors |
|----------|----------------------|---------------------|------|-----------|
| Столы | 15px | 15px | OK | none |
| Моечные ванны | 15px | 15px | OK | none |
| Подтоварники | 15px | 15px | OK | none |
| Тележки | 15px | 15px | OK | none |

**Live JS checks:** `scrollToCategorySection` present · `getPageScrollOffset` present · `var offset = 15` present · `grid.scrollIntoView` absent from filter path.

Evidence: [m9.8.9-04a-work/qa-results.json](m9.8.9-04a-work/qa-results.json)

---

## 5. Rollback

Restore pre-04A live `main.js`:

```
backups/main.js.pre-m9.8.9-04a-filter-scroll-offset-tuning.bak
→ FTP assets/js/main.js
```

Or revert single line in `scrollToCategorySection()`:

```javascript
var offset = getPageScrollOffset();
```

Full M9.8.9-04 rollback (pre scroll fix):

```
backups/main.js.pre-m9.8.9-04-filter-scroll-offset.bak
```

---

**Git:** commit NO · push NO
