# CORVONERO — РСЯ exclusions draft v0.1

**Status:** DRAFT_REVIEW_REQUIRED  
**Important:** RSY exclusions are **not** identical to Search minus phrases. Do not blindly copy the Search negative list into Networks.

Search still has **no deployable minus list** as a finished RSY artefact (`CORVONERO-EXT-W1-NEGATIVE-RISK-AUDIT-v1.md`: Deployable minus list = NO). This draft is thematic.

---

| ID | Theme | Draft action | Source | Copy Search minus? | Status |
| --- | --- | --- | --- | --- | --- |
| EX-01 | Brand safety / identity | Не использовать чужие бренды, партнёрские знаки 1С, сертификаты, логотипы клиентов без подтверждения. | v1 architecture + claims register caution | NO — conceptual only | DRAFT_REVIEW_REQUIRED |
| EX-02 | Jobs / vacancies / резюме | Исключать вакансионный и соискательский intent из сообщений и, если Direct позволит, из тематик/площадок. Не делать креатив «ищем программиста / ищу работу». | Search negatives already exclude job-seeker intent; RSY messages must keep the same caution | REVIEW — do not blind-copy phrase list | DRAFT_REVIEW_REQUIRED |
| EX-03 | Education / courses / how-to / DIY | Не строить холодный РСЯ вокруг «как в 1С…», «как настроить честный знак», «как интегрировать». Это услуга, не обучение. | Search query export: how-to leakage, 0 conversions in converting-spend slice | REVIEW themes, not a dump of Search minus | DRAFT_REVIEW_REQUIRED |
| EX-04 | Free / download / crack / null | Держать вне сообщений и при возможности вне тематик: бесплатно, скачать, кряк, торрент, null. Не обещать бесплатный аудит. | B2B service caution; Search minus practice exists but not auto-imported here | REVIEW | DRAFT_REVIEW_REQUIRED |
| EX-05 | ITS / личный кабинет curiosity | Не делать холодный угол только про «ИТС 1С» / личный кабинет ИТС: в Search большой показ, почти без конверсий. | Query report: «1с итс» 1 215 показов / 1 клик; «итс 1с» 921 / 3 | NO — this is intent caution, not a ready minus list | DRAFT_REVIEW_REQUIRED |
| EX-06 | Third-party vendor support | Не целиться в чужую техподдержку вендоров (пример Search: Калуга Астрал). CorvoNero не подменяет вендора. | Search queries; v1 exclusions | REVIEW competitor/vendor names separately; legal caution | DRAFT_REVIEW_REQUIRED |
| EX-07 | Licensing / franchising / 1C as product | Не продавать лицензии 1С, франшизу, «официальный продукт 1С». Услуга специалиста/сопровождения. | v1 message map | REVIEW | DRAFT_REVIEW_REQUIRED |
| EX-08 | Adult / gambling / irrelevant placements | Если кабинет ЕПК/РСЯ даёт фильтры площадок/категорий — рассмотреть brand-safety ограничения. Точные Direct toggles: SAFE UNKNOWN / DIRECT_CONFIRMATION_REQUIRED. | Generic RSY brand-safety; not proven for this login | NO — Search minus ≠ RSY placement filters | DRAFT_REVIEW_REQUIRED |
| EX-09 | Weak-intent Search categories | Сопутствующие / альтернативные / широкие в Search: 171 клик, 0 ₽, 0 conv. Не копировать их как РСЯ-темы. Не слепо переносить все Search minus. | Search query categories in final stats | DO_NOT_BLIND_COPY | DRAFT_REVIEW_REQUIRED |
| EX-10 | LOCAL/REMOTE message bleed | LOCAL не обещает Россию без визита; REMOTE не обещает Новосибирск/выезд. Исключение — смешение оффера, не Help-бан. | v1.1 R-10 | NO | DRAFT_REVIEW_REQUIRED |

---

## What not to do

- Do not import Search Commander negatives wholesale into RSY.
- Do not globally exclude the word «программист» (Search guard still relevant).
- Do not broadly exclude marking codes / «Честный знак» as a category — the service is in-scope.
- Do not treat ITS curiosity as a proven RSY theme, and do not treat it as a finished minus list either.
- Exact placement-category checkboxes in Direct remain **SAFE UNKNOWN / DIRECT_CONFIRMATION_REQUIRED**.

Operator review is required before any later import package.
