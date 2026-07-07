# FP-0002 V9-06E18 — Batch 1 Baseline Audit

Evidence: `validation/v9-06e18-reusable-blocks-batch-1-fields/batch-1-baseline-audit.json`

## Summary

Batch 1 covers four reusable blocks from E16 priority-1 inventory. Reviews already editable via `fp02-reviews`; specialists and final form were partial/hardcoded; CTA bands hybrid service/global.

## Key findings

| Block | Editable before | E18 approach |
|-------|-----------------|--------------|
| Финальная форма | PARTIAL | New `fp02-block-final-form` fields + renderer fallback chain |
| Специалисты | NO | Repeater seeded from V9 static cards |
| Отзывы | YES | ALIAS_ONLY under `fp02-block-reviews` |
| CTA-блоки | PARTIAL | Global defaults on `fp02-block-cta-bands`; service overrides preserved |
