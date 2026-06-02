# EAR Runtime Scope v1

**Type:** Engineering scope definition  
**Date:** 2026-06-02  
**Complements:** [EAR-RUNTIME-NON-GOALS-v1.md](EAR-RUNTIME-NON-GOALS-v1.md), architecture [EAR-SCOPE-v1.md](../../shared/external-access-runtime/EAR-SCOPE-v1.md)

---

## What Runtime owns

Runtime owns **implementation and operation** of chartered acquisition helpers that conform to frozen architecture.

| Area | Runtime responsibility | Backlog |
|------|------------------------|---------|
| **Connector execution** | Mode 2 read-only SFTP (first class); contract-shaped status and artefact refs | R1 |
| **Evidence generation** | Assemble Evidence Package from connector output; quarantine paths per storage model | R2 |
| **Snapshot generation** | Build candidate Level 1 OpenCart snapshot from validated evidence | R3 |
| **Publishing tooling** | Apply Publish gate; produce consumer-visible immutable snapshot reference | R4 |
| **Validation tooling** | Human-operated Validate assistants — checklists, structural checks, gate reminders | R5 |
| **Operator-run helpers** | CLIs/scripts **when chartered** — human-invoked, logged | Engineering charter |
| **Runtime configuration bindings** | Concrete paths, `credential_ref` resolution **outside git** | Operator + charter |
| **Run logs & acquisition records** | Per-run telemetry for pilots — not normative architecture | `pilots/`, external storage |
| **Runtime engineering state** | Roadmap progress, implementation honesty | [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) |
| **Runtime pilots (execution)** | Execution artefacts for chartered pilots | `projects/ear-runtime/pilots/` |

---

## What Runtime does NOT own

| Area | Owner | Notes |
|------|-------|-------|
| **Architecture governance** | EAR Architecture (`shared/external-access-runtime/`) | Contracts, modes, tracks, connector **design**, gates |
| **Architecture amendments** | Human Architecture Amendment Charter | Not runtime team README edits |
| **Pilot charter & governance** | Architecture + [PILOT-GOVERNANCE-v1.md](../../shared/external-access-runtime/PILOT-GOVERNANCE-v1.md) | PILOT-001 charter lives in shared tree |
| **Consumer logic** | OCPilot, WPilot, Factory, etc. | Audit, diff, reports, deployment |
| **OCPilot decisions** | OCPilot program | Run 5 phases, findings, remediation |
| **Website Factory decisions** | Factory program | Production site policy |
| **Credential storage product** | Operator / external secret store | Runtime uses `credential_ref` only |
| **Autonomous orchestration** | Out of EAR v1 | No unattended production acquisition platform |
| **MARS survivability enforcement** | [projects/mars-survivability/](../mars-survivability/) | Complementary discipline — not EAR scope |

---

## Interface contract (Runtime ↔ Architecture)

| Direction | Rule |
|-----------|------|
| Architecture → Runtime | Backlog R1–R5 + contracts define **acceptance** |
| Runtime → Architecture | **No** silent contract changes; propose amendments via charter |
| Runtime → Consumers | **Published snapshots** and metadata only at boundary |
| Consumers → Runtime | **No** direct connector invocation |

---

## Storage and paths

| Concern | Owner |
|---------|-------|
| **Normative storage roles** | Architecture [EAR-STORAGE-MODEL-v1.md](../../shared/external-access-runtime/EAR-STORAGE-MODEL-v1.md) |
| **Concrete disk paths** | Operator — e.g. external bulk storage under `C:\AI MARS STORAGE\` per consumer registry |
| **Git repository** | MARS docs + future **source** under `projects/ear-runtime/runtime/` — **not** snapshot bulk |

---

## v1 platform focus

| Platform | Runtime v1 |
|----------|------------|
| **OpenCart** (OCPilot) | **In scope** — PILOT-001 / CON-L1-A |
| **WordPress** (WPilot) | **Out of scope** for implementation — documented future |
| **Other CMS** | **SAFE UNKNOWN** |

---

## Truth statement

Scope document describes **intended** ownership at Runtime Program foundation. **Nothing** listed under "owns" is implemented until [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) records otherwise.
