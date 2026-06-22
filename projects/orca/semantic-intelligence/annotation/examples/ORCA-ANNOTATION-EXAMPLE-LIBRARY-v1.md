# ORCA Annotation Example Library v1

**Library ID:** orca-annotation-example-library  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** PROPOSED — OPERATOR APPROVAL REQUIRED  
**Machine reference:** [orca-annotation-example-library-v1.json](orca-annotation-example-library-v1.json)

---

## Purpose

Training illustrations for ORCA Semantic Intelligence v1 human annotation. **Not gold benchmark labels.**

Domain: B2B IT/PPC Russian (1С, CRM, ERP themes).

Each example includes: phrase, literal meaning, signals, primary intent, competing intent, eligibility, risk, reason, common wrong decision, why wrong fails.

---

## Clear ACCEPT examples (minimum 20)

*Count in this section: 24*

### ACC-01 — «заказать внедрение crm под ключ москва»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь хочет заказать полное внедрение CRM в Москве. |
| **Signals** | PROVIDER_HIRE:EXPLICIT:заказать; IMPLEMENTATION:STRONG:внедрение crm под ключ; GEO:MEDIUM:москва |
| **Primary intent** | REQUEST_IMPLEMENTATION |
| **Competing intent** | HIRE_SERVICE |
| **Eligibility** | **ACCEPT** |
| **Risk** | LOW |
| **Reason** | Явный глагол заказа и scoped implementation object; landing внедрения честно закрывает запрос. |
| **Common wrong decision** | ACCEPT по теме crm без глагола |
| **Why wrong fails** | Нет автоматического ACCEPT от доменного термина. |

### ACC-02 — «нужен подрядчик на интеграцию 1с с битрикс»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь ищет подрядчика для интеграции 1С с Битрикс. |
| **Signals** | PROVIDER_HIRE:EXPLICIT:нужен подрядчик; INTEGRATION:STRONG:интеграцию 1с с битрикс |
| **Primary intent** | REQUEST_INTEGRATION |
| **Competing intent** | HIRE_SERVICE |
| **Eligibility** | **ACCEPT** |
| **Risk** | LOW |
| **Reason** | EXPLICIT provider hire + integration task object. |
| **Common wrong decision** | ACCEPT из-за слова интеграция без подрядчика |
| **Why wrong fails** | Интеграция без hire-маркера часто ABSTAIN. |

### ACC-03 — «вызвать программиста 1с на выезд»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь хочет вызвать программиста 1С с выездом. |
| **Signals** | PROVIDER_HIRE:EXPLICIT:вызвать; SUPPORT:STRONG:программиста 1с на выезд |
| **Primary intent** | HIRE_SERVICE |
| **Competing intent** | REQUEST_SUPPORT |
| **Eligibility** | **ACCEPT** |
| **Risk** | LOW |
| **Reason** | Прямой запрос специалиста с выездом — paid service path. |
| **Common wrong decision** | REJECT как career из-за программист |
| **Why wrong fails** | Есть глагол вызвать — provider path, не вакансия. |

### ACC-04 — «доработка отчёта 1с на заказ»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь хочет заказать доработку отчёта в 1С. |
| **Signals** | MODIFICATION:EXPLICIT:доработка; PROVIDER_HIRE:MEDIUM:на заказ |
| **Primary intent** | REQUEST_MODIFICATION |
| **Competing intent** | HIRE_SERVICE |
| **Eligibility** | **ACCEPT** |
| **Risk** | LOW |
| **Reason** | Scoped modification с коммерческим framing «на заказ». |
| **Common wrong decision** | ABSTAIN как short head |
| **Why wrong fails** | Три токена с task object и заказ-маркером достаточны. |

### ACC-05 — «сопровождение 1с абонентская плата оформить»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь хочет оформить абонентское сопровождение 1С. |
| **Signals** | SUPPORT:STRONG:сопровождение 1с; PROVIDER_HIRE:MEDIUM:оформить; COMMERCIAL_PRICE:MEDIUM:абонентская плата |
| **Primary intent** | REQUEST_SUPPORT |
| **Competing intent** | HIRE_SERVICE |
| **Eligibility** | **ACCEPT** |
| **Risk** | MEDIUM |
| **Reason** | Контекст оформления и цены снимает short-head неоднозначность сопровождения. |
| **Common wrong decision** | ACCEPT на «сопровождение 1с» без контекста |
| **Why wrong fails** | Без оформить/цена — ABSTAIN. |

### ACC-06 — «аудит учётной политики 1с стоимость работ»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь интересуется стоимостью работ по аудиту учётной политики в 1С. |
| **Signals** | AUDIT_DIAGNOSTIC:STRONG:аудит учётной политики; COMMERCIAL_PRICE:EXPLICIT:стоимость работ |
| **Primary intent** | REQUEST_AUDIT |
| **Competing intent** | INFORMATIONAL |
| **Eligibility** | **ACCEPT** |
| **Risk** | MEDIUM |
| **Reason** | Цена работ + audit object — hire/quote path, не справка. |
| **Common wrong decision** | REJECT как informational quote |
| **Why wrong fails** | Стоимость работ на scoped audit — commercial quote. |

### ACC-07 — «восстановить базу 1с срочно специалист»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь срочно ищет специалиста для восстановления базы 1С. |
| **Signals** | RECOVERY:STRONG:восстановить базу 1с; PROVIDER_HIRE:EXPLICIT:специалист; URGENCY:MEDIUM:срочно |
| **Primary intent** | REQUEST_RECOVERY |
| **Competing intent** | PROBLEM_UNRESOLVED |
| **Eligibility** | **ACCEPT** |
| **Risk** | LOW |
| **Reason** | Problem + explicit specialist hire — paid recovery path. |
| **Common wrong decision** | ABSTAIN как чистый problem |
| **Why wrong fails** | Специалист явно запрошен. |

### ACC-08 — «интеграция erp с маркетплейсом под ключ»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь ищет интеграцию ERP с маркетплейсом под ключ. |
| **Signals** | INTEGRATION:STRONG:интеграция erp; IMPLEMENTATION:EXPLICIT:под ключ |
| **Primary intent** | REQUEST_INTEGRATION |
| **Competing intent** | HIRE_SERVICE |
| **Eligibility** | **ACCEPT** |
| **Risk** | LOW |
| **Reason** | Под ключ — implementation hire signal. |
| **Common wrong decision** | REJECT как product compare |
| **Why wrong fails** | Нет покупки ПО — услуга интеграции. |

### ACC-09 — «настройка обмена 1с заказать услугу»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь хочет заказать услугу настройки обмена в 1С. |
| **Signals** | CONFIGURATION:STRONG:настройка обмена; PROVIDER_HIRE:EXPLICIT:заказать услугу |
| **Primary intent** | REQUEST_CONFIGURATION |
| **Competing intent** | DIY_HOW_TO |
| **Eligibility** | **ACCEPT** |
| **Risk** | LOW |
| **Reason** | DIY конкурирует, но EXPLICIT заказать услугу разрешает. |
| **Common wrong decision** | ABSTAIN из-за настроить |
| **Why wrong fails** | Явный заказ услуги перевешивает DIY. |

### ACC-10 — «внедрение сквозной аналитики crm цена подрядчика»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь ищет цену подрядчика на внедрение сквозной аналитики в CRM. |
| **Signals** | IMPLEMENTATION:STRONG:внедрение; PROVIDER_HIRE:STRONG:цена подрядчика |
| **Primary intent** | REQUEST_IMPLEMENTATION |
| **Competing intent** | INFORMATIONAL |
| **Eligibility** | **ACCEPT** |
| **Risk** | LOW |
| **Reason** | Цена подрядчика — commercial quote path. |
| **Common wrong decision** | REJECT как price shopping only |
| **Why wrong fails** | Подрядчик указывает hire, не прайс-лист ПО. |

### ACC-11 — «доработка печатной формы 1с подрядчик москва»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь ищет подрядчика в Москве для доработки печатной формы 1С. |
| **Signals** | MODIFICATION:STRONG:доработка печатной формы; PROVIDER_HIRE:EXPLICIT:подрядчик; GEO:MEDIUM:москва |
| **Primary intent** | REQUEST_MODIFICATION |
| **Competing intent** | HIRE_SERVICE |
| **Eligibility** | **ACCEPT** |
| **Risk** | LOW |
| **Reason** | Scoped task + подрядчик. |
| **Common wrong decision** | ABSTAIN как печатная форма 1с |
| **Why wrong fails** | Добавлены подрядчик и доработка scope. |

### ACC-12 — «миграция данных из sap в 1с услуга»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь ищет услугу миграции данных из SAP в 1С. |
| **Signals** | MIGRATION:STRONG:миграция данных; PROVIDER_HIRE:MEDIUM:услуга |
| **Primary intent** | REQUEST_MIGRATION |
| **Competing intent** | INFORMATIONAL |
| **Eligibility** | **ACCEPT** |
| **Risk** | LOW |
| **Reason** | Migration object + услуга marker. |
| **Common wrong decision** | REJECT как IT topic |
| **Why wrong fails** | Миграция между ERP — типичная платная услуга. |

