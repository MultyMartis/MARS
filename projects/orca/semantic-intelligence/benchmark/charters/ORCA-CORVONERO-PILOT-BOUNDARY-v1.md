# ORCA Corvonero Pilot Boundary v1

**Boundary ID:** `orca-corvonero-pilot-boundary`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`

---

## Purpose

Bound the **Corvonero pilot** (300–500 phrases, D5) within the universal ORCA benchmark program. Define what the pilot may and may not authorize.

---

## Current system state

| Item | Status |
|------|--------|
| Corvonero clean-room v1 | **FROZEN** (D2) |
| Campaign production | **BLOCKED** (D7) |
| Classifier | **NOT STARTED** |
| Old Corvonero v1 admission labels | **FORBIDDEN** as benchmark ground truth |

---

## Pilot scope

| Parameter | Value |
|-----------|-------|
| Size | 300–500 phrases |
| Draw | Stratified from universal sampling frame + Corvonero-relevant domain overweight where operator approves |
| Double annotation | **100%** |
| Blind subset | ≥ 100 phrases — sealed per blind governance |
| Hard-negative pack | Separate fixed subset within pilot |

---

## What pilot pass permits

- Proceed to P0-F baseline measurement on **released dev/calibration splits** (not blind)
- Operator review for **semantic admission rerun** on preserved Corvonero corpus (D2 path)
- Continued B2 universal benchmark build

---

## What pilot pass does NOT permit

- Campaign architecture, ad groups, creatives, bids, Commander export (D7)
- Treating pilot as full universal benchmark
- Using diagnostic failed v1 labels as silver standard
- Auto-accept production threshold changes without P0-G gate

---

## Go/no-go inputs (P0-G)

Operator-approved (D3):

- Commercial precision on auto-accept ≥ **0.95**
- Protected-strata FPR ≤ **0.01** per class

Additional metrics: PROPOSED — VALIDATE DURING B0/B1; measured at P0-G against blind subset.

---

## Relationship to universal benchmark

```text
Universal program (1200–2000)
├── Corvonero pilot slice (300–500) ── go/no-go for rerun
├── Dev / calibration splits
├── Blind test pack (≥300–400)
└── Hard-negative / regression anchors (fixed)
```

Pilot records use the same benchmark record schema and gold authority as universal records.
