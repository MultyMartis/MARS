# CORVONERO — РСЯ exclusions candidates v0.2

**EXCLUSIONS_STATUS:** CANDIDATE_FOR_REVIEW / NOT_FINAL

RSY exclusions are **not** the same as Search minus phrases. Do not blindly copy Search negatives.

| ID | Theme | Candidate action | Source | Copy Search minus? | Status |
| --- | --- | --- | --- | --- | --- |
| EX-01 | Brand safety / identity | Не использовать чужие бренды, партнёрские знаки 1С, сертификаты, логотипы клиентов без подтверждения. | v1 architecture + claims register caution | NO — conceptual only | CANDIDATE_FOR_REVIEW / NOT_FINAL |
| EX-02 | Jobs / vacancies / резюме | Исключать вакансионный и соискательский intent из сообщений и, если Direct позволит, из тематик/площадок. Не делать креатив «ищем программиста / ищу работу». | Search negatives already exclude job-seeker intent; RSY messages must keep the same caution | REVIEW — do not blind-copy phrase list | CANDIDATE_FOR_REVIEW / NOT_FINAL |
| EX-03 | Education / courses / how-to / DIY | Не строить холодный РСЯ вокруг «как в 1С…», «как настроить честный знак», «как интегрировать». Это услуга, не обучение. | Search query export: how-to leakage, 0 conversions in converting-spend slice | REVIEW themes, not a dump of Search minus | CANDIDATE_FOR_REVIEW / NOT_FINAL |
| EX-04 | Free / download / crack / null | Держать вне сообщений и при возможности вне тематик: бесплатно, скачать, кряк, торрент, null. Не обещать бесплатный аудит. | B2B service caution; Search minus practice exists but not auto-imported here | REVIEW | CANDIDATE_FOR_REVIEW / NOT_FINAL |
| EX-05 | ITS / личный кабинет curiosity | Не делать холодный угол только про «ИТС 1С» / личный кабинет ИТС: в Search большой показ, почти без конверсий. | Query report: «1с итс» 1 215 показов / 1 клик; «итс 1с» 921 / 3 | NO — this is intent caution, not a ready minus list | CANDIDATE_FOR_REVIEW / NOT_FINAL |
| EX-06 | Third-party vendor support | Не целиться в чужую техподдержку вендоров (пример Search: Калуга Астрал). CorvoNero не подменяет вендора. | Search queries; v1 exclusions | REVIEW competitor/vendor names separately; legal caution | CANDIDATE_FOR_REVIEW / NOT_FINAL |
| EX-07 | Licensing / franchising / 1C as product | Не продавать лицензии 1С, франшизу, «официальный продукт 1С». Услуга специалиста/сопровождения. | v1 message map | REVIEW | CANDIDATE_FOR_REVIEW / NOT_FINAL |
| EX-08 | Adult / gambling / irrelevant placements | Если кабинет ЕПК/РСЯ даёт фильтры площадок/категорий — рассмотреть brand-safety ограничения. Точные Direct toggles: SAFE UNKNOWN / DIRECT_CONFIRMATION_REQUIRED. | Generic RSY brand-safety; not proven for this login | NO — Search minus ≠ RSY placement filters | CANDIDATE_FOR_REVIEW / NOT_FINAL |
| EX-09 | Weak-intent Search categories | Сопутствующие / альтернативные / широкие в Search: 171 клик, 0 ₽, 0 conv. Не копировать их как РСЯ-темы. Не слепо переносить все Search minus. | Search query categories in final stats | DO_NOT_BLIND_COPY | CANDIDATE_FOR_REVIEW / NOT_FINAL |
| EX-10 | LOCAL/REMOTE message bleed | LOCAL не обещает Россию без визита; REMOTE не обещает Новосибирск/выезд. Исключение — смешение оффера, не Help-бан. | v1.1 R-10 | NO | CANDIDATE_FOR_REVIEW / NOT_FINAL |
| EX-11 | Non-business consumer intent | Не целиться в бытовой/потребительский 1С-интерес (домашняя бухгалтерия, учёба «для себя», развлечения). Холодный РСЯ — B2B услуга для бизнеса. | v0.2 import-candidate charter / B2B tone | NO — thematic caution, not a Search minus dump | CANDIDATE_FOR_REVIEW / NOT_FINAL |

## What not to do

- Do not import Search Commander negatives wholesale into RSY.
- Do not globally exclude the word «программист».
- Do not broadly exclude marking codes / «Честный знак» as a category — the service is in-scope.
- Exact placement-category checkboxes in Direct remain **CHECK_REQUIRED**.

Operator review is required before any later import package v1.
