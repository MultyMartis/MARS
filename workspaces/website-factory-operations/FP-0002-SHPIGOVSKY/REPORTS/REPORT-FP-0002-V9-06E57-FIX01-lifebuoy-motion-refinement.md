# REPORT — FP-0002 V9-06E57-FIX01 Lifebuoy Motion Refinement

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

- **Path:** `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e57-fix01-before-lifebuoy-motion-refinement-20260716-214936\`
- **Protected files:** source/runtime `fp02-lifebuoy-parallax.css/js`, `body-start.php`, `assets.php`, `v9-style.css`, `lifebuoy.webp`
- **Hashes:** see `hashes.csv` / `asset-hash-record.txt` in checkpoint
- **Marker:** V9-06E57-FIX01; lifebuoy motion refinement; operator CSS/HTML protected; no broad sync; DB writes prohibited; no commit/push/freeze

## 3. Operator Changes Preserved

- Pre-wave lifebuoy + operator CSS source↔runtime: **MATCH** (no promote required)
- **Promoted files:** none
- **Protected baseline:** `v9-style.css` SHA256 `2F7CC5ACE7E6718ADE81B9871FBE73B62D2D0D3AE5B5C1818E2F9266D374793E` (unchanged)
- Unresolved drift: none for scoped theme files

## 4. Motion Refinement Implemented

| Adjustment | Model |
|------------|--------|
| Base size +≈30% | CSS width E57×1.30: `min(88vw,806px)` / tablet `min(100vw,676px)` / mobile `min(100vw,546px)` |
| Reveal → ~70% | Long X `-70% → -30%` + mid arc×8; measured Home bottom **~72%** visible width |
| Scale mid +20% | Piecewise: `1.00 → 1.20` for `t 0→0.5` (smoothstep) |
| Scale end −40% from peak | `1.20 → 0.72` (= mid×0.60) for `t 0.5→1` |
| Rotation | Long `-6° → +18°` (24° total) on eased progress; origin center |
| Reverse | Same live progress mapping; reverse-p50 matches forward-p50 |

Opacity remains **0.3**.

## 5. Technical Implementation

### CSS (`fp02-lifebuoy-parallax.css`)

- Larger base widths (+30%)
- Transform stack: `translate3d → scale → rotate` via `--fp02-lb-*` vars
- `transform-origin: center center`
- Reduced-motion: `will-change: auto` only (freeze still in JS)

### JS (`fp02-lifebuoy-parallax.js`)

- Normalized `t` + short-page `tRaw = progress × 0.55`
- X/Y/rotate: `easeInOutCubic(tRaw)`
- Scale: Hermite `smoothstep` per half (soft midpoint, no snap)
- Short envelope: X end −42%, Y end 28vh, scale `1→1.12→0.85`, rotate `-3°→+10°`
- Threshold unchanged: `scrollable < max(2400, 4×vh)`
- Passive scroll + rAF; reduced-motion freeze at `0.28` (**unchanged**)

### Unchanged

- `body-start.php`, `inc/assets.php`, asset file, operator `v9-style.css`

## 6. Exact Files Changed

### Canonical source

- `WORDPRESS/theme/shpigovsky/assets/css/fp02-lifebuoy-parallax.css`
- `WORDPRESS/theme/shpigovsky/assets/js/fp02-lifebuoy-parallax.js`

### Runtime (exact-file delivery)

- Same two paths under `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky\wp-content\themes\shpigovsky\`

### Reports / evidence

- `REPORTS/REPORT-FP-0002-V9-06E57-FIX01-lifebuoy-motion-refinement.md`
- `REPORTS/evidence/v9-06e57-fix01-lifebuoy-motion-refinement/`
- `PROJECT-STATUS.md` (status line)

## 7. Source-to-Runtime Delivery

| File | Before (prefix) | After SHA256 | Match |
|------|-----------------|--------------|-------|
| `fp02-lifebuoy-parallax.css` | `119C0CCC…` | `2B5AB9324DFCB8F2…` | source=runtime |
| `fp02-lifebuoy-parallax.js` | `008226FC…` | `DB9EEDC24F06D263…` | source=runtime |
| `v9-style.css` | `2F7CC5AC…` | unchanged | preserved |

- No broad theme sync
- Operator CSS preserved byte-identical

## 8. Validation

Evidence: `REPORTS/evidence/v9-06e57-fix01-lifebuoy-motion-refinement/` (45 screenshots + CSV/JSON)

### Long-page matrix (Home @1440)

| State | Scale | Rotate | ≈Visible |
|-------|-------|--------|----------|
| top | 1.00 | −6° | ~32% |
| 25% | 1.10 | −4.5° | ~37% |
| 50% | 1.20 | +6° | ~56% |
| 75% | 0.96 | +16.5° | ~66% |
| bottom | 0.72 | +18° | ~72% |

- Routes long mode: Home, `/uslugi/`, section, service, О центре — PASS
- Reverse scroll: forward/reverse p50 identical — PASS
- Overflow X: **0** across matrix — PASS
- Console/page errors: **0** — PASS
- Perf 21-step scroll: **~349 ms**, 1 instance — PASS

### Short-page matrix

- Контакты / Blog: `mode=short`; Kontakty bottom ~51% visible, milder scale/rotation — PASS

### Viewports

- 1440 / 1280 / 1024 / 768 / 390 / 375 / 320 — PASS, no overflow

### Reduced motion

- Freeze at progress 0.28 top=bottom — **unchanged** from E57

## 9. Regression

| Area | Result |
|------|--------|
| Home hero | PASS |
| Floating header | PASS |
| Forms | PASS (pointer-events none on decor) |
| Galleries | PASS (present) |
| Video | PASS as untouched scope (no video element in home probe; routes 200) |
| Offcanvas | PASS |
| Horizontal overflow | PASS (0) |

## 10. Risks and Tails

- Exact “70% visible” is composition-dependent; measured ~72% at Home bottom — operator taste may still tweak X end
- Short pages intentionally milder; Kontakty peak reveal ~51% — may want slightly more if operator prefers
- Rotation amplitude (24°) is modest; taste-dependent
- Local perf only; not a production load test

## 11. Git Status

- No commit
- No push
- Exact FP-0002 theme CSS/JS + report/evidence only
- Foreign WIP elsewhere in monorepo untouched

## 12. Operator Review Checklist

- [ ] Larger circle (~+30% base)
- [ ] Reveal to ~70% on long pages
- [ ] Larger by mid-scroll (+20% scale)
- [ ] Smaller by page end (−40% from mid peak)
- [ ] Smooth rotation
- [ ] Reverse on upward scroll
- [ ] Long pages
- [ ] Short pages
- [ ] Desktop / mobile
- [ ] No interference with content
