# V8 Git Whitelist Validation

**Date:** 2026-06-28  
**Policy:** Pointed negate-rules under global `workspaces/*` ignore

## Previous workspace ignore rule

```gitignore
workspaces/*
!workspaces/README.md
```

Plus existing per-workspace allow-lists (Triumph, FP-0002 V7, etc.).

## Rules added

- `!workspaces/fp-0002-shpigovsky-v8/` un-ignore root
- Explicit allow-list for README, package/build files, `src/`, `foundation/`, `docs/`, `audits/`, `plans/`, `tools/`
- Re-ignore inside V8: `node_modules/`, `dist/`, screenshots, temp/logs/cache, zip, `.server.pid`

## Validation (`git check-ignore -v`)

| Path | Expected | Result |
|------|----------|--------|
| `workspaces/fp-0002-shpigovsky-v8/README.md` | tracked (negated) | PASS — matched `!workspaces/fp-0002-shpigovsky-v8/README.md` |
| `workspaces/fp-0002-shpigovsky-v8/src/pages/index.html` | tracked | PASS — matched `!workspaces/fp-0002-shpigovsky-v8/src/**` |
| `workspaces/fp-0002-shpigovsky-v8/dist/index.html` | ignored | PASS — matched `workspaces/fp-0002-shpigovsky-v8/**/dist/` |
| `workspaces/fp-0002-shpigovsky-v8/node_modules/` | ignored | PASS — matched `workspaces/fp-0002-shpigovsky-v8/**/node_modules/` |

## Other workspaces

No changes to other `workspaces/*` allow-lists. V7 and unrelated workspaces remain under existing rules.

## Result

**V8 GIT WHITELIST — ENABLED**
