# PARSER 3.3 REGRESSION FIXTURE CATALOG v1

**IMPLEMENTED — Phase 3E.1.** Executable catalog: [P33-FIXTURE-CATALOG-v1.md](../../implementation/parser-fixtures/P33-FIXTURE-CATALOG-v1.md). Все fixtures synthetic и используют reserved example values.

| ID | Класс | Ожидание |
|---|---|---|
| P33-01 | multiline canonical | поля и provenance корректны |
| P33-02 | collapsed line | те же semantics |
| P33-03 | reordered labels | порядок не меняет результат |
| P33-04 | site explicitly absent | `explicitly_absent` |
| P33-05 | messenger in site | `alternative_contact` |
| P33-06 | placeholder site/contact | `invalid_or_placeholder` |
| P33-07 | label words in comment | граница не обрезается |
| P33-08 | comment vs form title | comment wins; conflict stamped |
| P33-09 | structured vs selected service | structured wins по contract |
| P33-10 | page vs subject | page wins |
| P33-11 | missing all intent | Other/unknown, no invention |
| P33-12 | reply consistency | no unsupported facts |
| P33-13 | quoted history/signature | current form isolated |
| P33-14 | Unicode/NBSP/CRLF | normalized deterministically |
| P33-15 | backward v3.2 fixture set | no approved regression |

Acceptance: exact expected semantic JSON, zero PII, zero external calls, stable repeat run.