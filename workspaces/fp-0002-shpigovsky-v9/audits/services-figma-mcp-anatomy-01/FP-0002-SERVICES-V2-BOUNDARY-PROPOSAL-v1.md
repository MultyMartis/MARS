# FP-0002 — Services V2 Boundary Proposal v1

**Date:** 2026-06-26  
**Strategy gate:** `HYBRID_RECONSTRUCTION`  
**V1 preserved:** `src/pages/uslugi.html` @ `641295e1` (fallback, untouched)

## Parallel page

| Proposed path | Status |
| ------------- | ------ |
| `src/pages/uslugi-v2.html` | **Proposed only — NOT created in this task** |

## Proposed components

| Proposed path | Responsibility | Figma node | Reuses current source | Home impact |
| ------------- | -------------- | ---------- | --------------------: | ----------: |
| `partials/sections/services-hero-v2.html` | Hero shell + overlay content + in-banner CTA + breadcrumbs + tabs | `1:1311` subtree | Shell patterns from `hero-inner` | 0 |
| `partials/components/breadcrumbs.html` | BLK-005 trail | `1:1363` | None | 0 |
| `partials/components/page-subnav.html` | Category tab shortcuts | `1:1367` | None | 0 |
| `partials/sections/services-category-section-v2.html` | Parameterized hub with gallery optional | `1:1405` family | Data/hrefs from V1 hubs | 0 |
| `partials/sections/services-program-v2.html` | 2×2 program grid | `1:1610` | Copy from `home-rehabilitation-program` | 0 |
| `partials/sections/services-mid-cta.html` | Dark contact strip | `1:1715` | None | 0 |

## Reusable without rebuild (lower page)

- `home-founder-quote.html` (parametric)
- `home-comfort.html` (polish only)
- `home-faq.html`
- `home-final-form.html`
- `header.html` / `footer.html` / modal

## Boundaries

| Rule | Value |
| ---- | ----- |
| Navigation wiring | Do not change header nav active states for V2 experiment |
| Home | Zero changes to `index.html` and home partials |
| V1 fallback | Keep `uslugi.html` buildable |
| Assets | Export from Figma nodes; no PNG-as-asset |
| Rollback | Delete `uslugi-v2.html` + v2 partials only |

## Naming

Final filenames subject to V7 naming review — not approved in this audit.
