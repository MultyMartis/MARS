# ORCA User Goal Taxonomy v1

**Taxonomy ID:** `orca-user-goal-taxonomy`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`  
**Machine reference:** [`orca-user-goal-taxonomy-v1.json`](orca-user-goal-taxonomy-v1.json)

---

## Purpose

`likely_user_goal` captures the user's **desired outcome** in goal vocabulary. Goals are finer-grained and more outcome-oriented than `primary_intent`; one intent may map to several goals and vice versa.

---

## Employment distinction (mandatory)

Three employment-related goals **must not** be collapsed into one label:

| Role | goal_id | Description |
|------|---------|-------------|
| Job seeker | `SEEK_EMPLOYMENT` | Соискатель ищет работу |
| Employer | `HIRE_EMPLOYEE` | Работодатель ищет сотрудника в штат |
| Service buyer | `HIRE_PROVIDER` | Заказчик ищет подрядчика / исполнителя услуги |

**Signals:** `CAREER_SEEKER` ↔ SEEK_EMPLOYMENT; `EMPLOYEE_HIRING` ↔ HIRE_EMPLOYEE; `PROVIDER_HIRE` ↔ HIRE_PROVIDER.

Confusion between these triggers `CAREER_VS_PROVIDER` ambiguity and mandatory ABSTAIN when unresolved.

---

## Goal catalog

### HIRE_PROVIDER

| Поле | Значение |
|------|----------|
| **goal_id** | `HIRE_PROVIDER` |
| **typical primary_intent mapping** | HIRE_SERVICE |

**definition:** Нанять внешнего исполнителя / подрядчика для оказания услуги.

**positive examples:**
- «заказать монтаж вентиляции»
- «найти подрядчика 1с»

**counterexamples:**
- «вакансия монтажник»
- «как смонтировать самому»
### REQUEST_QUOTE

| Поле | Значение |
|------|----------|
| **goal_id** | `REQUEST_QUOTE` |
| **typical primary_intent mapping** | INFORMATIONAL / HIRE_SERVICE |

**definition:** Получить коммерческое предложение или расчёт стоимости без явного заказа.

**positive examples:**
- «расчёт стоимости внедрения crm»
- «сколько стоит монтаж под ключ»

**counterexamples:**
- «заказать внедрение crm»
- «что такое crm»
### CONTACT_SUPPORT

| Поле | Значение |
|------|----------|
| **goal_id** | `CONTACT_SUPPORT` |
| **typical primary_intent mapping** | REQUEST_SUPPORT |

**definition:** Связаться с поддержкой или сервисом.

**positive examples:**
- «телефон техподдержки 1с»
- «связаться с сервисным центром»

**counterexamples:**
- «как исправить ошибку самому»
### OBTAIN_IMPLEMENTATION

| Поле | Значение |
|------|----------|
| **goal_id** | `OBTAIN_IMPLEMENTATION` |
| **typical primary_intent mapping** | REQUEST_IMPLEMENTATION |

**definition:** Получить услугу внедрения / развёртывания.

**positive examples:**
- «внедрение erp под ключ»
- «развернуть crm на сервере»

**counterexamples:**
- «что такое внедрение erp»
### CONFIGURE_SYSTEM

| Поле | Значение |
|------|----------|
| **goal_id** | `CONFIGURE_SYSTEM` |
| **typical primary_intent mapping** | REQUEST_CONFIGURATION |

**definition:** Настроить систему под свои нужды (часто с исполнителем).

**positive examples:**
- «настроить модуль складского учёта»
- «конфигурация отчётов»

**counterexamples:**
- «как настроить самому»
### MODIFY_SYSTEM

| Поле | Значение |
|------|----------|
| **goal_id** | `MODIFY_SYSTEM` |
| **typical primary_intent mapping** | REQUEST_MODIFICATION |

**definition:** Доработать или изменить существующее решение.

**positive examples:**
- «доработка отчёта 1с»
- «изменить логику crm»

**counterexamples:**
- «инструкция изменения отчёта»
### INTEGRATE_SYSTEMS

| Поле | Значение |
|------|----------|
| **goal_id** | `INTEGRATE_SYSTEMS` |
| **typical primary_intent mapping** | REQUEST_INTEGRATION |

**definition:** Соединить две или более системы.

**positive examples:**
- «интеграция 1с с сайтом»
- «api обмен с wms»

**counterexamples:**
- «что такое api»
### RECOVER_OPERATION

| Поле | Значение |
|------|----------|
| **goal_id** | `RECOVER_OPERATION` |
| **typical primary_intent mapping** | REQUEST_RECOVERY |

**definition:** Восстановить работу или данные после сбоя.

**positive examples:**
- «восстановление базы 1с»
- «вернуть доступ к crm»

**counterexamples:**
- «как восстановить базу инструкция»
### DIAGNOSE_ISSUE

| Поле | Значение |
|------|----------|
| **goal_id** | `DIAGNOSE_ISSUE` |
| **typical primary_intent mapping** | REQUEST_AUDIT_OR_DIAGNOSTIC |

**definition:** Провести диагностику или аудит.

**positive examples:**
- «диагностика производительности 1с»
- «аудит it»

**counterexamples:**
- «ошибка 1с что делать»
### MIGRATE_DATA

| Поле | Значение |
|------|----------|
| **goal_id** | `MIGRATE_DATA` |
| **typical primary_intent mapping** | REQUEST_MIGRATION |

**definition:** Перенести данные или систему.

**positive examples:**
- «миграция crm в битрикс24»
- «переход на 1с 8.3»

**counterexamples:**
- «интеграция двух crm»
### MAINTAIN_SYSTEM

| Поле | Значение |
|------|----------|
| **goal_id** | `MAINTAIN_SYSTEM` |
| **typical primary_intent mapping** | REQUEST_MAINTENANCE |

**definition:** Плановое обслуживание или сопровождение.

**positive examples:**
- «абонентское обслуживание серверов»
- «то холодильного оборудования»

**counterexamples:**
- «срочное восстановление»
### BUY_MODULE_OR_PRODUCT

| Поле | Значение |
|------|----------|
| **goal_id** | `BUY_MODULE_OR_PRODUCT` |
| **typical primary_intent mapping** | BUY_PRODUCT_OR_MODULE |

**definition:** Приобрести продукт, лицензию, модуль.

**positive examples:**
- «купить лицензию 1с»
- «цена модуля erp»

**counterexamples:**
- «заказать внедрение»
### COMPARE_OPTIONS

| Поле | Значение |
|------|----------|
| **goal_id** | `COMPARE_OPTIONS` |
| **typical primary_intent mapping** | INFORMATIONAL |

**definition:** Сравнить варианты без покупки.

**positive examples:**
- «сравнение crm систем»
- «битрикс24 vs amocrm»

**counterexamples:**
- «купить битрикс24»
### LEARN

| Поле | Значение |
|------|----------|
| **goal_id** | `LEARN` |
| **typical primary_intent mapping** | EDUCATIONAL |

**definition:** Обучиться навыку или теме.

**positive examples:**
- «курс 1с программирование»
- «обучение crm»

**counterexamples:**
- «как настроить отчёт»
### PERFORM_TASK_INDEPENDENTLY

| Поле | Значение |
|------|----------|
| **goal_id** | `PERFORM_TASK_INDEPENDENTLY` |
| **typical primary_intent mapping** | DIY_HOW_TO |

**definition:** Выполнить задачу самостоятельно по инструкции.

**positive examples:**
- «как самому настроить 1с»
- «монтаж своими руками»

**counterexamples:**
- «заказать монтаж»
### READ_DOCUMENTATION

| Поле | Значение |
|------|----------|
| **goal_id** | `READ_DOCUMENTATION` |
| **typical primary_intent mapping** | DOCUMENTATION_LOOKUP |

**definition:** Найти справочную документацию.

**positive examples:**
- «документация api 1с»
- «руководство пользователя»

**counterexamples:**
- «скачать руководство pdf»
### DOWNLOAD

| Поле | Значение |
|------|----------|
| **goal_id** | `DOWNLOAD` |
| **typical primary_intent mapping** | DOWNLOAD_RESOURCE |

**definition:** Скачать ресурс.

**positive examples:**
- «скачать демо 1с»
- «загрузить драйвер»

**counterexamples:**
- «купить 1с»
### COMPLY_WITH_REGULATION

| Поле | Значение |
|------|----------|
| **goal_id** | `COMPLY_WITH_REGULATION` |
| **typical primary_intent mapping** | REGULATORY |

**definition:** Узнать или соблюсти нормативные требования.

**positive examples:**
- «требования санпин к холодильнику»
- «гост вентиляция»

**counterexamples:**
- «заказать монтаж по гост»
### SEEK_EMPLOYMENT

| Поле | Значение |
|------|----------|
| **goal_id** | `SEEK_EMPLOYMENT` |
| **typical primary_intent mapping** | CAREER_EMPLOYMENT |

**definition:** Найти работу как соискатель.

**positive examples:**
- «вакансия 1с программист»
- «работа инженер вентиляция»
- «резюме администратор»

**counterexamples:**
- «найти подрядчика»
- «курс 1с»
### HIRE_EMPLOYEE

| Поле | Значение |
|------|----------|
| **goal_id** | `HIRE_EMPLOYEE` |
| **typical primary_intent mapping** | CAREER_EMPLOYMENT |

**definition:** Нанять сотрудника в штат (работодатель).

**positive examples:**
- «требуется 1с программист в штат»
- «найти сотрудника на склад»

**counterexamples:**
- «найти подрядчика на монтаж»
- «вакансия для меня»
### NAVIGATE_TO_KNOWN_SITE

| Поле | Значение |
|------|----------|
| **goal_id** | `NAVIGATE_TO_KNOWN_SITE` |
| **typical primary_intent mapping** | NAVIGATIONAL |

**definition:** Перейти на известный сайт или бренд.

**positive examples:**
- «сайт 1с официальный»
- «битрикс24 вход на сайт»

**counterexamples:**
- «войти в битрикс24»
### ACCESS_ACCOUNT

| Поле | Значение |
|------|----------|
| **goal_id** | `ACCESS_ACCOUNT` |
| **typical primary_intent mapping** | LOGIN_ACCOUNT_ACCESS |

**definition:** Войти в аккаунт или восстановить доступ.

**positive examples:**
- «войти в личный кабинет»
- «восстановить пароль»

**counterexamples:**
- «сайт личный кабинет»
### UNKNOWN

| Поле | Значение |
|------|----------|
| **goal_id** | `UNKNOWN` |
| **typical primary_intent mapping** | UNKNOWN / AMBIGUOUS |

**definition:** Цель не определена.

**positive examples:**
- «1с»
- «crm»

**counterexamples:**
- «заказать внедрение 1с»


---

## Mapping guidance

| goal_id | Primary intent (typical) |
|---------|--------------------------|
| HIRE_PROVIDER | HIRE_SERVICE |
| REQUEST_QUOTE | INFORMATIONAL or HIRE_SERVICE |
| CONTACT_SUPPORT | REQUEST_SUPPORT |
| OBTAIN_IMPLEMENTATION | REQUEST_IMPLEMENTATION |
| CONFIGURE_SYSTEM | REQUEST_CONFIGURATION |
| MODIFY_SYSTEM | REQUEST_MODIFICATION |
| INTEGRATE_SYSTEMS | REQUEST_INTEGRATION |
| RECOVER_OPERATION | REQUEST_RECOVERY |
| DIAGNOSE_ISSUE | REQUEST_AUDIT_OR_DIAGNOSTIC |
| MIGRATE_DATA | REQUEST_MIGRATION |
| MAINTAIN_SYSTEM | REQUEST_MAINTENANCE |
| BUY_MODULE_OR_PRODUCT | BUY_PRODUCT_OR_MODULE |
| COMPARE_OPTIONS | INFORMATIONAL |
| LEARN | EDUCATIONAL |
| PERFORM_TASK_INDEPENDENTLY | DIY_HOW_TO |
| READ_DOCUMENTATION | DOCUMENTATION_LOOKUP |
| DOWNLOAD | DOWNLOAD_RESOURCE |
| COMPLY_WITH_REGULATION | REGULATORY |
| SEEK_EMPLOYMENT | CAREER_EMPLOYMENT |
| HIRE_EMPLOYEE | CAREER_EMPLOYMENT |
| NAVIGATE_TO_KNOWN_SITE | NAVIGATIONAL |
| ACCESS_ACCOUNT | LOGIN_ACCOUNT_ACCESS |
| UNKNOWN | UNKNOWN or AMBIGUOUS |

---

## Related documents

- [`ORCA-PRIMARY-INTENT-TAXONOMY-v1.md`](ORCA-PRIMARY-INTENT-TAXONOMY-v1.md)
- [`ORCA-SEMANTIC-SIGNAL-TAXONOMY-v1.md`](ORCA-SEMANTIC-SIGNAL-TAXONOMY-v1.md)
