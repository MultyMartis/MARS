# REPORT — FP-0002-V9-06E13-CURRENT-WP-SPECIALISTS-PROVENANCE-AUDIT-v1


| Component | Role | Provenance | Risk |
|---|---|---|---|
| `alcohol-direct-v9.php` | Stack orchestrator | HOME_PARTIAL_REUSE | HIGH |
| `home/specialists.php` | Block renderer | HOME_PARTIAL_REUSE | HIGH |
| `home-vendors.php` | Swiper enqueue | front-page-only gate | **CRITICAL** |
| `v9-shell.js` | Slider init | DIRECT_V9_PORT (neutral) | LOW when Swiper missing |

## Root cause

Markup was structurally identical to static V9, but **Swiper vendor was not enqueued** on alcohol leaf. Without Swiper, `data-specialists-slider` cards display at full intrinsic image width — operator-observed oversized photos.
