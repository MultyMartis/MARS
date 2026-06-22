# ORCA Semantic Signal Taxonomy v1

**Taxonomy ID:** `orca-semantic-signal-taxonomy`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`  
**Machine reference:** [`orca-semantic-signal-taxonomy-v1.json`](orca-semantic-signal-taxonomy-v1.json)

---

## Purpose

Typed **signals** with **strength** and **evidence** support multi-axis interpretation. Signals are evidence axes — not final labels.

---

## Strength scale

| Value | Meaning |
|-------|---------|
| `NONE` | Сигнал не обнаружен; не записывать evidence или strength=NONE. |
| `WEAK` | Косвенная лексема или доменное соседство без явного глагола. |
| `MEDIUM` | Устойчивая лексема в контексте фразы. |
| `STRONG` | Несколько согласованных маркеров или устойчивое словосочетание. |
| `EXPLICIT` | Прямой однозначный маркер (глагол найма, «вакансия», «скачать»). |

---

## Core rule

> **Do not infer an entire intent solely from one signal.**

A single STRONG `IMPLEMENTATION` does not alone justify `REQUEST_IMPLEMENTATION` if `DIY` is EXPLICIT. Aggregation requires multiple signals, ambiguity check, and eligibility policy.

---

## Signal record fields

Each element of `signals[]` in the semantic record:

| Field | Required | Description |
|-------|----------|-------------|
| `signal_id` | yes | Taxonomy ID from this document |
| `strength` | yes | NONE / WEAK / MEDIUM / STRONG / EXPLICIT |
| `evidence_span` | recommended | Substring from `raw_query` or `normalized_query` supporting the signal |
| `normalized_evidence_token` | recommended | Lemmatized or normalized token/phrase |
| `source_type` | recommended | `rule`, `model`, `llm`, `human`, `operator` |
| `source_id` | recommended | Identifier of rule pack, model, or reviewer |
| `confidence` | optional | Assessor confidence 0.0–1.0 |
| `conflict_flag` | optional | `true` if this signal opposes another active signal |

---

## Signal catalog (31 signals)

### PROVIDER_HIRE

**definition:** Признаки найма исполнителя: заказать, нанять, подрядчик, мастер, под ключ.

| strength | example (RU) |
|----------|----------------|
| EXPLICIT | «заказать» в прямом коммерческом/задачном контексте |
| STRONG | устойчивое сочетание с объектом услуги |
| MEDIUM | доменный термин без глагола действия |
| WEAK | тематическое соседство |
| NONE | отсутствует |

**typical intent/goal influence:** HIRE_SERVICE
### TRANSACTION

**definition:** Коммерческая транзакция: купить, цена, стоимость, оплата.

| strength | example (RU) |
|----------|----------------|
| EXPLICIT | «купить» в прямом коммерческом/задачном контексте |
| STRONG | устойчивое сочетание с объектом услуги |
| MEDIUM | доменный термин без глагола действия |
| WEAK | тематическое соседство |
| NONE | отсутствует |

**typical intent/goal influence:** BUY_PRODUCT_OR_MODULE
### QUOTE_PRICE

**definition:** Запрос цены или КП без явного заказа.

| strength | example (RU) |
|----------|----------------|
| EXPLICIT | «сколько стоит» в прямом коммерческом/задачном контексте |
| STRONG | устойчивое сочетание с объектом услуги |
| MEDIUM | доменный термин без глагола действия |
| WEAK | тематическое соседство |
| NONE | отсутствует |

**typical intent/goal influence:** REQUEST_QUOTE goal
### CONTACT

**definition:** Контакт с компанией: телефон, связаться, email.

| strength | example (RU) |
|----------|----------------|
| EXPLICIT | «связаться» в прямом коммерческом/задачном контексте |
| STRONG | устойчивое сочетание с объектом услуги |
| MEDIUM | доменный термин без глагола действия |
| WEAK | тематическое соседство |
| NONE | отсутствует |

**typical intent/goal influence:** CONTACT_SUPPORT
### GEOGRAPHY

**definition:** Географическая привязка: город, регион, рядом.

| strength | example (RU) |
|----------|----------------|
| EXPLICIT | «москва» в прямом коммерческом/задачном контексте |
| STRONG | устойчивое сочетание с объектом услуги |
| MEDIUM | доменный термин без глагола действия |
| WEAK | тематическое соседство |
| NONE | отсутствует |

**typical intent/goal influence:** modifies commercial intents
### URGENCY

**definition:** Срочность: срочно, сегодня, экстренно.

| strength | example (RU) |
|----------|----------------|
| EXPLICIT | «срочно» в прямом коммерческом/задачном контексте |
| STRONG | устойчивое сочетание с объектом услуги |
| MEDIUM | доменный термин без глагола действия |
| WEAK | тематическое соседство |
| NONE | отсутствует |

**typical intent/goal influence:** REQUEST_RECOVERY
### IMPLEMENTATION

**definition:** Внедрение, развёртывание, запуск.

| strength | example (RU) |
|----------|----------------|
| EXPLICIT | «внедрение» в прямом коммерческом/задачном контексте |
| STRONG | устойчивое сочетание с объектом услуги |
| MEDIUM | доменный термин без глагола действия |
| WEAK | тематическое соседство |
| NONE | отсутствует |

**typical intent/goal influence:** REQUEST_IMPLEMENTATION
### CONFIGURATION

**definition:** Настройка, конфигурация, параметры.

| strength | example (RU) |
|----------|----------------|
| EXPLICIT | «настроить» в прямом коммерческом/задачном контексте |
| STRONG | устойчивое сочетание с объектом услуги |
| MEDIUM | доменный термин без глагола действия |
| WEAK | тематическое соседство |
| NONE | отсутствует |

**typical intent/goal influence:** REQUEST_CONFIGURATION
### MODIFICATION

**definition:** Доработка, изменение, кастомизация.

| strength | example (RU) |
|----------|----------------|
| EXPLICIT | «доработать» в прямом коммерческом/задачном контексте |
| STRONG | устойчивое сочетание с объектом услуги |
| MEDIUM | доменный термин без глагола действия |
| WEAK | тематическое соседство |
| NONE | отсутствует |

**typical intent/goal influence:** REQUEST_MODIFICATION
### INTEGRATION

**definition:** Интеграция, API, обмен, синхронизация.

| strength | example (RU) |
|----------|----------------|
| EXPLICIT | «интеграция» в прямом коммерческом/задачном контексте |
| STRONG | устойчивое сочетание с объектом услуги |
| MEDIUM | доменный термин без глагола действия |
| WEAK | тематическое соседство |
| NONE | отсутствует |

**typical intent/goal influence:** REQUEST_INTEGRATION
### SUPPORT

**definition:** Техподдержка, сопровождение, консультация.

| strength | example (RU) |
|----------|----------------|
| EXPLICIT | «техподдержка» в прямом коммерческом/задачном контексте |
| STRONG | устойчивое сочетание с объектом услуги |
| MEDIUM | доменный термин без глагола действия |
| WEAK | тематическое соседство |
| NONE | отсутствует |

**typical intent/goal influence:** REQUEST_SUPPORT
### RECOVERY

**definition:** Восстановление после сбоя.

| strength | example (RU) |
|----------|----------------|
| EXPLICIT | «восстановить» в прямом коммерческом/задачном контексте |
| STRONG | устойчивое сочетание с объектом услуги |
| MEDIUM | доменный термин без глагола действия |
| WEAK | тематическое соседство |
| NONE | отсутствует |

**typical intent/goal influence:** REQUEST_RECOVERY
### AUDIT_DIAGNOSTIC

**definition:** Аудит, диагностика, обследование.

| strength | example (RU) |
|----------|----------------|
| EXPLICIT | «аудит» в прямом коммерческом/задачном контексте |
| STRONG | устойчивое сочетание с объектом услуги |
| MEDIUM | доменный термин без глагола действия |
| WEAK | тематическое соседство |
| NONE | отсутствует |

**typical intent/goal influence:** REQUEST_AUDIT_OR_DIAGNOSTIC
### MIGRATION

**definition:** Миграция, перенос данных.

| strength | example (RU) |
|----------|----------------|
| EXPLICIT | «миграция» в прямом коммерческом/задачном контексте |
| STRONG | устойчивое сочетание с объектом услуги |
| MEDIUM | доменный термин без глагола действия |
| WEAK | тематическое соседство |
| NONE | отсутствует |

**typical intent/goal influence:** REQUEST_MIGRATION
### MAINTENANCE

**definition:** Плановое обслуживание, ТО.

| strength | example (RU) |
|----------|----------------|
| EXPLICIT | «обслуживание» в прямом коммерческом/задачном контексте |
| STRONG | устойчивое сочетание с объектом услуги |
| MEDIUM | доменный термин без глагола действия |
| WEAK | тематическое соседство |
| NONE | отсутствует |

**typical intent/goal influence:** REQUEST_MAINTENANCE
### PROBLEM

**definition:** Проблема, ошибка, не работает.

| strength | example (RU) |
|----------|----------------|
| EXPLICIT | «не работает» в прямом коммерческом/задачном контексте |
| STRONG | устойчивое сочетание с объектом услуги |
| MEDIUM | доменный термин без глагола действия |
| WEAK | тематическое соседство |
| NONE | отсутствует |

**typical intent/goal influence:** PROBLEM_UNRESOLVED
### DIY

**definition:** Самостоятельное выполнение.

| strength | example (RU) |
|----------|----------------|
| EXPLICIT | «самому» в прямом коммерческом/задачном контексте |
| STRONG | устойчивое сочетание с объектом услуги |
| MEDIUM | доменный термин без глагола действия |
| WEAK | тематическое соседство |
| NONE | отсутствует |

**typical intent/goal influence:** DIY_HOW_TO
### INFORMATIONAL

**definition:** Информационный запрос.

| strength | example (RU) |
|----------|----------------|
| EXPLICIT | «что такое» в прямом коммерческом/задачном контексте |
| STRONG | устойчивое сочетание с объектом услуги |
| MEDIUM | доменный термин без глагола действия |
| WEAK | тематическое соседство |
| NONE | отсутствует |

**typical intent/goal influence:** INFORMATIONAL
### EDUCATIONAL

**definition:** Обучение, курс, тренинг.

| strength | example (RU) |
|----------|----------------|
| EXPLICIT | «курс» в прямом коммерческом/задачном контексте |
| STRONG | устойчивое сочетание с объектом услуги |
| MEDIUM | доменный термин без глагола действия |
| WEAK | тематическое соседство |
| NONE | отсутствует |

**typical intent/goal influence:** EDUCATIONAL
### CAREER_SEEKER

**definition:** Соискатель: вакансия, работа, резюме.

| strength | example (RU) |
|----------|----------------|
| EXPLICIT | «вакансия» в прямом коммерческом/задачном контексте |
| STRONG | устойчивое сочетание с объектом услуги |
| MEDIUM | доменный термин без глагола действия |
| WEAK | тематическое соседство |
| NONE | отсутствует |

**typical intent/goal influence:** SEEK_EMPLOYMENT
### EMPLOYEE_HIRING

**definition:** Работодатель: требуется сотрудник, в штат.

| strength | example (RU) |
|----------|----------------|
| EXPLICIT | «требуется программист» в прямом коммерческом/задачном контексте |
| STRONG | устойчивое сочетание с объектом услуги |
| MEDIUM | доменный термин без глагола действия |
| WEAK | тематическое соседство |
| NONE | отсутствует |

**typical intent/goal influence:** HIRE_EMPLOYEE
### REGULATORY

**definition:** Нормативка: гост, санпин, закон.

| strength | example (RU) |
|----------|----------------|
| EXPLICIT | «санпин» в прямом коммерческом/задачном контексте |
| STRONG | устойчивое сочетание с объектом услуги |
| MEDIUM | доменный термин без глагола действия |
| WEAK | тематическое соседство |
| NONE | отсутствует |

**typical intent/goal influence:** REGULATORY
### NAVIGATIONAL

**definition:** Навигация на бренд/сайт.

| strength | example (RU) |
|----------|----------------|
| EXPLICIT | «официальный сайт» в прямом коммерческом/задачном контексте |
| STRONG | устойчивое сочетание с объектом услуги |
| MEDIUM | доменный термин без глагола действия |
| WEAK | тематическое соседство |
| NONE | отсутствует |

**typical intent/goal influence:** NAVIGATIONAL
### LOGIN

**definition:** Вход, логин, пароль.

| strength | example (RU) |
|----------|----------------|
| EXPLICIT | «войти» в прямом коммерческом/задачном контексте |
| STRONG | устойчивое сочетание с объектом услуги |
| MEDIUM | доменный термин без глагола действия |
| WEAK | тематическое соседство |
| NONE | отсутствует |

**typical intent/goal influence:** LOGIN_ACCOUNT_ACCESS
### DOCUMENTATION

**definition:** Документация, руководство.

| strength | example (RU) |
|----------|----------------|
| EXPLICIT | «документация» в прямом коммерческом/задачном контексте |
| STRONG | устойчивое сочетание с объектом услуги |
| MEDIUM | доменный термин без глагола действия |
| WEAK | тематическое соседство |
| NONE | отсутствует |

**typical intent/goal influence:** DOCUMENTATION_LOOKUP
### DOWNLOAD

**definition:** Скачивание ресурса.

| strength | example (RU) |
|----------|----------------|
| EXPLICIT | «скачать» в прямом коммерческом/задачном контексте |
| STRONG | устойчивое сочетание с объектом услуги |
| MEDIUM | доменный термин без глагола действия |
| WEAK | тематическое соседство |
| NONE | отсутствует |

**typical intent/goal influence:** DOWNLOAD_RESOURCE
### FREE

**definition:** Бесплатность.

| strength | example (RU) |
|----------|----------------|
| EXPLICIT | «бесплатно» в прямом коммерческом/задачном контексте |
| STRONG | устойчивое сочетание с объектом услуги |
| MEDIUM | доменный термин без глагола действия |
| WEAK | тематическое соседство |
| NONE | отсутствует |

**typical intent/goal influence:** DOWNLOAD_RESOURCE
### PRODUCT_MODULE

**definition:** Продукт, модуль, лицензия.

| strength | example (RU) |
|----------|----------------|
| EXPLICIT | «лицензия» в прямом коммерческом/задачном контексте |
| STRONG | устойчивое сочетание с объектом услуги |
| MEDIUM | доменный термин без глагола действия |
| WEAK | тематическое соседство |
| NONE | отсутствует |

**typical intent/goal influence:** BUY_PRODUCT_OR_MODULE
### VERSION_CONFIGURATION

**definition:** Версия, релиз, конфигурация 1с.

| strength | example (RU) |
|----------|----------------|
| EXPLICIT | «1с 8.3» в прямом коммерческом/задачном контексте |
| STRONG | устойчивое сочетание с объектом услуги |
| MEDIUM | доменный термин без глагола действия |
| WEAK | тематическое соседство |
| NONE | отсутствует |

**typical intent/goal influence:** REQUEST_CONFIGURATION
### INDUSTRY_CONTEXT

**definition:** Отраслевой контекст: общепит, склад, ритейл.

| strength | example (RU) |
|----------|----------------|
| EXPLICIT | «общепит» в прямом коммерческом/задачном контексте |
| STRONG | устойчивое сочетание с объектом услуги |
| MEDIUM | доменный термин без глагола действия |
| WEAK | тематическое соседство |
| NONE | отсутствует |

**typical intent/goal influence:** context modifier
### MALFORMED_NOISE

**definition:** Мусор, неразборчивый ввод.

| strength | example (RU) |
|----------|----------------|
| EXPLICIT | «asdfgh» в прямом коммерческом/задачном контексте |
| STRONG | устойчивое сочетание с объектом услуги |
| MEDIUM | доменный термин без глагола действия |
| WEAK | тематическое соседство |
| NONE | отсутствует |

**typical intent/goal influence:** MALFORMED


---

## Conflict patterns

| Conflict | Signals | Ambiguity type |
|----------|---------|----------------|
| Provider vs DIY | PROVIDER_HIRE vs DIY | PROVIDER_VS_DIY |
| Product vs service | PRODUCT_MODULE vs IMPLEMENTATION | PRODUCT_VS_SERVICE |
| Career vs provider | CAREER_SEEKER vs PROVIDER_HIRE | CAREER_VS_PROVIDER |
| Support vs info | SUPPORT vs INFORMATIONAL | SUPPORT_VS_INFORMATION |
| Free vs paid | FREE vs TRANSACTION | may affect eligibility |

Set `conflict_flag: true` on opposing signals; unresolved conflicts → ABSTAIN.

---

## Related documents

- [`ORCA-PRIMARY-INTENT-TAXONOMY-v1.md`](ORCA-PRIMARY-INTENT-TAXONOMY-v1.md)
- [`ORCA-AMBIGUITY-TAXONOMY-v1.md`](ORCA-AMBIGUITY-TAXONOMY-v1.md)
