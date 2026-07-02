# FP-0002 V9-04 Checkpoint Scope v1

**Date:** 2026-07-02

## Explicit staging allowlist

```
.gitignore (forge-intake allow-list exception only)
workspaces/fp-0002-shpigovsky-v9/forge-intake/**
workspaces/fp-0002-shpigovsky-v9/tools/v9-generate-forge-manifests.mjs
workspaces/fp-0002-shpigovsky-v9/tools/v9-generate-forge-intake-docs.mjs
workspaces/fp-0002-shpigovsky-v9/tools/v9-validate-forge-intake.mjs
workspaces/fp-0002-shpigovsky-v9/package.json
workspaces/fp-0002-shpigovsky-v9/README.md
workspaces/fp-0002-shpigovsky-v9/foundation/FP-0002-V9-OPERATIONAL-STATUS.md
workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/PROJECT-STATUS.md
```

## Explicit exclusions

- V9 `src/**`, `dist/**`
- V8/V7 workspaces
- Triumph workspaces
- Storage paths
- Foreign WIP across repo
