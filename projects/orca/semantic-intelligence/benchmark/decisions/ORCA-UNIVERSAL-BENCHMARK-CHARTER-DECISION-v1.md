# ORCA Universal Benchmark Charter Decision v1

**Decision ID:** `orca-universal-benchmark-charter-decision`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — ON HOLD` (pending operator review of [triumph-to-orca capability recovery audit v1](../../audits/triumph-to-orca-capability-recovery-v1/))  
**Machine reference:** [`orca-universal-benchmark-charter-decision-v1.json`](orca-universal-benchmark-charter-decision-v1.json)

---

## Decision summary

Adopt **P0-D Universal Benchmark Charter v1** as the documentation authority for ORCA stratified gold benchmark construction — subject to operator approval.

---

## Selected model (D5)

| Product | Size |
|---------|------|
| Universal ORCA benchmark | 1,200–2,000 phrases |
| Corvonero pilot | 300–500 phrases |
| Blind test | 300–400 phrases |
| Phases | B0 → B1 → B2 |

---

## Operator-approved thresholds (D3)

- Commercial precision on auto-accept: **≥ 0.95**
- Protected-strata FPR per class: **≤ 0.01**

All other numeric gates: **PROPOSED — VALIDATE DURING B0/B1**.

---

## Deferred decisions

| ID | Topic | Status |
|----|-------|--------|
| U-D01 | Long-term double-annotation % | OPERATOR DECISION REQUIRED AFTER B0 |
| U-D02 | Proposed metric thresholds | VALIDATE B0/B1 |
| U-D03 | Hard-negative pack exact size | VALIDATE B0/B1 |

---

## Consequences until approval

| Item | Status |
|------|--------|
| Benchmark rows | NOT STARTED |
| B0 execution | BLOCKED |
| Corvonero | FROZEN |
| Classifier | NOT STARTED |
| Campaign production | BLOCKED |

---

## Operator action required

Approve or reject P0-D charter package. Approval unblocks **B0 qualification planning only** — not Corvonero rerun or campaign production.
