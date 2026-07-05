# FP-0002 V9-06D9E Vendor Init Parity Repair v1

**Date:** 2026-07-05

## Fix

`inc/home-vendors.php` enqueue order aligned with static V9:

**Before:** `v9-style` → `swiper` → `fancybox` (theme overrides overridden by Swiper defaults)  
**After:** `swiper` → `fancybox` → `v9-style`

JS order unchanged: `swiper` → `fancybox` → `v9-shell` (init blocks already present).

No new init file; no duplicate Swiper constructors.

Evidence: `validation/v9-06d9e-home-slider-vendor-pagination-repair/vendor-init-parity-repair-result.json`
