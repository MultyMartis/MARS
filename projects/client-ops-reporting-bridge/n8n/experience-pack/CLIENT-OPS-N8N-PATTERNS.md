# Client Ops n8n Patterns

**Status:** PARTIAL — Phase 1B-B inactive create captured

## Frozen design patterns

- PROFILE_B authenticated webhook intake.
- `responseMode=responseNode` + `respondToWebhook@1.1`.
- Structured accept/reject JSON responses.
- Auth failure before business validation.
- Dedupe deferred in first sandbox (`DEDUPE_DEFERRED_SANDBOX`).
- No Telegram in first sandbox.
- No manual n8n UI node assembly — Cursor/MetaBOT programmer generates JSON.
- Sandbox-first; inactive create; never auto-activate.

## Patterns proven in Phase 1B-B

- Separate write-capable create client from GET-only exporter.
- Dry-run default; `--apply` + exact confirmation phrase for live create.
- Immediate re-GET + sanitized structural diff after create.
- `AUTH_BLOCKED_INACTIVE_ONLY` is acceptable when native credential binding is not evidenced.
- Leave inactive by default; deletion HITL-only.

## Runtime note

Initial exporter runtime remains temporary on operator workstation. Long-term must migrate toward n8n host, bzpm.ru hosting, or a justified split — independently of this pack.
