# Git Diff Summary — FP-0002 V9 Stable v1

## Method

Exact-file application of allowlisted paths from dirty main `X:\AI MARS` onto a clean worktree based on `origin/mars/canonical-post-recovery`.

## Counts

| Area | Paths |
|------|------:|
| Theme | 63 |
| Plugin | 3 |
| ACF JSON | 12 |
| Reports/evidence | 87 |
| Docs | 4 |
| Other FP-0002 | 36 |
| **Allowlist total** | **207** |
| Excluded within FP-0002 (caches/temps) | 55 |
| Foreign WIP excluded | 336 |

## Secrets check

Allowlist scanned for `.env`, credentials, `wp-config`, SQL dumps, backup archives: **none included**.

## Rejected classes

generated cache, logs, temp files, DB dumps, backups, node_modules, secrets, editor state, unrelated MARS systems.
