# PPC Exporter Production Baseline v1

**Project:** Triumph Manipulator (`triumph-manipulator-krasnodar`)  
**Freeze date:** 2026-05-29  
**Lane:** B — ORCA PPC Production Baseline Freeze  
**Status:** **PRODUCTION BASELINE** — export path validated — **not** launch approval

---

## Purpose

Зафиксировать успешный human-validated цикл как официальный Source of Truth для Triumph Manipulator Search PPC export:

```
ORCA doctrine + JSON instance
    → validation-cli (human-triggered)
    → Exporter v1.2 (transport split)
    → XLSX (Commander template v1)
    → Direct Commander import
    → Human QA
```

Этот документ — **главный freeze** папки `ppc-exporter-production-baseline-v1/`.

---

## Explicit non-goals (this freeze)

| Prohibited | Rationale |
|------------|-----------|
| Change ads, headlines, descriptions | Out of scope — semantic/content freeze elsewhere |
| Change keywords / match types | Out of scope |
| Change URLs / display paths | Locked by [commander-url-sync-v1](../commander-url-sync-v1/) |
| Change campaign / group structure | Out of scope |
| Launch ads / set live budgets | Human operator only; never agent-automated |
| Git push | Explicitly excluded per task charter |

---

## Production pipeline (frozen)

| Step | Owner | Artifact / tool |
|------|-------|-----------------|
| 1. ORCA JSON SoT | Human + schema | `schema/instances/triumph-s-tier-draft-v1.json` |
| 2. Validation | Human-triggered CLI | `tools/validation-cli/` → `validation-report.output.json` |
| 3. Cross-negative matrix | ORCA obligation | [CROSS-NEGATIVE-RULES-v1.md](CROSS-NEGATIVE-RULES-v1.md) — **before** export READY |
| 4. Hygiene audit | Human checklist | [COMMANDER-HYGIENE-AUDIT-v1.md](COMMANDER-HYGIENE-AUDIT-v1.md) |
| 5. Export | Exporter v1.2 | `npm run export:sheet1-patch:full-cycle-v1.2` |
| 6. Transport QA | Automated local script | `npm run validate:no-duplicate-ads-v1.2` |
| 7. Commander import | Human | [COMMANDER-TEMPLATE-SOT-v1.md](COMMANDER-TEMPLATE-SOT-v1.md) |
| 8. Human QA | Human | Bids, negatives live, schedule — [COMMANDER-CALIBRATION-FINDINGS-v1.md](COMMANDER-CALIBRATION-FINDINGS-v1.md) |

---

## Source-of-truth hierarchy

| Layer | SoT | Notes |
|-------|-----|-------|
| **Meaning** | ORCA JSON + doctrine + validation rules | Intent, segmentation, landing routing |
| **Export transport** | Commander template v1 + Exporter v1.2 mapping | [COMMANDER-TEMPLATE-SOT-v1.md](COMMANDER-TEMPLATE-SOT-v1.md) |
| **Bids (human-applied)** | [BID-MANAGEMENT-RULES-v1.md](BID-MANAGEMENT-RULES-v1.md) | Exporter may emit placeholders; operator calibrates in Commander |
| **Cross-route negatives** | [CROSS-NEGATIVE-RULES-v1.md](CROSS-NEGATIVE-RULES-v1.md) | Mandatory pre-export stage |
| **Excel output** | Generated snapshot | `tools/exporter-cli/output/*.xlsx` — gitignored; not SoT |

---

## Commander template (production)

| Field | Value |
|-------|-------|
| **File** | `triumph-manipulator-commander-template-v1.xlsx` |
| **Path** | `projects/orca/ppc/triumph-manipulator/assets/direct-commander-template/` |
| **Strategy** | Реклама на поиске · Ручное управление ставками |
| **Status** | approved · production validated · commander imported · human calibrated |
| **Use** | Primary template for **all** future ORCA Search PPC exports (Triumph family) |

---

## Exporter governance

| Item | Reference |
|------|-----------|
| Approved exporter revision | v1.2 transport split |
| Approval doc | [EXPORTER-V1.2-APPROVAL-v1.md](EXPORTER-V1.2-APPROVAL-v1.md) |
| Prior transport fix | [commander-transport-fix-v1](../commander-transport-fix-v1/) |
| Import checklist | [commander-transport-fix-v1/COMMANDER-IMPORT-CHECKLIST-v1.2.md](../commander-transport-fix-v1/COMMANDER-IMPORT-CHECKLIST-v1.2.md) |

---

## Export READY gates (summary)

All must pass before treating an XLSX as production-ready:

1. Validation report — export not blocked  
2. Cross-negative matrix built and group negatives exported — [CROSS-NEGATIVE-RULES-v1.md](CROSS-NEGATIVE-RULES-v1.md)  
3. Commander hygiene audit — [COMMANDER-HYGIENE-AUDIT-v1.md](COMMANDER-HYGIENE-AUDIT-v1.md)  
4. `validate:no-duplicate-ads-v1.2` — PASS  
5. Human spot-check per import checklist  
6. Human QA post-import — [COMMANDER-CALIBRATION-FINDINGS-v1.md](COMMANDER-CALIBRATION-FINDINGS-v1.md)

---

## Relationship to prior freezes

| Prior freeze | What this baseline adds |
|--------------|-------------------------|
| Route family v1 | Semantic 12-route packs — **unchanged** |
| Commander URL sync v1 | Canonical `.html` URLs — **unchanged** |
| Commander transport fix v1 | v1.2 ad/keyword split — **promoted to production baseline** |
| **This freeze** | End-to-end export production SoT + bid/cross-negative/hygiene rules |

---

## Honesty boundaries

| Claim | Allowed? |
|-------|----------|
| Documentation production baseline for export path | **Yes** |
| Exporter v1.2 validated on full-cycle fixture | **Yes** (see approval doc) |
| Commander import PASS (human-operated session) | **Yes** (calibration findings) |
| Autonomous PPC runtime / orchestration | **No** — not in repo |
| Launch approval / live campaign proof | **No** — human gates only |

---

## Related artifacts

- Pack index: [ppc/triumph-manipulator/OPERATIONAL-INDEX.md](../../ppc/triumph-manipulator/OPERATIONAL-INDEX.md)  
- ORCA index: [OPERATIONAL-INDEX.md](../../OPERATIONAL-INDEX.md)  
- Git checkpoint: [GIT-CHECKPOINT-v1.md](GIT-CHECKPOINT-v1.md)
