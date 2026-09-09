# SITE-002 — YooKassa MVP: payment links after manager approval

**Plan id:** SITE-002-PAYMENTS-YOOKASSA-MVP-PAYMENT-LINKS-PLAN-01  
**Parent decision:** SITE-002-PAYMENTS-YOOKASSA-STRATEGY-ADOPTION-01  
**Date:** 2026-09-09  
**Status:** plan only. **No implementation in this wave.**  
**Correction:** SITE-002-PAYMENTS-YOOKASSA-MVP-LK-AUTO-EMAIL-CORRECTION-01 (2026-09-09).

> MVP formula: **manager approval inside site + payment block in existing customer ЛК + automatic email with YooKassa link**.  
> ЛК is a **mandatory MVP surface**. The manager does **not** send the payment email. Email is automatic after approval. Manual remainder: **reconciliation**, unless later automated.

---

## Purpose

Define the first operational model for YooKassa at ЗПМ: **individual payment links after the manager has approved a commercial order inside the site/admin workflow**, with the same payment information in the **existing customer account (ЛК)** and an **automatic email** (documents + YooKassa link). This is not checkout activation and not a replacement of bank invoice / bank transfer. Phase 1 is **not** “email + manager only”.

---

## Current request / anketa / manager process (unchanged)

1. Buyer submits a **заявка** (primarily custom anketa; OpenCart cart/checkout is not the commercial source of truth).
2. Manager checks the request: комплектация, наличие, доставка, цена, VAT.
3. Manager issues **КП** and ordinary **счёт** (bank invoice).
4. Buyer pays by **безнал** (bank transfer) as today.

YooKassa does **not** enter this path until step 3–4, and only if the manager (and accounting rules) choose the online-link option for that order.

Discovery counts (not re-probed): `oc_anketa` 94; `oc_order` 18, mostly `free_checkout` / status 1.

---

## When the site creates or attaches a payment link

Only after the manager has **approved payment inside the site/admin workflow**, and:

- the commercial order is **согласован** (manager approved);
- **amount** is final for this payment (or an explicitly agreed prepayment amount);
- **payer** is identified (who pays: company / person as required by fiscal rules);
- **VAT** treatment for this payment is decided;
- **delivery** cost and whether it is in this payment / this receipt is decided;
- **receipt need** is decided (who fiscalizes, what is in the receipt);
- **order / reference number** exists (КП number, счёт number, anketa id, or an internal commercial order id).

The manager does **not** create a link from an unreviewed cart or from a raw anketa.

---

## What documents remain primary

- КП remains the commercial offer.
- Ordinary bank **счёт** / bank transfer remains a full payment path.
- YooKassa payment link is an **additional** way to pay an already-agreed amount.
- The link must carry the same reference as the счёт / КП so accounting can match the payment.

Do not treat the YooKassa UI or `return_url` as the commercial document.

---

## How ordinary bank invoice remains

- Keep issuing the bank invoice as today.
- Do not disable or hide безнал because a link exists.
- Buyer may pay by bank transfer **or** by the YooKassa link — not both for the same amount unless a partial-payment rule is later approved.
- MVP reconciliation is manual: manager / accounting matches incoming YooKassa payout or cabinet status to the счёт / КП.

---

## Payment methods to consider first

| Method | Phase 1 stance |
|--------|----------------|
| Card | Consider first, if tariff and fiscalization allow. |
| SBP | Consider first, if available on the chosen tariff. |
| SberPay | Consider first **if available** on the shop / tariff. Do not invent availability. |
| SberBusiness | **Separate B2B option only.** Not the default consumer methods bundle. Confirm need, limits, VAT-per-order constraints, and refund rules before offering. |

Do not enable “all methods YooKassa can turn on” without accounting / tariff confirmation.

---

## Data that must be fixed before the link

