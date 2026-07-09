# FP-0002 V9-06E26B Final Blog Archive Contract v1

## Archive

| Item | State |
|---|---|
| Route | `/blog/` |
| page_for_posts | 19 |
| Template | `home.php` + blog partials |
| Permalink | `/blog/%postname%/` |
| Posts | 0 (empty state active) |

## ACF

- `group_fp02_blog_archive_settings` on posts page
- `group_fp02_blog_post_article_meta` preserved on `post`

## Behaviour

| Feature | Contract |
|---|---|
| Category filter | Absent (matches static V9) |
| Empty state | `blog-archive__empty-state` when no posts |
| Cards | V9 `blog-archive-card` when posts exist |
| Pagination | `blog-archive-pagination` when >1 page |
| Lower stack | CTA band + expert quote always on archive |

## Deferred

| Wave | Scope |
|---|---|
| E26C | Blog single template |
| E26D | Demo/fixture post seeding |
| WPilot | Future import automation |

## Operator QA checklist

- [ ] Edit archive H1/intro on page «Статьи» in admin
- [ ] Confirm `/blog/` shows empty state (0 posts)
- [ ] Confirm lower CTA opens consultation modal
- [ ] Regression: `/o-centre/`, services, contacts, reviews, privacy
- [ ] After E26D: verify cards + pagination with seeded posts

Evidence: `validation/v9-06e26b-blog-archive-wordpress-acf-port/final-e26b-blog-archive-contract.json`
