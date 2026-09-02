# MARS Bot Data Platform — Roadmap

**project_id:** `mars-data-layer`  
**Status:** Architecture V1 / Foundation  
**Last updated:** 2026-09-03

Phases are **sequential gates**. Later phases must not start without explicit human charter when they touch production.

---

## Phase 0 — Current Sheets incident containment

**Goal:** Minimal containment only for live Sheets/workflow incidents.

- Stabilize production behavior without redesigning Sheets as a long-term architecture.
- Do **not** perfect Sheets schema or build a permanent Sheets platform.
- Capture incident facts for later PG mapping (dedupe, retry, delivery gaps).

**Exit:** Production stable enough to design PG shadow without firefighting.

---

## Phase 1 — PostgreSQL Foundation

**Owner:** `Pro: MARS Server Ops pt.2`  
**Handoff:** [runbooks/SERVER-OPS-POSTGRES-FOUNDATION-HANDOFF-v1.md](runbooks/SERVER-OPS-POSTGRES-FOUNDATION-HANDOFF-v1.md)

- PostgreSQL 18 container on `VEESP-N8N-01`
- Persistent volume, internal Docker network with n8n
- No public `5432`
- Healthcheck, logs, resource baseline, backup hooks
- Secret handoff mechanism

**Exit:** Empty healthy `mars` database reachable only from approved internal clients.

---

## Phase 2 — MARS Data Layer v1

**Owner:** this project

- `mars_core` (small)
- Roles / grants specification
- Migration toolchain + standards applied
- MARS DB Toolkit **base** (narrow validated operations)

**Exit:** Core schemas + Toolkit contract usable in local/dev; production apply only under migration standard.

---

## Phase 3 — i-SEO Sales Manager data model

- Map Sheets concepts → relational model (`app_iseo_sales`)
- Primitives: jobs, events, errors, idempotency, audit, outbox
- No blind 1:1 Sheet→table copy

**Exit:** Approved schema + migration set for Sales Manager (still Sheets-primary).

---

## Phase 4 — PG shadow / import / validation

- Sheets remains Source of Truth
- Dual-write or import/shadow validation
- Reconciliation reports

**Exit:** Shadow data quality accepted; candidate workflow design unlocked.

---

## Phase 5 — Operational.v3.dev

- **New** workflow version/ID (inactive until gate)
- PostgreSQL-backed candidate
- Production Operational.dev remains frozen

**Exit:** Candidate validated in controlled environment.

---

## Phase 6 — Controlled cutover

States: `SHEETS_PRIMARY` → `PG_SHADOW` → `PG_CANDIDATE_VALIDATED` → `CUTOVER` → `PG_PRIMARY`

**Exit:** PostgreSQL authoritative for Sales Manager domain data.

---

## Phase 7 — Google Sheets projection

- One-way async projection / manual command UI
- Sheets no longer authoritative

**Exit:** Projection lag/SLA acceptable; operators trained.

---

## Phase 8 — SEO Content Agent migration

- Schema `app_seo_content`
- Same versioning/cutover discipline as Sales Manager

**Exit:** Content agent on PG-primary (or shadow-complete pending cutover charter).

---

## Phase 9 — Hardening / DR / restore tests

- Nightly logical backups, off-VPS copy
- Restore drills
- Beget evaluated as off-host target (not hot replica by default)

**Exit:** Documented restore success within retention policy.

---

## Phase 10 — Scale only when evidence requires

Triggers only (not premature):

- separate DB per app;
- separate DB host;
- PgBouncer;
- HTTP Data Gateway;
- pgvector;
- dedicated queue.

---

## Current position

**Completed this wave:** Architecture V1 + local development contract + registry registration (documentation).  
**Next:** Local schema design (post–Architecture V1 gate).
