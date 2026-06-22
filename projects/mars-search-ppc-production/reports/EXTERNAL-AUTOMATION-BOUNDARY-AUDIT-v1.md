# External Automation Boundary — Search PPC v1

**Date:** 2026-06-23  
**Wave:** 1.2

---

## Repository inspection scope

- n8n workflow exports under `incoming/`
- `mars-runtime/adapters/n8n-adapter.js`
- npm scripts in Triumph exporter `package.json`
- PowerShell/batch wrappers in `projects/mig/`
- Project documentation references

---

## Classification

| Reference | Classification | Action |
|-----------|----------------|--------|
| `incoming/mars-bridge/mars-bridge-workflow.json` | **Unrelated** — SEO content stub | No change |
| `projects/seo-content-agent/integrations/n8n-mars-bridge-map-code.txt` | **Unrelated** | No change |
| Triumph `exporter-cli/package.json` npm scripts | **Active legacy** | Documented LOCKED; use `run-ppc-gated-export.mjs` |
| `projects/mig/tools/verify-runtime-mvp-v0.mjs` | **Diagnostic** | Uses module import without PPC flags — allowed |
| `projects/mig/lib/task-file-adapter/process-inbox.js` | **Generic MIG** | Non-PPC; no Search PPC lockdown applied |
| Remote n8n production runtime | **SAFE UNKNOWN** | Not accessible from repository |

---

## Deployment verification checklist (mandatory before production automation)

- [ ] Confirm no remote workflow invokes `run-mig-session.js` with Search PPC intake without gated wrapper  
- [ ] Confirm no remote workflow invokes `orca-admission.mjs integration:run` without `orca-ppc-gate.mjs`  
- [ ] Confirm no remote workflow invokes Triumph `export.js` or `sheet1-patch-export.js` directly  
- [ ] Confirm all automation passes `--manifest` to gated CLIs  
- [ ] Confirm execution receipts are collected per run  

**Cannot be marked verified** until external runtime is inspected.

---

## Wave 2 impact

Repository canonical entry points are gated. External route documented as deployment verification requirement. Does not block Wave 2 authorization.