### ACC-13 — «обслуживание сервера 1с удалённо договор»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь хочет договор на удалённое обслуживание сервера 1С. |
| **Signals** | MAINTENANCE:STRONG:обслуживание сервера 1с; PROVIDER_HIRE:MEDIUM:договор |
| **Primary intent** | REQUEST_MAINTENANCE |
| **Competing intent** | HIRE_SERVICE |
| **Eligibility** | **ACCEPT** |
| **Risk** | LOW |
| **Reason** | Maintenance scope + commercial contract framing. |
| **Common wrong decision** | ABSTAIN как обслуживание |
| **Why wrong fails** | Договор и удалённо конкретизируют hire. |

### ACC-14 — «коммерческое предложение на внедрение erp»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь запрашивает коммерческое предложение на внедрение ERP. |
| **Signals** | COMMERCIAL_QUOTE:EXPLICIT:коммерческое предложение; IMPLEMENTATION:STRONG:внедрение erp |
| **Primary intent** | REQUEST_QUOTE |
| **Competing intent** | REQUEST_IMPLEMENTATION |
| **Eligibility** | **ACCEPT** |
| **Risk** | LOW |
| **Reason** | Явный КП запрос на implementation. |
| **Common wrong decision** | REJECT как document download |
| **Why wrong fails** | КП — commercial engagement, не шаблон. |

### ACC-15 — «найти компанию по внедрению 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь хочет найти компанию для внедрения 1С. |
| **Signals** | PROVIDER_HIRE:EXPLICIT:найти компанию; IMPLEMENTATION:STRONG:внедрению 1с |
| **Primary intent** | HIRE_SERVICE |
| **Competing intent** | REQUEST_IMPLEMENTATION |
| **Eligibility** | **ACCEPT** |
| **Risk** | LOW |
| **Reason** | Поиск компании = provider hire. |
| **Common wrong decision** | NAVIGATIONAL reject |
| **Why wrong fails** | Компания здесь — подрядчик, не сайт 1С. |

### ACC-16 — «1с не работает вызвать специалиста»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь сообщает, что 1С не работает, и хочет вызвать специалиста. |
| **Signals** | PROBLEM:STRONG:1с не работает; PROVIDER_HIRE:EXPLICIT:вызвать специалиста |
| **Primary intent** | REQUEST_SUPPORT |
| **Competing intent** | PROBLEM_UNRESOLVED |
| **Eligibility** | **ACCEPT** |
| **Risk** | LOW |
| **Reason** | Problem + explicit вызвать специалиста. |
| **Common wrong decision** | ABSTAIN как problem only |
| **Why wrong fails** | Вызвать специалиста — explicit provider. |

### ACC-17 — «настроить обмен с кассой заказать»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь хочет заказать настройку обмена с кассой. |
| **Signals** | CONFIGURATION:STRONG:настроить обмен с кассой; PROVIDER_HIRE:EXPLICIT:заказать |
| **Primary intent** | REQUEST_CONFIGURATION |
| **Competing intent** | DIY_HOW_TO |
| **Eligibility** | **ACCEPT** |
| **Risk** | LOW |
| **Reason** | Заказать разрешает provider vs DIY. |
| **Common wrong decision** | ABSTAIN на настроить |
| **Why wrong fails** | Без заказать — ABSTAIN. |

### ACC-18 — «разработка внешней обработки 1с цена работ»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь спрашивает цену работ на разработку внешней обработки 1С. |
| **Signals** | MODIFICATION:STRONG:разработка внешней обработки; COMMERCIAL_PRICE:EXPLICIT:цена работ |
| **Primary intent** | REQUEST_MODIFICATION |
| **Competing intent** | INFORMATIONAL |
| **Eligibility** | **ACCEPT** |
| **Risk** | MEDIUM |
| **Reason** | Цена работ на scoped dev task. |
| **Common wrong decision** | REJECT как DIY code |
| **Why wrong fails** | Цена работ — commercial, не пример кода. |

### ACC-19 — «внедрение маркировки в 1с под ключ»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь хочет внедрение маркировки в 1С под ключ. |
| **Signals** | IMPLEMENTATION:EXPLICIT:внедрение маркировки; REGULATORY_CONTEXT:MEDIUM:маркировки |
| **Primary intent** | REQUEST_IMPLEMENTATION |
| **Competing intent** | REGULATORY |
| **Eligibility** | **ACCEPT** |
| **Risk** | MEDIUM |
| **Reason** | Paid implementation under regulatory topic; под ключ decisive. |
| **Common wrong decision** | REJECT как regulatory info |
| **Why wrong fails** | Внедрение под ключ — service, не норма. |

### ACC-20 — «техподдержка 1с абонентское обслуживание оформить»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь хочет оформить абонентское техобслуживание 1С. |
| **Signals** | SUPPORT:STRONG:техподдержка 1с; PROVIDER_HIRE:MEDIUM:оформить; MAINTENANCE:MEDIUM:абонентское обслуживание |
| **Primary intent** | REQUEST_SUPPORT |
| **Competing intent** | HIRE_SERVICE |
| **Eligibility** | **ACCEPT** |
| **Risk** | LOW |
| **Reason** | Оформить + абонентка — commercial support path. |
| **Common wrong decision** | ABSTAIN на техподдержка 1с |
| **Why wrong fails** | Оформить снимает head-term ambiguity. |

### PVS-03 — «настроить купленную 1с заказать»

| Field | Value |
|-------|-------|
| **Literal meaning** | Заказать настройку уже купленной 1С. |
| **Signals** | CONFIGURATION:STRONG:настроить; PROVIDER_HIRE:EXPLICIT:заказать; PRODUCT:MEDIUM:купленную |
| **Primary intent** | REQUEST_CONFIGURATION |
| **Competing intent** | BUY_PRODUCT_OR_MODULE |
| **Eligibility** | **ACCEPT** |
| **Risk** | LOW |
| **Reason** | Service on owned product — ACCEPT. |
| **Common wrong decision** | REJECT product |
| **Why wrong fails** | Заказать настройку — service. |

### PVS-04 — «доработать купленный модуль 1с на заказ»

| Field | Value |
|-------|-------|
| **Literal meaning** | Доработать купленный модуль 1С на заказ. |
| **Signals** | MODIFICATION:STRONG:доработать; PROVIDER_HIRE:MEDIUM:на заказ |
| **Primary intent** | REQUEST_MODIFICATION |
| **Competing intent** | BUY_PRODUCT_OR_MODULE |
| **Eligibility** | **ACCEPT** |
| **Risk** | LOW |
| **Reason** | Modification service on owned module. |
| **Common wrong decision** | REJECT |
| **Why wrong fails** | На заказ — service. |

### CVP-03 — «нужен программист 1с на проект подряд»

| Field | Value |
|-------|-------|
| **Literal meaning** | Нужен программист 1С на проект по подряду. |
| **Signals** | PROVIDER_HIRE:EXPLICIT:подряд; ROLE:MEDIUM:программист |
| **Primary intent** | HIRE_SERVICE |
| **Competing intent** | CAREER_EMPLOYMENT |
| **Eligibility** | **ACCEPT** |
| **Risk** | MEDIUM |
| **Reason** | Подряд disambiguates contractor. |
| **Common wrong decision** | REJECT career |
| **Why wrong fails** | Подряд — provider. |

### CVP-06 — «аутсорсинг программистов 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Аутсорсинг программистов 1С. |
| **Signals** | PROVIDER_HIRE:STRONG:аутсорсинг; ROLE:MEDIUM:программистов |
| **Primary intent** | HIRE_SERVICE |
| **Competing intent** | CAREER_EMPLOYMENT |
| **Eligibility** | **ACCEPT** |
| **Risk** | LOW |
| **Reason** | Outsourcing — B2B provider. |
| **Common wrong decision** | REJECT |
| **Why wrong fails** | Not job seeker. |

---

## Clear REJECT examples (minimum 20)

*Count in this section: 32*

### REJ-01 — «вакансия программист 1с удалённо»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь ищет вакансию программиста 1С с удалённой работой. |
| **Signals** | CAREER:EXPLICIT:вакансия; ROLE:MEDIUM:программист 1с |
| **Primary intent** | CAREER_EMPLOYMENT |
| **Competing intent** | HIRE_SERVICE |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Dominant career stratum; protected REJECT. |
| **Common wrong decision** | ABSTAIN как short head |
| **Why wrong fails** | Вакансия — explicit career, не ABSTAIN. |

### REJ-02 — «курсы 1с бухгалтерия с нуля»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь ищет курсы 1С для бухгалтерии с нуля. |
| **Signals** | EDUCATION:EXPLICIT:курсы; EDUCATION:STRONG:с нуля |
| **Primary intent** | EDUCATIONAL |
| **Competing intent** | REQUEST_IMPLEMENTATION |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Dominant educational intent. |
| **Common wrong decision** | ACCEPT как commercial training sale |
| **Why wrong fails** | Нет hire подрядчика — обучение. |

### REJ-03 — «как настроить обмен 1с самому пошагово»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь хочет самостоятельную пошаговую настройку обмена 1С. |
| **Signals** | DIY:EXPLICIT:самому; DIY:STRONG:пошагово; HOW_TO:EXPLICIT:как настроить |
| **Primary intent** | DIY_HOW_TO |
| **Competing intent** | REQUEST_CONFIGURATION |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Explicit DIY markers. |
| **Common wrong decision** | ABSTAIN как настроить |
| **Why wrong fails** | Самому и пошагово — clear DIY. |

