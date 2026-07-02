# FP-0002 V9 Stable Working-Tree Ownership Audit

**Phase:** V9-03 stable baseline checkpoint  
**Date:** 2026-07-02  
**Parent HEAD:** `5e7c86db73398df6a01074a60af3afa796de41b3`

## Summary

| Classification | Scope | Staged |
|----------------|-------|--------|
| `FP0002_V9_PRODUCT_SOURCE` | `workspaces/fp-0002-shpigovsky-v9/src/**`, `dist/**` | Yes |
| `FP0002_V9_BUILD_TOOLING` | `gulpfile.js`, `package.json`, `package-lock.json` | Yes |
| `FP0002_V9_VALIDATION_TOOLING` | `workspaces/fp-0002-shpigovsky-v9/tools/**` | Yes |
| `FP0002_V9_DOCUMENTATION` | V9 `*.md`, `foundation/**`, `audits/**`, `README.md` | Yes |
| `FP0002_OPERATIONAL_STATUS` | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/PROJECT-STATUS.md` | Yes |
| `FP0002_TRACKING_EXCEPTION` | `.gitignore` (V9 narrow allow-list) | Yes |
| `FOREIGN_WIP_PRESERVE` | governance/, projects/atlas/, projects/orca/, projects/mars-*, corvonero pilots, `.tools/`, V7/V8 local edits, etc. | **No** |
| `STORAGE_EXCLUDED` | `X:\AI MARS STORAGE/**` | **No** |
| `GENERATED_OR_CACHE_EXCLUDE` | V9 `node_modules/`, caches | **No** |
| `UNKNOWN_STOP` | **0 paths** | — |

## V9 workspace

Entire operator-approved V9-03G baseline — **new to Git** (previously ignored). All 1233 eligible paths classified as FP-0002 V9 checkpoint scope.

## Protected authorities (not staged)

| Authority | Staged changes | Notes |
|-----------|----------------|-------|
| V8 `workspaces/fp-0002-shpigovsky-v8/` | Local modifications exist | Pre-existing WIP — **not** part of V9 checkpoint |
| Triumph `workspaces/triumph-manipulator-landing/` | 0 diff vs HEAD | Unchanged |
| Excel / canonical spreadsheets | Not in working tree | Unchanged |
| Storage evidence | Excluded | Backup at `v9-03-stable-baseline-checkpoint/` |

## Foreign WIP (preserve, do not stage)

Representative groups (~450 total working-tree entries):

- `governance/mars-reality-index-v0.md`
- `projects/atlas/**` (Corvonero registration)
- `projects/mars-localhost-infrastructure/**`, `projects/mars-website-factory/**`
- `projects/orca/**`
- `projects/mars-search-ppc-production/pilots/corvonero/**`
- `.tools/corvonero-*`, `.recovery-temp/`, `.restore-test-temp/`
- `workspaces/fp-0002-shpigovsky-v7/**` (modified evidence)
- `workspaces/fp-0002-shpigovsky-v8/**` (14 modified paths — **not staged**)
- `web-gpt-sources/**`

## Conclusion

**OWNERSHIP RESOLVED.** Zero unknown paths. Checkpoint stages only `.gitignore`, FP-0002 `PROJECT-STATUS.md`, and `workspaces/fp-0002-shpigovsky-v9/**` (allow-listed).
