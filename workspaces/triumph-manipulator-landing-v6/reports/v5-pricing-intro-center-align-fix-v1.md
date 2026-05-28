# REPORT — V5 Pricing Intro Center Align Fix

**Workspace:** `workspaces/triumph-manipulator-landing-v5/`  
**Lane:** A — Frontend Production / Micro Fix  
**Date:** 2026-05-24  
**Build:** `npm run build` — **PASS** (exit 0, ~1.25s)  
**Git:** no commit, no push (per task)

---

## Problem

In the pricing section (`#pricing`), the intro line under the H2 — *«Точную цену рассчитываем по вашей задаче заранее — без скрытых доплат после выезда.»* — was not visually centered after the Pass 3 forensic layout fixes, while the H2 and card grid were acceptable.

---

## Fix

| Item | Value |
|------|--------|
| **Selector changed** | `.pricing-factors .section-heading--center .section-lead` |
| **File changed** | `src/scss/sections/_v5-pricing-factors.scss` |
| **Properties added** | `text-align: center;` `margin-left: auto;` `margin-right: auto;` |
| **Preserved** | Global `.section-lead` `max-width: 620px` (from `src/scss/base/_base.scss`) — not overridden |
| **Not changed** | H2 (`.section-title`), `.pricing-factors__list` grid, hover/interactions, global typography |

---

## Dist CSS verification

Compiled rule in `dist/assets/css/style.css` (minified block ~line 4274):

```css
.pricing-factors .section-heading--center .section-lead {
  text-align: center;
  margin-left: auto;
  margin-right: auto;
}
```

Scope check: selector is scoped to **pricing section intro only**; other `.section-lead` instances (FAQ, trust, etc.) are unaffected.

---

## SAFE UNKNOWN

- **Live browser pixel check** not run in this session — human QA recommended at 320 / 375 / 760 / 1180 / 1440 px.
- **PPC-only HTML variants** (14 partials under `v5-ppc/*/screen-02c-pricing-factors.html`) share the same markup class stack; fix applies via shared SCSS when those pages are built — **UNKNOWN** whether all PPC dist targets are in the default `gulp build` output (current build emits `dist/index.html` only).

---

## Browser QA path

1. Open `workspaces/triumph-manipulator-landing-v5/dist/index.html` (`file://` or local static server).
2. Scroll to section `#pricing` (class `pricing-factors`).
3. Confirm H2 remains unchanged; confirm `.section-lead` under «Стоимость» is centered; confirm factor cards grid unchanged.
4. Optional: resize to 320, 375, 760, 1180, 1440 px and re-check intro alignment.

---

## Changed files

| File | Action |
|------|--------|
| `src/scss/sections/_v5-pricing-factors.scss` | Added pricing intro center-align rule |
| `reports/v5-pricing-intro-center-align-fix-v1.md` | This report |

**Generated (build):** `dist/assets/css/style.css`, `dist/index.html`
