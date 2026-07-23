# Safe Apply and Rollback — Client Ops Bridge (bzpm.ru)

**Workflow name:** `MARS Client Ops Bridge — bzpm.ru`
**Profile:** `PROFILE_B_REQUIRED`
**Status:** RUNBOOK / NOT EXECUTED by this charter

## 1. Preconditions

- Client Ops baseline commit present.
- Offline harness PASS.
- Template structural gates PASS.
- Auth binding HITL completed (placeholder removed).
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
3. Reject unresolved `<<<HITL_REQUIRED:CLIENT_OPS_WEBHOOK_AUTH_SECRET>>>`.
4. Reject Telegram / HTTP Request / credentials / webhookId / secrets.

## 4. Create inactive

1. Prepare create payload (name, nodes, connections, settings only).
2. Require `--apply` + typed confirmation.
3. POST through **write-capable** client only.
4. Do **not** activate.
5. Do **not** execute webhook test in the create charter unless separately authorized.

## 5. Post-create re-read

1. Re-GET created workflow by id.
2. Diff name / active / node types / connections.
3. Sanitize evidence (no secrets, no raw bodies).
4. Record rollback boundary.

## 6. Rollback default (safer)

**Default:** leave the inactive sandbox in place and mark it **ABANDONED** if not proceeding.

Rationale: avoids accidental delete of the wrong workflow id; keeps forensic evidence.

## 7. Delete rollback (HITL only)

Delete is allowed **only** when:

- workflow is confirmed inactive;
- name matches exactly;
- id matches create evidence;
- operator explicitly approves delete;
- no production traffic path is attached.

Deletion is **never** automatic.

## 8. Future PUT update rollback

1. Keep before-PUT sanitized export.
2. PUT only under explicit charter.
3. On failure, restore previous inactive export via approved apply procedure.
4. Never activate as part of rollback.

## 9. Credential binding gate

- Secret value never in Git / template / reports.
- Binding mechanism remains HITL until live evidence freezes env/credential access syntax.
- Failed auth must return HTTP 401 without mismatch details.

## 10. Test POST gate (later charter)

- Authorized only after inactive create + auth binding.
- Uses synthetic envelope fixtures.
- No SITE-002 mutation.
- No Telegram send.

## 11. Telegram gate (later)

- Separate charter.
- Dedicated Client Ops bot recommended.
- Not part of first sandbox create.

## 12. Production activation gate

- Explicit HITL.
- Separate from sandbox create.
- Requires multi-day observation plan and rollback plan acceptance.
