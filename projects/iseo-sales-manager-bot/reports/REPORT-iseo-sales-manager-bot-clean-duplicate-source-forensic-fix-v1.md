# REPORT — ISEO-SALES-MANAGER-BOT CLEAN DUPLICATE SOURCE FORENSIC / FIX

**Process-line:** CLEAN DUPLICATE SOURCE FORENSIC, SOURCE FIX, AND INGEST IDEMPOTENCY PROOF  
**Date:** 2026-08-26  
**Base tip:** `12327f1d` (`origin/mars/canonical-post-recovery` verified)  
**Worktree:** `X:\\AI MARS STORAGE\\git-sync-iseo-sm-clean-duplicate-forensic-20260826-175345\\repo`

## 1. Verdict

`CLEAN DUPLICATE SOURCE FIXED — INGEST IDEMPOTENCY LIVE PASS`

Historical production-real / test residual clusters **retained** (no destructive cleanup). Soak: `READY FOR NEW 48H SOAK` — awaiting operator approval.

## 2. Current CLEAN duplicate inventory

3 `lead_id` clusters (155 rows / 112 unique): 2 PRODUCTION_REAL_DUPLICATE, 1 PROVEN_TEST_RESIDUAL, 0 SAFE_UNKNOWN_DUPLICATE. Strongest: `lead_19fcce0e42028e45` ×16 / 1 Gmail id. See CLEAN-DUPLICATE-INVENTORY-v1.md.

## 3. Logical identity contract

SOURCE_EVENT_ID = Gmail message id; LOGICAL_LEAD_ID = `lead_id` (≈ `lead_` + message id). Spec: same message → update CLEAN, do not append. Contact repeats may create new CLEAN intentionally.

## 4. Current CLEAN writers

Ops: Append or Update CLEAN v2 (+ DEDUP_INDEX). Admin: update/read only for lifecycle — not ingest append. All writers accounted for.

## 5. Proven duplicate incident

Same SOURCE_EVENT_ID reprocessed ~30s → repeated CLEAN **append** via Ops node that was append-only despite name.

## 6. Temporal sequence

T0 event → RAW → classify → CLEAN append → DEDUP append → retry → CLEAN append again → … (16 rows). Earliest missing barrier: CLEAN upsert by `lead_id`.

## 7. Exact root cause

`DEDUP_GUARD_BYPASSED` + always-`append` CLEAN/DEDUP; Classify reprocess did not divert write. Live PRE backup proved defect still current on 2026-08-26.

## 8. Whether current or historical-only

**CURRENT** (patched). Historical clusters are residual symptoms.

## 9. Repair

Ops: CLEAN `appendOrUpdate`/`lead_id`; DEDUP `appendOrUpdate`/`dedup_key`; Classify preserves lifecycle on gmailMatch. Live updatedAt 2026-08-26T11:08:16.779Z.

## 10. Retry/race safety

Same-event upsert ×3 → 1 row. Distinct event B → second row, A preserved. Overlapping poll still upsert-safe on `lead_id` (Sheets match).

## 11. Same-event replay proof

PASS — additional CLEAN leads = 0 (IDEMPOTENCY-REPLAY-A-v1.md).

## 12. Distinct-event non-false-dedupe proof

PASS — false_dedupe_events = 0 (DISTINCT-EVENT-B-v1.md).

## 13. Event/ledger proof

One logical creation per SOURCE_EVENT_ID on CLEAN; DEDUP upsert; fixtures archived from pending; 0 Telegram customer/moderator side effects in harness.

## 14. Historical real/unknown duplicates

KEEP — residual matrix in HISTORICAL-DUPLICATE-RESIDUALS-v1.md. real historical rows mutated = 0; SAFE_UNKNOWN mutated = 0.

## 15. Reminder/group regression

Admin untouched; prior set equality / proven artificial pending = 0 baseline stands; this wave fixtures pending = 0 after archive.

## 16. Production invariants

ACCESS, recipients, reminder schedule/dedupe, AI OFF, Gmail poll cadence, customer auto-messages OFF, reporting MANUAL — unchanged. No moderator restoration.

## 17. Backup

PRE SHA256 `7CF95282...`; POST SHA256 `DCA6B25C...` — private only; sanitized manifests in evidence.

## 18. Git

Selective commits under `projects/iseo-sales-manager-bot/**` from clean worktree; push to `origin/mars/canonical-post-recovery` (no force). Private backups/scripts not committed.

## 19. Remaining stabilization work

- Separate reconciliation for historical PRODUCTION_REAL_DUPLICATE / PROVEN_TEST_RESIDUAL CLEAN rows.
- Optional: full Ops path creation-event telemetry soak under operator charter.
- Operator-approved 48h soak start.

## 20. Soak readiness

`READY FOR NEW 48H SOAK` — **stop; wait for operator approval**.

## Required counters

| Counter | Value |
|---------|------:|
| duplicate CLEAN clusters found | 3 |
| production-real duplicate clusters | 2 |
| SAFE_UNKNOWN duplicate clusters | 0 |
| proven-test residual clusters | 1 |
| current duplicate-producing paths | 0 |
| CLEAN writer nodes | 1 (Ops ingest upsert) |
| same-event executions tested | 3 |
| additional CLEAN leads from same-event replay | 0 |
| distinct events tested | 2 |
| false dedupe events | 0 |
| duplicate creation events after fix | 0 |
| real historical rows mutated | 0 |
| SAFE_UNKNOWN rows mutated | 0 |
| moderator messages | 0 |
| customer messages | 0 |
| AI calls | 0 |
