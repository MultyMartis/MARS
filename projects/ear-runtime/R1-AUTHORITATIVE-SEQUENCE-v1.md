# R1 — Authoritative Execution Sequence v1

**Type:** Phase authority record — reconciles task index drift (PC-07)  
**Date:** 2026-06-04  
**Supersedes for execution order:** Phase numbering in [R1-IMPLEMENTATION-TASKS-v1.md](R1-IMPLEMENTATION-TASKS-v1.md) § Task overview (2026-06-02 original index)  
**Does not rename:** Completed deliverable filenames (`R1.3-CONNECTION-LAYER-SKELETON-v1.md`, etc.)  
**Does not rewrite:** Historical milestone reports or gate decisions (R1.8A–R1.8C remain as recorded)

---

## Purpose

Provide a **single authoritative execution order** for the EAR Runtime R1 program after architecture-led sub-phases R1.8A–R1.8D. Resolves **PC-07** (task index drift between original implementation tasks and executed engineering phases).

---

## Authority rules

| Rule | Detail |
|------|--------|
| **Execution authority** | This document + [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) |
| **Historical task catalog** | [R1-IMPLEMENTATION-TASKS-v1.md](R1-IMPLEMENTATION-TASKS-v1.md) — preserved; see § Legacy mapping |
| **Architecture backlog** | [shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) — R1–R5 program phases |
| **R1.8 meaning (current)** | **Persistence Model** — Store-stage binding and bounded persistence implementation; **not** original task “Failures / logging” |
| **Suffix letters (A–D)** | Architecture / kickoff sub-phases only; **not** implementation tasks |

---

## Authoritative sequence (executed → next)

| Order | Phase ID | Name | Status | Evidence |
|------:|----------|------|--------|----------|
| 1 | **R1.1** | Runtime Skeleton | **DONE** | [R1.1-FOUNDATION-STATE-v1.md](R1.1-FOUNDATION-STATE-v1.md) |
| 2 | **R1.2** | Config Input Model | **DONE** | [R1.2-CONFIG-INPUT-MODEL-v1.md](R1.2-CONFIG-INPUT-MODEL-v1.md) |
| 3 | **R1.3** | Connection Layer Skeleton | **DONE** | [R1.3-CONNECTION-LAYER-SKELETON-v1.md](R1.3-CONNECTION-LAYER-SKELETON-v1.md) |
| 4 | **R1.4** | Remote Listing Model | **DONE** | [R1.4-REMOTE-LISTING-MODEL-v1.md](R1.4-REMOTE-LISTING-MODEL-v1.md) |
| 5 | **R1.5** | Manifest Builder Skeleton | **DONE** | [R1.5-MANIFEST-BUILDER-SKELETON-v1.md](R1.5-MANIFEST-BUILDER-SKELETON-v1.md) |
| 6 | **R1.6** | Evidence Package Model | **DONE** | [R1.6-EVIDENCE-PACKAGE-MODEL-v1.md](R1.6-EVIDENCE-PACKAGE-MODEL-v1.md) |
| 7 | **R1.7** | Snapshot Package Model | **DONE** | [R1.7-SNAPSHOT-PACKAGE-MODEL-v1.md](R1.7-SNAPSHOT-PACKAGE-MODEL-v1.md) |
| 8 | **R1.8A** | Persistence Design Review | **DONE** | [R1.8A-PERSISTENCE-DESIGN-REVIEW-v1.md](R1.8A-PERSISTENCE-DESIGN-REVIEW-v1.md) |
| 9 | **R1.8B** | Snapshot Storage Contract | **DONE** | [R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md](R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md) |
| 10 | **R1.8C** | Persistence Layout Charter | **DONE** | [R1.8C-PERSISTENCE-LAYOUT-CHARTER-v1.md](R1.8C-PERSISTENCE-LAYOUT-CHARTER-v1.md) |
| 11 | **R1.8D** | Persistence Kickoff Charter | **DONE** | [R1.8D-PERSISTENCE-KICKOFF-CHARTER-v1.md](R1.8D-PERSISTENCE-KICKOFF-CHARTER-v1.md) |
| 12 | **R1.8** | Persistence Model | **NEXT** | [R1.8D-PERSISTENCE-KICKOFF-DECISION-v1.md](R1.8D-PERSISTENCE-KICKOFF-DECISION-v1.md) |

---

## What **R1.8** means (post-review)

