# FP-0002 V8 — Frontend Rules and Exceptions v1

**Date:** 2026-07-01  
**Baseline:** Operator-approved V8 source  
**Scope:** Project rules for `workspaces/fp-0002-shpigovsky-v8/`

---

## 1. SCSS architecture (project exception)

| Rule | V8 state |
|------|----------|
| All production SCSS in one file | `src/scss/style.scss` only |
| SCSS partial tree for production | **Not used** |
| New block styles | Append to `style.scss` in scoped sections |

This is a **project-specific consolidation** — not a global Website Factory mandate to abandon partials in all projects.

---

## 2. Design tokens (V8)

| Token | Status |
|-------|--------|
| `--radius-main: 30px` | **Canonical** radius token |
| `--radius-small`, `--radius-medium`, `--radius-large` | **Absent** — do not introduce |
| `--button-letter-spacing` | **Absent** |

---

## 3. Button system

| Rule | Implementation |
|------|----------------|
| Base class | `.btn` |
| Dark modifier | `.btn_dark` |
| Primary modifier | `.btn--primary` |
| Approved stack | `.btn.btn_dark.btn--primary` |
| Parallel block-specific button systems | **Prohibited** without operator approval |

Aligns with [universal-button-system-law-v1.md](../../../projects/mars-website-factory/universal-button-system-law-v1.md) at modifier level.

---

## 4. Compatibility spelling

| Class | Rule |
|-------|------|
| `.block-whith-red-line` | **Intentional misspelling** — retained for source/CSS compatibility |

Do not silently rename during unrelated work. Migration requires explicit operator charter + full regression.

---

## 5. Source authority

| Rule | Detail |
|------|--------|
| Manual operator edits | **Canonical** once saved in approved baseline |
| Casual normalization | **Prohibited** — approved visual values must not be "cleaned up" |
| New fonts, colors, dimensions | **Prohibited** without operator approval |
| Figma vs approved source | Approved source wins when operator has signed off |

---

## 6. Responsive model

| Rule | Detail |
|------|--------|
| DOM | One semantic DOM per page |
| Mobile implementation | SCSS-first (`max-width: 1024px`) |
| Mobile content duplication | **Prohibited** |
| Desktop breakpoint | `min-width: 1025px` |
| Mobile/tablet breakpoint | `max-width: 1024px` |
| Container padding | Desktop ~50px; mobile/tablet 10px; very small 5px (where applied) |

Verify mobile against mobile authority exports — not only by shrinking desktop browser.

---

## 7. Image fit / crop

- Per-block wrappers control `object-fit`, aspect ratio, and overflow.
- Gallery blocks (comfort, home-gallery) use Swiper — do not add manual scroll hacks on same axis.
- Blog inline images: full-width figures in body stream; responsive width in SCSS.

---

## 8. Component ownership

| Rule | Detail |
|------|--------|
| Shared component mutation | Do not change shared blocks for one page only |
| Page-owned adaptation | Use when CMS fields or content ownership differ |
| Early over-generalization | Avoid — promote to shared only with stable consumers |

---

## 9. JavaScript hooks

Prefer `data-*` attributes (`data-accordion`, `data-modal`, `data-offcanvas`, `data-mask`, `data-slider`, `data-fancybox`).

Do not use presentational classes as primary JS selectors when a `data-*` hook is appropriate.

---

## 10. Build and evidence

| Rule | Detail |
|------|--------|
| Stable checkpoint | Requires `npm run build` clean build |
| Incremental watch output | Insufficient for release baseline |
| `dist/` | Generated — never hand-edit |
| Evidence | Storage under `X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\` |

---

## 11. Operator approval boundary

| Rule | Detail |
|------|--------|
| Visual PASS | Operator only |
| Technical PASS | Necessary but not sufficient |
| Commit before operator visual approval | **Prohibited** (priority visual protocol) |
| Automated pixel diff | Evidence only — not final authority |

---

## 12. Design authority hierarchy (FP-0002)

1. Explicit operator decision  
2. Approved visual reference PNG (where used)  
3. Current approved source implementation  
4. Figma geometry (`Spig_v1.2.fig`)  
5. Approved shared components  
6. Audits and historical documents  

---

## 13. Project exceptions summary

| Exception | Global rule conflict | Resolution |
|-----------|---------------------|------------|
| Single `style.scss` | Gulp-starter partial mirror | FP-0002-only documented exception |
| `--radius-main` only | Universal style scale law pad/radius roles | FP-0002 calibrated values frozen |
| `uslugi.html` + `uslugi-v2.html` both exist | Single hub URL in Excel | v2 canonical for templates; legacy retained |
| Lorem in service leaf program | No filler content rule | Known demo limitation — DEFERRED polish |
| `robots: noindex` on demo pages | Production SEO | Acceptable for static demo |

---

## 14. Reusable vs project-only

Rules in §2–§11 marked as aligning with Website Factory laws are candidates for **GLOBAL_RECOMMENDED** or **GLOBAL_MANDATORY** — see [FP-0002-TO-WEBSITE-FACTORY-RULE-PROMOTION-MATRIX-v1.md](FP-0002-TO-WEBSITE-FACTORY-RULE-PROMOTION-MATRIX-v1.md).

Single-file SCSS and `--radius-main`-only are **FP0002_ONLY** unless another case confirms.

---

*FP-0002 V8 frontend rules — approved baseline.*
