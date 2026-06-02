# R1 — SFTP Read-Only Connector Implementation Readiness Review v1

**Type:** Formal implementation readiness assessment — **not** implementation, **not** code, **not** SFTP access, **not** pilot execution  
**Date:** 2026-06-02  
**Backlog item:** R1 — First SFTP Read-Only Connector  
**Question:** Is R1 ready for **Implementation Charter** authorization (human gate)?

**Scope boundary:** This review judges whether frozen architecture, runtime engineering documents, and PILOT-001 traceability are sufficient to **author and seek human approval** of an **R1 Implementation Charter**. It does **not** authorize implementation, library selection, live SFTP, PILOT-001 Execution, or snapshot publication.

**Prerequisites reviewed:**

| Prerequisite | Status |
|--------------|--------|
| EAR Architecture Program | **COMPLETE** (frozen 2026-06-01) |
| EAR Runtime Transition Freeze | **YES** |
| EAR Runtime v1 Engineering Charter | **APPROVED** (2026-06-02) |
| R1 Planning Charter | **DONE** — [R1-SFTP-CONNECTOR-CHARTER-v1.md](R1-SFTP-CONNECTOR-CHARTER-v1.md) |
| Runtime implementation in repo | **NONE** (expected) |
| PILOT-001 Execution | **NOT AUTHORIZED** |

---

## 1. Artifacts reviewed

### 1.1 Runtime engineering (mandatory)

| Document | Reviewed | Finding |
|----------|----------|---------|
| [ENGINEERING-CHARTER-v1.md](ENGINEERING-CHARTER-v1.md) | Yes | Program **STARTED**; Python, CLI-first, human-operated, read-only first |
| [ENGINEERING-BOUNDARIES-v1.md](ENGINEERING-BOUNDARIES-v1.md) | Yes | Runtime vs architecture vs consumer split clear |
| [ENGINEERING-PRINCIPLES-v1.md](ENGINEERING-PRINCIPLES-v1.md) | Yes | HITL, credential boundary, fail closed, status honesty |
| [RUNTIME-STRUCTURE-v1.md](RUNTIME-STRUCTURE-v1.md) | Yes | Proposed `runtime/` layout — **not materialized** |
| [R1-SFTP-CONNECTOR-CHARTER-v1.md](R1-SFTP-CONNECTOR-CHARTER-v1.md) | Yes | Inputs, outputs, boundaries, success criteria — **PLANNED** |
| [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) | Yes | Honest: no code, R1 gate was pending |
| [EAR-RUNTIME-ROADMAP-v1.md](EAR-RUNTIME-ROADMAP-v1.md) | Yes | R1 is Phase 1 after Engineering Charter |
| [STATE-TRANSITION-v1.md](STATE-TRANSITION-v1.md) | Yes | Engineering charter transition recorded |

### 1.2 EAR architecture contracts (mandatory)

