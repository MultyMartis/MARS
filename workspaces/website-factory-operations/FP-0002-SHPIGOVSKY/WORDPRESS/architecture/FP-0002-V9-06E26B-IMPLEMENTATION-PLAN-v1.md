# FP-0002 V9-06E26B Implementation Plan v1

## 1. Archive template

| Component | Plan |
|---|---|
| Primary template | `home.php` (posts page / `page_for_posts=19`) |
| Helpers | `inc/blog-helpers.php` |
| Partials | `archive-list`, `empty-state`, `pagination`, `lower-stack`, `expert-quote`, `blog-archive-card` |
| Body class | `page-blog` + `data-page="blog"` |

## 2. ACF

| Item | Value |
|---|---|
| Group | `group_fp02_blog_archive_settings` |
| Location | `page_type == posts_page` |
| Registration | Plugin `FieldGroups.php` + `acf-json/` |

## 3. Data

- Seed archive copy on page #19 from static V9
- 0 post creation
- 0 category seed (no filter UI in V9)

## 4. Permalink

- Change to `/blog/%postname%/`
- `flush_rewrite_rules(true)` recorded
- No redirects

## 5. Validation

- `/blog/` HTTP 200, V9 markers, empty state at 0 posts
- Regression routes unchanged
- Blog single (`single.php`) remains skeleton — E26C

Evidence: `validation/v9-06e26b-blog-archive-wordpress-acf-port/implementation-plan.json`
