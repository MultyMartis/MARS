# PILOT-001 — Connected Acquisition Pilot Charter v1

**Type:** Pilot charter — authorization and scope only  
**Phase:** 4 — Connected Acquisition Pilot Charter  
**Date:** 2026-06-01  
**Pilot ID:** `PILOT-001`  
**Folder:** [README.md](README.md)

**Prerequisite decision:** [EAR-PHASE-3-DECISION-v1.md](../../EAR-PHASE-3-DECISION-v1.md) — **CONDITIONAL GO** for first pilot charter; architectural blockers: **none**.

**This document does not authorize:** runtime code, connector scripts, SFTP logic, live access, snapshot publication, or site modification.

---

## 1. Pilot identity

| Field | Value |
|-------|-------|
| **Pilot ID** | `PILOT-001` |
| **Pilot slug** | `PILOT-001-SITE-001-SFTP-READONLY` |
| **Target site** | `SITE-001` |
| **Site name** | Автосалон СИБКАР |
| **Platform** | ocStore 3.0.3.8 (rs.2) |
| **Baseline** | `ocstore-3038-rs2` |
| **Environment** | `TEST` |
| **Track** | Connected Acquisition |
| **EAR mode** | **Mode 2** — Connected Read Only |
| **Connector class** | **SFTP Read-Only** |
| **Canonical path** | **CON-L1-A** per [EAR-CONNECTED-PATHS-v1.md](../../EAR-CONNECTED-PATHS-v1.md) |
| **Consumer** | **OCPilot** (SITE-001 Run 5 read-only audit — paused pending acquisition path) |
| **First authorized EAR pilot** | Yes |

---

## 2. Purpose

Validate the **EAR Connected Acquisition** architecture (Phases 1–3, tracks, connector model, snapshot contract, credential boundary, consumer separation) **without performing site modifications** and **without claiming runtime or connector implementation exists**.

The pilot proves — at documentation and (future) controlled execution assessment — that the architecture can govern a read-only SFTP acquisition path toward an honest consumer handoff.

---

## 3. Primary objective

**Primary goal:** Demonstrate that a **future** SFTP Read-Only connector could **theoretically** produce a valid **Snapshot Level 1** for SITE-001 in TEST, per:

- [EAR-SNAPSHOT-CONTRACT-v1.md](../../EAR-SNAPSHOT-CONTRACT-v1.md)
- [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](../../EAR-OPENCART-SNAPSHOT-SPEC-v1.md)
- [EAR-OPENCART-QUALITY-MAPPING-v1.md](../../EAR-OPENCART-QUALITY-MAPPING-v1.md) (Level 1 minimum evidence)
- [EAR-SNAPSHOT-MAPPING-v1.md](../../EAR-SNAPSHOT-MAPPING-v1.md) (SFTP → sections)

**At Charter stage:** “Demonstrate” means **scoped proof plan + architecture traceability** — not live acquisition.

---

## 4. Explicit non-objectives

The following are **out of scope** for PILOT-001 unless a **separate human charter** explicitly expands scope:

| Excluded | Rationale |
|----------|-----------|
| **Snapshot Level 2** | Requires extension inventory + corroboration — hybrid or additional connectors |
| **Snapshot Level 3** | Comprehensive manifest — deferred per Phase 3 recommendation |
| **Operations Layer** | Consumer write/deploy paths — not EAR acquisition |
| **Site modification** | Any write to host, DB, admin, or config |
| **Mode 3** | Forbidden in EAR v1 |
| **Hybrid coordinator pilot** | SFTP + PMA + Admin deferred |
| **SSH / FTP / PMA-only pilots** | Deferred first-connector recommendation |
| **Runtime or connector code** | Phase 4 authorization only |
| **Production environment** | TEST only for this charter |

---

## 5. Architecture validation scope

| Layer | What pilot validates (design / future execution) |
|-------|------------------------------------------------|
| **Track** | Connected Acquisition managed-project model |
| **Workflow** | Request → Acquire → Validate → Publish → Archive |
| **Connector** | SFTP Read-Only → Evidence Package → EAR Validate → Snapshot |
| **Security** | Read-only scope, credential boundary, no secrets in git |
| **Consumer** | OCPilot intake at Level 1 without credential exposure |
| **Honesty** | Partial acquisition, `safe-unknown`, no inflated publish |

**Reference flow:** [EAR-MODE-2-OPENCART-REFERENCE-v1.md](../../EAR-MODE-2-OPENCART-REFERENCE-v1.md)

---

## 6. Request record (G0)

Embedded per [EAR-READINESS-GATES-v1.md](../../EAR-READINESS-GATES-v1.md) G0 and Phase 3 condition #2 (DD-2E-09 template gap).

