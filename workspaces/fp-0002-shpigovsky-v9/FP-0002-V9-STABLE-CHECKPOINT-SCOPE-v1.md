# FP-0002 V9 Stable Checkpoint Scope v1

**Phase:** V9-03 stable baseline checkpoint  
**Date:** 2026-07-02

## Staging groups

### Tracking policy

- `.gitignore` — V9 narrow allow-list block

### V9 product source

- `workspaces/fp-0002-shpigovsky-v9/src/**`

### V9 dist (rendered authority)

- `workspaces/fp-0002-shpigovsky-v9/dist/**`

### Build / package

- `workspaces/fp-0002-shpigovsky-v9/package.json`
- `workspaces/fp-0002-shpigovsky-v9/package-lock.json`
- `workspaces/fp-0002-shpigovsky-v9/gulpfile.js`
- `workspaces/fp-0002-shpigovsky-v9/.gitignore` (if present)

### Tooling

- `workspaces/fp-0002-shpigovsky-v9/tools/**`

### V9 documentation

- `workspaces/fp-0002-shpigovsky-v9/*.md`
- `workspaces/fp-0002-shpigovsky-v9/foundation/**`
- `workspaces/fp-0002-shpigovsky-v9/audits/**`
- `workspaces/fp-0002-shpigovsky-v9/README.md`

### Operational status

- `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/PROJECT-STATUS.md`

## Explicit exclusions

- `X:\AI MARS STORAGE/**`
- `workspaces/fp-0002-shpigovsky-v8/**` (including local WIP)
- `workspaces/triumph-manipulator-landing/**`
- Other workspaces
- Foreign WIP (governance, atlas, orca, corvonero, `.tools/`, etc.)
- `node_modules/`, caches, temp logs
- Failed-state ZIPs inside repo

## Expected staged file count

~1235+ (1233 V9 allow-listed + `.gitignore` + `PROJECT-STATUS.md` + new checkpoint docs)

## Staging method

Explicit path-based `git add` — no `git add .`, no root `-A`, no broad `workspaces/` add.
