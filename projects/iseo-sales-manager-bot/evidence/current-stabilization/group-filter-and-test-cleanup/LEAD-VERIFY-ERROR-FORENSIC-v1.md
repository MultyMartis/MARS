# LEAD-VERIFY-ERROR-FORENSIC-v1

## Symptom

`Не удалось проверить заявку. Попробуйте ещё раз через минуту.`

## Execution

| Field | Value |
|-------|-------|
| Exec | **40889** |
| callback_data | `sm:q:e64921b60ff5` |
| Outcome | `ambiguous` / `ambiguous_duplicate` |
| Lead identity (sanitized) | `lead_synth_p3b1_c01` |

## Failure node

Lead match / resolve path inside Admin callback handling: multiple CLEAN rows for same lead identity → fail-closed.

## Relation to pollution

Proven: synthetic fixture with many duplicate CLEAN copies (inventory showed ×24 for `lead_synth_p3b1_c01`).

## Repair

1. Fixture cleanup archived proven pending rows (including duplicate copies by `row_number`).
2. `readOnlyAmbiguous`: for read-only opens (`queue_open` / `full_card` / `raw_source`), pick latest row instead of hard fail; **mutate** actions remain fail-closed.

## Post-fix

Proven artificial pending = 0. Acceptance opened SEO lead path without verification error in test send. Remaining real CLEAN duplicates deferred to dedicated forensic phase.
