# FP-0002 V9-06D7F Final Route Matrix v1

**Date:** 2026-07-05  
**Task:** V9-06D7-F Final Route QA (read-only)

## Matrix

| Route | URL | HTTP | Expected object | Resolved object | Root marker | Header | Footer | CSS | JS | Result |
|---|---|---:|---|---|---|---:|---:|---:|---:|---|
| Home | http://shpigovsky.test/ | 200 | page #4 | page #4 | home wp-singular page-template-default page page-id-4 wp-the | True | True | True | True | PASS |
| Services Hub | http://shpigovsky.test/uslugi/ | 200 | page #5 | page #5 | wp-singular page-template page-template-page-templates page- | True | True | True | True | PASS |
| Parent Service — Зависимости | http://shpigovsky.test/uslugi/zavisimosti/ | 200 | service #73 | service #73 | wp-singular service-template-default single single-service p | True | True | True | True | PASS |
| Child Service — Алкоголь | http://shpigovsky.test/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/ | 200 | service #74 | service #74 | wp-singular service-template-default single single-service p | True | True | True | True | PASS |
| Parent Service — Психическое здоровье | http://shpigovsky.test/uslugi/psihicheskoe-zdorovie/ | 200 | service #77 | service #77 | wp-singular service-template-default single single-service p | True | True | True | True | PASS |
| Parent Service — РПП | http://shpigovsky.test/uslugi/rasstroystva-pischevogo-povedeniya/ | 200 | service #84 | service #84 | wp-singular service-template-default single single-service p | True | True | True | True | PASS |
| Contacts | http://shpigovsky.test/kontakty/ | 200 | page #20 | page #20 | wp-singular page-template page-template-page-templates page- | True | True | True | True | PASS |

## Summary

- All HTTP 200: True
- Object resolution: True
- Result: **PASS**
