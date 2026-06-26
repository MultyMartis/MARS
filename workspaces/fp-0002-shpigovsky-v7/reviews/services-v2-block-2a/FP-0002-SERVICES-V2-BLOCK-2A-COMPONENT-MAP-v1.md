# FP-0002 — Services V2 Block 2A Component Map v1

**Date:** 2026-06-26

## Partial

`src/partials/sections/services-category-section-v2.html`

## Root class

`.services-category-section-v2`

## Parameters (implemented)

| Parameter | Addictions value |
| --------- | ---------------- |
| `id` | `services-category-addictions` |
| `modifierClass` | `services-category-section-v2--addictions` |
| `sectionId` | `services-category-addictions-heading` |
| `icon` | `01` |
| `heading` | Зависимости и пристрастия |
| `intro` | Figma `1:1410` |
| `lead` | Figma `1:1413` |
| `bodyHtml` | empty |
| `servicesHtml` | 4 articles inline |
| `galleryHtml` | 3 figures |
| `ctaText` | Записаться на консультацию |
| `ctaSource` | `services-addictions` |
| `decorImage` | `assets/img/content/services/services-hub-decor.webp` |

## Optional regions

| Region | Addictions |
| ------ | ---------- |
| bodyHtml | hidden via `:empty` |
| gallery | 3 images |
| decor | shared hub decor asset |

## Reuse

- Button: `.btn.btn_dark.btn--primary` + modal hooks
- Link arrow: `assets/svg/external-link.svg`
- Service leader dots: pattern from `home-treatment-prevention__service-leader`
- Marker badge: geometry from `home-rehabilitation-requirements__step-number`

## Over-abstraction

None — single parameterized partial; no universal engine.

## Future categories

Same partial; different `modifierClass`, content params, optional empty `bodyHtml` / gallery.
