# FP-0002 V9-06D7D Service Post-Delivery Smoke Result v1

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

## Service section render smoke

| Service | URL | Variant | Hero | Subnav | Children | Programme | FAQ | Final form | Result |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 73 | http://shpigovsky.test/uslugi/zavisimosti/ | subdivision | True | True | True | True | True | True | PASS |
| 74 | http://shpigovsky.test/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/ | leaf | True | True | False | True | True | True | PASS |
| 77 | http://shpigovsky.test/uslugi/psihicheskoe-zdorovie/ | subdivision | True | True | True | True | True | True | PASS |
| 84 | http://shpigovsky.test/uslugi/rasstroystva-pischevogo-povedeniya/ | subdivision | True | True | True | True | True | True | PASS |

## Layout variant runtime check

| Service | Expected | Detected | Method | Result |
|---|---|---|---|---|
| 73 | subdivision | subdivision | html_regex:site-main--service-subdivision|shpigovsky-service--subdivision | PASS |
| 74 | alcohol-special | alcohol-special | html_regex:shpigovsky-service--alcohol|service-leaf-signs | PASS |
| 77 | subdivision | subdivision | html_regex:site-main--service-subdivision|shpigovsky-service--subdivision | PASS |
| 84 | subdivision | subdivision | html_regex:site-main--service-subdivision|shpigovsky-service--subdivision | PASS |

## Home / Services Hub stability

| Route | HTTP | Key marker | Result |
|---|---:|---|---|
| Home | 200 | site-main--front | PASS |
| Services Hub | 200 | site-main--services-hub | PASS |

## Asset smoke

| Asset | Status |
|---|---|
| V9 CSS | PASS |
| V9 shell JS | PASS |
| Logo SVG | PASS |

## Service 74 regression

URL: http://shpigovsky.test/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/ — HTTP 200 — variant alcohol-special — PASS

## Visual smoke

Screenshots: PASS — 14 captured.

## Result

PASS
