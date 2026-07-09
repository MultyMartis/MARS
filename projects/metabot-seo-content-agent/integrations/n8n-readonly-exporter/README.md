# MetaBOT Developer — n8n Read-only Exporter v1

**Status:** tooling — GET-only read access to live n8n workflows for MetaBOT SEO Content Agent Beta v14.

## Purpose

This package exports **exact allowlisted** n8n workflows via the **n8n REST API** (not webhook task dispatch), sanitizes workflow JSON, and writes an **evidence pack** for MetaBOT Developer documentation and parity review.

## What this tool does

- Loads credentials from `local/tokens/n8n-api.env` (gitignored)
- **GET-only** calls to n8n:
  - `GET /api/v1/workflows`
  - `GET /api/v1/workflows/{id}`
- Matches workflows by **exact name** (default allowlist — see below)
- Sanitizes credentials, tokens, webhook IDs, personal IDs, pin/execution data
- Writes **raw** exports only to gitignored `projects/metabot-seo-content-agent/raw/`
- Writes **sanitized** JSON + manifest docs to `projects/metabot-seo-content-agent/exports/live-v14-evidence/YYYY-MM-DD/`
- Runs a post-export secret pattern scan on evidence files

## What this tool does NOT do

- No POST, PUT, PATCH, DELETE to n8n
- No workflow activation/deactivation
- No Telegram, OpenRouter, or Google Sheets calls
- No webhook task dispatch
- No live workflow modifications
- No npm dependencies (Node.js built-ins only)
- No automatic git commit

## Credential setup

Create (local only, never commit):

```
X:\AI MARS\local\tokens\n8n-api.env
```

Required variables:

```env
N8N_API_URL=https://n8n.ai-metacode.com
N8N_API_KEY=<your-api-key>
```

The API key is sent as header `X-N8N-API-KEY`. The exporter never prints the key.

## Target workflow names (exact match)

Default allowlist:

1. `SEO Content Agent Beta.v14 - Intake`
2. `SEO Content Agent Beta.v14 - Worker`
3. `SEO Content Agent Beta.v14 - Admin`

Override only with explicit CLI input: `--names "Name A|Name B"`.

## Commands

Run from repository root (`X:\AI MARS`):

### Dry-run (default)

Lists target workflows found by exact name. No file writes.

```bash
node projects/metabot-seo-content-agent/integrations/n8n-readonly-exporter/export-workflows.mjs --dry-run
```

### Report-only

Fetches workflow JSON and prints summary. No file writes.

```bash
node projects/metabot-seo-content-agent/integrations/n8n-readonly-exporter/export-workflows.mjs --report-only
```

### Full export

Fetches workflows, writes raw + sanitized outputs. **Requires operator approval.**

```bash
node projects/metabot-seo-content-agent/integrations/n8n-readonly-exporter/export-workflows.mjs --export
```

Optional date override:

```bash
node projects/metabot-seo-content-agent/integrations/n8n-readonly-exporter/export-workflows.mjs --export --date 2026-07-10
```

## Output locations

| Output | Path |
|--------|------|
| Raw (gitignored) | `projects/metabot-seo-content-agent/raw/live-export-YYYY-MM-DD/*.raw.json` |
| Sanitized JSON | `projects/metabot-seo-content-agent/exports/live-v14-evidence/YYYY-MM-DD/*.sanitized.json` |
| Evidence docs | Same evidence folder — `EXPORT-MANIFEST.md`, `SANITIZATION-REPORT.md`, etc. |

Sanitized filenames:

- `SEO-Content-Agent-Beta-v14-Intake.sanitized.json`
- `SEO-Content-Agent-Beta-v14-Worker.sanitized.json`
- `SEO-Content-Agent-Beta-v14-Admin.sanitized.json`

## Sanitization policy

Recursive redaction with markers:

- `REDACTED_CREDENTIAL`, `REDACTED_CREDENTIAL_ID`
- `REDACTED_TOKEN`, `REDACTED_WEBHOOK_URL`, `REDACTED_WEBHOOK_ID`
- `REDACTED_SHEET_ID`, `REDACTED_PRIVATE_DATA`, `REDACTED_PERSONAL_ID`
- `REDACTED_EXECUTION_DATA`, `REDACTED_PINNED_DATA`

**Kept (after pattern scan):** workflow name, node names/types, connections, routing structure, code node bodies, prompt text, model names, non-sensitive tab names.

## Safe-to-commit policy

- **Never** commit `raw/` exports
- Review `SANITIZATION-REPORT.md` before committing evidence
- If post-export scan finds risky patterns → `NOT_SAFE_TO_COMMIT`
- Operator manual review is always required

## No-mutation guarantee

The API client rejects any HTTP method other than `GET`. There is no code path for create/update/delete/activate operations.

## Operator approval gates

1. Run `--dry-run` first
2. Confirm exactly 3 target workflows found (or document gaps)
3. Run `--report-only` if needed for node counts without writes
4. Run `--export` only with explicit operator approval
5. Review evidence pack and sanitization report before any git staging

## Troubleshooting

### 401 Unauthorized

- Verify `N8N_API_KEY` in `local/tokens/n8n-api.env`
- Ensure the key is valid and not expired
- Confirm the key has workflow read permissions in n8n
- Check `N8N_API_URL` matches the live instance (`https://n8n.ai-metacode.com`)

### Workflow not found in dry-run

- Names must match **exactly** (including `Beta.v14` and spacing)
- Use `--names` override only when intentionally exporting a different set

### Raw write blocked

- Exporter verifies `projects/metabot-seo-content-agent/raw/` is listed in `.gitignore`
- Fix `.gitignore` before export if missing

## Files

| File | Role |
|------|------|
| `export-workflows.mjs` | CLI entrypoint |
| `sanitize-workflow.mjs` | Recursive sanitizer + secret scan |
| `lib/n8n-api-client.mjs` | GET-only API client |
| `lib/allowlist.mjs` | Exact workflow name allowlist |
| `lib/manifest.mjs` | Evidence pack markdown generators |
