# REPORT — FP-0002 V9-06E18 REUSABLE BLOCKS BATCH 1 FIELDS

**Wave:** V9-06E18  
**Date:** 2026-07-08  
**Verdict:** PASS

## Summary

Implemented Batch 1 reusable block admin fields under `Настройки сайта → Повторяемые блоки` for **Финальная форма**, **Специалисты**, **Отзывы** (alias), and **CTA-блоки**. Seeded options from live/static sources, migrated frontend renderers with fallback chains, delivered to runtime, validated 8/8 routes HTTP 200 with visual parity screenshots.

## Evidence

- Validation: `validation/v9-06e18-reusable-blocks-batch-1-fields/`
- DB checkpoint: `v9-06e18-reusable-blocks-batch-1-fields-pre-20260708-001410`
- E17 baseline: `5ad621a9e5db13f0200fd751f8c38c7971d7578b`

## Changed source (canonical)

**Plugin (2):** `OptionsPage.php`, `FieldGroups.php`  
**Theme (7):** `functions.php`, `inc/reusable-blocks-helpers.php` (new), `inc/admin-options.php`, `inc/service-helpers.php`, `final-form.php`, `home/specialists.php`, `alcohol-direct-v9/specialists.php`  
**ACF JSON (4):** 3 new block groups + reviews dual-location update

## Key decisions

1. **Отзывы:** ALIAS_ONLY — `fp02-block-reviews` uses `post_id=fp02-reviews`; top-level menu unchanged.
2. **Специалисты:** Seeded via theme asset paths; media attachments deferred.
3. **CTA-блоки:** Global defaults only; per-service `cta_*` overrides preserved.

## Next

`CREATE_V9_06E19_OPERATOR_REUSABLE_BLOCKS_ADMIN_QA_TASK`
