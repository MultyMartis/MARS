# ISEO-SU-SITE-OPS Phase Model v1

**Status:** ACCEPTED (Phase 1.5)  
**Decision date:** 2026-07-22  
**Canonical locus:** `X:\AI MARS\projects\iseo-su-site-ops\`

---

## PHASE 0 — MARS / SYSTEMS PREFLIGHT

| Field | Value |
|-------|-------|
| **Status** | **COMPLETE** |
| **Goal** | Confirm MARS workspace, volume identity, governance posture, and safe locus recommendation before any site mutation |
| **Inputs** | AGENTS.md, `.cursorrules`, X-drive authority, infrastructure reality, current operational state, project registry |
| **Outputs** | Phase 0 preflight closeout REPORT |
| **HITL gates** | Operator acceptance that Phase 0 is complete and Phase 1 may proceed |
| **Prohibited** | Production access; secrets capture; registry/ATLAS mutation; FTP; WPilot install |
| **Stop condition** | Volume/workspace mismatch → `STOP — X VOLUME IDENTITY MISMATCH`; wrong branch without charter → STOP |

---

## PHASE 1 — CROSS-CHAT KNOWLEDGE INTAKE

| Field | Value |
|-------|-------|
| **Status** | **COMPLETE** |
| **Goal** | Intake WPilot / Plugin / Forge / ATLAS handoffs; reconcile conflicts; record SAFE UNKNOWN |
| **Inputs** | Operator-provided cross-chat handoffs; current WPilot / Forge / ATLAS / Report Hub docs |
| **Outputs** | Cross-chat handoff closeout; Phase 1 REPORT |
| **HITL gates** | Operator confirms reconciliations and authorizes Phase 1.5 |
| **Prohibited** | External access; production action; inventing facts; minting ATLAS IDs |
| **Stop condition** | Unreconciled conflict that would force dual SoT → STOP and escalate |

---

## PHASE 1.5 — PROJECT CHARTER AND LOCUS CREATION

| Field | Value |
|-------|-------|
| **Status** | **COMPLETE** (after Phase 1.5 REPORT) |
| **Goal** | Create canonical locus `projects/iseo-su-site-ops/` and persist Phase 0/1 decisions |
| **Inputs** | Accepted Phase 0/1 decisions; system boundaries; supporting methodology paths |
| **Outputs** | OPERATIONAL-INDEX, README, charter, boundaries, phase model, registers, deferred Firefox record, Phase 1.5 REPORT |
| **HITL gates** | Operator review/acceptance of Phase 1.5 REPORT before Phase 2 |
| **Prohibited** | Production connection; credentials folders; registry row write; ATLAS mint; Localhost mirror; Browser Workstation implementation |
| **Stop condition** | Conflicting existing locus → STOP without overwrite; foreign WIP collision on write path → STOP |

---

## PHASE 2 — NON-SECRET SITE EVIDENCE INTAKE

| Field | Value |
|-------|-------|
| **Status** | **OPEN / AWAITING OPERATOR WAVE A EVIDENCE** (intake structure CREATED 2026-07-22; Phase 2 not COMPLETE) |
| **Goal** | Collect non-secret evidence about i-seo.su structure and tools without production mutation |
| **Inputs** | Operator-provided non-secret materials; public observations only if operator-supplied (no agent crawl) |
| **Outputs** | Evidence intake ledger; evidence request waves; route register; access classification; questionnaire; redaction guide; Phase 2 REPORT |
| **HITL gates** | Phase 2 charter acceptance; Wave A answers; Phase 2A Wave A evidence review before Waves B–E; do not authorize Phase 3 yet |
| **Prohibited** | Credentials; FTP; admin login; REST; plugin install; inventing architecture as verified; agent crawl |
| **Stop condition** | Secret material appears → quarantine procedure; do not store in Git; wait for Wave A if evidence empty |

---

## PHASE 3 — SITE PASSPORT AND HYBRID OWNERSHIP

| Field | Value |
|-------|-------|
| **Status** | **PLANNED** |
| **Goal** | Produce site passport, static/WP boundary map, hybrid SoT matrix, entity/tool maps |
| **Inputs** | Phase 2 non-secret evidence; WPilot site-passport template patterns |
| **Outputs** | `ISEO-SITE-PASSPORT-v1`, boundary map, SoT matrix, WP/custom-tool/ACF maps (as evidence allows) |
| **HITL gates** | Operator acceptance of passport and ownership claims |
| **Prohibited** | Treating OPERATOR-CONTEXT as CONFIRMED; production mutation |
| **Stop condition** | Hybrid ownership unresolved for critical surface → do not proceed to connection planning for that surface |

---

## PHASE 4A — FTP / STATIC CONNECTION PLAN

| Field | Value |
|-------|-------|
| **Status** | **PLANNED** |
| **Goal** | Plan FTP/SFTP/static file connection without configuring live credentials in Git |
| **Inputs** | Passport; access model; ROL checklists; Survivability protected-zone patterns |
| **Outputs** | `FTP-CONNECTION-PLAN-v1` (non-secret) |
| **HITL gates** | Operator approval of plan before any live FTP |
| **Prohibited** | Storing FTP passwords/keys in locus; live FTP use without Phase 6 charter |
| **Stop condition** | Access class unknown → plan remains incomplete; no improvised connection |

---

## PHASE 4B — WPILOT PREINSTALL DECISION

| Field | Value |
|-------|-------|
| **Status** | **PLANNED / OPTIONAL UNTIL APPROVED** |
| **Goal** | Decide whether WPilot plugin is appropriate for WordPress surfaces on i-seo.su |
| **Inputs** | WPilot RC5 docs; clean-install checklist; compatibility SAFE UNKNOWN; passport WP facts |
| **Outputs** | `WPILOT-PLUGIN-CONNECTION-PLAN-v1` or explicit deferral decision |
| **HITL gates** | Operator approve/deny install path |
| **Prohibited** | Install; token creation; REST; treating DEV proof as production readiness |
| **Stop condition** | Compatibility unresolved and operator requires certainty → HOLD |

---

## PHASE 5 — LOCAL MIRROR DECISION

| Field | Value |
|-------|-------|
| **Status** | **PLANNED / DEFAULT DEFER** |
| **Goal** | Decide whether a local mirror under MLI/`X:\MARS-Localhost` is needed |
| **Inputs** | Risk assessment; MLI consumer model; hybrid complexity |
| **Outputs** | `LOCAL-MIRROR-DECISION-v1` |
| **HITL gates** | Operator decision required before any mirror creation |
| **Prohibited** | Creating mirror by default; treating Localhost as production |
| **Stop condition** | Default = defer unless operator charter requires mirror |

---

## PHASE 6 — CONTROLLED CONNECTION

| Field | Value |
|-------|-------|
| **Status** | **NOT AUTHORIZED** |
| **Goal** | Execute tightly scoped, HITL-approved connection and smoke under backup/rollback |
| **Inputs** | Accepted plans; access; backup/rollback model; smoke plans; ROL preflight |
| **Outputs** | Connection evidence; smoke results; incident stops if any |
| **HITL gates** | Explicit connection charter per channel and action class |
| **Prohibited** | Broad sync; unconstrained promote; secret commits; skipping backup for writes |
| **Stop condition** | Any failed preflight / unknown environment / missing rollback → STOP |

---

## PHASE 7 — OPERATIONAL WORK

| Field | Value |
|-------|-------|
| **Status** | **NOT AUTHORIZED** |
| **Goal** | Ongoing bounded operational changes under runbook |
| **Inputs** | Operational runbook; change requests; backups |
| **Outputs** | Change reports; evidence |
| **HITL gates** | Per-change approval for production mutations |
| **Prohibited** | Autonomous writes; foreign WIP entanglement; FP-0002 copy-paste architecture |
| **Stop condition** | Drift without promote discipline → halt and re-passport |

---

## Phase progression rule

```text
COMPLETE phase REPORT
  → operator acceptance
    → next phase charter
      → execute
```

Phase 2 intake documentation is **OPEN**. Phase 2 programme completion requires accepted evidence waves and later closeout — **not** declared COMPLETE by structure creation alone.  
Next gate after Wave A: **PHASE 2A WAVE A EVIDENCE REVIEW**. Phase 3 remains unauthorized until later acceptance.

---

*Phase Model v1 · updated 2026-07-22 (Phase 2 OPEN).*
