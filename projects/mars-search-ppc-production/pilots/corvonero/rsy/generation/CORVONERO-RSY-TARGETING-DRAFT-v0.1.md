# CORVONERO — РСЯ targeting draft v0.1

**Status:** DRAFT / NOT_A_DIRECT_SETTING  
**Recommended now:** cold RSY planning  
**Retargeting:** prepare separately when Metrica audiences/goals are confirmed — do not merge as final

Exact Direct Networks fields (interests, keywords, autotargeting, audience IDs, device toggles, placement categories) are **SAFE UNKNOWN / DIRECT_CONFIRMATION_REQUIRED** unless later cabinet-checked. This file is conceptual.

---

## Shared cold RSY audience (all groups)

Primary B2B:

- владельцы бизнеса / ИП
- директора
- главные бухгалтеры и бухгалтеры, работающие в 1С
- руководители операций / производства / розницы
- IT-ответственные
- пользователи 1С внутри компании (не соискатели)

Do not target as primary: соискатели, курсы, how-to без услуги, покупатели лицензий 1С, чужая вендорская поддержка.

Device mix from Search (not RSY proof): smartphones 4 conversions / 18 900 ₽ vs desktops 2 / 8 200 ₽. Device controls for the chosen RSY type: **SAFE UNKNOWN / DIRECT_CONFIRMATION_REQUIRED**.

---

## Geo logic (candidates only)

| Mode | Draft geo | Status |
|------|-----------|--------|
| LOCAL | Новосибирск / Новосибирская область candidate | OPEN / OC-07 |
| REMOTE | Россия candidate; исключение Новосибирска/области — candidate | OPEN / OC-08 |

Exact Direct geo trees are not claimed.

---

## Per-group targeting draft

| group_code | direction | mode | cold themes | geo draft | retargeting later | exact Direct fields |
| --- | --- | --- | --- | --- | --- | --- |
| 01-LOCAL-PROGRAMMIST-1S | Программист 1С | LOCAL | тематика «программист 1С», «специалист 1С», услуги 1С для бизнеса; интересы учёта/ERP на уровне концепции | Новосибирск / Новосибирская область candidate; exact geo OPEN | посетители LP-01; клики Search CA-01 — TO_CONFIRM / не смешивать с cold RSY сейчас | SAFE UNKNOWN / DIRECT_CONFIRMATION_REQUIRED |
| 02-LOCAL-SOPROVOZHDENIE-1S | Сопровождение 1С / техподдержка / ошибки 1С | LOCAL | тематика сопровождения 1С, техподдержки, ошибок 1С, обслуживания рабочей базы | Новосибирск / Новосибирская область candidate; exact geo OPEN | посетители LP-02; Search CA-02 converters — TO_CONFIRM | SAFE UNKNOWN / DIRECT_CONFIRMATION_REQUIRED |
| 03-LOCAL-DORABOTKA-1S | Доработка / разработка 1С | LOCAL | тематика доработки/разработки 1С, доработки типовой конфигурации как услуги | Новосибирск / Новосибирская область candidate; exact geo OPEN | посетители LP-03 — TO_CONFIRM; low Search proof | SAFE UNKNOWN / DIRECT_CONFIRMATION_REQUIRED |
| 04-LOCAL-INTEGRACII-1S | Интеграции 1С | LOCAL | тематика интеграций 1С, обмена, связи с сайтом/CRM как услуги, не how-to | Новосибирск / Новосибирская область candidate; exact geo OPEN | посетители LP-04 — TO_CONFIRM | SAFE UNKNOWN / DIRECT_CONFIRMATION_REQUIRED |
| 05-LOCAL-MARKIROVKA-CHESTNY-ZNAK | Маркировка / Честный знак | LOCAL | тематика маркировки, Честного знака, настройки 1С под маркировку как услуги | Новосибирск / Новосибирская область candidate; exact geo OPEN | посетители LP-05 — TO_CONFIRM | SAFE UNKNOWN / DIRECT_CONFIRMATION_REQUIRED |
| 01-REMOTE-PROGRAMMIST-1S | Программист 1С | REMOTE | тематика удалённого программиста 1С / специалиста 1С по России | Россия candidate; исключение Новосибирска/области — candidate, exact geo OPEN | посетители LP-01 из не-локальных сессий — SAFE UNKNOWN / TO_CONFIRM | SAFE UNKNOWN / DIRECT_CONFIRMATION_REQUIRED |
| 02-REMOTE-SOPROVOZHDENIE-1S | Сопровождение 1С / техподдержка / ошибки 1С | REMOTE | тематика удалённого сопровождения 1С, ошибок, техподдержки рабочей базы | Россия candidate; исключение Новосибирска/области — candidate, exact geo OPEN | посетители LP-02 — TO_CONFIRM | SAFE UNKNOWN / DIRECT_CONFIRMATION_REQUIRED |
| 03-REMOTE-DORABOTKA-1S | Доработка / разработка 1С | REMOTE | тематика удалённой доработки/разработки 1С как услуги | Россия candidate; исключение Новосибирска/области — candidate, exact geo OPEN | посетители LP-03 — TO_CONFIRM | SAFE UNKNOWN / DIRECT_CONFIRMATION_REQUIRED |
| 04-REMOTE-INTEGRACII-1S | Интеграции 1С | REMOTE | тематика интеграций 1С как услуги; избегать DIY «как интегрировать» | Россия candidate; исключение Новосибирска/области — candidate, exact geo OPEN | посетители LP-04 — TO_CONFIRM | SAFE UNKNOWN / DIRECT_CONFIRMATION_REQUIRED |
| 05-REMOTE-MARKIROVKA-CHESTNY-ZNAK | Маркировка / Честный знак | REMOTE | тематика удалённой настройки Честного знака / маркировки в 1С как услуги | Россия candidate; исключение Новосибирска/области — candidate, exact geo OPEN | посетители LP-05 — TO_CONFIRM | SAFE UNKNOWN / DIRECT_CONFIRMATION_REQUIRED |

---

## Possible RSY targeting concepts (not settings)

1. **Service-themed keywords/interests** — conceptual themes from Search seeds and landings. RSY will not reuse 926 Search keyword placements as bidding units.
2. **Landing/content themes** — LP-01…LP-05 page topics as relevance hints.
3. **Audience segments if Metrica exists** — site/landing visitors, goal audiences. IDs: **SAFE UNKNOWN**.
4. **Retargeting later** — form abandoners, Search clickers, converters. Separate confirmation (OC-R11). Not mixed into first cold plan as final.
5. **LOCAL geo logic** — city/region candidate + local message.
6. **REMOTE geo logic** — Russia candidate ± Novosibirsk exclusion + remote message.
7. **Device considerations if supported later** — smartphone-heavy Search signal is a hint only.
8. **Exclusion/caution notes** — see exclusions draft; do not blindly copy Search minus phrases.

---

## Cold vs retargeting

| Layer | This pack |
|-------|-----------|
| Cold RSY | **Recommended now** — 10 groups as planned |
| Warm / retargeting | Prepare separately; do not treat as ready |
| Search converters as RSY seed | TO_CONFIRM, not built |

Metrica goal names behind the 6 Search conversions remain **SAFE UNKNOWN**.
