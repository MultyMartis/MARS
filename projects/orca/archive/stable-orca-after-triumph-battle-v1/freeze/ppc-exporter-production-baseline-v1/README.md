# PPC Exporter Production Baseline v1 — freeze index

**Label:** `orca-ppc-exporter-production-baseline-v1`  
**Date:** 2026-05-29  
**Lane:** B — ORCA PPC Production Baseline Freeze  
**Project:** Triumph Manipulator Search PPC  
**Status:** **FROZEN** — production export baseline — **not** launch, **not** push

---

## Purpose

Зафиксировать официальный production baseline цикла:

**ORCA → JSON → Exporter v1.2 → XLSX → Direct Commander → Human QA**

как Source of Truth для Triumph Manipulator Search PPC export governance.

Этот freeze **не** меняет объявления, ключевые фразы, URL, структуру кампании и **не** запускает рекламу.

---

## Artifact map

| Doc | Role |
|-----|------|
| [PPC-EXPORTER-PRODUCTION-BASELINE-v1.md](PPC-EXPORTER-PRODUCTION-BASELINE-v1.md) | Main freeze — scope, pipeline, SoT hierarchy |
| [COMMANDER-TEMPLATE-SOT-v1.md](COMMANDER-TEMPLATE-SOT-v1.md) | Commander Search Manual Bids Template SoT |
| [EXPORTER-V1.2-APPROVAL-v1.md](EXPORTER-V1.2-APPROVAL-v1.md) | Exporter transport split approval |
| [BID-MANAGEMENT-RULES-v1.md](BID-MANAGEMENT-RULES-v1.md) | Official bid range and variation rules |
| [CROSS-NEGATIVE-RULES-v1.md](CROSS-NEGATIVE-RULES-v1.md) | Route-family cross-negative matrix obligation |
| [COMMANDER-HYGIENE-AUDIT-v1.md](COMMANDER-HYGIENE-AUDIT-v1.md) | Pre-export READY hygiene checklist |
| [COMMANDER-CALIBRATION-FINDINGS-v1.md](COMMANDER-CALIBRATION-FINDINGS-v1.md) | Human calibration findings from full cycle |
| [GIT-CHECKPOINT-v1.md](GIT-CHECKPOINT-v1.md) | Git checkpoint record (hash, scope, exclusions) |

---

## Canonical assets (not duplicated here)

| Asset | Path |
|-------|------|
| Commander template SoT | `projects/orca/ppc/triumph-manipulator/assets/direct-commander-template/triumph-manipulator-commander-template-v1.xlsx` |
| Exporter CLI | `projects/orca/ppc/triumph-manipulator/tools/exporter-cli/` |
| PPC JSON instance (reference) | `projects/orca/ppc/triumph-manipulator/schema/instances/triumph-s-tier-draft-v1.json` |

---

## Related freezes (prior milestones)

| Freeze | Relationship |
|--------|----------------|
| [route-family-freeze-v1](../route-family-freeze-v1/) | Semantic 12-route family — upstream |
| [commander-url-sync-v1](../commander-url-sync-v1/) | Canonical `.html` URLs — upstream |
| [commander-transport-fix-v1](../commander-transport-fix-v1/) | Transport split v1.2 — incorporated here |

---

## Boundaries

| In scope | Out of scope |
|----------|--------------|
| Export governance, template SoT, bid/cross-negative rules | Ad copy / keyword / URL edits |
| Hygiene audit gates before export READY | Campaign launch, bidding automation |
| Exporter v1.2 approval documentation | Git push, live ads |
| Human QA requirements | Runtime / orchestration claims |
