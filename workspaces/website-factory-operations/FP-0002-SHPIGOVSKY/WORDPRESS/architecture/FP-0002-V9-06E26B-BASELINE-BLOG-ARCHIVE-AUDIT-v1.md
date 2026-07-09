# FP-0002 V9-06E26B Baseline Blog Archive Audit v1

## Static V9 `/blog/` section stack

| Order | Section | DOM markers | Notes |
|---|---|---|---|
| 1 | Breadcrumbs | `blog-page__breadcrumbs`, `breadcrumbs` | Home → Статьи |
| 2 | Archive list | `blog-archive`, `blog-archive__heading`, `blog-archive__intro`, `blog-archive__grid`, `blog-archive-pagination` | H1 + intro + cards + pagination |
| 3 | Lower CTA | `blog-lower-stack`, `program-cta-band-section`, `#blog-cta-01` | Modal CTA band |
| 4 | Expert quote | `blog-expert-quote` | Founder quote block |

**Category/filter UI:** absent in static V9 — not required for E26B.

## Current WP before E26B

| Item | State |
|---|---|
| page_for_posts | 19 |
| Route | `/blog/` |
| Template | `home.php` skeleton (`shpigovsky-skeleton--blog-archive`) |
| Posts | 0 |
| Categories | 1 (default Uncategorized) |
| Permalink | `/%postname%/` |
| Gaps | No V9 classes, no ACF archive settings, placeholder card partial, no lower stack |

## Field gap summary

| Setting | Existing ACF | E26B action |
|---|---|---|
| Archive H1/intro | No | `group_fp02_blog_archive_settings` on posts page |
| Empty state copy | No | Seeded on page #19 |
| Card fallback image | No | Theme asset fallback |
| Final CTA / expert quote | No | ACF on posts page |
| Post card meta (reading time) | `group_fp02_blog_post_article_meta` | Preserved; used by card helper |

## Permalink gap

- Current: `/%postname%/`
- Target: `/blog/%postname%/`
- Decision: **APPLY in E26B** (0 posts; no URL dependency)

Evidence: `validation/v9-06e26b-blog-archive-wordpress-acf-port/baseline-blog-archive-audit.json`
