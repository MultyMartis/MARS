# FP-0002 V9-06E18 — Implementation Plan

Evidence: `validation/v9-06e18-reusable-blocks-batch-1-fields/implementation-plan.json`

## Field groups

| Block | Slug | Group |
|-------|------|-------|
| Финальная форма | `fp02-block-final-form` | `group_fp02_block_final_form` |
| Специалисты | `fp02-block-specialists` | `group_fp02_block_specialists` |
| Отзывы | `fp02-block-reviews` | `group_fp02_site_options_reviews` (alias) |
| CTA-блоки | `fp02-block-cta-bands` | `group_fp02_block_cta_bands` |

## Reviews strategy

- Keep top-level `fp02-reviews` active.
- Set `post_id => fp02-reviews` on block subpage registration.
- Add dual ACF location for `fp02-block-reviews`.
- No data migration or storage key change.

## Visual parity

Renderer changes read new options first; seeded values mirror current live output. Chrome headless screenshots captured for 11 frontend routes.
