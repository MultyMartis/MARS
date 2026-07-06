# REPORT — FP-0002-V9-06E13-BASELINE-BEFORE-REPAIR-v1


**Wave:** V9-06E13 Alcohol Leaf Specialists Block V9 Parity Repair  
**Date:** 2026-07-07

## Operator evidence

Operator screenshot after E12 shows oversized specialists cards on `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/`. Screenshot available in Web-GPT chat only (`Screenshot 2026-07-07 at 05-03-51`).

## Technical baseline

| Check | Before E13 | Notes |
|---|---|---|
| Renderer | `template-parts/home/specialists.php` | HOME_PARTIAL_REUSE via alcohol-direct-v9.php |
| Swiper JS | **false** | `home-vendors.php` gates on `is_front_page()` |
| Swiper CSS | **false** | Same gate |
| Card count | 5 | Markup matched static V9 |
| Slider init | **broken** | v9-shell specialists boot requires `window.Swiper` |
| Root cause | Missing vendor on service leaf | Cards render at unconstrained width |

## Screenshots captured

- `runtime-alcohol-specialists-before-e13.png`
- `runtime-full-alcohol-leaf-before-e13.png`
- `static-v9-alcohol-specialists-reference-e13-before.png`
- `static-v9-full-alcohol-leaf-reference-e13-before.png`
