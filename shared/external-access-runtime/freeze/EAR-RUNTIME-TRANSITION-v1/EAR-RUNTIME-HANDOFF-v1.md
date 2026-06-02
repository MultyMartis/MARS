# EAR Runtime Handoff v1

**Type:** Handoff package — assets and boundaries for EAR Runtime v1 Engineering  
**Date:** 2026-06-01  
**Audience:** Runtime engineering charter author and implementers

**This document does not define:** implementation language, libraries, repo layout for code, SFTP commands, deployment, or automation schedules.

---

## Handoff summary

EAR Runtime v1 receives a **frozen architecture corpus**, an **engineering backlog**, **default exclusion policy**, a **runtime boundary definition**, and an **authorized first pilot** (execution not authorized). Runtime work **implements** documented contracts — it does not **redesign** them without amendment.

---

## What Runtime v1 receives

### 1. Architecture corpus (read-only default)

| Package | Entry point |
|---------|-------------|
| Navigation | [OPERATIONAL-INDEX.md](../../OPERATIONAL-INDEX.md) |
| Freeze inventory | [EAR-ARCHITECTURE-COMPLETE-v1.md](EAR-ARCHITECTURE-COMPLETE-v1.md) |
| Boundary rules | [EAR-RUNTIME-BOUNDARY-v1.md](../../EAR-RUNTIME-BOUNDARY-v1.md) |
| Engineering targets | [EAR-RUNTIME-BACKLOG-v1.md](../../EAR-RUNTIME-BACKLOG-v1.md) |

### 2. PILOT-001 (first implementation reference)

| Asset | Location | Runtime use |
|-------|----------|-------------|
| Pilot charter | [PILOT-CHARTER-v1.md](../../pilots/PILOT-001-SITE-001-SFTP-READONLY/PILOT-CHARTER-v1.md) | Scope ceiling — Level 1, TEST, SFTP only |
| Implementation sub-charter | [IMPLEMENTATION-SUBCHARTER-v1.md](../../pilots/PILOT-001-SITE-001-SFTP-READONLY/IMPLEMENTATION-SUBCHARTER-v1.md) | Boundaries, preflight, §4 bindings (when signed) |
| Success / stop / risks | Pilot folder | Acceptance and halt conditions |
| Governance | [PILOT-GOVERNANCE-v1.md](../../PILOT-GOVERNANCE-v1.md) | Lifecycle gates |

**Status:** Charter **AUTHORIZED**; sub-charter **DRAFTED**; **Execution NOT AUTHORIZED**.

### 3. SITE-001 (target site context)

| Input | State | Runtime implication |
|-------|-------|---------------------|
| **Site ID** | `SITE-001` | OpenCart/ocStore reference site |
| **Platform** | ocStore 3.0.3.8 (rs.2) | Use OpenCart snapshot spec |
| **Environment** | TEST only | No production targeting |
| **Access channels** | Defined **externally** | Runtime reads operator bindings — not invented |
| **Consumer** | OCPilot Run 5 (paused) | Published snapshot feeds consumer intake |
| **Workflow example** | [EAR-SITE-001-WORKFLOW-EXAMPLE-v1.md](../../EAR-SITE-001-WORKFLOW-EXAMPLE-v1.md) | Illustrative — not execution script |
| **Acquisition options (theoretical)** | [EAR-SITE-001-ACQUISITION-OPTIONS-v1.md](../../EAR-SITE-001-ACQUISITION-OPTIONS-v1.md) | PILOT-001 chose SFTP CON-L1-A |

### 4. SFTP Read-Only strategy (design inputs)

| Input | Source | Notes |
|-------|--------|-------|
| Connector class | [EAR-CONNECTOR-TYPES-v1.md](../../EAR-CONNECTOR-TYPES-v1.md) | SFTP Read-Only |
| Connected path | [EAR-CONNECTED-PATHS-v1.md](../../EAR-CONNECTED-PATHS-v1.md) | **CON-L1-A** |
| Mode 2 reference flow | [EAR-MODE-2-OPENCART-REFERENCE-v1.md](../../EAR-MODE-2-OPENCART-REFERENCE-v1.md) | Channel → evidence → snapshot |
| Contract I/O | [EAR-CONNECTOR-CONTRACT-v1.md](../../EAR-CONNECTOR-CONTRACT-v1.md) | `scope`, status, evidence refs |
| Section mapping | [EAR-SNAPSHOT-MAPPING-v1.md](../../EAR-SNAPSHOT-MAPPING-v1.md) | SFTP → snapshot sections |
| Failures | [EAR-CONNECTOR-FAILURES-v1.md](../../EAR-CONNECTOR-FAILURES-v1.md) | Fail closed behaviors |
| Default exclusions | [EAR-DEFAULT-EXCLUSIONS-v1.md](../../EAR-DEFAULT-EXCLUSIONS-v1.md) | Plus pilot-specific `excluded_paths` at sign-off |

**Not in handoff:** SFTP hostnames, ports, credentials, session commands, or transfer scripts.

### 5. Snapshot Level 1 target

