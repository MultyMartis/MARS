# PILOT-001 — Implementation Sub-Charter v1

**Type:** Operational authorization package — boundaries and gates only  
**Phase:** 6 — Implementation Sub-Charter (planning layer)  
**Date:** 2026-06-01  
**Pilot ID:** `PILOT-001`  
**Folder:** [README.md](README.md)

**Prerequisites:** [PILOT-CHARTER-v1.md](PILOT-CHARTER-v1.md) · [PHASE-5-DECISION-v1.md](PHASE-5-DECISION-v1.md) (**CONDITIONAL GO**) · [IMPLEMENTATION-SUBCHARTER-REQUIREMENTS-v1.md](IMPLEMENTATION-SUBCHARTER-REQUIREMENTS-v1.md)

**This document does not authorize:** runtime code, connector implementation, credential use, SFTP sessions, snapshot publication, site modification, or pilot **Execution**.

**Truth:** This artifact **defines** operational boundaries required before PILOT-001 may be executed. Human sign-off in §10 is **pending** until operator bindings and governance gates are satisfied.

---

## 1. Pilot identity

| Field | Value |
|-------|-------|
| **Pilot ID** | `PILOT-001` |
| **Pilot slug** | `PILOT-001-SITE-001-SFTP-READONLY` |
| **Site ID** | `SITE-001` |
| **Site name** | Автосалон СИБКАР |
| **Platform** | ocStore 3.0.3.8 (rs.2) |
| **Baseline** | `ocstore-3038-rs2` |
| **Environment** | `TEST` |
| **Track** | Connected Acquisition |
| **EAR mode** | **Mode 2** — Connected Read Only |
| **Connector class** | **SFTP Read-Only** |
| **Canonical path** | **CON-L1-A** per [EAR-CONNECTED-PATHS-v1.md](../../EAR-CONNECTED-PATHS-v1.md) |
| **Consumer** | **OCPilot** (SITE-001 Run 5 read-only audit — paused pending acquisition path) |
| **Snapshot target** | **Level 1** (honest maximum for this pilot) |
| **Current status** | Implementation Sub-Charter **drafted** (Phase 6) — operator bindings **SAFE UNKNOWN** |
| **Execution status** | **NOT AUTHORIZED** |
| **Approval status** | Charter **Approval:** **NOT STARTED** ([STATUS.md](STATUS.md)) · Sub-charter **authorization:** **PENDING** human sign-off (§10) · **Execution:** **NOT AUTHORIZED** |

---

## 2. Purpose and scope of this sub-charter

| In scope | Out of scope |
|----------|--------------|
| Operational boundaries before Execution | Writing connector code |
| Placeholder operational paths (no invented values) | Live SFTP or SSH access |
| Approval progression rules | Runtime deployment |
| Preflight **requirements** (not steps) | Performing acquisition |
| Execution readiness checklist (honest unresolved items) | Claiming Execution readiness |

**Relationship to other artifacts:**

| Artifact | Relationship |
|----------|--------------|
| [PILOT-CHARTER-v1.md](PILOT-CHARTER-v1.md) | Parent scope — sub-charter does not expand charter exclusions |
| [IMPLEMENTATION-SUBCHARTER-REQUIREMENTS-v1.md](IMPLEMENTATION-SUBCHARTER-REQUIREMENTS-v1.md) | Checklist this document must satisfy before sign-off |
| [EXECUTION-PREPARATION-PLAN-v1.md](EXECUTION-PREPARATION-PLAN-v1.md) | Phase 6 planning — stages only, no execution detail |
| [PILOT-GOVERNANCE-v1.md](../../PILOT-GOVERNANCE-v1.md) | Lifecycle gates §5 |

**Charter ≠ Implementation Sub-Charter ≠ Execution** — repeating [PILOT-GOVERNANCE-v1.md](../../PILOT-GOVERNANCE-v1.md) §2.

---

## 3. Execution boundaries

### 3.1 Allowed (planning and authorization package only)

Until **Execution** is separately authorized and preflight is satisfied:

