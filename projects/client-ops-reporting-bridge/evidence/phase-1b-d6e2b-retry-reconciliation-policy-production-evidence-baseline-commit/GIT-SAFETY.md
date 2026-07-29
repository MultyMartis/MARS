# GIT-SAFETY — D6E2B

## Model

- Monorepo: `X:\AI MARS`
- Canonical branch: `mars/canonical-post-recovery`
- Dirty MAIN may contain foreign WIP — **not** used for commit construction
- Commit construction: temporary clean git-sync worktree under `X:\AI MARS STORAGE\git-sync-d6e2b-<unique>\repo`

## Concurrent HEAD

| Label | Role |
|-------|------|
| MAIN_HEAD_A | before clean worktree (`929cda7b8fd41544df5f643896eb124d6074aa83` at phase start) |
| MAIN_HEAD_B | immediately before `git commit --trailer "Co-authored-by: Cursor <cursoragent@cursor.com>"` |
| MAIN_HEAD_C | immediately before canonical `update-ref` |

If tip moves: no force; rebuild on newer tip.

## MAIN protections

- No `git add` / `reset` / `read-tree` / `restore` / `stash` / `clean` / `pull` / `merge` / `rebase` / `switch` on MAIN
- Required: `MAIN_INDEX_UNTOUCHED_BY_D6E2B`
- MAIN read-tree: **NOT USED**
- MAIN reset/stash/restore: **NOT USED**

## Staging

Exact allowlist only. Forbidden: `git add .` / `git add -A`.
SITE-002 / MetaBOT / unrelated: **0**.

## Push

**NO**
