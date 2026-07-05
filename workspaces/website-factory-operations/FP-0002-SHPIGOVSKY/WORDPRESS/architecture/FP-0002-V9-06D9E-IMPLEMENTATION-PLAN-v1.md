# FP-0002 V9-06D9E Implementation Plan v1

**Date:** 2026-07-05

## Scope

Repair only slider/vendor/pagination parity on Home — no Home main rewrite, no ACF.

## Changes

1. `template-parts/home/specialists.php` — restore V9 heading/id/aria
2. `inc/home-vendors.php` — fix CSS cascade order to match static V9 head

## Not in scope

- `faq.php` wrong heading (same D9-D class of bug; deferred)
- Inputmask local vendor copy (forms only)
- ACF wiring

## Evidence

`validation/v9-06d9e-home-slider-vendor-pagination-repair/implementation-plan.json`
