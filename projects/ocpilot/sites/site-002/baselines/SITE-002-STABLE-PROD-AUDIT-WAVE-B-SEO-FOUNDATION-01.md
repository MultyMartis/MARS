# SITE-002-STABLE-PROD-AUDIT-WAVE-B-SEO-FOUNDATION-01

**Issued:** 2026-07-10  
**Parent checkpoint:** [SITE-002-STABLE-PROD-CRON-RUN-REPORTS-DURATION-FIX-01.md](SITE-002-STABLE-PROD-CRON-RUN-REPORTS-DURATION-FIX-01.md)  
**Operation:** `SITE-002-PROD-AUDIT-WAVE-B-SEO-FOUNDATION-01`  
**OCPilot run:** 4.243  
**Environment:** https://bzpm.ru/ (Production)

## Changes

| Remote path | Change |
|-------------|--------|
| `/public_html/catalog/controller/extension/feed/google_sitemap.php` | Route-based `information/*` sitemap emission; skip migrated legacy `information_id` rows; includes `/contact` |

| DB table | Change |
|----------|--------|
| `oc_seo_url` | DELETE redundant rows **928** (`compare-products`), **927** (`wishlist`); owners **850**, **857** retained |

## Sitemap behaviour (after)

- Total URLs: **1409**
- Legacy `index.php?route=information/...`: **0**
- Pretty corporate routes: `/about`, `/contact`, `/custom-equipment`, `/dealers`, `/delivery`, `/guarantee`, `/payment-methods`
- `/kontakty`: **not** in sitemap (accepted 404 policy unchanged)

## Unchanged

- `/contact` canonical URL and routing
- Category/product data
- Lari 301 redirects (Run 4.235)
- Import/monitor/cron
- Header/footer/Yandex
- robots.txt / llms.txt

## Rollback

1. Re-upload pre-patch `google_sitemap.php` from Storage `deployments/SITE-002-PROD-AUDIT-WAVE-B-SEO-FOUNDATION-01/source-before/`
2. Run `rollback/db-rollback-plan.sql` to restore seo_url rows 928/927

Pre-patch sitemap SHA: see `rollback/source-before-manifest.json`

## Report

[sites/site-002/reports/SITE-002-PROD-AUDIT-WAVE-B-SEO-FOUNDATION-01.md](../reports/SITE-002-PROD-AUDIT-WAVE-B-SEO-FOUNDATION-01.md)
