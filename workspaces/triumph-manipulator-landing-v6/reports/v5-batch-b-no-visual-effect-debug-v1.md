# V5 Batch B No Visual Effect Debug

**Date:** 2026-05-24  
**Scope:** `workspaces/triumph-manipulator-landing-v5/` only  
**Page under test:** `dist/index.html` (`data-page-type="ppc-zakaz-manip"`, zakaz / page-01)  
**Baseline reference:** Batch B report `v5-production-hardening-batch-b-report-v1.md`

---

## Build output status

| Artifact | Path | Before `npm run build` | After `npm run build` |
|----------|------|------------------------|------------------------|
| HTML | `dist/index.html` | 2026-05-24 05:40:25 (51 362 B) | 2026-05-24 05:48:54 |
| CSS | `dist/assets/css/style.css` | 2026-05-24 05:40:25 (103 745 B) | 2026-05-24 05:48:54 |

- `npm run build` (gulp `cleanDist` → html/styles/scripts/…) **completed successfully**.
- `style.css` **timestamp and content regenerated** (`CHANGED: True`).

**Conclusion:** Build pipeline is working; dist is not stale relative to source at investigation time.

---

## CSS path status

From `dist/index.html` `<head>`:

```html
<link rel="stylesheet" href="assets/css/style.css">
```

- Relative path `assets/css/style.css` — **correct** for `file:///…/dist/index.html`.
- No alternate/legacy stylesheet linked in HTML.
- Font Awesome vendor CSS is separate (`assets/vendor/fontawesome/css/screen-icons.css`); does not replace `style.css`.

**Conclusion:** HTML loads the expected compiled bundle.

---

## Batch B rules in dist CSS

String presence check on `dist/assets/css/style.css` (all **present**):

| Pattern | In dist? |
|---------|----------|
| `overflow-wrap: break-word` | Yes |
| `word-break: normal` | Yes |
| `.hero--v5 .hero__title` | Yes |
| `.machine-showcase__title` | Yes |
| `.site-header` | Yes |
| `.machine-showcase__specs` | Yes |
| `.faq` / `.faq-item` | Yes |
| `@media (max-width: 420px)` | Yes |
| `@media (max-width: 760px)` | Yes |

Git diff vs baseline `f86dd59` shows **11 SCSS files / +130 −22 lines** compiled into dist (matches Batch B report).

**Conclusion:** Batch B rules **are compiled into dist** — not an SCSS import/build omission.

---

## Matching selector check

### HTML (`dist/index.html`) vs Batch B SCSS

| Area | Expected (audit list) | Actual markup | Match for Batch B? |
|------|----------------------|---------------|-------------------|
| Page type | — | `body data-page-type="ppc-zakaz-manip"` | Yes (PPC overrides apply via `body[data-page-type^=ppc-]`) |
| Hero | `.hero--v5 .hero__title` | `<section class="hero hero--v5">` + `<h1 class="hero__title">` | **Yes** |
| Specs title | `.machine-showcase__title` | `<h2 class="machine-showcase__title">` | **Yes** |
| Specs values | `.machine-showcase__specs dd` | `<dl class="machine-showcase__specs">` + `<dd>` | **Yes** |
| Section H2 | `.section-title` | `<h2 class="section-title">` | **Yes** |
| Trust | `.trust__title` | `<h2 class="trust__title">` | **Yes** |
| Contact lead | `.contact-cta h2` | `<h2 id="contact-title">` inside `.contact-cta` | **Yes** |
| Header nav | `.site-header__nav a` | `<a class="site-header__nav-link">` inside `.site-header__nav` | **Partial** — SCSS targets `.site-header__nav-link` (equivalent intent) |
| FAQ Q/A | `.faq__question` / `.faq__answer` | `<details class="faq-item"><summary>…</summary><div class="faq-item__body">` | **Mismatch on audit names only** — Batch B changed `.faq-item summary` and `.faq-item__body p` (correct for markup) |
| Buttons | `.button` | `class="button button--primary"` etc. | **Yes** |

**Conclusion:** No blocking class/HTML mismatch for implemented Batch B rules. Audit checklist used legacy FAQ/header selector names; real DOM uses `faq-item` / `site-header__nav-link`.

---

## Overrides found

Cascade review on compiled `style.css` (last relevant declarations per target):

### `.hero--v5 .hero__title`

| Viewport | Winning rule (summary) | Batch B effect |
|----------|------------------------|----------------|
| Desktop (wide) | `font-size: clamp(40px, 4.8vw, 82px); line-height: 1.06` (base) | **Unchanged** vs pre-batch at typical desktop widths |
| ≤761px | Smaller clamps, `line-height: 1.12` | Batch B added **420px** band + `line-height: 1.12` instead of fixed `42px` at **320px** only |
| ≤320px | `line-height: 1.12` (was `line-height: 42px`) | Visible only at very narrow width |

