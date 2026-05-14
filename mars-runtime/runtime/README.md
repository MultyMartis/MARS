# MARS Runtime (R1)

**Posture:** experimental **manual** scripts only — **not** a MARS runtime product, **not** an orchestrator, **not** a control plane, **not** background or hidden execution.

## Current scope

- Narrow in-process **sketch**: validate task → static workflow map → adapter **dispatch** → optional JSON run snapshots
- `execution-engine.js` — task/run helper (not a full “engine” product subsystem)
- `execution-bridge.js` — adapter routing (not the full v0 Execution Bridge contract implementation)
- n8n adapter (HTTP POST to **your** configured webhook)
- SEO Content Agent adapter (separate env URL; external system owns behavior)
- Runtime config + static tool registry (demo lookup, not repo-wide policy)
- Smoke tests

## Requirements

- Node.js 18+
- A reachable **operator-configured** n8n webhook URL you supply (**external** instance; “production” here means *your* live/stage n8n, **not** a shipped MARS runtime tier)
- `N8N_WEBHOOK_URL` environment variable

## Environment

PowerShell:

$env:N8N_WEBHOOK_URL="https://n8n.ai-metacode.com/webhook/test"

## Run one test task

node mars-runtime/runtime/run-test.js

Expected:

- status: completed
- signals: []

## Run smoke tests

node mars-runtime/runtime/test-runtime.js

Expected:

- valid task → completed
- invalid task → failed + UNKNOWN
- unknown workflow → failed + UNKNOWN

## State files

Runtime state snapshots are stored in:

mars-runtime/state/runs/

They are generated artifacts and are ignored by git.

## Not implemented yet

- queue
- orchestrator
- retries
- memory/RAG integration
- model routing
- production deployment
