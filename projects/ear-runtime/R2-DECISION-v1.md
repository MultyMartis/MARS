# R2 Decision v1

**Type:** Charter gate decision — R2 Evidence Package Layer  
**Date:** 2026-06-04  
**Charter:** [R2-CHARTER-v1.md](R2-CHARTER-v1.md)  
**Prior decision:** [R2-PLANNING-DECISION-v1.md](R2-PLANNING-DECISION-v1.md) — **APPROVED WITH NOTES** (planning → charter)

---

## Decision

| Field | Value |
|-------|-------|
| **Question** | May **R2 Charter** close and **R2 Implementation Charter** phase proceed? |
| **Outcome** | **APPROVED WITH NOTES** |
| **Scope of approval** | R2 mission, scope, non-goals, Evidence Package Contract, Evidence Quarantine Charter, success/stop criteria, and boundaries per [R2-CHARTER-v1.md](R2-CHARTER-v1.md) |
| **Explicitly not approved by this decision** | R2 runtime code, live acquisition, SFTP execution, snapshot section expansion, Publish, OCPilot integration, persistence redesign |

---

## Rationale

1. **Planning gate satisfied** — [R2-PLANNING-REVIEW-v1.md](R2-PLANNING-REVIEW-v1.md) and [R2-PLANNING-DECISION-v1.md](R2-PLANNING-DECISION-v1.md) define R2 as **Evidence Package Generator**, not OpenCart section expansion; gap matrix is evidence-backed.
2. **Authoritative mission aligned** — [EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) § R2 and [EAR-EVIDENCE-PACKAGE-v1.md](../../shared/external-access-runtime/EAR-EVIDENCE-PACKAGE-v1.md) match charter scope (identity, provenance, scope echo, artifact index, connector status, quarantine).
3. **Dependency chain preserved** — `R1 → R2 → R3`; file-manifest and L1 sections deferred to R3 per planning notes N-01, N-02.
4. **Store boundary respected** — R1.9 complete; R2 charters `evidence/` only; does not redesign mock snapshot Store ([R1.8E-PERSISTENCE-DECISION-v1.md](R1.8E-PERSISTENCE-DECISION-v1.md)).
5. **Consumer and pilot boundaries explicit** — Publish/OCPilot/SITE-001/SFTP out of scope per planning decision and charter non-goals.

**APPROVED WITH NOTES** (not bare **APPROVED**): implementation charter must carry planning notes; **R2 code implementation remains NOT AUTHORIZED** until R2 Implementation Charter and human decision per [R1-IMPLEMENTATION-DECISION-v1.md](R1-IMPLEMENTATION-DECISION-v1.md) pattern.

**NOT APPROVED** would apply if charter contradicted backlog (e.g. chartered OpenCart sections as R2) or omitted evidence/snapshot boundary — neither condition holds.

---

## Notes (carried to R2 Implementation Charter)

| Note | Action |
|------|--------|
| N-01 | Title implementation work **R2 — Evidence Package Generator**; not “snapshot sections” |
| N-02 | Defer File Manifest Expansion and L1 OpenCart sections to **R3** |
| N-03 | Maintain **Level 0** honest quality on mock snapshot persist until R3 |
| N-04 | **Publish** and OCPilot intake remain **R4** / consumer |
| N-05 | Live acquisition, SFTP, SITE-001 — PILOT Execution Authorization only |
| N-06 | Human implementation approval gate — R2 Implementation Charter does not bypass R1 gate pattern |
| N-07 | Exact `evidence/` on-disk index file names — resolve at implementation charter (**SAFE UNKNOWN** at R2 Charter) |

---

## Evidence

| # | Evidence | Location |
|---|----------|----------|
| D-R2-01 | R2 planning review — gap matrix, recommended scope | [R2-PLANNING-REVIEW-v1.md](R2-PLANNING-REVIEW-v1.md) |
| D-R2-02 | Planning kickoff — APPROVED WITH NOTES | [R2-PLANNING-DECISION-v1.md](R2-PLANNING-DECISION-v1.md) |
| D-R2-03 | Evidence package semantics | [EAR-EVIDENCE-PACKAGE-v1.md](../../shared/external-access-runtime/EAR-EVIDENCE-PACKAGE-v1.md) |
| D-R2-04 | Lifecycle Acquire → Validate → Store | [EAR-SNAPSHOT-LIFECYCLE-v1.md](../../shared/external-access-runtime/EAR-SNAPSHOT-LIFECYCLE-v1.md) |
| D-R2-05 | Storage roles and quarantine | [EAR-STORAGE-MODEL-v1.md](../../shared/external-access-runtime/EAR-STORAGE-MODEL-v1.md) |
| D-R2-06 | Evidence path + PC-08 retention | [R1.8C-PERSISTENCE-LAYOUT-CHARTER-v1.md](R1.8C-PERSISTENCE-LAYOUT-CHARTER-v1.md) |
| D-R2-07 | Evidence persist deferred | [R1.8E-PERSISTENCE-DECISION-v1.md](R1.8E-PERSISTENCE-DECISION-v1.md) |
| D-R2-08 | Backlog R2 definition | [EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) |
| D-R2-09 | R2 Charter artifact | [R2-CHARTER-v1.md](R2-CHARTER-v1.md) |

---

## Gate transition

| Gate | Before R2 Charter | After R2 Charter |
|------|-------------------|------------------|
| R2 Planning Review | **DONE** | **DONE** |
| R2 Charter | **READY** | **COMPLETE** |
| R2 Implementation Charter | **READY** | **NEXT** — authorized to draft |
| R2 Implementation (code) | **NOT AUTHORIZED** | **NOT AUTHORIZED** until Implementation Charter + human decision |

---

## Sign-off record

| Role | Record |
|------|--------|
| Charter executor | Agent architecture charter 2026-06-04 |
| Human implementation approval | **PENDING** (R2 Implementation Charter) |