| Category | Allowed activity |
|----------|------------------|
| **Acquisition planning** | Read-only acquisition **planning** — scope, CON-L1-A traceability, partial-acquisition semantics |
| **Evidence planning** | Evidence Package **planning** per [EAR-EVIDENCE-PACKAGE-v1.md](../../EAR-EVIDENCE-PACKAGE-v1.md) |
| **Snapshot planning** | Snapshot Level 1 **planning** per [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](../../EAR-OPENCART-SNAPSHOT-SPEC-v1.md) |
| **Validation planning** | Validate stage **planning** (G1–G4 ownership, checklists) — **not** live Validate |
| **Consumer handoff planning** | OCPilot intake **planning** per [EAR-OPENCART-CONSUMER-GUIDE-v1.md](../../EAR-OPENCART-CONSUMER-GUIDE-v1.md) — **no** Run 5 completion claim |

**Documentation:** Authoring and updating pilot/EAR docs under explicit human task charter.

### 3.2 Forbidden (unless separate future human charter)

| Category | Forbidden activity |
|----------|---------------------|
| **Writes** | Any **write** operation to remote host, local production mirrors, or consumer deploy paths |
| **Database** | Database modifications, dumps with write side effects, or schema changes |
| **Admin** | Admin panel modifications, installer runs, extension installs |
| **Theme** | Theme file modifications on target |
| **Modules** | Module install, enable, disable, or upload |
| **Catalog** | Catalog, product, category, or customer data changes |
| **Server config** | Server configuration changes (web server, PHP, cron, permissions escalation) |
| **SSH escalation** | SSH shell access, command execution, or privilege escalation beyond read-only SFTP scope |
| **Production** | Production environment access or production host targeting |
| **Mode 3** | EAR Mode 3 — forbidden in v1 |
| **Scope creep** | Level 2+, Hybrid connectors, PMA-only, FTP-only without charter amendment |
| **Inflated publish** | Publish above honest Level 1 or with triggered stop conditions |
| **Secrets in git** | Storing credentials, keys, or unredacted sensitive config in MARS git |

**Live read-only acquisition** is **forbidden** until: approved sub-charter (§10) + **Execution Authorization** + preflight §6 satisfied — see [STOP-CONDITIONS-v1.md](STOP-CONDITIONS-v1.md) ST-17.

---

## 4. Operational paths (placeholders only)

**Rule:** No values invented in Phase 6. Operator resolves at sign-off. Unresolved = **SAFE UNKNOWN**.

| Field | Value | Notes |
|-------|-------|-------|
| **credential_ref** | **SAFE UNKNOWN** | External store reference only — per [EAR-CREDENTIAL-BOUNDARY-v1.md](../../EAR-CREDENTIAL-BOUNDARY-v1.md); **no** secrets in git |
| **sftp_root** | **SAFE UNKNOWN** | TEST document root — operator-confirmed at sign-off |
| **allowed_paths** | **SAFE UNKNOWN** | Approved list/globs (e.g. version proof files) — CON-L1-A scope |
| **excluded_paths** | **SAFE UNKNOWN** | e.g. `cache/`, `logs/`, `sessions/`, large `image/` policy — per charter risk R-11 |
| **quarantine_location** | **SAFE UNKNOWN** | Pre-redaction Evidence Package quarantine per [EAR-STORAGE-MODEL-v1.md](../../EAR-STORAGE-MODEL-v1.md) |
| **evidence_location** | **SAFE UNKNOWN** | Evidence Package workspace (may align with quarantine pre-Validate) |
| **snapshot_location** | **SAFE UNKNOWN** | Candidate snapshot workspace pre-publish |
| **publish_location** | **SAFE UNKNOWN** | Consumer-visible published snapshot reference (OCPilot intake policy) |

**Bulk payload storage** (large downloads): **SAFE UNKNOWN** — required per requirements P-02; name at operator sign-off.

**Git exclusion:** Operator must confirm no secrets, dumps, or unredacted bulk in MARS git (requirements P-05).

---

## 5. Approval model

Per [PILOT-GOVERNANCE-v1.md](../../PILOT-GOVERNANCE-v1.md) §5.1. Phase 6 documents gates; **does not** satisfy them.

### 5.1 Gate definitions

