# CORVONERO NEW CONTROLLED SEMANTIC RUN — GATE MATRIX v1

**Date:** 2026-06-26  
**Status:** DRAFT — pending charter approval

---

## Gate A — Charter approval

| Attribute | Value |
|-----------|-------|
| When | Before any runtime execution |
| Evidence | Operator charter, input manifest, old-run non-resume declaration |
| Decisions | APPROVE_CHARTER / REJECT_CHARTER / REQUEST_REVISION |
| On reject | Stop — no run ID, no lock, no model calls |

## Gate B — SPPC-05 result

| Attribute | Value |
|-----------|-------|
| When | Before live canary |
| Evidence | Closed-dataset SPPC-05 report, Wave 3.1F regression receipts |
| Decisions | PASS / FAIL / FAIL_CLOSED |
| On reject | Stop — no canary, no production batches |
| New run ID if | Authority mismatch or corruption |

## Gate C — Canary review

| Attribute | Value |
|-----------|-------|
| When | Before full corpus |
| Evidence | Canary batch receipt, class distribution, operator sample (30) |
| Decisions | APPROVE_CONTINUE / REJECT_STOP / REQUEST_CANARY_RERUN |
| On reject | Stop batches; lock retained for forensic review |

## Gate D — Mid-run quality review

| Attribute | Value |
|-----------|-------|
| When | Fixed threshold (proposed: 500 processed) |
| Evidence | ACCEPT/REJECT/ABSTAIN counts, error-family audit, cost report |
| Decisions | CONTINUE / PAUSE / STOP_FAIL_CLOSED |
| Resume | Permitted within same run if operator approves |

## Gate E — Final semantic reconciliation

| Attribute | Value |
|-----------|-------|
| When | Before semantic assembly authority |
| Evidence | Reconciliation receipt, orphan/duplicate audit, 2368 completeness |
| Decisions | APPROVE_ASSEMBLY / REJECT_RECONCILIATION |
| On reject | No semantic registry promotion |

## Gate F — Final handoff approval

| Attribute | Value |
|-----------|-------|
| When | Before Search PPC strategy work |
| Evidence | Semantic registry, operator review package, handoff manifest |
| Decisions | APPROVE_HANDOFF / REJECT_HANDOFF |
| Note | Wave 5 remains **BLOCKED** until separate lifecycle authorization |

Machine-readable companion: `CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-GATE-MATRIX-v1.json`
