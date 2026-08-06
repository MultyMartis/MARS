# GIT-SAFETY — D6B2B

## Model

- Monorepo: `X:\AI MARS`
- Canonical branch: `mars/canonical-post-recovery`
- Dirty MAIN may contain foreign WIP — **not** used for commit construction
- Commit construction: temporary clean git-sync worktree under `X:\AI MARS STORAGE\git-sync-d6b2b-<unique>\repo`

## Concurrent HEAD notes

| Label | Value |
|-------|-------|
| MAIN_HEAD_A | `6cb66b545004993a22a92a2072fde78528e3ca7e` |
| origin tip (observed) | `bd46565f98c84e8546125a23cb0c0f2e06b3742c` |
| ahead/behind | 142 ahead / 64 behind |
| MAIN_HEAD_B | immediately before commit creation |
| MAIN_HEAD_C | immediately before canonical ref advance |

## MAIN protections

- No `git add` / `reset` / `read-tree` / `restore` / `stash` / `clean` / `pull` / `merge` / `rebase` / `switch` on MAIN
- Required: `MAIN_INDEX_UNTOUCHED_BY_D6B2B`
- MAIN read-tree: **NOT USED**
- Push: **NO**
