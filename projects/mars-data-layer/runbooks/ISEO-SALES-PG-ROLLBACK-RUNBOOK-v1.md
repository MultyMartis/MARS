# ISEO Sales — PostgreSQL Rollback Runbook v1

**Document:** `ISEO-SALES-PG-ROLLBACK-RUNBOOK-v1`  
**Status:** DESIGN + PIN READY — activate only after future `PG_PRIMARY` hard failure  
**Updated:** 2026-09-03 (Admin.v3.rollback pin)

---

## Hard rule

After PostgreSQL is authoritative and has received production mutations:

- **Operational.dev (Sheets)** is **NOT** a valid rollback for data authority.
- **Admin.dev (Sheets)** is **NOT** a valid automatic rollback after `PG_PRIMARY`.

Rollback must be **PG-compatible** for both Operational and Admin lanes.

---

## Pins

### Operational

| Field | Value |
|-------|-------|
| Name | `i-SEO Sales Manager - Operational.v3.rollback` |
| n8n ID | `favawMOzVwtFMdyH` |
| Status | **INACTIVE** |
| Export | `projects/mars-data-layer/workflows/operational-v3-rollback/Operational.v3.rollback.n8n.json` |
| Registry | `mars_core.workflow_releases` family=`operational_intake` status=`rollback` |

### Admin

| Field | Value |
|-------|-------|
| Name | `i-SEO Sales Manager - Admin.v3.rollback` |
| n8n ID | `8uStgSN9brsxmz6g` |
| Status | **INACTIVE** |
| Export | `projects/mars-data-layer/workflows/admin-v3-rollback/Admin.v3.rollback.n8n.json` |
| Hash (with id) | `1e19672ac9a9ef79783a475e8950d33c007aba1237a58c0fd29434c6eb037f6a` |
| Registry | `mars_core.workflow_releases` family=`admin_runtime` status=`rollback` |

Credential (both): `ISEO Runtime PG (v3)` / `XCmmOgzZ1RWT4Fg3` (no secret in docs). Role: `iseo_runtime`.

---

## Future joint rollback sequence (post `PG_PRIMARY` failure)

1. Deactivate failed active v3 Admin and/or Operational workflow(s).
2. Prove no competing Gmail intake / Admin Telegram webhook remains on failed workflows.
3. Activate PG-compatible rollback pin(s) matching the failed lane(s):
   - Operational → `favawMOzVwtFMdyH`
   - Admin → `8uStgSN9brsxmz6g`
4. Prove exactly one Gmail intake and one Admin Telegram intake as required.
5. **Preserve PostgreSQL as authoritative** (`data_authority_state` stays `PG_PRIMARY` or documented repair — never silent Sheets SoT).
6. Do **not** switch back to Sheets Admin.dev / Operational.dev automatically.
7. File incident evidence; repair forward on PG.

---

## Pre-cutover rollback (before SoT switch)

If cutover is aborted before `PG_PRIMARY`:

1. Keep / restore Operational.dev + Admin.dev active.
2. Keep all v3 + rollback pins inactive.
3. Leave `data_authority_state` at `PG_CANDIDATE_VALIDATED` or revert with operator note.
4. Sheets remain SoT.

---

## Triggers

See `evidence/cutover-prep/iseo-sales-v1/rollback_triggers.json`.
