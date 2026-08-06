# Phase 1B-D6B Evidence Pack

Offline separation of factual `source_status` from evaluation-time `delivery_eligibility`.

**No production apply. No webhook. No Telegram. No Data Table mutation. No commit.**

| Artifact | Purpose |
|----------|---------|
| `D6B-CHARTER.json` | Charter freeze |
| `D6B-DECISION.json` | Machine-readable decision |
| `LIVE-BASELINE-GET-ONLY.md` | Client Ops GET-only baseline |
| `RUNTIME-BASELINE.md` | SITE-002 runtime read-only |
| `CURRENT-FRESHNESS-FLOW.md` | Pre-fix conflation map |
| `SOURCE-STATUS-AUTHORITY.md` | Factual mapping |
| `DELIVERY-ELIGIBILITY-MODEL.md` | Eligibility states |
| `NOTIFICATION-POLICY-BOUNDARY.md` | Status vs eligibility vs notify |
| `THRESHOLD-BOUNDARY.md` | 93600 operator |
| `EVENT-IDENTITY-FRESHNESS-INDEPENDENCE.md` | event_id proofs |
| `BACKWARD-COMPATIBILITY.md` | Compatibility notes |
| `CONTRACT-SURFACE-DECISION.md` | Internal-only decision |
| `FIXTURE-MATRIX.md` | B1–B15 |
| `OFFLINE-IMPLEMENTATION.md` | Changed files |
| `TEST-RESULTS.md` | D6B harness |
| `REGRESSION-RESULTS.md` | Full offline suites |
| `SECURITY-REVIEW.md` | Security gate |
| `_get-baseline.mjs` | GET-only helper (no mutation) |
