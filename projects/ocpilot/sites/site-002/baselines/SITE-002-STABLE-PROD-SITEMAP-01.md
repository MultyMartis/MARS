# SITE-002-STABLE-PROD-SITEMAP-01

**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** PRODUCTION — https://bzpm.ru/  
**Issued:** 2026-07-06  
**Operation:** `SITE-002-PROD-SITEMAP-ENABLE-01` (OCPilot Run 4.191)  
**Parent checkpoint:** `SITE-002-STABLE-PROD-HTML-BODY-FIX-01`

---

## Summary

Production SEO crawl baseline: **valid XML sitemap live** via OpenCart Google Sitemap feed; **robots.txt** includes single `Sitemap:` directive.

| Field | Value |
|-------|-------|
| Valid sitemap URL | https://bzpm.ru/sitemap.xml |
| Alternate feed route | https://bzpm.ru/index.php?route=extension/feed/google_sitemap |
| Sitemap URL count | **1320** |
| Google Sitemap admin status | **Enabled** (`feed_google_sitemap_status=1`) |
| robots.txt Sitemap line | `Sitemap: https://bzpm.ru/sitemap.xml` |
| robots post-deploy SHA-256 | `8428d6e43b5f5cc79167504137491a4300c4fe92328768e64e860db13a2b6d40` |
| Changed remote paths | `/public_html/robots.txt` only (file) + admin setting |
| Twig / Yandex / duplicate body | **unchanged / preserved** |
| Meta / product / cron / mail | **untouched** |

---

## Verification evidence

| Check | Result |
|-------|--------|
| Sitemap HTTP 200 + valid XML | **PASS** |
| robots exactly one Sitemap directive | **PASS** |
| Prior robots Disallow rules preserved | **PASS** |
| 4-URL spot check (Yandex + single body) | **PASS** |

---

## Rollback

1. Upload `deployments/SITE-002-PROD-SITEMAP-ENABLE-01/rollback/robots.txt` → `/public_html/robots.txt`  
2. Admin: set Google Sitemap status → Disabled  

Pre-robots SHA-256: `9fe056f7a2d84112ce053d20083537ef245d8bf083d41c0273058ccec701a9d8`

---

## Report

[sites/site-002/reports/SITE-002-PROD-SITEMAP-ENABLE-01.md](../reports/SITE-002-PROD-SITEMAP-ENABLE-01.md)
