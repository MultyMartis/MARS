# SITE-002-MAIL-SYSTEM-DISCOVERY-01

**Site:** SITE-002 (ЗПМ / bzpm.ru)
**Environment:** PRODUCTION — https://bzpm.ru/
**Issued:** 2026-07-08
**Operation:** `SITE-002-PROD-MAIL-SYSTEM-DISCOVERY-01` (OCPilot Run 4.222)
**Type:** Read-only mail architecture audit baseline — **not** a Production mutation checkpoint
**Parent checkpoint:** `SITE-002-STABLE-PROD-CATEGORY-ENTRYPOINTS-SORT-AZ-01`

---

## Summary

Mail system authority mapped for redesign planning. **No Production mutation.**

| Field | Value |
|-------|-------|
| Primary form handler | `catalog/controller/checkout/anketa.php` |
| Form POST route | `checkout/anketa` |
| Admin form recipients | `config_mail_alert_email` |
| Order admin alerts | `config_email` + `config_mail_alert_email` |
| Standard order mail | `catalog/controller/mail/order.php` + twig templates |
| Current form mail design | minimal inline HTML — no template |
| Service info in admin mail | **absent** |
| Customer form copy | **not implemented** |
| FTP files downloaded | 53 |
| HTTP forms inventoried | 29 instances / 6 URLs |
| Production mutations | **0** |

---

## Redesign readiness

- Design system proposal: documented
- Implementation option: **Hybrid (D)** recommended
- Future charters: 5 prepared (design system → admin forms → customer forms → account → order)

Report: [SITE-002-PROD-MAIL-SYSTEM-DISCOVERY-01.md](../reports/SITE-002-PROD-MAIL-SYSTEM-DISCOVERY-01.md)
