# FP-0002 — Services Component Boundary Map v1

**Date:** 2026-06-26  
**Authority:** `Spig_v1.2.fig` visible anatomy + V1 @ `641295e1`

| Component | Classification | Existing source candidate | Reuse allowed | New component required |
| --------- | -------------- | ------------------------- | ------------: | ---------------------: |
| Site header | GLOBAL_SHARED | `partials/layout/header.html` | Yes | No |
| Hero outer shell (media, radius, gutters) | INNER_PAGE_SHARED | `hero-inner.html` shell classes | Partial (shell only) | Yes — services hero assembly |
| Home hero content | DO_NOT_REUSE | `hero.html` | No | N/A |
| Inner hero content (services) | SERVICES_SPECIFIC | `hero-inner.html` params | No | Yes |
| Breadcrumbs | INNER_PAGE_SHARED | **none** | No | Yes |
| Page submenu / tabs | SERVICES_SPECIFIC | **none** | No | Yes |
| Category hub — addictions | SERVICES_SPECIFIC | `services-category-hub.html` | Partial (data model) | Yes — layout v2 |
| Category hub — mental health | SERVICES_SPECIFIC | same partial | Partial | Yes |
| Category hub — eating disorders | SERVICES_SPECIFIC | same partial | Partial | Yes |
| Category hub — genotyping | SERVICES_SPECIFIC | same partial | Partial | Yes |
| Program — content | CONTENT_SHARED_LAYOUT_SPECIFIC | `home-rehabilitation-program.html` | Content only | Yes — services layout |
| Program — layout/grid | SERVICES_SPECIFIC | home partial layout | No | Yes |
| Founder quote | CONTENT_SHARED_LAYOUT_SPECIFIC | `home-founder-quote.html` | Yes (variant param) | Optional variant |
| Comfort gallery | CONTENT_SHARED_LAYOUT_SPECIFIC | `home-comfort.html` | Partial | Polish pass |
| Mid-page CTA strip | SERVICES_SPECIFIC | **none dedicated** | No | Yes |
| FAQ | INNER_PAGE_SHARED | `home-faq.html` | Yes | No |
| Final form | GLOBAL_SHARED | `home-final-form.html` | Yes | No |
| Footer | GLOBAL_SHARED | `footer.html` | Yes | No |
| Modal consultation | GLOBAL_SHARED | `modal-consultation.html` | Yes | No |

## Critical boundaries

```text
Hero shell          → INNER_PAGE_SHARED (geometry only)
Home hero content   → DO_NOT_REUSE for Services
Inner hero content  → SERVICES_SPECIFIC (overlay panel + in-banner CTA)
Breadcrumbs         → INNER_PAGE_SHARED (new partial required)
Page submenu        → SERVICES_SPECIFIC (tab/anchor nav — not category body)
Program data        → CONTENT_SHARED
Program layout      → SERVICES_SPECIFIC (2×2 image grid per PNG)
```

## Home impact

All new components must **not** alter `index.html` or home partial defaults. Services V2 page assembly only.
