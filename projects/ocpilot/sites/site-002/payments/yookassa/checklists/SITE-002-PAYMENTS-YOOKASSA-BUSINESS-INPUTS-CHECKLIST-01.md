# SITE-002 — YooKassa business inputs checklist

**Checklist id:** SITE-002-PAYMENTS-YOOKASSA-BUSINESS-INPUTS-CHECKLIST-01  
**Audience:** ЗПМ operator, accounting, YooKassa manager, Sber (if SberPay / SberBusiness).  
**Date:** 2026-09-09  
**Parent:** SITE-002-PAYMENTS-YOOKASSA-STRATEGY-ADOPTION-01  

This is an **operator/business** checklist. It is not a Cursor implementation charter and not a blocker phrased as “does the account exist?”. Items are **create / confirm**.

Do not put shopId, secret keys, or test secrets in this file, chat, or git.

---

## 1. Account and legal

- [ ] Create or confirm YooKassa account for the ЗПМ legal entity that will receive payouts.
- [ ] Confirm legal entity (name, INN, KPP if applicable) matches site commercial documents.
- [ ] Confirm settlement account (расчётный счёт) that YooKassa will pay out to.
- [ ] Confirm who is the contract signer and who is the day-to-day cabinet owner.

## 2. Tariff and money movement

- [ ] Confirm tariffs / commission for intended methods (card, SBP, others).
- [ ] Confirm payout terms (when money arrives on the settlement account).
- [ ] Confirm minimum / maximum payment amounts if YooKassa or the bank imposes them.
- [ ] Confirm who watches payouts vs КП / счёт (accounting owner).

## 3. Payment methods

- [ ] Confirm card as a first-wave method (yes / no / later).
- [ ] Confirm SBP as a first-wave method (yes / no / later).
- [ ] Confirm SberPay if available on this shop / tariff (yes / no / unknown → ask YooKassa).
- [ ] Confirm SberBusiness need: only as a **separate B2B option**, not mixed into default consumer methods.
- [ ] If SberBusiness: confirm limits, who can pay, VAT-per-order constraints, and refund rules **before** offering it.

## 4. Fiscalization (54-ФЗ)

- [ ] Confirm fiscalization scheme: YooKassa fiscalization vs own KKT vs mixed vs not for this method.
- [ ] Confirm KKT / OFD owner and who is responsible if a receipt fails.
- [ ] Confirm VAT rates used on ЗПМ invoices today and how they map to a YooKassa receipt.
- [ ] Confirm delivery receipt treatment (in the same receipt, separate, or not in this payment).
- [ ] Confirm prepayment / second receipt rules (аванс → отгрузка).
- [ ] Confirm what happens if goods/delivery change after a prepayment.
- [ ] Confirm who issues the receipt legal name the buyer must see.

## 5. Refunds and disputes

- [ ] Confirm refund process: who initiates, from which cabinet, how it maps to 1C / accounting.
- [ ] Confirm partial refunds if needed for ЗПМ (complectation change).
- [ ] Confirm B2B method refund limitations (especially SberBusiness if used).
- [ ] Confirm buyer-facing SLA: who answers “I paid / I want a refund”.

## 6. Roles and access

- [ ] Confirm who may create payment links (named roles, not “anyone with admin”).
- [ ] Confirm roles / access in YooKassa cabinet (owner, manager, view-only accounting).
- [ ] Confirm secret storage owner for later keys (ignored Storage path only; not this checklist).
- [ ] Confirm test mode availability and who may use the test shop.
- [ ] Confirm that production keys will never be pasted into chat, git, or reports.

## 7. Pilot

- [ ] Confirm first pilot scenario: counterparty type, amount range, one manager, test mode first then limited live.
- [ ] Confirm what “success” means for the pilot (payment matched to счёт; receipt correct; refund tested if required).
- [ ] Confirm ordinary bank invoice remains available during the pilot.

## 8. Status language (accounting + sales)

- [ ] Confirm that YooKassa `payment.succeeded` is **not** the same as «сделка завершена» / shipped / closed in 1C.
- [ ] Confirm how accounting marks «оплачено по ЮKassa» vs «оплачено по р/с».
- [ ] Confirm OpenCart status 5 «Сделка завершена» will **not** be used as «paid».

## 9. Sber (only if methods require it)

- [ ] Confirm with Sber / YooKassa anything required for SberPay or SberBusiness that ЗПМ does not already have.
- [ ] Do not assume SberBusiness is “just another toggle”.

## 10. Sign-off

- [ ] Accounting sign-off that fiscal and VAT answers are good enough for a **test-mode** pilot.
- [ ] Operator sign-off that MVP is still **links after manager approval**, not cart payment.
- [ ] Date and names of people who answered (fill when used).

---

## How to use this GO

Work this list offline with accounting and YooKassa support. Return answers in a later operator note. Cursor must not implement payments until this list is answered enough that tax treatment is not invented in code.
