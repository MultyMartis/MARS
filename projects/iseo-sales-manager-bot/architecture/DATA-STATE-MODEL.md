# Data State Model

**Authority:** [CURRENT-PRODUCTION-ARCHITECTURE.md](CURRENT-PRODUCTION-ARCHITECTURE.md) and [PRODUCTION-STABLE-BASELINE-2026-08-17.md](../baselines/PRODUCTION-STABLE-BASELINE-2026-08-17.md)

## Core Rule

RAW and CLEAN are different authorities.

- RAW is the durable visible source captured from Gmail before parsing.
- CLEAN is the normalized operational lead used for manager cards, lifecycle, reminders, dedupe, and reporting.
- RAW must not be reconstructed from CLEAN.
- CLEAN must not be used as a substitute for RAW in `📄 Исходная заявка`.

## Sheets Workbooks

| Workbook / tab | Role | Writer | Reader |
|----------------|------|--------|--------|
| RAW `lead_raw_v2` | Original visible source and intake metadata | Operational.dev | Admin.dev raw callback, forensics |
| CLEAN `lead_clean_v2` | Normalized lead and lifecycle | Operational.dev, Admin.dev callbacks | Telegram card, reminders, admin |
| CLEAN `CONFIG` | Runtime keys and operator config | Admin/operator-controlled process | Operational.dev, Admin.dev |
| CLEAN `LEAD_EVENTS` | Audit trail of lead actions | Operational.dev, Admin.dev | Operators, forensics |
| CLEAN `ERRORS` | Error and anomaly records | Operational.dev, Admin.dev | Operators, forensics |
| CLEAN `DEDUP_INDEX` | Duplicate and delivery guard state | Operational.dev | Operational.dev |

## RAW Fields Purpose

RAW fields exist to preserve intake authority and allow safe source display:

- `lead_id`: cross-system identity.
- `source_message_id`: Gmail identity for legacy READ-only fallback.
- `raw_text` / `source_body_full`: full visible source body.
- intake timestamps and source metadata: provenance.
- lossy/snippet classification when applicable: warning that stored source is not complete.

RAW is append-oriented for new intake. Raw-source display must not mutate RAW.

## CLEAN Fields Purpose

CLEAN fields exist to support operations:

- `lead_id`: stable lead identity.
- normalized contact/request/site fields: manager card content.
- lifecycle/status fields: pending/actionable, processed, spam, test/archive handling.
- delivery fields: Telegram message ids, attempts, finalization markers.
- reminder fields or derived state: candidate selection and exclusion.
- parser/config/version markers: reproducibility and forensics.

CLEAN may mutate only through defined operational actions: intake creation, Telegram delivery stamping, processed/spam callbacks, admin-approved config or correction flows, and explicit forensic repair charters.

## CONFIG

CONFIG stores runtime keys by name. Current stable keys include:

- `ai_enabled=false`
- `pending_reminders_enabled=true`
- `pending_reminder_time=10:00`
- `pending_reminder_timezone=Europe/Moscow`
- parser/version and operator allow-list keys as configured in n8n/Sheets

Secret values do not belong in docs. Use CONFIG key names and n8n credential names only.

## Events, Errors, Dedupe

- `LEAD_EVENTS` records what happened and why.
- `ERRORS` records operational failures without exposing secrets or raw PII.
- `DEDUP_INDEX` prevents re-ingestion and supports delivery guards.

## Mutation Boundaries

| Action | Mutates RAW | Mutates CLEAN | Notes |
|--------|-------------|---------------|-------|
| New Gmail intake | yes, append | yes, create/update operational row | Captures RAW before parse |
| Telegram delivery | no | yes | Delivery stamps/attempts only |
| `✅ Обработано` | no | yes | Idempotent lifecycle action |
| `🚫 Спам` | no | yes | Idempotent lifecycle action |
| `📄 Исходная заявка` | no | no | Read-only source display |
| Reminder notification | no | no | No lifecycle mutation |
| Legacy Gmail fallback | no | no | READ-only by `source_message_id` |

