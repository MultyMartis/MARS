# EAR Lessons Learned v1

**Type:** Architecture-phase retrospective — **no** execution or connector lessons  
**Date:** 2026-06-01  
**Scope:** Phases 1–6 documentation program

---

## What this document is not

- Not a post-mortem of live SFTP acquisition (none performed under EAR runtime).
- Not connector implementation feedback (no connector code in repo).
- PILOT-001 [LESSONS-LEARNED.md](../../pilots/PILOT-001-SITE-001-SFTP-READONLY/LESSONS-LEARNED.md) remains the **pilot-local** log for future execution notes.

---

## Structural lessons

| Lesson | Implication for Runtime v1 |
|--------|----------------------------|
| **Separate acquisition from consumer analysis** | EAR produces snapshots; OCPilot consumes — do not merge roles in one tool |
| **Evidence Package ≠ Snapshot** | Runtime must preserve quarantine → Validate → Publish separation ([EAR-EVIDENCE-PACKAGE-v1.md](../../EAR-EVIDENCE-PACKAGE-v1.md)) |
| **Honest snapshot levels** | Do not publish Level 2+ without mapped evidence — fail closed ([EAR-SNAPSHOT-PUBLISHING-v1.md](../../EAR-SNAPSHOT-PUBLISHING-v1.md)) |
| **Two tracks are permanent** | Offline Archive First and Connected Managed Project are not “phases to merge” ([EAR-ACQUISITION-TRACKS-v1.md](../../EAR-ACQUISITION-TRACKS-v1.md)) |
| **Mode 2 is the v1 target** | Mode 0–1 remain valid; Mode 3 stays out of scope |

---

## Process lessons

| Lesson | Implication |
|--------|-------------|
| **OPERATIONAL-INDEX vs EAR-ROADMAP phase numbers diverge** | Runtime charter must name which numbering it follows; prefer OPERATIONAL-INDEX for EAR operational phases |
| **CONDITIONAL GO is useful** | Distinguishes “ready to engineer” from “ready to execute live access” |
| **Pilot lifecycle gates prevent drift** | Charter ≠ Sub-Charter ≠ Execution ([PILOT-GOVERNANCE-v1.md](../../PILOT-GOVERNANCE-v1.md)) |
| **SAFE UNKNOWN is preferable to invented paths** | Phase 6 sub-charter placeholders avoided false operational truth |
| **Phase deliverables stay documentation-only** | Each phase explicitly stated no code — reduced status inflation |

---

## Design lessons

| Lesson | Implication |
|--------|-------------|
| **Connector contract before implementation** | Runtime implements [EAR-CONNECTOR-CONTRACT-v1.md](../../EAR-CONNECTOR-CONTRACT-v1.md) — do not redesign I/O in code first |
| **Credential boundary early** | `credential_ref` only; secrets never in git ([EAR-CREDENTIAL-BOUNDARY-v1.md](../../EAR-CREDENTIAL-BOUNDARY-v1.md)) |
| **Default exclusions are policy** | Cache/runtime paths excluded by default — [EAR-DEFAULT-EXCLUSIONS-v1.md](../../EAR-DEFAULT-EXCLUSIONS-v1.md) |
| **Partial storage model is acceptable at freeze** | Conceptual roles defined; concrete paths bound at pilot sign-off |
| **First connector: SFTP Read-Only** | Phase 3 and PILOT-001 aligned on CON-L1-A — defer Hybrid/PMA-only pilots |

---

## Cross-program lessons

| Lesson | Source |
|--------|--------|
| Pre-runtime bridge informed SITE-001 | [projects/ocpilot/freeze/site-001-pre-runtime-bridge/](../../../../projects/ocpilot/freeze/site-001-pre-runtime-bridge/) |
| External access patterns complement EAR | [shared/external-access-patterns/](../../external-access-patterns/) — human gates per channel |
| Consumer Run 5 pause is expected | OCPilot waits for honest Level 1 snapshot path — not an EAR architecture gap |

---

## Anti-patterns observed (documentation phase)

| Anti-pattern | Corrective |
|--------------|------------|
| Claiming “runtime ready” because docs exist | Use **CONDITIONAL GO** and separate Execution Authorization |
| Expanding pilot scope in sub-charter | Sub-charter must not exceed charter exclusions |
| Downloading cache/logs by default | Exclusions policy + manifest metadata |
| Storing secrets in MARS git | External credential store only |

---

## Carry-forward to Runtime Engineering

1. Implement **smallest** Mode 2 path: SFTP Read-Only → Evidence → Snapshot Level 1 for PILOT-001.
2. Preserve **human HITL** at Request, Validate, Publish, Execution.
3. Do not reopen connector **architecture** unless amendment charter — use [EAR-RUNTIME-BOUNDARY-v1.md](../../EAR-RUNTIME-BOUNDARY-v1.md).
4. Record execution lessons in pilot LESSONS-LEARNED — not in architecture freeze folder.
