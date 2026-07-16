# REPORT — FP-0002 V9-06E54-FIX01 Floating Header Background + Menu Scroll

**Wave:** V9-06E54-FIX01  
**Date:** 2026-07-16  
**Runtime:** http://shpigovsky.test/  
**Status:** Implementation + automated validation **PASS** — **awaiting operator visual acceptance** (no freeze)

---

## 1. Status

| Field | Value |
|-------|-------|
| **Overall** | **PASS** (scoped fix + reproducible scroll preservation) |
| **Operator acceptance** | **Pending** |
| **DB writes** | **0** |
| **Commit / push** | **Not performed** (per charter) |
| **Freeze** | **No** |

---

## 2. Pre-Fix Checkpoint

| Item | Value |
|------|-------|
| **Path** | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e54-fix01-before-background-menu-scroll-fix-20260716-153527\` |
| **Marker** | `BACKUP-INFO.md` |
| **Hashes** | `hashes.csv` |
| **Files** | `floating-header.php`, `fp02-floating-header.css`, `fp02-floating-header.js`, `v9-shell.js`, `header.php`, `inc/assets.php` |
| **DB dump** | Not included (file-only task) |

### Pre-fix runtime hashes (prefix)

| File | SHA256 prefix |
|------|---------------|
| `fp02-floating-header.css` | `B200CE3D…` |
| `v9-shell.js` | `05247716…` |
| `v9-style.css` (preserved) | `11A45ABE…` |

---

## 3. Root Cause

**Evidence-based diagnosis (pre-fix behavior reproduced via Playwright probe against backup-era logic):**

1. **`initOffcanvas()` had no JS scroll-lock contract.** Opening the menu only toggled `data-offcanvas-state="open"`, which activated CSS `body[data-offcanvas-state=open] { overflow: hidden; }` (from `v9-style.css` and `fp02-floating-header.css` on desktop).
2. **Applying `overflow: hidden` on a scrolled document without preserving `scrollY` resets the viewport to the top** in Chromium/WebKit when the lock is applied synchronously on open — observed as `scrollY` jumping from ~800 to `0` on Menu click from the floating header.
3. **The floating Menu opener was already a correct `<button type="button">` with `event.preventDefault()`** — not an `href="#"` anchor issue. `floating-header.php` required no semantic change.
4. **`focus()` without `preventScroll: true`** on open/close was a secondary risk for focus-induced scroll, but the primary jump was the missing scroll-lock lifecycle in `initOffcanvas()`.

**Not the cause:** hash URL change, `scrollTo(0,0)` in offcanvas code, separate offcanvas instance, or link-based opener.

---

## 4. Changes

### Background (`#e5ecf4`)

- `assets/css/fp02-floating-header.css` — `.fp02-floating-header { background-color: #e5ecf4; }` replaces `var(--color-surface, #fff)`.
- Validated computed `rgb(229, 236, 244)` in hidden/visible/menu-open across desktop and mobile viewports.
- Main header and offcanvas panel backgrounds unchanged.

### JS / offcanvas scroll-lock (`initOffcanvas` in `v9-shell.js`)

- Added `is-offcanvas-scroll-locked` class contract (scoped CSS in `fp02-floating-header.css`, mirrors modal overflow lock pattern).
- `lockOffcanvasBodyScroll()` — captures `scrollY` before open, applies lock class, `requestAnimationFrame` correction if drift > 1px.
- `unlockOffcanvasBodyScroll()` — removes lock class, restores saved `scrollY` on close.
- `focusOffcanvasElement(el, true)` — `focus({ preventScroll: true })` on open (close button) and close (return focus to trigger).
- Lock/unlock wired into existing `openMenu()` / `closeMenu()` — **no duplicate offcanvas lifecycle**.

### Files changed (exact scope)

| File | Change |
|------|--------|
| `assets/css/fp02-floating-header.css` | Background `#e5ecf4`; offcanvas scroll-lock CSS |
| `assets/js/v9-shell.js` | `initOffcanvas()` scroll preservation + focus guard |

**Not changed:** `floating-header.php`, `fp02-floating-header.js`, `header.php`, `inc/assets.php`, `v9-style.css`.

---

## 5. Scroll Preservation Proof

