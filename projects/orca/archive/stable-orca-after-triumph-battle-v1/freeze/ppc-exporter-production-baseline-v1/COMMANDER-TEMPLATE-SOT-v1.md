# Commander Template SoT v1

**Title:** Commander Search Manual Bids Template SoT v1  
**Freeze:** PPC Exporter Production Baseline v1  
**Date:** 2026-05-29

---

## Canonical template

| Field | Value |
|-------|-------|
| **Filename** | `triumph-manipulator-commander-template-v1.xlsx` |
| **Repository path** | `projects/orca/ppc/triumph-manipulator/assets/direct-commander-template/triumph-manipulator-commander-template-v1.xlsx` |
| **template_id** | `triumph-manipulator-commander-template` |
| **template_revision** | `v1` |
| **Supersedes** | `triumph-manipulator-commander-template-v0.xlsx` (reference only — do not use for new exports) |

---

## Campaign strategy (frozen)

| Parameter | Value |
|-----------|-------|
| **Placement** | Реклама на поиске (Search) |
| **Bidding** | Ручное управление ставками (Manual CPC) |
| **Automation** | None — ORCA does not autobid or auto-launch |
| **RSYA / retargeting** | Out of scope for this template |

---

## Status

| Gate | State |
|------|-------|
| Template approved | **Yes** |
| Production validated | **Yes** — full-cycle export + integrity checks |
| Commander imported | **Yes** — human-operated import session |
| Human calibrated | **Yes** — bids, negatives, URL spot-check per calibration doc |

---

## Role in ORCA stack

```
ORCA JSON (meaning SoT)
    → validation
    → Exporter v1.2 (mapping + sheet1 patch)
    → triumph-manipulator-commander-template-v1.xlsx (transport shape)
    → Direct Commander import
    → Human QA
```

| Layer | SoT? |
|-------|------|
| JSON + doctrine | **Yes** — campaign meaning |
| Template v1 | **Yes** — Commander **transport** shape for Search manual bids |
| Generated output XLSX | **No** — disposable import snapshot |

---

## Operator rules

1. **All** new Triumph Search PPC exports MUST use template **v1** as the patch base (`sheet1-patch-export.js` reads this asset).  
2. Do **not** edit template in place as the campaign — reconcile via JSON.  
3. On Commander UI drift — copy template to `v2`, update mapping contract, re-run golden export — do not silently mutate v1.  
4. Bid fields follow [BID-MANAGEMENT-RULES-v1.md](BID-MANAGEMENT-RULES-v1.md) after import (human-applied in Commander).  
5. Pre-export: [COMMANDER-HYGIENE-AUDIT-v1.md](COMMANDER-HYGIENE-AUDIT-v1.md) + [CROSS-NEGATIVE-RULES-v1.md](CROSS-NEGATIVE-RULES-v1.md).

---

## Exporter binding

| Config | Expected value |
|--------|----------------|
| Exporter label | `ORCA Commander Transport Split v1.2` |
| Mapping rev | `entity-to-commander-mapping-v1` + transport split v1.2 |
| npm script | `export:sheet1-patch:full-cycle-v1.2` |
| Post-export QA | `validate:no-duplicate-ads-v1.2` |

See [EXPORTER-V1.2-APPROVAL-v1.md](EXPORTER-V1.2-APPROVAL-v1.md).

---

## Asset README

Operator-facing asset notes: [assets/direct-commander-template/README.md](../../ppc/triumph-manipulator/assets/direct-commander-template/README.md) — updated to reflect v1 SoT.

---

## SAFE UNKNOWN

- Exact Yandex Direct Commander column order drift vs pinned template — confirm at import if UI version changed since 2026-05-29.  
- Account-type-specific field requirements — human check on first import after account changes.