| Input | Source |
|-------|--------|
| Level definition | [EAR-OPENCART-QUALITY-MAPPING-v1.md](../../EAR-OPENCART-QUALITY-MAPPING-v1.md) |
| Package shape | [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](../../EAR-OPENCART-SNAPSHOT-SPEC-v1.md) |
| Logical contract | [EAR-SNAPSHOT-CONTRACT-v1.md](../../EAR-SNAPSHOT-CONTRACT-v1.md) |
| Publish gate | [EAR-SNAPSHOT-PUBLISHING-v1.md](../../EAR-SNAPSHOT-PUBLISHING-v1.md) |
| Validate gates | [EAR-READINESS-GATES-v1.md](../../EAR-READINESS-GATES-v1.md) |

**Honest maximum for PILOT-001:** Level **1** only — no Level 2+ without charter amendment.

### 6. Credential boundary

| Rule | Source |
|------|--------|
| `credential_ref` points to external store | [EAR-CREDENTIAL-BOUNDARY-v1.md](../../EAR-CREDENTIAL-BOUNDARY-v1.md) |
| No secrets in MARS git | [EAR-SECURITY-MODEL-v1.md](../../EAR-SECURITY-MODEL-v1.md), sub-charter §3.2 |
| Read-only account scope | Pilot charter + connector contract `scope` |
| HITL for Execution | [PILOT-GOVERNANCE-v1.md](../../PILOT-GOVERNANCE-v1.md) |

**Known fact:** `credential_ref` **exists** externally — path and rotation are **operator** responsibilities.

### 7. Storage model

| Role | Source | Runtime responsibility (conceptual) |
|------|--------|--------------------------------------|
| Quarantine (pre-redaction evidence) | [EAR-STORAGE-MODEL-v1.md](../../EAR-STORAGE-MODEL-v1.md) | Implement workspace — paths from sub-charter §4 |
| Evidence Package | [EAR-EVIDENCE-PACKAGE-v1.md](../../EAR-EVIDENCE-PACKAGE-v1.md) | Assemble before Validate |
| Candidate snapshot | Storage model | Pre-publish workspace |
| Published snapshot | [EAR-SNAPSHOT-PUBLISHING-v1.md](../../EAR-SNAPSHOT-PUBLISHING-v1.md) | Consumer-visible reference |
| Archive | Lifecycle | Post-publish retention |
| Bulk payload | Sub-charter requirements P-02 | External to git — **SAFE UNKNOWN** until sign-off |

**Approved direction:** Snapshot storage **outside** MARS git for bulk and published packages.

### 8. Risk model (inputs for runtime design)

| Layer | Document |
|-------|----------|
| OpenCart per-channel risks | [EAR-OPENCART-RISK-MODEL-v1.md](../../EAR-OPENCART-RISK-MODEL-v1.md) |
| EAR failure models | [EAR-FAILURE-MODELS-v1.md](../../EAR-FAILURE-MODELS-v1.md) |
| Connector failures | [EAR-CONNECTOR-FAILURES-v1.md](../../EAR-CONNECTOR-FAILURES-v1.md) |
| PILOT-001 risks | [RISK-REGISTER-v1.md](../../pilots/PILOT-001-SITE-001-SFTP-READONLY/RISK-REGISTER-v1.md) |

**Runtime must:** respect read-only default, exclusion policy, byte/file limits (when bound), stop conditions ST-*.

---

## Handoff assets checklist (for Runtime v1 charter)

| # | Asset | Included |
|---|-------|----------|
| A1 | Frozen architecture docs (`shared/external-access-runtime/`) | Yes |
| A2 | Freeze package (`freeze/EAR-RUNTIME-TRANSITION-v1/`) | Yes |
| A3 | EAR-RUNTIME-BACKLOG-v1.md | Yes |
| A4 | EAR-DEFAULT-EXCLUSIONS-v1.md | Yes |
| A5 | EAR-RUNTIME-BOUNDARY-v1.md | Yes |
| A6 | PILOT-001 pilot folder | Yes |
| A7 | External `credential_ref` | Exists — **not** in repo |
| A8 | Operator path bindings (§4 sub-charter) | **Pending** sign-off |
| A9 | Execution Authorization | **Not issued** |

---

## Explicit non-handoff (out of scope for Runtime v1 default charter)

| Item | Reason |
|------|--------|
| Live SFTP execution under PILOT-001 | Requires Execution Authorization |
| OCPilot Run 5 completion | Consumer program |
| Mode 3 / write connectors | Forbidden v1 |
| WordPress acquisition | Future roadmap |
| Production SITE-001 | Pilot TEST only |

---

## Suggested runtime engineering sequence (planning only)

1. Human charter: **EAR Runtime v1 Engineering** (scope = backlog R1–R5).
2. Resolve PILOT-001 §4 bindings at Implementation Authorization.
3. Implement backlog items in dependency order (see [EAR-RUNTIME-BACKLOG-v1.md](../../EAR-RUNTIME-BACKLOG-v1.md)).
4. Dry-run / validate without Execution until preflight satisfied.
5. Separate task: Execution Authorization for live acquisition.

No implementation detail in this handoff — sequence is **governance order** only.
