# SITE-002 — YooKassa technical readiness note

**Note id:** SITE-002-PAYMENTS-YOOKASSA-TECHNICAL-READINESS-NOTE-01  
**Date:** 2026-09-09  
**Parent:** SITE-002-PAYMENTS-YOOKASSA-STRATEGY-ADOPTION-01  
**Source facts:** SITE-002-PAYMENTS-YOOKASSA-DISCOVERY-READONLY-01 (not re-probed).

> **Correction 2026-09-09 — [SITE-002-PAYMENTS-YOOKASSA-MVP-LK-AUTO-EMAIL-CORRECTION-01](../decisions/SITE-002-PAYMENTS-YOOKASSA-MVP-LK-AUTO-EMAIL-CORRECTION-01.md)**  
> MVP surfaces: **site/admin approval**, **customer ЛК payment block**, **automatic payment email**. Bind the payment link/status to the order/request. ЛК is not optional. Implementation is not authorized.

This note is **readiness and constraints**. It does not authorize install, API keys, or checkout activation.

---

## Platform (from discovery)

| Item | Value |
|------|--------|
| CMS | OpenCart / ocStore 3.0.3.9 |
| Theme | default |
| Web PHP | 7.4.33 |
| HTTPS | live; `config_secure=1` |
| cURL | present |
| Enabled payments now | `cod`, `free_checkout` |
| YooKassa / yandex_money files | none installed |
| Anketa vs Order | `oc_anketa` 94 vs `oc_order` 18 (mostly free_checkout / status 1) |

---

## PHP 7.4.33 EOL risk

PHP 7.4 is end-of-life. Any later payment **module or API** work needs a **separate** hardening / staging / upgrade plan. Do not treat “cURL exists and OC 3.0.3.9 can load a module” as production-safe for money.

Roadmap stage 12 runs **in parallel** with links MVP. EOL PHP is not a reason to skip fiscal decisions; it is a reason not to rush checkout-module install on this runtime.

---

## Official OC3 module: compatible, not first step

Discovery: official OpenCart 3 module is **version-compatible** with 3.0.3.9. It is **not** a business drop-in:

- built around OpenCart Order / checkout;
- ЗПМ commercial object is заявка / manager / КП / счёт;
- callback route is **SAFE UNKNOWN** until a real module/API exists;
- installing it as phase 1 would pull the process into cart payment.

Adopted strategy: **do not install the module as the first production step.** Evaluate it only if hybrid checkout for a simple-SKU whitelist becomes a real process (roadmap stage 11).

---

## Custom anketa vs OpenCart Order mismatch

Anketa is the dominant B2B lead path. Checkout exists but is not checkout-first commercially.

MVP links must bind to **КП / счёт / anketa / commercial reference**, not assume `oc_order_id` from checkout. The site **stores** the payment link and payment status against that order/request so **ЛК** and **auto-email** show the same data.

Later API may still create or update an OpenCart order **only if** a later charter defines that mapping. Default: do not force every paid link into `oc_order`.

### MVP surfaces (design, not implementation)

| Surface | Role in MVP |
|---------|-------------|
| Site / admin | Manager reviews and **approves payment**. Site creates or attaches the YooKassa link. |
| Customer account / ЛК | **Mandatory** payment block: order, status, amount, documents if available, payment link, payment status. |
| Automatic email | Duplicate notification after approval. Not a replacement for ЛК. Not assembled by the manager. |
| YooKassa cabinet | Manual **reconciliation** until webhook/API. |

PHP 7.4 / no module-first / three statuses / no `return_url` as truth remain.

---

## Staging / sandbox before module / API

Required before any automation:

- YooKassa test shop / test mode;
- staging site or isolated procedure so a test payment cannot hit production checkout settings;
- test payment, receipt (if required), refund **before** production automation.

This operation does **not** create staging or run test payments.

---

## Secrets

Later required (not in this wave): shopId, secret key, test shopId, test secret, webhook URL after install.

**Storage only (ignored local):** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md`

- Never print secrets in chat, git, or reports.
- This wave: **no secrets edit, no secrets read for implementation.**
- Confirm secret storage **owner** in the business checklist.

---

## Webhook / API later

- Do not trust `return_url` as paid.
- Use webhook and/or API confirmation.
- Design for duplicate, delayed, and missed webhooks (**idempotency later**).
- Callback URL is unknown until the integration exists. Do not invent a production webhook path in this note.

---

## Three statuses stay separate

1. **Payment status** (YooKassa, e.g. `payment.succeeded`).
2. **Business order status** (manager / 1C / «можно отгружать»).
3. **Receipt status** (54-ФЗ / OFD success, second receipt).

Do not map paid to OpenCart status 5 «Сделка завершена». Discovery: no dedicated paid / waiting-for-capture status. Do not invent one in production in MVP.

MVP: humans keep these statuses apart. Automation must not collapse them.

---

## Tests before production automation

Before webhooks change any business state:

- test payment;
- test receipt path if fiscalization is on;
- test refund.

Accidental real payment is a named risk. Git cannot roll back money.

---

## No direct checkout activation yet

- No OpenCart payment method enablement.
- No official module install.
- No “pay in cart” for the general catalogue.
- Technical capability of checkout ≠ adopted commercial model.
