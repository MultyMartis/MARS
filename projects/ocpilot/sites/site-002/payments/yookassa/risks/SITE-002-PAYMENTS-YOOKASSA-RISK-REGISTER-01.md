# SITE-002 — YooKassa risk register

**Register id:** SITE-002-PAYMENTS-YOOKASSA-RISK-REGISTER-01  
**Date:** 2026-09-09  
**Parent:** SITE-002-PAYMENTS-YOOKASSA-STRATEGY-ADOPTION-01  

> **Correction 2026-09-09 — [SITE-002-PAYMENTS-YOOKASSA-MVP-LK-AUTO-EMAIL-CORRECTION-01](../decisions/SITE-002-PAYMENTS-YOOKASSA-MVP-LK-AUTO-EMAIL-CORRECTION-01.md)**  
> Added R15–R18: bypassing ЛК; manager-sent payment email; email replacing ЛК; conflating order / payment / fulfillment statuses.

Risks are for **strategy and future implementation**. This wave does not create money movement. Residual risk of **docs-only** work is mainly: later teams ignoring the adopted sequence.

| ID | Risk | Why it matters for ЗПМ | Mitigation (strategy) |
|----|------|------------------------|------------------------|
| R01 | Wrong business model | Universal cart payment takes money before комплектация / цена / доставка are reliable. | Payment links after manager approval first. Cart/checkout not phase 1. |
| R02 | Paid before manager approval | Buyer pays a stale cart; manager cannot fulfil or must refund. | Link only after согласование. No checkout activation in MVP. |
| R03 | Stale price / stock / delivery | Catalogue and live fulfilment diverge. | Fix amount, stock implication, and delivery **before** the link. |
| R04 | VAT / receipt errors | Wrong NDS on receipt vs счёт; tax and buyer claims. | Accounting decides VAT and fiscalization **before payment code**. |
| R05 | Second receipt missed | Prepayment without отгрузка receipt (54-ФЗ). | Confirm prepayment / second-receipt rules in checklist; do not automate until known. |
| R06 | Refund process missing | Money captured, order cancelled, no operational refund. | Confirm refund owner and cabinet process before live links at scale. |
| R07 | B2B method refund limitations | SberBusiness / similar may not refund like card. | SberBusiness is a **separate** option; confirm limits before offering. |
| R08 | `return_url` trusted incorrectly | Buyer lands on success page; payment pending/fail; stock released or order marked paid. | UX only. Confirm via webhook / API. MVP: cabinet check, not return_url. |
| R09 | Webhook duplicated / delayed / missed | Double status updates or never-paid / paid-unnoticed. | Idempotency and API reconcile later; MVP is manual cabinet. |
| R10 | Status mismatch | `payment.succeeded` treated as shipped / status 5 «Сделка завершена». | Three statuses: payment / business / receipt. Do not use status 5 as paid. |
| R11 | Secret leakage | shopId/secret in git, chat, or report. | Ignored Storage only; this wave no secrets print/edit. |
| R12 | Accidental real payment | Test on live keys; real charge during “discovery”. | No test order / real payment in this operation. Test mode first later. |
| R13 | PHP 7.4 / platform risk | EOL runtime for future module/API; security and support. | Parallel hardening / staging / upgrade plan. Do not rush module onto this PHP. |
| R14 | Git cannot roll back money | Revert of code does not undo capture, payout, or receipt. | Treat money ops as irreversible; staging; manual pilot; no git-as-backup for payments. |
| R15 | Payment MVP bypasses ЛК | Client has no in-site payment surface; process lives only in email/manager chat; ЛК becomes a dead account. | ЛК is a **mandatory MVP surface**. Do not ship links-only email. |
| R16 | Manager manually sends payment email | Duplicate/wrong links, missed documents, no stored link on the order, audit gap. | Site sends the email **automatically** after approval. Manager does not assemble/send it. |
| R17 | Email treated as replacement for ЛК | Logged-out or returning client cannot find the same payment data; support load; status drift. | Email is a **duplicate notification**. Same block must exist in ЛК. |
| R18 | Order / payment / fulfillment statuses conflated | Client or manager treats OC status as paid, or paid as shipped. | Keep three lines: order/request status, payment status, fulfillment status. Do not map paid → OC status 5. |

---

## Risk of ignoring this adoption

If a later charter installs the official module “because discovery said compatible”, R01–R03 and R10 return. Sequencing in the roadmap is the control.

---

## Out of this register

SEO, robots, M9, PDP, dirty-main git, and category canonical architecture are **out of payments scope**. They are not payment risks; they must not be “fixed” in a payments wave.
