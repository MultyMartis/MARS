# FP-0002 V9-06D.4 RERUN Visual Route QA URL List v1

Domain: `http://shpigovsky.test/`

| URL | Expected object | HTTP (post-seed) | Generated permalink match | Notes |
|---|---|---:|---|---|
| `/` | Page 4 | 200 | YES | Home ACF seed |
| `/uslugi/` | Page 5 | 200 | YES | Services hub ACF seed |
| `/uslugi/zavisimosti/` | Service 73 | 200 | YES | Page ID 6 also shares this path historically |
| `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | Service 74 | 404 | YES | **REWRITE_FLUSH_MICRO_GATE_REQUIRED** |
| `/uslugi/psihicheskoe-zdorovie/` | Service 77 | 200 | YES | |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` | Service 84 | 200 | YES | |
| `/kontakty/` | Page 20 | 200 | YES | Contacts ACF seed |

## Rewrite flush

- Required for Service 74 HTTP resolution: **YES**
- Performed in D.4: **NO**
- Status document: `FP-0002-V9-06D4-RERUN-REWRITE-FLUSH-STATUS-v1.md`