| Document | Reviewed | Relevance |
|----------|----------|-----------|
| [EAR-CONNECTOR-CONTRACT-v1.md](../../shared/external-access-runtime/EAR-CONNECTOR-CONTRACT-v1.md) | Yes | Connector I/O, status, errors, warnings |
| [EAR-CREDENTIAL-BOUNDARY-v1.md](../../shared/external-access-runtime/EAR-CREDENTIAL-BOUNDARY-v1.md) | Yes | `credential_ref` only; no secrets in git |
| [EAR-SNAPSHOT-CONTRACT-v1.md](../../shared/external-access-runtime/EAR-SNAPSHOT-CONTRACT-v1.md) | Yes | Consumer package shape (downstream of R1) |
| [EAR-EVIDENCE-PACKAGE-v1.md](../../shared/external-access-runtime/EAR-EVIDENCE-PACKAGE-v1.md) | Yes | Evidence vs snapshot; R2 domain |
| [EAR-SNAPSHOT-MAPPING-v1.md](../../shared/external-access-runtime/EAR-SNAPSHOT-MAPPING-v1.md) | Yes | SFTP primary for `file-manifest`, extensions |
| [EAR-CONNECTOR-FAILURES-v1.md](../../shared/external-access-runtime/EAR-CONNECTOR-FAILURES-v1.md) | Yes | Fail-closed connector behavior |
| [EAR-FAILURE-MODELS-v1.md](../../shared/external-access-runtime/EAR-FAILURE-MODELS-v1.md) | Yes | Workflow-level failure philosophy |
| [EAR-STORAGE-MODEL-v1.md](../../shared/external-access-runtime/EAR-STORAGE-MODEL-v1.md) | Yes | External bulk; paths **SAFE UNKNOWN** |
| [EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) | Yes | R1 acceptance criteria |
| [EAR-CONNECTOR-ARCHITECTURE-v1.md](../../shared/external-access-runtime/EAR-CONNECTOR-ARCHITECTURE-v1.md) | Yes | Connector → Evidence Package (full architecture) |
| [EAR-CONNECTED-PATHS-v1.md](../../shared/external-access-runtime/EAR-CONNECTED-PATHS-v1.md) | Yes | CON-L1-A reference path |
| [EAR-DEFAULT-EXCLUSIONS-v1.md](../../shared/external-access-runtime/EAR-DEFAULT-EXCLUSIONS-v1.md) | Yes | Default path exclusions for scope |
| [EAR-RUNTIME-BOUNDARY-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BOUNDARY-v1.md) | Yes | Architecture ↔ runtime boundary |

### 1.3 PILOT-001 package

| Document | Reviewed | Finding |
|----------|----------|---------|
| [PILOT-CHARTER-v1.md](../../shared/external-access-runtime/pilots/PILOT-001-SITE-001-SFTP-READONLY/PILOT-CHARTER-v1.md) | Yes | SITE-001, TEST, Mode 2, SFTP, Level 1 |
| [STATUS.md](../../shared/external-access-runtime/pilots/PILOT-001-SITE-001-SFTP-READONLY/STATUS.md) | Yes | Charter ACTIVE; Approval **NOT STARTED**; Execution **NOT AUTHORIZED** |
| [PHASE-5-DECISION-v1.md](../../shared/external-access-runtime/pilots/PILOT-001-SITE-001-SFTP-READONLY/PHASE-5-DECISION-v1.md) | Yes | Pilot impl readiness **CONDITIONAL GO** (sub-charter drafting) |
| [PHASE-6-DECISION-v1.md](../../shared/external-access-runtime/pilots/PILOT-001-SITE-001-SFTP-READONLY/PHASE-6-DECISION-v1.md) | Yes | Sub-charter **drafted**; operator bindings **SAFE UNKNOWN** |
| [IMPLEMENTATION-SUBCHARTER-v1.md](../../shared/external-access-runtime/pilots/PILOT-001-SITE-001-SFTP-READONLY/IMPLEMENTATION-SUBCHARTER-v1.md) | Yes | Path placeholders; no execution authorization |
| [SUCCESS-CRITERIA-v1.md](../../shared/external-access-runtime/pilots/PILOT-001-SITE-001-SFTP-READONLY/SUCCESS-CRITERIA-v1.md) | Yes | Referenced for alignment |
| [STOP-CONDITIONS-v1.md](../../shared/external-access-runtime/pilots/PILOT-001-SITE-001-SFTP-READONLY/STOP-CONDITIONS-v1.md) | Yes | Read-only and implementation boundaries |

### 1.4 Consumer context (supporting)

| Document | Reviewed | Finding |
|----------|----------|---------|
| [projects/ocpilot/sites/site-001/project-access-brief.md](../../projects/ocpilot/sites/site-001/project-access-brief.md) | Yes | External `secrets/` pattern documented; live channel unverified |

---

## 2. Readiness categories (summary)

