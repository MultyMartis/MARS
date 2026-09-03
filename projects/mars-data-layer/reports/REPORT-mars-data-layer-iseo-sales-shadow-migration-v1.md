# REPORT — mars-data-layer iSEO Sales shadow migration v1

**Wave:** MARS DATA LAYER — ISEO SALES SHEETS → POSTGRES SHADOW MIGRATION 01  
**Date:** 2026-09-03  
**Worktree:** `X:\AI MARS\worktrees\mars-data-layer-iseo-sales-sheets-to-pg-shadow-01`  
**Branch:** `wave/mars-data-layer-iseo-sales-sheets-to-pg-shadow-01`

---

## 1. Verdict

**`ISEO SALES PG SHADOW MIGRATION PASS — READY FOR POSTGRESQL CANDIDATE WORKFLOW BUILD`**

Gate achieved: **`PG_SHADOW VALIDATED`**.  
Sheets remains authoritative. No n8n cutover. No Operational.v3.dev.

Documented residuals exist (see §26) but are **non-blocking for shadow**.

---

## 2. Authority model

| Layer | Role |
|---|---|
| Google Sheets | **AUTHORITATIVE** runtime SoT |
| PostgreSQL `mars.app_iseo_sales` | **`PG_SHADOW`** candidate dataset |
| Migration tool | one-way Sheets → PG |
| n8n Operational.dev / Admin.dev | unchanged; still Sheets-backed |

Forbidden in this wave (honored): PG→Sheets, bidirectional sync, production PG credential bind, Telegram/AI tests.

---

## 3. Source snapshot

| Item | Value |
|---|---|
| Apply snapshot | `20260903T091128Z` |
| Cutoff UTC | ~`2026-09-03T09:11:28Z` |
| RAW spreadsheet | `1Ba1iveHphZqHSTjkHdih0Aqekk5gmonELEX5dKXZ2NU` |
| CLEAN spreadsheet | `1aeIWHeaqHwgJSKLCFZP8M4qG5y9qmOcPt6rvSWsltRU` |
| RAW tab used | `lead_raw_v2` (+ legacy `lead-base` classified obsolete) |
| CLEAN primary | `lead_clean_v2` |

Live Sheets may grow after T0; that is **not** treated as migration failure (§24 / delta design).

---

## 4. Sheets forensic

Inventories (sanitized) under:

`projects/mars-data-layer/evidence/shadow-migration/iseo-sales-v1/run_*`

Observed tabs include: RAW `lead_raw_v2` / `lead-base`; CLEAN `lead_clean_v2`, `CONFIG`, `LEAD_EVENTS`, `ERRORS`, `DEDUP_INDEX`, `ACCESS_CONTROL`, `ACCESS_EVENTS`, `LEAD_DELIVERIES`, `REMINDER_DELIVERIES`, archives, `LEADS`, `LEAD_EVENTS_V2`, `TEST_*`, empty sync tabs, `PROFILE_EVENTS`, etc.

Approximate volumes at apply:

- RAW body ~17.5k rows (heavy append duplicates)
- CLEAN ~7.9k rows
- DEDUP ~7.9k rows (keys mostly empty for business)
- ERRORS ~2.9k (almost all synthetic)
- LEAD_EVENTS ~241 sheet rows → 126 migrated after filters
- ACCESS_CONTROL = 5

---

## 5. Row classification

Classes used: `ACTIVE BUSINESS DATA`, `TERMINAL/HISTORICAL BUSINESS DATA`, `TEST/SYNTHETIC`, `ARCHIVE`, `MALFORMED`, `LEGACY/OBSOLETE`, `UNKNOWN`.

Counters (apply): synth RAW 78 / CLEAN 93; terminal CLEAN 32; unknown 1 (malformed delivery). Uncertain rows not silently dropped — unknown retained in evidence.

---

## 6. RAW → inbound_events

- Identity: `(source_system='gmail', source_id=gmail_message_id)`
- Collapse duplicates → **59** unique inbound
- Re-import does not create second logical event (UPSERT)
- Synthetic message ids excluded

---

## 7. CLEAN → leads

- Identity: `lead_id` (latest `_sheet_row` wins)
- **65** unique leads
- Status mapped into CHECK vocabulary; distribution exact match Sheets collapse
- `source_message_id` linked to inbound where unique; duplicate source_message_id nulled after first lead
- Sheet row numbers never used as business identity

---

## 8. DEDUP reconciliation

No `dedup_index` table (by design).  
Sheet DEDUP largely empty-key → **129** `lead_dedup_keys` synthesized from lead phone/email/site/messenger/gmail.  
UNIQUE/idempotency constraints reproduce protection intent.  
See evidence `RECONCILIATION-MATRIX-v1.md`.

---

## 9. Events

- 126 genuine sheet events migrated
- 65 bootstrap `lead.migrated_from_sheets` (at import time, not backdated)
- Total PG `lead_events` = **191**
- Orphan sheet events excluded (19); test excluded (96)
- Types include `lead.sheet_event`, `telegram_sent`, `manager_*`, etc.

---

## 10. Moderator / audit

Moderator actions preserved primarily via `lead_events` actor fields + ACCESS principals.  
ACCESS_EVENTS not duplicated into multiple audit tables. No test ACCESS mutations.

---

## 11. ACCESS