1. **Amount** — exact копейки / currency (RUB unless later decided otherwise).
2. **Payer** — legal name / INN if required for the chosen method and receipt.
3. **VAT** — rate(s) for this payment; mixed VAT is a stop until accounting answers.
4. **Delivery** — included in this payment or not; how it appears on the receipt.
5. **Receipt need** — whether this payment requires a 54-ФЗ receipt now; who is the receipt sender.
6. **Order / reference number** — stable id shared with КП / счёт / anketa.

If any of these is unknown, **do not create the link**.

---

## Who sees the payment result

- **Buyer (ЛК — mandatory MVP surface):** order/request, statuses, amount, documents / КП / счёт if available, YooKassa payment link, payment status. Same data as the automatic email.
- **Buyer (YooKassa UI):** YooKassa payment page and YooKassa’s own success/fail screen. `return_url` is UX only — **not** confirmation.
- **Buyer (email):** automatic notification after manager approval — duplicate of the ЛК payment block, not a replacement.
- **Manager:** approves payment **inside site/admin**; sees stored link/status on the order/request; YooKassa cabinet for MVP reconciliation; later API/webhook.
- **Accounting:** payout / registry in YooKassa / bank statement; matches to счёт. Roles confirmed in the business checklist.
- **OpenCart admin:** **no automatic business order-status change** in MVP. Do not write paid into `oc_order` status 5. Storing the payment link/status against the request is an MVP **site** action, distinct from OC status 5.

---

## Manual reconciliation first

MVP operating loop:

1. Manager reviews composition, price, availability, delivery, payer, then **approves payment inside the site/admin workflow**.
2. Site **creates or attaches** the YooKassa payment link and **stores** it (and payment status) against the order/request. (Creating the link in the YooKassa cabinet and attaching it in the site is allowed in MVP; the manager still does not run a side-channel email.)
3. Site **automatically** emails the client: summary, documents / КП / счёт if available, YooKassa link, bank-transfer remains, manager contact. Manager does **not** assemble/send this payment email.
4. Client sees the **same** payment block in ЛК.
5. Buyer pays or does not pay (YooKassa link **or** ordinary bank transfer — not both for the same amount unless later approved).
6. Manager / accounting **reconciles** in the YooKassa cabinet / payout (manual in MVP).
7. Commercial “оплачено” is a **business** mark — not an OpenCart checkout event and **not** status 5.

No webhook automation, no 1C auto-posting, no checkout module in this MVP. Webhook/API status updates are **later**.

---

## No automatic order status change in MVP

Unless a later charter explicitly approves it:

- Do not change `oc_order` status from a payment event.
- Do not map `payment.succeeded` to status 5 «Сделка завершена».
- Do not create a new OpenCart status in production in this wave.
- Keep payment status, business order status and receipt status **separate** even when only humans update them.

---

## No checkout activation in MVP

- Do not install the official OpenCart YooKassa module as the MVP vehicle.
- Do not enable YooKassa (or any new method) in OpenCart checkout settings.
- Do not tell buyers to “pay in cart” for the general catalogue.
- Standard checkout may remain as it is today (`cod`, `free_checkout`); this plan does not activate it as an online-pay path.

---

## Explicit non-goals of this MVP

- Production module install, DB write, FTP, secrets in repo, test/real payment from Cursor.
- Universal checkout payment; official OpenCart YooKassa module as first production step.
- Webhook/API **status** automation (later). A later “generate link via API” button is later if MVP used cabinet-attach.
- Hybrid whitelist checkout.
- PHP upgrade (parallel track — see roadmap).
- 1C/CRM sync.
- **Not a non-goal:** existing customer ЛК as payment surface; automatic email after approval; manager approval inside the site. Those **are** MVP.

Canonical workflow summary: `SITE-002-PAYMENTS-YOOKASSA-MVP-APPROVED-WORKFLOW-01.md`.

---

## Exit criteria to leave “manual links” MVP

Only after business checklist answers and a **manual pilot** with test mode (and then limited live links under accounting rules):

- Repeatable manager procedure exists.
- Reconciliation works without lost payments or double-pay.
- Fiscal receipts (if required) match the payment.
- Refund path is known.

Then a later charter may introduce API-assisted link creation. That is **not** this MVP.