| Category | Status |
|----------|--------|
| Mission | **READY** |
| Scope | **READY** |
| Inputs | **READY** |
| Outputs | **PARTIAL** |
| Connector Contract | **PARTIAL** |
| Credential Boundary | **PARTIAL** |
| Snapshot Mapping | **READY** |
| Evidence Package | **READY** |
| Failure Handling | **READY** |
| Pilot Alignment | **PARTIAL** |
| Read-Only Compliance | **READY** |
| Engineering Boundaries | **READY** |
| Runtime Structure | **PARTIAL** |
| Storage Model | **PARTIAL** |
| Operational Safety | **READY** |
| Documentation Consistency | **PARTIAL** |

**Summary counts:** READY = 10 · PARTIAL = 6 · NOT READY = 0

---

## 3. Implementation readiness matrix

| Category | Status | Evidence | Blocking? | Notes |
|----------|--------|----------|-----------|-------|
| **Mission** | READY | [ENGINEERING-CHARTER-v1.md](ENGINEERING-CHARTER-v1.md); [R1-SFTP-CONNECTOR-CHARTER-v1.md](R1-SFTP-CONNECTOR-CHARTER-v1.md) | No | Mode 2 read-only SFTP; CON-L1-A; first connected helper |
| **Scope** | READY | R1 charter § Boundaries; [EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) § R1 | No | SSH/FTP/PMA/DB/Hybrid/production/write excluded |
| **Inputs** | READY | R1 charter § Inputs; [EAR-CONNECTOR-CONTRACT-v1.md](../../shared/external-access-runtime/EAR-CONNECTOR-CONTRACT-v1.md) | No | Connector Input fields defined; forbidden secrets explicit |
| **Outputs** | PARTIAL | R1 charter § Outputs; connector contract | No | R1 scopes **raw acquisition artefacts** for R2; full contract lists `evidence_package_ref` on connector output — **R1+R2** chain must be named in Implementation Charter |
| **Connector Contract** | PARTIAL | [EAR-CONNECTOR-CONTRACT-v1.md](../../shared/external-access-runtime/EAR-CONNECTOR-CONTRACT-v1.md); [EAR-CONNECTOR-ARCHITECTURE-v1.md](../../shared/external-access-runtime/EAR-CONNECTOR-ARCHITECTURE-v1.md) | No | Normative contract complete; runtime mapping R1 vs R2 deferred to Implementation Charter |
| **Credential Boundary** | PARTIAL | [EAR-CREDENTIAL-BOUNDARY-v1.md](../../shared/external-access-runtime/EAR-CREDENTIAL-BOUNDARY-v1.md); pilot sub-charter §4 | No | Model **READY**; operator `credential_ref` path **SAFE UNKNOWN** until bindings fixed |
| **Snapshot Mapping** | READY | [EAR-SNAPSHOT-MAPPING-v1.md](../../shared/external-access-runtime/EAR-SNAPSHOT-MAPPING-v1.md); CON-L1-A | No | SFTP primary for Level 1 file evidence — R3+ concern for publish |
| **Evidence Package** | READY | [EAR-EVIDENCE-PACKAGE-v1.md](../../shared/external-access-runtime/EAR-EVIDENCE-PACKAGE-v1.md) | No | R2 owns assembly; R1 must not claim Evidence Package completeness |
| **Failure Handling** | READY | [EAR-CONNECTOR-FAILURES-v1.md](../../shared/external-access-runtime/EAR-CONNECTOR-FAILURES-v1.md); [ENGINEERING-PRINCIPLES-v1.md](ENGINEERING-PRINCIPLES-v1.md) | No | Fail closed, no secret leakage — runtime binding in Implementation Charter |
| **Pilot Alignment** | PARTIAL | [PILOT-CHARTER-v1.md](../../shared/external-access-runtime/pilots/PILOT-001-SITE-001-SFTP-READONLY/PILOT-CHARTER-v1.md); [STATUS.md](../../shared/external-access-runtime/pilots/PILOT-001-SITE-001-SFTP-READONLY/STATUS.md) | No | PILOT-001 design target aligned; **human Approval** and **Execution** not authorized — does not block R1 **code charter** |
| **Read-Only Compliance** | READY | [ENGINEERING-PRINCIPLES-v1.md](ENGINEERING-PRINCIPLES-v1.md); [EAR-MODES-v1.md](../../shared/external-access-runtime/EAR-MODES-v1.md) | No | Mode 2 only; Mode 3 forbidden |
| **Engineering Boundaries** | READY | [ENGINEERING-BOUNDARIES-v1.md](ENGINEERING-BOUNDARIES-v1.md) | No | Runtime owns connector execution; not consumer logic |
| **Runtime Structure** | PARTIAL | [RUNTIME-STRUCTURE-v1.md](RUNTIME-STRUCTURE-v1.md) | No | Proposed only; `runtime/connectors/` etc. **not created** |
| **Storage Model** | PARTIAL | [EAR-STORAGE-MODEL-v1.md](../../shared/external-access-runtime/EAR-STORAGE-MODEL-v1.md); pilot §4 | No | Roles defined; absolute quarantine/bulk paths **SAFE UNKNOWN** |
| **Operational Safety** | READY | Principles; pilot stop conditions; credential boundary | No | No live access in this phase |
| **Documentation Consistency** | PARTIAL | R1 charter vs connector architecture Evidence Package emit | No | Intentional R1/R2 split — must be explicit in Implementation Charter to avoid drift |