| Gate | What it authorizes | What it does **not** authorize |
|------|-------------------|-------------------------------|
| **Operator Approval** | Progression past **Charter**; may plan and draft Implementation Sub-Charter | Implementation work, live access, publish |
| **Implementation Authorization** | Bound scope for **future** implementation artifacts (connector module location, helper policy — human decision); credential **plan** and path bindings when §4 filled | Execution, live SFTP, snapshot publish |
| **Execution Authorization** | Live read-only acquisition under approved sub-charter + preflight | Production, writes, Mode 3, Level 2+ claims |
| **Assessment Acceptance** | Pass/fail vs [SUCCESS-CRITERIA-v1.md](SUCCESS-CRITERIA-v1.md) | Architecture change without governed doc update |
| **Lessons Learned Acceptance** | Close pilot loop; optional EAR/pilot doc updates | Retroactive Execution approval |

### 5.2 Progression rules

```
Charter (Phase 4) — DONE
    ↓
Operator Approval — record in STATUS.md (G-03) — NOT STARTED
    ↓
Implementation Sub-Charter drafted (Phase 6) — THIS DOCUMENT
    ↓
Implementation Authorization — human sign-off §10 when requirements met
    ↓
(Optional) Implementation work — only after Implementation Authorization; separate task charter
    ↓
Execution Authorization — separate explicit HITL; not implied by sub-charter
    ↓
Preflight §6 + Execution readiness §7 — all mandatory items resolved or honestly waived per risk register
    ↓
Live read-only acquisition (future) — Assessment → Lessons Learned
```

| Rule | Statement |
|------|-----------|
| **R-01** | No gate may be skipped |
| **R-02** | Later gate never implies earlier gate |
| **R-03** | Agents document; humans approve Execution and Production |
| **R-04** | Stop condition → halt; no soft continue ([STOP-CONDITIONS-v1.md](STOP-CONDITIONS-v1.md)) |
| **R-05** | Sub-charter sign-off with **SAFE UNKNOWN** in §4 blocks **Execution Authorization** until resolved |

### 5.3 Roles (sign-off §10)

| Role | Typical responsibility |
|------|------------------------|
| Human charter authority | Operator Approval; Assessment / Lessons acceptance |
| Operator technical lead | Path, SFTP scope, storage bindings |
| Validate owner | G1–G4 manual Validate (named at sign-off — **SAFE UNKNOWN** until recorded) |

---

## 6. Preflight requirements

**Requirements only** — not execution steps. Operator attestation or evidence **before** Execution Authorization.

| # | Requirement | Status at Phase 6 close |
|---|-------------|-------------------------|
| PF-01 | Read-only SFTP account **confirmed** (or documented fail → ST-21) | **SAFE UNKNOWN** |
| PF-02 | Target environment **TEST** confirmed (not production) | **Documented** in charter — live host mapping **SAFE UNKNOWN** |
| PF-03 | `credential_ref` exists in operator external store | **SAFE UNKNOWN** |
| PF-04 | Baseline `ocstore-3038-rs2` confirmed for SITE-001 TEST | **Documented** in charter — live proof **SAFE UNKNOWN** |
| PF-05 | Storage locations confirmed (`quarantine`, evidence, snapshot, publish, bulk) | **SAFE UNKNOWN** (§4) |
| PF-06 | SFTP scope documented (`sftp_root`, allowed/excluded paths, byte/file limits) | **SAFE UNKNOWN** |
| PF-07 | Risk acceptance recorded (pilot [RISK-REGISTER-v1.md](RISK-REGISTER-v1.md) + waivers) | **Partial** — register exists; execution waivers **SAFE UNKNOWN** |
| PF-08 | Stop conditions reviewed ([STOP-CONDITIONS-v1.md](STOP-CONDITIONS-v1.md)) | **Met** (documentation) |
| PF-09 | Redaction plan for sensitive paths (e.g. `config.php`) | **SAFE UNKNOWN** — required before live acquisition |
| PF-10 | Validate owner and `operator_approver` named | **SAFE UNKNOWN** |
| PF-11 | G-03 **Operator Approval** recorded in [STATUS.md](STATUS.md) | **Not met** |
| PF-12 | Implementation Authorization (§10) recorded | **Not met** |
| PF-13 | No active stop conditions | **Met** |

---

## 7. Execution readiness checklist

Answer **YES** only with repository or operator-recorded evidence. **NO** = known gap. **SAFE UNKNOWN** = not proven in repo.

