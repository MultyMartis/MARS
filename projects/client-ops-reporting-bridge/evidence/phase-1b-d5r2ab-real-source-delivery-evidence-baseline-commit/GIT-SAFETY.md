# GIT-SAFETY — D5R2AB

## Model

- Monorepo: `X:\AI MARS`
- Canonical branch: `mars/canonical-post-recovery`
- Dirty MAIN may contain foreign WIP — **not** used for commit construction
- Commit construction: temporary clean git-sync worktree under `X:\AI MARS STORAGE\git-sync-d5r2ab-<unique>\repo`

## Concurrent HEAD notes

| Label | Value |
|-------|-------|
| Session-start observed tip | `86338d666f08146b6feff06536ae6d7b50eb332c` |
| MAIN_HEAD_A (before clean worktree) | recorded at worktree creation time |
| MAIN_HEAD_B | immediately before `git commit` |
| MAIN_HEAD_C | immediately before canonical ref advance |

If tip moves between A and commit parent inequality vs tip: rebuild on newer tip (no force).

## MAIN protections

- No `git add` / `reset` / `read-tree` / `restore` / `stash` / `clean` / `pull` / `merge` / `rebase` / `switch` on MAIN
- Required: `MAIN_INDEX_UNTOUCHED_BY_D5R2AB`
- MAIN read-tree: **NOT USED**
- MAIN reset/stash/restore: **NOT USED**

## Staging

- Exact allowlist only
- Forbidden: `git add .` / `git add -A`
- Expected SITE-002 source files: **0**
- Expected MetaBOT files: **0**
- Expected unrelated files: **0**

## Push

**NO**

## Worktree lifecycle

Created 1 / removed 1 (expected on success).

Exact commit hash, parent, and ref-advance method are recorded in the operator REPORT (sections 18–20). This pack remains free of secrets and of MAIN index mutation claims requiring post-hoc edits.
