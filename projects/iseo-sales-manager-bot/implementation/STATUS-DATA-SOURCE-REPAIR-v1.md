# STATUS DATA SOURCE REPAIR v1

**Phase:** 3H.4  
**Workflow:** Admin.dev (`wLrLp4WQHm1VJmxz`)  
**Nodes:** Status · Health (Code)

---

## 1. Defects

### 1.1 Stale poll display

`/status` read frozen `last_poll_success_at` because scheduled empty polls did not write heartbeat (Operational fix — see `SCHEDULED-POLL-OBSERVABILITY-v1.md`).

### 1.2 Wrong last processed lead

`/status` showed **22:23 МСК** from synthetic test `msg_synth_3g11d_t1_*` via `last_lead_success_at`, not production lead `lead_19fd2052066e18b7` (**17:22 МСК**).

### 1.3 Health conflation risk

Operators could misread `/health` Gmail probe as scheduled poll truth.

---

## 2. Repair

**Status Code node:**

- Poll line → `last_poll_success_at` + `gmail_poll_heartbeat`
- Production lead line → `last_production_processed_at` + `last_production_processed_lead_id`
- Decouple synthetic technical stamps from production display

**Health Code node:**

- Clarify probe semantics; no substitution for poll heartbeat

**CONFIG backfill:**

- `last_production_processed_at=2026-08-05T14:22:55.186Z`
- `last_production_processed_lead_id=lead_19fd2052066e18b7`
- `pending_reminder_active_recipients_count=3`

---

## 3. Validation

| Check | Result |
|---|---|
| `/status` production lead time | 05.08.2026 17:22 МСК PASS |
| Poll line advances on empty runs | PASS |
| `node --check` Status/Health | PASS |
| HEALTH vs STATUS separation | documented PASS |

---

## 4. Architecture

`architecture/OPERATIONAL-STATUS-TRUTH-CONTRACT-v1.md`

## 5. Evidence

`evidence/phase3h4/STATUS-DATA-SOURCE-MATRIX-v1.md` · `LAST-PROCESSED-LEAD-FORENSIC-v1.md` · `STATUS-LIVE-ACCEPTANCE-v1.md`

## Phase 3H.4.1

Confirmed empty `last_production_processed_at` after 3H.4 backfill. 3H.4.1 rewrote cache from LEADS (`2026-08-05T14:22:55.186Z`) and hardened Status resolver. See `implementation/LAST-PROCESSED-STATUS-READBACK-REPAIR-v1.md`.

