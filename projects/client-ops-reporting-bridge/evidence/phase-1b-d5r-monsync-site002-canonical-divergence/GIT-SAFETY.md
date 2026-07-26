# GIT-SAFETY

## Preflight

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Volume | `X:` / `AI WS` |
| Branch (MAIN) | `mars/canonical-post-recovery` |
| LOCAL_HEAD_A | `a6802b1abd78af4128844d868227919a3b17b308` |
| Staged in MAIN before | empty |
| `9a48e93b` ancestor | YES |

## Operations performed

| Op | Where | Allowed |
|----|-------|---------|
| `git worktree add --detach` | STORAGE git-sync | YES |
| `git checkout <commit> -- <one path>` | git-sync worktree | YES |
| exact path staging | git-sync worktree | YES |
| one commit | git-sync worktree | YES |
| update-ref advance of local canonical branch | from MAIN using update-ref only if parent matches | YES (planned) |

## Operations NOT performed

`git pull`, merge origin, rebase MAIN, `read-tree`, reset, stash, restore, clean, push, MAIN index mutation.

## Concurrent HEAD gate

| Marker | Value |
|--------|-------|
| LOCAL_HEAD_A | `a6802b1abd78af4128844d868227919a3b17b308` |
| LOCAL_HEAD_B (pre-commit check) | `a6802b1abd78af4128844d868227919a3b17b308` |
| Movement | NONE |

## MAIN index

`MAIN_INDEX_UNTOUCHED_BY_MONSYNC`
