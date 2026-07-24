# Client Ops n8n Patterns

**Status:** PARTIAL — Phase 1B-B/B1/B2 + C0S semantics captured

## Frozen design patterns

- PROFILE_B authenticated webhook intake.
- `responseMode=responseNode` + `respondToWebhook@1.1`.
- Structured accept/reject JSON responses.
- Auth failure before business validation.
- Dedupe deferred in first sandbox (`DEDUPE_DEFERRED_SANDBOX`).
- No Telegram in first sandbox create; Telegram apply is a later gate.
- **Pattern B (runtime-confirmed on this host):** accepted path → Respond to Webhook → Telegram `sendMessage`.
- No manual n8n UI node assembly — Cursor/MetaBOT programmer generates JSON.
- Sandbox-first; inactive create; never leave activated after POST tests.

## Patterns proven in Phase 1B-B / B1 / B2

- Separate write-capable create client from GET-only exporter.
- Dry-run default; `--apply` + exact confirmation phrase for live create.
- Immediate re-GET + sanitized structural diff after create.
- `AUTH_BLOCKED_INACTIVE_ONLY` is acceptable when native credential binding is not evidenced.
- Prefer `AUTH_NATIVE_HEADER_CREDENTIAL_BOUND` / confirmed with dedicated `httpHeaderAuth` credential and Webhook `authentication=headerAuth`.
- Keep secrets in gitignored local files and n8n credential store — never in workflow JSON / Code / Git evidence.
- Controlled temporary activation allowlisted by workflow ID; deactivate in `finally`; never print full webhook URL.
- Native Header Auth rejects with HTTP 403 text before business executions.
- Malformed/oversized bodies may be rejected by native parse (HTTP 422) before workflow size gates.
- Leave inactive by default; deletion HITL-only.

## Patterns proven in Phase 1B-C0S

- Downstream nodes after `Respond to Webhook` execute on this installation.
- Telegram `sendMessage` after Respond delivers exactly once when placed on the sequential accepted path.
- Temporary semantics workflow containment: activate only for the test window; delete after evidence.

## Runtime note

Initial exporter runtime remains temporary on operator workstation. Long-term must migrate toward n8n host, bzpm.ru hosting, or a justified split — independently of this pack.
