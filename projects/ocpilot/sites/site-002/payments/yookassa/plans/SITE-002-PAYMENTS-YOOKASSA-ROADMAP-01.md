# SITE-002 — YooKassa later roadmap

**Plan id:** SITE-002-PAYMENTS-YOOKASSA-ROADMAP-01  
**Parent decision:** SITE-002-PAYMENTS-YOOKASSA-STRATEGY-ADOPTION-01  
**Date:** 2026-09-09  
**Status:** staged roadmap. Later stages are **not** authorized by this document.

> **Correction 2026-09-09 — [SITE-002-PAYMENTS-YOOKASSA-MVP-LK-AUTO-EMAIL-CORRECTION-01](../decisions/SITE-002-PAYMENTS-YOOKASSA-MVP-LK-AUTO-EMAIL-CORRECTION-01.md)**  
> Stage 4 is **not** “email + manager only”. MVP formula: manager approval inside site + ЛК payment block + automatic email. Webhook/API status and fuller API “generate link” stay later (stages 6–7). Checkout-first remains rejected.

Each stage needs its own GO. Do not skip fiscal / tariff stages to “install the module”.

---

## Stage 1 — Strategy adoption

**This operation.** Adopt payment links first → API-assisted manager workflow → hybrid checkout later. No production change.

**Exit:** decision + MVP plan + checklist + risks published. Operator accepts next GO.

---

## Stage 2 — YooKassa account / contract / tariff

Operator / ЗПМ / accounting:

- Create or confirm YooKassa account.
- Confirm legal entity and settlement account.
- Confirm tariff, commission, payout terms, available methods.

**Not Cursor.** No keys in chat. Secrets later only in ignored Storage `...\site-002\secrets\secrets.md`.

---

## Stage 3 — Accounting / fiscal decision

Before any payment used as a business process:

- 54-ФЗ, KKT/OFD, who fiscalizes.
- VAT rates; delivery in receipt; prepayment / second receipt.
- Refunds; SberBusiness constraints if used.

**Exit:** checklist `SITE-002-PAYMENTS-YOOKASSA-BUSINESS-INPUTS-CHECKLIST-01` answered enough to run a **test-mode** pilot without inventing tax treatment.

---

## Stage 4 — Payment links MVP (ЛК + auto-email)

After stages 2–3 are confirmed enough for a pilot:

- Manager **approves payment inside the site/admin workflow**.
- Site **creates or attaches** a YooKassa payment link and **stores** it against the order/request.
- Site **automatically emails** the client (summary, documents if available, payment link).
- The **same** payment block is visible in the **existing customer account / ЛК** (mandatory MVP surface; UX fixes allowed).
- Ordinary invoice / bank transfer remains.
- No OpenCart checkout activation. No automatic OpenCart business-status change. No `return_url` as payment truth.
- **Manual remainder:** payment **reconciliation** in the YooKassa cabinet (and cabinet-create + attach if API create is not yet in this stage). Manager does **not** assemble/send the payment email.

Canonical: `SITE-002-PAYMENTS-YOOKASSA-MVP-APPROVED-WORKFLOW-01.md`.

Do **not** postpone ЛК or auto-email to stage 6.

---

## Stage 5 — Manual pilot

- Test shop / test mode first.
- Then a **limited** live pilot: defined SKU or defined counterparty, defined amount range, named manager.
- Test payment, receipt (if required), refund **before** any automation.
- Record misses: double pay, unpaid-but-shipped, receipt mismatch.

**Exit:** operator + accounting accept that links are operable.

---

## Stage 6 — Manager workflow / API-assisted link creation (later)

Productize **link creation** without opening the whole cart — **if** stage 4 started with cabinet-attach:

- Button / procedure «Сформировать ссылку на оплату» on the **already approved** request / commercial order.
- Still no universal checkout.
- Audit: who, when, amount, reference.

Stage 4 already requires **approval inside the site**, **ЛК**, and **auto-email**. Stage 6 is not “introduce ЛК”. It is API-assisted generation / richer manager tooling.

---

## Stage 7 — API + webhook status automation

- YooKassa API creates payments for approved amounts.
- Webhooks update **payment** status.
- Do not trust `return_url`.
- Idempotency for duplicate / delayed / missed webhooks.
- Still do not conflate payment / business / receipt statuses.
- Staging / sandbox required. PHP 7.4 EOL is in scope for this track’s hardening.

Callback route remains SAFE UNKNOWN until the actual integration exists.

---

## Stage 8 — 1C / CRM sync

Only after payment confirmation is reliable:

- Post paid / unpaid / refunded to 1C or CRM as accounting defines.
- Keep anketa / commercial order as the join key unless Order becomes real.

Do not invent a 1C connector in a payments MVP.

---

## Stage 9 — SKU eligibility rules

Define whitelist vs manager-mandatory:

- current price
- confirmed stock
- calculable delivery
- unambiguous VAT
- no manager approval required
- amount within payment limits

Everything else stays manager-approved.

---

## Stage 10 — Hybrid checkout for simple SKU

Only the whitelist from stage 9. Complex / high-value / B2B / custom stay on КП / счёт / link.

---

## Stage 11 — Official OpenCart module evaluation

Evaluate the official OC3 module **if and only if** checkout becomes a real commercial process for the whitelist (or a later operator decision).

The module is version-compatible with 3.0.3.9 in discovery, **not** a business drop-in, **not** stage 4.

If checkout never becomes the process, the module may never be installed. That is acceptable.

---

## Stage 12 — PHP / platform hardening (parallel)

PHP 7.4.33 is EOL. Payment module / API work needs:

- staging separate from dirty production assumptions;
- upgrade / isolation plan;
- no “we installed payments on EOL PHP with no plan”.

This track **runs in parallel** from stage 4 onward. It does not authorize skipping stages 2–3.

---

## Sequencing rule

Do not start stage 11 (module) or stage 10 (hybrid checkout) because they are “technically compatible”. Business reliability of the order comes first.
