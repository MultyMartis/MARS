# Patch notes (Admin.dev) — sanitized excerpts

Workflow: `wLrLp4WQHm1VJmxz` · stamp `2026-08-26T09-48-02-505Z` · `sha16_nodes=62CB6CEC5ED92C86`

## 1. Aggregate Card Sync Result — DIGEST_GROUP_PRESERVE_REPLY

When `skip_card_edits` and outcome is `group_opened` / queue / full_card: **do not** assign `reply_text = answer_text` (prevents literal `Группа`).

## 2. Handle Callback Action — AUTHORITATIVE_GROUP_PENDING

In `group_open`: exclude archive + `isTestRow`; unique by `bkey`; `pickLatestRow` — aligned with reminder current-state selector.

## 3. Handle Callback Action — readOnlyAmbiguous

For `queue_open` / `full_card` / `raw_source`: on duplicate matches, pick latest. Mutate actions (`processed` / `spam` / `reopen`) remain fail-closed.

Full private POST dumps live under wave `backups\` / `patches\` (not Git).
