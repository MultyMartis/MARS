# Operations — Indexing vs SEO robots ownership (FP-0002)

**Status:** Active  
**Updated:** 2026-08-24

## Two separate concerns

| Concern | Owner | Mechanism |
|--------|--------|-----------|
| Global indexability OPEN / CLOSED | Human (Admin Dashboard) | `blog_public` + temporary close robots + meta via `IndexingControl` |
| SEO crawl policy (paths, Clean-param, sitemap, bot groups) | Olya / site SEO | Canonical file `WORDPRESS/plugins/shpigovsky-core/assets/robots-seo-policy.txt` → physical `robots.txt` when OPEN |

These are **not** the same thing.

## OPEN behavior

When indexing is OPEN (human-approved):

1. Physical docroot `robots.txt` must serve the canonical Olya SEO policy.
2. `IndexingControl::robots_body(true)` loads that policy (never a generic MARS open template).
3. Dashboard shows **Индексация сайта: открыта** based on absence of global `Disallow: /`, not on SEO-specific Disallows.

## CLOSED behavior

When a human explicitly closes indexing:

1. Current SEO robots body is copied to `robots.txt.fp02-seo-open.bak`.
2. Physical `robots.txt` becomes global `Disallow: /` (+ Sitemap).
3. Re-opening restores the canonical SEO policy intact (plugin asset), not a generic template.

## Do not

- Replace OPEN-state SEO robots with a short generic “safe” file.
- Optimize, normalize, simplify, or otherwise change the current Olya-approved policy without a new explicit Olya/operator SEO decision.
- Treat Olya `Disallow: /wp-` / legal / UTM rules as “indexing closed”.
- Let read-only probes, WPilot, or watchdog rewrite `robots.txt`.
- Maintain a second editable robots truth outside the canonical policy file.

The current canonical Olya policy is the human-approved SEO robots truth. P18G owns temporary global OPEN/CLOSED safety only; it does not own SEO-policy redesign.

## Canonical recovery

- Source: `workspaces/.../WORDPRESS/seo/OLYA-ROBOTS-REVIEWED-CANDIDATE.txt` (review copy)
- Runtime canonical: `shpigovsky-core/assets/robots-seo-policy.txt`
- Production physical: `/robots.txt` must match OPEN policy when indexability is OPEN

## References

- Report: `REPORTS/REPORT-FP-0002-PROD-MAINT-OLYA-ROBOTS-RESTORATION.md`
- Evidence: `REPORTS/evidence/prod-maint-olya-robots-restoration/`
