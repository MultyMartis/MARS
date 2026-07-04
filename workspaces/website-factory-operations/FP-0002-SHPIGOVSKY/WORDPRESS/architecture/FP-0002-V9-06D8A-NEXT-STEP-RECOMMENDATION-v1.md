# FP-0002 V9-06D8A Next Step Recommendation v1

**Date:** 2026-07-05  
**Prior task:** V9-06D8-A Site Options Seed — BLOCKED

---

## Recommended next action

**OPERATOR_DECISION_REQUIRED**

## Rationale

D8-A planning gates passed (allowlist, payload, dry-run). Apply blocked by infrastructure:

1. Start local MySQL/Laragon for `mars_wp_fp0002`.
2. Confirm HTTP `http://shpigovsky.test/` responds.
3. Resolve strict HEAD pin (`989b97a9` vs current `d98557fb`) if required.
4. Re-run D8-A apply using prepared runner + checkpoint.

## After successful D8-A apply

**CREATE_V9_06D8B_HOME_CONTENT_SEED_TASK** — only when site options seeded and route smoke PASS.

## Parallel operator data collection

**CREATE_V9_06D8A_OPERATOR_DATA_COLLECTION_TASK** — for `map_link`, `social_links`, `legal_org_identifiers`, production confirmation of phone/email.

## V9-06D8B authorization

**NO** — blocked until D8-A COMPLETE.
