# FP-0002 V9-06D9A Visual Difference Register v1

**Date:** 2026-07-05  
**Evidence:** `validation/v9-06d9a-visual-parity-audit/visual-difference-register.json`

| Area | Static state | Runtime state | Severity | Root cause | Repair type |
|------|--------------|---------------|----------|------------|-------------|
| Hero image/overlay | Photo hero 620px | Empty panel, no media | CRITICAL | ACF_IMAGE_NOT_SEEDED | HERO_ASSET_REPAIR |
| Missing Home sections | 20 sections | 6 sections | CRITICAL | TEMPLATE_HTML_PORT incomplete | TEMPLATE_HTML_PORT |
| Inter fonts | 11/11 OK | 5/10 404 | HIGH | Absolute /assets/ paths | FONT_ASSET_REPAIR |
| Nav structure | V9 mega-menu | WP flat menu | HIGH | Menu seed differs | CONTENT_REVIEW |
| Nav typography | Inter 16px/400 | Same computed; fonts partial | MEDIUM | Font 404 synthesis | FONT_ASSET_REPAIR |
| Gallery | 4-slide swiper | Not rendered | HIGH | ACF empty | ACF_SEED_REQUIRED |
| Articles teaser | 3 cards | Not rendered | MEDIUM | No posts / disabled | CONTENT_REVIEW |
| Page density | ~1.48 MB screenshot | ~46 KB screenshot | CRITICAL | Combined gaps | TEMPLATE_HTML_PORT |
| Vendor CSS/JS | Swiper+Fancybox | v9-style only | MEDIUM | Not enqueued | CSS_TOKEN_REPAIR |
| Services hub | Rich layout | Sparse | MEDIUM | Deferred sections | DEFERRED → D9-F |

## Result

Repair required: **YES**
