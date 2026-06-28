# CORVONERO Phase 6.2 — Маркировка / Честный знак Requirements v1

**Landing page ID:** LP-05  
**Campaign:** CA-05  
**Priority:** P1  
**Allocated phrases:** 220  
**Ad groups:** 5

## A. Commercial purpose

| Field | Value |
|-------|-------|
| Target service | Marking, Честный знак, TS ПИОТ in 1C |
| Primary audience | Retail/wholesale/manufacturing businesses subject to marking requirements |
| Primary conversion | Marking setup/support inquiry |
| Commercial objective | Capture marking and TS ПИОТ service demand distinct from generic 1C |

## B. Intent coverage

**Primary intents:** DIRECT_SERVICE_ORDER, MODIFICATION, IMPLEMENTATION, INTEGRATION, PROBLEM_RESOLUTION, PRICE_AND_COST

**Permitted secondary:** MODIFICATION, INTEGRATION, PROBLEM_RESOLUTION

**Prohibited:** CAREER_OR_EDUCATION, INFORMATIONAL, AMBIGUOUS

**Ambiguous excluded:** regulatory research-only queries, product catalog navigation

### Ad groups

- **ca-05-direct-service-order** (DIRECT_SERVICE_ORDER, 199 phrases): тестирование доработок 1с, продажа доработок 1с, маркировка в 1с
- **ca-05-integration** (INTEGRATION, 14 phrases): интеграция честного знака и сайта 1с битрикс, интеграция маркировки в 1с, интеграция маркировки товаров в 1с
- **ca-05-ts-piot** (DIRECT_SERVICE_ORDER, 4 phrases): тс пиот честный знак 1с, тс пиот честный знак 1с розница, настройка тс пиот в 1с ут 11.5
- **ca-05-support-and-maintenance** (SUPPORT_AND_MAINTENANCE, 2 phrases): поддержка 1с честный знак, техподдержка честный знак 1с
- **ca-05-specialist-search** (SPECIALIST_SEARCH, 1 phrases): как заказать коды маркировки в 1с

## C. Required content blocks

- first_screen_marking_proposition
- value_proposition_compliance_operations
- service_scope_chestny_znak_ts_piot_ut_retail
- problems_codes_exchange_errors
- marking_scenarios_industries
- process_audit_setup_test_support
- integration_with_operators
- configurations_ut_retail_erp
- pricing_approach_project_support
- trust_marking_experience
- faq_marking_deadlines
- cta_marking_consultation
- contact_block
- ts_piot_subsection

## D. Required message evidence

- **company_name_korvo_nero:** CONFIRMED
- **phone_383_390_29_28:** CONFIRMED
- **service_delivery_novosibirsk:** NEEDS_OPERATOR_CONFIRMATION
- **remote_service_russia:** NEEDS_CLIENT_CONFIRMATION
- **hourly_rates:** PROHIBITED_UNSUPPORTED
- **partner_1c_status:** NEEDS_CLIENT_CONFIRMATION
- **response_time_sla:** PROHIBITED_UNSUPPORTED
- **marking_competency:** NEEDS_CLIENT_CONFIRMATION
- **integration_systems_list:** NEEDS_CLIENT_CONFIRMATION
- **case_studies:** NEEDS_CLIENT_CONFIRMATION
- **nds_vat_included:** NEEDS_OPERATOR_CONFIRMATION

## E. Conversion requirements

- **Primary CTA:** Request service — service-specific label
- **Secondary CTA:** Phone +7 (383) 390-29-28
- **Form fields:** name, contact, task description; configuration optional
- **Response-time claims:** PROHIBITED_UNSUPPORTED unless confirmed
- **Analytics (later):** form_submit, phone_click, cta_click

## F. Search and advertising alignment

- Message match: first screen = Маркировка / Честный знак
- Risky wording: 100% compliance guarantee, официальный представитель ЧЗ без evidence
- Exclusions: see EXCLUSION-BOUNDARIES-v2

## G. Geography

- **Primary:** Новосибирск + Новосибирская область
- **Remote:** only if confirmed
- **Expansion cities:** not in initial LP

## H. SEO and technical (planning only)

- **Slug:** `markirovka-chestny-znak`
- **H1 direction:** Маркировка и Честный знак в 1С — настройка и сопровождение
- **Canonical:** self on dedicated URL
- **Mobile:** responsive, click-to-call
