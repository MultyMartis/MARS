# FP-0002 V9-06D7C Services Hub Post-Delivery Smoke Result v1

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

## Services Hub section render smoke

| Section/check | Present | Expected if empty | Result |
|---|---:|---|---|
| page-template orchestration | True | False | PASS |
| page-uslugi/root class | True | False | PASS |
| hero | True | False | PASS |
| service groups | True | False | PASS |
| parent service 73 | True | False | PASS |
| parent service 77 | True | False | PASS |
| parent service 84 | True | False | PASS |
| child service cards | True | False | PASS |
| rehabilitation-program | True | False | PASS |
| FAQ or omitted if empty | False | True | PASS_OMITTED |
| final-form | True | False | PASS |
| deferred sections documented | True | founder-quote, comfort, genotyping, category galleries deferred per D7-C scope | PASS |

## Home stability after D7-C

| Check | Present | Result |
|---|---:|---|
| site-main--front | True | PASS |
| hero--home | True | PASS |
| treatment-prevention | True | PASS |
| rehabilitation-program | True | PASS |
| final-form | True | PASS |

## Asset smoke

| Asset | Status |
|---|---|
| V9 CSS | PASS |
| V9 shell JS | PASS |
| Logo SVG | PASS |

## Service 74 regression

URL: http://shpigovsky.test/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/ — HTTP 200 — PASS

## Visual smoke

Screenshots: PASS — 8 captured.

## Result

PASS
