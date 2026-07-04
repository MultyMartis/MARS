# FP-0002 V9-06D.5 Readiness After Route Investigation v1

**Date:** 2026-07-04  
**Phase:** ROUTE-OWNERSHIP-INVESTIGATION

## Decision

**D5_BLOCKED_ROUTE_REPAIR_REQUIRED**

## Reason

Service ID 74 remains HTTP **404** on its canonical generated path:

`/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/`

That URL is an authorized visual route QA target from V9-06D.4. Root cause is identified (`POST_TYPE_LINK_REWRITE_MISMATCH`) but repair is **not** authorized or applied in this diagnostics-only task.

## Alternatives considered

| Outcome | Verdict |
|---|---|
| `D5_READY` | Rejected — blocking 404 remains |
| `D5_CAN_PROCEED_WITH_KNOWN_404_EXCLUSION` | Rejected — alcohol leaf service is in-scope for D.5 visual QA; exclusion would weaken gate value |
| `D5_BLOCKED_ROUTE_REPAIR_REQUIRED` | **Selected** |

## Prerequisites before D.5

1. Authorized rewrite-rule repair micro-task (recommended Option 2).
2. Source delivery of corrected `ServicePermalinks` depth-2 mapping.
3. Soft rewrite flush under checkpoint.
4. Post-repair route validation: Service 74 HTTP 200 + controls unchanged.

## Authorization status

V9-06D.5 visual route QA: **NOT AUTHORIZED**

## Result

D.5 **BLOCKED** pending rewrite rule repair.
