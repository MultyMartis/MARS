# REPORT — ISEO Sales PostgreSQL Cutover Prep v1

**Project:** `mars-data-layer`  
**Wave:** Controlled Postgres cutover prep 01  
**Date:** 2026-09-03  
**Mode:** PREP ONLY — no production cutover

---

## 1. Verdict

**`PARTIAL — CUTOVER BLOCKERS REMAIN`**

Topology decision (independent): **`JOINT OPERATIONAL + ADMIN PG CUTOVER REQUIRED`** (class B).

Prep achievements (rollback pin, registry, delta dry-run, authority marker, runbooks) are complete, but cutover remains blocked by Admin Sheets write paths, off-host backup/restore FAIL, and v3 Gmail/Telegram wire-before-activate.

---

## 2. Current authority

| Item | Value |
|------|-------|
| Marker store | `mars_core.apps.metadata.data_authority_state` |
| State | **`PG_CANDIDATE_VALIDATED`** |
| `sheets_sot` | **true** |
| Runtime truth | Google Sheets authoritative; PostgreSQL validated shadow/candidate |
| Progression next | `CUTOVER_IN_PROGRESS` → `PG_PRIMARY` (human GO only) |

Proof: `evidence/cutover-prep/iseo-sales-v1/authority_marker_update.txt`

---

## 3. Operational candidate

| Field | Value |
|-------|-------|
| Name | Operational.v3.dev |
| ID | `NH4uV145Amrgnmkm` |
| Active | **NO** |
| Runtime | PostgreSQL `app_iseo_sales` |
| Sheets nodes | 0 |
| Gmail/Telegram in export | **not wired** (deferred until cutover wire) |
| Credential | ISEO Runtime PG (v3) `XCmmOgzZ1RWT4Fg3` |
| Accepted export hash prefix | `dcd9ddd59510` |

---

## 4. PG rollback pin

| Field | Value |
|-------|-------|
| Name | Operational.v3.rollback |
| ID | `favawMOzVwtFMdyH` |
| Active | **NO** |
| Runtime | PostgreSQL (same contract) |
| Export hash | `ac28d8e5268a57390713397e7cc960e5f9742fd75a130b44381bcd632c61607d` |
| Registry status | `rollback` |

Hard stops proven: production still active; v3 + rollback inactive.  
Runbook: `runbooks/ISEO-SALES-PG-ROLLBACK-RUNBOOK-v1.md`

---

## 5. Release registry

`mars_core.workflow_releases` for `operational_intake` / `app_iseo_sales`:

| release_version | status | n8n_workflow_id | hash12 |
|-----------------|--------|-----------------|--------|
| Operational.dev | **active** | `xSnXPy8cEHoZw6xG` | `e299a967dbff` |
| Operational.v3.dev | **candidate** (latest + prior rows) | `NH4uV145Amrgnmkm` | `dcd9ddd59510` (+ older) |
| Operational.v3.rollback | **rollback** | `favawMOzVwtFMdyH` | `ac28d8e5268a` |

v3 was **not** marked active.

---

## 6. Current shadow delta

Class: **`SHADOW REFRESH / DELTA DRY RUN`** — not final cutover delta.  
Snapshot: `20260903T095930Z` vs prior apply `20260903T091128Z`.  
PG **not** updated by dry-run.

Stable business keys unchanged: inbound 59, leads 65, ACCESS 5, deliveries 251+13, events 126, malformed 1.  
Natural Sheets growth: RAW active +41, CLEAN active +50, config +1.

Evidence: `evidence/cutover-prep/iseo-sales-v1/delta_dry_run_summary.json`

---

## 7. Final delta mechanism

Tool: `projects/mars-data-layer/tools/iseo_sales_sheets_to_pg_shadow.py`  
Future fence invocation:

```text
python .../iseo_sales_sheets_to_pg_shadow.py dry-run
python .../iseo_sales_sheets_to_pg_shadow.py apply
python .../iseo_sales_sheets_to_pg_shadow.py reconcile
```

Acceptance properties (proven by shadow contract): repeatable, idempotent, bounded, stable keys (not Sheet row numbers), counter-producing. Operator must not hand-edit SQL.

---

## 8. Cutover fence

Designed in `runbooks/ISEO-SALES-PG-CUTOVER-RUNBOOK-v1.md` (announce → sole intake → in-flight wait → deactivate old → cutoff TS → final delta → reconcile → `PG_PRIMARY` → activate v3 → one poller → natural observe → rollback if hard fail).  
**Not executed.**

---

## 9. In-flight execution policy

Deactivate does **not** kill running executions. Cases covered: pre-deactivate runs; Gmail read incomplete; Sheets write without label; Telegram in progress — with PG stable-key reconcile after authority switch.  
Evidence: `in_flight_execution_policy.json`

---

## 10. Authority switch marker

Canonical: `mars_core.apps.metadata` on `app_iseo_sales` (`data_authority_state`, `sheets_sot`, notes/timestamp).  
No second competing state system.  
Progression: `SHEETS_PRIMARY` → `PG_SHADOW` → `PG_CANDIDATE_VALIDATED` → `CUTOVER_IN_PROGRESS` → `PG_PRIMARY`.

