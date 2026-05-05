# MARS Runtime (R1)

## Current scope

- Minimal runtime only
- Execution Engine
- Execution Bridge
- n8n Adapter
- Runtime Config
- Tool Registry
- Input / workflow validation
- Smoke tests

## Requirements

- Node.js 18+
- Active n8n production webhook
- N8N_WEBHOOK_URL environment variable

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
