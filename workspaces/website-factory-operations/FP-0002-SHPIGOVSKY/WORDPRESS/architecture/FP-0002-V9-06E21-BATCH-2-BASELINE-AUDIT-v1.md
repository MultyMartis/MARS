# FP-0002 V9-06E21 Batch 2 Baseline Audit

Evidence: `validation/v9-06e21-reusable-blocks-batch-2-fields/batch-2-baseline-audit.json`

## Summary

Batch 2 blocks mapped from E16 inventory. Header/footer remain hybrid with **Общие настройки** + **WP_NAV_MENU_AUTHORITY**. Hero fallbacks are global options only — page-local `hero_media` unchanged. Comfort/rehab blocks were hardcoded V9 PHP; now block options with static fallback.

## Scope exclusions

- Reviews alias not restored
- Batch 3 not started
- Additional CTA bands covered by Batch 1