Automated probe: `REPORTS/evidence/v9-06e54-fix01-floating-header/scroll-probe-results.json`

| Viewport | Route | Scroll before | Scroll after open | Scroll after close | Δ open | Δ close | URL/hash | Result |
|----------|-------|---------------|-------------------|--------------------|--------|---------|----------|--------|
| 1440×900 | `/` | 800 | 800 | 800 | 0 | 0 | unchanged / no hash | **PASS** |
| 1280×800 | `/` | 800 | 800 | 800 | 0 | 0 | unchanged / no hash | **PASS** |
| 1024×768 | `/` | 800 | 800 | 800 | 0 | 0 | unchanged / no hash | **PASS** |
| 390×844 | `/` | 700 | 700 | 700 | 0 | 0 | unchanged / no hash | **PASS** |
| 375×812 | `/` | 700 | 700 | 700 | 0 | 0 | unchanged / no hash | **PASS** |
| 320×568 | `/` | 700 | 700 | 700 | 0 | 0 | unchanged / no hash | **PASS** |

Visual marker delta on open: **0px** all viewports (content position stable).

Escape close: validated in probe (scroll restored). Overlay close: same `closeMenu()` path — no separate regression failure expected.

---

## 6. Responsive Validation

| Tier | Viewports | Background | Menu open | Scroll | Result |
|------|-----------|------------|-----------|--------|--------|
| Desktop | 1440, 1280, 1024 | `rgb(229,236,244)` | offcanvas open | preserved | **PASS** |
| Mobile | 390, 375, 320 | `rgb(229,236,244)` | offcanvas open | preserved | **PASS** |

---

## 7. Regression

| Route | HTTP | Floating visible @ scroll | Menu scroll jump | Result |
|-------|------|---------------------------|------------------|--------|
| `/` | 200 | yes | no | **PASS** |
| `/uslugi/` | 200 | yes | no | **PASS** |
| `/o-centre/` | 200 | yes | no | **PASS** |
| `/kontakty/` | 200 | yes | no | **PASS** |
| `/blog/` | 200 | yes | no | **PASS** |
| `/uslugi/zavisimosti/` (section) | 200 | — | — | **PASS** (HTTP smoke) |

- Primary header: unchanged (no edits).
- Offcanvas: single `#mobile-menu` reused; Escape + overlay paths intact.
- JS page errors in probe: **0**
- PHP warnings: not observed in HTTP responses (file-only task).

---

## 8. Source → Runtime Delivery

| File | Source SHA256 | Runtime match |
|------|---------------|---------------|
| `fp02-floating-header.css` | `1468248F826A2CA0D56618CEA3CD4F6A04ED025C1EF015C83AAB9B8BA950245E` | **yes** |
| `v9-shell.js` | `470165633200C1EB68862C91069F5415A1BF1BC569FFD7D75F45B63F22AE9D30` | **yes** |
| `v9-style.css` (untouched) | prefix `11A45ABE` | **preserved** |

Only 2 files copied to runtime. No broad theme sync.

---

## 9. Evidence

**Path:** `REPORTS/evidence/v9-06e54-fix01-floating-header/`

| Artifact | Description |
|----------|-------------|
| `desktop-1440-home-floating-bg.png` | Desktop floating header with `#e5ecf4` background |
| `mobile-390-home-floating-bg.png` | Mobile floating header with new background |
| `desktop-1440-home-menu-open.png` | Desktop menu open after deep scroll |
| `mobile-390-home-menu-open.png` | Mobile menu open after deep scroll |
| `scroll-probe-results.json` | Full scroll/URL/viewport probe |
| `scroll-probe-results.csv` | Tabular probe export |

---

## 10. Git Status

- **Commit:** not performed  
- **Push:** not performed  
- **Scope:** FP-0002 E54-FIX01 only (2 theme files)  
- **Foreign WIP:** untouched  

---

## 11. Operator Review (Андрей)

Please verify visually on http://shpigovsky.test/:

1. Floating header background is **`#e5ecf4`** (not white) on desktop and mobile.
2. Overall floating header appearance unchanged except background colour.
3. After scrolling down (>500px desktop / >650px mobile), **Menu** opens offcanvas **without page jump**.
4. After closing (Escape or overlay), page remains at the same scroll position.

No freeze, commit, or push until operator acceptance.
