# FP-0002 V6 FOOTER HTML REVIEW

**Date:** 2026-06-22  
**Partial:** `src/partials/layout/footer.html`  
**Gate:** Footer HTML — pre-SCSS

---

## Semantics

PASS — `footer.site-footer` with three logical groups (`__top`, `__main`, `__legal`). Contact data in structured groups; navigation in three `nav` elements with distinct `aria-label`.

## Exact texts

PASS — all strings match JPG evidence crops (`specifications/footer/evidence/`). Placeholder nav copy `Название раздела` / `Название` preserved as in mockup.

## Russian typography

PASS — `и&nbsp;Московская`, `с&nbsp;обработкой`, `на&nbsp;Info@shpigovsky.ru`.

## Links

| Element | Format |
|---------|--------|
| Phone | `tel:+79251836464` |
| Email | `mailto:Info@shpigovsky.ru` |
| Nav / legal | `data-safe-unknown` (no `href="#"`) |

## Phone formats

PASS — display `8 (925) 183-64-64`, tel E.164 `+79251836464`.

## Asset bindings

| Asset | Binding |
|-------|---------|
| logo.svg | PASS |
| telegram.svg | PASS |
| whatsapp.svg | PASS |
| youtube | `data-asset-required="footer-social-youtube"` — ASSET_REQUIRED |

## Accessibility

PASS — messenger `aria-label`; decorative FA icons `aria-hidden="true"`; nav `aria-label` per column.

## BEM

PASS — block `site-footer`, elements `site-footer__*`.

## Absence of styles

PASS — no inline styles.

## Absence of JS

PASS — no `data-accordion`, sliders, or new JS hooks.

## Footer-only scope

PASS — Header/Hero partials untouched.

---

## Verdict

```text
FOOTER HTML — APPROVED FOR SCSS
```
