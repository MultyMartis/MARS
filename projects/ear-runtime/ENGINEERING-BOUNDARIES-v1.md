# EAR Runtime Engineering Boundaries v1

**Type:** Runtime engineering boundary definition  
**Date:** 2026-06-02  
**Charter:** [ENGINEERING-CHARTER-v1.md](ENGINEERING-CHARTER-v1.md)  
**Architecture authority:** [shared/external-access-runtime/EAR-RUNTIME-BOUNDARY-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BOUNDARY-v1.md)

---

## Purpose

Define what the EAR Runtime Engineering Program **owns** and **does not own** so implementation work stays within chartered scope and does not drift into architecture governance or consumer logic.

This document **implements** the runtime-side view of the architecture boundary. Normative layer definitions remain in the architecture tree.

---

## Runtime owns

| Area | Description | Backlog |
|------|-------------|---------|
| **Connector execution** | Human-operated Mode 2 read-only SFTP acquisition per connector contract | R1 |
| **Evidence generation** | Assemble Evidence Packages from connector output; quarantine-bound paths | R2 |
| **Snapshot generation** | Build candidate Snapshot Level 1 packages from validated evidence | R3 |
| **Validation helpers** | Human-operated Validate assistants — checklists, structural checks, gate reminders | R5 |
| **Publishing helpers** | Apply Publish gate; produce consumer-visible immutable snapshot references | R4 |
| **Operator-run tooling** | CLIs and helpers when separately chartered — explicit invocation, logged runs | Engineering charter per item |
| **Runtime configuration bindings** | Concrete paths, `credential_ref` resolution **outside git** | Operator + charter |
| **Run logs and acquisition records** | Per-run telemetry for pilots — not normative architecture | `pilots/`, external storage |
| **Runtime engineering state** | Roadmap progress, implementation honesty | [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) |
| **Runtime pilot execution artefacts** | Execution outputs for chartered pilots | `projects/ear-runtime/pilots/` |

---

## Runtime does NOT own

| Area | Owner | Notes |
|------|-------|-------|
| **Architecture governance** | EAR Architecture (`shared/external-access-runtime/`) | Contracts, modes, tracks, connector **design**, readiness gates, pilot charters |
| **Architecture amendments** | Human Architecture Amendment Charter | Not runtime README or code comment drift |
| **Consumer decisions** | OCPilot, WPilot, Factory, Landing Pilot, etc. | What to do with published snapshots |
| **OCPilot logic** | OCPilot program | Audit diffs, Run 5 phases, findings, remediation |
| **WPilot logic** | WPilot program | WordPress-specific analysis and operations |
| **Website Factory logic** | Website Factory program | Production site policy and deployment |
| **Credential vault systems** | Operator / external secret store | Runtime uses `credential_ref` only — no vault product |
| **Production automation** | Out of EAR v1 scope | No unattended acquisition platform, cron jobs, or CI-driven live access without separate ops charter |
| **Pilot charter and governance** | Architecture + [PILOT-GOVERNANCE-v1.md](../../shared/external-access-runtime/PILOT-GOVERNANCE-v1.md) | PILOT-001 charter lives in shared tree |
| **MARS survivability enforcement** | [projects/mars-survivability/](../mars-survivability/) | Complementary discipline — not EAR runtime scope |

---

## Layer diagram

```
┌─────────────────────────────────────────────────────────────┐
│  EAR ARCHITECTURE (FROZEN)                                   │
│  shared/external-access-runtime/                             │
│  Contracts · workflows · gates · pilot governance            │
└──────────────────────────┬──────────────────────────────────┘
                           │ implements (must conform)
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  EAR RUNTIME (THIS PROJECT — ENGINEERING STARTED)            │
│  projects/ear-runtime/                                       │
│  Connectors · evidence · snapshots · validate · publish      │
└──────────────────────────┬──────────────────────────────────┘
                           │ produces (when authorized)
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  CONSUMERS (e.g. OCPilot)                                    │
│  Analysis · operations — not runtime                         │
└─────────────────────────────────────────────────────────────┘
```

---

## Interface rules

| Direction | Rule |
|-----------|------|
| Architecture → Runtime | Backlog R1–R5 + contracts define **acceptance** |
| Runtime → Architecture | **No** silent contract changes; propose amendments via charter |
| Runtime → Consumers | **Published snapshots** and metadata only at boundary |
| Consumers → Runtime | **No** direct connector invocation |

---

## Quick decision table

| Question | Owner |
|----------|-------|
| Should SFTP Read-Only connector use `credential_ref` only? | Architecture (decided) — runtime implements |
| Which SFTP library to use? | Runtime — R1 Implementation Readiness Review |
| Is Snapshot Level 1 honest for partial manifest? | Architecture — runtime + human Validate enforce |
| Where to store bulk downloads? | Runtime binding (operator paths) within storage model roles |
| Authorize live PILOT-001 session | Pilot Execution Authorization — separate gate |
| Run OCPilot audit diff on snapshot | OCPilot — not runtime |

---

## Truth statement

Boundary definitions do not imply any implementation exists. All runtime areas listed under "Runtime owns" remain **unimplemented** at engineering charter approval.
