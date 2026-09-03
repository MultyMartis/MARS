# ISEO Sales — PostgreSQL Cutover Runbook v1

**Document:** `ISEO-SALES-PG-CUTOVER-RUNBOOK-v1`  
**Status:** DESIGN ONLY — **DO NOT EXECUTE** in the prep wave  
**Date:** 2026-09-03  
**App:** `app_iseo_sales`

---

## 0. Preconditions (all must PASS)

1. Topology: **JOINT Operational + Admin PG cutover** approved (Admin.v3.dev ready or Admin Sheets writes fenced).
2. DR: off-host logical backup **PASS** + restore proof **PASS**.
3. Authority marker: `mars_core.apps.metadata.data_authority_state = PG_CANDIDATE_VALIDATED`, `sheets_sot=true`.
4. Workflows:
   - Operational.dev `xSnXPy8cEHoZw6xG` **active**
   - Operational.v3.dev `NH4uV145Amrgnmkm` **inactive** but Gmail+Telegram **wired**
   - Operational.v3.rollback `favawMOzVwtFMdyH` **inactive**
5. Final delta tool ready: `iseo_sales_sheets_to_pg_shadow.py`
6. Human GO recorded.

---

## 1. Cutover fence sequence (future)

1. Announce / start cutover window.
2. Verify Operational.dev is sole Gmail intake.
3. Wait for / inspect in-flight Operational.dev executions (see `in_flight_execution_policy.json`).
4. Fence / deactivate old Gmail intake (Operational.dev → inactive).
5. Record exact cutoff timestamp (UTC).
6. Set authority → `CUTOVER_IN_PROGRESS` in `mars_core.apps.metadata`.
7. Run **FINAL CUTOVER DELTA** (not ordinary shadow refresh):

```text
python projects/mars-data-layer/tools/iseo_sales_sheets_to_pg_shadow.py dry-run
python projects/mars-data-layer/tools/iseo_sales_sheets_to_pg_shadow.py apply
python projects/mars-data-layer/tools/iseo_sales_sheets_to_pg_shadow.py reconcile
```

8. Reconcile: zero unexplained differences; malformed delivery still `LEGACY INVALID ROW`.
9. Declare PostgreSQL authoritative: `data_authority_state=PG_PRIMARY`, `sheets_sot=false`.
10. Activate Operational.v3.dev.
11. Verify candidate active.
12. Verify Operational.dev inactive.
13. Verify exactly one Gmail poller.
14. Natural production observation (no synthetic Telegram).
15. Rollback via [ISEO-SALES-PG-ROLLBACK-RUNBOOK-v1.md](./ISEO-SALES-PG-ROLLBACK-RUNBOOK-v1.md) on hard failure.

---

## 2. Shadow refresh vs final cutover delta

| Class | When | Mutates PG | Authority |
|-------|------|------------|-----------|
| `SHADOW REFRESH` | Sheets still SoT | Optional apply if contract allows | Sheets |
| `FINAL CUTOVER DELTA` | Inside fence after old intake stopped | Required apply + reconcile | Becomes PG |

Operator must not hand-edit SQL/rows.

---

## 3. Post-activate natural acceptance (first window)

- Gmail intake functioning
- First natural new lead persists to PG
- No duplicate inbound
- Lead state correct
- Outbox/delivery correct
- Gmail processed only after DB commit
- No Sheets critical calls on Operational.v3
- No re-intake storm
- No PG errors
- One active intake only
- Admin path also PG-backed (joint cutover)

---

## 4. Sheets after cutover

- Sheets no longer authoritative
- Old production inactive
- No automatic Sheets → PG writeback
- Projection may remain **NOT IMPLEMENTED** (communicate explicitly)

---

## 5. Explicit non-actions of prep wave

This document was created during prep. **No step in §1 was executed.**
