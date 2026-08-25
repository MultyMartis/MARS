# TEST ROUTING v1

## Acceptance run

Captured: 2026-08-25T07:40:32Z  
Destination alias: **ADMIN_A**  
Destination hash12: `3FBE21323E22`

| Counter | Value |
|---|---|
| ADMIN_A test messages | 3 |
| MOD_A | 0 |
| MOD_B | 0 |
| MOD_C | 0 |
| customers | 0 |
| production reminder claims created by test | 0 |
| real lead status mutations by test | 0 |

## Isolation

Temporary webhook workflow created, activated, executed once, deactivated, deleted.

No last_window write. No claim write. ACCESS not modified. Moderators/customers not messaged.
