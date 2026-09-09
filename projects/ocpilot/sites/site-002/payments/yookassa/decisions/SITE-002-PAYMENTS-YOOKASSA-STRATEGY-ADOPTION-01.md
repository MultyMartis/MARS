# SITE-002 — YooKassa strategy adoption

**Operation:** SITE-002-PAYMENTS-YOOKASSA-STRATEGY-ADOPTION-01  
**Site:** SITE-002 / ЗПМ Production (`https://bzpm.ru/`)  
**Date:** 2026-09-09  
**Mode:** documentation / operator decision. **No implementation.**  
**Model routing:** Cursor Composer / Grok only.

> **Correction 2026-09-09 — [SITE-002-PAYMENTS-YOOKASSA-MVP-LK-AUTO-EMAIL-CORRECTION-01](SITE-002-PAYMENTS-YOOKASSA-MVP-LK-AUTO-EMAIL-CORRECTION-01.md)**  
> MVP formula: **manager approval inside site + payment block in existing customer ЛК + automatic email with YooKassa link**.  
> ЛК is a **mandatory MVP surface**. Email is automatic after approval; the manager does **not** assemble/send the payment email. Manual remainder: payment **reconciliation** unless later automated. Implementation is **not** authorized. Strategy id unchanged: `payment_links_first_api_manager_workflow_hybrid_later`.

---

## 1. Decision

Adopt `payment links first → API-assisted manager workflow → hybrid checkout later` for SITE-002 / ЗПМ YooKassa work.

Identifier: `payment_links_first_api_manager_workflow_hybrid_later`.

Universal cart payment is **not** the first phase (`universal_cart_payment_first_phase: false`).

This is an operator-approved strategy. It does not install YooKassa, does not enable a payment method, and does not change production.

---

## 2. Context

### Sources

1. Existing MARS report: SITE-002-PAYMENTS-YOOKASSA-DISCOVERY-READONLY-01 (repo + Storage pack).
2. External research pasted by the operator: «Online Payment Strategy Research для производственно-торговой B2B-компании». A dedicated file was **not found** in the workspace; conclusions below are the operator-approved paste, not fabricated citations.

### Technical snapshot (from discovery; not re-probed)

- OpenCart / ocStore 3.0.3.9, theme default, web PHP 7.4.33 (EOL).
- HTTPS live, `config_secure=1`, cURL present.
- Enabled payments now: `cod`, `free_checkout`. No YooKassa / `yandex_money` files installed.
- Standard checkout exists, but the commercial process is not checkout-first.
- Custom anketa is the dominant B2B lead path (`oc_anketa` 94 vs `oc_order` 18, mostly `free_checkout` / status 1).
- No dedicated paid / waiting-for-capture status. Do not map paid to status 5 «Сделка завершена».
- Official OC3 module is version-compatible technically, not a business drop-in.
- Callback route is SAFE UNKNOWN until a module/API exists.

### Current commercial process (ЗПМ)

заявка → проверка менеджером → уточнение комплектации / наличия / доставки → КП → счёт → безналичная оплата.

Payment should happen when the commercial order is reliable.

---

## 3. Adopted strategy

Three stages, in this order:

1. **Payment links first (MVP / phase 1)**  
   Keep the current B2B process. Manager **approves payment inside the site/admin workflow**. The site creates or attaches an **individual YooKassa payment link**, stores it against the order/request, exposes a **payment block in the existing customer account (ЛК)**, and **automatically emails** the client (summary, documents if available, YooKassa link). Ordinary bank invoice / bank transfer remains. Email is a duplicate channel, not a replacement for ЛК. Manual remainder in MVP: **payment reconciliation** (YooKassa cabinet), not email assembly.

2. **API-assisted manager workflow (later)**  
   Webhook/API **payment-status** updates, audit log, and (if MVP started with cabinet-attach) API-created links / manager button «Сформировать ссылку на оплату». **Not** “ЛК later” and **not** “site-side approval later”: those are MVP. Full API/webhook status automation is later.

