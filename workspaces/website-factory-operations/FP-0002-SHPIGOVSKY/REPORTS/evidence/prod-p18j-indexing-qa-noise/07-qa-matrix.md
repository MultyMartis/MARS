# QA matrix — PROD-P18J post-deploy

Evidence source: `03-post-deploy-qa.json`

## CASE A — Synthetic unauthorized close (authorized QA)

| Check | Result |
|-------|--------|
| Guard rejects close | **PASS** (`blocked: true`, `error: close_requires_human_authorization`) |
| Indexing stays OPEN | **PASS** (`blog_public` 1→1, `effective: OPEN`) |
| No critical production Activity Log row | **PASS** (`activity_blocked_rows_delta: 0`) |
| QA evidence recorded | **PASS** (`fp02_indexing_qa_evidence` tail, `test_id: p18j_qa_guard_test`, `result: PASS`) |

## CASE B — Real classification path (integration layer)

Blocked-close path without QA authorization still logs incident row (see CASE E). Real alert builder tested via `send_test_alert()` — **TEST — INDEXING SAFETY ALERT** channel, not conflated with blocked-close critical path.

## CASE C — Watchdog normal OPEN

| Check | Result |
|-------|--------|
| Dashboard | `ACTIVE · … · OPEN` |
| Snapshot | `effective: OPEN`, `signals_closed: false` |
| Synthetic close attempt | **None** |

## CASE D — Synthetic inconsistent-state test

Not executed as mutating production test in this wave (charter: no real inconsistency injection). Alert suppression code requires effective OPEN for QA suppression — **SAFE UNKNOWN** for live inconsistent-state QA until a bounded dry-run harness exists.

## CASE E — Public/admin cannot spoof QA suppression

| Check | Result |
|-------|--------|
| `request_state(false, ['source'=>'p18g_qa_guard_test'])` **without** `FP02_INDEXING_QA_MODE_AUTHORIZED` | Logs **1** new `indexing_close_blocked` row (`activity_blocked_rows_delta_without_const: 1`) |
| Guard still holds OPEN | **PASS** |
| Interpretation | Spoof marker alone does **not** enable QA suppression |
