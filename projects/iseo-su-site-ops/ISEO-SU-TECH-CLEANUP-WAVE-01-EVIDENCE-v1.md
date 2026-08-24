# ISEO-SU TECH CLEANUP WAVE 01 EVIDENCE v1

**Task:** ISEO-SU-SITE-OPS-TECH-CLEANUP-WAVE-01  
**Date:** 2026-08-24  
**Production:** https://i-seo.su/  
**Mode:** bounded technical cleanup (sitemap-gap recheck + redirect-link repair + two heavy images)

## 1. Scope

In scope:

1. Recheck `SM-MISSING-INDEXABLE` against current production crawl + current sitemap union.
2. Repair internal links that target redirecting URLs (`LINK-TO-REDIR`).
3. Optimize two confirmed oversized PNGs (`IMG-HUGE`).
4. Validate, update backlog/brain, persist/sync.

Out of scope: canonical/title/meta/H1/alt/OG, offer/tool sitemap policy (except classification), orphan strategy, forms, Metrika, glossary content, redirect-rule changes.

## 2. Starting Findings

| ID | Original count | Starting status |
|---|---:|---|
| SM-MISSING-INDEXABLE | 197 | NEEDS_RECHECK |
| LINK-TO-REDIR | 129 unique redirecting targets | OPEN_TECH |
| IMG-HUGE | 2 sample files | OPEN_TECH |

## 3. SM-MISSING-INDEXABLE Recheck Method

Fresh read-only crawl (2026-08-24):

