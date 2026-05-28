# REPORT — V5 Contact CTA Background Image Removal

**Workspace:** `workspaces/triumph-manipulator-landing-v5/`  
**Lane:** A — Frontend Production / Micro Fix  
**Date:** 2026-05-24  
**Build:** `npm run build` — **PASS** (exit 0, ~1.1s)  
**Git:** no commit, no push (per task)

---

## Summary

Removed the reconstruction truck background image from `.contact-cta`. The section keeps the dark gradient overlay and base night color (`#090c27` via `t.$color-night`). Padding, grid, form block, typography, and other background sections were not modified.

---

## File changed

| File | Change |
|------|--------|
| `src/scss/sections/_final-contact-cta.scss` | Dropped `url('../img/reconstruction/v1-04-contact-truck.png')` from `.contact-cta` `background` stack |

**Not touched:** HTML partials, `.contact-form` styles, typography-protection, `_v5-page01-overrides.scss`, other section backgrounds.

---

## Background — before / after

### Before (`.contact-cta`, desktop)

```scss
background:
    linear-gradient(90deg, rgba(9, 12, 39, 0.98) 0%, rgba(9, 12, 39, 0.88) 52%, rgba(9, 12, 39, 0.5) 100%),
    url('../img/reconstruction/v1-04-contact-truck.png') right center / auto 88% no-repeat,
    #090c27; /* t.$color-night */
```

### After (`.contact-cta`, desktop)

```scss
background:
    linear-gradient(90deg, rgba(9, 12, 39, 0.98) 0%, rgba(9, 12, 39, 0.88) 52%, rgba(9, 12, 39, 0.5) 100%),
    #090c27; /* t.$color-night */
```

**Note:** `@media (max-width: 980px)` already used gradient + base color only (no image); unchanged.

---

## Build status

```
npm run build  →  exit 0
gulp build: cleanDist, html, styles, scripts, images, favicon, vendorFontawesome, fonts — all finished
```

---

## Dist verification

| Check | Result |
|-------|--------|
| `dist/assets/css/style.css` contains `v1-04-contact-truck` | **PASS** — 0 matches |
| `.contact-cta` compiled background | **PASS** — gradient + `#090c27` only |
| Section stays dark | **PASS** — `rgba(9, 12, 39, …)` gradient + `#090c27` |
| Form layout preserved | **PASS** — `.contact-cta__grid` still `grid-template-columns: minmax(0, 1fr) minmax(360px, 470px)`; `padding-block` unchanged |

Compiled block (excerpt from `dist/assets/css/style.css`):

```css
.contact-cta {
  position: relative;
  overflow: hidden;
  padding-block: clamp(58px, 6vw, 94px);
  background: linear-gradient(90deg, rgba(9, 12, 39, 0.98) 0%, rgba(9, 12, 39, 0.88) 52%, rgba(9, 12, 39, 0.5) 100%), #090c27;
  color: #f7f9fc;
}
```

No `url(...)` in `.contact-cta` background in dist CSS or HTML from this build.

---

## SAFE UNKNOWN

- **Live browser QA** not run in this session — human check recommended (see path below).
- **Orphan asset:** `dist/assets/img/reconstruction/v1-04-contact-truck.png` may still be copied by `gulp images` because the file remains under `src/img/`; it is no longer referenced by CSS. Removing the file from `src/img/` was **out of scope** for this task.
- **PPC / multi-page dist:** default build emits `dist/index.html` (active page: `v5-ppc/zakaz`); other PPC HTML variants share the same SCSS — fix applies when those pages are built — **UNKNOWN** if all 14 PPC targets are in the default gulp output.

---

## Browser QA path

1. Open `workspaces/triumph-manipulator-landing-v5/dist/index.html` (`file://` or local static server).
2. Scroll to `#contacts` (`.contact-cta`).
3. Confirm: no truck image on the right; dark navy background with left-to-right gradient; contact copy + form grid unchanged.
4. Resize: **980px** (stack to single column, background without image), **760px** (mobile padding), **320 / 375 / 1440px** optional.
5. DevTools → Network: no request for `v1-04-contact-truck.png` when viewing contact section (unless cached from prior session).

---

## Git

No commit. No push.
