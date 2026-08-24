# ISEO-SU SITEMAP ARCHITECTURE AND CURRENT STATE v1

**Programme:** ISEO-SU-SITE-OPS  
**Updated:** 2026-08-24 (HIGH FIX WAVE 01)  
**Companion evidence:** `ISEO-SU-HIGH-FIX-WAVE-01-EVIDENCE-v1.md`

## Canonical entry

| Surface | Role |
|---------|------|
| `/sitemap.xml` | **Single canonical sitemap index** (physical file) |
| `/robots.txt` | `Sitemap: https://i-seo.su/sitemap.xml` |

## Children of `/sitemap.xml`

Exactly two:

1. `https://i-seo.su/sitemap-static.xml` — static marketing inventory (allowlist-generated)
2. `https://i-seo.su/wp-sitemap.xml` — WordPress core index (posts, pages, glossary CPT, taxonomies, etc.)

Obsolete Yoast-style children (`post|page|category-sitemap.xml`) are **not** advertised.

## Static sitemap operations

| Item | Path / command |
|------|----------------|
| Allowlist | `data/sitemaps/sitemap-static-urls-v1.txt` |
| Generator | `python projects/iseo-su-site-ops/tools/generate-sitemap-static.py` |
| Output SoT | `production-source/sitemaps/sitemap-static.xml` |
| Current URL count | **71** |

When adding/removing a public static marketing page: update allowlist → regenerate → deploy `sitemap-static.xml`.

Do **not** auto-dump every HTML file from disk (legacy twins / verification / handlers).

## Ownership split

| URL family | Owner sitemap |
|------------|---------------|
| Static marketing HTML (`services/`, `cases/`, legal, etc.) | `sitemap-static.xml` |
| WP blog posts, pages, glossary, taxonomies | `wp-sitemap.xml` |
| Glossary | WP only — **not** duplicated into static sitemap |

## Root SoT

`production-source/sitemaps/sitemap.xml`
