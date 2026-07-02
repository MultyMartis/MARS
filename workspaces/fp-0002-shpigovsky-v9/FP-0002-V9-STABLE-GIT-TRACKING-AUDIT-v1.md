# FP-0002 V9 Stable Git Tracking Audit v1

**Phase:** V9-03 stable baseline checkpoint  
**Date:** 2026-07-02

## Prior ignore rule

`workspaces/*` (`.gitignore` line 64) ignored the entire V9 workspace. Global rules also ignored `dist/` and `node_modules/`.

`git check-ignore -v workspaces/fp-0002-shpigovsky-v9` → matched `workspaces/*`.

## Chosen tracking method

**Narrow explicit allow-list** under `.gitignore`, mirroring FP-0002 V8 / Triumph patterns:

- Un-ignore `workspaces/fp-0002-shpigovsky-v9/` directory
- Re-ignore `workspaces/fp-0002-shpigovsky-v9/*` then allow-list approved subtrees and root `*.md`
- **Include `dist/`** as operator-approved rendered/deploy authority (unlike V8)
- Exclude `node_modules/`, caches, temp, logs, `.server.pid` within V9

## `.gitignore` change

Added block **FP-0002 Shpigovsky V9** after V8 block (lines ~346–369).

## Proof unrelated workspaces remain ignored

| Path | `check-ignore` result |
|------|------------------------|
| `workspaces/fp-0002-shpigovsky-v9/package.json` | **tracked** (`!workspaces/fp-0002-shpigovsky-v9/package.json`) |
| `workspaces/fp-0002-shpigovsky-v9/dist/index.html` | **tracked** (`!workspaces/fp-0002-shpigovsky-v9/dist/**`) |
| `workspaces/fp-0002-shpigovsky-v9/node_modules/test` | **ignored** (`**/node_modules/`) |
| `workspaces/fp-0002-shpigovsky-v7/package.json` | unchanged V7 allow-list (still tracked if previously tracked) |
| `workspaces/fp-0002-shpigovsky-v8/package.json` | unchanged V8 allow-list |

No broad `git add -f workspaces/` used.

## Eligible V9 paths for commit

- `workspaces/fp-0002-shpigovsky-v9/README.md`, `.gitignore`, `package.json`, `package-lock.json`, `gulpfile.js`
- `workspaces/fp-0002-shpigovsky-v9/src/**`
- `workspaces/fp-0002-shpigovsky-v9/dist/**`
- `workspaces/fp-0002-shpigovsky-v9/tools/**`
- `workspaces/fp-0002-shpigovsky-v9/foundation/**`
- `workspaces/fp-0002-shpigovsky-v9/audits/**`
- `workspaces/fp-0002-shpigovsky-v9/*.md` (checkpoint and phase reports)

**Untracked eligible count (pre-stage):** 1233 files

## Excluded V9 paths

- `node_modules/`
- `.cache/`, `temp/`, `logs/`, `coverage/`
- `.server.pid`

## Conclusion

**SAFE NARROW TRACKING ESTABLISHED.** V9 is the only newly un-ignored FP-0002 frontend workspace; unrelated workspaces remain under existing ignore/allow rules.
