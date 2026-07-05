# SITE-002-STABLE-PROD-SEO-ROBOTS-01

**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** PRODUCTION — https://bzpm.ru/  
**Issued:** 2026-07-06  
**Operation:** `SITE-002-PROD-SEO-READINESS-ROBOTS-01` (OCPilot Run 4.188)  
**Parent checkpoint:** `SITE-002-STABLE-PROD-LOAD-MORE-01`

---

## Summary

Production SEO readiness baseline: **non-product meta audit completed**, **robots.txt deployed**, product PDP meta **excluded**, meta fix plan issued for follow-up operation.

| Field | Value |
|-------|-------|
| robots.txt URL | https://bzpm.ru/robots.txt |
| Remote path | `/public_html/robots.txt` |
| Deploy SHA-256 | `9fe056f7a2d84112ce053d20083537ef245d8bf083d41c0273058ccec701a9d8` |
| Valid sitemap | **NOT FOUND** — `Sitemap:` omitted |
| Meta audit URLs | 43 non-product |
| Meta PASS / WARN / FAIL | 12 / 14 / 17 |
| Operator Twig analytics | **SAFE UNKNOWN** at audit time — not modified |
| Load More / cron / mail | **Untouched** |

---

## Changed files (Production)

| Remote path | Role |
|-------------|------|
| `/public_html/robots.txt` | SEO crawl rules — conservative OpenCart pattern + Yandex Clean-param |

---

## Verification evidence

| Check | Result |
|-------|--------|
| robots.txt HTTP 200 | **PASS** |
| Content matches prepared | **PASS** |
| Public catalog URLs HTTP 200 | **PASS** |
| Twig/header/footer modified | **NO** |

---

## Rollback

Upload `deployments/SITE-002-PROD-SEO-READINESS-ROBOTS-01/rollback/robots.txt` to `/public_html/robots.txt`.

Pre-deploy SHA-256: `72ab7d21cdb7f66bf69fcc2cd21a2571bad402e38b626377516d7fd4f22ba723`

---

## Report

[sites/site-002/reports/SITE-002-PROD-SEO-READINESS-ROBOTS-01.md](../reports/SITE-002-PROD-SEO-READINESS-ROBOTS-01.md)
