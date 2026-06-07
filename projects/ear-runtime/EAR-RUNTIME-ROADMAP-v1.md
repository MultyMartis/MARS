# EAR Runtime Roadmap v1

**Type:** Engineering roadmap — **no** implementation commitments or dates  
**Date:** 2026-06-02  
**Program:** EAR Runtime Program v1 — **STARTED**  
**Backlog authority:** [shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md)

---

## Roadmap principles

| Principle | Detail |
|-----------|--------|
| **Architecture-first** | Each phase implements frozen contracts — no parallel redesign |
| **Sequential core** | R1 → R2 → R3 → R4 dependency chain for connected OpenCart path |
| **HITL preserved** | Validate and Publish remain human-gated |
| **Pilot-gated execution** | Live SFTP only under PILOT Execution Authorization |
| **Honest status** | Phase "planned" ≠ "done" |

---

## Phase map

```
Foundation (DONE — 2026-06-02)
  Project placement · charter · scope · decision record
        │
        ▼
Phase 0 — Engineering Charter (DONE — 2026-06-02)
  EAR Runtime v1 Engineering Charter approved · Program STARTED
        │
        ▼
Phase 1 — R1 SFTP Read-Only Connector (IN PROGRESS — foundation only)
  R1.1 DONE · R1.2 DONE · R1.3 next
        │
        ▼
Phase 2 — R2 Evidence Package Generator
        │
        ▼
Phase 3 — R5 Validation Helpers (partial parallel OK after R2 stable)
        │
        ▼
Phase 4 — R3 Snapshot Builder
        │
        ▼
Phase 5 — R4 Snapshot Publisher
        │
        ▼
Phase 6 — PILOT-001 connected execution (separate Execution Authorization)
        │
        ▼
Horizon — WPilot / additional connectors (NOT v1 — architecture roadmap)
```

---

## Phase 0 — Engineering Charter (done)

| Item | Target |
|------|--------|
| **Deliverable** | Human-approved **EAR Runtime v1 Engineering Charter** |
| **Status** | **DONE** — 2026-06-02 |
| **Success** | [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) marks Program **STARTED** — **satisfied** |

---

## Phase 1 — R1: First SFTP Read-Only Connector

| Item | Target |
|------|--------|
| **Goal** | First Mode 2 connected helper — read-only SFTP per connector contract |
| **Reference path** | CON-L1-A |
| **First design consumer** | PILOT-001 (TEST, SITE-001) when execution authorized |
| **Out of scope** | SSH shell, FTP, PMA, DB, Hybrid, production hosts, writes |
| **Acceptance** | Contract-shaped status + artefact refs under human supervision — **no** publish claim |

**Architecture anchors:** [EAR-CONNECTOR-CONTRACT-v1.md](../../shared/external-access-runtime/EAR-CONNECTOR-CONTRACT-v1.md), [EAR-CONNECTOR-ARCHITECTURE-v1.md](../../shared/external-access-runtime/EAR-CONNECTOR-ARCHITECTURE-v1.md), [EAR-CREDENTIAL-BOUNDARY-v1.md](../../shared/external-access-runtime/EAR-CREDENTIAL-BOUNDARY-v1.md)

---

## Phase 2 — R2: Evidence Package Generator

| Item | Target |
|------|--------|
| **Goal** | Assemble Evidence Package from R1 output |
| **Inputs** | Connector artefacts + acquisition metadata |
| **Out of scope** | Consumer publish; autonomous redaction engine |
| **Acceptance** | Inspectable package traceable to connector run |

**Architecture anchor:** [EAR-EVIDENCE-PACKAGE-v1.md](../../shared/external-access-runtime/EAR-EVIDENCE-PACKAGE-v1.md)

---

## Phase 3 — R5: Validation Helpers

| Item | Target |
|------|--------|
| **Goal** | Human-operated Validate assistants |
| **Note** | May start after R2 output shape stable — may overlap R3/R4 with risk acceptance |
| **Out of scope** | Unattended certification; replacing human Validate sign-off |
| **Acceptance** | Operator can determine Publish allowance per gates |

**Architecture anchors:** [EAR-READINESS-GATES-v1.md](../../shared/external-access-runtime/EAR-READINESS-GATES-v1.md), [EAR-OPENCART-READINESS-CHECKLIST-v1.md](../../shared/external-access-runtime/EAR-OPENCART-READINESS-CHECKLIST-v1.md)

---

## Phase 4 — R3: Snapshot Builder

| Item | Target |
|------|--------|
| **Goal** | Candidate Snapshot Level 1 from validated evidence |
| **Quality** | Level 1 for PILOT-001 |
| **Out of scope** | Level 2+ completeness; auto-publish |
| **Acceptance** | Structural match to Level 1 spec; honest `safe-unknown` gaps |

**Architecture anchors:** [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](../../shared/external-access-runtime/EAR-OPENCART-SNAPSHOT-SPEC-v1.md), [EAR-SNAPSHOT-MAPPING-v1.md](../../shared/external-access-runtime/EAR-SNAPSHOT-MAPPING-v1.md)

---

## Phase 5 — R4: Snapshot Publisher

| Item | Target |
|------|--------|
| **Goal** | Publish gate + OCPilot-intake-compatible published reference |
| **Out of scope** | OCPilot Run 5; auto-publish without HITL |
| **Acceptance** | Immutable published version + publish log |

**Architecture anchors:** [EAR-SNAPSHOT-PUBLISHING-v1.md](../../shared/external-access-runtime/EAR-SNAPSHOT-PUBLISHING-v1.md), [EAR-READINESS-GATES-v1.md](../../shared/external-access-runtime/EAR-READINESS-GATES-v1.md) G4

---

## Phase 6 — PILOT-001 connected execution (gated)

| Item | Target |
|------|--------|
| **Goal** | End-to-end connected acquisition for SITE-001 under pilot governance |
| **Prerequisites** | R1–R4 sufficient for pilot scope; **Execution Authorization** |
| **Architecture pilot package** | [pilots/PILOT-001-SITE-001-SFTP-READONLY/](../../shared/external-access-runtime/pilots/PILOT-001-SITE-001-SFTP-READONLY/) |
| **Not implied** | Completing R1–R5 does not authorize live access |

---

## Horizon (not v1 roadmap commitments)

| Item | Program |
|------|---------|
| WordPress / WPilot Mode 2 connectors | Future architecture + runtime charter |
| Additional connector classes (FTP, PMA, DB) | Architecture amendment first |
| Unified snapshot schema v2 | Post–v1 lessons |
| Website Factory acquisition | **SAFE UNKNOWN** |

---

## Truth statement

This roadmap is **planning only**. No phase is **DONE** until recorded in [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) with evidence (e.g. charter, merged implementation, pilot report).
