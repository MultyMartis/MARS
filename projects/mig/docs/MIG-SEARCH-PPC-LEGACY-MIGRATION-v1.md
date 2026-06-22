# MIG Search PPC Legacy Migration v1

**Date:** 2026-06-23  
**Wave:** 1.2

---

## Legacy entry point

| Field | Value |
|-------|--------|
| Path | `projects/mig/lib/runtime/run-mig-session.js` |
| Direct CLI | `node run-mig-session.js <intake.json>` |
| Status | **LOCKED for Search PPC** — non-PPC MIG sessions unchanged |

---

## Search PPC detection

Direct CLI blocks when intake body includes any of:

- `mars_search_ppc: true`
- `search_ppc: true`
- `project_ppc_manifest` / `ppc_manifest_path` / `ppc_state_manifest`
- `workflow: search-ppc` or `mars-search-ppc`
- `intake.project_type: search_ppc`

---

## Canonical gated replacement

```bash
node projects/mig/tools/run-ppc-gated-session.mjs \
  --manifest <project-ppc-state-manifest> \
  --action <source_registration|corpus_intake|normalization|paid_serp|competitor_audit> \
  -- <intake-json-body>
```

Gate adapter API: `projects/mig/tools/mig-ppc-gate.mjs`

---

## Diagnostic bypass

For fixture verification only:

```bash
node run-mig-session.js --diagnostic <fixture.json>
```

Sets diagnostic context; does not authorize production Search PPC evidence.

---

## Module import (non-CLI)

`require('run-mig-session').runMigSession()` remains available for:

- `verify-runtime-mvp-v0.mjs` (generic MIG fixtures without PPC flags)
- `process-inbox.js` (generic task file adapter)

Search PPC production must use the gated wrapper.

---

## Blocker

```text
BLOCKED — LEGACY SEARCH PPC ENTRY POINT REQUIRES LIFECYCLE GATE
```

---

## n8n / external automation

Repository evidence: `incoming/mars-bridge/mars-bridge-workflow.json` is an SEO content stub — **unrelated** to Search PPC MIG.

No repository-wired n8n workflow invoking `run-mig-session.js` for Search PPC was found.

**SAFE UNKNOWN:** remote n8n runtime may exist outside repository — deployment verification required before production Search PPC automation.
