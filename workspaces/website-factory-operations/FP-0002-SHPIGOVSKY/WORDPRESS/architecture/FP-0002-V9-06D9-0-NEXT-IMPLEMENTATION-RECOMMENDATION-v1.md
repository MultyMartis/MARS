# FP-0002 V9-06D9-0 Next Implementation Recommendation v1

**Date:** 2026-07-05  
**Evidence:** `validation/v9-06d9-0-full-visual-port-charter/next-implementation-recommendation.json`

## Recommendation

**CREATE_V9_06D9B_HEADER_FONT_ASSET_MESSENGER_REPAIR_TASK**

## Rationale (5–8 lines)

D9-A confirmed Inter font files return HTTP 404 on every page because `v9-style.css` retains static `/assets/fonts/` paths. This causes synthesized fallback typography that the operator perceives as thinner/paler nav text — a global defect, not a token mismatch. Static V9 shows messenger icon buttons (Telegram, WhatsApp, Max) with `href="#"` placeholders; WP template code exists but omits icons when `social_links` is empty after D8-A skip. D9-B can restore messenger **visuals** via V9-matching placeholder fallback without inventing production URLs. Swiper/Fancybox vendor assets must enqueue before gallery/reviews sections in later waves. Hero parity (D9-C) remains the correct **second** wave — highly visible but localized. Home section port (D9-D) should not precede global shell/font/header fixes.

## Alternatives considered

| Option | Why not first |
|--------|---------------|
| CREATE_V9_06D9C_HOME_HERO_PARITY_REPAIR_TASK | Does not fix fonts/messengers on all pages |
| CREATE_V9_06D9D_HOME_FULL_SECTION_TRANSFER_TASK | Premature before global assets and header |
| OPERATOR_DECISION_REQUIRED | Operator already authorized full port; D9-B scope is clear |

## Result

Next phase: **D9-B**.
