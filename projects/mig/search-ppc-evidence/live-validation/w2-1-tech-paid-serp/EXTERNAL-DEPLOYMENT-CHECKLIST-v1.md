# MIG Search PPC — External / n8n Deployment Checklist (Wave 2.1)

**Status:** `NOT VERIFIED — DEPLOYMENT CHECKLIST READY`  
**Remote n8n:** not updated in this task

## Canonical command

```bash
node projects/mig/search-ppc-evidence/runtime/cli/mig-evidence.mjs paid-serp:run \
  --manifest <project-ppc-state-manifest.json> \
  --session <session-config.json>
```

Live bounded session (Wave 2.1):

```bash
node projects/mig/search-ppc-evidence/runtime/cli/run-live-paid-serp-session.mjs \
  --manifest projects/mig/search-ppc-evidence/live-validation/w2-1-tech-paid-serp/project-ppc-state-manifest-v1.json \
  --session projects/mig/search-ppc-evidence/live-validation/w2-1-tech-paid-serp/session-config-v1.json \
  --queries projects/mig/search-ppc-evidence/live-validation/w2-1-tech-paid-serp/query-set-v1.json
```

## Preconditions

| Check | Requirement |
|-------|-------------|
| Manifest | Valid project PPC state manifest; lifecycle ACTIVE; stage SPPC-10 authorized |
| Business hours | `paid-serp:validate-window` or pre-live gate PASS |
| Environment | `PLAYWRIGHT_MODULE_PATH` or bundled Playwright available |
| Output path | Isolated under `C:\AI MARS STORAGE\incoming\mig\` — not production paths |
| CAPTCHA | `STOP_ON_CAPTCHA=1` policy active in session config |
| Timezone | Project `timezone` + `allowed_local_collection_windows` configured |

## Environment variables

| Variable | Purpose |
|----------|---------|
| `CAPTURE_HEADLESS` | `false` for headful (default in Wave 2.1 tech session) |
| `STOP_ON_CAPTCHA` | `1` — halt session on CAPTCHA |
| `CAPTURE_DELAY_MS` | Inter-query pacing base (default 45000) |
| `PLAYWRIGHT_MODULE_PATH` | Optional override for Playwright module location |

## Gated wrapper

All commands must pass `authorizeEvidenceCommand` → `mig-ppc-gate.mjs` → lifecycle gate. No direct ungated SERP scripts in production paths.

## Execution receipt

Receipts written to `projects/mars-search-ppc-production/runtime/receipts/mig/` per authorized action.

## Post-deploy smoke validation

1. `node projects/mig/search-ppc-evidence/tests/run-fixture-tests.mjs` — 20/20
2. `node projects/mig/search-ppc-evidence/tests/run-wave2-bypass-audit.mjs` — 15/15
3. Dry-run: `run-live-paid-serp-session.mjs --dry-run` — pre-live PASS, no browser
4. Single-query bounded live session in approved window

## Rollback

1. Stop n8n workflow / cron trigger
2. Set project manifest `lifecycle_status` to `FROZEN` if needed
3. Preserve evidence under storage path — do not delete for audit
4. Revert to fixture-only `paid-serp:run` mode

## Remote runtime status

`NOT VERIFIED — DEPLOYMENT CHECKLIST READY`
