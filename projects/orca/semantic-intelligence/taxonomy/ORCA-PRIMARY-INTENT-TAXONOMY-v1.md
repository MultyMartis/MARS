# ORCA Primary Intent Taxonomy v1

**Taxonomy ID:** `orca-primary-intent-taxonomy`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`  
**Machine reference:** [`orca-primary-intent-taxonomy-v1.json`](orca-primary-intent-taxonomy-v1.json)

---

## Purpose

Controlled vocabulary of **27 primary intents** for ORCA Semantic Intelligence v1. Primary intent describes the user's **most likely next task**, not topical category and **not** final PPC commercial eligibility.

> **Critical boundary:** `primary_intent` is **not** the final PPC decision. Commercial outcome lives in `commercial_eligibility.decision` (ACCEPT / REJECT / ABSTAIN). A query may be `PROBLEM_UNRESOLVED` with ACCEPT, or `HIRE_SERVICE` with ABSTAIN, depending on evidence.

---

## Intent families

| Family | Intents |
|--------|---------|
| `commercial` | HIRE_SERVICE, REQUEST_* (10), BUY_PRODUCT_OR_MODULE |
| `problem_self_service` | PROBLEM_UNRESOLVED, TROUBLESHOOT_SELF, DIY_HOW_TO, DOCUMENTATION_LOOKUP, DOWNLOAD_RESOURCE |
| `knowledge_regulation` | INFORMATIONAL, EDUCATIONAL, REGULATORY |
| `employment_navigation` | CAREER_EMPLOYMENT, NAVIGATIONAL, LOGIN_ACCOUNT_ACCESS |
| `quality_uncertainty` | AMBIGUOUS, IRRELEVANT, MALFORMED, UNKNOWN |

---

## Protected classes

| protected_class | Intents |
|-----------------|---------|
| `career` | CAREER_EMPLOYMENT |
| `educational` | EDUCATIONAL |
| `diy_how_to` | DIY_HOW_TO |
| `regulatory` | REGULATORY |
| `navigational` | NAVIGATIONAL |
| `null` | All others |

Protected strata require conservative eligibility; conflicting protected signals may force ABSTAIN (see invariants 3–4).

---

## Intent catalog

### HIRE_SERVICE

| Поле | Значение |
|------|----------|
| **intent_id** | `HIRE_SERVICE` |
| **label** | Hire service provider |
| **family** | `commercial` |
| **protected_class** | `null` |
| **may_support_accept** | `True` |
| **human_review_normally_required** | `False` |

**definition:** Пользователь ищет внешнего исполнителя для оказания платной услуги: заказ, подбор подрядчика, выезд специалиста, аутсорсинг работ.

**inclusion criteria:**
- Явные глаголы найма/заказа: «заказать», «нанять», «вызвать», «под ключ»
- Запрос подрядчика, бригады, сервисной компании
- Коммерческий контекст + услуга без признаков DIY или обучения

**exclusion criteria:**
- Покупка готового продукта/лицензии без услуги (→ BUY_PRODUCT_OR_MODULE)
- Самостоятельное выполнение (→ DIY_HOW_TO)
- Только информация о ценах без запроса исполнителя (→ INFORMATIONAL / AMBIGUOUS)

**positive examples:**
- «заказать внедрение crm под ключ»
- «найти подрядчика на монтаж вентиляции москва»
- «вызвать мастера по ремонту холодильного оборудования»

**counterexamples:**
- «сколько стоит внедрение crm»
- «как самому настроить crm»
- «вакансия инженер по вентиляции»

**common confusions:**
- REQUEST_IMPLEMENTATION (акцент на работе, не на найме)
- REQUEST_QUOTE goal vs HIRE_SERVICE intent
- BUY_PRODUCT_OR_MODULE при «купить и установить»

### REQUEST_IMPLEMENTATION

| Поле | Значение |
|------|----------|
| **intent_id** | `REQUEST_IMPLEMENTATION` |
| **label** | Request implementation |
| **family** | `commercial` |
| **protected_class** | `null` |
| **may_support_accept** | `True` |
| **human_review_normally_required** | `False` |

**definition:** Запрос на выполнение внедрения, развёртывания, запуска системы или комплекса работ исполнителем.

**inclusion criteria:**
- Внедрение, инсталляция, развёртывание, запуск «под ключ»
- IMPLEMENTATION signal STRONG/EXPLICIT

**exclusion criteria:**
- Только настройка параметров (→ REQUEST_CONFIGURATION)
- Только интеграция API (→ REQUEST_INTEGRATION)
- Обучение процессу (→ EDUCATIONAL)

**positive examples:**
- «внедрение 1с erp на предприятии»
- «развернуть bi систему на сервере заказчика»
- «запуск сквозной аналитики под ключ»

**counterexamples:**
- «что такое внедрение erp»
- «настроить отчёт в 1с самостоятельно»
- «интеграция 1с с сайтом api»

**common confusions:**
- HIRE_SERVICE
- REQUEST_CONFIGURATION
- REQUEST_INTEGRATION

### REQUEST_CONFIGURATION

| Поле | Значение |
|------|----------|
| **intent_id** | `REQUEST_CONFIGURATION` |
| **label** | Request configuration |
| **family** | `commercial` |
| **protected_class** | `null` |
| **may_support_accept** | `True` |
| **human_review_normally_required** | `False` |

**definition:** Запрос на настройку, параметризацию, конфигурацию существующей системы без полного внедрения с нуля.

**inclusion criteria:**
- Настройка модулей, ролей, справочников, workflow
- VERSION_CONFIGURATION + CONFIGURATION signals

**exclusion criteria:**
- Полное внедрение с нуля (→ REQUEST_IMPLEMENTATION)
- Самостоятельная настройка (→ DIY_HOW_TO / TROUBLESHOOT_SELF)

**positive examples:**
- «настроить права доступа в crm»
- «конфигурация отчётов 1с под наш учёт»
- «параметризация модуля складского учёта»

**counterexamples:**
- «как настроить crm самому»
- «внедрение crm с нуля»
- «скачать конфигурацию 1с»

**common confusions:**
- REQUEST_MODIFICATION
- DIY_HOW_TO
- DOCUMENTATION_LOOKUP

### REQUEST_MODIFICATION

| Поле | Значение |
|------|----------|
| **intent_id** | `REQUEST_MODIFICATION` |
| **label** | Request modification |
| **family** | `commercial` |
| **protected_class** | `null` |
| **may_support_accept** | `True` |
| **human_review_normally_required** | `False` |

**definition:** Запрос на доработку, изменение, кастомизацию существующего решения под требования заказчика.

**inclusion criteria:**
- Доработка, кастомизация, изменение логики/форм/отчётов
- MODIFICATION signal

**exclusion criteria:**
- Новая интеграция как отдельный проект (→ REQUEST_INTEGRATION)
- Исправление сбоя (→ REQUEST_SUPPORT / REQUEST_RECOVERY)

**positive examples:**
- «доработать отчёт в 1с под требования»
- «изменить форму заказа в crm»
- «кастомизация модуля производства»

**counterexamples:**
- «как изменить отчёт в 1с инструкция»
- «интеграция crm с телефонией»
- «ошибка при сохранении формы»

**common confusions:**
- REQUEST_CONFIGURATION
- REQUEST_INTEGRATION
- REQUEST_SUPPORT

### REQUEST_INTEGRATION

| Поле | Значение |
|------|----------|
| **intent_id** | `REQUEST_INTEGRATION` |
| **label** | Request integration |
| **family** | `commercial` |
| **protected_class** | `null` |
| **may_support_accept** | `True` |
| **human_review_normally_required** | `False` |

**definition:** Запрос на соединение систем, обмен данными, API-интеграцию, синхронизацию между платформами.

**inclusion criteria:**
- Интеграция, API, обмен, синхронизация, коннектор
- INTEGRATION signal

**exclusion criteria:**
- Внутренняя настройка одной системы (→ REQUEST_CONFIGURATION)
- Миграция данных как отдельная услуга (→ REQUEST_MIGRATION)

**positive examples:**
- «интеграция 1с с интернет магазином»
- «подключить crm к телефонии asterisk»
- «api обмен заказами между erp и wms»

**counterexamples:**
- «что такое api интеграция»
- «как самому подключить 1с к сайту»
- «миграция данных из старой crm»

**common confusions:**
- REQUEST_MIGRATION
- REQUEST_IMPLEMENTATION
- DIY_HOW_TO

### REQUEST_SUPPORT

| Поле | Значение |
|------|----------|
| **intent_id** | `REQUEST_SUPPORT` |
| **label** | Request support |
| **family** | `commercial` |
| **protected_class** | `null` |
| **may_support_accept** | `True` |
| **human_review_normally_required** | `False` |

**definition:** Запрос технической поддержки, сопровождения, консультации по работающей системе в рамках сервисного контракта или разовой помощи.

**inclusion criteria:**
- Техподдержка, сопровождение, консультация специалиста по инциденту
- SUPPORT signal без явного DIY

**exclusion criteria:**
- Только справочная информация (→ INFORMATIONAL)
- Восстановление после катастрофы (→ REQUEST_RECOVERY)
- Самодиагностика (→ TROUBLESHOOT_SELF)

**positive examples:**
- «техподдержка 1с удалённо»
- «консультация специалиста по ошибке проведения»
- «абонентское сопровождение crm»

**counterexamples:**
- «как исправить ошибку 1с самому»
- «что такое техподдержка 1с»
- «восстановить базу после сбоя»

**common confusions:**
- REQUEST_RECOVERY
- TROUBLESHOOT_SELF
- SUPPORT_VS_INFORMATION ambiguity

### REQUEST_RECOVERY

| Поле | Значение |
|------|----------|
| **intent_id** | `REQUEST_RECOVERY` |
| **label** | Request recovery |
| **family** | `commercial` |
| **protected_class** | `null` |
| **may_support_accept** | `True` |
| **human_review_normally_required** | `False` |

**definition:** Запрос на восстановление работоспособности, данных, доступа или операции после сбоя, потери или блокировки.

**inclusion criteria:**
- Восстановление базы, данных, доступа, работы после сбоя
- RECOVERY + PROBLEM signals

**exclusion criteria:**
- Профилактика (→ REQUEST_MAINTENANCE)
- Общая диагностика без срочности (→ REQUEST_AUDIT_OR_DIAGNOSTIC)

**positive examples:**
- «восстановить базу 1с после сбоя»
- «вернуть доступ к crm после блокировки»
- «экстренное восстановление сервера»

**counterexamples:**
- «как восстановить базу 1с инструкция»
- «аудит it инфраструктуры»
- «плановое обслуживание сервера»

**common confusions:**
- REQUEST_SUPPORT
- DIY_HOW_TO
- REQUEST_AUDIT_OR_DIAGNOSTIC

### REQUEST_AUDIT_OR_DIAGNOSTIC

| Поле | Значение |
|------|----------|
| **intent_id** | `REQUEST_AUDIT_OR_DIAGNOSTIC` |
| **label** | Request audit or diagnostic |
| **family** | `commercial` |
| **protected_class** | `null` |
| **may_support_accept** | `True` |
| **human_review_normally_required** | `False` |

**definition:** Запрос на аудит, диагностику, обследование, оценку состояния системы или процессов с целью выявления проблем.

**inclusion criteria:**
- Аудит, диагностика, обследование, экспертиза
- AUDIT_DIAGNOSTIC signal

**exclusion criteria:**
- Самостоятельная диагностика (→ TROUBLESHOOT_SELF)
- Регуляторная проверка (→ REGULATORY)

**positive examples:**
- «аудит it инфраструктуры предприятия»
- «диагностика производительности 1с»
- «обследование crm перед миграцией»

**counterexamples:**
- «как проверить производительность 1с»
- «требования регулятора к it»
- «ошибка 1с что делать»

**common confusions:**
- REQUEST_SUPPORT
- REGULATORY
- PROBLEM_UNRESOLVED

### REQUEST_MIGRATION

| Поле | Значение |
|------|----------|
| **intent_id** | `REQUEST_MIGRATION` |
| **label** | Request migration |
| **family** | `commercial` |
| **protected_class** | `null` |
| **may_support_accept** | `True` |
| **human_review_normally_required** | `False` |

**definition:** Запрос на перенос данных, системы или инфраструктуры с одной платформы/версии на другую.

**inclusion criteria:**
- Миграция, перенос, переход на новую версию/платформу
- MIGRATION signal

**exclusion criteria:**
- Интеграция без переноса (→ REQUEST_INTEGRATION)
- Внедрение с нуля (→ REQUEST_IMPLEMENTATION)

**positive examples:**
- «миграция данных из старой crm в битрикс24»
- «переход с 1с 7.7 на 1с 8.3»
- «перенос почты на новый сервер»

**counterexamples:**
- «как перенести данные crm самостоятельно»
- «интеграция двух crm»
- «что такое миграция данных»

**common confusions:**
- REQUEST_INTEGRATION
- REQUEST_IMPLEMENTATION
- DIY_HOW_TO

### REQUEST_MAINTENANCE

| Поле | Значение |
|------|----------|
| **intent_id** | `REQUEST_MAINTENANCE` |
| **label** | Request maintenance |
| **family** | `commercial` |
| **protected_class** | `null` |
| **may_support_accept** | `True` |
| **human_review_normally_required** | `False` |

**definition:** Запрос на плановое обслуживание, сопровождение, регламентные работы без аварийного восстановления.

**inclusion criteria:**
- ТО, регламентное обслуживание, абонентское сопровождение
- MAINTENANCE signal

**exclusion criteria:**
- Аварийное восстановление (→ REQUEST_RECOVERY)
- Разовая поддержка по инциденту (→ REQUEST_SUPPORT)

**positive examples:**
- «абонентское обслуживание серверов»
- «регламентное то холодильного оборудования»
- «ежемесячное сопровождение 1с»

**counterexamples:**
- «как обслуживать кондиционер самому»
- «срочное восстановление сервера»
- «техподдержка по ошибке»

**common confusions:**
- REQUEST_SUPPORT
- HIRE_SERVICE
- DIY_HOW_TO

### BUY_PRODUCT_OR_MODULE

| Поле | Значение |
|------|----------|
| **intent_id** | `BUY_PRODUCT_OR_MODULE` |
| **label** | Buy product or module |
| **family** | `commercial` |
| **protected_class** | `null` |
| **may_support_accept** | `True` |
| **human_review_normally_required** | `True` |

**definition:** Намерение приобрести продукт, лицензию, модуль, оборудование или ПО как товар, а не услугу внедрения.

**inclusion criteria:**
- Купить, приобрести, лицензия, модуль, оборудование
- PRODUCT_MODULE + TRANSACTION signals

**exclusion criteria:**
- Услуга внедрения без покупки продукта (→ REQUEST_IMPLEMENTATION)
- Бесплатная загрузка (→ DOWNLOAD_RESOURCE)

**positive examples:**
- «купить лицензию 1с erp»
- «цена модуля складского учёта»
- «приобрести промышленный холодильник»

**counterexamples:**
- «заказать внедрение 1с»
- «скачать демо версию 1с»
- «как выбрать crm бесплатно»

**common confusions:**
- HIRE_SERVICE
- PRODUCT_VS_SERVICE ambiguity
- INFORMATIONAL (сравнение цен)

### PROBLEM_UNRESOLVED

| Поле | Значение |
|------|----------|
| **intent_id** | `PROBLEM_UNRESOLVED` |
| **label** | Unresolved problem |
| **family** | `problem_self_service` |
| **protected_class** | `null` |
| **may_support_accept** | `False` |
| **human_review_normally_required** | `True` |

**definition:** Описание проблемы или симптома без явного выбора пути: найм, DIY, документация или поддержка.

**inclusion criteria:**
- Симптом, ошибка, «не работает» без глагола действия
- PROBLEM signal без PROVIDER_HIRE/DIY

**exclusion criteria:**
- Явный запрос мастера (→ HIRE_SERVICE)
- Явная инструкция (→ DIY_HOW_TO)

**positive examples:**
- «1с не проводит документ»
- «холодильник не морозит»
- «crm не сохраняет заказ»

**counterexamples:**
- «вызвать мастера холодильник не морозит»
- «как исправить ошибку 1с»
- «техподдержка 1с»

**common confusions:**
- TROUBLESHOOT_SELF
- REQUEST_SUPPORT
- PROVIDER_VS_DIY ambiguity

### TROUBLESHOOT_SELF

| Поле | Значение |
|------|----------|
| **intent_id** | `TROUBLESHOOT_SELF` |
| **label** | Self-troubleshoot |
| **family** | `problem_self_service` |
| **protected_class** | `null` |
| **may_support_accept** | `False` |
| **human_review_normally_required** | `True` |

**definition:** Пользователь пытается самостоятельно диагностировать или устранить проблему; ищет причину, код ошибки, способ исправления.

**inclusion criteria:**
- «почему», «что значит ошибка», «как исправить» в контексте сбоя
- PROBLEM + слабый DIY

**exclusion criteria:**
- Чистый how-to без проблемы (→ DIY_HOW_TO)
- Запрос специалиста (→ REQUEST_SUPPORT)

**positive examples:**
- «ошибка 1с 1234 что означает»
- «почему crm тормозит»
- «не открывается база 1с причины»

**counterexamples:**
- «заказать восстановление базы 1с»
- «инструкция по настройке отчёта»
- «скачать обновление 1с»

**common confusions:**
- DIY_HOW_TO
- PROBLEM_UNRESOLVED
- DOCUMENTATION_LOOKUP

### DIY_HOW_TO

| Поле | Значение |
|------|----------|
| **intent_id** | `DIY_HOW_TO` |
| **label** | DIY how-to |
| **family** | `problem_self_service` |
| **protected_class** | diy_how_to |
| **may_support_accept** | `False` |
| **human_review_normally_required** | `True` |

**definition:** Запрос инструкции для самостоятельного выполнения задачи без привлечения платного исполнителя.

**inclusion criteria:**
- «как сделать», «как настроить», «пошагово», «своими руками»
- DIY signal STRONG/EXPLICIT

**exclusion criteria:**
- Заказ услуги (→ HIRE_SERVICE)
- Обучающий курс (→ EDUCATIONAL)

**positive examples:**
- «как самому настроить 1с отчёт»
- «как подключить принтер к crm инструкция»
- «монтаж вентиляции своими руками»

**counterexamples:**
- «заказать монтаж вентиляции»
- «курс по 1с для начинающих»
- «требования снип к вентиляции»

**common confusions:**
- EDUCATIONAL
- DOCUMENTATION_LOOKUP
- PROVIDER_VS_DIY

### DOCUMENTATION_LOOKUP

| Поле | Значение |
|------|----------|
| **intent_id** | `DOCUMENTATION_LOOKUP` |
| **label** | Documentation lookup |
| **family** | `problem_self_service` |
| **protected_class** | `null` |
| **may_support_accept** | `False` |
| **human_review_normally_required** | `True` |

**definition:** Поиск официальной или справочной документации, руководства, API reference, release notes.

**inclusion criteria:**
- Документация, руководство, manual, api docs
- DOCUMENTATION signal

**exclusion criteria:**
- Обучение (→ EDUCATIONAL)
- Скачивание файла (→ DOWNLOAD_RESOURCE)

**positive examples:**
- «документация api битрикс24»
- «руководство пользователя 1с erp»
- «справка по функции проведения»

**counterexamples:**
- «скачать руководство 1с pdf»
- «курс 1с с нуля»
- «заказать консультацию по 1с»

**common confusions:**
- DOWNLOAD_RESOURCE
- INFORMATIONAL
- DIY_HOW_TO

### DOWNLOAD_RESOURCE

| Поле | Значение |
|------|----------|
| **intent_id** | `DOWNLOAD_RESOURCE` |
| **label** | Download resource |
| **family** | `problem_self_service` |
| **protected_class** | `null` |
| **may_support_accept** | `False` |
| **human_review_normally_required** | `True` |

**definition:** Намерение скачать, загрузить бесплатный ресурс: дистрибутив, демо, шаблон, драйвер, обновление.

**inclusion criteria:**
- Скачать, загрузить, download, демо, бесплатно
- DOWNLOAD + FREE signals

**exclusion criteria:**
- Покупка (→ BUY_PRODUCT_OR_MODULE)
- Только чтение docs (→ DOCUMENTATION_LOOKUP)

**positive examples:**
- «скачать демо 1с»
- «загрузить драйвер принтера»
- «бесплатный шаблон crm excel»

**counterexamples:**
- «купить лицензию 1с»
- «документация 1с онлайн»
- «заказать установку 1с»

**common confusions:**
- BUY_PRODUCT_OR_MODULE
- DOCUMENTATION_LOOKUP
- FREE signal vs commercial

### INFORMATIONAL

| Поле | Значение |
|------|----------|
| **intent_id** | `INFORMATIONAL` |
| **label** | Informational |
| **family** | `knowledge_regulation` |
| **protected_class** | `null` |
| **may_support_accept** | `False` |
| **human_review_normally_required** | `True` |

**definition:** Общий информационный запрос: что это, сколько стоит, сравнение, обзор без явного коммерческого действия.

**inclusion criteria:**
- Что такое, обзор, сравнение, цена без заказа
- INFORMATIONAL signal

**exclusion criteria:**
- Обучение (→ EDUCATIONAL)
- Нормативка (→ REGULATORY)
- Найм (→ HIRE_SERVICE)

**positive examples:**
- «что такое crm система»
- «сравнение битрикс24 и amocrm»
- «сколько стоит внедрение erp»

**counterexamples:**
- «заказать внедрение erp»
- «курс crm для менеджеров»
- «санпин требования к холодильнику»

**common confusions:**
- EDUCATIONAL
- COMPARE_OPTIONS goal
- SUPPORT_VS_INFORMATION

### EDUCATIONAL

| Поле | Значение |
|------|----------|
| **intent_id** | `EDUCATIONAL` |
| **label** | Educational |
| **family** | `knowledge_regulation` |
| **protected_class** | educational |
| **may_support_accept** | `False` |
| **human_review_normally_required** | `True` |

**definition:** Запрос обучения, курса, тренинга, сертификации, учебных материалов для развития навыков.

**inclusion criteria:**
- Курс, обучение, тренинг, сертификация, урок
- EDUCATIONAL signal

**exclusion criteria:**
- Разовая инструкция (→ DIY_HOW_TO)
- Документация продукта (→ DOCUMENTATION_LOOKUP)

**positive examples:**
- «курс 1с программирование»
- «обучение crm для отдела продаж»
- «сертификация 1с специалист»

**counterexamples:**
- «как настроить отчёт в 1с»
- «заказать внедрение 1с»
- «вакансия 1с программист»

**common confusions:**
- DIY_HOW_TO
- CAREER_EMPLOYMENT
- DOCUMENTATION_LOOKUP

### REGULATORY

| Поле | Значение |
|------|----------|
| **intent_id** | `REGULATORY` |
| **label** | Regulatory |
| **family** | `knowledge_regulation` |
| **protected_class** | regulatory |
| **may_support_accept** | `False` |
| **human_review_normally_required** | `True` |

**definition:** Запрос нормативных требований, законов, стандартов, сертификации продукции, compliance.

**inclusion criteria:**
- СНиП, ГОСТ, санпин, закон, требования регулятора
- REGULATORY signal

**exclusion criteria:**
- Внедрение под нормы (→ REGULATORY_VS_IMPLEMENTATION)
- Общая информация (→ INFORMATIONAL)

**positive examples:**
- «требования санпин к холодильному оборудованию»
- «гост на вентиляцию общепита»
- «нужна ли лицензия на монтаж»

**counterexamples:**
- «заказать монтаж по санпин»
- «как выбрать холодильник»
- «аудит соответствия санпин»

**common confusions:**
- REQUEST_AUDIT_OR_DIAGNOSTIC
- INFORMATIONAL
- REGULATORY_VS_IMPLEMENTATION

### CAREER_EMPLOYMENT

| Поле | Значение |
|------|----------|
| **intent_id** | `CAREER_EMPLOYMENT` |
| **label** | Career or employment |
| **family** | `employment_navigation` |
| **protected_class** | career |
| **may_support_accept** | `False` |
| **human_review_normally_required** | `True` |

**definition:** Запросы о трудоустройстве: поиск работы соискателем или найм сотрудника работодателем.

**inclusion criteria:**
- Вакансия, резюме, работа, зарплата, карьера
- CAREER_SEEKER или EMPLOYEE_HIRING signals

**exclusion criteria:**
- Найм подрядчика (→ HIRE_SERVICE / HIRE_PROVIDER goal)
- Навигация на hh.ru (→ NAVIGATIONAL)

**positive examples:**
- «вакансия 1с программист москва»
- «работа инженер по вентиляции»
- «резюме системный администратор»

**counterexamples:**
- «найти подрядчика на монтаж»
- «курс 1с для начинающих»
- «сайт компании вакансии»

**common confusions:**
- HIRE_SERVICE
- CAREER_VS_PROVIDER
- SEEK_EMPLOYMENT vs HIRE_EMPLOYEE goals

### NAVIGATIONAL

| Поле | Значение |
|------|----------|
| **intent_id** | `NAVIGATIONAL` |
| **label** | Navigational |
| **family** | `employment_navigation` |
| **protected_class** | navigational |
| **may_support_accept** | `False` |
| **human_review_normally_required** | `True` |

**definition:** Поиск конкретного сайта, бренда, личного кабинета, официальной страницы без коммерческого запроса услуги.

**inclusion criteria:**
- Название бренда + сайт/официальный/личный кабинет
- NAVIGATIONAL signal EXPLICIT

**exclusion criteria:**
- Запрос услуги бренда (→ commercial intents)
- Вход в аккаунт (→ LOGIN_ACCOUNT_ACCESS)

**positive examples:**
- «сайт 1с официальный»
- «битрикс24 личный кабинет»
- «компания триумф манипулятор»

**counterexamples:**
- «заказать 1с внедрение»
- «войти в битрикс24»
- «что такое битрикс24»

**common confusions:**
- LOGIN_ACCOUNT_ACCESS
- INFORMATIONAL
- HIRE_SERVICE (бренд + услуга)

### LOGIN_ACCOUNT_ACCESS

| Поле | Значение |
|------|----------|
| **intent_id** | `LOGIN_ACCOUNT_ACCESS` |
| **label** | Login or account access |
| **family** | `employment_navigation` |
| **protected_class** | `null` |
| **may_support_accept** | `False` |
| **human_review_normally_required** | `True` |

**definition:** Попытка входа в систему, восстановления пароля, доступа к аккаунту или личному кабинету.

**inclusion criteria:**
- Войти, логин, пароль, восстановить доступ
- LOGIN signal

**exclusion criteria:**
- Навигация на сайт без входа (→ NAVIGATIONAL)
- Техподдержка по доступу как услуга (→ REQUEST_SUPPORT)

**positive examples:**
- «войти в 1с онлайн»
- «восстановить пароль битрикс24»
- «не могу зайти в личный кабинет»

**counterexamples:**
- «сайт битрикс24»
- «техподдержка восстановление доступа»
- «заказать crm»

**common confusions:**
- NAVIGATIONAL
- REQUEST_RECOVERY
- REQUEST_SUPPORT

### AMBIGUOUS

| Поле | Значение |
|------|----------|
| **intent_id** | `AMBIGUOUS` |
| **label** | Ambiguous |
| **family** | `quality_uncertainty` |
| **protected_class** | `null` |
| **may_support_accept** | `False` |
| **human_review_normally_required** | `True` |

**definition:** Фраза допускает несколько равновероятных задач; автоматика не может выбрать primary intent без дополнительного контекста.

**inclusion criteria:**
- Короткий head-term
- Конфликт сигналов без разрешения
- MULTIPLE ambiguity types

**exclusion criteria:**
- Достаточно evidence для одного intent
- Мусор/нерелевант (→ IRRELEVANT/MALFORMED)

**positive examples:**
- «1с»
- «crm»
- «холодильник»
- «вентиляция»

**counterexamples:**
- «заказать внедрение 1с под ключ»
- «как настроить 1с отчёт»
- «вакансия 1с»

**common confusions:**
- UNKNOWN
- SHORT_HEAD_TERM
- INFORMATIONAL при слабом контексте

### IRRELEVANT

| Поле | Значение |
|------|----------|
| **intent_id** | `IRRELEVANT` |
| **label** | Irrelevant |
| **family** | `quality_uncertainty` |
| **protected_class** | `null` |
| **may_support_accept** | `False` |
| **human_review_normally_required** | `False` |

**definition:** Запрос не относится к домену услуг/продуктов кампании; тематически чужой или бессмысленный в контексте.

**inclusion criteria:**
- Нет пересечения с service catalog
- Другая отрасль/тема без связи

**exclusion criteria:**
- Неясный но доменный (→ AMBIGUOUS)
- Повреждённый ввод (→ MALFORMED)

**positive examples:**
- «рецепт борща»
- «погода москва»
- «купить кроссовки nike»

**counterexamples:**
- «купить промышленный холодильник»
- «1с»
- «asdfgh»

**common confusions:**
- MALFORMED
- AMBIGUOUS
- INFORMATIONAL в широком домене

### MALFORMED

| Поле | Значение |
|------|----------|
| **intent_id** | `MALFORMED` |
| **label** | Malformed |
| **family** | `quality_uncertainty` |
| **protected_class** | `null` |
| **may_support_accept** | `False` |
| **human_review_normally_required** | `False` |

**definition:** Синтаксически или лексически повреждённый запрос: опечатки-мусор, случайный набор символов, неразборчивый ввод.

**inclusion criteria:**
- MALFORMED_NOISE signal
- Нет лексем для интерпретации

**exclusion criteria:**
- Короткий но валидный термин (→ AMBIGUOUS)
- Иностранный язык валидный (→ нормальная классификация)

**positive examples:**
- «asdfghjkl»
- «1сьььь»
- «???!!!»
- «»

**counterexamples:**
- «1с»
- «crm система»
- «холодильник не работает»

**common confusions:**
- AMBIGUOUS
- IRRELEVANT
- UNKNOWN

### UNKNOWN

| Поле | Значение |
|------|----------|
| **intent_id** | `UNKNOWN` |
| **label** | Unknown |
| **family** | `quality_uncertainty` |
| **protected_class** | `null` |
| **may_support_accept** | `False` |
| **human_review_normally_required** | `True` |

**definition:** Недостаточно evidence для любого primary intent; отличается от AMBIGUOUS тем, что нет даже конкурирующих гипотез.

**inclusion criteria:**
- Пустой или near-empty после нормализации
- Все signals NONE
- provenance MISSING

**exclusion criteria:**
- Есть конкурирующие гипотезы (→ AMBIGUOUS)
- Явный мусор (→ MALFORMED)

**positive examples:**
- «»
- «…»
- «запрос без контекста в изолированном snapshot»

**counterexamples:**
- «1с внедрение»
- «как настроить»
- «вакансия»

**common confusions:**
- AMBIGUOUS
- MALFORMED
- provenance_status UNKNOWN


---

## Usage rules

1. Assign exactly one `primary_intent` per semantic record unless pipeline stage explicitly defers (pre-screen → UNKNOWN).
2. Use `secondary_intents` when a competing task has meaningful evidence but lower weight.
3. Do not map primary intent directly to campaign structure; no `campaign_group` or `ad_group` fields.
4. `may_support_accept: true` means the intent class **can** appear in ACCEPT records — not that it always should.
5. Pair every intent assignment with signal evidence; never infer full intent from one signal alone.

---

## Related documents

- [`ORCA-SEMANTIC-TAXONOMY-PRINCIPLES-v1.md`](ORCA-SEMANTIC-TAXONOMY-PRINCIPLES-v1.md)
- [`ORCA-USER-GOAL-TAXONOMY-v1.md`](ORCA-USER-GOAL-TAXONOMY-v1.md)
- [`ORCA-SEMANTIC-SIGNAL-TAXONOMY-v1.md`](ORCA-SEMANTIC-SIGNAL-TAXONOMY-v1.md)
- [`../schemas/ORCA-SEMANTIC-RECORD-SCHEMA-v1.md`](../schemas/ORCA-SEMANTIC-RECORD-SCHEMA-v1.md)
