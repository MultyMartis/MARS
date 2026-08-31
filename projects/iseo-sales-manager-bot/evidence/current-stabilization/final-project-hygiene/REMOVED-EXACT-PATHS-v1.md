# REMOVED EXACT PATHS v1

## Pre-approved list

| # | Exact path | Method |
|---|---|---|
| 1 | `X:\AI MARS\worktrees\iseo-smb-card-status-sync` | `git worktree remove --force` after recheck |
| 2 | `X:\AI MARS STORAGE\git-sync-iseo-sm-final-hygiene-closeout-20260831-170336` (+ `\repo`) | Duplicate empty closeout skeleton; `git worktree remove` then wrapper delete |

## Execution log

| Exact path | Recheck | Result | Notes |
|---|---|---|---|
| `X:\AI MARS\worktrees\iseo-smb-card-status-sync` | PASS (clean 0/0; no sidecars; `5d08ed07` ancestor of origin) | **REMOVED** | HEAD was `9a69ef08` (functionally promoted). Disk gone; worktree registration cleared. Branch ref may remain locally — objects not deleted. |
| `...\git-sync-iseo-sm-final-hygiene-closeout-20260831-170336` | PASS (clean; no private/runtime/backups; only `repo` + `CLOSEOUT-PATH.txt`) | **REMOVED** | Accidental duplicate closeout WT at tip; no unique content |

## Disk

| When | X: free GB |
|---|---:|
| Immediately before card-status remove | 335.35 |
| Immediately after card-status remove | 337.87 |
| Approximate gain (card-status) | **~2.52 GB** |
| Duplicate 170336 | additional small reclaim (checkout + wrapper) |

## Not removed

Wildcard / sibling / parent cleanup: none. Incoming STORAGE: none. Dirty WIP worktree: none. Natural-reminder STORAGE contour: none. Active closeout `...-170501`: retained until push complete.
