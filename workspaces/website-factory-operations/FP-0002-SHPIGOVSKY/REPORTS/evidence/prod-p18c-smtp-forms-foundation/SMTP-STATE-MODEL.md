# SMTP state model (P18C)

Computed by `MailOps::state()`. Saving fields does **not** move to VERIFIED.

| State | Meaning | Suppression | Outbound form mail |
|-------|---------|-------------|--------------------|
| `not_configured` | Incomplete (host/port/user/password/from/recipient) | ON | no |
| `configured_not_verified` | Complete, not tested | ON | no |
| `verified_ready` | Test accepted; operator has not activated | ON | no |
| `verified_active` | Operator activated sending | OFF (MU defers) | yes if complete |
| `error` | Last test failed while complete | ON | no |

This wave ended in **`not_configured`**. Dashboard line: `SMTP SETTINGS READY — CREDENTIALS REQUIRED`.