### REJ-04 — «скачать дистрибутив 1с бесплатно»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь хочет бесплатно скачать дистрибутив 1С. |
| **Signals** | DOWNLOAD:EXPLICIT:скачать; FREE:EXPLICIT:бесплатно; PRODUCT:STRONG:дистрибутив |
| **Primary intent** | DOWNLOAD_RESOURCE |
| **Competing intent** | BUY_PRODUCT_OR_MODULE |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Download/free — not service core. |
| **Common wrong decision** | ACCEPT как lead |
| **Why wrong fails** | Нет услуги — product/download. |

### REJ-05 — «личный кабинет 1с итс вход»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь хочет войти в личный кабинет 1С:ИТС. |
| **Signals** | NAVIGATION:EXPLICIT:личный кабинет; LOGIN:EXPLICIT:вход |
| **Primary intent** | LOGIN_ACCOUNT_ACCESS |
| **Competing intent** | NAVIGATIONAL |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Login/navigational dominant. |
| **Common wrong decision** | ABSTAIN |
| **Why wrong fails** | Clear login — REJECT. |

### REJ-06 — «требования маркировки молочной продукции 2025»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь ищет нормативные требования маркировки молочной продукции на 2025 год. |
| **Signals** | REGULATORY:EXPLICIT:требования; REGULATORY:STRONG:маркировки |
| **Primary intent** | REGULATORY |
| **Competing intent** | REQUEST_IMPLEMENTATION |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Pure regulatory information. |
| **Common wrong decision** | ACCEPT как внедрение маркировки |
| **Why wrong fails** | Нет заказа внедрения. |

### REJ-07 — «купить лицензию 1с предприятие 8»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь хочет купить лицензию 1С:Предприятие 8. |
| **Signals** | PRODUCT:EXPLICIT:купить лицензию; PRODUCT:STRONG:1с предприятие |
| **Primary intent** | BUY_PRODUCT_OR_MODULE |
| **Competing intent** | REQUEST_IMPLEMENTATION |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Product purchase dominant. |
| **Common wrong decision** | ACCEPT как внедрение |
| **Why wrong fails** | Купить лицензию — product. |

### REJ-08 — «документация api rest 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь ищет документацию по REST API 1С. |
| **Signals** | DOCUMENTATION:EXPLICIT:документация; TECHNICAL:MEDIUM:api rest |
| **Primary intent** | DOCUMENTATION_LOOKUP |
| **Competing intent** | INFORMATIONAL |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Documentation lookup. |
| **Common wrong decision** | ACCEPT как интеграция услуга |
| **Why wrong fails** | API docs — self-serve. |

### REJ-09 — «резюме программист 1с опыт 5 лет»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь ищет/размещает резюме программиста 1С. |
| **Signals** | CAREER:EXPLICIT:резюме; ROLE:MEDIUM:программист 1с |
| **Primary intent** | CAREER_EMPLOYMENT |
| **Competing intent** | HIRE_SERVICE |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Resume — job seeker stratum. |
| **Common wrong decision** | ABSTAIN |
| **Why wrong fails** | Резюме explicit. |

### REJ-10 — «обучение администратору 1с онлайн»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь ищет онлайн-обучение администратора 1С. |
| **Signals** | EDUCATION:EXPLICIT:обучение |
| **Primary intent** | EDUCATIONAL |
| **Competing intent** | HIRE_SERVICE |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Education dominant. |
| **Common wrong decision** | ACCEPT если оператор продаёт курсы |
| **Why wrong fails** | Service core ≠ course sales unless charter says otherwise. |

### REJ-11 — «сравнить crm битрикс и amo»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь хочет сравнить CRM Битрикс и amoCRM. |
| **Signals** | INFORMATIONAL:STRONG:сравнить; PRODUCT:MEDIUM:crm |
| **Primary intent** | INFORMATIONAL |
| **Competing intent** | BUY_PRODUCT_OR_MODULE |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Software comparison research. |
| **Common wrong decision** | ACCEPT как внедрение |
| **Why wrong fails** | Сравнение ≠ заказ услуги. |

### REJ-12 — «шаблон договора внедрения erp скачать»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь хочет скачать шаблон договора на внедрение ERP. |
| **Signals** | DOWNLOAD:EXPLICIT:скачать; TEMPLATE:STRONG:шаблон |
| **Primary intent** | DOWNLOAD_RESOURCE |
| **Competing intent** | REQUEST_QUOTE |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Template download. |
| **Common wrong decision** | ACCEPT из-за слова внедрения |
| **Why wrong fails** | Шаблон — resource, не hire. |

### REJ-13 — «зарплата 1с программист москва»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь интересуется зарплатой программиста 1С в Москве. |
| **Signals** | CAREER:EXPLICIT:зарплата; ROLE:MEDIUM:программист |
| **Primary intent** | CAREER_EMPLOYMENT |
| **Competing intent** | INFORMATIONAL |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Salary research — career. |
| **Common wrong decision** | INFORMATIONAL ACCEPT |
| **Why wrong fails** | Зарплата — career stratum. |

### REJ-14 — «инструкция печатная форма 1с своими руками»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь ищет инструкцию для самостоятельного создания печатной формы 1С. |
| **Signals** | DIY:EXPLICIT:своими руками; DOCUMENTATION:STRONG:инструкция |
| **Primary intent** | DIY_HOW_TO |
| **Competing intent** | REQUEST_MODIFICATION |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | DIY instruction. |
| **Common wrong decision** | ABSTAIN |
| **Why wrong fails** | Своими руками — clear DIY. |

### REJ-15 — «официальный сайт 1с скачать обновление»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь ищет официальный сайт 1С для скачивания обновления. |
| **Signals** | NAVIGATION:EXPLICIT:официальный сайт; DOWNLOAD:MEDIUM:скачать обновление |
| **Primary intent** | NAVIGATIONAL |
| **Competing intent** | DOWNLOAD_RESOURCE |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Nav + vendor download. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Not service hire. |

### REJ-16 — «экзамен 1с профессионал подготовка»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь готовится к экзамену 1С:Профессионал. |
| **Signals** | EDUCATION:EXPLICIT:экзамен; EDUCATION:MEDIUM:подготовка |
| **Primary intent** | EDUCATIONAL |
| **Competing intent** | REGULATORY |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Certification prep. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Education protected. |

### REJ-17 — «бесплатные курсы erp»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь ищет бесплатные курсы по ERP. |
| **Signals** | EDUCATION:EXPLICIT:курсы; FREE:EXPLICIT:бесплатные |
| **Primary intent** | EDUCATIONAL |
| **Competing intent** | INFORMATIONAL |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Free courses. |
| **Common wrong decision** | ABSTAIN |
| **Why wrong fails** | Clear education. |

### REJ-18 — «постановление правительства маркировка текст»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь ищет текст постановления правительства о маркировке. |
| **Signals** | REGULATORY:EXPLICIT:постановление; REGULATORY:STRONG:текст |
| **Primary intent** | REGULATORY |
| **Competing intent** | DOCUMENTATION_LOOKUP |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Legal text lookup. |
| **Common wrong decision** | ABSTAIN |
| **Why wrong fails** | Regulatory REJECT clear. |

### REJ-19 — «найти сотрудника 1с в штат вакансия»

| Field | Value |
|-------|-------|
| **Literal meaning** | Работодатель ищет сотрудника 1С в штат (вакансия). |
| **Signals** | CAREER:EXPLICIT:вакансия; EMPLOYER_HIRE:MEDIUM:сотрудника в штат |
| **Primary intent** | CAREER_EMPLOYMENT |
| **Competing intent** | HIRE_SERVICE |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Employee hiring ≠ customer seeking contractor. |
| **Common wrong decision** | ACCEPT как hire service |
| **Why wrong fails** | B2B employer hire — not service buyer. |

### REJ-20 — «пример кода обработки 1с github»

| Field | Value |
|-------|-------|
| **Literal meaning** | Пользователь ищет пример кода обработки 1С на GitHub. |
| **Signals** | DIY:STRONG:пример кода; DOWNLOAD:MEDIUM:github |
| **Primary intent** | DIY_HOW_TO |
| **Competing intent** | DOCUMENTATION_LOOKUP |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Code sample self-serve. |
| **Common wrong decision** | ACCEPT как доработка |
| **Why wrong fails** | Пример кода — not paid request. |

### PRB-05 — «ошибка обмена 1с как исправить»

| Field | Value |
|-------|-------|
| **Literal meaning** | Как исправить ошибку обмена 1С. |
| **Signals** | PROBLEM:MEDIUM:ошибка; DIY:EXPLICIT:как исправить |
| **Primary intent** | DIY_HOW_TO |
| **Competing intent** | PROBLEM_UNRESOLVED |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Explicit how-to. |
| **Common wrong decision** | ABSTAIN |
| **Why wrong fails** | DIY explicit — REJECT. |

### PVS-06 — «сравнить цены на erp системы»

| Field | Value |
|-------|-------|
| **Literal meaning** | Сравнить цены на ERP-системы. |
| **Signals** | INFORMATIONAL:STRONG:сравнить; PRODUCT:MEDIUM:erp |
| **Primary intent** | INFORMATIONAL |
| **Competing intent** | BUY_PRODUCT_OR_MODULE |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Product comparison. |
| **Common wrong decision** | ABSTAIN |
| **Why wrong fails** | Clear REJECT. |

