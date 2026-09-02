# n8n Data Contract Standard v1

**Document:** `N8N-DATA-CONTRACT-STANDARD-v1`  
**project_id:** `mars-data-layer`  
**Date:** 2026-09-03

---

## 1. Purpose

Define how n8n workflows interact with the MARS PostgreSQL data plane without turning workflows into ad-hoc DDL/SQL platforms.

---

## 2. Workflow versioning

| Rule | Detail |
|------|--------|
| Production frozen | Substantial redesign requires a **new** workflow ID/version |
| Candidate | Inactive until validation gate |
| One active intake | Only one intake path authoritative per product at a time |
| Record version | Persist `workflow_version` (or equivalent) on jobs/events |

No substantial in-place redesign of live production graphs.

---

## 3. Correlation and idempotency

Every mutating operational path should carry:

- `correlation_id` — ties intake → process → delivery → audit;
- idempotency / `dedupe_key` — prevents duplicate leads, duplicate Telegram sends, duplicate job enqueues.

Idempotency is enforced in PostgreSQL (unique constraints + Toolkit ops), not only in Sheets formulas.

---

## 4. DB operation boundaries

n8n may:

- call **MARS DB Toolkit** operations / approved parameterized queries;
- call narrow SQL **functions** granted to runtime roles;
- read via reader roles for diagnostics when chartered.

n8n must not:

- run arbitrary AI-composed SQL;
- perform DDL;
- use superuser credentials;
- hold transactions across LLM/HTTP waits.

---

## 5. Parameterized queries and atomic multi-table mutations

- All SQL uses bind parameters.
- Multi-table business mutations prefer a single DB function / transaction owned by Toolkit.
- Partial failure must leave a recoverable state (outbox + job retry), not silent split-brain.

---

## 6. AI prohibition

AI nodes/agents:

- invoke **named Toolkit ops** only;
- never receive credentials that allow unrestricted write SQL;
- agent roles are **narrower** than runtime roles.

---

## 7. Cutover compatibility

During shadow:

- Sheets remain SoT;
- PG writes are shadow/validation;
- workflows must be able to disable PG path without data-loss on Sheets.

After cutover:

- PG is SoT;
- Sheets projection is async/optional;
- **old Sheets-primary workflow is not a valid SoT rollback**.

---

## 8. Post-cutover rollback compatibility

Candidate workflows should:

- keep `workflow_version` distinguishable;
- avoid destructive one-way transforms without dump;
- support forward-fix of PG state rather than “reactivate Sheets SoT.”

---

## 9. Error contract

Structured error fields (conceptual): `code`, `retryable`, `correlation_id`, `safe_message`, optional `detail_ref` (not raw secrets).
