# EAR Pilot Governance v1

**Purpose:** Define how **EAR pilots** relate to runtime, production, and architecture — and who may authorize progression.  
**Phase:** 4 foundation  
**Status:** documentation governance only — **not** a policy engine, **not** automated enforcement  
**First pilot:** [pilots/PILOT-001-SITE-001-SFTP-READONLY/](pilots/PILOT-001-SITE-001-SFTP-READONLY/)

---

## 1. What is an EAR pilot?

An **EAR pilot** is a **human-chartered, bounded experiment** that validates acquisition architecture and (optionally, under separate authorization) controlled read-only execution — **without** implying product runtime, connector shipping, or consumer audit completion.

| Pilot is | Pilot is not |
|----------|--------------|
| Scoped authorization + evidence plan | Production service |
| Architecture and process validation | Default automation |
| Traceable folder + STATUS lifecycle | Connector registry product |
| Input to Phase 5+ decisions | Proof MARS hosts live EAR runtime |

---

## 2. Pilot vs Runtime

| Dimension | Pilot | Runtime (future) |
|-----------|-------|------------------|
| **Exists in repo today** | Charter docs in `pilots/` | **No** — unless future sub-charter + implementation |
| **Code** | Forbidden in charter phase unless sub-charter | Connectors, orchestration helpers |
| **Access** | Forbidden until Execution stage + sub-charter | Live SFTP/SSH sessions |
| **Success** | Assessment vs criteria | Repeatable operator runs |
| **Failure mode** | Stop pilot; no silent fallback | Connector status + fail closed |

**Rule:** Completing **Phase 4 Pilot Charter** does **not** create or authorize runtime.

**Rule:** Naming a connector class (e.g. SFTP Read-Only) in a pilot is **not** an implementation claim.

---

## 3. Pilot vs Production

| Dimension | Pilot | Production |
|-----------|-------|------------|
| **Environment** | Declared per charter (PILOT-001: **TEST** only) | Not in scope unless new charter |
| **Site impact** | Read-only; no modification | Operational changes require separate governance |
| **Publish** | HITL; may never occur | Consumer-facing continuity |
| **Credentials** | External; pilot-scoped refs | Rotation and access reviews |

**Rule:** Production acquisition requires a **new charter** — not an extension of TEST pilot.

**Rule:** Drift to production host triggers **stop conditions** — see pilot [STOP-CONDITIONS-v1.md](pilots/PILOT-001-SITE-001-SFTP-READONLY/STOP-CONDITIONS-v1.md).

---

## 4. Pilot vs Architecture

| Dimension | Pilot | Architecture (Phases 1–3) |
|-----------|-------|---------------------------|
| **Mutability** | Pilot may waive soft gaps with register | Foundation frozen at documentation level |
| **Contradiction** | Pilot cannot override Mode 3 ban or write access | Architecture wins — pilot must stop |
| **Extensions** | Hybrid connectors, Level 2+ need charter amendment | Documented in EAR-CONNECTED-PATHS etc. |
| **Evidence** | Pilot produces assessment artifacts | Specs define what “valid” means |

**Rule:** Pilots **test** architecture; they do **not** replace canonical EAR documents.

**Rule:** If pilot execution reveals architectural gap, **stop** and fix architecture via governed doc change — not silent pilot exception.

---

## 5. Approval boundaries

### 5.1 Lifecycle gates

| Stage | What it authorizes | Who authorizes |
|-------|-------------------|----------------|
| **Charter** | Scope, criteria, risks, assessment plan | Phase task + **pending** human charter authority |
| **Approval** | Progression past charter; may plan sub-charter | **Human charter authority** (HITL) |
| **Implementation Sub-Charter** | Code, scripts, credential use plan, paths | **Human** — separate document; not implied by Phase 4 |
| **Execution** | Live read-only acquisition | Human + sub-charter + preflight |
| **Assessment** | Pass/fail vs success criteria | Human assessor |
| **Lessons Learned** | EAR / pilot updates | Human + optional doc PR |

**MARS default:** Cursor agents **document** charters; they do **not** self-approve Execution or Production access.

### 5.2 What agents may do

| Allowed | Forbidden |
|---------|-----------|
| Author pilot documentation under explicit task charter | Approve live access |
| Update STATUS when task says charter complete | Store credentials in repo |
| Reference SAFE UNKNOWN | Claim pilot executed |

### 5.3 Phase boundaries (OPERATIONAL-INDEX)

| Phase | Authorizes |
|-------|------------|
| 3 | Pilot **charter** may be written (CONDITIONAL GO) |
| 4 | First pilot **charter package** (this phase) |
| 5 | Implementation Readiness Review — **not** automatic implementation |
| Execution | Only after sub-charter + Approval |

---

## 6. When a pilot must stop

Immediate stop per pilot stop conditions plus:

| Trigger | Action |
|---------|--------|
| Any stop condition in pilot STOP-CONDITIONS | Halt per protocol |
| Human revocation | Freeze STATUS |
| Phase 5 NO-GO | No Implementation Sub-Charter |
| Security incident | Halt + operator incident process |
| Scope creep without amendment | Halt |
| Architecture contradiction | Halt; fix docs |

**No “soft continue”** after credential exposure or inflated publish.

---

## 7. Pilot registry (documentation)

| Pilot ID | Folder | Stage |
|----------|--------|-------|
| `PILOT-001` | [pilots/PILOT-001-SITE-001-SFTP-READONLY/](pilots/PILOT-001-SITE-001-SFTP-READONLY/) | Charter |

Future pilots: new folder `PILOT-NNN-…` + update this table.

---

## 8. Related documents

| Document | Use |
|----------|-----|
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Phase status |
| [EAR-PHASE-3-DECISION-v1.md](EAR-PHASE-3-DECISION-v1.md) | CONDITIONAL GO |
| [PILOT-001-SITE-001-ASSESSMENT-PLAN-v1.md](PILOT-001-SITE-001-ASSESSMENT-PLAN-v1.md) | Assessment only |
| [AGENTS.md](../../AGENTS.md) | HITL, SAFE UNKNOWN, REPORT |

---

## 9. Truth statement

| Claim | Accurate? |
|-------|-----------|
| Pilot governance is automated | **No** |
| PILOT-001 approved for Execution | **No** |
| Pilot = runtime | **No** |
