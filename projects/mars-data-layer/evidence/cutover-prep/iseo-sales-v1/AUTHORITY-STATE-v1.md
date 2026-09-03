# ISEO Sales — Data Authority State Marker v1

**Canonical store:** `mars_core.apps.metadata` for `app_key = app_iseo_sales`  
**Field:** `data_authority_state`  
**Do not invent** a second competing control-plane state system.

## Progression

1. `SHEETS_PRIMARY`
2. `PG_SHADOW`
3. `PG_CANDIDATE_VALIDATED` ← **current (this prep wave)**
4. `CUTOVER_IN_PROGRESS` ← future human-approved fence only
5. `PG_PRIMARY` ← after final delta + activate v3 + sole intake proof

Companion flags (same JSONB):

- `sheets_sot` — must be `true` until `PG_PRIMARY`
- `pg_runtime` — `shadow_candidate` until cutover
- `data_authority_notes` / `data_authority_updated_at`

Architecture alias: docs also use `CUTOVER` / `SHEETS_PROJECTION` — map `CUTOVER` → `CUTOVER_IN_PROGRESS`; projection is post-`PG_PRIMARY` optional work.

## Current

Observed after prep UPDATE: `PG_CANDIDATE_VALIDATED` with `sheets_sot=true`.  
Sheets remain authoritative. PostgreSQL remains validated shadow/candidate. **No cutover executed.**