### PVS-07 — «демо версия crm скачать»

| Field | Value |
|-------|-------|
| **Literal meaning** | Скачать демо-версию CRM. |
| **Signals** | DOWNLOAD:EXPLICIT:скачать; PRODUCT:STRONG:демо версия |
| **Primary intent** | DOWNLOAD_RESOURCE |
| **Competing intent** | BUY_PRODUCT_OR_MODULE |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Demo download. |
| **Common wrong decision** | ABSTAIN |
| **Why wrong fails** | Clear product. |

### CVP-01 — «работа программистом 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Работа программистом 1С. |
| **Signals** | CAREER:EXPLICIT:работа; ROLE:MEDIUM:программистом |
| **Primary intent** | CAREER_EMPLOYMENT |
| **Competing intent** | HIRE_SERVICE |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Job seeker. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Career not customer. |

### CVP-02 — «найти программиста 1с в штат»

| Field | Value |
|-------|-------|
| **Literal meaning** | Найти программиста 1С в штат. |
| **Signals** | EMPLOYER_HIRE:EXPLICIT:в штат; CAREER:STRONG:программиста |
| **Primary intent** | CAREER_EMPLOYMENT |
| **Competing intent** | HIRE_SERVICE |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Employer hiring. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Not service buyer. |

### CVP-07 — «стажировка 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Стажировка по 1С. |
| **Signals** | CAREER:EXPLICIT:стажировка |
| **Primary intent** | CAREER_EMPLOYMENT |
| **Competing intent** | EDUCATIONAL |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Internship. |
| **Common wrong decision** | ABSTAIN |
| **Why wrong fails** | Career clear. |

### CVP-08 — «обязанности администратора 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Обязанности администратора 1С. |
| **Signals** | CAREER:MEDIUM:обязанности; EDUCATION:WEAK:implicit |
| **Primary intent** | CAREER_EMPLOYMENT |
| **Competing intent** | INFORMATIONAL |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Job duties research. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Career/info. |

### CVP-10 — «без опыта 1с работа»

| Field | Value |
|-------|-------|
| **Literal meaning** | Работа по 1С без опыта. |
| **Signals** | CAREER:EXPLICIT:без опыта; CAREER:EXPLICIT:работа |
| **Primary intent** | CAREER_EMPLOYMENT |
| **Competing intent** | EDUCATIONAL |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Entry-level job. |
| **Common wrong decision** | ABSTAIN |
| **Why wrong fails** | Explicit career. |

### CNT-02 — «курсы 1с для бухгалтеров цена»

| Field | Value |
|-------|-------|
| **Literal meaning** | Цена курсов 1С для бухгалтеров. |
| **Signals** | EDUCATION:STRONG:курсы; COMMERCIAL_PRICE:MEDIUM:цена |
| **Primary intent** | EDUCATIONAL |
| **Competing intent** | REQUEST_QUOTE |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Wrong ACCEPT due to цена. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Education dominates. |

### CNT-04 — «внедрение erp что это»

| Field | Value |
|-------|-------|
| **Literal meaning** | Что такое внедрение ERP. |
| **Signals** | EDUCATION:MEDIUM:что это; IMPLEMENTATION:WEAK:внедрение |
| **Primary intent** | INFORMATIONAL |
| **Competing intent** | EDUCATIONAL |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Wrong ABSTAIN/ACCEPT — definitional. |
| **Common wrong decision** | ABSTAIN |
| **Why wrong fails** | Clear informational. |

### CNT-05 — «1с вакансия москва»

| Field | Value |
|-------|-------|
| **Literal meaning** | Вакансия 1С Москва. |
| **Signals** | CAREER:EXPLICIT:вакансия; GEO:MEDIUM:москва |
| **Primary intent** | CAREER_EMPLOYMENT |
| **Competing intent** | HIRE_SERVICE |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Wrong ABSTAIN. |
| **Common wrong decision** | ABSTAIN |
| **Why wrong fails** | Career explicit. |

### CNT-06 — «техподдержка 1с бесплатно»

| Field | Value |
|-------|-------|
| **Literal meaning** | Бесплатная техподдержка 1С. |
| **Signals** | SUPPORT:MEDIUM:техподдержка; FREE:EXPLICIT:бесплатно |
| **Primary intent** | INFORMATIONAL |
| **Competing intent** | REQUEST_SUPPORT |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Wrong ACCEPT. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Free — not paid core. |

---

## Clear ABSTAIN examples (minimum 20)

*Count in this section: 48*

### ABS-01 — «1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Упоминание 1С без дополнительного контекста. |
| **Signals** | TOPIC:WEAK:1с |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | HIRE_SERVICE |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | SHORT_HEAD_TERM CRITICAL; нет task или hire маркеров. |
| **Common wrong decision** | ACCEPT по теме |
| **Why wrong fails** | Topic ≠ commercial. |

### ABS-02 — «программист 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Упоминание роли программист 1С. |
| **Signals** | ROLE:MEDIUM:программист 1с; CAREER:MEDIUM:role |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | CAREER_EMPLOYMENT |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | CAREER_VS_PROVIDER unresolved. |
| **Common wrong decision** | REJECT career |
| **Why wrong fails** | Может быть поиск подрядчика. |

### ABS-03 — «сопровождение 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Упоминание сопровождения 1С. |
| **Signals** | SUPPORT:MEDIUM:сопровождение; TOPIC:MEDIUM:1с |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | REQUEST_SUPPORT |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | Short head service noun без hire evidence. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Service noun ≠ ACCEPT. |

### ABS-04 — «1с не работает»

| Field | Value |
|-------|-------|
| **Literal meaning** | 1С не функционирует. |
| **Signals** | PROBLEM:STRONG:не работает; TOPIC:MEDIUM:1с |
| **Primary intent** | PROBLEM_UNRESOLVED |
| **Competing intent** | REQUEST_SUPPORT |
| **Eligibility** | **ABSTAIN** |
| **Risk** | MEDIUM |
| **Reason** | Problem without provider/DIY resolution. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Problem ≠ auto provider. |

### ABS-05 — «настроить обмен 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Настроить обмен в 1С. |
| **Signals** | CONFIGURATION:MEDIUM:настроить; DIY:MEDIUM:implicit |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | REQUEST_CONFIGURATION |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | PROVIDER_VS_DIY unresolved. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Настроить без заказать — ambiguous. |

### ABS-06 — «маркировка 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Маркировка в контексте 1С. |
| **Signals** | REGULATORY:MEDIUM:маркировка; TOPIC:MEDIUM:1с |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | REGULATORY |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | Regulatory vs implementation unclear. |
| **Common wrong decision** | REJECT regulatory |
| **Why wrong fails** | Может быть заказ внедрения. |

### ABS-07 — «печатная форма 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Печатная форма в 1С. |
| **Signals** | MODIFICATION:MEDIUM:печатная форма; TOPIC:MEDIUM:1с |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | REQUEST_MODIFICATION |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | Short head task noun. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Нет подрядчика/заказать. |

### ABS-08 — «обмен 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Обмен в 1С. |
| **Signals** | TOPIC:MEDIUM:обмен; CONFIGURATION:WEAK:implicit |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | REQUEST_CONFIGURATION |
| **Eligibility** | **ABSTAIN** |
| **Risk** | CRITICAL |
| **Reason** | 1–2 token head. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Frequency не доказательство. |

### ABS-09 — «crm внедрение»

| Field | Value |
|-------|-------|
| **Literal meaning** | Внедрение CRM. |
| **Signals** | IMPLEMENTATION:MEDIUM:внедрение; TOPIC:MEDIUM:crm |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | REQUEST_IMPLEMENTATION |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | Нет hire/под ключ/заказать. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Внедрение alone — ABSTAIN. |

### ABS-10 — «erp для производства»

| Field | Value |
|-------|-------|
| **Literal meaning** | ERP для производства. |
| **Signals** | TOPIC:STRONG:erp; INFORMATIONAL:MEDIUM:для производства |
| **Primary intent** | INFORMATIONAL |
| **Competing intent** | BUY_PRODUCT_OR_MODULE |
| **Eligibility** | **ABSTAIN** |
| **Risk** | MEDIUM |
| **Reason** | Product research vs implementation. |
| **Common wrong decision** | REJECT |
| **Why wrong fails** | Может быть selection phase. |

### ABS-11 — «интеграция 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Интеграция 1С. |
| **Signals** | INTEGRATION:MEDIUM:интеграция; TOPIC:MEDIUM:1с |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | REQUEST_INTEGRATION |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | Short head integration. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Need scope and hire. |

### ABS-12 — «доработка 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Доработка 1С. |
| **Signals** | MODIFICATION:MEDIUM:доработка |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | REQUEST_MODIFICATION |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | Task noun without provider. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Доработка — not auto commercial. |

### ABS-13 — «стоимость внедрения crm»

| Field | Value |
|-------|-------|
| **Literal meaning** | Стоимость внедрения CRM. |
| **Signals** | COMMERCIAL_PRICE:MEDIUM:стоимость; IMPLEMENTATION:MEDIUM:внедрения |
| **Primary intent** | INFORMATIONAL |
| **Competing intent** | REQUEST_QUOTE |
| **Eligibility** | **ABSTAIN** |
| **Risk** | MEDIUM |
| **Reason** | SUPPORT_VS_INFORMATION vs quote. |
| **Common wrong decision** | REJECT |
| **Why wrong fails** | Может предшествовать hire. |

