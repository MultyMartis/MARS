# FP-0002 — Services Inner Hero Architecture v1

**Date:** 2026-06-26  
**Target node:** `1:1311` (`1 - Главный экран`) inside `1:1310`  
**Mobile target:** `1:4625` (`Моби`) — pending full subtree MCP pass

## A. Shared hero shell

| Property | Home (`1:876`) | Services inner (`1:1311`) | Shared? |
| -------- | -------------- | ------------------------- | ------- |
| Outer frame role | Home hero | Services hero + header zone | Partial |
| Media layer | Yes | Yes (`1:1351` image 1400×628) | Yes — shell pattern |
| Radius / banner width | ~1400px class | 1400×628 `Group 6` | Yes |
| Site header inside frame | Yes | Yes (`1:1312`) | Yes (inner-page pattern) |
| Global header partial reuse | `header.html` separate in V1 | Figma nests header in hero frame | DOM split differs |

**Verdict:** **SHARED SHELL ONLY** — max-width media, rounded banner, overlay stack. Not a single parameterized React-style variant.

## B. Home hero content (`1:876`)

- Eyebrow: location/service area labels
- H1: `Шпиговский дом`
- Tagline: center subtitle
- CTA: header-adjacent / banner button placement

**Not applicable to Services.**

## C. Inner hero content (Services)

| Element | Node ID | Geometry / placement |
| ------- | ------- | -------------------- |
| Media image | `1:1351` | 1400×628, rounded rect |
| Overlay rects | `1:1352`, `1:1354` | Full-bleed gradient panels |
| Content group | `1:1353` `Group 5` | 1400×536 overlay |
| Eyebrow | `1:1355` | 515×32, **left** in overlay |
| H1 | `1:1356` | 582×70, **left** |
| Supporting copy | `1:1357` | 582×125, **left**, multi-line |
| CTA | `1:1358`/`1:1359` | 334×51 button **inside Group 6**, sibling to content group |

### Architecture answers

| Question | Answer |
| -------- | ------ |
| Unified central panel? | **Yes** — `Group 5` dark overlay panel on left portion of banner |
| Content centered or left? | **Left-aligned** within overlay (582px text column) |
| CTA inside text column or separate? | **Inside banner group**, not a separate page column below panel |
| Mobile differences | Hero compresses; breadcrumbs + tabs stack below banner (PNG confirmed) |
| Same DOM concept as Home Hero? | **No** — Home uses brand H1; Services uses service-area editorial block |

## V1 classification

| Area | V1 implementation | Classification |
| ---- | ------------------- | -------------- |
| Shell / media | `hero-inner.html` + `services-hero.webp` | **MINOR_POLISH** (crop/gradient tuned in final polish) |
| Content copy | Matches Figma visible text | **MATCH** |
| Content DOM | `hero__panel` + separate `hero__actions` column | **STRUCTURAL_MISMATCH** |
| Breadcrumbs in hero zone | **Missing** | **MISSING_COMPONENT** |
| Tab submenu in hero zone | **Missing** | **MISSING_COMPONENT** |

```text
HOME CONTENT REUSE — FORBIDDEN
SHARED SHELL ONLY
INNER HERO CONTENT — SERVICES_SPECIFIC DOM REQUIRED
```

## Required future strategy

New services hero partial (V2) combining: banner shell + overlay content + in-banner CTA + breadcrumbs + tab nav as **one anatomical block** matching `1:1311` decomposition — not bolted onto generic `hero-inner.html` params.
