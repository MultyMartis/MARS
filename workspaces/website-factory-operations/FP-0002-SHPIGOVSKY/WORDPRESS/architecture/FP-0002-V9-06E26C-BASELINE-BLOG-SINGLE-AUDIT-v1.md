# FP-0002 V9-06E26C Baseline Blog Single Audit v1

Static authority: `workspaces/fp-0002-shpigovsky-v9/src/pages/blog/nazvanie-stati.html`

## Static V9 section stack

1. Breadcrumbs (Главная → Статьи → article title)
2. Hero H1 + meta (date · reading time · author)
3. TOC from H2 headings
4. Featured image
5. Lead excerpt (`block-whith-red-line`)
6. Body typography (`blog-article-body__content`)
7. Conclusion + founder quote
8. Sources list
9. Related articles grid
10. Final CTA band

## WP baseline before E26C

- `single.php` skeleton only
- `article-content.php` / `article-lower-stack.php` placeholders
- 0 posts in DB
- Permalink already `/blog/%postname%/` from E26B

## Decision

Implement full V9 single stack with ACF extensions on `group_fp02_blog_post_article_meta`. No validation draft post (Option A).

Evidence: `validation/v9-06e26c-blog-single-template-wordpress-acf-port/baseline-blog-single-audit.json`