### ABS-14 — «ошибка обмена 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Ошибка обмена в 1С. |
| **Signals** | PROBLEM:STRONG:ошибка обмена |
| **Primary intent** | PROBLEM_UNRESOLVED |
| **Competing intent** | DIY_HOW_TO |
| **Eligibility** | **ABSTAIN** |
| **Risk** | MEDIUM |
| **Reason** | Problem triage unresolved. |
| **Common wrong decision** | REJECT DIY |
| **Why wrong fails** | DIY not proven. |

### ABS-15 — «купить и настроить 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Купить и настроить 1С. |
| **Signals** | PRODUCT:STRONG:купить; CONFIGURATION:MEDIUM:настроить |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | BUY_PRODUCT_OR_MODULE |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | PRODUCT_VS_SERVICE. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Product+config tied. |

### ABS-16 — «1с специалист москва»

| Field | Value |
|-------|-------|
| **Literal meaning** | Специалист 1С в Москве. |
| **Signals** | ROLE:MEDIUM:специалист; GEO:MEDIUM:москва |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | HIRE_SERVICE |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | Career vs provider + geo. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Специалист ambiguous. |

### ABS-17 — «техподдержка 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Техподдержка 1С. |
| **Signals** | SUPPORT:MEDIUM:техподдержка |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | REQUEST_SUPPORT |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | Vendor ITS vs paid support unclear. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Short head support. |

### ABS-18 — «модуль обмена 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Модуль обмена 1С. |
| **Signals** | PRODUCT:MEDIUM:модуль; TOPIC:MEDIUM:обмен |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | BUY_PRODUCT_OR_MODULE |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | Product module vs integration service. |
| **Common wrong decision** | REJECT product |
| **Why wrong fails** | May want install service. |

### ABS-19 — «1с итс продлить подписку»

| Field | Value |
|-------|-------|
| **Literal meaning** | Продлить подписку 1С:ИТС. |
| **Signals** | NAVIGATION:MEDIUM:итс; COMMERCIAL:MEDIUM:продлить |
| **Primary intent** | LOGIN_ACCOUNT_ACCESS |
| **Competing intent** | REQUEST_SUPPORT |
| **Eligibility** | **ABSTAIN** |
| **Risk** | MEDIUM |
| **Reason** | Nav/subscription vs paid support. |
| **Common wrong decision** | REJECT nav |
| **Why wrong fails** | Продление — vendor relationship. |

### ABS-20 — «битрикс интеграция»

| Field | Value |
|-------|-------|
| **Literal meaning** | Интеграция Битрикс. |
| **Signals** | INTEGRATION:MEDIUM:интеграция; TOPIC:MEDIUM:битрикс |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | REQUEST_INTEGRATION |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | Short head; scope missing. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Need partner hire signals. |

### PRB-01 — «не проводится документ 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Документ в 1С не проводится. |
| **Signals** | PROBLEM:STRONG:не проводится документ |
| **Primary intent** | PROBLEM_UNRESOLVED |
| **Competing intent** | DIY_HOW_TO |
| **Eligibility** | **ABSTAIN** |
| **Risk** | MEDIUM |
| **Reason** | Problem triage. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | No provider signal. |

### PRB-02 — «касса не подключается к 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Касса не подключается к 1С. |
| **Signals** | PROBLEM:STRONG:не подключается |
| **Primary intent** | PROBLEM_UNRESOLVED |
| **Competing intent** | REQUEST_CONFIGURATION |
| **Eligibility** | **ABSTAIN** |
| **Risk** | MEDIUM |
| **Reason** | Problem only. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Ambiguous fix path. |

### PRB-03 — «ошибка синхронизации crm»

| Field | Value |
|-------|-------|
| **Literal meaning** | Ошибка синхронизации CRM. |
| **Signals** | PROBLEM:STRONG:ошибка синхронизации |
| **Primary intent** | PROBLEM_UNRESOLVED |
| **Competing intent** | REQUEST_INTEGRATION |
| **Eligibility** | **ABSTAIN** |
| **Risk** | MEDIUM |
| **Reason** | Insufficient path. |
| **Common wrong decision** | REJECT |
| **Why wrong fails** | Not proven DIY. |

### PRB-04 — «маркировка не передаётся в честный знак»

| Field | Value |
|-------|-------|
| **Literal meaning** | Маркировка не передаётся в Честный ЗНАК. |
| **Signals** | PROBLEM:STRONG:не передаётся; REGULATORY:MEDIUM:маркировка |
| **Primary intent** | PROBLEM_UNRESOLVED |
| **Competing intent** | REGULATORY |
| **Eligibility** | **ABSTAIN** |
| **Risk** | MEDIUM |
| **Reason** | Problem + regulatory. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | No hire verb. |

### PRB-06 — «база 1с повреждена восстановить срочно»

| Field | Value |
|-------|-------|
| **Literal meaning** | База 1С повреждена, нужно срочно восстановить. |
| **Signals** | PROBLEM:STRONG:повреждена; RECOVERY:STRONG:восстановить; URGENCY:MEDIUM:срочно |
| **Primary intent** | REQUEST_RECOVERY |
| **Competing intent** | PROBLEM_UNRESOLVED |
| **Eligibility** | **ABSTAIN** |
| **Risk** | MEDIUM |
| **Reason** | Recovery likely but no explicit specialist. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Conservative without специалист. |

### PRB-07 — «не печатает чек из 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Из 1С не печатается чек. |
| **Signals** | PROBLEM:STRONG:не печатает чек |
| **Primary intent** | PROBLEM_UNRESOLVED |
| **Competing intent** | REQUEST_SUPPORT |
| **Eligibility** | **ABSTAIN** |
| **Risk** | MEDIUM |
| **Reason** | Hardware/driver vs 1C config. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Problem only. |

### PRB-08 — «зависает 1с при проведении»

| Field | Value |
|-------|-------|
| **Literal meaning** | 1С зависает при проведении. |
| **Signals** | PROBLEM:STRONG:зависает |
| **Primary intent** | PROBLEM_UNRESOLVED |
| **Competing intent** | REQUEST_SUPPORT |
| **Eligibility** | **ABSTAIN** |
| **Risk** | MEDIUM |
| **Reason** | Triage needed. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | No provider. |

### PRB-09 — «сбой обновления 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Сбой при обновлении 1С. |
| **Signals** | PROBLEM:STRONG:сбой обновления |
| **Primary intent** | PROBLEM_UNRESOLVED |
| **Competing intent** | DIY_HOW_TO |
| **Eligibility** | **ABSTAIN** |
| **Risk** | MEDIUM |
| **Reason** | DIY update vs support. |
| **Common wrong decision** | REJECT |
| **Why wrong fails** | Not clear DIY. |

### PRB-10 — «не формируется отчёт 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Отчёт в 1С не формируется. |
| **Signals** | PROBLEM:STRONG:не формируется отчёт |
| **Primary intent** | PROBLEM_UNRESOLVED |
| **Competing intent** | REQUEST_MODIFICATION |
| **Eligibility** | **ABSTAIN** |
| **Risk** | MEDIUM |
| **Reason** | Config vs custom report. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Ambiguous. |

### CVP-04 — «программист 1с услуги»

| Field | Value |
|-------|-------|
| **Literal meaning** | Услуги программиста 1С. |
| **Signals** | ROLE:MEDIUM:программист; SUPPORT:WEAK:услуги |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | HIRE_SERVICE |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | Still short; услуги weak. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Weak evidence. |

### CVP-05 — «1с разработчик удалённо»

| Field | Value |
|-------|-------|
| **Literal meaning** | 1С разработчик удалённо. |
| **Signals** | ROLE:MEDIUM:разработчик; CAREER:MEDIUM:удалённо |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | CAREER_EMPLOYMENT |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | Job vs freelance unclear. |
| **Common wrong decision** | REJECT |
| **Why wrong fails** | Not clear career. |

### CVP-09 — «требования к специалисту 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Требования к специалисту 1С. |
| **Signals** | CAREER:MEDIUM:требования; ROLE:MEDIUM:специалисту |
| **Primary intent** | CAREER_EMPLOYMENT |
| **Competing intent** | HIRE_SERVICE |
| **Eligibility** | **ABSTAIN** |
| **Risk** | MEDIUM |
| **Reason** | Job req vs hiring contractor. |
| **Common wrong decision** | REJECT |
| **Why wrong fails** | Could be employer. |

### SH-01 — «crm»

| Field | Value |
|-------|-------|
| **Literal meaning** | CRM. |
| **Signals** | TOPIC:WEAK:crm |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | REQUEST_IMPLEMENTATION |
| **Eligibility** | **ABSTAIN** |
| **Risk** | CRITICAL |
| **Reason** | Single token. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Head term. |

### SH-02 — «erp»

| Field | Value |
|-------|-------|
| **Literal meaning** | ERP. |
| **Signals** | TOPIC:WEAK:erp |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | BUY_PRODUCT_OR_MODULE |
| **Eligibility** | **ABSTAIN** |
| **Risk** | CRITICAL |
| **Reason** | Single token. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Head term. |

### SH-03 — «битрикс»

