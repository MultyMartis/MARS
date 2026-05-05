# MARS Runtime (R1)

Minimal execution flow:
Task → Execution Engine → Execution Bridge → Tool Adapter → Result

## Setup

1. Create .env file:

N8N_WEBHOOK_URL=https://n8n.ai-metacode.com/webhook/test

2. Use Node.js 18+

## Run test

node runtime/run-test.js

## Expected result

- status: completed
- signals: []

## Notes

- No queue
- No orchestrator
- No retries
- No secrets stored
- No runtime persistence except local JSON