3. **Hybrid checkout later (optional, constrained)**  
   Only for a **simple-SKU whitelist**: price is current; stock is confirmed; delivery is calculable; VAT is unambiguous; no manager approval required; amount is within payment limits. All complex / high-value / B2B / custom orders stay on the manager-approved branch.

---

## 4. Rejected first-phase strategy

Explicitly **rejected as the first production step**:

- Enabling online payment for the **whole** OpenCart cart / checkout.
- Installing the official OpenCart YooKassa checkout module as the first production action.
- Replacing ordinary bank invoice / bank transfer with YooKassa.
- Collecting money before manager approval, current price, stock, delivery and VAT are fixed.
- Automatic OpenCart order-status change on `return_url`.
- Mapping `payment.succeeded` to status 5 «Сделка завершена».

Discovery listed the official module as **technical option A**. This decision **overrides sequencing**: option A is not first.

---

## 5. Why cart payment is not first

ЗПМ is a production-trade B2B company. Catalogue SKU on the site is not always a ready-to-pay retail cart line:

- Complectation, availability, delivery and price often need a manager.
- Anketa (94) dominates OpenCart Order (18). Checkout is not the commercial source of truth.
- Universal cart payment would take money when the commercial order is still unreliable (stale price, unconfirmed stock, uncalculable delivery, ambiguous VAT).
- The official OC3 module is built around OpenCart Order / checkout. That is the wrong primary object for the current process.
- 54-ФЗ, VAT, KKT/OFD, delivery in the receipt, prepayment / second receipt and refunds are unresolved. Cart payment would freeze those errors into live money movement.

---

## 6. MVP model

**Formula:** manager approval inside site + payment block in existing customer ЛК + automatic email with YooKassa link.

**Path:** заявка / заказ в системе сайта → менеджер проверяет состав, цену, наличие, доставку, плательщика → менеджер **одобряет оплату внутри сайта/admin** → сайт создаёт или прикрепляет ссылку YooKassa и сохраняет её к заявке/заказу → сайт **автоматически** шлёт клиенту письмо (сводка, документы, ссылка) → клиент видит **тот же** payment block в ЛК → клиент платит по ссылке **или** безналом → MVP-сверка оплаты **вручную** в кабинете YooKassa → позже webhook/API обновляет статус оплаты.

YooKassa in phase 1 is an **additional** payment option after manager approval, not a replacement of the commercial process.

- Documents remain primary: КП and ordinary bank invoice / счёт.
- Bank transfer remains.
- Methods to consider first: card, SBP, SberPay if available. SberBusiness only as a separate B2B option.
- Amount, payer, VAT, delivery, receipt need and order/reference number are fixed **before** the link is created.
- **ЛК is a mandatory MVP surface.** It may need UX fixes; it must not be bypassed.
- Buyer sees: YooKassa payment UI **and** the same link/status/documents in ЛК. Email is automatic notification, not the primary product.
- Manager does **not** manually assemble or send the payment email.
- Result is seen by the manager (and accounting as agreed) plus stored against the order/request.
- Reconciliation is **manual** first (cabinet). That is the manual part — not email sending.
- No automatic OpenCart **business** order status change in MVP unless later approved. Do not map paid → status 5.
- No checkout activation in MVP.

Details: `plans/SITE-002-PAYMENTS-YOOKASSA-MVP-PAYMENT-LINKS-PLAN-01.md` and `plans/SITE-002-PAYMENTS-YOOKASSA-MVP-APPROVED-WORKFLOW-01.md`.

---

## 7. Later API model

After a manual **reconciliation** pilot and after fiscal / tariff decisions:

- If MVP used cabinet-created links attached in the site: add API creation / manager control «Сформировать ссылку на оплату».
- YooKassa API creates the payment / invoice for an already-approved commercial order.
- Webhooks update **payment status** only; business order status and receipt status stay separate.
- Audit log: who approved, who created/attached the link, amount, reference, timestamps, payment id.
- Link the payment to anketa / request / commercial order id — not necessarily to a checkout `oc_order`.
- Do not trust `return_url`. Confirm via webhook / API.
- Idempotency, refunds, partial payments, receipts and 1C/CRM sync belong here or later — not in MVP.
- **Do not** postpone ЛК payment block or automatic approval email to this stage. Those are MVP.

