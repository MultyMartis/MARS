# FP-0002 V6 SECTION-002 HTML REVIEW

**Date:** 2026-06-22  
**Partial:** `src/partials/sections/intro-programs.html`

## Structure

PASS — one `section.intro-programs` with four semantic groups matching grounded internal groups.

## Semantics

PASS — headings `h2`/`h3`, `blockquote` for founder quote, `ul/li` for cards and lists, `figure` for founder media slot.

## Exact text

PASS — extracted from JPG evidence crops; Russian typography with `&nbsp;` where applied.

## Asset bindings

PARTIAL — `data-asset-required` on founder figure and clinical grid items; no placeholder images.

## Accessibility

PASS — `aria-labelledby`, `visually-hidden` figcaption, decorative icons `aria-hidden`.

## BEM

PASS — block `intro-programs`, elements `intro-programs__*`.

## Absence of styles

PASS — no inline styles.

## Absence of JS

PASS — no hooks; static accordion markup.

## Token-ready class structure

PASS — classes map to SCSS partial.

---

## Verdict

```text
SECTION-002 HTML — APPROVED FOR SCSS
```
