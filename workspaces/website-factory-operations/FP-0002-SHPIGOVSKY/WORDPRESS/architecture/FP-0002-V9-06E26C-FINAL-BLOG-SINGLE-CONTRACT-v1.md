# FP-0002 V9-06E26C Final Blog Single Contract v1

## Route contract

- Archive: `/blog/` via `home.php` (unchanged from E26B)
- Single: `/blog/{slug}/` via `single.php` for standard `post`
- Permalink: `/blog/%postname%/`

## Render contract

| Block | Source | Fallback |
|---|---|---|
| Title | WP `post_title` | — |
| Lead | ACF `article_lead` | `post_excerpt` |
| Body | `the_content()` | hidden if empty |
| TOC | auto h2/h3 | hidden if none or toggle off |
| Featured image | post thumbnail | archive card fallback image |
| Meta | ACF flags + reading time | archive defaults |
| Conclusion | ACF quote | hidden if empty |
| Sources | ACF repeater | hidden if empty |
| FAQ | ACF repeater | hidden if empty |
| Related | ACF `related_posts` | same-category latest |
| CTA | ACF final CTA | blog archive CTA band |

## E26D remainder

- Seed demo/fixture article content from V9 `nazvanie-stati`
- Operator visual QA desktop/mobile
- WPilot remains out of scope

Evidence: `validation/v9-06e26c-blog-single-template-wordpress-acf-port/final-e26c-blog-single-contract.json`
