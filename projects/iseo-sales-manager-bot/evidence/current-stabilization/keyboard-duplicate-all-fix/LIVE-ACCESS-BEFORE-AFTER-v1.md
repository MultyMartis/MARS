# LIVE-ACCESS-BEFORE-AFTER-v1

## Authority

Live ACCESS sheet (Admin.dev), read-only. Repair did **not** write ACCESS.

## BEFORE (2026-08-27T14:58:42.564Z)

| alias | role | status | hash12 (sanitized) |
|-------|------|--------|--------------------|
| ADMIN_A | admin | active | 3FBE21323E22 |
| MOD_B | moderator | **active** | E67145502141 |
| MOD_A | moderator | revoked | 518CC34C4C0F |
| MOD_C | moderator | revoked | 26B9B999DE8A |
| UNK_D94B50 | public | pending | D94B50C8820C |

`MOD_B_ACCESS_BEFORE = ACTIVE`

## AFTER

Reconfirmed via:

1. Same ACCESS snapshot (no ACCESS node writes in patch).
2. Olya integrity pass: MOD_B `status=active`, actor prefix `u:48ad…` matches today's LEAD_EVENT actors.

`MOD_B_ACCESS_AFTER = ACTIVE`

| Counter | Value |
|---------|------:|
| MOD_B active before | 1 |
| MOD_B active after | 1 |
| ACCESS rows modified by repair | 0 |
