# GIT-SAFETY — D6A2B

## Model

- Monorepo: `X:\AI MARS`
- Canonical branch: `mars/canonical-post-recovery`
- Dirty MAIN may contain foreign WIP — **not** used for commit construction
- Commit construction: temporary clean git-sync worktree under `X:\AI MARS STORAGE\git-sync-d6a2b-<unique>\repo`

## Concurrent HEAD notes

| Label | Value |
|-------|-------|
| MAIN_HEAD_A (before clean worktree) | `65ab3a973f94c51fccae03c9e48868b75293316b` |
| origin tip (observed) | `dc1fa5c48255efd8819b1947408d82f67bf020ca` |
| ahead/behind (origin...HEAD) | 128 ahead / 62 behind (foreign divergence not reconciled) |
| MAIN_HEAD_B | immediately before `git commit` |
| MAIN_HEAD_C | immediately before canonical ref advance |

If tip moves between A and commit parent inequality vs tip: rebuild on newer tip (no force).

## MAIN protections

- No `git add` / `reset` / `read-tree` / `restore` / `stash` / `clean` / `pull` / `merge` / `rebase` / `switch` on MAIN
- Required: `MAIN_INDEX_UNTOUCHED_BY_D6A2B`
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

Exact commit hash, parent, and ref-advance method are recorded in the operator REPORT (sections 22–25). This pack remains free of secrets and of MAIN index mutation claims requiring post-hoc edits.
