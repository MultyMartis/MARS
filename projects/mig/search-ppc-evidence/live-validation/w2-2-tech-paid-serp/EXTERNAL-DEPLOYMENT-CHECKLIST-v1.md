# MIG Search PPC — External Deployment Checklist (Wave 2.2)

**Status:** `NOT VERIFIED — DEPLOYMENT CHECKLIST READY`  
**Remote n8n:** not updated in this task

## Acquisition modes

| Mode | Command | Status in local Cursor env |
|------|---------|---------------------------|
| **A — Automated** | `run-live-paid-serp-session.mjs` | Available — Playwright; CAPTCHA risk observed |
| **B — Assisted** | `paid-serp:import-assisted` + operator bundle | Available — pipeline validated |

## Mode A — Automated capture

```bash
node projects/mig/search-ppc-evidence/runtime/cli/run-live-paid-serp-session.mjs \
  --manifest projects/mig/search-ppc-evidence/live-validation/w2-1-tech-paid-serp/project-ppc-state-manifest-v1.json \
  --session projects/mig/search-ppc-evidence/live-validation/w2-2-tech-paid-serp/session-config-recovery-v1.json \
  --queries projects/mig/search-ppc-evidence/live-validation/w2-1-tech-paid-serp/query-set-v1.json
```

Recovery profile differences (vs session-001): persistent Chrome profile, warm navigation, single query.

## Mode B — Operator-assisted capture

1. Operator runs query in normal browser during approved window.
2. Use DevTools snippet: `runtime/tools/assisted-capture-snippet.js`
3. Prepare bundle: `runtime/cli/prepare-assisted-capture-bundle.mjs --bundle <dir>`
4. Save `screenshot.png` + `page.html`; finalize checksums.
5. Import:

```bash
node projects/mig/search-ppc-evidence/runtime/cli/mig-evidence.mjs paid-serp:import-assisted \
  --manifest projects/mig/search-ppc-evidence/live-validation/w2-1-tech-paid-serp/project-ppc-state-manifest-v1.json \
  --bundle <capture-bundle-dir> \
  --session projects/mig/search-ppc-evidence/live-validation/w2-1-tech-paid-serp/session-config-v1.json \
  --queries projects/mig/search-ppc-evidence/live-validation/w2-1-tech-paid-serp/query-set-v1.json \
  --output "C:/AI MARS STORAGE/incoming/mig/live-validation/w2-2-tech-paid-serp/assisted-import-001"
```

## Environment availability

| Environment | Mode A | Mode B |
|-------------|--------|--------|
| Local Cursor | Available (business-hours gated) | Available (operator browser required) |
| Local operator browser | N/A | Required for genuine live capture |
| Future n8n | NOT VERIFIED | NOT VERIFIED |
| Remote runtime | NOT VERIFIED | NOT VERIFIED |

## Preconditions (both modes)

| Check | Requirement |
|-------|-------------|
| Manifest | TECHNICAL TEST project; SPPC-10 authorized |
| Business hours | Within `allowed_local_collection_windows` |
| CAPTCHA | `STOP_ON_CAPTCHA` — no bypass |
| Authority | `production_authority: false` |

## Post-deploy smoke validation

1. `node projects/mig/search-ppc-evidence/tests/run-fixture-tests.mjs` — 20/20
2. `node projects/mig/search-ppc-evidence/tests/run-assisted-capture-tests.mjs` — 12/12
3. `node projects/mig/search-ppc-evidence/tests/run-wave2-bypass-audit.mjs` — 20/20

## Remote runtime status

`NOT VERIFIED — DEPLOYMENT CHECKLIST READY`

Contract: [operator-assisted-live-serp-capture-v1.md](../../contracts/operator-assisted-live-serp-capture-v1.md)
