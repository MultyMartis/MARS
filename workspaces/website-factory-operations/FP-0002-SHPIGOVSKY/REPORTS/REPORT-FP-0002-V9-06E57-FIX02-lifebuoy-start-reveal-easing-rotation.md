# REPORT — FP-0002 V9-06E57-FIX02 Lifebuoy Start, Reveal, Easing and Rotation

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

- **Path:** `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e57-fix02-before-lifebuoy-start-reveal-easing-rotation-20260716-220628\`
- **Files:** source/runtime lifebuoy CSS/JS, `v9-style` hash record, lifebuoy asset hash record, `hashes.csv`, `operator-change-manifest.csv`, `BACKUP-INFO.md`
- **Marker:** V9-06E57-FIX02; lifebuoy motion tuning only; operator CSS/HTML protected; DB writes prohibited; no broad sync; no commit/push/freeze

## 3. Operator Changes Preserved

- Pre-wave source↔runtime for scoped lifebuoy + operator CSS: **MATCH** (no promote)
- **Promoted files:** none
- **Protected baseline:** `v9-style.css` SHA256 `2F7CC5ACE7E6718ADE81B9871FBE73B62D2D0D3AE5B5C1818E2F9266D374793E` (unchanged)
- **Lifebuoy asset:** `B4F1C9F6…` unchanged
- Unresolved drift: none

## 4. Root Cause of Initial Sluggishness

### Previous (FIX01)

- X/Y/rotate used `easeInOutCubic`. First half is `4t³` → **derivative at t=0 is 0**.
- Scale used Hermite `smoothstep` per phase → **derivative at t=0 is also 0**.
- Together this produced a visible “waiting” dead zone at the start of scroll.
- CSS transitions, rAF batching, and scroll thresholds were inspected and were **not** the lag source.

### Replacement (FIX02)

- X/Y/rotate → `easeOutCubic` = `1-(1-t)³` with **de/dt(0)=3** (immediate response, still smooth finish).
- Scale → piecewise **linear** on raw effective `t` (non-zero initial slope); endpoints unchanged `1.00 → 1.20 → 0.72`.
- Measured at ~2% scroll: ΔX ≈ +3.23%, Δscale ≈ +0.008, Δrotate ≈ +1.69° — motion starts immediately.

## 5. Motion Changes

| Item | Before (FIX01) | After (FIX02) |
|------|----------------|---------------|
| Top reveal | ~30% (X −70%) | **~50%** (X −50%; measured **50.0%**) |
| Long max reveal | ~70–72% (X −30%) | **~80%** (X −20%; measured Home bottom **~81.1%**) |
| Scale endpoints | 1.00 → 1.20 → 0.72 | unchanged |
| Scale response | smoothstep dead zone | linear — immediate |
| Long rotation | −6° → +18° | **−7.2° → +21.6°** (+20%) |
| Short rotation | −3° → +10° | **−3.6° → +12°** (+20%) |
| Short max reveal | milder (~58%) | milder (~59%; X end −38%) |
| Long/short threshold | `scrollable < max(2400, 4×vh)` | unchanged |
| Reduced motion | freeze t=0.28 | unchanged |

## 6. Motion Metrics

Representative Home long @ 1440×900:

| mode | viewport | progress | X | Y | scale | rotation | visible % | result |
|------|----------|----------|---|---|-------|----------|-----------|--------|
| long | 1440×900 | 0% | −50.000% | −12.000vh | 1.0000 | −7.200° | **50.0** | PASS |
| long | 1440×900 | ~2% | −46.769% | −8.240vh | 1.0080 | −5.508° | 52.9 | PASS immediate |
| long | 1440×900 | 10% | −35.850% | 5.348vh | 1.0400 | +0.606° | 63.5 | PASS |
| long | 1440×900 | 25% | −24.895% | 25.003vh | 1.1000 | +9.451° | 69.8 | PASS |
| long | 1440×900 | 50% | −20.689% | 44.000vh | 1.2000 | +18.000° | 69.3 | PASS |
| long | 1440×900 | 75% | −20.076% | 51.000vh | 0.9600 | +21.150° | 74.0 | PASS |
| long | 1440×900 | ~98% | −20.000% | 51.999vh | 0.7392 | +21.600° | **81.1** | PASS ~80% |
| long | 1440×900 | reverse 50% | −20.689% | 44.000vh | 1.2000 | +18.000° | — | PASS = forward |

Short Kontakty @ 1440×900: start 50% visible; bottom ~59%; mode `short`; no overshoot to 80%.

Full CSV/JSON: `REPORTS/evidence/v9-06e57-fix02-lifebuoy-start-reveal-easing-rotation/`.

## 7. Exact Files Changed

### Canonical source

- `WORDPRESS/theme/shpigovsky/assets/css/fp02-lifebuoy-parallax.css`
- `WORDPRESS/theme/shpigovsky/assets/js/fp02-lifebuoy-parallax.js`

### Runtime

- `wp-content/themes/shpigovsky/assets/css/fp02-lifebuoy-parallax.css`
- `wp-content/themes/shpigovsky/assets/js/fp02-lifebuoy-parallax.js`

### Reports / evidence

- `REPORTS/REPORT-FP-0002-V9-06E57-FIX02-lifebuoy-start-reveal-easing-rotation.md`
- `REPORTS/evidence/v9-06e57-fix02-lifebuoy-start-reveal-easing-rotation/**`
- `PROJECT-STATUS.md`

## 8. Source-to-Runtime Delivery

| file | before | after | match |
|------|--------|-------|-------|
| CSS | `2B5AB932…` | `51DFD575…` | source=runtime |
| JS | `DB9EEDC2…` | `DCF1357B…` | source=runtime |
| v9-style | `2F7CC5AC…` | `2F7CC5AC…` | preserved |
| lifebuoy.webp | `B4F1C9F6…` | `B4F1C9F6…` | unchanged |

- Exact-file delivery only (2 files)
- No broad theme sync
- Operator CSS preserved
- Asset unchanged

## 9. Validation

- Long pages (`/`, `/uslugi/`, section, service, `/o-centre/`): mode `long`; top ~50%; bottom ~80–81%
- Short pages (`/kontakty/`, `/blog/`): mode `short`; milder reveal (~59%)
- Immediate response at ~2% scroll: confirmed (X/scale/rotate deltas non-zero)
- Reverse: forward p50 ≡ reverse p50
- Viewports 1440…320: matrix + screenshots captured
- JS console errors: **0**
- Overflow-X true samples: **0**
- Screenshots: 48

## 10. Regression

| Surface | Result |
|---------|--------|
| Home hero | PASS |
| Floating header | PASS |
| Offcanvas trigger | PASS |
| Forms | PASS |
| Galleries | PASS |
| Video | N/A on Home probe (no `<video>` in DOM) |
| Lifebuoy below content / `pointer-events: none` | PASS |

## 11. Risks and Tails

- Taste-based: easeOutCubic front-loads travel (by mid-scroll X is already near end envelope); operator may want a slightly softer mid if motion feels “too eager.”
- Short pages intentionally stay below 80% reveal.
- Viewport-specific: mobile widths still capped (`min(100vw, …)`); measured no horizontal overflow.
- Residual: Home video element absent in regression probe (unchanged vs prior waves).

## 12. Git Status

- No commit
- No push
- Exact FP-0002 scope only
- Foreign WIP in monorepo untouched

## 13. Operator Review Checklist

- [ ] ~50% visible at page start
- [ ] Immediate motion from first scroll (no lag)
- [ ] ~80% visible near end of long pages
- [ ] Stronger smooth rotation (~+20%)
- [ ] Smooth reverse to identical states
- [ ] Long vs short page behavior acceptable
- [ ] Desktop + mobile OK
- [ ] No content / control interference

---

**Evidence:** `REPORTS/evidence/v9-06e57-fix02-lifebuoy-start-reveal-easing-rotation/`  
**Checkpoint:** `v9-06e57-fix02-before-lifebuoy-start-reveal-easing-rotation-20260716-220628`
