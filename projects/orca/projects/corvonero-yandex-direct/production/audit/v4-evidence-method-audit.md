# V4 Evidence Method Audit — Корво Неро

**Status:** v4 = AUDIT INPUT (operator rejected)  
**Generated:** 2026-06-22

## Summary

v4 claimed human-grade semantic review but produced template-filled evidence. Collision QA reported PASS while 2451 stem-risk warnings remained unresolved.

## Root causes (code)

| ID | Issue | Location |
|----|-------|----------|
| RC-01 | 324 active phrases with identical `clear_commercial_service_intent` | `semantic-human-review-v4.mjs` → `reviewKeywordV4` |
| RC-02 | Generic intent fallback per group | `inferLikelyIntent` line 129 |
| RC-03 | Automatic `reviewer_status: REVIEWED` | `reviewKeywordV4` return object |
| RC-04 | No group-fit validation; stale v3 group_id kept | `run-full-production-v4.mjs` |
| RC-05 | `advertisement_match: yes` without mismatch check | `evaluateAdLandingMatch` |
| RC-06 | Unresolved stem warnings + PASS | `collision-evidence-v4.mjs` summary |
| RC-07 | `negativeRegistryWithQA` formal PASS | `collision-evidence-v4.mjs` |
| RC-08 | Empty correction column for STEM_RISK rows | `generate-review-workbook-v4.cjs` |
| RC-09 | Ad changes with empty issues | `ads-v4.mjs` → `reviewAllAdsCertainty` |
| RC-10 | Regression tests ignore workbook integrity | `regression-tests-v4.mjs` |

## Data flow

1. **Semantic:** v3 keywords → pattern classifier → template reason → JSON labeled human-grade → workbook.
2. **Collision:** Pre-filter removals → audit → count stem warnings → no resolution step → PASS.
3. **Workbook:** Operator-facing sheets populated with formal defaults (`yes`, `REVIEWED`, empty corrections).

## v5 corrections

- Phrase-specific reasons required for active phrases.
- Honest review states: `SEMANTICALLY REVIEWED`, `RULE-SCREENED`, etc.
- Separate group-fit gate and reassignment log.
- Unique negative risk resolution with zero unresolved before PASS.
- Literal vs semantic-risk corrections separated in collision evidence.
- Workbook integrity tests (no `1234`, no blank corrections for blocking findings).
