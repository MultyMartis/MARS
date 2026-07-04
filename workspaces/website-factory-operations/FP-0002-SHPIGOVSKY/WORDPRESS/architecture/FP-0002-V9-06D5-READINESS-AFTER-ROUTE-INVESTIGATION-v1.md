# FP-0002 V9-06D.5 Readiness After Route Investigation v1

**Date:** 2026-07-04  
**Phase:** ROUTE-OWNERSHIP-INVESTIGATION → REWRITE-RULE-REPAIR

## Decision (investigation-time)

**D5_BLOCKED_ROUTE_REPAIR_REQUIRED** — superseded by repair apply.

## Decision (post-repair)

**D5_READY** — Service 74 route repaired.

## Investigation-time reason (historical)

Service ID 74 remained HTTP **404** on its canonical generated path:

`/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/`

Root cause: `POST_TYPE_LINK_REWRITE_MISMATCH`. Repair was not applied during diagnostics-only investigation.

## Prerequisites (completed)

1. Authorized rewrite-rule repair micro-task (Option 2) — **DONE**
2. Source delivery of corrected `ServicePermalinks` depth-2 mapping — **DONE**
3. Soft rewrite flush under checkpoint — **DONE**
4. Post-repair route validation: Service 74 HTTP 200 + controls unchanged — **DONE**

## Authorization status

V9-06D.5 visual route QA: **UNBLOCKED** after REWRITE-RULE-REPAIR (Service 74 HTTP 200). See `FP-0002-REWRITE-RULE-REPAIR-REPORT-v1.md`.

## Result

D.5 **UNBLOCKED**. Next: V9-06D.5 visual route QA.
