# FP-0002 V9-06D7A Post-Delivery Smoke Result v1

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