| Field | Value |
|-------|-------|
| **Literal meaning** | Битрикс. |
| **Signals** | TOPIC:WEAK:битрикс |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | NAVIGATIONAL |
| **Eligibility** | **ABSTAIN** |
| **Risk** | CRITICAL |
| **Reason** | Brand head. |
| **Common wrong decision** | REJECT nav only |
| **Why wrong fails** | Too short. |

### SH-04 — «1с erp»

| Field | Value |
|-------|-------|
| **Literal meaning** | 1С ERP. |
| **Signals** | TOPIC:MEDIUM:1с erp |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | BUY_PRODUCT_OR_MODULE |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | Product line name. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | No verb. |

### SH-05 — «интеграция»

| Field | Value |
|-------|-------|
| **Literal meaning** | Интеграция. |
| **Signals** | INTEGRATION:WEAK:интеграция |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | REQUEST_INTEGRATION |
| **Eligibility** | **ABSTAIN** |
| **Risk** | CRITICAL |
| **Reason** | Generic noun. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | No scope. |

### SH-06 — «ТС ПИОТ»

| Field | Value |
|-------|-------|
| **Literal meaning** | ТС ПИОТ. |
| **Signals** | REGULATORY:MEDIUM:ТС ПИОТ |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | REGULATORY |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | Regulatory acronym head. |
| **Common wrong decision** | REJECT |
| **Why wrong fails** | Ambiguous. |

### SH-07 — «внедрение»

| Field | Value |
|-------|-------|
| **Literal meaning** | Внедрение. |
| **Signals** | IMPLEMENTATION:WEAK:внедрение |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | REQUEST_IMPLEMENTATION |
| **Eligibility** | **ABSTAIN** |
| **Risk** | CRITICAL |
| **Reason** | Lonely service noun. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | No object. |

### SH-08 — «1с бухгалтерия»

| Field | Value |
|-------|-------|
| **Literal meaning** | 1С Бухгалтерия. |
| **Signals** | PRODUCT:MEDIUM:1с бухгалтерия |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | BUY_PRODUCT_OR_MODULE |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | Product name. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Product vs service. |

### SH-09 — «обновление 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Обновление 1С. |
| **Signals** | TOPIC:MEDIUM:обновление; DOWNLOAD:WEAK:implicit |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | DOWNLOAD_RESOURCE |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | Update vs support. |
| **Common wrong decision** | REJECT |
| **Why wrong fails** | Ambiguous. |

### SH-10 — «1с отчётность»

| Field | Value |
|-------|-------|
| **Literal meaning** | 1С отчётность. |
| **Signals** | TOPIC:MEDIUM:отчётность; REGULATORY:WEAK:implicit |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | REGULATORY |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | Reporting module/regulatory. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Short head. |

### CNT-01 — «сопровождение 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Сопровождение 1С. |
| **Signals** | SUPPORT:MEDIUM:сопровождение |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | REQUEST_SUPPORT |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | Wrong ACCEPT tempting due to catalogue match. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Service noun ≠ evidence. |

### CNT-03 — «заказать 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Заказать 1С. |
| **Signals** | PROVIDER_HIRE:EXPLICIT:заказать; PRODUCT:MEDIUM:1с |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | BUY_PRODUCT_OR_MODULE |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | Wrong ACCEPT — buy or service? |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | PRODUCT_VS_SERVICE. |

### CNT-07 — «настроить crm»

| Field | Value |
|-------|-------|
| **Literal meaning** | Настроить CRM. |
| **Signals** | CONFIGURATION:MEDIUM:настроить |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | DIY_HOW_TO |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | Wrong ACCEPT from verb. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | No hire. |

### CNT-08 — «стоимость сопровождения 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Стоимость сопровождения 1С. |
| **Signals** | COMMERCIAL_PRICE:MEDIUM:стоимость; SUPPORT:MEDIUM:сопровождение |
| **Primary intent** | INFORMATIONAL |
| **Competing intent** | REQUEST_QUOTE |
| **Eligibility** | **ABSTAIN** |
| **Risk** | MEDIUM |
| **Reason** | Wrong REJECT. |
| **Common wrong decision** | REJECT |
| **Why wrong fails** | May precede hire. |

### CNT-09 — «программист 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Программист 1С. |
| **Signals** | ROLE:MEDIUM:программист 1с |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | CAREER_EMPLOYMENT |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | Wrong REJECT as career only. |
| **Common wrong decision** | REJECT |
| **Why wrong fails** | Provider path possible. |

### CNT-10 — «монтаж сервера 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Монтаж сервера 1С. |
| **Signals** | MAINTENANCE:MEDIUM:монтаж; TOPIC:MEDIUM:сервер 1с |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | REQUEST_MAINTENANCE |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | Wrong ACCEPT from IT topic. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | No подрядчик/заказать. |

---

## Problem-query examples (minimum 10)

*Count in this section: 10*

### PRB-01 — «не проводится документ 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Документ в 1С не проводится. |
| **Signals** | PROBLEM:STRONG:не проводится документ |
| **Primary intent** | PROBLEM_UNRESOLVED |
| **Competing intent** | DIY_HOW_TO |
| **Eligibility** | **ABSTAIN** |
| **Risk** | MEDIUM |
| **Reason** | Problem triage. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | No provider signal. |

### PRB-02 — «касса не подключается к 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Касса не подключается к 1С. |
| **Signals** | PROBLEM:STRONG:не подключается |
| **Primary intent** | PROBLEM_UNRESOLVED |
| **Competing intent** | REQUEST_CONFIGURATION |
| **Eligibility** | **ABSTAIN** |
| **Risk** | MEDIUM |
| **Reason** | Problem only. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Ambiguous fix path. |

### PRB-03 — «ошибка синхронизации crm»

| Field | Value |
|-------|-------|
| **Literal meaning** | Ошибка синхронизации CRM. |
| **Signals** | PROBLEM:STRONG:ошибка синхронизации |
| **Primary intent** | PROBLEM_UNRESOLVED |
| **Competing intent** | REQUEST_INTEGRATION |
| **Eligibility** | **ABSTAIN** |
| **Risk** | MEDIUM |
| **Reason** | Insufficient path. |
| **Common wrong decision** | REJECT |
| **Why wrong fails** | Not proven DIY. |

### PRB-04 — «маркировка не передаётся в честный знак»

| Field | Value |
|-------|-------|
| **Literal meaning** | Маркировка не передаётся в Честный ЗНАК. |
| **Signals** | PROBLEM:STRONG:не передаётся; REGULATORY:MEDIUM:маркировка |
| **Primary intent** | PROBLEM_UNRESOLVED |
| **Competing intent** | REGULATORY |
| **Eligibility** | **ABSTAIN** |
| **Risk** | MEDIUM |
| **Reason** | Problem + regulatory. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | No hire verb. |

### PRB-05 — «ошибка обмена 1с как исправить»

| Field | Value |
|-------|-------|
| **Literal meaning** | Как исправить ошибку обмена 1С. |
| **Signals** | PROBLEM:MEDIUM:ошибка; DIY:EXPLICIT:как исправить |
| **Primary intent** | DIY_HOW_TO |
| **Competing intent** | PROBLEM_UNRESOLVED |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Explicit how-to. |
| **Common wrong decision** | ABSTAIN |
| **Why wrong fails** | DIY explicit — REJECT. |

### PRB-06 — «база 1с повреждена восстановить срочно»

| Field | Value |
|-------|-------|
| **Literal meaning** | База 1С повреждена, нужно срочно восстановить. |
| **Signals** | PROBLEM:STRONG:повреждена; RECOVERY:STRONG:восстановить; URGENCY:MEDIUM:срочно |
| **Primary intent** | REQUEST_RECOVERY |
| **Competing intent** | PROBLEM_UNRESOLVED |
| **Eligibility** | **ABSTAIN** |
| **Risk** | MEDIUM |
| **Reason** | Recovery likely but no explicit specialist. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Conservative without специалист. |

### PRB-07 — «не печатает чек из 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Из 1С не печатается чек. |
| **Signals** | PROBLEM:STRONG:не печатает чек |
| **Primary intent** | PROBLEM_UNRESOLVED |
| **Competing intent** | REQUEST_SUPPORT |
| **Eligibility** | **ABSTAIN** |
| **Risk** | MEDIUM |
| **Reason** | Hardware/driver vs 1C config. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Problem only. |

### PRB-08 — «зависает 1с при проведении»

| Field | Value |
|-------|-------|
| **Literal meaning** | 1С зависает при проведении. |
| **Signals** | PROBLEM:STRONG:зависает |
| **Primary intent** | PROBLEM_UNRESOLVED |
| **Competing intent** | REQUEST_SUPPORT |
| **Eligibility** | **ABSTAIN** |
| **Risk** | MEDIUM |
| **Reason** | Triage needed. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | No provider. |

### PRB-09 — «сбой обновления 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Сбой при обновлении 1С. |
| **Signals** | PROBLEM:STRONG:сбой обновления |
| **Primary intent** | PROBLEM_UNRESOLVED |
| **Competing intent** | DIY_HOW_TO |
| **Eligibility** | **ABSTAIN** |
| **Risk** | MEDIUM |
| **Reason** | DIY update vs support. |
| **Common wrong decision** | REJECT |
| **Why wrong fails** | Not clear DIY. |

### PRB-10 — «не формируется отчёт 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Отчёт в 1С не формируется. |
| **Signals** | PROBLEM:STRONG:не формируется отчёт |
| **Primary intent** | PROBLEM_UNRESOLVED |
| **Competing intent** | REQUEST_MODIFICATION |
| **Eligibility** | **ABSTAIN** |
| **Risk** | MEDIUM |
| **Reason** | Config vs custom report. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Ambiguous. |

