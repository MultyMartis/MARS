# Client Ops n8n Patterns

**Status:** SKELETON — TO BE COMPLETED AFTER FIRST SANDBOX APPLY

## Frozen design patterns (pre-sandbox)

- PROFILE_B authenticated webhook intake.
- `responseMode=responseNode` + `respondToWebhook@1.1`.
- Structured accept/reject JSON responses.
- Auth failure before business validation.
- Dedupe deferred in first sandbox (`DEDUPE_DEFERRED_SANDBOX`).
- No Telegram in first sandbox.
- No manual n8n UI node assembly — Cursor/MetaBOT programmer generates JSON.
- Sandbox-first; inactive create; never auto-activate.

## Runtime note

Initial exporter runtime remains temporary on operator workstation. Long-term must migrate toward n8n host, bzpm.ru hosting, or a justified split — independently of this pack.