---

## 11. Backup state

Local ad-hoc logical dumps: **YES** (`/root/mars-backups/postgres/`).  
Script: `/opt/mars-postgres/backup-logical.sh` exists.  
Nightly cron: **NO**.

---

## 12. Off-host backup

**NO** — gate **`POSTGRESQL LOGICAL BACKUP OFF VPS = FAIL`**. Preferred future target: Beget (logical copy, not hot replication).

---

## 13. Restore proof

**NO** — **`RESTORE PROOF = FAIL`**. Class: **`BLOCKING UNTIL PASS`**.  
Handoff: `runbooks/SERVER-OPS-PG-DR-CUTOVER-GATE-HANDOFF-v1.md` → Pro: MARS Server Ops pt.2.

---

## 14. EncryptionKey residual

**Classification:** `SECURITY RESIDUAL — MAY BE REMEDIATED AFTER CUTOVER`  
**Not:** `BLOCKING BEFORE CUTOVER`

Audit: no key value in Git/evidence assignments; server file `/opt/n8n/n8n_data/config` mode `0600` (content not read). Unauthorized decryption via repo evidence **not proven**. Do not rotate in cutover wave.

---

## 15. Credential dependency

v3/rollback critical path: PostgreSQL credential only in current export; **0 Sheets nodes**.  
Gmail/Telegram: required for production activate but **deferred wire**.  
Operational.dev still uses Gmail + Sheets + Telegram.

---

## 16. Pre-cutover checklist

See `preflight_checklist.json`. Blocking fails today: off-host backup, restore proof, Admin.v3 (or Admin write fence), Gmail/Telegram wire on v3.

---

## 17. Post-cutover natural acceptance

Natural-traffic-only first window (no synthetic Telegram): Gmail → PG persist; no duplicates; outbox correct; label after commit; no Sheets critical path; one intake; Admin also on PG under joint cutover.

---

## 18. Rollback triggers

Hard: intake stop, duplicate leads, commit/source loss, Telegram corruption, ACCESS mismatch, PG down unsafe, dual intake, Sheets dependency on v3, Admin Sheets mutation after `PG_PRIMARY`.  
Non-rollback: Telegram retry, projection delay, Sheets idle after deactivate, known malformed exclusion.

---

## 19. Sheets post-cutover role

Non-authoritative; old workflow inactive; no automatic writeback into PG; projection may be NOT IMPLEMENTED (communicate).

---

## 20. Admin.dev dependency forensic

Admin.dev `wLrLp4WQHm1VJmxz` **ACTIVE**: 11 Sheets WRITE, 16 READ, 0 Postgres.  
Writes include CLEAN lifecycle, ACCESS, reminders, CONFIG, LEAD_EVENTS, PROFILE_EVENTS, ERRORS.  
Class for authoritative sheets: **`MUST MIGRATE BEFORE OPERATIONAL CUTOVER`**.

---

## 21. Split-authority analysis

If Operational.v3 writes PG while Admin.dev continues mutating lead/ACCESS/reminder state in Sheets → **split-brain**. Operational-only cutover is **unsafe**.

---

## 22. Cutover topology decision

**B — `JOINT OPERATIONAL + ADMIN PG CUTOVER REQUIRED`**

Preferred future candidate: `Admin.v3.dev` (inactive, PG-backed) — **not built in this wave**.

---

## 23. Remaining blockers

1. Admin.v3.dev (or equivalent joint PG Admin path) before SoT switch  
2. Off-host PG backup PASS  
3. Restore drill PASS  
4. Wire Gmail+Telegram on v3/rollback before activate  
5. Human-approved fence + final cutover delta (not done)  
6. Optional residuals: delivery orphans hygiene, lifecycle vocabulary — product/ops follow-ups

Non-blockers for SoT timing: encryptionKey residual (separate remediation).

---

## 24. Git

Worktree: `X:\AI MARS\worktrees\mars-data-layer-iseo-sales-cutover-prep-01`  
Branch: `wave/mars-data-layer-iseo-sales-cutover-prep-01`  
Commit: `5816b1e451410baddeb9ad53d78ff22442bf6a45`  
Remote: `origin/wave/mars-data-layer-iseo-sales-cutover-prep-01` (non-force push)  
Dirty main at `X:\AI MARS` **not** touched.

---

## 25. Exact next gate

1. Charter **Admin.v3.dev** inactive PG candidate (no in-place Admin.dev rewrite).  
2. Server Ops pt.2: nightly + **off-host** backup + **restore proof PASS**.  
3. Cutover wire plan for Gmail/Telegram on v3 + rollback pin.  
4. Human GO for joint fence — still **no activate** until gates green.

---

## Hard stops observed (prep end)

- Operational.dev **ACTIVE**
- Operational.v3.dev **INACTIVE**
- Operational.v3.rollback **INACTIVE**
- Sheets **authoritative**
- PostgreSQL **candidate / shadow**
- No final cutover delta, no SoT switch, no Admin.dev mutation, no encryptionKey rotation, no Telegram tests
