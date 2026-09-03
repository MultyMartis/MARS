# Server Ops — PostgreSQL DR Cutover Gate Handoff v1

**Document:** `SERVER-OPS-PG-DR-CUTOVER-GATE-HANDOFF-v1`  
**Audience:** `Pro: MARS Server Ops pt.2`  
**From:** `mars-data-layer` / ISEO Sales cutover prep 01  
**Date:** 2026-09-03  
**Execution status:** **NOT EXECUTED HERE** — gate requirements only

---

## 1. Why this blocks cutover

Before `app_iseo_sales` can become sole SoT on PostgreSQL, MARS requires:

| Gate | Current (2026-09-03 probe) | Required |
|------|----------------------------|----------|
| On-VPS logical dumps | **PASS_PARTIAL** — ad-hoc dumps under `/root/mars-backups/postgres/` | Keep |
| Nightly logical backup | **NO** — script exists, cron not configured | YES |
| Off-host copy | **NO** | YES — preferred target Beget |
| Restore proof | **NO** | YES — restore to isolated scratch DB + sanity checks |

Classification: **`BLOCKING UNTIL PASS`**.

---

## 2. Observed assets (do not treat as DR complete)

- Script: `/opt/mars-postgres/backup-logical.sh` (mode 0700/root)
- Dump dir: `/root/mars-backups/postgres/` (wave dumps present)
- No `/root/mars-backups/offhost`, no `/mnt/beget`
- No restore-drill artifacts

Evidence: `projects/mars-data-layer/evidence/cutover-prep/iseo-sales-v1/backup_restore_gate_status.json`

---

## 3. Acceptance for cutover gate

1. Nightly logical dump of database `mars` scheduled and monitored.
2. Encrypted off-host copy of recent dump(s) on approved target (Beget preferred; not hot standby unless separately chartered).
3. Restore drill:
   - restore archive into **isolated scratch** database/runtime
   - schema/data sanity checks for `app_iseo_sales` (+ `mars_core` metadata)
   - document PASS with timestamps/hashes (no PII)
4. Evidence filed under Server Ops reports; notify data-layer.

**Not acceptable:** “`pg_dump` file exists on the same VPS.”

---

## 4. Non-goals for this handoff

- Do not activate Operational.v3 / switch SoT
- Do not rotate n8n encryptionKey in the same wave as cutover (separate security wave if needed)
- Do not invent hot replication
- Do not open public `5432`

---

## 5. Optional companion security residual

encryptionKey residual classified **non-blocking for SoT** in cutover-prep audit (no key value in Git). If historical exposure is later proven, schedule a **separate** Server Ops credential-rotation wave.
