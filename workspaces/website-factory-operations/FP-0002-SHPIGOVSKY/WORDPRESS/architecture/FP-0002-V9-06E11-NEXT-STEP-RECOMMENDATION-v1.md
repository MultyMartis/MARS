# FP-0002 V9-06E11 Next Step Recommendation v1

**Date:** 2026-07-07  
**Verdict:** PASS  
**Recommended next action:** CREATE_V9_06E12_DIRECT_STATIC_PORT_REPAIR_ALCOHOL_LEAF_TASK

## Rationale

E11 contract inventory confirms E10 root cause: WordPress routes use semantic PHP reconstruction (alcohol-stack.php, leaf-stack.php, CPT-driven hub) rather than direct static V9 HTML section-stack ports.

| Signal | Evidence |
|---|---|
| Highest-risk static-backed page | /uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/ — NEEDS_DIRECT_V9_REPLACEMENT |
| Section class probe | 18 classes match static dist order (E10/E11 live probe) |
| Visual drift | Operator + E10 screenshot diff — inner markup/home partial reuse |
| Truncated generic leaf | leaf-stack.php — 10 sections vs 17 static authority |
| Governance gate | E10 contract sections 2–4 — no PASS without screenshot after direct port |

## E12 scope (recommended)

1. Replace alcohol-stack.php orchestration with direct static V9 section HTML port from usluga-konechnaya-v1.html / dist counterpart.
2. Fork home partials used on service context (specialists, reviews, comfort, clinic-landscape) or parameterize with service-leaf IDs.
3. Classify each section content as EXACT_V9_CONTENT vs V9_FIXTURE_DEMO vs OPERATOR_REAL_CONTENT.
4. Mandatory screenshot pair: static dist vs runtime before any PASS.
5. No broad refactor — single page only.

## Deferred (post-E12)

- /uslugi/ hub direct port (E13)
- / home content reseed (E14)
- Legal shell gaps (subnav/final-form) — low severity
- Blog — DEFERRED
- Placeholder leaf routes — DEMO_ACCEPTED

Authority: validation/v9-06e11-static-to-wp-page-contract-inventory/final-verdict.json
