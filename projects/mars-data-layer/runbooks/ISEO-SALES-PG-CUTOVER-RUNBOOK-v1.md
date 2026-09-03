# ISEO Sales — PostgreSQL Cutover Runbook v1

**Document:** `ISEO-SALES-PG-CUTOVER-RUNBOOK-v1`  
**Status:** DESIGN ONLY — **DO NOT EXECUTE** in candidate waves  
**Updated:** 2026-09-03 (Admin.v3.dev candidate wave)  
**App:** `app_iseo_sales`

---

## 0. Preconditions (all must PASS)

1. Topology: **JOINT Operational + Admin PG cutover** (both v3 candidates ready).
2. DR: off-host logical backup **PASS** + restore proof **PASS** (prep residual may still block GO).
3. Authority marker: `mars_core.apps.metadata.data_authority_state = PG_CANDIDATE_VALIDATED`, `sheets_sot=true` until fence.
4. Workflows (expected pre-cutover):

| Workflow | ID | Status |
|----------|----|--------|
| Operational.dev | `xSnXPy8cEHoZw6xG` | **ACTIVE** |
| Admin.dev | `wLrLp4WQHm1VJmxz` | **ACTIVE** |
| Operational.v3.dev | `NH4uV145Amrgnmkm` | **INACTIVE** |
| Admin.v3.dev | `Zk9b1BiXpYN9rMMo` | **INACTIVE** |
| Operational.v3.rollback | `favawMOzVwtFMdyH` | **INACTIVE** |
| Admin.v3.rollback | `8uStgSN9brsxmz6g` | **INACTIVE** |

5. Final delta tool ready: `iseo_sales_sheets_to_pg_shadow.py`
6. Human GO recorded.

---

## 1. Joint cutover fence sequence (future — DO NOT RUN NOW)

1. Old Operational.dev **active**; old Admin.dev **active**; both v3 candidates **inactive**.
2. Preflight: DR, ACCESS shadow parity, current lead state, one Gmail intake, Admin Telegram webhook on Admin.dev only.
3. Fence old **Operational** intake (stop Gmail poller / deactivate Operational.dev intake path).
4. Fence old **Admin** mutation intake / Telegram handling (deactivate Admin.dev Telegram trigger path so webhook is free for Admin.v3).
5. Wait / reconcile in-flight executions on both old workflows.
6. Final Sheets→PG delta + reconcile (malformed delivery remains `LEGACY INVALID ROW`).
7. Verify ACCESS + current lead state in PostgreSQL.
8. Mark `data_authority_state=PG_PRIMARY`, `sheets_sot=false`.
9. Activate **Operational.v3.dev**.
10. Activate **Admin.v3.dev** (Telegram trigger wiring only at this step — never before).
11. Verify old Operational.dev and Admin.dev **inactive**.
12. Verify exactly **one** Gmail intake.
13. Verify exactly **one** Telegram Admin intake (Admin.v3).
14. Natural production acceptance (no synthetic Telegram to Olya/customers).
15. On hard failure: joint PG rollback runbook — **never** auto-reactivate Sheets Admin.dev / Operational.dev as SoT after `PG_PRIMARY`.

---

## 2. Shadow refresh vs final cutover delta

| Class | When | Mutates PG | Authority |
|-------|------|------------|-----------|
| `SHADOW REFRESH` | Sheets still SoT | Optional apply if contract allows | Sheets |
| `FINAL CUTOVER DELTA` | Inside fence after old intakes stopped | Required apply + reconcile | Becomes PG |

Operator must not hand-edit SQL/rows.

---

## 3. Post-activate natural acceptance (first window)

- Gmail intake functioning (Operational.v3)
- Admin Telegram commands/callbacks on Admin.v3 only
- First natural new lead persists to PG
- No duplicate inbound
- Lead status actions via `change_lead_status` / Admin closed ops
- Reminder digest/group navigation from PG (no Sheets 429)
- Outbox/delivery correct
- Gmail processed only after DB commit
- No Sheets critical calls on either v3 workflow
- No re-intake storm
- No PG errors
- One Gmail + one Admin Telegram intake only

---

## 4. Sheets after cutover

- Sheets no longer authoritative
- Old production inactive
- No automatic Sheets → PG writeback
- No Admin PG → Sheets sync in v1
- Projection may remain **NOT IMPLEMENTED** (communicate explicitly)

---

## 5. Explicit non-actions of Admin.v3 candidate wave

This document was updated during Admin.v3 candidate preparation. **No step in §1 was executed.**
No Admin.v3 / Operational.v3 activation. No SoT switch. No live Telegram tests.
