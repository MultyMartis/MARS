# Safe Apply and Rollback — Client Ops Bridge (bzpm.ru)

**Status:** RUNBOOK + PHASE 1B-B EXECUTED (inactive create)
**Workflow name:** `MARS Client Ops Bridge — bzpm.ru`
**Profile:** `PROFILE_B_REQUIRED`
**Phase 1B-B result:** inactive workflow created; auth blocked; no webhook test; no Telegram

## 1. Preconditions

- Client Ops baseline commit present.
- Offline harness PASS.
- Template structural gates PASS.
- For Phase 1B-B: blocked-inactive auth mode authorized when native binding unproven.
- Write-capable n8n client available (not GET-only exporter).
- Operator confirmation phrase prepared.
- Telegram **not** in scope for first sandbox.

## 2. Pre-create snapshot

1. Record HEAD SHA.
2. Record template SHA / path.
3. List existing workflows by name via GET-only client (read).
4. Confirm no workflow already named `MARS Client Ops Bridge — bzpm.ru`.

## 3. Template validation

1. Run `validate-template.mjs`.
2. Run `run-harness.mjs`.
3. For blocked-inactive mode: retain placeholder; validate via `validate-client-ops-apply-payload.mjs`.
4. Reject Telegram / HTTP Request / webhookId / live secrets.

## 4. Create inactive

1. Prepare create payload under local ignored apply locus.
2. Require `--apply` + confirmation `CREATE INACTIVE MARS CLIENT OPS BRIDGE BZPM`.
3. POST through **write-capable** client only.
4. Do **not** activate.
5. Do **not** execute webhook test unless separately authorized.

## 5. Post-create re-read

1. Re-GET created workflow by id.
2. Diff name / active / node types / connections.
3. Sanitize evidence (no secrets, no raw bodies).
4. Record rollback boundary.

## 6. Rollback default (safer)

**Default:** leave the inactive sandbox in place and mark it **ABANDONED** if not proceeding.

## 7. Delete rollback (HITL only)

Delete only when inactive, exact name/id match, explicit operator approval, and no production traffic path. Never automatic.

## 8. Credential binding gate

- Secret value never in Git / template / reports.
- Phase 1B-B: `AUTH_BLOCKED_INACTIVE_ONLY` at create; local secret prepared outside Git.
- Phase 1B-B1: `AUTH_NATIVE_HEADER_CREDENTIAL_BOUND`; dedicated `httpHeaderAuth` credential created and bound; workflow remains inactive; no webhook POST.
- Failed auth must return HTTP 401 without mismatch details.

## 9. Test POST gate (later charter)

- Authorized only after inactive create + auth binding.
- Synthetic envelopes only; no SITE-002 mutation; no Telegram send.

## 10. Telegram gate

- Phase 1B-C: bot `@monitor_bzpm_metacode_bot` + unbound `telegramApi` credential intake complete; no message send; workflow unchanged.
- Phase 1B-C0: chat-target discovery retry returned 0 updates.
- Phase 1B-C0R2: chat target confirmed (`TELEGRAM_CHAT_TARGET_CONFIRMED`); local ignored target file created.
- Phase 1B-C0S: Pattern B continuation-after-Respond **confirmed** via temporary semantics workflow (deleted); readiness `READY_FOR_TELEGRAM_SANDBOX_INTEGRATION_APPLY`; apply still requires Phase 1B-C1 charter.
- Display name: `Монитор bzpm.ru — MetaCODE`.
- Avatar requirement: bzpm.ru logo (verification SAFE UNKNOWN via Bot API).
- Never put bot token in workflow JSON.
- Avatar: bzpm.ru logo.
- Not part of first sandbox create.

## 11. Production activation gate

- Explicit HITL; separate from sandbox create.
