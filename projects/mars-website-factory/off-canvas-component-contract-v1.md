# Website Factory — Off-Canvas Component Contract v1

**Status:** ACCEPTED (minimal reusable contract)  
**Date:** 2026-06-23  
**Scope:** Gulp delivery projects — mobile navigation panel pattern  
**Authority:** FP-0002 V6 responsive phase evidence

**Not:** runtime component library, npm package, CMS module, automated enforcement

---

## 1. Purpose

Minimal normative contract for a **right-side off-canvas mobile menu** in Website Factory Gulp projects. Behavior is **vanilla JS** in project `main.js`; styling in single project `style.scss`.

---

## 2. Markup contract (minimum)

```html
<div class="offcanvas" id="mobile-menu" data-offcanvas data-offcanvas-state="closed" aria-hidden="true">
  <div class="offcanvas__overlay" data-offcanvas-overlay></div>
  <div class="offcanvas__panel" data-offcanvas-panel role="dialog" aria-modal="true" aria-label="Мобильное меню">
    <button type="button" data-offcanvas-close aria-label="Закрыть меню">…</button>
    <!-- nav + contacts -->
  </div>
</div>
```

Open trigger (outside panel):

```html
<button type="button" data-offcanvas-open aria-controls="mobile-menu" aria-expanded="false" aria-label="Открыть меню">…</button>
```

---

## 3. Required data hooks

| Hook | Role |
|------|------|
| `data-offcanvas` | Root component |
| `data-offcanvas-open` | Open trigger(s) |
| `data-offcanvas-close` | Close control(s) |
| `data-offcanvas-overlay` | Dimmed backdrop |
| `data-offcanvas-panel` | Sliding panel / dialog |
| `data-offcanvas-state` | Functional state on root (`open` / `closed`) |

Optional: `data-offcanvas-state` on `<body>` for scroll lock (set by JS).

**Forbidden:** binding open/close behavior to presentational CSS classes, DOM nesting, or `nth-child`.

---

## 4. ARIA states

| State | Closed | Open |
|-------|--------|------|
| Root `aria-hidden` | `true` | `false` |
| Trigger `aria-expanded` | `false` | `true` |
| Panel | `role="dialog"` `aria-modal="true"` | same |

Do not set `aria-hidden="true"` on an element that currently holds focus.

---

## 5. Behavior minimum

- Open on `[data-offcanvas-open]` click
- Close on `[data-offcanvas-close]`, overlay click (dimmed area), `Escape`
- Body scroll lock while open (`body[data-offcanvas-state='open'] { overflow: hidden; }`)
- Focus moves into panel on open (close button or first focusable)
- Focus returns to open trigger on close
- Tab / Shift+Tab focus trap inside open panel
- Resize to desktop breakpoint: force close, remove scroll lock, reset ARIA
- Default HTML/CSS state: **closed** (no flash before JS)
- `prefers-reduced-motion: reduce`: minimal transition duration

---

## 6. Responsive boundary

Desktop-first projects: off-canvas active at **`max-width: 1024px`** unless project spec states otherwise. Desktop (`min-width: 1025px`) must not show mobile bar or open panel; CSS safety net recommended.

---

## 7. Reference implementation

- `workspaces/fp-0002-shpigovsky-v6/src/partials/layout/header.html`
- `workspaces/fp-0002-shpigovsky-v6/src/js/main.js`
- `workspaces/fp-0002-shpigovsky-v6/src/scss/style.scss` (sections 12 + Responsive)
- Review: `workspaces/fp-0002-shpigovsky-v6/reviews/responsive/FP-0002-V6-MOBILE-HEADER-OFFCANVAS-FOOTER-REVIEW.md`

---

## 8. QA matrix (operator)

| Test | Expected |
|------|----------|
| Open | panel visible, ARIA synced |
| Overlay / close / Escape | closed, focus restored |
| Body scroll | locked open, restored closed |
| Desktop width while open | forced closed |
| Hidden panel | not tab-focusable when closed |

Automated helper: `reviews/responsive/_offcanvas-functional-test.py` (Playwright, FP-0002).
