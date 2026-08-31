# CLEANUP DECISION MATRIX v1

| Exact path | Classification | Remove this wave? | Reason |
|---|---|---|---|
| `...\worktrees\iseo-smb-card-status-sync` | `SAFE_CLOSED_REGENERABLE` | **YES** | Clean; no sidecars; functionally promoted (`5d08ed07`); no active natural-reminder dependency; regenerable via `git worktree add` |
| `...\worktrees\iseo-smb-reminder-final-natural-01` | `DIRTY_WIP_DO_NOT_TOUCH` | NO | 2 untracked acceptance artifacts |
| `...\git-sync-iseo-sm-natural-reminder-action-card-20260831-141343` | `ACTIVE_KEEP` | NO | Supports current live natural-reminder confirmation; HEAD already origin tip |
| `...\git-sync-iseo-sm-final-hygiene-closeout-20260831-170501` | `ACTIVE_KEEP` → post-push regenerable | Post-push optional | This wave vehicle |
| `...\git-sync-iseo-sm-final-hygiene-closeout-20260831-170336` | `SAFE_CLOSED_REGENERABLE` / empty duplicate | **YES** | Duplicate clean closeout skeleton |
| All `incoming\iseo-sales-manager-bot\**` | `SECRET_OR_BACKUP_KEEP` / `PRODUCTION_EVIDENCE_KEEP` / `ARCHIVE_REVIEW_KEEP` | NO | Backups, private, forensic |
| Stale prunable registrations (disk absent) | n/a (registry debt) | NO global prune | Charter forbids global prune |

## Approved exact removal list

1. `X:\AI MARS\worktrees\iseo-smb-card-status-sync` — **REMOVED**
2. `X:\AI MARS STORAGE\git-sync-iseo-sm-final-hygiene-closeout-20260831-170336` — **REMOVED**
