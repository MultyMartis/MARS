# FP-0002 V9-06E26B Frontend Template v1

## Implemented stack

`home.php` renders:

1. `blog-page__breadcrumbs` — V9 breadcrumb markup
2. `template-parts/blog/archive-list.php` — section `blog-archive`
3. `template-parts/blog/lower-stack.php` — CTA + expert quote

## Partials

| Partial | Role |
|---|---|
| archive-list.php | H1, intro, grid loop or empty state, pagination hook |
| empty-state.php | `blog-archive__empty-state` when 0 posts |
| pagination.php | `blog-archive-pagination` via `paginate_links` |
| blog-archive-card.php | V9 card markup; date, reading time, excerpt |
| lower-stack.php | Wraps CTA band + expert quote |
| expert-quote.php | `blog-expert-quote` block |

## Loop

- Standard WP `post` type main query
- 12 posts per page (`pre_get_posts`)
- Card data from `shpigovsky_build_blog_archive_card_args()`

## Not implemented (E26C)

- `single.php` article layout remains skeleton

Evidence: `validation/v9-06e26b-blog-archive-wordpress-acf-port/frontend-template-result.json`
