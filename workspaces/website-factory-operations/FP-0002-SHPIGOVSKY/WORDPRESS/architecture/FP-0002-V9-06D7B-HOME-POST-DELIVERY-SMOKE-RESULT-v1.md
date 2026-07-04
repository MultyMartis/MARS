# FP-0002 V9-06D7B Home Post-Delivery Smoke Result v1

**Date:** 2026-07-05

## Route smoke

| Route | URL | HTTP | Expected | Header | Footer | CSS | JS | Result |
|---|---|---:|---|---:|---:|---:|---:|---|
| Home | http://shpigovsky.test/ | 200 | page #4 | True | True | True | True | PASS |
| Services Hub | http://shpigovsky.test/uslugi/ | 200 | page #5 | True | True | True | True | PASS |
| Parent Service — Зависимости | http://shpigovsky.test/uslugi/zavisimosti/ | 200 | service #73 | True | True | True | True | PASS |
| Child Service — Алкоголь | http://shpigovsky.test/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/ | 200 | service #74 | True | True | True | True | PASS |
| Parent Service — Психическое здоровье | http://shpigovsky.test/uslugi/psihicheskoe-zdorovie/ | 200 | service #77 | True | True | True | True | PASS |
| Parent Service — РПП | http://shpigovsky.test/uslugi/rasstroystva-pischevogo-povedeniya/ | 200 | service #84 | True | True | True | True | PASS |
| Contacts | http://shpigovsky.test/kontakty/ | 200 | page #20 | True | True | True | True | PASS |

## Home section render smoke

| Section/check | Present | Expected if empty | Result |
|---|---:|---|---|
| front_page_orchestration | True | False | PASS |
| site-main--front | True | False | PASS |
| hero | True | False | PASS |
| feature-grid | False | True | PASS_OMITTED |
| treatment-prevention | True | False | PASS |
| rehabilitation-program | True | False | PASS |
| gallery | False | True | PASS_OMITTED |
| articles-teaser | False | True | PASS_OMITTED |
| faq | False | True | PASS_OMITTED |
| final-form | True | False | PASS |
| deferred_sections_documented | True | 12/20 V9 sections deferred per D7-B scope | PASS |

## Asset smoke

| Asset | Status |
|---|---|
| V9 CSS | PASS |
| V9 shell JS | PASS |
| Logo SVG | PASS |

## Visual smoke

Screenshots: PASS — 8 captured.

## Result

PASS
