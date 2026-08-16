# E64 Git Worktree Cleanup

## Preflight note

Main worktree `X:\AI MARS` remains dirty with foreign WIP. Local HEAD `7443c4e9` is ahead of `origin/mars/canonical-post-recovery` (`9d5dcc28`) with unrelated unpushed commits. **No pull/reset/clean/stash/commit/push** in this wave.

## Worktrees found (`git-sync-fp0002-*`)

| Path | Ownership | HEAD | Clean? | vs remote | Size before | Action |
|------|-----------|------|--------|-----------|-------------|--------|
| `…\git-sync-fp0002-e63-stable-v1-20260718-004331\repo` | FP-0002 | `9d5dcc28` | Yes | Equals remote tip | ~2.99 GB | **REMOVED** via `git worktree remove` |
| `…\git-sync-fp0002-push-divergence-20260716-040930\repo` | FP-0002 | `03ff6777` | Yes | Ancestor of remote | ~2.68 GB | **REMOVED** |
| `…\git-sync-fp0002-e29b-fix2c-20260710-180821` | FP-0002 | `996489e3` | Yes | Ancestor of remote | ~2.61 GB | **REMOVED** |
| `…\git-sync-fp0002-e29c-e35-20260713-032549\repo` | FP-0002 | `e93a4ca3` | Yes (working tree) | **6 commits NOT ancestor of remote** | ~452 MB | **SKIPPED — MANUAL_REVIEW** |
| `…\git-sync-fp0002-e38-e51-20260716-031000` | FP-0002 | n/a | Empty, unregistered | n/a | 0 | **REMOVED** (empty dir) |
| `…\git-sync-fp0002-e58-20260716-225851` | FP-0002 | n/a | Empty, unregistered | n/a | 0 | **REMOVED** (empty dir) |
| `…\git-sync-e01\repo` | SITE-002 | `85bf2902` | n/a | n/a | n/a | **SKIP_FOREIGN** |

## e29c stop reason

`git log origin/mars/canonical-post-recovery..e93a4ca3` lists six FP-0002 persistence commits not reachable from the remote tip. Per charter stop conditions, the worktree was **not** deleted.

## Git metadata after

```
X:/AI MARS                                                       7443c4e9 [mars/canonical-post-recovery]
X:/AI MARS STORAGE/git-sync-e01/repo                             85bf2902 [site-002-…]
X:/AI MARS STORAGE/git-sync-fp0002-e29c-e35-20260713-032549/repo e93a4ca3 [fp0002/v9-06e36-e37-…]
```

- `git worktree prune -v` run (no harmful file changes)
- Main dirty worktree unchanged by worktree removals
- Remote tip unchanged: `9d5dcc285eb45c827231bfe89c7611fb84e850d2`
- Release content commit still on remote: `d1befe9b…`

## Reclaimed

Approximately **8.29 GB** from removed FP-0002 sync trees (exact sizes in `E64-DELETION-LOG.csv`).
