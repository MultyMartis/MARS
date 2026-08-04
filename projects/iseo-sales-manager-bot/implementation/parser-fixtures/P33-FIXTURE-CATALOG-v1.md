# P33 FIXTURE CATALOG v1

**Product:** i-SEO Sales Manager Bot  
**Phase:** 3E.1 Parser 3.3  
**Status:** Implemented — exercised by `implementation/harness/phase3e1-harness.mjs`  
**Rule:** synthetic / reserved example values only; zero external calls; zero real PII

**Libs:** `parse-lead-lib.mjs` · `processor-lib.mjs` · `formatter-lib.mjs`

---

## Catalog (semantic classes)

| ID | Class | Expectation |
|----|-------|-------------|
| P33-01 | multiline canonical | fields + provenance OK |
| P33-02 | collapsed / one-line | same semantics (H03) |
| P33-03 | reordered labels | order-independent |
| P33-04 | site explicitly absent | `website_state=explicitly_absent` |
| P33-05 | messenger in site | `alternative_contact` (H09) |
| P33-06 | placeholder site/contact | `invalid_or_placeholder` (H10) |
| P33-07 | label words in comment | boundary not cut early (H12) |
| P33-08 | comment vs form title | comment wins; conflict stamped |
| P33-09 | structured vs selected service | structured wins |
| P33-10 | page vs subject | page context wins when stronger |
| P33-11 | missing all intent | Other/unknown, no invention |
| P33-12 | reply consistency | no unsupported facts (H19–H21, H25) |
| P33-13 | quoted history / signature | current form isolated |
| P33-14 | Unicode / NBSP / CRLF | deterministic normalize |
| P33-15 | backward v3.2 set | no approved regression (H29) |

Harness IDs H01–H42 + P33-04 + MSG cover the acceptance matrix (46 checks). Full expected JSON lives in harness assertions, not in committed PII dumps.

---

## Run

```text
cd projects/iseo-sales-manager-bot
node implementation/harness/phase3e1-harness.mjs
```

Required: **46/46 PASS**. Evidence: `evidence/phase3e1/HARNESS-RESULTS-v1.md`.
