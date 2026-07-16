# REPORT — FP-0002 V9-06E57 Lifebuoy Global Background Parallax

**Date:** 2026-07-16  
**Project:** FP-0002 «Шпиговский»  
**Runtime:** http://shpigovsky.test/  
**Overall:** PASS (local validation); **awaiting operator review**  
**Commit / push / freeze:** none  
**DB writes:** 0  

---

## 1. Status

- **Verdict:** PASS (local)
- Operator review pending
- DB writes: **0**
- No commit, no push, no freeze

## 2. Pre-Change Checkpoint

- **Path:** `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e57-before-lifebuoy-global-parallax-20260716-212623\`
- **Protected files backed up:** `v9-style.css`, `v9-shell.js`, `assets.php`, `body-start.php`, floating-header set, header/footer, incoming `lifebuoy.webp`
- **Protected operator CSS hash (before = after):** `2F7CC5ACE7E6718ADE81B9871FBE73B62D2D0D3AE5B5C1818E2F9266D374793E`
- **Marker:** V9-06E57; operator CSS/HTML is current canon; lifebuoy parallax task; no broad sync; DB writes prohibited; no commit/push/freeze

## 3. Operator Changes Preserved

- Pre-wave theme source↔runtime: **DIFF_COUNT = 0** (647/647)
- Post-wave theme source↔runtime: **mismatch = 0** (650/650; +3 new files)
- **Promoted files:** none required (already matched)
- **Protected baseline:** `v9-style.css` untouched (separate scoped CSS used instead)
- Unresolved drift: none in theme for this wave

## 4. Asset Integration

| Role | Path |
|------|------|
| Incoming | `INCOMING/OPERATOR-ASSETS/E56/lifebuoy.webp` |
| Canonical | `WORDPRESS/theme/shpigovsky/assets/img/decor/lifebuoy.webp` |
| Runtime | `…/wp-content/themes/shpigovsky/assets/img/decor/lifebuoy.webp` |

- Size: **95568** bytes  
- Dimensions: **1075×1093**  
- SHA256: `B4F1C9F6A09A68F6F7C31565CF1383DA92F223BB99347D9E22D19B7543430011`  
- Recompress: **no** (byte-identical copy)  
- HTTP: **200**

## 5. Implementation Architecture

- **Mount:** `template-parts/layout/body-start.php` — single global node before `.site-page-shell`
- **CSS:** new scoped `assets/css/fp02-lifebuoy-parallax.css` (operator `v9-style.css` not edited)
- **JS:** `assets/js/fp02-lifebuoy-parallax.js` — scroll progress → CSS custom properties
- **Enqueue:** additive block in `inc/assets.php`
- **Layering:** fixed layer `z-index: 0`; `.site-page-shell { position: relative; z-index: 1 }`
- **Pointer:** `pointer-events: none` on root; `aria-hidden="true"`
- **Reduced motion:** freeze at effective progress `0.28` (decoration kept)

## 6. Motion Model

| State | Progress | Approx visible width | Notes |
|-------|----------|----------------------|-------|
| Top | 0 | ~29% | X≈−70%, Y≈−12vh, scale 0.96 |
| Mid | 0.5 | ~46% | Arc bulge via `sin(π·t)` |
| Bottom | ~1 | ~50% | X≈−50%, Y≈52vh, scale 1.0 |

- Opacity fixed at **0.3**
- Arc: X interpolates −70%→−50% plus mild mid-journey inward bulge
- Y: −12vh → 52vh (long), capped for short mode
- Reverse: same mapping of live scroll progress (no separate reverse engine)
- Rotation: **not used** (subtle scale only)

## 7. Long vs Short Page Handling

- **Threshold:** `scrollable < max(2400px, 4 × innerHeight)`
- **Long** (Home, `/uslugi/`, sections, services, О центре): full travel
- **Short** (Контакты ~3425px @1440, Blog ~1988px): travel factor `progress × 0.5`, reduced end X/Y
- Rationale: Contacts is “short” relative to Home (~16k scroll) but still >720px; viewport-relative threshold matches operator intent

## 8. Exact Files Changed

### Canonical source

- `WORDPRESS/theme/shpigovsky/assets/img/decor/lifebuoy.webp` (new)
- `WORDPRESS/theme/shpigovsky/assets/css/fp02-lifebuoy-parallax.css` (new)
- `WORDPRESS/theme/shpigovsky/assets/js/fp02-lifebuoy-parallax.js` (new)
- `WORDPRESS/theme/shpigovsky/template-parts/layout/body-start.php` (mount)
- `WORDPRESS/theme/shpigovsky/inc/assets.php` (enqueue)

### Runtime (exact-file delivery only)

- Same five paths under `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky\wp-content\themes\shpigovsky\`

### Reports / evidence

- `REPORTS/REPORT-FP-0002-V9-06E57-lifebuoy-global-parallax.md`
- `REPORTS/evidence/v9-06e57-lifebuoy-global-parallax/`
- `PROJECT-STATUS.md` (status line)

## 9. Source-to-Runtime Delivery

| File | SHA256 (source=runtime) |
|------|-------------------------|
| `lifebuoy.webp` | `B4F1C9F6…430011` |
| `fp02-lifebuoy-parallax.css` | `119C0CCC…EABB01` |
| `fp02-lifebuoy-parallax.js` | `008226FC…C11B214` |
| `body-start.php` | `916376F8…E554A9` |
| `assets.php` | `4D6E6FDA…212CE4` |

- No broad theme sync
- Operator `v9-style.css` preserved byte-identical

## 10. Validation

- Long-page matrix (Home top/25/50/75/bottom + reverse): PASS  
- Short-page matrix (Контакты top/mid/bottom, short mode): PASS  
- Viewports 1440 / 1280 / 1024 / 768 / 390 / 375 / 320: PASS, overflow **0**  
- Reverse scroll: transform returns to start at progress 0  
- Performance: single instance; rAF coalesce; ~348ms for 21-step harness scroll  
- JS/PHP: **0** console/page errors; routes HTTP 200  

Evidence: `REPORTS/evidence/v9-06e57-lifebuoy-global-parallax/` (35 screenshots + CSV/JSON)

## 11. Regression

| Area | Result |
|------|--------|
| Home hero | PASS |
| Floating header | PASS (z 950 above decor) |
| Forms | PASS (markup present; pointer-events none on decor) |
| Galleries / video | PASS (untouched; routes 200) |
| Offcanvas trigger | PASS |
| Horizontal overflow | PASS (0) |

## 12. Risks and Tails

- Taste of arc amplitude / end Y on ultrawide or very tall mobile may still need operator tweak
- Short-page travel is intentionally modest on Contacts; operator may want slightly more presence
- Lifebuoy shows through translucent content sections by design (opacity 0.3) — confirm taste
- No performance issue observed locally; not a production load test

## 13. Git Status

- No commit
- No push
- Exact FP-0002 theme + report paths only for this wave
- Foreign WIP elsewhere in monorepo untouched

## 14. Operator Review Checklist

- [ ] Overall look of the lifebuoy on the page
- [ ] Start position at top-left (~30% visible)
- [ ] Movement path while scrolling down (left-edge arc)
- [ ] Reverse motion while scrolling up
- [ ] Long pages (Home / services)
- [ ] Short pages (Contacts)
- [ ] Desktop and mobile
- [ ] No interference with content / header / forms
