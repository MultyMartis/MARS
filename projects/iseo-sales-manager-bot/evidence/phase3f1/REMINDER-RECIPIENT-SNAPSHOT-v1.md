# REMINDER RECIPIENT SNAPSHOT v1

**Function:** `selectActiveStaffRecipients(accessRows)` in `implementation/runtime-libs/pending-leads-lib.mjs`.

## Rule

From an ACCESS_CONTROL snapshot, select rows where:

- `status === 'active'`, **and**
- `role` is `admin` or `moderator`.

Public, pending, revoked, and blocked rows are always excluded, regardless of any legacy CONFIG allowlist. Rows without a resolvable delivery chat id are skipped (cannot deliver). Deduplication is by opaque `recipient_ref` (or delivery chat id when no hash is present) — one reminder per person even if the ACCESS_CONTROL row appears more than once.

## Output shape (no PII)

```
{
  recipient_ref: '<opaque hash or short masked chat-id ref>',
  role_snapshot: 'admin' | 'moderator',
  delivery_chat_id: '<internal, never logged externally>',
  display_name: '<optional, ACCESS_CONTROL only>'
}
```

## Fixture proof

| ACCESS_CONTROL row | Included? |
|---|---|
| admin, active | yes |
| moderator, active | yes |
| moderator, revoked | **no** |
| public, pending | **no** |

Result: exactly **2** eligible recipients from a 4-row fixture (harness #23, #28); revoked never included (#29).

## Live access snapshot (Phase 3F.1 closeout, sanitized)

| Role | Status | Included in reminder snapshot |
|---|---|---|
| Admin (Андрей) | active | yes |
| Moderator (Мопс) | active | yes |
| Moderator (Оля) | revoked | no |
| Moderator (Никита) | revoked | no |

This matches the eligible-recipients counter used in the Phase 3F.1 report (`reminder eligible recipients = 2`).

*Related: [REMINDER-SCHEDULE-GATE-v1.md](REMINDER-SCHEDULE-GATE-v1.md), [COMMAND-AUTHORIZATION-v1.md](COMMAND-AUTHORIZATION-v1.md).*
