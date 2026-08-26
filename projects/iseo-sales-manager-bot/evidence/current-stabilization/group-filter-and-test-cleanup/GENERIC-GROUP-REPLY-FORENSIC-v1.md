# GENERIC-GROUP-REPLY-FORENSIC-v1

## Symptom

Operator-visible Telegram replies containing only: `Группа`.

## Cause (proven)

Not a separate Telegram template. Pipeline defect:

1. HCA `group_open` sets `answer_text = 'Группа'`, full text in `reply_text`, `skip_card_edits = true`.
2. Aggregate Card Sync Result, for non-raw outcomes with `skip_card_edits`, assigned `reply_text = answer_text`.

## Classification

`FALLBACK_TO_GENERIC_GROUP` / wrong field reuse between answer vs reply.

## Repair

`DIGEST_GROUP_PRESERVE_REPLY`: for `group_opened` / queue / full_card outcomes, preserve existing `reply_text`.

## Post-fix

ADMIN_A acceptance `2026-08-26T10-00-11Z`: `generic_gruppa_replies = 0`.
