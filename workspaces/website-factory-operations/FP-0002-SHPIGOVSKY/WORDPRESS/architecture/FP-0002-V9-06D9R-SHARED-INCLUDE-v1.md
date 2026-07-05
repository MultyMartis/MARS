# FP-0002 V9-06D9-R Shared Include

**File:** `template-parts/shared/reviews-slider.php`

## Context args

| Arg | Default | Notes |
|-----|---------|-------|
| `context` | `home` | `home` or `reviews_page` |
| `limit` | 0 | Home defaults to 10 |
| `featured_only` | false | Home forces true |
| `section_class` | `reviews` | Reviews page adds `reviews--page` |
| `show_heading` | true | False on reviews page |
| `show_all_link` | true | False on reviews page |

Preserves V9 Swiper markup, pagination dots, and card structure. Renders nothing when explicitly disabled.

Evidence: `validation/v9-06d9r-reviews-shared-include-implementation/shared-include-result.json`