| Aspect | Definition |
|--------|------------|
| **Program name** | R1.8 — **Persistence Model** |
| **Goal** | Bind in-memory pipeline (`Listing` → `Manifest` → `Evidence` → `SnapshotPackage`) to chartered Store layout; production `snapshot_id` policy; Store-state metadata; **dry_run-gated** external writers |
| **Inputs** | R1.8B storage contract, R1.8C layout charter, R1.7 `SnapshotPackage`, operator `output_root` / `acquisition_id` |
| **Predecessors** | R1.1–R1.7 (mock pipeline), R1.8A–R1.8D (architecture + kickoff) |
| **Not the same as** | Original [R1-IMPLEMENTATION-TASKS-v1.md](R1-IMPLEMENTATION-TASKS-v1.md) row **R1.8 — Failures / logging** (deferred — see legacy mapping) |

---

## Deferred work (still required for full R1 connector — not renumbered)

Original implementation tasks **not yet executed** under executed phase IDs. Track here; do not confuse with **R1.8 Persistence Model**.

| Legacy task ID | Original name | Disposition | Notes |
|----------------|---------------|-------------|-------|
| R1.3 (full) | SFTP connection test mode | **DEFERRED** | R1.3 skeleton done; live `test-connection` not implemented |
| R1.5 (full) | Exclusion engine | **DEFERRED** | Partial coverage in manifest mock; defaults engine not shipped |
| R1.8 (legacy) | Failures / logging | **DEFERRED** → assign **R1.8L** when scheduled | Renumbered label only; no deliverable rename |
| R1.9 | Dry-run local test | **DEFERRED** | CI mock E2E not chartered as phase yet |
| R1.10 | Pilot preflight | **DEFERRED** | Requires PILOT Execution Authorization |

**Label R1.8L** = legacy “Failures / logging” task — use when that work is scheduled to avoid collision with **R1.8 Persistence Model**.

---

## Drift evidence table (PC-07)

| Drift type | Source A | Source B | Resolution |
|------------|----------|----------|------------|
| **R1.8 naming** | Tasks: Failures / logging | State/Index: Persistence Model | **R1.8** = Persistence Model; legacy → **R1.8L** |
| **R1.3 naming** | Tasks: SFTP connection test | Deliverable: Connection Layer Skeleton | Deliverable name **frozen**; full SFTP test **deferred** |
| **R1.6 vs R1.7** | Tasks: R1.6 manifest, R1.7 evidence writer | Executed: R1.5 manifest, R1.6 evidence, R1.7 snapshot | **Executed IDs authoritative**; tasks table is historical |
| **Missing R1.7 in tasks** | Tasks jump R1.6 → R1.7 evidence writer | Executed R1.7 = Snapshot Package Model | Snapshot model inserted in execution path; tasks index stale |
| **R1.8A–D not in tasks** | Tasks list R1.8–R1.10 only | Eight sub-phases after R1.7 | Sub-phases documented in this sequence; not in 2026-06-02 task table |
| **Roadmap Phase 1** | [EAR-RUNTIME-ROADMAP-v1.md](EAR-RUNTIME-ROADMAP-v1.md): “R1.3 next” | State: R1.3–R1.8C done | Roadmap diagram **stale** — trust this doc + STATE |
| **Tasks truth statement** | “No code exists” | `runtime/` exists R1.1–R1.7 | Tasks doc historical; see [R1-IMPLEMENTATION-TASKS-v1.md](R1-IMPLEMENTATION-TASKS-v1.md) reconciliation header |
| **Backlog R1 status** | “connector NOT STARTED” | Skeleton + mock models exist | [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) authoritative |
| **OPERATIONAL-INDEX triggers** | “next: R1.6” on R1.3–R1.5 | R1.6+ done | Triggers updated in OPERATIONAL-INDEX (2026-06-04 R1.8D pass) |

---

## PC-07 resolution

| Blocker | Status |
|---------|--------|
| **PC-07** R1-IMPLEMENTATION-TASKS reconciled with executed R1.4–R1.8 sequence | **RESOLVED** — this document is authoritative for execution order |

---

## Related documents

| Document | Use |
|----------|-----|
| [R1.8D-PERSISTENCE-KICKOFF-CHARTER-v1.md](R1.8D-PERSISTENCE-KICKOFF-CHARTER-v1.md) | R1.8 scope, bounds, success criteria |
| [R1-IMPLEMENTATION-TASKS-v1.md](R1-IMPLEMENTATION-TASKS-v1.md) | Legacy task catalog + reconciliation pointer |
| [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) | Honest implementation status |

---

## Truth statement

This document is **architecture reconciliation only**. It does not implement persistence, create directories, or authorize live acquisition.
