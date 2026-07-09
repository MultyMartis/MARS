# FP-0002 V9-06E26C Implementation Plan v1

## Single template

- `single.php` renders V9 `page-blog-article` stack for standard `post`
- Template parts under `template-parts/blog/single-*` plus `toc.php`, `faq.php`, `related.php`
- `blog-helpers.php` extended with single-article helpers and TOC heading-id filter

## ACF

- Extend `group_fp02_blog_post_article_meta` (preserve 6 existing fields)
- WP core remains authority for title/content/excerpt/featured image/taxonomies

## Validation

- No DB content seed
- Archive regression + `/blog/nazvanie-stati/` 404 expected
- E26D: demo content + visual QA

Evidence: `validation/v9-06e26c-blog-single-template-wordpress-acf-port/implementation-plan.json`
