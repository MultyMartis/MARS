# Gmail Intake Contract

**Authority:** [CURRENT-PRODUCTION-ARCHITECTURE.md](CURRENT-PRODUCTION-ARCHITECTURE.md)

## Stable Contract

New leads are fetched from Gmail by Operational.dev with full message access:

1. Gmail fetch uses `simple=false`.
2. The parser captures the full visible body before field extraction.
3. `text/plain` is preferred when complete.
4. HTML fallback preserves structure: line breaks, block boundaries, and URLs.
5. The full source is written to RAW before CLEAN-only normalization becomes operational authority.
6. Snippet is not authoritative when a body exists.

## Required Outputs

- RAW row with `lead_id`, Gmail provenance, and full visible source body.
- CLEAN row with normalized operational fields.
- Dedupe state sufficient to avoid treating the same Gmail source as a new lead.
- Events/errors where intake fails or the source is lossy.

## Anti-Pattern: `simple=true`

`simple=true` / snippet-only fetch caused lossy source behavior. It can hide body content, collapse structure, and make `📄 Исходная заявка` impossible to satisfy literally.

Reusable rule: never build raw-source UX from Gmail snippets when the full body is available.

## Parsing Boundary

The parser may normalize fields for CLEAN cards, but it must not destroy source authority. The order is:

```text
fetch full Gmail body -> capture durable RAW -> parse/normalize -> write CLEAN -> deliver card
```

## HTML Fallback

When `text/plain` is unavailable or incomplete, HTML must be converted to readable text without flattening the message into a single lossy paragraph. Links should remain visible where they were part of the source.

## Gmail State

Gmail fallback for legacy records is READ-only by `source_message_id`. It must not mark messages, replay ingestion, mutate labels, or create new leads.

## Acceptance Checks

- A real full-body message yields literal RAW source.
- `📄 Исходная заявка` can display the original visible request.
- Snippet-only records are classified as lossy.
- No raw PII or Gmail body is committed to Git documentation.

