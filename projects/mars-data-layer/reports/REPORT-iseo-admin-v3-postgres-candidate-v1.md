# REPORT — ISEO Admin.v3.dev PostgreSQL candidate v1

**Document:** `REPORT-iseo-admin-v3-postgres-candidate-v1`  
**Date:** 2026-09-03  
**Process-line:** ISEO SALES MANAGER — ADMIN V3 POSTGRES CANDIDATE / JOINT PG CUTOVER  
**Mode:** Agent — Cursor Auto  
**Cutover executed:** NO

---

## 1. Verdict

**ADMIN V3 POSTGRES CANDIDATE PASS — JOINT PG CUTOVER READY AFTER DR GATE**

Inactive `Admin.v3.dev` exists with PG-authoritative closed contracts, zero Google Sheets nodes on critical path, zero Telegram trigger collision, offline parity tests PASS, and `Admin.v3.rollback` pin registered. Production `Admin.dev` remains ACTIVE. Joint cutover still blocked by prior DR residual (`OFF_HOST_BACKUP` / `RESTORE_PROOF`) until that gate PASS.

---

## 2. Current Admin.dev

| Field | Value |
|-------|-------|
| Name | `i-SEO Sales Manager - Admin.dev` |
| ID | `wLrLp4WQHm1VJmxz` |
| Status | **ACTIVE** |
| Authority | Google Sheets |
| Sheets WRITE paths | **11** |
| Topology | JOINT OPERATIONAL + ADMIN PG CUTOVER REQUIRED |

---

## 3. Admin.v3.dev

| Field | Value |
|-------|-------|
| Name | `i-SEO Sales Manager - Admin.v3.dev` |
| ID | `Zk9b1BiXpYN9rMMo` |
| Status | **INACTIVE** |
| Export | `projects/mars-data-layer/workflows/admin-v3-dev/Admin.v3.dev.n8n.json` |
| Export hash | `6c8526b255d41cd302d09dcc04450fa8cdf61047ea1898accbb565440cc5dfb1` |
| Trigger | Manual inject only (no Telegram Trigger) |
| PG credential | `ISEO Runtime PG (v3)` / `XCmmOgzZ1RWT4Fg3` / role `iseo_runtime` |
| Sheets nodes | **0** |

---

## 4. Functional inventory

Full matrix: `evidence/candidate-workflow/iseo-admin-v3/admin_dev_functional_inventory.md`.

Covered: `/help`, `/status`, `/ai_status`, `/health`, `/stats`, `/last_error`, `/config`, `/ai_on`/`/ai_off`, `/leads`, reminder digest/group/exact lead, callbacks Processed/Spam, canonical cards, ACCESS, deliveries, current-state, errors, config mutations.

---

## 5. Sheets WRITE migration

All **11** Admin.dev Sheets WRITE nodes mapped — see `sheets_write_migration_matrix.json`.

Critical authoritative Sheets writes in Admin.v3: **0**.  
`Append PROFILE_EVENTS` classified **DEFERRED** (not critical Admin.v3 SoT); still accounted.

---

## 6. PG data contracts

Migration: `database/app_iseo_sales/migrations/0006_admin_v3_runtime_functions.sql` applied.

Closed functions (no `execute_sql` / generic update):

- `check_access`, `set_config_value`
- `get_admin_health`, `get_admin_status_snapshot`, `get_admin_stats`, `get_last_error`
- `list_leads_page`, `list_pending_lead_groups`, `get_pending_leads_in_group`
- `get_lead_card_payload`
- `admin_callback_lead_action` → `change_lead_status`
- `claim_reminder_window`, `record_reminder_delivery`, `update_delivery_message_binding`
- `admin_runtime_call` allowlist dispatcher

Toolkit: `toolkit/ops_iseo_sales.py` extended with matching Admin ops.

---

## 7. ACCESS

Authority target: `app_iseo_sales.access_rules`.  
Synthetic + shadow read validation PASS.  
No revoke/restore of Olya / MOD_* during wave.  
Known production principals (ADMIN_A, MOD_B/Olya active; MOD_A/MOD_C revoked) treated as read-only parity targets.

---

## 8. Lead status actions

Flow: callback fixture → ACCESS → `admin_callback_lead_action` → `change_lead_status` → events/audit → card payload.  
No Sheet row mutate reconstruct path.

Tests: pending→processed, pending→spam, denied actor — PASS.

---

## 9. Idempotency

Repeated callback / stable callback identity: **PASS** (`ACTION_IDEMPOTENT_OK`).  
Contract uses idempotency / current version checks inside status transition path.

---

## 10. Reminders

Digest grouping, claim window, delivery record, group navigation from PG — PASS.  
Sheets 429 historical failure mode eliminated for Admin.v3 reminder reads.

---

## 11. Canonical cards

Pending actionable: `✅ Обработано`, `🚫 Спам`, `📄 Исходная заявка`.  
Terminal processed/spam reflected via lifecycle.  
Stray standalone `Карточка` forbidden in builder.  
No live Telegram card sends in this wave.

---

## 12. `/leads`

`list_leads_page` from PostgreSQL — PASS. Statuses/grouping/pagination via closed function args.

