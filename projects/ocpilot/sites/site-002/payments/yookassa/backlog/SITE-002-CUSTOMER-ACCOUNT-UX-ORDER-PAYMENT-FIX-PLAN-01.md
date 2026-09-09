# Backlog — SITE-002-CUSTOMER-ACCOUNT-UX-ORDER-PAYMENT-FIX-PLAN-01

**Plan id:** SITE-002-CUSTOMER-ACCOUNT-UX-ORDER-PAYMENT-FIX-PLAN-01  
**Date:** 2026-09-09  
**Status:** backlog / requirements. **Not implementation.**  
**Parent correction:** [SITE-002-PAYMENTS-YOOKASSA-MVP-LK-AUTO-EMAIL-CORRECTION-01.md](../decisions/SITE-002-PAYMENTS-YOOKASSA-MVP-LK-AUTO-EMAIL-CORRECTION-01.md)  
**Historical guest-HTTP note:** [SITE-002-CUSTOMER-ACCOUNT-UX-ORDER-PAYMENT-READONLY-01.md](SITE-002-CUSTOMER-ACCOUNT-UX-ORDER-PAYMENT-READONLY-01.md)

ЛК клиента **уже существует** и **обязан** поддерживать payment MVP. Это не «кабинет потом». Email — дубль, не замена.

---

## Mandatory MVP support in ЛК

ЛК должен давать клиенту:

1. **Список заявок/заказов** — не пустая/бессмысленная таблица OpenCart как единственный ответ.
2. **Деталь заявки/заказа** — состав, сумма, понятный статус заявки.
3. **Состояние «одобрено к оплате»** — когда менеджер одобрил оплату внутри сайта.
4. **Ссылку YooKassa** — после одобрения, пока оплата не завершена / пока ссылка действительна.
5. **Статус оплаты** — отдельно от статуса заявки и отгрузки.
6. **Документы / КП / счёт** — ссылки, если файлы есть; не путать с stock `/downloads`.
7. **Контакт менеджера**.
8. **Ясный русский текст** — без англ. leftover и бессмысленных пунктов OC.
9. **Мобильную читаемость** — сумма, ссылка, статусы доступны без «сломался default theme».
10. **Не сломанный/default OpenCart UX** как поверхность оплаты (wishlist, reward points, recurring, пустые downloads не маскируют кабинет ЗПМ).
11. **Различие трёх линий:**
    - статус заявки/заказа;
    - статус оплаты;
    - статус исполнения / отгрузки.

Не мапить paid → OpenCart status 5 «Сделка завершена». Не считать `return_url` оплатой.

---

## Why fixes may be needed (not a reason to drop ЛК)

Guest HTTP (2026-09-09) показал авторизацию на `/my-account`, `/order-history`, leftover OC на forgot-password, `/downloads` как stock OC. **Logged-in** страницы не инспектировались.

Вывод: нужны аудит с тестовым аккаунтом и правки UX. Вывод **не**: «MVP без ЛК» или «жить на email».

Регистрация с B2B-полями (ФИО, город, компания, ИНН, группы) — сохранить, не ломать.

---

## Suggested later sequence (still not this wave)

1. Read-only logged-in audit (operator test account).
2. Минимальный payment block на существующих страницах списка/детали (один implementation charter вместе с auto-email, не отдельно «только письмо»).
3. UX polish блоками (не batch всей темы).
4. Позже webhook подставляет статус оплаты в тот же блок.

Implementation charter: `SITE-002-PAYMENTS-YOOKASSA-MVP-LK-AUTO-EMAIL-IMPLEMENTATION-CHARTER-01` — только после подтверждения чеков, тарифа YooKassa и пилота.

---

## Out of this plan

- Код, шаблоны, production, секреты, платежи, git.
- Замена ЛК почтой менеджера.
- Checkout-first.
- SEO / header / footer / M9 / PDP.
