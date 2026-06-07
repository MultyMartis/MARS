# R3 Decision v1

**Type:** Charter gate decision — R3 Snapshot Assembly Layer  
**Date:** 2026-06-05  
**Charter:** [R3-CHARTER-v1.md](R3-CHARTER-v1.md)  
**Prior decision:** [R2-READINESS-DECISION-v1.md](R2-READINESS-DECISION-v1.md) — **READY FOR R3 WITH NOTES**

---

## Decision

| Field | Value |
|-------|-------|
| **Question** | May **R3 Charter** close and **R3 Implementation Charter** phase proceed? |
| **Outcome** | **APPROVED WITH NOTES** |
| **Scope of approval** | R3 mission, scope, non-goals, Snapshot Package Contract, identity continuity, ownership boundaries, R3→R5 boundary, success/stop criteria per [R3-CHARTER-v1.md](R3-CHARTER-v1.md) |
| **Explicitly not approved by this decision** | R3 runtime code, snapshot builder implementation, Store redesign, Validate automation, Publish, OCPilot integration, live acquisition, SITE-001 / PILOT execution |

---

## Rationale

1. **R2 readiness gate satisfied** — [R2-READINESS-DECISION-v1.md](R2-READINESS-DECISION-v1.md) authorizes R3 Charter; R2.1–R2.7 architecture contracts complete; R2.6 handoff spec is authoritative input for R3.

2. **Authoritative mission aligned** — [EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) § R3 defines Snapshot Builder as candidate Level 1 assembly from validated evidence shape; charter correctly positions R3 as transformation layer before R5 Validate.

3. **Pipeline contract explicit** — `R2 Evidence → R3 Assembly → R5 Validate → R4 Publish` documented; no bypass of Validate or Publish gates.

4. **Boundary preservation** — R3 does not redesign Store (R1.9 frozen), does not mutate evidence (R2 owns), does not certify quality (R5 owns), does not publish (R4 owns). Matches R2.6 HO-* invariants.

5. **OpenCart spec used without redesign** — Section classification Required/Optional/Future follows [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](../../shared/external-access-runtime/EAR-OPENCART-SNAPSHOT-SPEC-v1.md) and [EAR-OPENCART-QUALITY-MAPPING-v1.md](../../shared/external-access-runtime/EAR-OPENCART-QUALITY-MAPPING-v1.md).

6. **R2 debt acknowledged** — Quarantine persist (IAC-03), HandoffContract code, R1.6 migration carried as notes — not blockers for charter per R2 readiness decision.

**APPROVED WITH NOTES** (not bare **APPROVED**): Implementation charter must carry R2 readiness notes and R2 debt; **R3 code implementation remains NOT AUTHORIZED** until R3 Implementation Charter and human gate per R1/R2 pattern.

**REJECTED** would apply if charter contradicted backlog (e.g. chartered Publish as R3), omitted R3→R5 boundary, or merged evidence into snapshot tree — **none apply**.

---

## Notes (carried to R3 Implementation Charter)

| Note | Action |
|------|--------|
| N-R3-01 | Title implementation work **R3 — Snapshot Assembly** / Snapshot Builder — not Validate or Publish |
| N-R3-02 | First implementation consumes `evidence_package_models.EvidencePackage` — deprecate R1.6 at snapshot boundary |
| N-R3-03 | Candidate `package_quality_level: 0` default until R5 certifies possession |
| N-R3-04 | Retain `--contract-evidence` and R1.6 mock paths until R3 chain wired — no unsafe deletion |
| N-R3-05 | Quarantine persist (D-R2-01) — schedule in Implementation Charter or R3-adjacent milestone |
| N-R3-06 | Implement `HandoffContract` code module — deferred from R2.6 |
| N-R3-07 | Disambiguate **Validate** (R5 EAR Validate) vs R2 structural validation in all R3 docs |
| N-R3-08 | Per-section field mapping detail — resolve at Implementation Charter (**SAFE UNKNOWN** at R3 Charter) |
| N-R3-09 | Live acquisition, SFTP, SITE-001 — Execution Authorization only |
| N-R3-10 | Human implementation approval gate — R3 Implementation Charter does not bypass R1/R2 gate pattern |

---

## Evidence

| # | Evidence | Location |
|---|----------|----------|
| D-R3-01 | R2 readiness review — R3 entry assessment | [R2-READINESS-REVIEW-v1.md](R2-READINESS-REVIEW-v1.md) |
| D-R3-02 | R2 closure — READY FOR R3 WITH NOTES | [R2-READINESS-DECISION-v1.md](R2-READINESS-DECISION-v1.md) |
| D-R3-03 | Evidence → Snapshot handoff | [R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md](R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md) |
| D-R3-04 | OpenCart snapshot spec | [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](../../shared/external-access-runtime/EAR-OPENCART-SNAPSHOT-SPEC-v1.md) |
| D-R3-05 | Quality level mapping | [EAR-OPENCART-QUALITY-MAPPING-v1.md](../../shared/external-access-runtime/EAR-OPENCART-QUALITY-MAPPING-v1.md) |
| D-R3-06 | Storage roles | [EAR-STORAGE-MODEL-v1.md](../../shared/external-access-runtime/EAR-STORAGE-MODEL-v1.md) |
| D-R3-07 | Snapshot storage contract | [R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md](R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md) |
| D-R3-08 | Backlog R3 definition | [EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) |
| D-R3-09 | R3 Charter artifact | [R3-CHARTER-v1.md](R3-CHARTER-v1.md) |

---

## Gate transition

| Gate | Before R3 Charter | After R3 Charter |
|------|-------------------|------------------|
| R2 Readiness Review | **COMPLETE** | **COMPLETE** |
| R3 Charter | **READY** | **COMPLETE** |
| R3 Implementation Charter | **NOT STARTED** | **NEXT** — authorized to draft |
| R3 Implementation (code) | **NOT AUTHORIZED** | **NOT AUTHORIZED** until Implementation Charter + human decision |

---

## Sign-off record

| Role | Record |
|------|--------|
| Charter executor | Agent architecture charter 2026-06-05 |
| Human implementation approval | **PENDING** (R3 Implementation Charter) |
