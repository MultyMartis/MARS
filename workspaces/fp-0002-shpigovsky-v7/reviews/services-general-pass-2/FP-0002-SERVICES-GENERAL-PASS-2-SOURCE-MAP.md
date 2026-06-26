# FP-0002 — Services General Pass 2 Source Map

**Date:** 2026-06-26

## Changed files

| File | Action | Reason |
| ---- | ------ | ------ |
| `src/pages/uslugi.html` | Modified | Final hero params; 4× category hub includes; section order |
| `src/partials/sections/services-category-hub.html` | Created | Parameterized category hub partial |
| `src/partials/sections/hero-inner.html` | Modified | Optional eyebrow + CTA slot for Services hero |
| `src/scss/style.scss` | Modified | `.services-category-hub` block; `.page-uslubi` hero scope |
| `src/img/content/services/*.webp` | Created | Figma exports (hero, 6 gallery, decor) |

## Unchanged (protected)

| Path | Hash vs Pass 1 |
| ---- | -------------- |
| `src/pages/index.html` | Match |
| `src/partials/sections/home-*.html` | Match |
| `src/js/main.js` | Match |
| `gulpfile.js` | Match |

## Partial parameters (hub)

| Param | Purpose |
| ----- | ------- |
| `modifierClass` | Hub variant + optional `--no-gallery` |
| `sectionId` | Accessible heading id |
| `heading`, `leadPrimary`, `leadSecondary` | Copy |
| `servicesHtml`, `galleryHtml` | Prebuilt list/gallery fragments |
| `decorImage` | Shared watermark asset |
| `ctaText`, `ctaSource` | Modal CTA |

## CSS scope

Single block: `.services-category-hub` + `.page-uslugi` hero overrides under Pass 2 section in `style.scss`.
