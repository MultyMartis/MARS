# GROUP-ROOT-CAUSE-v1

## Primary root cause

`AUTHORITATIVE_SELECTOR_DIVERGENCE`

| Path | Selector behavior (pre-patch) |
|------|-------------------------------|
| Reminder digest | authoritative: no tests, no archive, unique `bkey` |
| `group_open` | pending-only over full CLEAN; **no** `isTest`; **no** unique-by-bkey |

Category token filtering worked (Audit vs SEO returned different titles), so this is **not** collapsed callbacks. Counts inflated because synthetic fixtures + CLEAN duplicates remained pending and were included in group views.

## Secondary root cause

`FALLBACK_TO_GENERIC_GROUP`

`Handle Callback Action` set `answer_text: 'Группа'` with `reply_text` = full body and `skip_card_edits: true`.  
`Aggregate Card Sync Result` on `skip_card_edits` overwrote `reply_text` with `answer_text` → operator saw literal **Группа**.

## Tertiary (verify error)

Exec `40889` / `sm:q:e64921b60ff5`: `callback_outcome: ambiguous` / `ambiguous_duplicate` on synthetic lead `lead_synth_p3b1_c01` (many CLEAN copies). Fail-closed message: `Не удалось проверить заявку…`.

## Repair (Admin.dev `wLrLp4WQHm1VJmxz`)

1. `AUTHORITATIVE_GROUP_PENDING` in `group_open` (align with reminder selector).
2. `DIGEST_GROUP_PRESERVE_REPLY` in Aggregate (preserve group body).
3. `readOnlyAmbiguous`: queue/full_card/raw_source pick-latest; mutate actions still fail-closed.

Proof stamp: `2026-08-26T09-48-02-505Z`, `sha16_nodes: 62CB6CEC5ED92C86`, markers all true, node_count 111.