---

## Product vs service examples (minimum 10)

*Count in this section: 10*

### PVS-01 — «установить и настроить crm под ключ»

| Field | Value |
|-------|-------|
| **Literal meaning** | Установить и настроить CRM под ключ. |
| **Signals** | IMPLEMENTATION:EXPLICIT:под ключ; PRODUCT:MEDIUM:установить |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | REQUEST_IMPLEMENTATION |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | PRODUCT_VS_SERVICE. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Install may be product+service. |

### PVS-02 — «лицензия 1с цена»

| Field | Value |
|-------|-------|
| **Literal meaning** | Цена лицензии 1С. |
| **Signals** | PRODUCT:MEDIUM:лицензия; COMMERCIAL_PRICE:MEDIUM:цена |
| **Primary intent** | INFORMATIONAL |
| **Competing intent** | BUY_PRODUCT_OR_MODULE |
| **Eligibility** | **ABSTAIN** |
| **Risk** | MEDIUM |
| **Reason** | Price research vs buy. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Not hire. |

### PVS-03 — «настроить купленную 1с заказать»

| Field | Value |
|-------|-------|
| **Literal meaning** | Заказать настройку уже купленной 1С. |
| **Signals** | CONFIGURATION:STRONG:настроить; PROVIDER_HIRE:EXPLICIT:заказать; PRODUCT:MEDIUM:купленную |
| **Primary intent** | REQUEST_CONFIGURATION |
| **Competing intent** | BUY_PRODUCT_OR_MODULE |
| **Eligibility** | **ACCEPT** |
| **Risk** | LOW |
| **Reason** | Service on owned product — ACCEPT. |
| **Common wrong decision** | REJECT product |
| **Why wrong fails** | Заказать настройку — service. |

### PVS-04 — «доработать купленный модуль 1с на заказ»

| Field | Value |
|-------|-------|
| **Literal meaning** | Доработать купленный модуль 1С на заказ. |
| **Signals** | MODIFICATION:STRONG:доработать; PROVIDER_HIRE:MEDIUM:на заказ |
| **Primary intent** | REQUEST_MODIFICATION |
| **Competing intent** | BUY_PRODUCT_OR_MODULE |
| **Eligibility** | **ACCEPT** |
| **Risk** | LOW |
| **Reason** | Modification service on owned module. |
| **Common wrong decision** | REJECT |
| **Why wrong fails** | На заказ — service. |

### PVS-05 — «купить и внедрить erp»

| Field | Value |
|-------|-------|
| **Literal meaning** | Купить и внедрить ERP. |
| **Signals** | PRODUCT:STRONG:купить; IMPLEMENTATION:STRONG:внедрить |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | REQUEST_IMPLEMENTATION |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | Bundled product+service. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Split unclear. |

### PVS-06 — «сравнить цены на erp системы»

| Field | Value |
|-------|-------|
| **Literal meaning** | Сравнить цены на ERP-системы. |
| **Signals** | INFORMATIONAL:STRONG:сравнить; PRODUCT:MEDIUM:erp |
| **Primary intent** | INFORMATIONAL |
| **Competing intent** | BUY_PRODUCT_OR_MODULE |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Product comparison. |
| **Common wrong decision** | ABSTAIN |
| **Why wrong fails** | Clear REJECT. |

### PVS-07 — «демо версия crm скачать»

| Field | Value |
|-------|-------|
| **Literal meaning** | Скачать демо-версию CRM. |
| **Signals** | DOWNLOAD:EXPLICIT:скачать; PRODUCT:STRONG:демо версия |
| **Primary intent** | DOWNLOAD_RESOURCE |
| **Competing intent** | BUY_PRODUCT_OR_MODULE |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Demo download. |
| **Common wrong decision** | ABSTAIN |
| **Why wrong fails** | Clear product. |

### PVS-08 — «внедрить купленную лицензию sap»

| Field | Value |
|-------|-------|
| **Literal meaning** | Внедрить купленную лицензию SAP. |
| **Signals** | IMPLEMENTATION:STRONG:внедрить; PRODUCT:MEDIUM:лицензию |
| **Primary intent** | REQUEST_IMPLEMENTATION |
| **Competing intent** | BUY_PRODUCT_OR_MODULE |
| **Eligibility** | **ABSTAIN** |
| **Risk** | MEDIUM |
| **Reason** | Implementation service likely but product owned. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | May need reviewer. |

### PVS-09 — «подключить модуль эдо 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Подключить модуль ЭДО в 1С. |
| **Signals** | CONFIGURATION:MEDIUM:подключить; PRODUCT:MEDIUM:модуль |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | REQUEST_INTEGRATION |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | Install module vs integration project. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Ambiguous. |

### PVS-10 — «аренда 1с в облаке»

| Field | Value |
|-------|-------|
| **Literal meaning** | Аренда 1С в облаке. |
| **Signals** | PRODUCT:MEDIUM:аренда; CLOUD:MEDIUM:облаке |
| **Primary intent** | BUY_PRODUCT_OR_MODULE |
| **Competing intent** | REQUEST_IMPLEMENTATION |
| **Eligibility** | **ABSTAIN** |
| **Risk** | MEDIUM |
| **Reason** | SaaS product vs hosted service. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Product/service blur. |

---

## Career vs provider examples (minimum 10)

*Count in this section: 11*

### CVP-01 — «работа программистом 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Работа программистом 1С. |
| **Signals** | CAREER:EXPLICIT:работа; ROLE:MEDIUM:программистом |
| **Primary intent** | CAREER_EMPLOYMENT |
| **Competing intent** | HIRE_SERVICE |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Job seeker. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Career not customer. |

### CVP-02 — «найти программиста 1с в штат»

| Field | Value |
|-------|-------|
| **Literal meaning** | Найти программиста 1С в штат. |
| **Signals** | EMPLOYER_HIRE:EXPLICIT:в штат; CAREER:STRONG:программиста |
| **Primary intent** | CAREER_EMPLOYMENT |
| **Competing intent** | HIRE_SERVICE |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Employer hiring. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Not service buyer. |

### CVP-03 — «нужен программист 1с на проект подряд»

| Field | Value |
|-------|-------|
| **Literal meaning** | Нужен программист 1С на проект по подряду. |
| **Signals** | PROVIDER_HIRE:EXPLICIT:подряд; ROLE:MEDIUM:программист |
| **Primary intent** | HIRE_SERVICE |
| **Competing intent** | CAREER_EMPLOYMENT |
| **Eligibility** | **ACCEPT** |
| **Risk** | MEDIUM |
| **Reason** | Подряд disambiguates contractor. |
| **Common wrong decision** | REJECT career |
| **Why wrong fails** | Подряд — provider. |

### CVP-04 — «программист 1с услуги»

| Field | Value |
|-------|-------|
| **Literal meaning** | Услуги программиста 1С. |
| **Signals** | ROLE:MEDIUM:программист; SUPPORT:WEAK:услуги |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | HIRE_SERVICE |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | Still short; услуги weak. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Weak evidence. |

### CVP-05 — «1с разработчик удалённо»

| Field | Value |
|-------|-------|
| **Literal meaning** | 1С разработчик удалённо. |
| **Signals** | ROLE:MEDIUM:разработчик; CAREER:MEDIUM:удалённо |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | CAREER_EMPLOYMENT |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | Job vs freelance unclear. |
| **Common wrong decision** | REJECT |
| **Why wrong fails** | Not clear career. |

### CVP-06 — «аутсорсинг программистов 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Аутсорсинг программистов 1С. |
| **Signals** | PROVIDER_HIRE:STRONG:аутсорсинг; ROLE:MEDIUM:программистов |
| **Primary intent** | HIRE_SERVICE |
| **Competing intent** | CAREER_EMPLOYMENT |
| **Eligibility** | **ACCEPT** |
| **Risk** | LOW |
| **Reason** | Outsourcing — B2B provider. |
| **Common wrong decision** | REJECT |
| **Why wrong fails** | Not job seeker. |

### CVP-07 — «стажировка 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Стажировка по 1С. |
| **Signals** | CAREER:EXPLICIT:стажировка |
| **Primary intent** | CAREER_EMPLOYMENT |
| **Competing intent** | EDUCATIONAL |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Internship. |
| **Common wrong decision** | ABSTAIN |
| **Why wrong fails** | Career clear. |

### CVP-08 — «обязанности администратора 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Обязанности администратора 1С. |
| **Signals** | CAREER:MEDIUM:обязанности; EDUCATION:WEAK:implicit |
| **Primary intent** | CAREER_EMPLOYMENT |
| **Competing intent** | INFORMATIONAL |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Job duties research. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Career/info. |

### CVP-09 — «требования к специалисту 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Требования к специалисту 1С. |
| **Signals** | CAREER:MEDIUM:требования; ROLE:MEDIUM:специалисту |
| **Primary intent** | CAREER_EMPLOYMENT |
| **Competing intent** | HIRE_SERVICE |
| **Eligibility** | **ABSTAIN** |
| **Risk** | MEDIUM |
| **Reason** | Job req vs hiring contractor. |
| **Common wrong decision** | REJECT |
| **Why wrong fails** | Could be employer. |

### CVP-10 — «без опыта 1с работа»

