# SITE-002 — Info Page Forms Discovery Baseline

**Operation:** `SITE-002-PROD-INFO-PAGE-FORMS-DISCOVERY-01` (OCPilot Run 4.229)  
**Date:** 2026-07-09  
**Type:** read-only discovery audit baseline — **not** a production checkpoint  
**Production checkpoint (unchanged):** `SITE-002-STABLE-PROD-MAIL-CUSTOMER-FORMS-01`

---

## Summary

Five information-page Corporate CTA forms on Production are **present but non-functional** — markup exists, no JS submit handler binds, `action="#"` prevents useful native submit.

| Page | URL | Form | Status |
|------|-----|------|--------|
| Оборудование на заказ | `/custom-equipment` | `zpm-custom-form` | broken — dialog=7 mislabel |
| Оплата | `/payment-methods` | `zpm-payment-form` | broken — no dialog, no handler |
| Доставка | `/delivery` | `zpm-delivery-form` | broken — no dialog, no handler |
| Дилерам | `/dealers` | `zpm-dealers-form` | broken — dialog=7 ok, no handler |
| Гарантия | `/guarantee` | `zpm-warranty-form` | broken — no dialog, no handler |

## Authority

- Report: [../reports/SITE-002-PROD-INFO-PAGE-FORMS-DISCOVERY-01.md](../reports/SITE-002-PROD-INFO-PAGE-FORMS-DISCOVERY-01.md)
- Storage: `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-INFO-PAGE-FORMS-DISCOVERY-01\`
- Tool: [../tools/site-002-prod-info-page-forms-discovery-01.py](../tools/site-002-prod-info-page-forms-discovery-01.py)

## Next production task

`SITE-002-PROD-INFO-PAGE-FORMS-INTEGRATION-01` — charter in Storage `implementation-plan/`.

## Production mutation

**0** — read-only discovery only.
