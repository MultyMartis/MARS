# REPORT — FP-0002-V9-06E13-REPAIR-PLAN-v1


1. **Renderer:** `template-parts/service/alcohol-direct-v9/specialists.php` — exact static V9 block; bypass `home/specialists.php`.
2. **Data:** `shpigovsky_get_v9_specialists_cards()` in `v9-static-content.php`.
3. **Vendor:** `inc/alcohol-direct-v9-vendors.php` — enqueue Swiper on `alcohol-special` variant only.
4. **Orchestrator:** Update `alcohol-direct-v9.php` to call new partial.
5. **Bootstrap:** `functions.php` requires new vendor file.
6. **CSS:** none (existing `specialists__photo` height 260px sufficient once Swiper active).
7. **Regression:** home specialists unchanged; 9 regression routes.
