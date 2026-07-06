# SITE-002-STABLE-PROD-LLMS-TXT-UTF8-01

**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** PRODUCTION — https://bzpm.ru/  
**Issued:** 2026-07-07  
**Operation:** `SITE-002-PROD-LLMS-TXT-ENCODING-FIX-01` (OCPilot Run 4.204)  
**Parent checkpoint:** `SITE-002-STABLE-PROD-LLMS-TXT-01`

---

## Summary

Production `llms.txt` reuploaded with **UTF-8 BOM** for correct browser/HTTP client Cyrillic display. Public URL https://bzpm.ru/llms.txt — HTTP 200, readable Russian, no mojibake. Semantic content unchanged from Run 4.203. No `.htaccess`, PHP, DB, admin, header/footer, robots, sitemap, or product meta changes.

| Field | Value |
|-------|--------|
| File changed | `/public_html/llms.txt` (1 overwrite) |
| Public URL | https://bzpm.ru/llms.txt |
| SHA-256 (before, Run 4.203) | `e2e752c6dab1ebf751283cc3013fee711925c77a4c764d2474500383c8b8de58` |
| SHA-256 (after, UTF-8 BOM) | `126a2508950f4158fc732ab310ada45d59ab781d18861565fe291733089ac313` |
| BOM added | **yes** (+3 bytes) |
| Content-Type charset | still `text/plain` without explicit charset — BOM sufficient |
| `.htaccess` change | **0** |
| DB writes | **0** |
| Admin saves | **0** |
| PHP changes | **0** |
| header.twig / footer.twig | **unchanged** |
| robots / sitemap | **unchanged** (1320 URLs) |
| Product meta generator | **unchanged** (Run 4.202 keywords v1.1) |
| Yandex / single body | **preserved** |

---

## Rollback

Restore pre-fix file from Storage deployment backup:

`deployments/SITE-002-PROD-LLMS-TXT-ENCODING-FIX-01/rollback/llms.txt`

SHA-256: `e2e752c6dab1ebf751283cc3013fee711925c77a4c764d2474500383c8b8de58`

---

## Report

[sites/site-002/reports/SITE-002-PROD-LLMS-TXT-ENCODING-FIX-01.md](../reports/SITE-002-PROD-LLMS-TXT-ENCODING-FIX-01.md)
