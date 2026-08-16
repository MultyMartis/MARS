# REPORT — FP-0002 PROD-P10 Technical SEO Audit

**Date:** 2026-08-14  
**Host:** http://shpigovsky.beget.tech/  
**Evidence:** `REPORTS/evidence/prod-p10-seo-search-integrations/seo-audit/`

## Scope

Bounded GET crawl of public URLs discovered from native sitemap + homepage internal links.  
No admin crawl. No destructive requests. Rate-limited.

## Response summary

| Metric | Value |
|--------|-------|
| URLs fetched | 89 |
| HTTP 200 | 88 |
| HTTP 405 | 1 (`/xmlrpc.php?rsd`) |
| Critical | 0 |
| High | 1 |
| Medium | 6 |
| Low | 71 |
| Informational | 75 |

## Classification counts

| Class | Count |
|-------|-------|
| DOMAIN CUTOVER | 79 |
| OPERATOR DECISION | 72 |
| FALSE POSITIVE / ACCEPTED | 2 |
| SAFE TECH FIX | 0 remaining after robots fix (1 applied outside crawl dataset timing) |
| CONTENT / DEMO | (included inside Low/Medium title/H1/meta clusters; see findings.json) |
| SAFE UNKNOWN | present for some missing-canonical edge cases |

## Notable findings

### SAFE TECH FIX (applied)

1. **Physical `robots.txt` lacked Sitemap discovery** while WP `robots_txt` filter was bypassed by a static file.  
   - Action: append `Sitemap: http://shpigovsky.beget.tech/wp-sitemap.xml`  
   - Preserved: `User-agent: *` / `Disallow: /`  
   - Rollback: `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p10-layer-b-pre\docroot__robots.txt.prod-before`  
   - Evidence: `SAFE-FIX-ROBOTS-SITEMAP.json`

### DOMAIN CUTOVER (deferred)

- Sitewide `noindex,nofollow` via `blog_public=0`
- `Disallow: /` indexing policy on temporary Beget host
- Sitemap/index URLs use `shpigovsky.beget.tech` via `home_url()` (correct until cutover)
- `.test` / localhost residue strings in HTML on several pages

### OPERATOR DECISION

- Missing meta descriptions across most templates (no SEO-plugin owner)
- `/xmlrpc.php?rsd` returns 405 (often intentional hardening)

### CONTENT / DEMO

- Placeholder/local title patterns where present
- Multiple/missing H1 where demo/editorial layout applies
- Duplicate titles among demo blog pages (see findings.json)

### FALSE POSITIVE / ACCEPTED

- XML sitemap generation live while indexing remains closed (by design for temporary host)
- Sitemap line present alongside Disallow

## Safe fixes applied

| Finding | Owner | Action | Before/After | Rollback |
|---------|-------|--------|--------------|----------|
| robots Sitemap discovery missing (static file) | docroot `robots.txt` | Append Sitemap URL; keep Disallow | 26 B Disallow-only → Disallow + Sitemap | Layer B `docroot__robots.txt.prod-before` |

No editorial rewrites. No domain/homeurl changes. No indexing policy flip.

## Deferred recommendations

1. At DNS cutover to `shpigovsky.ru`: flip visibility / remove Disallow; regenerate robots (prefer WP dynamic robots or update static file host); resubmit sitemap in Google/Yandex.
2. Decide whether to install/own meta descriptions (theme fields vs SEO plugin) — operator decision.
3. Broad `.test` cleanup remains migration/P06 territory.
4. Demo blog titles/content cleanup remains editorial.

## Dataset

- `seo-audit/crawl-dataset.json`
- `seo-audit/findings.json`
