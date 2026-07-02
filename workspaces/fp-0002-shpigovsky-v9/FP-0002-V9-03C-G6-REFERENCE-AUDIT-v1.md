# FP-0002 V9-03C — G6 Reference Audit v1

## Post-deletion classification

| Reference | Classification | Action |
|-----------|----------------|--------|
| `data-inf-group="g6"` in `infrastructure-narrative.html` | REMOVE_DEAD_G6_REFERENCE | **Removed** |
| `infrastructure-narrative__group--g6` in SCSS | REMOVE_DEAD_G6_REFERENCE | **None existed** |
| `.infrastructure-narrative__group--mobile-close` in SCSS | REMOVE_DEAD_G6_REFERENCE | **Removed** (only G6 used it) |
| `.infrastructure-narrative__figure--mobile-only` in SCSS | REMOVE_DEAD_G6_REFERENCE | **Removed** (only G6 used it) |
| `.infrastructure-narrative__figure--desktop-only` in SCSS | REMOVE_DEAD_G6_REFERENCE | **Removed** (no HTML usage) |
| `infrastructure-narrative__subgallery--mobile-stack` | REMOVE_DEAD_G6_REFERENCE | **Removed with HTML** (no SCSS) |
| `initInfrastructureSliders` in `main.js` | KEEP — generic `[data-inf-slider]` | **Unchanged** |
| Fancybox `o-centre-infrastructure-g5` | KEEP_UNRELATED | **Unchanged** |
| `img6Src` in comfort-gallery component | KEEP_UNRELATED_G6_TOKEN | **Unchanged** (G5 gallery slot 6) |
| `micro-pass-13-capture.mjs` G6 query | HISTORICAL_DOC_ONLY | **Unchanged** (audit tool) |

## JavaScript

No G6-specific logic found. Slider init discovers DOM dynamically — no count hardcoding.

## mobile-close decision

**Removed** — sole consumer was G6 block.
