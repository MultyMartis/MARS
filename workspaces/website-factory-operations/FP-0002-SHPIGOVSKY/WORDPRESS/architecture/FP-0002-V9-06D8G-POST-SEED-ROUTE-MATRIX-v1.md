# FP-0002 V9-06D8G Post-Seed Route Matrix v1

**Date:** 2026-07-05  
**Phase:** V9-06D8-G Post-Seed QA  
**Evidence:** `validation/v9-06d8g-post-seed-qa/post-seed-route-matrix.json`

---

## Summary

| Metric | Result |
|---|---|
| Required routes | 7 |
| HTTP 200 | 7 |
| Object resolution | 7/7 PASS |
| V9 CSS loaded | 7/7 |
| V9 JS loaded | 7/7 |
| Fatal/raw PHP | 0 |
| **Overall** | **ALL_200** |

---

## Route matrix

| Route | URL | HTTP | Expected | Resolved | Header | Footer | CSS | JS | Result |
|---|---|---:|---|---|---:|---:|---:|---:|---|
| Home | `/` | 200 | page #4 | page #4 | yes | yes | yes | yes | PASS |
| Services Hub | `/uslugi/` | 200 | page #5 | page #5 | yes | yes | yes | yes | PASS |
| Service 73 | `/uslugi/zavisimosti/` | 200 | service #73 | service #73 | yes | yes | yes | yes | PASS |
| Service 74 | `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | 200 | service #74 | service #74 | yes | yes | yes | yes | PASS |
| Service 77 | `/uslugi/psihicheskoe-zdorovie/` | 200 | service #77 | service #77 | yes | yes | yes | yes | PASS |
| Service 84 | `/uslugi/rasstroystva-pischevogo-povedeniya/` | 200 | service #84 | service #84 | yes | yes | yes | yes | PASS |
| Contacts | `/kontakty/` | 200 | page #20 | page #20 | yes | yes | yes | yes | PASS |

---

## Result

**COMPLETE — ALL_200**
