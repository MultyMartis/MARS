# FP-0002 — Services V2 Block 1 Hero Architecture v1

**Date:** 2026-06-26

## Boundary

| Layer | V1 (`hero-inner.html`) | V2 (`services-inner-hero-v2.html`) |
| ----- | ---------------------- | ----------------------------------- |
| Media shell | Shared pattern | Reused shell rules (max-width 1400, radius, cover) |
| Content panel | Frosted centered `hero__panel` | **Removed** — left overlay stack |
| CTA placement | Separate `hero__actions` column | In-banner copy stack |
| Breadcrumbs / subnav | Absent | **Outside hero** (page assembly) |

## DOM (V2)

```text
.services-inner-hero-v2
  .services-inner-hero-v2__shell
    .services-inner-hero-v2__media
      img + gradient overlay
    .services-inner-hero-v2__content
      .container
        .services-inner-hero-v2__copy
          eyebrow → h1 → lead → CTA
```

## Figma mapping

| Element | Node | V2 class |
| ------- | ---- | -------- |
| Banner | `1:1347` / `1:1351` | `__media` / `__image` |
| Overlay | `1:1352`–`1:1354` | `__overlay` |
| Copy group | `1:1353` | `__copy` |
| Eyebrow | `1:1355` | `__eyebrow` |
| H1 | `1:1356` | `__title` |
| Lead | `1:1357` | `__lead` |
| CTA | `1:1359` | `__cta` |

## Key differences from V1

- No `hero__panel` frosted glass
- Left alignment (`align-items: flex-start`)
- CTA inside copy block (334px desktop, 206px mobile)
- Asset: existing `assets/img/content/services/services-hero.webp`

## Verdict

```text
HOME HERO CONTENT REUSE — ZERO
SHARED SHELL — PARTIAL (geometry only)
SERVICES-SPECIFIC COMPOSITION — IMPLEMENTED
```
