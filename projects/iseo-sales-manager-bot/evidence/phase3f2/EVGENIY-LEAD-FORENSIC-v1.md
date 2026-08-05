# EVGENIY LEAD FORENSIC v1 — Phase 3F.2

**Subject:** «Клиент A» (internal label «Евгений», first name only — sanctioned by operator charter; no surname, phone, or email recorded in this file).

## Timeline (authoritative)

| Event | Timestamp (UTC) | Europe/Moscow | Source |
|---|---|---|---|
| Gmail `internalDate` (authoritative `received_at`) | `2026-08-05T13:02:57.000Z` | 05.08.2026 16:02:57 МСК | Gmail API, immutable |
| Operational (Ops) execution success | `2026-08-05T13:04:30.051Z` (duration ≈13.7s) | ≈16:04:16 → 16:04:30 МСК | n8n execution log (exec 23273, `ops-evgeniy`) |
| Process `received_at` (as written) | `2026-08-05T13:04:30.781Z` | 05.08.2026 16:04:30 МСК | CLEAN row |
| Moderator (Мопс) processed-callback attempt | `2026-08-05T14:22:55.186Z` | 05.08.2026 17:22:55 МСК | n8n execution log (exec 23320, `mops-callback`); see [CALLBACK-NOT-FOUND-ROOT-CAUSE-v1.md](CALLBACK-NOT-FOUND-ROOT-CAUSE-v1.md) |

Gap between intake completion and moderator's callback attempt: ≈1h18m — the card was already in the moderator's Telegram chat and acted on well before the lookup failure was diagnosed.

## Processing facts

| Field | Value | Note |
|---|---|---|
| `parser_version` at Parse | `sm-parser-v3.3` | live Parse node |
| `parser_version` reflected on CLEAN write | `sm-parser-v3.2` | **schema/mapping lag** — CLEAN append mapped an older cached value, not the live Parse output |
| `message_format_version` at Format | `sm-msg-v2.4` | live Format node |
| `message_format` reflected on CLEAN write | `sm-msg-v2.2` | same schema/mapping lag pattern as `parser_version` |
| `website` | none | |
| Quality/routing | `NeedsClarification` | |
| Client comment (verbatim, non-sensitive) | «Добрый день!» | |
| `first_reply_ready` | `true` | |
| `is_probable_test` | `false` | correctly classified as a real business lead |
| Delivery recipients | `2` | both stamped delivered |
| `manager_status` before reconciliation | `pending` | tri-state (`pending`/`processed`/`spam`) per [PENDING-SOURCE-FORENSIC-v1.md](../phase3f1/PENDING-SOURCE-FORENSIC-v1.md) |

## Token facts at callback time

| Field | Value |
|---|---|
| CLEAN `telegram_action_token` stored length | `0` |
| Format-generated token length | `12` (hex), embedded identically in both delivered cards |
| CLEAN rows present at callback read time | `106` |

## SAFE UNKNOWN

- Exact RAW row count at this time (not re-derived in this pass; only the CLEAN read count of 106 at callback time is attested).
- Root cause of the `parser_version`/`message_format` mapping lag on CLEAN write — out of scope for the Phase 3F.2 callback-token repair; not fixed in this pass. Tracked as a known anomaly, not resolved.

*Related: [CURRENT-REAL-LEAD-SAFETY-v1.md](CURRENT-REAL-LEAD-SAFETY-v1.md), [CALLBACK-LOOKUP-REPAIR-v1.md](CALLBACK-LOOKUP-REPAIR-v1.md), [EVGENIY-LIFECYCLE-RECONCILIATION-v1.md](EVGENIY-LIFECYCLE-RECONCILIATION-v1.md).*
