# GIT-SAFETY — D6D2B

## Model

- Monorepo: `X:\AI MARS`
- Canonical branch: `mars/canonical-post-recovery`
- Dirty MAIN may contain foreign WIP — **not** used for commit construction
- Commit construction: temporary clean git-sync worktree under `X:\AI MARS STORAGE\git-sync-d6d2b-<unique>\repo`

## Concurrent HEAD

| Label | Role |
|-------|------|
| MAIN_HEAD_A | before clean worktree |
| MAIN_HEAD_B | immediately before commit |
| MAIN_HEAD_C | immediately before canonical `update-ref` |

If tip moves: no force; rebuild on newer tip.

## MAIN protections

- No `git add` / `reset` / `read-tree` / `restore` / `stash` / `clean` / `pull` / `merge` / `rebase` / `switch` on MAIN
- Required: `MAIN_INDEX_UNTOUCHED_BY_D6D2B`
- MAIN read-tree: **NOT USED**
- MAIN reset/stash/restore: **NOT USED**

## Staging

Exact allowlist only. Forbidden: `git add .` / `git add -A`.
SITE-002 / MetaBOT / unrelated / runtime-state: **0**.

## Push

**NO**
