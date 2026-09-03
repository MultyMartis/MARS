# ISEO Sales — PostgreSQL Rollback Runbook v1

**Document:** `ISEO-SALES-PG-ROLLBACK-RUNBOOK-v1`  
**Status:** DESIGN + PIN READY — activate only after future `PG_PRIMARY` hard failure  
**Date:** 2026-09-03

---

## Hard rule

After PostgreSQL is authoritative and has received production mutations, **Operational.dev (Sheets)** is **NOT** a valid rollback for data authority.

Rollback must be **PG-compatible**.

---

## Pin (prep wave)

| Field | Value |
|-------|-------|
| Name | `i-SEO Sales Manager - Operational.v3.rollback` |
| n8n ID | `favawMOzVwtFMdyH` |
| Status | **INACTIVE** |
| Runtime | PostgreSQL `app_iseo_sales` |
| Export | `projects/mars-data-layer/workflows/operational-v3-rollback/Operational.v3.rollback.n8n.json` |
| Hash (with id) | `ac28d8e5268a57390713397e7cc960e5f9742fd75a130b44381bcd632c61607d` |
| Registry | `mars_core.workflow_releases` status=`rollback` |

Credential: `ISEO Runtime PG (v3)` / `XCmmOgzZ1RWT4Fg3` (no secret in docs).

---

## Future rollback sequence (post `PG_PRIMARY` failure)

1. Deactivate current active v3 (`NH4uV145Amrgnmkm` or whichever production v3 ID is live).
2. Prove no active execution / Gmail intake remains on the failed workflow.
3. Activate PG-compatible rollback workflow `favawMOzVwtFMdyH` (after confirming Gmail/Telegram wiring matches accepted contract).
4. Prove exactly one Gmail intake.
5. **Preserve PostgreSQL as authoritative** (`data_authority_state` stays `PG_PRIMARY` or moves to a documented repair state — never silent Sheets SoT).
6. Do **not** switch back to Sheets automatically.
7. File incident evidence; repair forward on PG.

---

## Pre-cutover rollback (before SoT switch)

If cutover is aborted before `PG_PRIMARY`:

1. Keep / restore Operational.dev active.
2. Keep v3 + rollback inactive.
3. Leave `data_authority_state` at `PG_CANDIDATE_VALIDATED` or revert to `PG_SHADOW` / `SHEETS_PRIMARY` with operator note.
4. Sheets remain SoT.

---

## Triggers

See `evidence/cutover-prep/iseo-sales-v1/rollback_triggers.json`.
