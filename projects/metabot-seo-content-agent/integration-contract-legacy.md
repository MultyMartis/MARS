# SEO Content Agent — Workflow Contract

## Webhook

- Workflow exposes a webhook endpoint in n8n for MARS runtime calls.
- Transport: HTTP `POST` with JSON payload.

## Input

- `action`: workflow action identifier (for example: `outline`, `text`, `factcheck`, `seoqa`).
- `payload`: task data for the selected action.
- `meta` (optional): request metadata (trace ID, source, timestamp).

## Output

- `ok`: boolean execution status.
- `result`: structured workflow output for the requested action.
- `error` (optional): normalized error object when `ok=false`.

## Responsibility split

- MARS is the caller: it triggers this n8n workflow and consumes response payload.
- n8n is the executor: it runs automation steps and keeps credential references.
- Secrets are stored only in n8n credentials; repository exports must stay sanitized.