| # | Item | YES | NO | SAFE UNKNOWN |
|---|------|-----|-----|--------------|
| ER-01 | Human **Operator Approval** in STATUS | | ✓ | |
| ER-02 | Implementation Sub-Charter **authorized** (§10 signed) | | ✓ | |
| ER-03 | **Execution Authorization** explicitly granted | | ✓ | |
| ER-04 | `credential_ref` named (no values in git) | | | ✓ |
| ER-05 | Read-only SFTP account verified on TEST host | | | ✓ |
| ER-06 | `sftp_root` operator-confirmed | | | ✓ |
| ER-07 | `allowed_paths` / `excluded_paths` documented | | | ✓ |
| ER-08 | Quarantine and evidence locations confirmed | | | ✓ |
| ER-09 | Snapshot and publish locations confirmed | | | ✓ |
| ER-10 | Bulk storage path confirmed | | | ✓ |
| ER-11 | Baseline version proof obtainable via CON-L1-A | | | ✓ |
| ER-12 | Validate owner named | | | ✓ |
| ER-13 | Redaction plan approved | | | ✓ |
| ER-14 | Stop conditions incorporated in runbook | ✓ | | |
| ER-15 | Connector/runtime code exists in repo | | ✓ | |
| ER-16 | Live acquisition previously executed for PILOT-001 | | ✓ | |
| ER-17 | Snapshot Level 1 published for this pilot | | ✓ | |
| ER-18 | OCPilot Run 5 completed | | ✓ | |
| ER-19 | Production access planned or used | | ✓ | |
| ER-20 | Risk register reviewed for Execution | ✓ | | |

**Phase 6 honest summary:** **Execution is not ready.** Live-access items remain **SAFE UNKNOWN** or **NO** by design.

---

## 8. Implementation scope reference (non-binding until authorized)

When **Implementation Authorization** is granted, allowed deliverable **categories** (exact location **SAFE UNKNOWN**):

| Category | Boundary |
|----------|----------|
| SFTP Read-Only connector | CON-L1-A only; read-only; fail-closed |
| Evidence assembly | Per [EAR-EVIDENCE-PACKAGE-v1.md](../../EAR-EVIDENCE-PACKAGE-v1.md) |
| Helper scripts | Human-operated; no hidden automation; per [PILOT-GOVERNANCE-v1.md](../../PILOT-GOVERNANCE-v1.md) |

**Explicit non-deliverables:** Restate [PILOT-CHARTER-v1.md](PILOT-CHARTER-v1.md) §4 — no Level 2+, no Hybrid, no prod, no Mode 3, no OCPilot Run 5 completion claim at implementation stage.

---

## 9. Related documents

| Document | Use |
|----------|-----|
| [EXECUTION-PREPARATION-PLAN-v1.md](EXECUTION-PREPARATION-PLAN-v1.md) | Phase 6 stage plan (no execution detail) |
| [PHASE-6-DECISION-v1.md](PHASE-6-DECISION-v1.md) | Phase 6 decision record |
| [SUCCESS-CRITERIA-v1.md](SUCCESS-CRITERIA-v1.md) | Assessment pass conditions |
| [STOP-CONDITIONS-v1.md](STOP-CONDITIONS-v1.md) | Halt triggers |
| [PILOT-001-SITE-001-ASSESSMENT-PLAN-v1.md](../../PILOT-001-SITE-001-ASSESSMENT-PLAN-v1.md) | Assessment taxonomy |

---

## 10. Authorization block (human sign-off — pending)

| Role | Name / ID | Date | Authorizes | Does not authorize |
|------|-----------|------|------------|-------------------|
| Human charter authority | **Pending** | — | Operator Approval; Assessment acceptance | Execution |
| Operator technical lead | **Pending** | — | §4 path bindings when filled | Production; Mode 3 |
| Implementation Authorization | **Pending** | — | Implementation scope per §8 | Execution; live SFTP |
| Execution Authorization | **Not requested** | — | — | — |

**Sub-charter document status:** **DRAFT** — Phase 6 planning complete; **Implementation Authorization** requires resolved §4 fields (or explicit documented waivers per risk register) and G-03 Approval.

---

## 11. Truth statement

| Claim | Accurate? |
|-------|-----------|
| This document authorizes Execution | **No** |
| This document authorizes connector implementation | **No** — only after Implementation Authorization |
| All §4 operational paths resolved | **No** — SAFE UNKNOWN |
| PILOT-001 execution-ready | **No** |
| Phase 6 creates runtime | **No** |
