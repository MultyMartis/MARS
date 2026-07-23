# Client Ops n8n Experience Pack

**Status:** PARTIAL — FIRST INACTIVE SANDBOX CREATE CAPTURED
Full experience remains incomplete until authenticated POST and later Telegram testing.

## Contents

| File | Purpose |
|------|---------|
| `CLIENT-OPS-N8N-PATTERNS.md` | Accepted patterns |
| `CLIENT-OPS-N8N-ANTI-PATTERNS.md` | Forbidden patterns |
| `CLIENT-OPS-N8N-SYNTAX-MATRIX.md` | Live-evidenced syntax |
| `CLIENT-OPS-N8N-APPLY-EVIDENCE-TEMPLATE.md` | Apply evidence template |
| `CLIENT-OPS-N8N-ROLLBACK-EVIDENCE-TEMPLATE.md` | Rollback evidence template |

## Facts learned from Phase 1B-B inactive create

- Greenfield `POST /api/v1/workflows` with `{name, nodes, connections, settings}` creates inactive workflow successfully.
- Server-managed fields observed on create/re-GET: `id`, `versionId`, `createdAt`, `updatedAt`, plus `settings.callerPolicy` / `settings.availableInMCP`.
- n8n may assign `webhookId` on inactive create even when omitted from the client payload — treat as server-managed; do not embed client-invented webhook IDs.
- Credential binding pattern for this phase: **AUTH_BLOCKED_INACTIVE_ONLY** — no n8n credential created; local gitignored secret prepared; Code placeholder retained.
- Read-back matched client-managed graph (names/types/typeVersions/disabled/connections); no material unexpected graph drift.
- Apply runner lessons: separate write client from GET-only exporter; require `--apply` + exact confirmation phrase; re-GET immediately; sanitize evidence; never activate.
- Rollback boundary: leave inactive; delete HITL-only; no credential orphan in this phase.

## Still incomplete until later charters

- Authenticated POST behavior
- Telegram delivery
- Production activation
- Native header-auth credential create payload shape (still unproven)
