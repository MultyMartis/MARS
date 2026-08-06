# CLEAN-WORKTREE-MATERIALIZATION

## Worktree

| Field | Value |
|-------|-------|
| Class | temporary git-sync (NOT runtime checkout) |
| Path | `X:\AI MARS STORAGE\git-sync-monsync-20260726-182443\repo` |
| Mode | detached HEAD |
| Base | `a6802b1abd78af4128844d868227919a3b17b308` (= LOCAL_HEAD_A) |
| Clean before materialization | YES (empty porcelain) |
| Foreign WIP | NONE |
| Runtime relation | NONE |

## Gate

`CLEAN_GIT_SYNC_WORKTREE_READY`

## Materialization

| Item | Value |
|------|-------|
| Method | `git checkout af5f3fca -- <monitor path>` |
| Source commit | `af5f3fcae588cdf0631ae7b3a4b7b7d48f404ef6` |
| Source blob | `9c0272f6271a666cd50bad501779b8468c03e68c` |
| Resulting worktree blob | `9c0272f6271a666cd50bad501779b8468c03e68c` |
| Semantic parity | YES (byte-identical) |
| Accidental MAIN/runtime WIP | NO |

## Unrelated origin paths imported

`0`
