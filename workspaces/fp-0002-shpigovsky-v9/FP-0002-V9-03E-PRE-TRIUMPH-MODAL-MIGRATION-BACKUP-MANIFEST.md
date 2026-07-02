# FP-0002 V9-03E Pre-Triumph Modal Migration Backup Manifest

**Phase:** V9-03F pre-edit backup  
**Created:** 2026-07-02  
**Scope:** `X:\AI MARS\workspaces\fp-0002-shpigovsky-v9` only

## Archive

| Field | Value |
|-------|-------|
| ZIP path | `X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v9\v9-03f-triumph-modal-migration\FP-0002-V9-03E-PRE-TRIUMPH-MODAL-MIGRATION.zip` |
| Snapshot root | `X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v9\v9-03f-triumph-modal-migration\snapshot-before-triumph-modal-migration\` |
| Size | 484,755,376 bytes |
| File count (workspace copy) | 1914 |
| SHA-256 | `134F4D887770A0F8ADABB0BFC26AB400B867BEA3FEF1DBCD384F9501A11E6730` |

## Preflight captured

- Branch: `mars/canonical-post-recovery`
- HEAD: `5e7c86db73398df6a01074a60af3afa796de41b3`
- Git status/diff under `snapshot-before-triumph-modal-migration/preflight/`

## Scoped restore guidance

Restore **only** into `X:\AI MARS\workspaces\fp-0002-shpigovsky-v9` when rolling back V9-03F modal migration.

1. Stop V9 preview/build processes using the workspace.
2. Extract ZIP to a temporary folder outside git roots.
3. Copy **only** matching paths from extracted `v9-workspace/` into `X:\AI MARS\workspaces\fp-0002-shpigovsky-v9\` — file-by-file or folder merge with review.
4. Re-run `npm run build` in the V9 workspace.

**Prohibited:** `/MIR`, `/PURGE`, `git clean`, `git reset`, broad overwrite of `X:\AI MARS`, restore into V8, Triumph, or Storage evidence trees.

## Exclusions

- `node_modules`, caches, V8, unrelated projects, recursive Storage evidence.
