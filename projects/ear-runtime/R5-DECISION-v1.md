# R5 Decision v1

**Type:** Charter gate decision — R5 EAR Validate Layer  
**Date:** 2026-06-06  
**Charter:** [R5-CHARTER-v1.md](R5-CHARTER-v1.md)  
**Prior decision:** [R3-READINESS-DECISION-v1.md](R3-READINESS-DECISION-v1.md) — **READY FOR R5 WITH NOTES**

---

## Decision

| Field | Value |
|-------|-------|
| **Question** | May **R5 Charter** close and **R5 Implementation Charter** phase proceed? |
| **Outcome** | **APPROVED WITH NOTES** |
| **Scope of approval** | R5 mission, scope, non-goals, inputs, outputs, quality ownership, validation categories, publish boundary, success/stop criteria per [R5-CHARTER-v1.md](R5-CHARTER-v1.md) |
| **Explicitly not approved by this decision** | R5 runtime code, Validate automation implementation, Publish execution, Store redesign, snapshot assembly, evidence generation, OCPilot integration, live acquisition, SITE-001 / PILOT execution |

---

## Rationale

1. **R3 readiness gate satisfied** — [R3-READINESS-DECISION-v1.md](R3-READINESS-DECISION-v1.md) authorizes R5 Charter; R3.1–R3.7 complete; R3.6 documents R3/R5 boundary with invariants VB-R3-01–18.

2. **Authoritative mission aligned** — [EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) § R5 defines Validation Helpers as human-operated Validate assistants with fail-closed Publish blockers; charter correctly positions R5 as certification layer between R3 candidate and R4 Publish.

3. **Pipeline contract explicit** — `R2 Evidence → R3 Candidate → R5 Validate → R4 Publish` documented; Validate cannot be bypassed; R5 never publishes.

4. **Boundary preservation** — R5 does not redesign R1/R2/R3, does not assemble sections (R3), does not generate evidence (R2), does not execute Publish (R4). Matches R2.4 ownership matrix and R3.6 complementary checks.

5. **Quality ownership explicit** — R3 candidate L0 only; R5 sole certifier of L0–L3 possession per [EAR-OPENCART-QUALITY-MAPPING-v1.md](../../shared/external-access-runtime/EAR-OPENCART-QUALITY-MAPPING-v1.md).

6. **R3 debt acknowledged** — In-memory candidate path, Store persist adapter, bulk expansion (HO-ALLOW-10), R1.6 parallel path carried as notes — not blockers for charter per R3 readiness decision.

**APPROVED WITH NOTES** (not bare **APPROVED**): Implementation charter must carry R3 readiness notes N-R3R-01–08 and R3 debt; **R5 code implementation remains NOT AUTHORIZED** until R5 Implementation Charter and human gate per R1/R2/R3 pattern.

**FAIL** would apply if charter contradicted backlog (e.g. chartered Publish as R5), omitted R5→R4 boundary, assigned quality certification to R3, or merged Validate with assembly — **none apply**.

---

## Notes (carried to R5 Implementation Charter)

| Note | Action |
|------|--------|
| N-R5-01 | Title implementation work **R5 — EAR Validate Layer** / Validation Helpers — not Publish or Snapshot Assembly |
| N-R5-02 | First implementation consumes R3.1 `SnapshotPackage` via `--contract-snapshot` path — not R1.7 flat model |
| N-R5-03 | Emit distinct artefacts: `ValidationResult`, `ValidateReport` — never reuse R2/R3 eligibility outputs |
| N-R5-04 | R3 assembly pass is precondition only — implement VB-R3-01 invariant in Validate entry gate |
| N-R5-05 | Human HITL mandatory for pilot — helpers assist, do not replace operator Validate sign-off |
| N-R5-06 | Fail closed on Publish Eligibility Recommendation per EAR-READINESS-GATES-v1 |
| N-R5-07 | Disambiguate R2 structural / R3 assembly eligibility / R5 EAR Validate in all R5 docs |
| N-R5-08 | Per-category validation rules (R5-V-*) — resolve at Implementation Charter (**SAFE UNKNOWN** at R5 Charter) |
| N-R5-09 | Contract-path Store persist and bulk expansion — schedule parallel or pre-live Validate (R3 debt) |
| N-R5-10 | Human implementation approval gate — R5 Implementation Charter does not bypass R1/R2/R3 gate pattern |

---

## Evidence

| # | Evidence | Location |
|---|----------|----------|
| D-R5-01 | R3 readiness review — R5 entry assessment | [R3-READINESS-REVIEW-v1.md](R3-READINESS-REVIEW-v1.md) |
| D-R5-02 | R3 closure — READY FOR R5 WITH NOTES | [R3-READINESS-DECISION-v1.md](R3-READINESS-DECISION-v1.md) |
| D-R5-03 | R3/R5 validation boundary | [R3.6-VALIDATION-BOUNDARY-REVIEW-v1.md](R3.6-VALIDATION-BOUNDARY-REVIEW-v1.md) |
| D-R5-04 | R2/R5 evidence validation boundary | [R2.4-EVIDENCE-VALIDATION-BOUNDARY-v1.md](R2.4-EVIDENCE-VALIDATION-BOUNDARY-v1.md) |
| D-R5-05 | Evidence → Snapshot handoff | [R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md](R2.6-EVIDENCE-SNAPSHOT-HANDOFF-v1.md) |
| D-R5-06 | OpenCart quality mapping | [EAR-OPENCART-QUALITY-MAPPING-v1.md](../../shared/external-access-runtime/EAR-OPENCART-QUALITY-MAPPING-v1.md) |
| D-R5-07 | Readiness gates | [EAR-READINESS-GATES-v1.md](../../shared/external-access-runtime/EAR-READINESS-GATES-v1.md) |
| D-R5-08 | Backlog R5 definition | [EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) |
| D-R5-09 | R5 Charter artifact | [R5-CHARTER-v1.md](R5-CHARTER-v1.md) |

---

## Gate transition

| Gate | Before R5 Charter | After R5 Charter |
|------|-------------------|------------------|
| R3 Readiness Review | **COMPLETE** | **COMPLETE** |
| R5 Charter | **AUTHORIZED** | **COMPLETE** |
| R5 Implementation Charter | **NOT STARTED** | **NEXT** — authorized to draft |
| R5 Implementation (code) | **NOT AUTHORIZED** | **NOT AUTHORIZED** until Implementation Charter + human decision |
| R4 Publish | **PLANNED** | **PLANNED** — remains after R5 implementation path chartered |

---

## Sign-off record

| Role | Record |
|------|--------|
| Charter executor | Agent architecture charter 2026-06-06 |
| Human implementation approval | **PENDING** (R5 Implementation Charter) |
