# GIT-SAFETY — D6DB

- Monorepo `X:\AI MARS`; branch `mars/canonical-post-recovery`
- Commit via temporary clean worktree under `X:\AI MARS STORAGE\git-sync-d6db-<unique>\repo`
- Forbidden on MAIN: add/reset/read-tree/restore/stash/clean/pull/merge/rebase/switch
- Required: `MAIN_INDEX_UNTOUCHED_BY_D6DB`
- Exact allowlist staging only; no `git add .` / `-A`
- Push: NO
