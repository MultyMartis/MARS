# SITE-002-STABLE-PROD-BRAND-ZPM-01

**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** PRODUCTION — https://bzpm.ru/  
**Issued:** 2026-07-07  
**Operation:** `SITE-002-PROD-BRAND-ZPM-REMEDIATION-01` (OCPilot Run 4.205)  
**Parent checkpoint:** `SITE-002-STABLE-PROD-LLMS-TXT-UTF8-01`

---

## Summary

Public brand text corrected: **БЗПМ** → **ЗПМ** in llms.txt, controller meta literals, product meta generator, and 3 category admin SEO fields. Domain `bzpm.ru` unchanged. UTF-8 BOM on llms.txt preserved. Robots/sitemap/Yandex/single-body/product-meta infrastructure preserved.

| Field | Value |
|-------|--------|
| Files changed | 10 FTP overwrites |
| Admin saves | 3 category SEO meta_description fields |
| Public `БЗПМ` in sampled crawl | **0** (was 37 URLs / 59 occurrences) |
| llms.txt UTF-8 BOM | **preserved** |
| sitemap URL count | **1320** |
| DB writes | **0** |
| header.twig / footer.twig | **unchanged** |

---

## Public brand policy (active)

- **Correct public Russian brand:** ЗПМ  
- **Forbidden in public content:** БЗПМ  
- **Domain:** bzpm.ru (URL only)

---

## Rollback

Restore files from Storage:

`deployments/SITE-002-PROD-BRAND-ZPM-REMEDIATION-01/rollback/`

Restore admin category SEO from:

`deployments/SITE-002-PROD-BRAND-ZPM-REMEDIATION-01/admin-evidence/category-brand-before.json`

---

## Report

[sites/site-002/reports/SITE-002-PROD-BRAND-ZPM-REMEDIATION-01.md](../reports/SITE-002-PROD-BRAND-ZPM-REMEDIATION-01.md)