- Seeds + full current sitemap union (`sitemap-static.xml` + `wp-sitemap.xml` children).
- Result: **1060** fetched URLs; raw evidence under `X:\AI MARS STORAGE\iseo-su-site-ops\tech-cleanup-wave-01\`.
- Current sitemap union observed live: static **127**, WP children **416**, union **543**, overlap **0**.
- Gap formula: indexable canonical crawled 200s − sitemap union membership (same semantics as original audit analyzer).

## 4. Current Sitemap Gap Result

| Metric | Value |
|---|---:|
| ORIGINAL COUNT | 197 |
| CURRENT RAW GAP | 161 |
| CURRENT TRUE ELIGIBLE GAP | **0** |
| Indexable crawled (fresh) | 663 |
| Indexable present in sitemap | 502 |

## 5. Residual Classification

Of the 161 raw gaps:

| Class | Count | Notes |
|---|---:|---|
| QUERY_VARIANT | 149 | `/blog/?tags=` / `/blog/?sort=` filter variants |
| REPORT_HUB | 8 | `/report-hub/**` tool surfaces |
| NONCANONICAL_VARIANT | 4 | `home.html`, `blog.html`, `/glossary/` (redirect), `/glossary` archive hub not listed in WP post sitemaps |
| SHOULD_BE_IN_STATIC_SITEMAP | 0 | |
| SHOULD_BE_IN_WP_SITEMAP | 0 | |
| ACTUAL MISSING CANONICAL URLS | **0** | |

No sitemap auto-add performed. Architecture unchanged.

## 6. LINK-TO-REDIR Forensic

Historical (audit): **129** unique redirecting link targets; dominant pattern trailing-slash normalization:

- `/blog/` → `/blog`
- `/glossary/` → `/glossary`
- `/offers/` → `/offers`
- `/blog/?…` → `/blog?…`

Pre-deploy sample on key pages: **38** redirecting link occurrences (mostly nav + blog filters).

Source authorities:

| Authority | Role |
|---|---|
| Theme PHP (`content-topbar.php`, `content-mobilemenu.php`, `single.php`, `page-blog.php`, `archive.php`, `index.php`, `functions.php`) | Primary shared nav + blog filters/tags |
| Static HTML (`blog.html`, `blog-article.html`) | Legacy blog shells |
| WP block `core/archives` on `/offers` | Month archives that 301 → homepage |

Redirect rules themselves were **not** changed (`header.php` wp_redirect retained).

## 7. Redirect-Link Repair

File-based (SFTP deploy stamp `20260824T115820Z` + archives follow-up):

1. Theme hrefs rewritten to final non-slash URLs (`/blog`, `/glossary`, `/blog?tags=…`, `/blog?sort=…`).
2. Static `blog.html` / `blog-article.html` trailing-slash blog hrefs fixed.
3. `get_archives_link` filter added so dead date-archive widget URLs point to `/blog` (deterministic; avoids homepage surprise; no redirect-rule mutation).

Scoped production backups under `_tech-cleanup-wave-01/backups/`.

## 8. Redirect-Link Validation

- Pattern scan across **546** sitemap/seed HTML pages for residual bad href patterns: **0 hit pages**.
- Key-page live checks (`/`, `/blog`, `/offers`): `href="/blog/"`, `href="/glossary/"`, `/blog/202…`, author links = **0**.
- Redirect chains ≥2 in fresh crawl: **0**.
- New broken internal document links: **0** observed in smoke set.

LINK-TO-REDIR after approved fix set: **0**.

## 9. IMG-HUGE Forensic

| Asset | Before bytes | Dims | Format | Alpha used | Usage |
|---|---:|---|---|---|---|
| `/img/cases/seo_ai_cases/makita_01.png` | 2 760 350 | 2848×2092 | PNG RGBA | No (opaque) | `cases/makita.html` (+ related case pages) |
| `/img/cases/seo_ai_cases/maltipoo_01.png` | 2 726 005 | 3052×1778 | PNG RGBA | No (opaque) | `cases/maltipoo-honey-club.html` |

No srcset/picture; same PNG filenames retained (no markup change).

## 10. Image Optimization

Method: PNG palette quantization (256 colors, Floyd–Steinberg), dimensions unchanged, no crop/content change. WebP candidates generated for comparison only; **not** deployed (PNG path kept for safest integration).

## 11. Before / After Image Metrics

| FILE | BEFORE_BYTES | AFTER_BYTES | REDUCTION_PERCENT | DIMS | FORMAT |
|---|---:|---:|---:|---|---|
| makita_01.png | 2760350 | 333369 | 87.92% | 2848×2092 → same | PNG → PNG |
| maltipoo_01.png | 2726005 | 312435 | 88.54% | 3052×1778 → same | PNG → PNG |

Both below 1.5 MB threshold after deploy. Remote checksum verified.

## 12. Visual QA

| File | mean abs RGB diff | RMS | Result |
|---|---:|---:|---|
| makita_01.png | 0.229 | 1.38 | PASS |
| maltipoo_01.png | 0.698 | 1.94 | PASS |

Comparison thumbs stored in local wave `images/qa/` (not git).

## 13. Production Deployment

SFTP uploads (exact paths):

- `wp-content/themes/iseoblog/functions.php`
- `wp-content/themes/iseoblog/page-blog.php`
- `wp-content/themes/iseoblog/archive.php`
- `wp-content/themes/iseoblog/index.php`
- `wp-content/themes/iseoblog/single.php`
- `wp-content/themes/iseoblog/template-parts/content-mobilemenu.php`
- `wp-content/themes/iseoblog/template-parts/content-topbar.php`
- `blog.html`, `blog-article.html`
- `img/cases/seo_ai_cases/makita_01.png`, `maltipoo_01.png`

MARS source mirror: `production-source/theme/iseoblog/**`, `production-source/static-html/**`.

## 14. Regression

Smoke HTTP 200 / no PHP fatal: `/`, `/services.html`, `/cases.html`, makita + maltipoo case pages, `/blog/`, `/blog`, `/offers`, `/tariff-calc`, `/glossary`, `/sitemap.xml`, `/sitemap-static.xml`, `/wp-sitemap.xml`.

Forms / Metrika / glossary / SEO semantic metadata / sitemap architecture: **unchanged**.

## 15. Finding Status Reconciliation

| ID | Final status |
|---|---|
| SM-MISSING-INDEXABLE | **CLOSED / RECHECKED** (eligible gap 0; residuals EXPECTED) |
| LINK-TO-REDIR | **CLOSED** (residual 0) |
| IMG-HUGE | **CLOSED** (both assets below threshold) |

SEO-review findings intentionally untouched.

## 16. Production / Source Alignment

YES — deployed bytes mirrored into `production-source/` for theme + static HTML; images optimized from production originals with checksumed deploy.

## 17. Rollback

Restore from:

`X:\AI MARS\local\sites\iseo-su-production\_tech-cleanup-wave-01\backups\deploy-20260824T115820Z\`  
and archives follow-up backup under `backups/deploy-archives-*`.

## 18. Final Decision

**COMPLETE** — technical cleanup wave 01 closed: sitemap gaps rechecked (0 eligible), redirect links clean, heavy images optimized.
