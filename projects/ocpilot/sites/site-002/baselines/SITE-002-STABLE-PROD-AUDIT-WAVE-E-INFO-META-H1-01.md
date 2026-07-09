# SITE-002-STABLE-PROD-AUDIT-WAVE-E-INFO-META-H1-01

**Issued:** 2026-07-10  
**Parent checkpoint:** [SITE-002-STABLE-PROD-AUDIT-WAVE-B-SEO-FOUNDATION-01.md](SITE-002-STABLE-PROD-AUDIT-WAVE-B-SEO-FOUNDATION-01.md)  
**Operation:** `SITE-002-PROD-AUDIT-WAVE-E-INFO-META-H1-01`  
**OCPilot run:** 4.244  
**Environment:** https://bzpm.ru/ (Production)

## Changes

| DB table | Row | Field | Change |
|----------|-----|-------|--------|
| `oc_information_description` | `information_id=4` language_id=1 | `meta_description` | Added ЗПМ about-us description |
| `oc_information_description` | `information_id=5` language_id=1 | `meta_description` | Added terms/user agreement description |

| Remote path | Change |
|-------------|--------|
| `/public_html/catalog/controller/product/manufacturer.php` | Scoped `setDescription()` for `manufacturer_id=11` (Assum) |
| `/public_html/catalog/view/theme/default/template/product/manufacturer_info.twig` | Brand PLP heading `h2` → `h1` |

## Target pages (after)

| URL | Meta description | H1 |
|-----|------------------|-----|
| `/about_us` | present (134 chars) | О нас |
| `/terms` | present (115 chars) | Условия соглашения |
| `/brands/assum` | present (133 chars) | Assum |

## Unchanged

- SEO URL keywords and canonicals
- Category/product data
- Sitemap/robots/llms
- Lari redirects (Run 4.242)
- `/contact` canonical policy
- Import/monitor/cron
- Header/footer/Yandex

## Rollback

1. Run `rollback/db-rollback-plan.sql` from Storage `deployments/SITE-002-PROD-AUDIT-WAVE-E-INFO-META-H1-01/rollback/`
2. Re-upload pre-patch files from Storage `source-before/` per `rollback/source-before-manifest.json`

## Report

[sites/site-002/reports/SITE-002-PROD-AUDIT-WAVE-E-INFO-META-H1-01.md](../reports/SITE-002-PROD-AUDIT-WAVE-E-INFO-META-H1-01.md)
