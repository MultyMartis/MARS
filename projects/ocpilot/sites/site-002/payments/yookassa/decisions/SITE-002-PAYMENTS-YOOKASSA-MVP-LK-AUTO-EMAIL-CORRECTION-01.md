# SITE-002 — коррекция MVP оплаты: ЛК + автоматическое письмо

**Decision id:** SITE-002-PAYMENTS-YOOKASSA-MVP-LK-AUTO-EMAIL-CORRECTION-01  
**Site:** SITE-002 / ЗПМ Production (`https://bzpm.ru/`)  
**Date:** 2026-09-09  
**Mode:** documentation correction. **No implementation.**  
**Model routing:** Cursor Composer / Grok only.  
**Parent strategy:** `payment_links_first_api_manager_workflow_hybrid_later` — **не отменяется.**

---

## 1. Previous ambiguity

Предыдущие формулировки (strategy / workflow / backlog / historical reports) местами склонялись к модели:

- «фаза 1 через email + менеджера»;
- «ЛК не главная поверхность» / «ЛК потом»;
- кабинет клиента — только поздний UX-аудит;
- менеджер может сам собрать и отправить платёжное письмо;
- «MVP может жить на email», если ЛК не идеален.

Это **неверно или неполно**. Исторические отчёты **не переписываются**; эта decision — каноническая коррекция для будущих задач.

---

## 2. Corrected MVP understanding

1. У ЗПМ **уже есть** ЛК клиента.
2. ЛК **обязан** войти в payment MVP.
3. Payment MVP **не** обходит ЛК.
4. Менеджер **не** собирает и **не** шлёт платёжное письмо вручную.
5. Менеджер проверяет заявку и **одобряет оплату внутри сайта / admin**.
6. После одобрения **сайт автоматически** шлёт клиенту письмо со сводкой, документами (если есть) и ссылкой YooKassa.
7. Те же данные оплаты должны быть в ЛК: заявка/заказ, статус, сумма, документы / КП / счёт (если есть), ссылка YooKassa, статус оплаты.
8. Email — **автоматический канал-дубль**, не замена ЛК.
9. ЛК может требовать правок UX, но остаётся **поверхностью MVP**.

**Формула MVP (везде):**

manager approval inside site  
+ payment block in existing customer account / ЛК  
+ automatic email with YooKassa link

---

## 3. ЛК is a mandatory MVP surface

- Не «later only».
- Не опциональный polish после email-процесса.
- Обход ЛК (только письмо / только чат менеджера) **запрещён** как модель MVP.
- Guest-HTTP аудит **не** исключает ЛК. Logged-in правки — backlog, не снятие обязательности.

См. [SITE-002-CUSTOMER-ACCOUNT-UX-ORDER-PAYMENT-FIX-PLAN-01.md](../backlog/SITE-002-CUSTOMER-ACCOUNT-UX-ORDER-PAYMENT-FIX-PLAN-01.md).

---

## 4. Automatic email after manager approval

- Триггер: одобрение оплаты **внутри сайта**.
- Отправитель: **сайт**, не менеджер.
- Содержание: сводка заявки/заказа, сумма, документы если доступны, ссылка YooKassa, как отличить статус заказа / оплаты / отгрузки, контакт менеджера.
- Письмо **дублирует** блок ЛК; источник истины по ссылке/статусу — запись, привязанная к заявке/заказу на сайте.

---

## 5. Manager does not send the payment email

Менеджер:

- проверяет состав, цену, наличие, доставку, плательщика;
- одобряет оплату в admin / site workflow.

Менеджер **не**:

- собирает письмо вручную;
- вставляет ссылку из кабинета в почтовый клиент как основной процесс;
- заменяет ЛК перепиской.

Создание или прикрепление ссылки — действие **сайта** после одобрения (API create **или** attach ссылки из кабинета — деталь implementation charter, не отмена auto-email и ЛК).

---

## 6. Phase 1 may still use manual YooKassa reconciliation

Ручное в MVP:

- сверка факта оплаты в кабинете YooKassa;
- при необходимости: создание ссылки в кабинете и **прикрепление** к заявке, если API-create ещё не в этом этапе.

**Не** ручное: платёжное письмо клиенту; скрытие оплаты от ЛК.

Позже: webhook/API обновляет статус оплаты автоматически. `return_url` по-прежнему **не** истина оплаты.

---

## 7. Implementation still not authorized

Эта decision **не**:

- не ставит YooKassa;
- не создаёт ссылки;
- не меняет шаблоны/контроллеры/модели;
- не пишет в production / DB / FTP;
- не трогает секреты;
- не делает git mutation.

Следующий implementation charter **не** стартует, пока не подтверждены: чеки/фискализация, аккаунт/тариф YooKassa, пилотный сценарий.

---

## 8. Payment-links strategy remains valid

Не отменяется:

- `payment_links_first_api_manager_workflow_hybrid_later`
- нет универсального checkout payment first
- нет официального модуля OpenCart как первого production-шага
- нет оплаты до одобрения менеджера
- обычный счёт / безнал остаётся
- нет `return_url` как истины оплаты
- нет маппинга paid → OpenCart status 5 «Сделка завершена»
- чеки/фискализация до live
- чеки YooKassa предпочтительны, если юридически/учётно подходят
- НДС планировочно **22%**
- доставка изначально вне онлайн-платежа/чека, если возможно
- предоплата / второй чек — не первый MVP

---

## 9. Checkout-first remains rejected

Универсальная оплата в корзине **не** становится фазой 1 из-за этой коррекции. Hybrid checkout — поздний этап roadmap (простой SKU whitelist), не MVP.

---

## 10. Canonical docs after this correction

| Role | Path |
|------|------|
| This decision | `decisions/SITE-002-PAYMENTS-YOOKASSA-MVP-LK-AUTO-EMAIL-CORRECTION-01.md` |
| MVP workflow summary | `plans/SITE-002-PAYMENTS-YOOKASSA-MVP-APPROVED-WORKFLOW-01.md` |
| ЛК fix plan | `backlog/SITE-002-CUSTOMER-ACCOUNT-UX-ORDER-PAYMENT-FIX-PLAN-01.md` |
| Strategy (corrected, still adopted) | `decisions/SITE-002-PAYMENTS-YOOKASSA-STRATEGY-ADOPTION-01.md` |

Historical reports (`*-DISCOVERY-*`, `*-STRATEGY-ADOPTION-01` report, `*-MVP-LINKS-WORKFLOW-READONLY-01`) remain historical. Do not treat them as current MVP wording.