| G0 field | Value |
|----------|-------|
| `request_id` | `req-pilot-001-site-001-v1` |
| `site_id` | `SITE-001` |
| `environment` | `TEST` |
| `track` | `connected` |
| `ear_mode` | `2` |
| `connector_plan` | Single leg: **SFTP Read-Only** (CON-L1-A) |
| `quality_target` | **Level 1** (honest claim cap for pilot) |
| `consumer` | `ocpilot` |
| `channels approved (charter)** | SFTP read-only list + selective download — **paths and exclusions TBD at Implementation Sub-Charter** |
| `channels excluded** | SSH shell, DB writes, admin write, production |
| `credential_ref` | **SAFE UNKNOWN** until operator names external store path at sub-charter — no values in git |
| `operator_approver` | **Pending** — human signature at Approval stage |
| `waived_risks` | See [RISK-REGISTER-v1.md](RISK-REGISTER-v1.md) |

**Site facts (repo only):** [EAR-SITE-001-ACQUISITION-OPTIONS-v1.md](../../EAR-SITE-001-ACQUISITION-OPTIONS-v1.md). Channel availability on live host: **not verified** in Phase 4.

---

## 7. Acquisition path (theoretical)

```
Operator HITL (Request approved)
    ↓
Future SFTP Read-Only Connector (not implemented in Phase 4)
    ↓
Evidence Package (file listing, version proof files, root inventory)
    ↓
EAR Validate (manual acceptable for pilot per EAR-RUNTIME-READINESS-v1)
    ↓
Candidate Snapshot Level 1
    ↓
Operator Publish (HITL)
    ↓
OCPilot consumer intake
```

**Optional future leg (not in PILOT-001 scope):** PMA metadata for stronger `database-metadata` — would remain Level 1 unless charter amended.

---

## 8. Credential and storage boundaries

| Topic | Charter rule |
|-------|----------------|
| Credentials | External operator store only — [EAR-CREDENTIAL-BOUNDARY-v1.md](../../EAR-CREDENTIAL-BOUNDARY-v1.md) |
| Git | No secrets, no live dumps |
| Evidence quarantine | Named at Implementation Sub-Charter — global paths remain **SAFE UNKNOWN** per storage model |
| Bulk payload | External bulk root — reference in snapshot metadata only |

---

## 9. Waived / accepted soft gaps (pilot-level)

Documented in [RISK-REGISTER-v1.md](RISK-REGISTER-v1.md); acceptable for charter authorization per Phase 3 **CONDITIONAL GO**:

| Gap | Pilot handling |
|-----|----------------|
| No machine-readable snapshot schema | Manual Validate allowed |
| No org-wide vault product | `credential_ref` to operator `secrets/` |
| No connector registry implementation | Pilot folder + STATUS as registry substitute |
| Request template not published | Embedded G0 in this charter |
| Roadmap vs OPERATIONAL-INDEX phase labels | OPERATIONAL-INDEX authoritative |

---

## 10. Pilot lifecycle

```
Charter          ← CURRENT (Phase 4 complete)
    ↓
Approval         ← explicit human HITL sign-off required
    ↓
Implementation Sub-Charter   ← scope for code/access; separate authorization
    ↓
Execution        ← live read-only acquisition (if sub-charter approves)
    ↓
Assessment       ← evidence vs success criteria
    ↓
Lessons Learned  ← [LESSONS-LEARNED.md](LESSONS-LEARNED.md)
```

**Current stage:** **Charter** — see [STATUS.md](STATUS.md).

---

## 11. Related artifacts

| Artifact | Path |
|----------|------|
| Success criteria | [SUCCESS-CRITERIA-v1.md](SUCCESS-CRITERIA-v1.md) |
| Stop conditions | [STOP-CONDITIONS-v1.md](STOP-CONDITIONS-v1.md) |
| Risk register | [RISK-REGISTER-v1.md](RISK-REGISTER-v1.md) |
| Assessment plan (no execution) | [../../PILOT-001-SITE-001-ASSESSMENT-PLAN-v1.md](../../PILOT-001-SITE-001-ASSESSMENT-PLAN-v1.md) |
| Pilot governance | [../../PILOT-GOVERNANCE-v1.md](../../PILOT-GOVERNANCE-v1.md) |

---

## 12. Approvals (charter stage)

| Role | Action | Date | Identifier |
|------|--------|------|------------|
| Charter author (Phase 4 task) | Documented | 2026-06-01 | Agent task closeout |
| Human charter authority | **Pending** | — | Required for Approval stage |

**Signing this charter in git does not constitute Approval** unless a human operator records approval in [STATUS.md](STATUS.md) with identifier and date.

---

## 13. Truth statement

| Statement | Accurate? |
|-----------|-----------|
| EAR foundation complete | Yes (Phases 1–3) |
| First EAR pilot chartered | Yes |
| SFTP connector exists in repo | **No** |
| SITE-001 acquired via Mode 2 | **No** |
| OCPilot Run 5 unblocked | **No** — requires future execution + publish |
| Pilot executed | **No** |
