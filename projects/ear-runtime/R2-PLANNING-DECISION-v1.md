# R2 Planning Decision v1

**Type:** Planning decision record  
**Phase:** R2 Planning Review  
**Date:** 2026-06-04  
**Review:** [R2-PLANNING-REVIEW-v1.md](R2-PLANNING-REVIEW-v1.md)  
**Subject:** R2 program kickoff readiness (planning → charter)

---

## Decision

| Scope | Verdict |
|-------|---------|
| **R2 planning review** | **COMPLETE** |
| **R2 kickoff (charter phase)** | **APPROVED WITH NOTES** |

---

## Rationale

The planning review closes the post-R1 gap analysis with evidence-backed scope boundaries:

1. **Target state is documented** — OpenCart 10-section tree and quality levels 0–3 are fully specified in architecture; gap matrix maps every section to Implemented / Partial / Missing against runtime source.
2. **Current honest capability is Level 0** — mock persist sets `package_quality_level: 0` and enumerates unpopulated sections in `safe-unknown` ([R2-PLANNING-REVIEW-v1.md](R2-PLANNING-REVIEW-v1.md) § Current Runtime Capability).
3. **Architecture backlog R2 is unambiguous** — Evidence Package Generator precedes Snapshot Builder (R3); recommended first milestone aligns with dependency chain ([EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md)).
4. **Consumer gates are explicit** — OCPilot Run 5 structural minimum is Level 1+ with `file-manifest`; not achievable without R3; not in R2 scope per consumer and backlog evidence.
5. **Out-of-scope items respected** — No connector, SFTP, SITE-001 pilot, persistence redesign, or OCPilot implementation in this planning lane.

**APPROVED WITH NOTES** (not bare APPROVED): charter authors must resolve **backlog R2 vs section-expansion naming** and confirm mock-only vs pilot-connected boundaries before implementation starts.

**NOT APPROVED** would apply if scope were undefined or contradicted frozen architecture — neither condition holds.

---

## Notes (charter preconditions — non-blocking for planning approval)

| Note | Action for R2 Implementation Charter |
|------|--------------------------------------|
| N-01 | Title backlog item **R2 — Evidence Package Generator** explicitly; do not charter “snapshot sections” as R2 |
| N-02 | Defer **File Manifest Expansion** and L1 OpenCart sections to **R3** charter |
| N-03 | Maintain **Level 0** honest quality on mock persist until R3 validates Level 1 possession |
| N-04 | **Publish** and OCPilot intake remain **R4** / consumer — store stays `stored_unpublished` |
| N-05 | Live acquisition, SFTP, SITE-001 — require separate PILOT Execution Authorization |
| N-06 | Human implementation approval gate remains open per [R1-IMPLEMENTATION-DECISION-v1.md](R1-IMPLEMENTATION-DECISION-v1.md) — R2 charter does not bypass |

---

## Evidence

| # | Evidence | Location |
|---|----------|----------|
| D-01 | OpenCart snapshot spec — sections, quality levels | [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](../../shared/external-access-runtime/EAR-OPENCART-SNAPSHOT-SPEC-v1.md) |
| D-02 | Consumer quality gating — Run 5 Level 1+ | [EAR-OPENCART-CONSUMER-GUIDE-v1.md](../../shared/external-access-runtime/EAR-OPENCART-CONSUMER-GUIDE-v1.md), [EAR-OCPILOT-INTEGRATION-v1.md](../../shared/external-access-runtime/EAR-OCPILOT-INTEGRATION-v1.md) |
| D-03 | Quality possession matrix | [EAR-OPENCART-QUALITY-MAPPING-v1.md](../../shared/external-access-runtime/EAR-OPENCART-QUALITY-MAPPING-v1.md) |
| D-04 | Backlog R2/R3/R4/R5 definitions | [EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) |
| D-05 | Evidence vs snapshot boundary | [EAR-EVIDENCE-PACKAGE-v1.md](../../shared/external-access-runtime/EAR-EVIDENCE-PACKAGE-v1.md) |
| D-06 | Runtime gap — flat SnapshotPackage | `runtime/shared/snapshot_models.py` |
| D-07 | Mock Store — 3 JSON, quality 0 | `runtime/shared/persistence_contract.py`, `runtime/persistence/snapshot_store.py` |
| D-08 | R1.8B field mapping | [R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md](R1.8B-SNAPSHOT-STORAGE-CONTRACT-v1.md) |
| D-09 | Evidence quarantine deferred | [R1.8E-PERSISTENCE-DECISION-v1.md](R1.8E-PERSISTENCE-DECISION-v1.md) |
| D-10 | Full planning artifact | [R2-PLANNING-REVIEW-v1.md](R2-PLANNING-REVIEW-v1.md) |

---

## Next gate

| Step | Status after this decision |
|------|----------------------------|
| R2 Planning Review | **DONE** |
| R2 Implementation Charter | **READY** — next engineering artifact |
| R2 Implementation | **NOT AUTHORIZED** until charter + human decision |

---

## Sign-off record

| Role | Record |
|------|--------|
| Planning review executor | Agent architecture review 2026-06-04 |
| Human charter approval | **PENDING** |
