# REPORT — FP-0002-V9-06E13-SPECIALISTS-BLOCK-GAP-MATRIX-v1


| Area | Static V9 | WP before | Gap | Repair |
|---|---|---|---|---|
| Renderer | `partials/sections/specialists.html` | `home/specialists.php` | WRONG_CONTENT_SOURCE | `alcohol-direct-v9/specialists.php` |
| Swiper vendor | loaded | missing | WRONG_LAYOUT_MODE | `alcohol-direct-v9-vendors.php` |
| Card sizing | 3.5-slide grid | full-width stretch | WRONG_SIZE | Swiper init |
| Section ID | `service-leaf-specialists` | match | MATCH | — |
| Inner markup | `specialists__*` | match | MATCH | — |
