# EAR Runtime Engineering Backlog v1

**Type:** Engineering target backlog — **no** implementation  
**Date:** 2026-06-01  
**Program:** EAR Runtime v1 (not started)  
**Prerequisite:** [freeze/EAR-RUNTIME-TRANSITION-v1/](freeze/EAR-RUNTIME-TRANSITION-v1/) architecture freeze

**Boundary:** Items below describe **what** to build, not **how**. Design contracts remain in architecture docs — see [EAR-RUNTIME-BOUNDARY-v1.md](EAR-RUNTIME-BOUNDARY-v1.md).

---

## Dependency overview

```
R1 (SFTP Read-Only Connector)
    ↓
R2 (Evidence Package Generator)
    ↓
R3 (Snapshot Builder) ──→ R4 (Snapshot Publisher)
    ↓
R5 (Validation Helpers) — may overlap R3/R4; human Validate remains HITL
```

R5 may be developed in parallel with R3 once R2 output shape is stable — charter may reorder with explicit risk acceptance.

---

## R1 — First SFTP Read-Only Connector

**Engineering target:** First **Mode 2** connected helper that performs **read-only** SFTP acquisition per connector contract — no writes, no shell, no Mode 3.

| Aspect | Target |
|--------|--------|
| **Implements** | [EAR-CONNECTOR-CONTRACT-v1.md](EAR-CONNECTOR-CONTRACT-v1.md), [EAR-CONNECTOR-ARCHITECTURE-v1.md](EAR-CONNECTOR-ARCHITECTURE-v1.md) |
| **Connector class** | SFTP Read-Only ([EAR-CONNECTOR-TYPES-v1.md](EAR-CONNECTOR-TYPES-v1.md)) |
| **Reference path** | CON-L1-A ([EAR-CONNECTED-PATHS-v1.md](EAR-CONNECTED-PATHS-v1.md)) |
| **Credential use** | `credential_ref` only ([EAR-CREDENTIAL-BOUNDARY-v1.md](EAR-CREDENTIAL-BOUNDARY-v1.md)) |
| **Scope inputs** | `sftp_root`, `allowed_paths`, `excluded_paths` — operator-provided; default exclusions [EAR-DEFAULT-EXCLUSIONS-v1.md](EAR-DEFAULT-EXCLUSIONS-v1.md) |
| **Outputs** | Raw acquisition artifacts → input for R2 (not final snapshot) |
| **Failure behavior** | [EAR-CONNECTOR-FAILURES-v1.md](EAR-CONNECTOR-FAILURES-v1.md) — fail closed, logged status |
| **First consumer of design** | PILOT-001 (TEST, SITE-001) — when Execution separately authorized |

**Non-goals for R1:** SSH shell, FTP, PMA, DB connector, Hybrid coordinator, production hosts, write operations.

**Acceptance (engineering):** Connector can complete a scoped read-only transfer plan under human supervision and emit contract-shaped status + artifact references — **without** claiming snapshot publish.

---

## R2 — Evidence Package Generator

**Engineering target:** Assemble **Evidence Package** from connector output per evidence semantics — distinct from consumer snapshot.

| Aspect | Target |
|--------|--------|
| **Implements** | [EAR-EVIDENCE-PACKAGE-v1.md](EAR-EVIDENCE-PACKAGE-v1.md) |
| **Inputs** | R1 artifacts + acquisition metadata (request id, scope, timestamps) |
| **Storage** | Quarantine / evidence workspace per [EAR-STORAGE-MODEL-v1.md](EAR-STORAGE-MODEL-v1.md) — paths operator-bound |
| **Sensitive handling** | Pre-redaction quarantine; no secrets in git |
| **Outputs** | Evidence Package structure ready for Validate (human + R5) |

**Non-goals for R2:** Publish to consumer; final snapshot quality claim; automated redaction policy engine (beyond chartered rules).

**Acceptance (engineering):** Evidence Package is inspectable, traceable to connector run, and separable from published snapshot tree.

