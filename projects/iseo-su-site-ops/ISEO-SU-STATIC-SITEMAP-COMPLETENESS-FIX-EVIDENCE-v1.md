# ISEO-SU STATIC SITEMAP COMPLETENESS FIX EVIDENCE v1

**Task ID:** ISEO-SU-SITE-OPS-STATIC-SITEMAP-COMPLETENESS-FIX-01  
**Date:** 2026-08-24  
**Production:** https://i-seo.su/  
**Deploy stamp:** `20260824T110230Z`

## 1. Incident

After HIGH FIX WAVE 01, `/sitemap.xml` and `/sitemap-static.xml` were **technically valid** (HTTP 200, well-formed XML, all listed URLs resolving). SEO review then found **54 existing public marketing pages missing** from the static sitemap.

Methodological defect:

> VALID SITEMAP does **not** imply COMPLETE SITEMAP.

Previous validation checked XML/HTTP health only; it did not reconcile against the full public static route inventory.

## 2. SEO Review Input

Operator/SEO referenced file: `отсутсвуют в сайтмепе.txt` (54 URLs).

**SAFE UNKNOWN / reconstruction note:** the Cyrillic filename was **not found** in the Cursor workspace, Downloads, Desktop, Storage incoming, or project tree at task start. The 54-URL set was **deterministically reconstructed** from the tech-SEO URL inventory gap vs the then-current allowlist, matching the three groups named in the charter:

| Group | Count |
|-------|------:|
| `/cases/**` additional leaves | 13 |
| `/services/ai-optimization**` | 10 |
| `/services/seo/prodvizhenie-*.html` niche landings | 31 |
| **Total** | **54** |

Canonical acceptance list stored as: `data/sitemaps/seo-missing-54-urls-v1.txt`.

## 3. Missing URL List

Full list: `data/sitemaps/seo-missing-54-urls-v1.txt`  
Live validation CSV: `data/sitemaps/seo-missing-54-validation-v1.csv`

## 4. Root Cause

`tools/generate-sitemap-static.py` correctly implemented a **deny-safe curated allowlist** (`data/sitemaps/sitemap-static-urls-v1.txt`).

The allowlist itself was **incomplete**:

- captured an early subset of `cases/` and `services/seo/` hubs;
- omitted the entire `services/ai-optimization/` family;
- omitted later niche SEO landings (`prodvizhenie-*.html`);
- omitted several additional case pages (incl. SMM cases).

HIGH FIX WAVE 01 discovery via shallow SFTP HTML walk also under-counted nested marketing HTML, reinforcing reliance on the incomplete allowlist. No uncontrolled crawl was used to publish — the safety model was correct; the **source inventory coverage** was not.

## 5. Generator Before

- Allowlist: 71 URLs  
- Output: `production-source/sitemaps/sitemap-static.xml` (71)  
- Production SHA-256 (pre-fix): `384d45512c43a9d083b3ba9f645c05670b108ee0663bb9b659ee4f3f5c9306d0`  
- Completeness gate: **absent**

## 6. Route Inventory

New completeness inventory (must equal allowlist after exclusions):

`data/sitemaps/public-canonical-static-routes-v1.txt` — **127** URLs

Approved exclusions (not in static sitemap):

| Exclusion | Reason |
|-----------|--------|
| `/` | WP homepage template |
| `/blog/**`, `blog.html` | WordPress / `wp-sitemap.xml` |
| `/home.html` | LEGACY_OR_PARALLEL twin |
| `/report-hub/**` | EXTERNAL_SIBLING app |
| handlers / `__FORM.php` / admin / tests / backups | non-marketing / technical |

## 7. Supplied URL Validation

| Metric | Value |
|--------|------:|
| SEO supplied URLs | 54 |
| ADD_TO_STATIC_SITEMAP | 54 |
| REDIRECT / NON_INDEXABLE / NOT_FOUND / DUPLICATE | 0 |
| Accepted for sitemap | **54** |

