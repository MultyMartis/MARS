# SITE-002-STABLE-PROD-LOAD-MORE-01

**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** PRODUCTION — https://bzpm.ru/  
**Issued:** 2026-07-06  
**Operation:** `SITE-002-PROD-LOAD-MORE-01` (OCPilot Run 4.185)  
**Parent checkpoint:** `SITE-002-STABLE-PROD-CRON-BEGET-ACTIVE-01`

---

## Summary

Catalog product listing pages use **load-more append UX** with counter «Показано X из Y». Numeric pagination hidden as primary UI when JavaScript active (`js-load-more` on `<html>`). Direct `page=N` URLs remain valid server-side.

| Field | Value |
|-------|-------|
| Primary CTA | «Показать ещё» (`.pagination__more[data-next]`) |
| Counter | `[data-load-more-counter]` — «Показано X из Y» |
| Append target | `.category__grid` — `.p-card` elements |
| JS handler | `initLoadMore()` in `/assets/js/main.js` |
| Numeric pages | Hidden via `.js-load-more .pagination__pages` |
| Cron/import/mail | **Untouched** |

---

## Changed files (Production)

| Remote path | Role |
|-------------|------|
| `/public_html/catalog/view/theme/default/template/product/category.twig` | Counter + pagination wrap |
| `/public_html/catalog/controller/product/category.php` | `product_total`, `product_shown` data |
| `/public_html/assets/js/main.js` | `initLoadMore()` append handler |
| `/public_html/assets/css/style.css` | Load-more visibility rules |

---

## Verification evidence

| Check | Result |
|-------|--------|
| Primary URL HTTP 200 | https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly |
| Append 15→30 on click | **PASS** (desktop + mobile Playwright) |
| Hub URL unchanged | https://bzpm.ru/katalog/nejtralnoe-oborudovanie |
| Rollback path | `deployments/SITE-002-PROD-LOAD-MORE-01/rollback/` |

---

## Rollback

Upload rollback copies via `site-002-prod-load-more-01.py rollback` or manual FTP from Storage rollback folder.

---

## Report

[sites/site-002/reports/SITE-002-PROD-LOAD-MORE-01.md](../reports/SITE-002-PROD-LOAD-MORE-01.md)
