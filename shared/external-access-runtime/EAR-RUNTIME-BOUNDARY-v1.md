# EAR Runtime Boundary v1

**Type:** Layer boundary definition — anti–architecture-creep guard  
**Date:** 2026-06-01  
**Effective:** Runtime Transition Freeze onward

---

## Purpose

Define where **EAR Architecture** ends and **EAR Runtime** begins so future work does not silently expand design scope while implementing helpers, and so architecture docs remain the **stable contract** for runtime behavior.

---

## Two layers

```
┌─────────────────────────────────────────────────────────────┐
│  EAR ARCHITECTURE LAYER (FROZEN — amendment by charter only) │
│  Contracts · workflows · modes · tracks · connector design   │
│  Snapshot spec · governance · pilot charters                 │
└──────────────────────────────┬──────────────────────────────┘
                               │ implements (must conform)
                               ▼
┌─────────────────────────────────────────────────────────────┐
│  EAR RUNTIME LAYER (engineering — not started at freeze)     │
│  Connectors · evidence assembly · snapshot build/publish     │
│  Validation helpers · operator-run tooling                     │
└──────────────────────────────┬──────────────────────────────┘
                               │ produces (when authorized)
                               ▼
┌─────────────────────────────────────────────────────────────┐
│  CONSUMERS (e.g. OCPilot) — analysis / operations            │
│  Not part of EAR runtime                                     │
└─────────────────────────────────────────────────────────────┘
```

---

## Architecture layer — what it is

| In scope | Examples |
|----------|----------|
| **Normative design** | [EAR-ARCHITECTURE-v1.md](EAR-ARCHITECTURE-v1.md), connector architecture, acquisition tracks |
| **Contracts** | Snapshot contract, connector contract, credential boundary |
| **Workflows and gates** | Acquisition workflow, lifecycle, readiness gates, publishing rules |
| **Policies** | Security model, default exclusions, non-goals, failure models |
| **Pilot governance** | Pilot charters, sub-charters, governance, stop conditions |
| **Readiness assessments** | Phase 3 assessment, freeze package |
| **Examples** | SITE-001 workflow example — illustrative |

**Authority:** Human architecture program + explicit **Architecture Amendment Charter** for changes after freeze.

**Location:** Primarily `shared/external-access-runtime/*.md` and `freeze/EAR-RUNTIME-TRANSITION-v1/`.

---

## Architecture layer — what it is not

| Out of scope | Belongs to |
|--------------|------------|
| SFTP/SSH client code | Runtime |
| Transfer scripts, cron, CI jobs | Runtime / ops charter |
| Live credential use | Runtime + Execution Authorization |
| OCPilot diff engine | OCPilot consumer |
| Autonomous orchestration platform | Out of EAR v1 non-goals |

---

## Runtime layer — what it is

| In scope | Backlog reference |
|----------|-------------------|
| **Connector implementations** | R1 — SFTP Read-Only |
| **Evidence assembly tooling** | R2 |
| **Snapshot build tooling** | R3 |
| **Publish tooling** | R4 |
| **Validate assistants** | R5 |
| **Operator-run CLIs/helpers** | Runtime charter |
| **Concrete path bindings** | Operator config external to git |
| **Run logs and acquisition records** | Runtime / pilot artifacts (not architecture) |

**Authority:** **EAR Runtime v1 Engineering Charter** (human) + pilot Execution Authorization for live access.

**Constraint:** Runtime **must conform** to architecture contracts — not redefine them in code comments or README drift.

---

## Runtime layer — what it is not

| Out of scope | Notes |
|--------------|-------|
| Changing snapshot level semantics | Architecture amendment |
| Adding Mode 3 or write connectors | Forbidden v1 — charter required |
| Replacing HITL gates with full automation | Against security model |
| Consumer analysis logic | OCPilot / WPilot |
| New acquisition tracks | Architecture amendment |

---

## Where architecture ends (freeze line)

Architecture program is **COMPLETE** when:

1. Phases 1, 2A–2E, 3, 4, 5, 6 deliverables exist per [EAR-PHASE-CLOSEOUT-v1.md](EAR-PHASE-CLOSEOUT-v1.md).
2. [freeze/EAR-RUNTIME-TRANSITION-v1/](freeze/EAR-RUNTIME-TRANSITION-v1/) freeze package is published.
3. [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) marks **EAR Architecture Program: COMPLETE**.

**After this line:** New markdown in `shared/external-access-runtime/` that **changes normative behavior** is architecture work and requires **Architecture Amendment Charter** — not a routine runtime PR.

**Allowed without amendment:**

- Runtime code repos/folders chartered separately
- Pilot status updates, execution logs, lessons learned in pilot folders
- Typos and cross-links that do not change normative meaning
- Runtime engineering charters and reports

---

## Where runtime begins

Runtime program **starts** when:

1. **EAR Runtime v1 Engineering Charter** is human-approved, and  
2. At least one backlog item ([EAR-RUNTIME-BACKLOG-v1.md](EAR-RUNTIME-BACKLOG-v1.md)) is in active implementation.

Runtime **does not** begin merely because freeze docs exist.

---

## Decision table (quick reference)

| Question | Layer |
|----------|-------|
| Should SFTP Read-Only connector expose `credential_ref` only? | Architecture (already decided) — runtime implements |
| Which library for SFTP? | Runtime charter |
| Is Snapshot Level 1 honest for partial manifest? | Architecture — runtime + human Validate enforce |
| Where to store bulk downloads? | Runtime binding (operator paths) within storage model roles |
| Add WordPress connector class definition | Architecture amendment |
| Implement WordPress connector code | Runtime (future charter) |
| Authorize live PILOT-001 session | Pilot Execution Authorization — not architecture |
| Add new default exclusion path | Architecture policy update (this doc version bump) or pilot Request |

---

## Anti–architecture-creep rules

1. **No “small design doc”** to justify runtime shortcuts that contradict contracts.  
2. **No new phase 2F** without amendment — use backlog or runtime charter.  
3. **Freeze package is historical truth** — supersede via new freeze version + amendment, not silent edits.  
4. **OPERATIONAL-INDEX** tracks program status — architecture vs runtime programs are separate rows.

---

## Related documents

| Document | Role |
|----------|------|
| [EAR-NON-GOALS-v1.md](EAR-NON-GOALS-v1.md) | Permanent outs |
| [EAR-RUNTIME-BACKLOG-v1.md](EAR-RUNTIME-BACKLOG-v1.md) | Runtime work units |
| [freeze/EAR-RUNTIME-TRANSITION-v1/EAR-RUNTIME-HANDOFF-v1.md](freeze/EAR-RUNTIME-TRANSITION-v1/EAR-RUNTIME-HANDOFF-v1.md) | Handoff assets |
| [PILOT-GOVERNANCE-v1.md](PILOT-GOVERNANCE-v1.md) | Pilot vs runtime vs execution |
