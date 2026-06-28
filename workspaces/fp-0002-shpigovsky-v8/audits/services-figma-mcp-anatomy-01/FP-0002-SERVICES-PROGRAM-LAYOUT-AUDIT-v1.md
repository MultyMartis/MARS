# FP-0002 — Services Program Layout Audit v1

**Date:** 2026-06-26  
**Target node:** `1:1610` (`Программа центра`)  
**Mobile node:** `1:4880`

## Target anatomy (PNG + frame bounds)

| Property | Desktop | Mobile |
| -------- | ------- | ------ |
| Heading | Program section title + «подробнее» link (PNG) | Stacked |
| Intro blocks | Multi-paragraph lead (matches home copy) | Stacked |
| Card count | **4** directions | **4** |
| Desktop layout | **2×2 grid** with large image tiles + numbered titles (`01 — …`) | Vertical stack |
| Card structure | Image background + number + title overlay (PNG) | Full-width cards |
| CTA/link | Section-level «подробнее» | Same |

## Current V1 reuse

| Aspect | Source | Notes |
| ------ | ------ | ----- |
| Partial | `home-rehabilitation-program.html` | Home page partial included on `uslugi.html` |
| Content | Shared visible copy | **MATCH** |
| Layout | Home vertical direction cards (image left / text right pattern) | **MISMATCH** vs Services 2×2 grid |
| Style | Home SCSS `.home-rehabilitation-program*` | Partial style overlap |
| Assets | Shared program webp set | **MATCH** |

## Reuse classification

| Dimension | Verdict |
| --------- | ------- |
| CONTENT_REUSE | **Yes** |
| LAYOUT_REUSE | **No** |
| STYLE_REUSE | **Partial** (tokens/buttons only) |
| ASSET_REUSE | **Yes** |

```text
SHARED CONTENT + SERVICES-SPECIFIC LAYOUT
```

## V1 classification

**STRUCTURAL_MISMATCH** — functional content present, grid geometry wrong for Services target.

**Root cause:** incorrect reuse assumption from home block inventory without Services program frame decomposition.
