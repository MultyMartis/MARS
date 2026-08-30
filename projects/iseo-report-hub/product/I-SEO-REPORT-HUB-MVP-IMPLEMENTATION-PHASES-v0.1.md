# I-SEO Report Hub — MVP Implementation Phases v0.1

**Status:** PLANNING — phased implementation roadmap  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-24  
**Implementation:** **NOT STARTED** — phases not executed

**Basis:** [PHP + MySQL MVP Technical Brief](I-SEO-REPORT-HUB-PHP-MYSQL-MVP-TECHNICAL-BRIEF-v0.1.md), [Platform Decision](I-SEO-REPORT-HUB-PLATFORM-DECISION-v0.1.md)

---

## How to use this document

Each phase is a **future** HITL-gated work package. This file does **not** authorize code, SQL, Laragon, or demo changes.

For each phase below:

- **Goal** — what success means
- **Deliverables** — expected artifacts
- **Allowed writes (future)** — where future charters may write
- **Validation** — how to verify
- **HITL gate** — human approval before next phase

---

## Phase 0 — Runtime confirmation / local scaffold charter

| Field | Content |
|-------|---------|
| **Goal** | Verify Laragon/PHP/MySQL identity; choose runtime layout; write implementation charter |
| **Deliverables** | Runtime confirmation notes; chosen Option A/B layout; ignore rules plan; Phase 0 charter |
| **Allowed writes (future)** | Docs under `projects/iseo-report-hub/`; optional empty scaffold only if charter lists exact paths |
| **Validation** | Volume/path/version evidence recorded; no secrets committed |
| **HITL gate** | Operator approves runtime layout and Phase 1 start |

---

## Phase 1 — App skeleton + config + auth baseline

| Field | Content |
|-------|---------|
| **Goal** | Bootable PHP app with config loading and login/session |
| **Deliverables** | Front controller / light MVC; config; login/logout; password hashing; CSRF baseline |
| **Allowed writes (future)** | Chartered app paths under Localhost or project `app\` |
| **Validation** | Login works locally; unauthenticated routes blocked |
| **HITL gate** | Operator smoke-test login |

---

## Phase 2 — DB schema + seed demo data

| Field | Content |
|-------|---------|
| **Goal** | Create MVP tables and sanitized seed data |
| **Deliverables** | Migration/SQL scripts (chartered); seed users/clients/projects/periods |
| **Allowed writes (future)** | Schema files in app; local DB only |
| **Validation** | Schema matches Schema Draft; seed loads; no real private client metrics |
| **HITL gate** | Operator reviews schema + seed |

---

## Phase 3 — Clients / projects / sites / periods

| Field | Content |
|-------|---------|
| **Goal** | CRUD for core org structure and reporting periods |
| **Deliverables** | Screens/routes for clients, projects, sites, periods |
| **Allowed writes (future)** | App modules for entities above |
| **Validation** | Role-scoped create/list/detail works |
| **HITL gate** | Operator walkthrough |

---

## Phase 4 — Specialist workspace MVP

| Field | Content |
|-------|---------|
| **Goal** | Primary specialist fill surface for assigned periods |
| **Deliverables** | Workspace screen aligned to demo v0.4 UX intent |
| **Allowed writes (future)** | Workspace views/controllers |
| **Validation** | Specialist sees assigned only; navigation to week/month |
| **HITL gate** | Operator accepts workspace MVP |

---

## Phase 5 — Weekly checkpoints

| Field | Content |
|-------|---------|
| **Goal** | Week 1–3 editors with states and blocks |
| **Deliverables** | Weekly editor; save; state transitions |
| **Allowed writes (future)** | Weekly checkpoint modules |
| **Validation** | Lifecycle states match Report Lifecycle v0.1 |
| **HITL gate** | Operator reviews weekly flow |

---

## Phase 6 — Monthly report editor

| Field | Content |
|-------|---------|
| **Goal** | Month-close editor with synthesis, not blind rollup |
| **Deliverables** | Monthly editor; block values; KPI notes |
| **Allowed writes (future)** | Monthly report modules |
| **Validation** | Submit-to-review path works |
| **HITL gate** | Operator reviews monthly editor |

---

## Phase 7 — Review workflow

| Field | Content |
|-------|---------|
| **Goal** | Lead review queue: request changes / approve |
| **Deliverables** | Review screens; comments; state transitions |
| **Allowed writes (future)** | Review modules + audit events |
| **Validation** | Specialist cannot approve; Lead can |
| **HITL gate** | Operator reviews role gates |

---

## Phase 8 — Published snapshot / client report

| Field | Content |
|-------|---------|
| **Goal** | Publish immutable snapshot; client token URL |
| **Deliverables** | Snapshot builder; `/p/{token}` renderer; supersede/revoke rules |
| **Allowed writes (future)** | Publishing modules |
| **Validation** | Client URL never shows live draft/internal notes |
| **HITL gate** | Operator publish smoke-test |

---

## Phase 9 — Evidence / files security

| Field | Content |
|-------|---------|
| **Goal** | Safe uploads and private file serving |
| **Deliverables** | Upload pipeline; private storage; download auth; link evidence |
| **Allowed writes (future)** | Evidence modules; private upload dir outside docroot |
| **Validation** | Direct URL to upload file denied without auth |
| **HITL gate** | Operator security spot-check |

---

## Phase 10 — QA / demo migration from static prototype

| Field | Content |
|-------|---------|
| **Goal** | Map demo v0.4 flows onto real app; close gaps |
| **Deliverables** | QA checklist; gap list vs demo; UX polish within MVP |
| **Allowed writes (future)** | App UI fixes; docs QA notes — **not** required demo HTML rewrite unless chartered |
| **Validation** | End-to-end period → publish path works with seed data |
| **HITL gate** | Operator accepts MVP demo on PHP app |

---

## Phase 11 — Deployment / backup decision

| Field | Content |
|-------|---------|
| **Goal** | Decide production host, backup, deploy path |
| **Deliverables** | Deployment decision doc; backup strategy; go-live checklist |
| **Allowed writes (future)** | Ops docs under programme; no production deploy without separate charter |
| **Validation** | Hosting/backup ownership named; secrets path defined |
| **HITL gate** | Operator approves production approach |

---

## Phase dependency (summary)

```
0 → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10 → 11
```

Phases 5–6 may overlap slightly after Phase 4 if chartered; Phase 8 must not precede Phase 7 approval path. Phase 9 may start earlier in parallel with 5–8 **only** if upload paths are stubbed safely.

---

## Boundaries

- **Do not implement** any phase from this document alone.
- Each phase needs its own explicit operator charter.
- Foreign WIP and demo workspace remain out of scope unless a phase charter explicitly includes them.
