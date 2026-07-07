# SITE-002-SITEMAP-AUTHORITY-DISCOVERY-01

**Site:** SITE-002 (ЗПМ / bzpm.ru)  
**Environment:** PRODUCTION — https://bzpm.ru/  
**Issued:** 2026-07-07  
**Operation:** `SITE-002-PROD-SITEMAP-AUTHORITY-DISCOVERY-01` (OCPilot Run 4.214)  
**Type:** Read-only authority audit baseline — **not** a Production mutation checkpoint  
**Parent checkpoint:** `SITE-002-STABLE-PROD-CATALOG-BRANCH-FOLLOWUP-01`  
**Prior audit baseline:** `SITE-002-POST-1C-CATALOG-MONITOR-02`

---

## Summary

Sitemap authority confirmed: **automatic OpenCart Google Sitemap feed** — not manually maintained by MARS.

| Field | Value |
|-------|-------|
| Public URL | https://bzpm.ru/sitemap.xml |
| Route | `extension/feed/google_sitemap` |
| Controller | `/public_html/catalog/controller/extension/feed/google_sitemap.php` |
| Physical file | **absent** |
| `.htaccess` rewrite | `^sitemap.xml$` → feed route |
| Live URL count | **1377** |
| Sitemap SHA-256 | `9c81305483d7fb79b829e562598e5a3a0eb74a29350fae142fa78f97c3eca6c1` |
| Generation | live per HTTP request |
| Manual MARS maintenance | **no** |
| Production mutations | **0** |

---

## Policy anchor

- MARS: monitor/audit sitemap delta only.
- Do not manually edit `sitemap.xml` in normal operations.
- 1C catalog growth → sitemap growth is expected.
- Fix problematic URLs at catalog/SEO source.

Report: [SITE-002-PROD-SITEMAP-AUTHORITY-DISCOVERY-01.md](../reports/SITE-002-PROD-SITEMAP-AUTHORITY-DISCOVERY-01.md)
