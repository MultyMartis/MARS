# P18I — Final Crawl Charter (Prepared, Not Executed)

## Scope

- HTTP status classes: 2xx / 3xx / 4xx / 5xx
- Redirect chains (apex, www, legacy paths)
- Canonical link tags
- Title, meta description, H1
- robots / meta robots / X-Robots-Tag
- Sitemap URL coverage vs crawl
- Orphan URLs (best effort)
- Duplicate URL patterns
- Broken assets (sample + critical pages)
- Internal link smoke
- HTTP vs HTTPS consistency
- www vs non-www
- Mobile smoke (key templates)
- Privacy regressions: consent banner, Metrika gating, form consent checkbox
- Form submit smoke (QA row + delete)
- Indexing guard state read-only (`blog_public=1`, no global noindex)

## Explicit non-goals

- Do not close indexing
- Do not change DNS/SMTP
- Do not purge leads

## Entry condition

P18H **READY WITH NON-BLOCKING LEGAL NOTE** — proceed unless operator blocks.