## 8. Additional Completeness Reconciliation

Broader compare of tech-SEO inventory indexable static HTML vs allowlist (after approved exclusions) found **2** additional eligible marketing/legal pages outside the SEO-54 list:

- `https://i-seo.su/cookie-files-policy.html`
- `https://i-seo.su/user-agreement.html`

(`privacy-policy.html` was already present.)

After adding those, tech-SEO unexpected static gaps = **0**.

## 9. Generator Fix

Kept **allowlist strategy** (deny-safe). Changes:

1. Expanded allowlist to 127 URLs (71 + 54 + 2).  
2. Added `public-canonical-static-routes-v1.txt` as completeness authority twin.  
3. Generator now **fails** if allowlist ≠ inventory.  
4. Added `tools/validate-sitemap-static-completeness.py` with acceptance criterion:

`PUBLIC_CANONICAL_STATIC_ROUTES - SITEMAP_STATIC_URLS = 0`

## 10. Sitemap Before / After

| Metric | Before | After |
|--------|-------:|------:|
| Static sitemap URL count | 71 | **127** |
| SEO-54 accepted added | — | 54 |
| Additional (legal) added | — | 2 |
| Duplicate locs | 0 | 0 |

Production SHA-256 after deploy: `7a38727836b9f62fa6f28d881531f80f3b5c10ddf6fe83e28c0b30f612a07c0d`

## 11. Exclusions

Generator reject substrings include: `__form`, `form.php`, `wp-admin`, `wp-login`, `.bak`, `test.html`, `report-hub`, `/blog/`, `blog.html`, metrika, sitemap self-refs.

Static ↔ WP URL overlap after deploy: **0**.

## 12. Deployment

| Item | Value |
|------|-------|
| Method | SFTP (scoped) |
| File | `sitemap-static.xml` only |
| Stamp | `20260824T110230Z` |
| Backup | `X:\AI MARS\local\sites\iseo-su-production\_static-sitemap-completeness-01\backups\deploy-20260824T110230Z\sitemap-static.xml` |
| Backup SHA-256 | `384d45512c43a9d083b3ba9f645c05670b108ee0663bb9b659ee4f3f5c9306d0` |
| Verify match | YES |

Python tooling was **not** uploaded to production.

## 13. Post-Deploy Validation

| Check | Result |
|-------|--------|
| `/sitemap-static.xml` HTTP | 200 |
| Valid XML | YES |
| URL count live | 127 |
| SHA match local↔live | YES |
| SEO-54 still missing | 0 |
| Sitemap-listed 4xx | 0 |
| Sitemap-listed 5xx | 0 |
| Sitemap-listed noindex | 0 |
| Static/WP overlap | 0 |

## 14. Root Sitemap Regression

| Surface | Result |
|---------|--------|
| `/sitemap.xml` | 200; children = static + wp only |
| `/wp-sitemap.xml` | 200 |
| Obsolete Yoast children | still absent |
| `robots.txt` Sitemap directive | `Sitemap: https://i-seo.su/sitemap.xml` |

## 15. Future Completeness Rule

Every regeneration must include:

1. XML / HTTPS / uniqueness / HTTP health validation; **and**  
2. Completeness reconciliation:

`PUBLIC_CANONICAL_STATIC_ROUTES - SITEMAP_STATIC_URLS = 0`

Commands:

```text
python projects/iseo-su-site-ops/tools/generate-sitemap-static.py
python projects/iseo-su-site-ops/tools/validate-sitemap-static-completeness.py
```

## 16. Final Decision

**COMPLETE — ISEO-SU STATIC SITEMAP COVERAGE RECONCILED / SEO MISSING URLS ADDED / GENERATOR COMPLETENESS FIXED**

HIGH FIX WAVE 01 technical sitemap health remains closed. This task closes the **post-review completeness defect** without erasing the historical fact that the initial allowlist was incomplete.