---

## 4. Runtime decisions evaluation

| Decision area | Status | Evidence / notes |
|---------------|--------|------------------|
| **Python Version** | SAFE UNKNOWN | [ENGINEERING-CHARTER-v1.md](ENGINEERING-CHARTER-v1.md) selects Python; **no** minor version pin in repo |
| **Packaging Strategy** | SAFE UNKNOWN | Engineering charter defers frameworks/libraries to this review; explicitly **not** decided — no venv/poetry/uv evidence |
| **Execution Style** | KNOWN | CLI-first, human-operated — [ENGINEERING-CHARTER-v1.md](ENGINEERING-CHARTER-v1.md), [ENGINEERING-PRINCIPLES-v1.md](ENGINEERING-PRINCIPLES-v1.md) |
| **Credential Binding** | PARTIAL | `credential_ref` model KNOWN; resolution procedure and paths SAFE UNKNOWN — [EAR-CREDENTIAL-BOUNDARY-v1.md](../../shared/external-access-runtime/EAR-CREDENTIAL-BOUNDARY-v1.md), pilot sub-charter §4 |
| **Output Location** | SAFE UNKNOWN | Raw acquisition bulk — operator-bound per storage model; not named in repo |
| **Evidence Location** | SAFE UNKNOWN | R2 workspace; [EAR-EVIDENCE-PACKAGE-v1.md](../../shared/external-access-runtime/EAR-EVIDENCE-PACKAGE-v1.md) conceptual only |
| **Snapshot Location** | SAFE UNKNOWN | R3/R4; pilot sub-charter placeholders |
| **Logging Strategy** | PARTIAL | Inspectability principle KNOWN; structured logging **examples only** in [RUNTIME-STRUCTURE-v1.md](RUNTIME-STRUCTURE-v1.md) — no format/path policy |
| **Failure Reporting** | PARTIAL | Taxonomy KNOWN per architecture; runtime log artefact location SAFE UNKNOWN |

---

## 5. Blockers

**Architectural blockers for R1 Implementation Charter:** **none**

**Engineering gaps (resolve in Implementation Charter or operator binding — not NO-GO):**

