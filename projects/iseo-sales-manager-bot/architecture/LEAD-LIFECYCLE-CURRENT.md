# Lead Lifecycle Current

**Authority:** [PRODUCTION-STABLE-BASELINE-2026-08-17.md](../baselines/PRODUCTION-STABLE-BASELINE-2026-08-17.md)

## Status Vocabulary

| State | Meaning | Actionable |
|-------|---------|------------|
| Pending / actionable | Real lead still awaiting manager disposition | yes |
| Processed | Manager marked as handled via `✅ Обработано` | no |
| Spam | Manager marked as spam via `🚫 Спам` | no |
| Test | Test/non-real record excluded from production reminders | no |
| Archive / legacy non-production | Historical or excluded record | no |

This is not a CRM pipeline. Do not invent stages such as negotiating, won, lost, delivery, or follow-up unless a new product phase explicitly adds them.

## Button Effects

| Telegram action | Effect |
|-----------------|--------|
| `✅ Обработано` | Mark lead processed; record event; make repeated clicks idempotent |
| `🚫 Спам` | Mark lead spam; record event; make repeated clicks idempotent |
| `📄 Исходная заявка` | Display literal raw source; no lifecycle mutation |

## Reminder Non-Effects

Reminder delivery does not change status, timestamps that imply processing, or eligibility except through normal future manager actions. A reminder is notification only.

## Raw Non-Effects

Viewing raw source is read-only:

- no processed/spam transition;
- no reminder exclusion;
- no Gmail state mutation;
- no CLEAN substitution into RAW.

## Idempotency

Lifecycle callbacks must tolerate repeated Telegram callback delivery. The safe result of repeated processed/spam clicks is the same final status plus either a no-op or an auditable repeated-action event.

## Exactly Once Boundaries

Exactly-once is a product intent, not a guarantee from external systems. The implementation uses dedupe indexes, message ids, and delivery stamps to prevent duplicate lead creation and duplicate card delivery where possible.

## Re-Delivery Vs Re-Ingestion

- Re-delivery: a known lead/card is sent or updated again because delivery or callback state needs recovery.
- Re-ingestion: a Gmail source is treated as a new lead.

Recovery may re-deliver. It must not re-ingest an already known Gmail message as a new lead unless a human-approved forensic charter proves that the previous record is invalid.

