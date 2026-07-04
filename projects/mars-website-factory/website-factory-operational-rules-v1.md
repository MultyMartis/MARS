# Website Factory — Operational Rules v1

**Status:** **ACTIVE** — compact operational gates and completion rules  
**Date:** 2026-07-02  
**Not:** runtime orchestration, automated enforcement, or scheduler

**Purpose:** High-signal operational rules operators check before closing waves, programs, or client-facing milestones. Detail lives in linked standards — this file states **gates only**.

---

## 1. Execution baseline

| Rule | Authority |
|------|-----------|
| Human-operated; prompt → execute → REPORT | [cursor-execution-standard-v0.md](cursor-execution-standard-v0.md) |
| No fake autonomous approval | [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md) |
| REPORT format | [reporting-standard-v0.md](reporting-standard-v0.md) |
| First operational path | [first-operational-runbook-v0.md](first-operational-runbook-v0.md) |

---

## 2. Research completion rule (NEW — 2026-07-02)

**Rule RS-COMPLETE-001:** A Website Factory research program is **not complete** until **ORCA-RS-001** Publication Gate passes (ORCA publishes Executive Research; Factory consumes).

| Required before "research complete" | Standard |
|-----------------------------------|----------|
| Executive Research.xlsx + Research Conclusions.docx + README.md + sources.md | [ORCA-RS-001](../orca/standards/ORCA-RS-001-EXECUTIVE-RESEARCH-PUBLICATION-STANDARD-v1.md) (ORCA-owned) |
| generator.py when package is generatable | ORCA-RS-001 §3 |

**Blocked actions before gate:**

- Research Freeze as final state
- Client delivery of internal Registry / Presentation Pack alone
- Knowledge map registration without Executive Package path

**Overview:** [research-standards-v1.md](research-standards-v1.md) · [publication-standards-v1.md](publication-standards-v1.md)

---

## 3. Frontend production gates (summary)

| Gate | Authority |
|------|-----------|
| Production Standards Draft + Approval | [production-standards-governance-v1.md](production-standards-governance-v1.md) |
| Shell-first start | [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md) |
| Operator visual approval | [operator-visual-approval-law-v1.md](operator-visual-approval-law-v1.md) |
| Production mode intake | [website-factory-production-modes-charter-v1.md](website-factory-production-modes-charter-v1.md) |

Full frontend rules: [frontend-production-rules-v0.md](frontend-production-rules-v0.md)

---

## 4. Validation & delivery gates (summary)

| Gate | Authority |
|------|-----------|
| VL0–VL6 validation chain | [website-factory-validation-architecture-charter-v1.md](website-factory-validation-architecture-charter-v1.md) |
| Delivery lifecycle | [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md) |
| Artifact publication classes | [artifact-publication-semantics-v0.md](artifact-publication-semantics-v0.md) |

---

## 5. Registration & knowledge

| Action | Rule |
|--------|------|
| New execution case | Append [execution-cases-registry-v1.md](execution-cases-registry-v1.md) before silent delivery |
| Research knowledge | Register Executive Package in [website-factory-knowledge-map-v1.md](website-factory-knowledge-map-v1.md) |
| New WF standard | Append [website-factory-standards-register-v1.md](website-factory-standards-register-v1.md) |

---

*Website Factory Operational Rules v1 — 2026-07-02.*
