# PRODUCTION INVARIANTS — Phase 3G.1.1

**Date:** 2026-08-06

## Unchanged production guards

| Invariant | State |
|-----------|-------|
| AI / OpenRouter | OFF — nodes disabled; `/ai_status` → OFF |
| Reminders | OFF — `pending_reminders_enabled=false` |
| Sales-Manager-v2 | inactive — sole Gmail intake on Operational.dev |
| Automatic client messages | 0 |
| Workflows created | 0 |
| Access-role changes | 0 |
| Revoked users restored | 0 |
| Existing production lead regenerated | 0 |
| Destructive deletions | 0 |

## Reporting / stats

- One business lead = one reporting row (no per-recipient multiplication)
- Acceptance fixtures excluded from production stats via synthetic markers
- Stats baseline epoch unchanged unless independent real lead arrives

## Delivery / lifecycle

- Claim-before-send preserved
- Fail-closed on missing/invalid sender name (copy omitted; card still delivers)
- Shared lifecycle across recipients; personalized drafts only in recipient storage

## Sheets

- ACCESS_CONTROL profile columns Q–V live and seeded
- TEST_LEADS used for acceptance mirror rows only
- No second spreadsheet file introduced

## Gmail intake

- Sole active intake path preserved on Operational.dev
- No filter or label mutations in this documentation wave

## Operator boundary

Engineering invariants met. **Operator visual acceptance** of T1/T3 Telegram cards remains the human gate before declaring full acceptance complete.
