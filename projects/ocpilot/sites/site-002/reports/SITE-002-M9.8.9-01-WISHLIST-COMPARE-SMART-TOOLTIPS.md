# REPORT — M9.8.9-01 WISHLIST COMPARE SMART TOOLTIPS

**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01`  
**Environment:** TEST — https://zpm.new-site.space/  
**Date:** 2026-06-19  
**Commit / push:** NO

---

## Authority confirmation

| Item | Value |
|------|-------|
| Knowledge Map | Read — [SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) |
| Stable checkpoint | [SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01.md](../baselines/SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01.md) |
| Site passport | [site-passport.md](../site-passport.md) |
| **Authority state** | **`SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01`** — confirmed |
| Operator Manual JS | §10 respected — live `scrollToCategorySection()` offset = **0** (pre-patch capture) |

---

## 1. Forensic Findings

### Wishlist buttons

| Layer | Location |
|-------|----------|
| **Markup PLP** | `catalog/view/theme/default/template/product/productcard.twig` — `[data-fav-toggle]` + `{% if wishlisted %}active{% endif %}` |
| **Markup PDP** | `catalog/view/theme/default/template/product/producthero.twig` — same hooks |
| **Controller PLP** | `catalog/controller/product/product_results.php` — `isWishlisted()` per card |
| **Controller PDP** | `catalog/controller/product/product.php` — `$data['wishlisted']` |
| **JS handler** | `assets/js/main.js` — block `FAVORITES / COMPARE` — click delegate on `[data-fav-toggle]` |

### Compare buttons

Same chain as wishlist with `[data-compare-toggle]` and `isCompared()` / `compared`.

### `.active` class

- **Server-rendered:** Twig adds `active` when `wishlisted` / `compared` is true on first paint.
- **Client toggled:** JS `btn.classList.toggle('active')` on click (optimistic, before AJAX completes).

### Toast / tip notifications (wishlist / compare)

- **Mechanism:** Custom popup inside button — `.zpm-tip` + `.zpm-tip__popup` + `.zpm-tip__body`.
- **Trigger classes:** `is-tip` (show), `is-remove` (remove state styling).
- **JS:** `showTip(el, text, isRemove)` in FAVORITES/COMPARE IIFE — texts **«Добавлено»** / **«Удалено»**.
- **Duration:** 3000 ms.

### «Артикул скопирован»

- **Separate IIFE** later in `main.js` (PDP/card copy block) — `[data-copy]` click → `showTip(copy, 'Артикул скопирован!')`.
- Uses same `.zpm-tip__popup` visual pattern but **different** `showTip` function scope — **not modified**.

### Duplicate copy block (historical)

Pre-patch live `main.js` contained **two** «COPY TO CLIPBOARD» sections (lines ~3944 and ~4878). Only the **second** (with `.zpm-copy__value`) is used on current PLP/PDP markup. Left untouched.

### Common tooltip mechanism

- **Visual system:** shared `.zpm-tip` CSS component (popup on `is-tip` / `is-copied`).
- **Native `title`:** not set before this pass — only `aria-label` («В избранное» / «Сравнить») in Twig.
- **No** Bootstrap/custom tooltip library.

### Notification competition (pre-fix)

Each fav/compare button had independent `_tipTimer`. Clicking fav then compare on the same card could show **two popups simultaneously** (adjacent buttons). Confirmed in code review.

---

## 2. Existing Notification System

| Feature | Element | Text | Scope |
|---------|---------|------|-------|
| Wishlist add/remove | `.zpm-tip__body` on action btn | Добавлено / Удалено | Per-button popup |
| Compare add/remove | same | Добавлено / Удалено | Per-button popup |
| Article copy | `.zpm-tip__body` on `[data-copy]` | Артикул скопирован! | Separate handler |

**Preserved:** all three notification types and texts unchanged.

**Enhanced:** before showing fav/compare popup, all **other** fav/compare popups on the page are dismissed (`hideAllActionTips`).

---

## 3. Tooltip Strategy

**Chosen approach:** native HTML `title` attribute — minimal, reliable, no new dependencies.

| State | Wishlist `title` | Compare `title` |
|-------|------------------|-----------------|
| Inactive | Добавить в избранное | Добавить к сравнению |
| Active (`.active`) | Удалить из избранного | Удалить из сравнения |

**Implementation (JS only):**

- `updateActionTitle(btn)` — sets `title` from `.active` + hook type.
- `initActionTitles()` — runs on `DOMContentLoaded` for all buttons on page.
- Called again after each toggle.

**Twig not modified** — per SITE-002 working rules (`productcard.twig` touch restriction) and because JS init covers SSR `active` state on load.

**Popup tips («Добавлено»/«Удалено»)** — unchanged; only dedup added.

---

## 4. Files Changed

| File | Action |
|------|--------|
| `assets/js/main.js` (live FTP) | **patched** — smart titles + tip dedup |
| `backups/main.js.pre-m9.8.9-01-wishlist-compare-tooltips.bak` | **created** — pre-deploy backup |
| `reports/m9.8.9-01-work/live-capture/assets__js__main.js` | **created** — FTP capture |
| `reports/m9.8.9-01-work/assets__js__main.js.patched` | **created** — patched local |
| `reports/m9.8.9-01-work/manifest-pre-20260619-122743.json` | **created** |
| `reports/m9.8.9-01-work/manifest-post-20260619-122743.json` | **created** |
| `reports/m9.8.9-01-work/m9.8.9-01-deploy-run.py` | **created** — deploy helper |
| `reports/m9.8.9-01-work/m9.8.9-01-qa-run.py` | **created** — QA helper |
| `qa/m9.8.9-01-wishlist-compare-tooltips/m9.8.9-01-qa-result.json` | **created** — QA evidence |
| `reports/SITE-002-M9.8.9-01-WISHLIST-COMPARE-SMART-TOOLTIPS.md` | **created** — this report |

**Pre-deploy SHA256:** `bd7d0f65cbefb86bd4348b7daabe53e8c9fd856be7d93760a0e10331b3d72eb1`  
**Post-deploy SHA256:** `6ad3aa524679f4d873289a52b0c20379fed9b6b095747a5ed963f6948257addc`  
**Deploy verify:** OK

---

## 5. QA Results

Playwright QA on live TEST (post-deploy):

| Page | Scenarios | Result |
|------|-----------|--------|
| **PLP Столы** (`…/stoly-premium-600/`) | titles init · fav add/remove · compare add/remove · tip dedup · article copy | **PASS** |
| **PLP Моечные ванны** (`…/moechnye-vanny/`) | same | **PASS** |
| **PDP** (SPKB-18/7-ВЛ5) | same | **PASS** |

**Title checks:**

- Inactive → «Добавить в избранное» / «Добавить к сравнению»
- After add → «Удалить из избранного» / «Удалить из сравнения»
- After remove → back to add titles

**Notification dedup:**

- Fav click → fav popup visible
- Compare click immediately after → fav popup hidden, compare popup visible

**Article copy:**

- «Артикул скопирован!» popup still appears — **PASS**

Evidence: [m9.8.9-01-qa-result.json](../qa/m9.8.9-01-wishlist-compare-tooltips/m9.8.9-01-qa-result.json)

---

## 6. Rollback

1. Restore from backup:
   ```
   backups/main.js.pre-m9.8.9-01-wishlist-compare-tooltips.bak
   → FTP upload to assets/js/main.js
   ```
2. Verify SHA256 matches pre-deploy: `bd7d0f65cbefb86bd4348b7daabe53e8c9fd856be7d93760a0e10331b3d72eb1`
3. Hard-refresh browser / bypass CDN cache if applicable
4. Tier-2: Beget full backup per site passport

---

## 7. Risks

| Risk | Level | Mitigation |
|------|-------|------------|
| Browser/CDN caches old `main.js` | Low | Post-deploy SHA verified on FTP; users may need hard refresh |
| Native `title` delay on hover | Low | Expected browser behaviour; acceptable per task spec |
| AJAX failure after optimistic toggle | Pre-existing | Not introduced by this pass — title follows `.active` like before |
| Dynamic PLP AJAX reload | Medium | **SAFE UNKNOWN** — if category grid re-renders via AJAX without full page load, `initActionTitles()` may need re-run on inject; not observed in QA URLs |
| `aria-label` still static in Twig | Low | Task scoped to `title` only; screen readers still get generic aria-label |

---

## Scope compliance

**Not touched:** wishlist/compare AJAX routes, PHP controllers, Twig templates, filter, megamenu, overlay, 1C, price logic, article copy handler.

**Git:** no commit, no push (per task).
