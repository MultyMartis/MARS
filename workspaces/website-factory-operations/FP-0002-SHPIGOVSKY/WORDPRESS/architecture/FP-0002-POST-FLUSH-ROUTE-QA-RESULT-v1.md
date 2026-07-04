# FP-0002 Post-Flush Route QA Result v1

**Domain:** `http://shpigovsky.test/`  
**After:** REWRITE-FLUSH-MICRO-GATE soft flush

| URL | Expected object | HTTP after | Generated permalink match | Result |
|---|---|---:|---|---|
| `/` | Page 4 | 200 | YES | PASS |
| `/uslugi/` | Page 5 | 200 | YES | PASS |
| `/uslugi/zavisimosti/` | Service 73 | 200 | YES | PASS |
| `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | Service 74 | **404** | YES | FLUSH_NOT_SUFFICIENT |
| `/uslugi/psihicheskoe-zdorovie/` | Service 77 | 200 | YES | PASS |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` | Service 84 | 200 | YES | PASS |
| `/kontakty/` | Page 20 | 200 | YES | PASS |

## Summary

- HTTP 200: 6 / 7
- HTTP 404: 1 / 7 (Service 74 only)
- Rewrite flush performed: YES (soft)
- Hard flush: NO
- D.4 QA URLs all pass: NO
- Classification: `FLUSH_NOT_SUFFICIENT`

## Service 74 detail

Generated permalink remains:

`/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/`

Rewrite rules include depth-2 service pattern:

`^uslugi/([^/]+)/([^/]+)/?$ => index.php?post_type=service&service=$matches[2]`

Flush alone does not resolve HTTP 404. Do not create redirects or edit content in this gate.
