# ISEO-SU SITEMAP ARCHITECTURE AND CURRENT STATE v1

**Programme:** ISEO-SU-SITE-OPS  
**Updated:** 2026-09-03 (CITY PAGES WAVE 02 — static inventory 127 → 132)  
**Companion evidence:** `ISEO-SU-CITY-PAGES-WAVE-02-EVIDENCE-v1.md` · `ISEO-SU-STATIC-SITEMAP-COMPLETENESS-FIX-EVIDENCE-v1.md` · historical `ISEO-SU-HIGH-FIX-WAVE-01-EVIDENCE-v1.md`

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
| Allowlist (source) | `data/sitemaps/sitemap-static-urls-v1.txt` |
| Completeness inventory | `data/sitemaps/public-canonical-static-routes-v1.txt` |
| Generator | `python projects/iseo-su-site-ops/tools/generate-sitemap-static.py` |
| Completeness validator | `python projects/iseo-su-site-ops/tools/validate-sitemap-static-completeness.py` |
| Output SoT | `production-source/sitemaps/sitemap-static.xml` |
| Current URL count | **132** |

### Mandatory regeneration rule

1. XML / HTTPS / uniqueness / HTTP health of listed URLs  
2. Completeness:

`PUBLIC_CANONICAL_STATIC_ROUTES - SITEMAP_STATIC_URLS = 0`

(after approved exclusions: blog/WP, `home.html`, `report-hub/**`, handlers/admin/tests/backups)

When adding/removing a public static marketing page: update **both** allowlist and inventory → regenerate → validate completeness → deploy `sitemap-static.xml`.

Do **not** auto-dump every HTML file from disk (legacy twins / verification / handlers).

**Historical note:** HIGH FIX WAVE 01 shipped a valid 71-URL static sitemap whose allowlist was later shown incomplete by SEO review; completeness fix 01 expanded coverage to 127 without abandoning deny-safe allowlist discipline. **CITY PAGES WAVE 02** (2026-09-03) added five regional SEO landings under `/services/seo/prodvizhenie-v-*.html` → static inventory **127 → 132**; completeness gate still PASS.

## Ownership split

| URL family | Owner sitemap |
|------------|---------------|
| Static marketing HTML (`services/`, `cases/`, legal, etc.) | `sitemap-static.xml` |
| WP blog posts, pages, glossary, taxonomies | `wp-sitemap.xml` |
| Glossary | WP only — **not** duplicated into static sitemap |

## Root SoT

`production-source/sitemaps/sitemap.xml`
