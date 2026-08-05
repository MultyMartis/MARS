# MOD_A self-profile acceptance

**Phase:** 3G.2.2
**Status:** FILLED — engineering proof PASS; operator live acceptance PENDING
**Sanitized labels only:** MOD_A
**Forbidden in this file:** Telegram IDs, chat IDs, usernames, workbook IDs, URLs, raw updates, secrets.

## 1. Acceptance criteria

| # | Criterion | Result |
|---|-----------|--------|
| 1 | `/my_reply_profile` as MOD_A shows client name «Михаил» (never «Мопс») | PASS (offline: harness check #20) |
| 2 | `/my_reply_profile` as MOD_A shows «Персональный ответ: включён» | PASS (harness check #20) |
| 3 | `/my_reply_profile` as MOD_A shows role «Модератор» | PASS (harness check #20) |
| 4 | Moderator `/start` reply-name line shows «Михаил», not blank | PASS (offline resolution — harness check #21) |
| 5 | Same resolver version reported for MOD_A as for ADMIN_A | PASS (harness check #22) |
| 6 | No blank profile after auto-rehydrate on a wiped row | PASS (harness check #24) |
| 7 | No false-disabled state after rehydrate for an active profile | PASS (harness check #25) |
| 8 | Client-copy draft never contains «Мопс» | PASS (harness check #50) |

## 2. Restore trigger commands (same pattern as ADMIN_A)

`/my_reply_profile`, `/reply_profiles`, `/reply_profile 3` (Admin-issued), or moderator `/start` — any of these run against MOD_A's row exercise the rehydrate check before formatting output.

## 3. Operator live acceptance packet (pending)

As MOD_A, send in order:

1. `/start` — confirm reply-name line shows «Михаил», not blank.
2. `/my_reply_profile` — confirm name «Михаил», «Персональный ответ: включён», role «Модератор».
3. Confirm no «Мопс» anywhere in the reply text.

## 4. Status

Engineering proof is complete offline against the exact wiped-row shape captured in the forensic. Live Telegram confirmation from the operator as MOD_A remains **PENDING** — the agent cannot inject a live Telegram update (webhook secret required; see `ADMIN-A-RESTORE-v1.md` §4).

## Result

- [x] Offline acceptance criteria 1–8 PASS
- [ ] Operator live Telegram acceptance (PENDING)
