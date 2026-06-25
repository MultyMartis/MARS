# ORCA Production Method Improvements — v4

## Why v3 automation incorrectly passed

1. **Pattern classifier treated as final approval** — v3 `classifyKeywordV3` allowed informational/regulatory phrases when MIG intent was commercial-mixed.
2. **Collision summary not materialized** — JSON reported 24k pairs but review workbook `Collision audit` sheet had zero rows (only blocking records exported).
3. **Empty QA sheet = false PASS** — validation boolean did not verify workbook content.
4. **Inline-minus repair** — bad phrases kept via long minus tails instead of exclusion.
5. **Ad certainty not gated separately** — guarantee wording passed keyword scan.

## v4 corrections

| Rule | Implementation |
|------|----------------|
| Semantic review mandatory | `semantic-human-review-v4.json` — 100% v3 active coverage |
| Classifier = screening only | Final gate = `reviewKeywordV4` decision |
| Collision evidence published | Review workbook sheets 14–17 populated |
| Workbook content verification | `validate-commander-xlsx-v4` + semantic checks |
| Ad certainty QA | `ads-v4.mjs` + `adCertaintyQA` |
| Regression anchors | Operator forensic list + generalized patterns in `semantic-human-review-v4.mjs` |

## Reusable regression checks

- `semantic-review-v4.json` — operator anchor leaks, informational in active
- `collision-evidence-v4.json` — findings + passed samples + regression rows
- `regression-tests-v4.mjs` — collision + semantic gates
