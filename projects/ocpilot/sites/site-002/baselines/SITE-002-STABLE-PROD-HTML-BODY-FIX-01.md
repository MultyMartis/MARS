# SITE-002-STABLE-PROD-HTML-BODY-FIX-01

**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** PRODUCTION — https://bzpm.ru/  
**Issued:** 2026-07-06  
**Operation:** `SITE-002-PROD-HTML-BODY-DUPLICATE-FIX-01` (OCPilot Run 4.190)  
**Parent checkpoint:** `SITE-002-STABLE-PROD-SEO-ROBOTS-01`

---

## Summary

Production HTML structure baseline: **duplicate `<body>` / preloader / overlay removed** from live `header.twig`; Yandex Webmaster meta preserved; Yandex Metrika in footer unchanged.

| Field | Value |
|-------|-------|
| Changed remote path | `/public_html/catalog/view/theme/default/template/common/header.twig` |
| Pre-fix SHA-256 | `8e41c9bfc3ab6c31a519f3e0b754ac11cacb0f93ca2e71e0c8b9eddf16a50ecb` |
| Post-fix SHA-256 | `4fac43f8823e9e4c8c60b4d541455eec29a06256f73fbdd73a08f0875d09d8c7` |
| Live `<body` count (4 URLs) | **1** each (was 2) |
| Yandex blocks | **unchanged** |
| robots.txt / sitemap / meta | **untouched** |
| Load More / cron / mail | **untouched** |

---

## Changed files (Production)

| Remote path | Role |
|-------------|------|
| `catalog/view/theme/default/template/common/header.twig` | Remove duplicate body + global preloader + page_overlay block (L113–126) |

---

## Verification evidence

| Check | Result |
|-------|--------|
| HTTP 200 on 4 sampled URLs | **PASS** |
| Exactly one `<body` per page | **PASS** |
| Yandex Metrika + Webmaster on live HTML | **PASS** |
| Upload hash matches prepared | **PASS** |
| footer.twig modified | **NO** |

---

## Rollback

Upload `deployments/SITE-002-PROD-HTML-BODY-DUPLICATE-FIX-01/rollback/header.twig` to `/public_html/catalog/view/theme/default/template/common/header.twig`.

Pre-fix SHA-256: `8e41c9bfc3ab6c31a519f3e0b754ac11cacb0f93ca2e71e0c8b9eddf16a50ecb`

---

## Report

[sites/site-002/reports/SITE-002-PROD-HTML-BODY-DUPLICATE-FIX-01.md](../reports/SITE-002-PROD-HTML-BODY-DUPLICATE-FIX-01.md)