| Metric | Count |
|---|---:|
| Migrated rules | 5 |
| Active | 1 (admin) |
| Revoked | 3 |
| Pending | 1 |
| Roles | admin×1, moderator×4 |

`principal_key` = `tg:{telegram_user_id}`.  
PG shadow only — Sheets ACCESS not overwritten.

---

## 12. Deliveries

- lead_card 251 + reminder 13 = **264**
- Historical pending/processing forced to `sent` or `cancelled`
- **`pending_deliveries = 0`** (hard invariant: no re-send)
- 67 orphan lead refs stored with `lead_id NULL`
- 1 malformed webhook dump → UNKNOWN, not imported

---

## 13. Reminder / retry state

| Class | Decision |
|---|---|
| REMINDER_DELIVERIES | DURABLE → `deliveries` type `reminder` |
| Sheets quota defer/retry folklore | NOT perpetuated as active jobs |
| Ephemeral selector/cache | DROPPED / regeneratable |

---

## 14. CONFIG

340 keys migrated as strings; secret-pattern keys skipped/excluded; secretish flags set for chat/user-ish keys. Secrets not copied as live credentials.

---

## 15. ERRORS

- 2951 synthetic excluded
- 1 historical → shadow-import with `retryable=false`, `resolved=true`
- Idempotent reload via `DELETE … app_component='shadow-import'`
- 3 schema-seed synthetic fixtures neutralized (`retryable=false`, `resolved=true`)

---

## 16. Import tool

| Path | Role |
|---|---|
| `tools/iseo_sales_sheets_to_pg_shadow.py` | Windows orchestrator (SSH/sudo, evidence download) |
| `tools/iseo_sales_shadow_worker.py` | Host worker: inventory / dry-run / apply / reconcile / prove-live |

Modes: dry-run (no writes), apply (×2 UPSERT + dumps), reconcile, prove-live.  
Credentials: n8n Google OAuth RO decrypt on host; PG via `docker exec` — no secrets in Git.

---

## 17. Dry run

Successful runs include `run_dry-run_20260903T090702Z` (and earlier). Counters aligned with apply.

---

## 18. Initial apply

Canonical apply: `run_apply_20260903T091128Z`  
PRE/POST dumps on host (see §28).

---

## 19. Repeatability / idempotency

Second apply run `rc=0`; stable counts; no duplicate identities.  
Evidence: `IDEMPOTENCY-v1.json` → **IDEMPOTENCY PASS**.

---

## 20. Reconciliation matrix

See `evidence/.../RECONCILIATION-MATRIX-v1.md` — all core domains **PASS**.

---

## 21. Status distribution

Exact match collapsed Sheets ↔ PG (`new/pending/processed/spam`).

---

## 22. Temporal validation

Sheets naive timestamps → Europe/Moscow offset → `TIMESTAMPTZ`.  
Bootstrap events timestamped at import. No unexplained TZ drift in status/event counts.

---

## 23. FK / orphan validation

orphan_events=0, orphan_dedup=0, pending_deliveries=0.  
Nullable delivery.lead_id intentional for orphans.

---

## 24. Delta-import design

Documented in `DELTA-IMPORT-DESIGN-v1.md` (identity keys, NEW/UPDATED classification, cutover freeze step). No cutover executed.

---

## 25. Open questions

Updated in `ISEO-SALES-DATA-OPEN-QUESTIONS-v1.md`:

| ID | Classification after forensic |
|---|---|
| Q1 lead_id mint | NON-BLOCKING for shadow; OPERATOR DECISION before Toolkit mint freeze |
| Q2 append vs upsert Sheets | RESOLVED for import strategy (collapse+PG unique); Sheets hygiene optional |
| Q3 delivery enums | RESOLVED enough for shadow mapping (adapter applied) |
| Q4 dual lifecycle vocab | NON-BLOCKING; soft product decision |
| Q5 local PG | NON-BLOCKING — server PG18 used for this wave |

---

## 26. Cutover blockers

See `CUTOVER-BLOCKERS-v1.md`. Shadow gate does **not** clear SoT switch.

---

## 27. PG does not affect live — proof

`PROVE-LIVE-v1.json`:

- postgres-type credentials = **0**
- workflows with postgres nodes = **0**
- i-SEO Operational.dev + Admin.dev still active
- Shadow writes only via migration docker exec path

---

## 28. PRE/POST backups

Host paths (contents not in Git):

| Kind | Path (example) | Size (bytes) |
|---|---|---:|
| PRE (apply 091128) | `/root/mars-backups/postgres/mars-pre-shadow-20260903T091128Z.sql.gz` | 55410 |
| POST | `/root/mars-backups/postgres/mars-post-shadow-20260903T091128Z.sql.gz` | 55831 |
| Earlier POST-schema baseline | `/root/mars-backups/postgres/mars-post-app-schema-20260903T074124Z.sql.gz` | (prior wave) |

---

## 29. Git

Commit/push from clean worktree only; allowlisted tools/docs/evidence/report. No dumps, no credentials, no raw PII.

---

## 30. Next gate

**Next application wave (not this charter):** build PostgreSQL **candidate** workflow (e.g. Operational.v3.dev) against `PG_SHADOW`, still without SoT switch until cutover blockers clear.

**Stop condition:** satisfied — shadow/reconciliation complete; no workflow build in this wave.
