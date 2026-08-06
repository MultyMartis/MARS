# SCHEDULED POLL OBSERVABILITY v1

**Phase:** 3H.4  
**Workflow:** Operational.dev (`xSnXPy8cEHoZw6xG`)  
**Nodes:** Update Last Success · Apply Runtime State / CONFIG writers

---

## 1. Problem

Classification: `POLLING_ACTIVE_BUT_HEARTBEAT_NOT_WRITTEN_ON_EMPTY_RUNS`.

Schedule Trigger (`minutesInterval=2`) fired ~every 2 minutes. Empty inbox path completed Gmail Fetch + Intake Gate but Update Last Success returned `[]` — CONFIG `last_poll_success_at` frozen at **2026-08-05T10:34:00.459Z**.

---

## 2. Repair

Implement `iseo-gmail-poll-heartbeat-v1.0`:

- Always write `gmail_poll_heartbeat` JSON on successful poll completion
- Mirror `last_poll_success_at` on empty and non-empty runs
- Stamp `last_production_processed_*` only on non-test processing success

---

## 3. Proof

Three post-repair empty polls with CONFIG heartbeat write: executions **24222**, **24223**, **24228**.

---

## 4. Operator impact

`/status` Gmail poll line now advances during quiet inbox periods. `/health` remains independent on-demand probe.

---

## 5. Architecture

`architecture/GMAIL-POLL-HEARTBEAT-CONTRACT-v1.md`

## 6. Evidence

`evidence/phase3h4/SCHEDULED-GMAIL-POLL-FORENSIC-v1.md` · `THREE-CONSECUTIVE-POLLS-v1.md`
