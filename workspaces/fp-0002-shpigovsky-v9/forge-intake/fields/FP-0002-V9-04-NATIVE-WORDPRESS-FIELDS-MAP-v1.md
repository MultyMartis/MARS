# FP-0002 V9-04 Native WordPress Fields Map v1

**Date:** 2026-07-02

## Global preferences

| Native field | Use |
|--------------|-----|
| post_title | All pages/posts H1 source |
| post_name (slug) | Exact V9 slugs — do not regenerate |
| post_parent | Service/O-Centre hierarchy |
| post_content | Blog article body; optional legal pages |
| post_excerpt | Blog cards + article hero excerpt |
| featured image | Blog archive/article |
| menu_order | Rare — prefer explicit menus |
| page_template | Maps to template family |
| author / date | Blog posts — visibility per open decision |
| categories / tags | Blog posts |

## Prefer native over ACF

- Post title, excerpt, content, featured image for blog
- Page title and parent for hierarchy
- Menu system for navigation ordering

## ACF required when

- Repeating cards (reviews, FAQ, sources)
- Global contacts not suitable for Customizer alone
- Structured bands with mixed media + copy
