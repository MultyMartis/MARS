# ISEO-SU HIGH FIX WAVE 01 EVIDENCE v1

**Task ID:** ISEO-SU-SITE-OPS-HIGH-FIX-WAVE-01  
**Date:** 2026-08-24  
**Production:** https://i-seo.su/  
**Deploy stamp:** `20260824T083857Z`

## 1. Scope

Close two confirmed HIGH findings from the tech/SEO audit:

1. broken root sitemap architecture (`SM-CHILD-404`);
2. broken relative blog/theme image paths (`IMG-BROKEN`).

No MEDIUM / LOW / REVIEW backlog work. No form, Metrika, or glossary mutations.

## 2. Starting HIGH Findings

| ID | Issue | Status before |
|----|-------|---------------|
| SM-CHILD-404 | `/sitemap.xml` advertised `post|page|category-sitemap.xml` (404) | OPEN / CONFIRMED |
| IMG-BROKEN | ~96 broken image occurrences from relative `img/` resolution under `/blog/...` | OPEN / CONFIRMED |

## 3. Root Sitemap Forensic

| Surface | HTTP | Authority |
|---------|------|-----------|
| `/sitemap.xml` | 200 | **Physical file** at webroot (`sitemap.xml`, 513 B pre-fix) |
| `/sitemap-static.xml` | 200 | Physical file; 71 marketing URLs |
| `/wp-sitemap.xml` | 200 | WordPress core sitemap index |
| `/robots.txt` | 200 | Physical file; already `Sitemap: https://i-seo.su/sitemap.xml` |
| `/post-sitemap.xml` | 404 | Obsolete Yoast-style child |
| `/page-sitemap.xml` | 404 | Obsolete Yoast-style child |
| `/category-sitemap.xml` | 404 | Obsolete Yoast-style child |

Pre-fix `/sitemap.xml` was a static Yoast-styled sitemapindex referencing `sitemap-static.xml` + three dead children. It was **not** a live Yoast-generated endpoint.

## 4. Root Sitemap Fix

Replaced physical `/sitemap.xml` with a valid sitemapindex of exactly two children:

1. `https://i-seo.su/sitemap-static.xml`
2. `https://i-seo.su/wp-sitemap.xml`

MARS SoT: `production-source/sitemaps/sitemap.xml`  
Production SHA-256 after deploy: `636169b17036186d33c34847aab010bbf23289a44e1c80624fa73aec3d387f8a`  
Rollback: `X:\AI MARS\local\sites\iseo-su-production\_high-fix-wave-01\backups\deploy-20260824T083857Z\sitemap.xml`

## 5. Static Sitemap Strategy

**Decision: ALLOWLIST_GENERATOR (safe automation).**

- Full disk HTML enumeration is unsafe as a default (legacy twins, verification files, handlers, `test.html`).
- Current `sitemap-static.xml` (71 URLs) validated **all HTTP 200**.
- Implemented project-owned generator:

```text
python projects/iseo-su-site-ops/tools/generate-sitemap-static.py
```

- Allowlist: `data/sitemaps/sitemap-static-urls-v1.txt`
- Output: `production-source/sitemaps/sitemap-static.xml`
- No invented `lastmod` / `changefreq` / `priority`.
- Operational model: edit allowlist → regenerate → deploy resulting XML.

## 6. Static Sitemap Result

| Metric | Before | After |
|--------|-------:|------:|
| URL count | 71 | 71 |
| HTTP 200 | 71 | 71 |
| Valid XML | yes | yes |

Production SHA-256: `384d45512c43a9d083b3ba9f645c05670b108ee0663bb9b659ee4f3f5c9306d0`

## 7. robots.txt

Already correct:

`Sitemap: https://i-seo.su/sitemap.xml`

**NO CHANGE.**

## 8. Blog Image Forensic

Audit sample URL pattern examples:

- `/blog/2025/img/Portniagin.png`
- `/blog/author/.../img/...`