No later rule nullifies mobile hero title rules; desktop simply never enters those media blocks.

### `.machine-showcase__specs dd`

| Viewport | Winning `white-space` / wrap | Notes |
|----------|-------------------------------|-------|
| ≤760px | `white-space: normal; overflow-wrap: break-word` | Batch B mobile behavior **active** |
| ≥761px | `white-space: nowrap` (intentional desktop) | **Unchanged look** on desktop — by design |

### `.site-header__nav-link`

| Viewport | Visibility | Batch B impact |
|----------|--------------|----------------|
| **>1240px** | Inline nav visible; `overflow-wrap: break-word`, no `nowrap` | Subtle unless nav wraps / clips |
| **≤1240px** | `.site-header__nav { display: none }` | **Batch B nav-link rules not applied to visible UI** — burger drawer uses `.site-header__drawer-link` (not updated in Batch B) |

### `.button`

| Viewport | Key props | Notes |
|----------|-----------|-------|
| ≤760px | `white-space: normal; overflow-wrap: break-word; line-height: calc(1em + 4px)` | Visible only if label wraps or overflowed before |
| Desktop | Prior button sizing/colors dominate | **Little or no visible delta** at full width |

### `.faq-item summary` / `.faq-item__body p`

- Rules present with `line-height: calc(1em + 4px)` and **420px** padding tweaks.
- PPC grouped rule `body[data-page-type^=ppc-] … { min-width: 0; max-width: 100% }` comes **later** but does not remove line-height/wrap — **no harmful override**.
- `.faq__question` / `.faq__answer` selectors: **0 rules** in CSS (not used in HTML).

### `.section-title` / `.trust__title`

- Typography via `section-h2-mobile` mixin: mobile/`420px`/`375px` bands in dist.
- At **desktop width**, base H2 sizes unchanged — **expected no visible change**.

**Conclusion:** Overrides are not “breaking” Batch B. The dominant pattern is **media-gated rules** (≤760 / ≤420) and **desktop-intentional** values (`nowrap` on spec `dd` ≥761px). Inline header nav changes are **inactive** below 1240px.

---

## Class mismatch found

| Item | Severity |
|------|----------|
| `.faq__question` / `.faq__answer` in audit checklist | **Informational** — markup uses `.faq-item` / `summary` / `.faq-item__body`; SCSS matches markup |
| `.site-header__nav a` vs `.site-header__nav-link` | **Informational** — SCSS uses `__nav-link`; matches HTML |
| **No blocking mismatch** that would prevent Batch B CSS from applying to live DOM | — |

---

## Root cause

**Primary (most likely):** Batch B is a **mobile/narrow-viewport typography and overflow-hardening** pass. Most deltas live inside `@media (max-width: 760px)` and `@media (max-width: 420px)`, or only matter when text **overflows** (`overflow-wrap`, removed `nowrap`). Opening `file:///…/dist/index.html` at **default desktop width** shows **little or no perceptible change** — this matches the implementation, not a failed build.

**Secondary:**

1. **Header:** Inline `.site-header__nav-link` changes apply only when viewport **>1240px** (nav hidden below that; mobile menu uses **drawer links**, not updated in Batch B).
2. **Subtle deltas:** `line-height: calc(1em + 4px)` vs fixed px, and `break-word` vs `anywhere`, are **low-contrast** unless copy clips.
3. **Operator environment (SAFE UNKNOWN):** `file://` + browser cache may serve an older `style.css` until hard reload — dist on disk was verified fresh after build.

**Ruled out:**

- Stale dist / build not updating CSS  
- Wrong stylesheet path in HTML  
- Batch B rules missing from compiled CSS  
- Wrong hero/specs/button classes on `index.html`

---

## Recommended minimal fix

**Do not redesign.** After operator confirms viewport:

1. **Operator QA (required):** DevTools → device mode **375×812** and **390×844**; hard reload (`Ctrl+Shift+R`). Re-check hero H1, spec `dd`, FAQ, long CTA labels.
2. **If header wrap was the concern at tablet/mobile:** extend Batch B wrap/line-height to `.site-header__drawer-link` (and drawer phone/CTA if needed) — minimal SCSS-only follow-up.
3. **If desktop spec `dd` nowrap still clips at 1024–1180:** narrow follow-up in `_screen-02-prices.scss` per Batch B SAFE UNKNOWN (audit note).

**No code change applied in this debug pass** (per task: root-cause first).

---

## SAFE UNKNOWN

- Whether operator tested at **desktop vs ≤420px** — not recorded.
- Whether browser used **cached** `style.css` on `file://` — not verified in browser.
- Live before/after screenshot diff at 375px — not captured in this pass.
- Whether pre-batch page already showed acceptable wrap at operator’s viewport (Batch B may fix edge cases only).

---

*Debug pass: build/CSS/HTML/cascade only. No commits, no layout redesign.*
