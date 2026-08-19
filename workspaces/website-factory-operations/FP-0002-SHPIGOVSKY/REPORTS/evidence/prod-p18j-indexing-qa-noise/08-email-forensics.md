# Email alert forensics — PROD-P18J

## Historical four events (2026-08-19 20:23–21:09)

| Event | Critical admin alert |
|-------|---------------------|
| IDs 155–158 `indexing_close_blocked` / `p18g_qa_guard_test` | **A — no alert attempted** |

Rationale: P18G/P18I blocked-close path logs Activity Log only; `IndexingAlerts::send_critical_blocked_alert` is not invoked on guard rejection.

## P18G separate channel

P18G deploy also invoked `IndexingAlerts::send_test_alert()` → subject **TEST — INDEXING SAFETY ALERT** (intentional proof of mail path). This is **not** the same as a critical unauthorized-close alert.

## P18J post-deploy

| Test | Result |
|------|--------|
| Authorized QA blocked close | No critical email (expected) |
| `send_test_alert()` | **sent: true**, recipients count recorded in evidence (addresses redacted) |

## Classification

**SYNTHETIC QA EMAIL BEHAVIOR VERIFIED** — synthetic blocked-close does not trigger real critical admin alerts; test alert uses explicit TEST subject.
