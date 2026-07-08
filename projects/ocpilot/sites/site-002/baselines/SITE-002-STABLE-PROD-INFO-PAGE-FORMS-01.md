# SITE-002 — Stable Production Info Page Forms Baseline

**Operation:** `SITE-002-PROD-INFO-PAGE-FORMS-INTEGRATION-01` (OCPilot Run 4.230)  
**Date:** 2026-07-09  
**Type:** production checkpoint  
**Parent checkpoint:** `SITE-002-STABLE-PROD-MAIL-CUSTOMER-FORMS-01`

---

## Summary

Five information-page Corporate CTA forms on Production are **integrated** with SITE-002 AJAX mail pipeline:

| Page | URL | Dialog | Status |
|------|-----|--------|--------|
| Оборудование на заказ | `/custom-equipment` | 11 | **verified** |
| Оплата | `/payment-methods` | 9 | **verified** |
| Доставка | `/delivery` | 8 | **verified** |
| Дилерам | `/dealers` | 7 | **verified** |
| Гарантия | `/guarantee` | 10 | **verified** |

## Behavior

- Submit: `checkout/anketa` + CSRF + reCAPTCHA v3 + loading/abort UX.
- Success: inline panel (icon `#zpm_ico__successful`, «Спасибо», «Ваша заявка отправлена!»).
- Customer copy: conditional (valid posted email or logged-in customer); **no** service info in customer mail.
- Live HTML wired via `information/*.twig` inline corp CTA blocks.

## Authority

- Report: [../reports/SITE-002-PROD-INFO-PAGE-FORMS-INTEGRATION-01.md](../reports/SITE-002-PROD-INFO-PAGE-FORMS-INTEGRATION-01.md)
- Storage: `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-INFO-PAGE-FORMS-INTEGRATION-01\`
- Tool: [../tools/site-002-prod-info-page-forms-integration-01.py](../tools/site-002-prod-info-page-forms-integration-01.py)

## Production mutation

**14** exact FTP file overwrites; **0** DB/admin/SMTP/header/footer changes.
