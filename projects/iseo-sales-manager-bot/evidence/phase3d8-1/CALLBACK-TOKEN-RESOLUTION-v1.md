# CALLBACK TOKEN RESOLUTION v1

## Contract

| Action | Callback data |
|--------|----------------|
| processed | `sm:p:<opaque-lead-token>` |
| spam | `sm:s:<opaque-lead-token>` |

## Token algorithm

- **FNV dual-hash** over `lead_id` (12 hex chars) — same as Operational Format Telegram Lead Card
- Actor identity hashing remains SHA-256 (`u:` + 12 hex)
- No Telegram message ID / recipient / PII in token
- Byte length of full callback_data observed: **17** (`sm:p:` + 12)

## Resolution

1. Prefer CLEAN.`telegram_action_token` exact match
2. Else recompute FNV from CLEAN.`lead_id`
3. Exactly one business lead must match

## Phase 3D.8.1

Live Admin Handle Callback already FNV-aligned (from 3D.8). Harness confirms processed/spam parse + mismatch reject.