---

## R3 — Snapshot Builder

**Engineering target:** Build **candidate Snapshot Level 1** package from validated evidence per OpenCart spec and mapping.

| Aspect | Target |
|--------|--------|
| **Implements** | [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](EAR-OPENCART-SNAPSHOT-SPEC-v1.md), [EAR-SNAPSHOT-MAPPING-v1.md](EAR-SNAPSHOT-MAPPING-v1.md), [EAR-SNAPSHOT-CONTRACT-v1.md](EAR-SNAPSHOT-CONTRACT-v1.md) |
| **Quality target** | Level **1** for PILOT-001 — [EAR-OPENCART-QUALITY-MAPPING-v1.md](EAR-OPENCART-QUALITY-MAPPING-v1.md) |
| **Manifest** | Path list respects exclusion policy; documents exclusions in metadata |
| **Inputs** | Validated evidence (post R5 / human Validate gate) |
| **Outputs** | Candidate snapshot workspace — **unpublished** |

**Non-goals for R3:** Level 2+ inventory completeness; automatic Publish; consumer-specific report generation.

**Acceptance (engineering):** Candidate package structurally matches Level 1 spec sections required for CON-L1-A / SFTP path — honest `safe-unknown` where evidence gaps exist.

---

## R4 — Snapshot Publisher

**Engineering target:** Apply **Publish** gate and produce consumer-visible snapshot reference.

| Aspect | Target |
|--------|--------|
| **Implements** | [EAR-SNAPSHOT-PUBLISHING-v1.md](EAR-SNAPSHOT-PUBLISHING-v1.md), [EAR-READINESS-GATES-v1.md](EAR-READINESS-GATES-v1.md) G4 |
| **Inputs** | Candidate snapshot + human Publish approval (HITL) |
| **Outputs** | Published snapshot location per storage model — OCPilot intake compatible |
| **Rules** | No credentials in published tree; quality level matches validated evidence |

**Non-goals for R4:** OCPilot Run 5 execution; auto-publish without HITL.

**Acceptance (engineering):** Published artifact is immutable reference version; publish log records gate satisfaction.

---

## R5 — Validation Helpers

**Engineering target:** Human-operated **Validate** assistants — checklists, structural checks, gate reminders — not autonomous certification.

| Aspect | Target |
|--------|--------|
| **Implements** | [EAR-READINESS-GATES-v1.md](EAR-READINESS-GATES-v1.md), [EAR-OPENCART-READINESS-CHECKLIST-v1.md](EAR-OPENCART-READINESS-CHECKLIST-v1.md), lifecycle Validate stage |
| **Inputs** | Evidence Package and/or candidate snapshot |
| **Outputs** | Validate report (pass/fail/partial), gate checklist status, blockers for Publish |
| **Behavior** | Fail closed — block Publish on failed mandatory checks |

**Non-goals for R5:** Unattended production gate; governance enforcement product; replacing human Validate sign-off for pilot.

**Acceptance (engineering):** Operator can run helpers to determine if Publish is **allowed** per documented gates — PILOT-001 preflight items mappable.

---

## Backlog governance

| Rule | Notes |
|------|-------|
| Charter required | No implementation without **EAR Runtime v1 Engineering Charter** |
| Architecture amendments | Out of backlog — separate human charter |
| Pilot execution | Backlog does not authorize live SFTP — [PILOT-GOVERNANCE-v1.md](PILOT-GOVERNANCE-v1.md) |
| Status honesty | Backlog existence ≠ runtime exists |

---

## Traceability

| Backlog | Primary architecture anchors |
|---------|------------------------------|
| R1 | Connector architecture, contract, CON-L1-A, credential boundary |
| R2 | Evidence package, storage quarantine |
| R3 | OpenCart snapshot spec, mapping, quality Level 1 |
| R4 | Publishing, readiness G4 |
| R5 | Gates, readiness checklist, failure models |
