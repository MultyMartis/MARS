# Four-event forensic timeline — PROD-P18J

**Site:** https://shpigovsky.ru/  
**Marker:** `p18g_qa_guard_test`  
**Classification:** synthetic P18G guard QA (not real production incidents)

## Summary

All four Activity Log rows are **synthetic guard validation** from the P18G deploy harness (`_p18g_runtime.py` → `wp_eval` → `IndexingControl::request_state(false, ['source'=>'p18g_qa_guard_test'])`). They are **not** cron, watchdog, Admin UI, or WPilot. **blog_public remained 1** throughout.

## Per-event table

| Timestamp (site) | ID | Caller | Path | State change | Critical email |
|------------------|-----|--------|------|--------------|----------------|
| 2026-08-19 20:23:07 | 155 | P18G QA harness | SSH `wp_eval` / PHP CLI | **None** — OPEN held | **No** — blocked-close path does not alert |
| 2026-08-19 20:23:54 | 156 | P18G QA harness (re-run) | SSH `wp_eval` | **None** | **No** |
| 2026-08-19 20:29:33 | 157 | P18G git-push QA re-run | SSH `wp_eval` | **None** | **No** |
| 2026-08-19 21:09:12 | 158 | P18G git-push QA re-run | SSH `wp_eval` | **None** | **No** |

## Code entry point

```php
IndexingControl::request_state( false, array( 'source' => 'p18g_qa_guard_test' ) );
```

Invoked from `REPORTS/evidence/prod-p18g-indexing-safety/_p18g_runtime.py` function `post_deploy_qa()` → `blocked_close`.

## Email forensics (historical four)

- **Classification:** **A — no critical alert attempted** for blocked-close synthetic tests.
- P18G did send **`TEST — INDEXING SAFETY ALERT`** via `IndexingAlerts::send_test_alert()` (intentional channel proof) — separate from the four Activity Log rows.

## P18J fix

- Authorized QA uses `FP02_INDEXING_QA_MODE_AUTHORIZED` + `qa_test` / `test_id` → bounded option `fp02_indexing_qa_evidence` only.
- Historical rows **preserved**; Admin UI renders them as **QA: защита индексации проверена — PASS**.