| ID | Gap | Owner | Blocks |
|----|-----|-------|--------|
| G-01 | Python minor version not pinned | Implementation Charter | Reproducible dev environment |
| G-02 | Packaging / dependency manager not chosen | Implementation Charter | Dependency install procedure |
| G-03 | SFTP client library not chosen | Implementation Charter | **Expected** — out of scope for this review |
| G-04 | Operator paths (`credential_ref`, bulk, quarantine) SAFE UNKNOWN | Operator + charter | Live pilot preflight — **not** R1 charter drafting |
| G-05 | `runtime/` subdirectories not materialized | Implementation Charter | Repo layout |
| G-06 | R1 output shape vs full connector contract boundary | Implementation Charter | Contract conformance documentation |

**Process notes (do not block R1 Implementation Charter):**

| ID | Note |
|----|------|
| P-01 | PILOT-001 human **Approval** not in [STATUS.md](../../shared/external-access-runtime/pilots/PILOT-001-SITE-001-SFTP-READONLY/STATUS.md) — blocks pilot **Execution**, not R1 engineering charter |
| P-02 | No connector code in repo — **expected** |

---

## 6. Readiness decision

| Field | Value |
|-------|-------|
| **Result** | **CONDITIONAL GO** |
| **Meaning** | R1 **Implementation Charter** may be drafted and submitted for human approval; minor engineering bindings remain |
| **Does not authorize** | Implementation, libraries, SFTP sessions, PILOT-001 Execution |

---

## 7. Decision rationale

| Factor | Assessment |
|--------|------------|
| Frozen architecture | Complete; R1 traceable to CON-L1-A, connector contract, failures, credential boundary |
| Runtime engineering program | **STARTED** with approved stack direction (Python, CLI, human-operated, read-only) |
| R1 planning | Charter complete with inputs, outputs, boundaries, success criteria |
| Implementation in repo | None — honest and expected |
| Gaps | Version pin, packaging, paths, R1/R2 contract boundary — resolvable in Implementation Charter without architecture amendment |
| Pilot | Aligned as design consumer; execution gates intentionally separate |

**Why not GO:** Operator bindings and several runtime decisions remain **SAFE UNKNOWN** — Implementation Charter must fix them before coding starts.

**Why not NO-GO:** Zero **NOT READY** categories; no architecture contradiction; backlog and principles provide sufficient authorization to **plan** implementation.

---

## 8. Implementation requirements pointer

See [R1-IMPLEMENTATION-CHARTER-REQUIREMENTS-v1.md](R1-IMPLEMENTATION-CHARTER-REQUIREMENTS-v1.md) for mandatory content before implementation may begin.

---

## 9. Risks

| Risk | Mitigation |
|------|------------|
| Treating CONDITIONAL GO as implementation approval | Separate human **R1 Implementation Charter** gate |
| R1/R2 boundary drift vs connector architecture | Implementation Charter must document session output vs Evidence Package |
| Inventing operator paths during coding | Charter must reference operator sign-off or remain blocked |
| Library selection without read-only tests plan | Implementation Charter includes non-production test strategy |
| Conflating R1 readiness with PILOT Execution | STATUS and governance docs keep gates separate |
| Secrets in git during implementation | Credential boundary + code review discipline |

---

## 10. Recommended next step

| Step | Action |
|------|--------|
| 1 | Human review this document + [R1-PHASE-DECISION-v1.md](R1-PHASE-DECISION-v1.md) |
| 2 | Author **R1 Implementation Charter** per [R1-IMPLEMENTATION-CHARTER-REQUIREMENTS-v1.md](R1-IMPLEMENTATION-CHARTER-REQUIREMENTS-v1.md) |
| 3 | Update [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) when Implementation Charter approved |
| 4 | Do **not** start live SFTP without PILOT Execution Authorization |

---

## Truth statement

| Claim | Accurate? |
|-------|-----------|
| R1 implementation exists | **No** |
| This review authorizes coding | **No** |
| SFTP was accessed during review | **No** |
| Architecture requires amendment for R1 | **No** |