Inventory shows author/year-month URLs **301 → homepage** (`final_url=https://i-seo.su/`, 1 hop). The audit crawler resolved homepage relative `img/...` against the **pre-redirect** request URL, producing the 96 broken image occurrences.

Ordinary blog posts (`/blog/{slug}.html`) already used root-absolute `/img/` in most chrome; recommendations used `../../img/` (works on post depth, fragile).

## 9. Image Source Authority

| Source | Pattern | Class |
|--------|---------|-------|
| `wp-content/themes/iseoblog/page-home.php` | `img/...`, `../img/...` | PRIMARY (homepage + redirect attribution) |
| `template-parts/content-recomendations.php` | `../../img/...` | included from `single.php` |
| `template-parts/cases-seo.php` | `../img/...` | included from `single.php` |
| `template-parts/cases-context.php` | `../../img/...` | theme case block |
| `template-parts/cases-geo.php` | `../../img/...` | theme case block |

**Not** WordPress `post_content` DB rows for this HIGH class. **DB mutation: NO.**

All intended `/img/...` assets checked for patched references: **35/35 HTTP 200**.

## 10. Repair Method

Template source repair only:

`img/...` / `../img/...` / `../../img/...` → `/img/...`

No browser JS rewrite. No CSS mask. No global site-wide string replace outside the five theme files above.

## 11. DB Backup / Mutation

| Item | Value |
|------|-------|
| DB mutation | **NO** |
| DB backup | **N/A** |

## 12. Image Repair Result

| File | Replacements |
|------|-------------:|
| `page-home.php` | 37 |
| `content-recomendations.php` | 3 |
| `cases-seo.php` | 1 |
| `cases-context.php` | 1 |
| `cases-geo.php` | 3 |

Post-fix relative defects remaining in those sources: **0**.

## 13. Targeted Re-crawl

Focused crawl after deploy (`targeted-recrawl-wave01.json`):

- root/static/wp sitemaps + robots + obsolete children
- homepage, blog hub, two posts, author + year-month samples
- regression smoke set

Result: **PASS**

- broken under `/blog/.../img/` after fix: **0**
- relative `img/` defects remaining in rendered HTML sample: **0**
- `/img/` asset 404 in sample: **0**

## 14. Regression

Checked: `/`, `/services.html`, `/blog/`, representative post, `/offers`, `/tariff-calc`, `/glossary/`, glossary single, three sitemaps, robots.

All HTTP 200; no PHP fatal; forms/Metrika/glossary not mutated.

## 15. Production / Source Alignment

| Production path | MARS SoT |
|-----------------|----------|
| `/sitemap.xml` | `production-source/sitemaps/sitemap.xml` |
| `/sitemap-static.xml` | `production-source/sitemaps/sitemap-static.xml` |
| theme files above | `production-source/theme/iseoblog/...` |

Generator + allowlist committed under project tools/data.

## 16. Rollback

Restore exact pre-deploy bytes from:

`X:\AI MARS\local\sites\iseo-su-production\_high-fix-wave-01\backups\deploy-20260824T083857Z\`

| Remote | Backup SHA-256 (prefix) |
|--------|-------------------------|
| `sitemap.xml` | `3326c713a77d75a5…` |
| `sitemap-static.xml` | `1bb56416c7bf2669…` |
| `page-home.php` | `501b73d7a2072b60…` |
| `content-recomendations.php` | `18436adfbe948177…` |
| `cases-seo.php` | `74163ea1899084bd…` |
| `cases-context.php` | `7871068a0f8992e9…` |
| `cases-geo.php` | `64d247065e5ced37…` |

## 17. Final HIGH Closure

| Finding | Status |
|---------|--------|
| HIGH 1 SM-CHILD-404 | **CLOSED** |
| HIGH 2 IMG-BROKEN | **CLOSED** |
| HIGH OPEN AFTER TASK (these two) | **0** |
