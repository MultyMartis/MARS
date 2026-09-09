# Backlog — SITE-002-CUSTOMER-ACCOUNT-UX-ORDER-PAYMENT-READONLY-01

**Future task id:** SITE-002-CUSTOMER-ACCOUNT-UX-ORDER-PAYMENT-READONLY-01  
**Created by:** SITE-002-PAYMENTS-YOOKASSA-MVP-LINKS-WORKFLOW-READONLY-01  
**Date:** 2026-09-09  
**Status:** historical guest-HTTP findings + logged-in audit still needed. **Do not implement in this wave.**

> **Correction 2026-09-09 — [SITE-002-PAYMENTS-YOOKASSA-MVP-LK-AUTO-EMAIL-CORRECTION-01](../decisions/SITE-002-PAYMENTS-YOOKASSA-MVP-LK-AUTO-EMAIL-CORRECTION-01.md)**  
> ЛК **существует** и является **обязательной** поверхностью payment MVP. Эта заметка **не** означает «MVP живёт на email». Правки ЛК: [SITE-002-CUSTOMER-ACCOUNT-UX-ORDER-PAYMENT-FIX-PLAN-01.md](SITE-002-CUSTOMER-ACCOUNT-UX-ORDER-PAYMENT-FIX-PLAN-01.md).

---

## Goal

Провести read-only аудит и затем (отдельным charter) улучшить ЛК покупателя на bzpm.ru так, чтобы он подходил к MVP оплаты ссылкой:

- заявка/заказ виден;
- статус понятен;
- документы доступны, если они есть;
- ссылка на оплату видна только после одобрения и пока не оплачено;
- статус оплаты виден после сверки (не по `return_url`);
- есть контакт менеджера;
- нет сломанного/пустого default OpenCart UX.

Эта задача **не** ставит YooKassa и **не** меняет checkout.

---

## Why this is needed now

Guest HTTP (workflow wave, 2026-09-09):

- `/my-account`, `/order-history`, `/downloads` без сессии → авторизация;
- `/order-history` как гость не показывает заказы;
- `/downloads` — stock OpenCart downloads, не кабинет счетов ЗПМ;
- `/forgot-password` содержит leftover OC-навигацию (wishlist, rewards, recurring и т.д.);
- регистрация уже кастомная (ФИО, город, компания, ИНН, группы клиентов) — это сохранить, не ломать;
- **logged-in** ЛК не инспектировался (логин запрещён workflow-задачей).

Вывод: guest HTTP **не** доказывает, что ЛК можно исключить из MVP. ЛК **уже есть** и **должен** войти в payment MVP. Logged-in страницы **не** инспектировались — нужен аудит с тестовым аккаунтом и FIX-PLAN. UX может требовать правок; **обход ЛК** и «жить на email» **запрещены**.

---

## Audit / improve later (scope of the future task)

| Area | Intent |
|------|--------|
| Login / registration | Ясный русский поток; сохранить B2B-поля; проверить ошибки и мобильный вид |
| Order history | Список заявок/заказов, понятные статусы, не пустая OC-таблица |
| Order detail | Состав, сумма, статус, документы, ссылка оплаты, статус оплаты |
| Documents | Реальные КП/счета/файлы менеджера; не путать с `/downloads` |
| Payment link | Только если одобрено и не оплачено |
| Payment status | После сверки кабинета / позже webhook |
| Manager contact | Куда писать/звонить, если ссылка не работает |
| Mobile | Читаемость, кнопки, письма vs ЛК |
| Russian copy | Без англ. leftover и бессмысленных OC-пунктов |
| Broken default UX | Убрать/починить wishlist, reward points, recurring, пустые downloads, если они не нужны ЗПМ |

---

## What the future task must not do

- Production write без отдельного charter.
- Установка YooKassa.
- Смена статусов заказов.
- Доверие `return_url`.
- Маппинг paid → status 5.
- Секреты в git.

---

## Suggested sequence

1. Read-only logged-in audit (operator test account).
2. Backlog правок UX (один блок за раз, если будет верстка).
3. Только после receipt-minimum confirmation, тарифа YooKassa и пилотного сценария — implementation charter `SITE-002-PAYMENTS-YOOKASSA-MVP-LK-AUTO-EMAIL-IMPLEMENTATION-CHARTER-01`. Charter **обязан** включить payment block в ЛК и auto-email. Полный polish UX может идти следом; MVP **не** «живёт на email вместо ЛК».

---

## Related docs

- [SITE-002-PAYMENTS-YOOKASSA-MVP-LINKS-WORKFLOW-01.md](../plans/SITE-002-PAYMENTS-YOOKASSA-MVP-LINKS-WORKFLOW-01.md)
- [SITE-002-CUSTOMER-ACCOUNT-UX-ORDER-PAYMENT-FIX-PLAN-01.md](SITE-002-CUSTOMER-ACCOUNT-UX-ORDER-PAYMENT-FIX-PLAN-01.md)
- Storage: `current-account-ux/` в пакете SITE-002-PAYMENTS-YOOKASSA-MVP-LINKS-WORKFLOW-READONLY-01