---

## 8. Later hybrid checkout model

Only if a **whitelist** of simple SKU is proven:

- Price is current.
- Stock is confirmed.
- Delivery is calculable.
- VAT is unambiguous.
- No manager approval required.
- Amount is within payment limits.

Then evaluate whether the official OpenCart module (or a constrained checkout) can serve **that whitelist only**. Default path for everything else remains manager-approved КП / счёт / payment link.

Do not turn the whole catalogue into a pay-now cart because a few SKU might qualify later.

---

## 9. What remains unchanged

- заявка → менеджер → КП / счёт → безналичная оплата as the default B2B process.
- Ordinary bank invoice / bank transfer.
- Anketa as the dominant lead path until a later charter says otherwise.
- SEO robots attr Disallow, category meta, blog canonical/sitemap, M9 filters, PDP hero specs, `product.php`, `/zapchasti`, protected Yandex tags in `header.twig` / `footer.twig`.
- Category canonical/sitemap architecture remains deferred.
- No production, DB, FTP, Git, secrets, or dirty-main mutation in this operation.

---

## 10. Preconditions before implementation

Must be decided **before any payment code**, module install, or live link used as a product process:

- YooKassa account / contract / tariff / commission / payout terms.
- Legal entity and settlement account.
- Payment methods (card, SBP, SberPay, SberBusiness as separate).
- Fiscalization scheme (54-ФЗ, KKT/OFD, who issues the receipt).
- VAT / NDS rates on goods, delivery, mixed orders.
- Delivery in the receipt.
- Prepayment and second-receipt rules.
- Refund process, including B2B method limits.
- Roles: who may create links; secret storage owner.
- Test mode availability and staging before production automation.
- PHP 7.4 EOL: separate hardening / staging / upgrade plan in parallel — not a substitute for the business sequence.
- Status model: `payment.succeeded` ≠ business order status ≠ receipt status. Do not use status 5 as «paid».

Checklist: `checklists/SITE-002-PAYMENTS-YOOKASSA-BUSINESS-INPUTS-CHECKLIST-01.md`.

---

## 11. Out of scope

This operation and the first phase do **not** include:

- Production write, DB write, FTP PUT, deploy, cache, import.
- Module install, OpenCart payment settings, checkout activation.
- Test order, real payment, YooKassa key creation.
- Secrets edit / print.
- Git mutation / dirty main mutation.
- SEO / robots / sitemap / canonical / header / footer / M9 / PDP / `product.php`.
- 1C/CRM sync, webhook automation, official module evaluation as a go-live.
- Category canonical/sitemap architecture.

---

## 12. Risks

See `risks/SITE-002-PAYMENTS-YOOKASSA-RISK-REGISTER-01.md`. Headline risks: wrong business model (cart-first); paid before manager approval; stale price/stock/delivery; VAT/receipt errors; missed second receipt; missing refunds; B2B refund limits; trusting `return_url`; webhook duplication/delay; status mismatch; secret leakage; accidental real payment; PHP 7.4; **Git cannot roll back money**.

---

## 13. Next GO

**Immediate next GO (operator / business, not Cursor code):**

Confirm receipt/fiscalization, YooKassa account/tariff, and one pilot scenario.

**Then (implementation still not authorized by this adoption doc):**

`SITE-002-PAYMENTS-YOOKASSA-MVP-LK-AUTO-EMAIL-IMPLEMENTATION-CHARTER-01`

Only after receipt/fiscalization confirmation, YooKassa account/tariff confirmed, and a pilot scenario selected.

Correction of the MVP surfaces: [SITE-002-PAYMENTS-YOOKASSA-MVP-LK-AUTO-EMAIL-CORRECTION-01](SITE-002-PAYMENTS-YOOKASSA-MVP-LK-AUTO-EMAIL-CORRECTION-01.md).