| Field | Value |
|-------|-------|
| **Literal meaning** | Работа по 1С без опыта. |
| **Signals** | CAREER:EXPLICIT:без опыта; CAREER:EXPLICIT:работа |
| **Primary intent** | CAREER_EMPLOYMENT |
| **Competing intent** | EDUCATIONAL |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Entry-level job. |
| **Common wrong decision** | ABSTAIN |
| **Why wrong fails** | Explicit career. |

### CNT-09 — «программист 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Программист 1С. |
| **Signals** | ROLE:MEDIUM:программист 1с |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | CAREER_EMPLOYMENT |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | Wrong REJECT as career only. |
| **Common wrong decision** | REJECT |
| **Why wrong fails** | Provider path possible. |

---

## Short head term examples (minimum 10)

*Count in this section: 10*

### SH-01 — «crm»

| Field | Value |
|-------|-------|
| **Literal meaning** | CRM. |
| **Signals** | TOPIC:WEAK:crm |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | REQUEST_IMPLEMENTATION |
| **Eligibility** | **ABSTAIN** |
| **Risk** | CRITICAL |
| **Reason** | Single token. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Head term. |

### SH-02 — «erp»

| Field | Value |
|-------|-------|
| **Literal meaning** | ERP. |
| **Signals** | TOPIC:WEAK:erp |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | BUY_PRODUCT_OR_MODULE |
| **Eligibility** | **ABSTAIN** |
| **Risk** | CRITICAL |
| **Reason** | Single token. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Head term. |

### SH-03 — «битрикс»

| Field | Value |
|-------|-------|
| **Literal meaning** | Битрикс. |
| **Signals** | TOPIC:WEAK:битрикс |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | NAVIGATIONAL |
| **Eligibility** | **ABSTAIN** |
| **Risk** | CRITICAL |
| **Reason** | Brand head. |
| **Common wrong decision** | REJECT nav only |
| **Why wrong fails** | Too short. |

### SH-04 — «1с erp»

| Field | Value |
|-------|-------|
| **Literal meaning** | 1С ERP. |
| **Signals** | TOPIC:MEDIUM:1с erp |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | BUY_PRODUCT_OR_MODULE |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | Product line name. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | No verb. |

### SH-05 — «интеграция»

| Field | Value |
|-------|-------|
| **Literal meaning** | Интеграция. |
| **Signals** | INTEGRATION:WEAK:интеграция |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | REQUEST_INTEGRATION |
| **Eligibility** | **ABSTAIN** |
| **Risk** | CRITICAL |
| **Reason** | Generic noun. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | No scope. |

### SH-06 — «ТС ПИОТ»

| Field | Value |
|-------|-------|
| **Literal meaning** | ТС ПИОТ. |
| **Signals** | REGULATORY:MEDIUM:ТС ПИОТ |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | REGULATORY |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | Regulatory acronym head. |
| **Common wrong decision** | REJECT |
| **Why wrong fails** | Ambiguous. |

### SH-07 — «внедрение»

| Field | Value |
|-------|-------|
| **Literal meaning** | Внедрение. |
| **Signals** | IMPLEMENTATION:WEAK:внедрение |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | REQUEST_IMPLEMENTATION |
| **Eligibility** | **ABSTAIN** |
| **Risk** | CRITICAL |
| **Reason** | Lonely service noun. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | No object. |

### SH-08 — «1с бухгалтерия»

| Field | Value |
|-------|-------|
| **Literal meaning** | 1С Бухгалтерия. |
| **Signals** | PRODUCT:MEDIUM:1с бухгалтерия |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | BUY_PRODUCT_OR_MODULE |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | Product name. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Product vs service. |

### SH-09 — «обновление 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Обновление 1С. |
| **Signals** | TOPIC:MEDIUM:обновление; DOWNLOAD:WEAK:implicit |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | DOWNLOAD_RESOURCE |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | Update vs support. |
| **Common wrong decision** | REJECT |
| **Why wrong fails** | Ambiguous. |

### SH-10 — «1с отчётность»

| Field | Value |
|-------|-------|
| **Literal meaning** | 1С отчётность. |
| **Signals** | TOPIC:MEDIUM:отчётность; REGULATORY:WEAK:implicit |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | REGULATORY |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | Reporting module/regulatory. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Short head. |

---

## Difficult counterexamples (minimum 10)

*Count in this section: 10*

### CNT-01 — «сопровождение 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Сопровождение 1С. |
| **Signals** | SUPPORT:MEDIUM:сопровождение |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | REQUEST_SUPPORT |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | Wrong ACCEPT tempting due to catalogue match. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Service noun ≠ evidence. |

### CNT-02 — «курсы 1с для бухгалтеров цена»

| Field | Value |
|-------|-------|
| **Literal meaning** | Цена курсов 1С для бухгалтеров. |
| **Signals** | EDUCATION:STRONG:курсы; COMMERCIAL_PRICE:MEDIUM:цена |
| **Primary intent** | EDUCATIONAL |
| **Competing intent** | REQUEST_QUOTE |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Wrong ACCEPT due to цена. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Education dominates. |

### CNT-03 — «заказать 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Заказать 1С. |
| **Signals** | PROVIDER_HIRE:EXPLICIT:заказать; PRODUCT:MEDIUM:1с |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | BUY_PRODUCT_OR_MODULE |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | Wrong ACCEPT — buy or service? |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | PRODUCT_VS_SERVICE. |

### CNT-04 — «внедрение erp что это»

| Field | Value |
|-------|-------|
| **Literal meaning** | Что такое внедрение ERP. |
| **Signals** | EDUCATION:MEDIUM:что это; IMPLEMENTATION:WEAK:внедрение |
| **Primary intent** | INFORMATIONAL |
| **Competing intent** | EDUCATIONAL |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Wrong ABSTAIN/ACCEPT — definitional. |
| **Common wrong decision** | ABSTAIN |
| **Why wrong fails** | Clear informational. |

### CNT-05 — «1с вакансия москва»

| Field | Value |
|-------|-------|
| **Literal meaning** | Вакансия 1С Москва. |
| **Signals** | CAREER:EXPLICIT:вакансия; GEO:MEDIUM:москва |
| **Primary intent** | CAREER_EMPLOYMENT |
| **Competing intent** | HIRE_SERVICE |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Wrong ABSTAIN. |
| **Common wrong decision** | ABSTAIN |
| **Why wrong fails** | Career explicit. |

### CNT-06 — «техподдержка 1с бесплатно»

| Field | Value |
|-------|-------|
| **Literal meaning** | Бесплатная техподдержка 1С. |
| **Signals** | SUPPORT:MEDIUM:техподдержка; FREE:EXPLICIT:бесплатно |
| **Primary intent** | INFORMATIONAL |
| **Competing intent** | REQUEST_SUPPORT |
| **Eligibility** | **REJECT** |
| **Risk** | LOW |
| **Reason** | Wrong ACCEPT. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | Free — not paid core. |

### CNT-07 — «настроить crm»

| Field | Value |
|-------|-------|
| **Literal meaning** | Настроить CRM. |
| **Signals** | CONFIGURATION:MEDIUM:настроить |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | DIY_HOW_TO |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | Wrong ACCEPT from verb. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | No hire. |

### CNT-08 — «стоимость сопровождения 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Стоимость сопровождения 1С. |
| **Signals** | COMMERCIAL_PRICE:MEDIUM:стоимость; SUPPORT:MEDIUM:сопровождение |
| **Primary intent** | INFORMATIONAL |
| **Competing intent** | REQUEST_QUOTE |
| **Eligibility** | **ABSTAIN** |
| **Risk** | MEDIUM |
| **Reason** | Wrong REJECT. |
| **Common wrong decision** | REJECT |
| **Why wrong fails** | May precede hire. |

### CNT-09 — «программист 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Программист 1С. |
| **Signals** | ROLE:MEDIUM:программист 1с |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | CAREER_EMPLOYMENT |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | Wrong REJECT as career only. |
| **Common wrong decision** | REJECT |
| **Why wrong fails** | Provider path possible. |

### CNT-10 — «монтаж сервера 1с»

| Field | Value |
|-------|-------|
| **Literal meaning** | Монтаж сервера 1С. |
| **Signals** | MAINTENANCE:MEDIUM:монтаж; TOPIC:MEDIUM:сервер 1с |
| **Primary intent** | AMBIGUOUS |
| **Competing intent** | REQUEST_MAINTENANCE |
| **Eligibility** | **ABSTAIN** |
| **Risk** | HIGH |
| **Reason** | Wrong ACCEPT from IT topic. |
| **Common wrong decision** | ACCEPT |
| **Why wrong fails** | No подрядчик/заказать. |

---

## Related documents

- [ORCA-SEMANTIC-ANNOTATION-GUIDELINE-v1.md](../guidelines/ORCA-SEMANTIC-ANNOTATION-GUIDELINE-v1.md)
- [ORCA-SEMANTIC-ANNOTATION-ANTI-PATTERNS-v1.md](ORCA-SEMANTIC-ANNOTATION-ANTI-PATTERNS-v1.md)
- [ORCA-SEMANTIC-ANNOTATION-DECISION-TREE-v1.md](../decision-trees/ORCA-SEMANTIC-ANNOTATION-DECISION-TREE-v1.md)

---

**Status:** PROPOSED — OPERATOR APPROVAL REQUIRED
