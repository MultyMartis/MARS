<!-- Phase 3H.7.3 operator resurface production-parity repair 2026-08-10 -->
## Phase 3H.7.3 (current)

| Field | Value |
|-------|-------|
| **Phase** | 3H.7.3 — Operator resurface production-parity, contact error fix, multi-card sync hardening |
| **Verdict** | `COMPLETE — RESURFACE PARITY REPAIRED; OPERATOR ACCEPTANCE PENDING` |
| **Repairs** | Canonical renderer for resurface · formula-error contact filter · authoritative card registry · semantic ack ≠ sync warning |
| **Acceptance leads** | REAL_REOPEN_A/B/C pending · 12 parity cards · no new LEADS rows |
| **Runtime** | Ops **45** active · Admin **87** active · v2 inactive · AI **OFF** · reminders recipients=4 |
| **Soak** | 3H.7.2 interrupted · Fresh T+0 **2026-08-10 12:44 Europe/Moscow** · earliest T+48 **2026-08-12 12:44 Europe/Moscow** |
| **Evidence** | [evidence/phase3h73/](evidence/phase3h73/) |
| **Report** | [REPORT-iseo-sales-manager-bot-phase3h73-resurface-production-parity-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3h73-resurface-production-parity-v1.md) |
| **Gate** | Phase 3I.1 blocked until soak PASS + operator acceptance |

# CALLBACK ACKNOWLEDGEMENT CONTRACT — iseo-lead-callback-ack-v1.0

One recognized callback → one route → ≤1 transition → exactly one user-visible acknowledgement.

## Required texts
- pending→processed: Лид отмечен как обработанный.
- pending→spam: Лид отмечен как спам.
- processed|spam→pending: Лид возвращён в обработку.
- already pending reopen: Заявка уже находится в обработке.
- already processed: Заявка уже отмечена как обработанная.
- already spam: Заявка уже отмечена как спам.
- not found: Заявка не найдена в рабочем реестре. Обратитесь к администратору.

## Hard rules
- No fallthrough after unknown_lead
- Aggregate Card Sync Result must not overwrite semantic ack with processed default
- acknowledgements=1 per execution


## Phase 3H.7.3 sync separation
Semantic acknowledgement is independent of card-sync result.
Do **not** replace spam/processed/reopen ack with «Статус сохранён. Не все копии карточки удалось обновить.» merely because a superseded historical message cannot be edited.
Current authoritative sync failures may be recorded separately (card_sync_warning).
