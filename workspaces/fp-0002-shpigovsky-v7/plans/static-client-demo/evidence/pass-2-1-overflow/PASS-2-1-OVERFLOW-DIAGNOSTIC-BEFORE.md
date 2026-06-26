# PASS 2.1 Overflow Diagnostic — BEFORE

## Summary

- Total probes: 110 (11 pages × 10 widths)
- Overflow detected: 60
- REAL_LAYOUT_OVERFLOW: 60
- VALIDATOR_FALSE_POSITIVE: 0
- Canonical compiled pages (`uslugi-v2.html`, `usluga-podrazdel-v1.html`, `usluga-konechnaya-v1.html`): **0 overflow**
- Generated nested instances (hub, subdivisions, leaves): **overflow at all widths**

## Root cause

`rewriteAssetPathsToRoot()` in `tools/static-demo-generator/path-utils.js` used a negative lookbehind that **skipped** `src="assets/…"` and `href="assets/…"` attributes. Nested generated pages kept relative `assets/` URLs, resolving to `/uslugi/.../assets/` (404).

Without stylesheet and images, layout collapsed to raw HTML `width` attributes on gallery/program images (e.g. 2201px), producing reproducible `document.documentElement.scrollWidth > clientWidth` and horizontal scroll.

## Top offenders (services-hub-generated @ 320)

| Selector | Right | Width | Classification |
| -------- | ----: | ----: | -------------- |
| `a.home-comfort__gallery-item--wide` | 2209 | 2201 | REAL_LAYOUT_OVERFLOW |
| `img.home-comfort__gallery-image` | 2209 | 2201 | REAL_LAYOUT_OVERFLOW |
| `img.services-program-v2__item-image` | 1640 | 1632 | REAL_LAYOUT_OVERFLOW |

## Classification

- REAL_LAYOUT_OVERFLOW — missing root asset rewrite on nested outputs (not slider/modal/off-canvas)
- CSS-only fix insufficient — stylesheet itself failed to load on nested pages