---

## 13. `/health`

`get_admin_health` returns component statuses; single dependency failure must not silently drop response. Offline harness PASS (`COMMANDS_OK`).

---

## 14. `/status` / `/stats`

PG snapshot/stats — **AVAILABLE FROM PG**.  
Historical Sheets-only metrics: **LEGACY HISTORY ONLY** / **DEFERRED** where not migrated — not fabricated.

---

## 15. Config / AI state

`set_config_value` rejects secret-like keys.  
Tests mutated only namespaced `adminv3test.ai.enabled`.  
Live production AI state **not** changed. Zero-token mode preserved as operator policy.

---

## 16. Errors

`/last_error` → `get_last_error` / `errors`.  
Sheets ERRORS not authoritative for Admin.v3. No active retry of historical Sheets errors.

---

## 17. Delivery / outbox

Reminder/card delivery binding via `deliveries` + `record_reminder_delivery` / `update_delivery_message_binding`.  
Candidate Telegram path is dry-run; `answerCallbackQuery` documented as deferred boundary / dry-run (not full outbox for immediate ACK).

---

## 18. Credential / security

Reused `iseo_runtime` credential — least-privilege sufficient for closed grants.  
No postgres / mars_admin / mars_migrator in Admin.v3 runtime.  
No password in Git/chat/evidence.  
**SECURITY RESIDUAL — MAY BE REMEDIATED AFTER CUTOVER** (encryptionKey) unchanged.

---

## 19. Telegram trigger safety

Admin.v3 Telegram Trigger nodes: **0**.  
Collision with production webhook: **0**.  
Admin.dev remains ACTIVE intake. Evidence: `telegram_trigger_safety.json`, `active_state_proof.json`.

---

## 20. Test methodology

Offline SQL harness namespace `adminv3test_%` + Manual inject workflow contract.  
Synthetic Telegram messages: **0**. Live callbacks: **0**. Olya/customer traffic: **0**.  
Cleanup of synthetic rows after tests: OK.

---

## 21. Acceptance

| Gate | Expected | Result |
|---|---|---|
| Admin.v3 created | YES | YES |
| Admin.v3 active | NO | NO |
| Admin.dev active | YES | YES |
| PG authoritative candidate path | YES | YES |
| Sheets authoritative writes in Admin.v3 | 0 | 0 |
| Lead action idempotency | PASS | PASS |
| ACCESS parity | PASS | PASS |
| Reminder PG reads | PASS | PASS |
| Card parity | PASS | PASS |
| /health resilience | PASS | PASS |
| Olya test traffic | 0 | 0 |
| Customer test traffic | 0 | 0 |
| Telegram trigger collision | 0 | 0 |
| Cutover performed | NO | NO |

---

## 22. Sheets dependency proof

`sheets_dependency_proof.json`: Google Sheets nodes = 0; authoritative writes = 0.

---

## 23. Workflow registry

Family `admin_runtime`:

- Admin.dev → `active`
- Admin.v3.dev → `candidate`
- Admin.v3.rollback → `rollback`

See `workflow_registry.json`.

---

## 24. Rollback pin

| Field | Value |
|-------|-------|
| Name | `i-SEO Sales Manager - Admin.v3.rollback` |
| ID | `8uStgSN9brsxmz6g` |
| Active | NO |
| Export hash | `1e19672ac9a9ef79783a475e8950d33c007aba1237a58c0fd29434c6eb037f6a` |

After `PG_PRIMARY`: never auto-reactivate Sheets Admin.dev.

---

## 25. Joint cutover contract

Updated:

- `runbooks/ISEO-SALES-PG-CUTOVER-RUNBOOK-v1.md`
- `runbooks/ISEO-SALES-PG-ROLLBACK-RUNBOOK-v1.md`

Sequence covers Operational.v3.dev + Admin.v3.dev fence/activate/verify; **not executed**.

---

## 26. Remaining blockers

1. **DR gate** from cutover prep (`OFF_HOST_BACKUP` / `RESTORE_PROOF`) — required before joint GO.
2. Production Telegram Trigger wiring onto Admin.v3 only at cutover activate step (intentionally absent on inactive candidate).
3. PROFILE_EVENTS path **DEFERRED** (non-blocking for Admin PG SoT).
4. encryptionKey **SECURITY RESIDUAL** (post-cutover remediation allowed).

---

## 27. Git

Worktree: `X:\AI MARS\worktrees\mars-data-layer-iseo-admin-v3-01`  
Branch: `wave/mars-data-layer-iseo-admin-v3-01`  
Dirty main: untouched.

Allowlisted commit content: migration, toolkit, orchestrator/rollback tools, workflow exports, evidence, runbooks, report.

---

## 28. Next gate

1. Close DR backup/restore proof.
2. Human GO for **joint** Operational.v3 + Admin.v3 cutover.
3. Execute cutover runbook §1 only after GO — activate both v3, fence both Sheets workflows, declare `PG_PRIMARY`.
4. Natural production acceptance; no synthetic Telegram.

---

## Evidence root

`projects/mars-data-layer/evidence/candidate-workflow/iseo-admin-v3/`
