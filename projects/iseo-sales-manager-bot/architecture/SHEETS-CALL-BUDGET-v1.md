# SHEETS CALL BUDGET v1

**Phase:** 3E.2.3  
**Status:** LIVE PROVEN; operator visual confirmation pending.

## Цель

Ограничить обращения к Google Sheets на один poll и одну доставку, не ослабляя fail-closed границы.

## Измеренный baseline BEFORE

- Пустой poll: 1 CONFIG write (`last_poll_success_at`) каждые 30 секунд, то есть примерно 120 writes/hour непрерывной фоновой нагрузки.
- Полный dual-recipient путь по executions 22254/22243: примерно 8 Sheets node runs до точки quota failure: RAW, CONFIG read, DEDUP read, CLEAN, DEDUP append, full LEAD_DELIVERIES read, ACCESS_CONTROL read, claim.
- Full-tab размеры наблюдения: CONFIG около 69 строк, DEDUP_INDEX около 100, LEAD_DELIVERIES около 52. Это forensic snapshot, не постоянная гарантия размера.
- Success path дополнительно записывал несколько CONFIG keys, включая дублирующие message-level и recipient-level guards.

## Target AFTER

| Операция | Budget на dual-recipient delivery |
|---|---:|
| CONFIG read | 1 |
| ACCESS_CONTROL read | 1 |
| LEAD_DELIVERIES bounded read | 1 |
| Claim writes | 2 |
| Delivered stamps | 2 |
| CONFIG fallback upserts | не более 4 |
| RAW append | 1 |
| CLEAN write | 1 |
| DEDUP read/append | без изменения текущего контракта |

Пустой poll AFTER возвращает `[]` из Runtime State и делает **0 Sheets writes**. Final schedule: `minutesInterval=2`; n8n rejected `secondsInterval=120` as `Invalid interval`.

## Инварианты

1. Budget не даёт права пропускать ACCESS_CONTROL, claim или delivery ledger.
2. Ошибка ACCESS_CONTROL или claim означает 0 Telegram cards.
3. Post-send persistence failure переводит запись в `reconciliation_required`; blind resend запрещён.
4. Один recipient guard: `tg_delivered:<stable_lead_ref>:<recipient_ref>`.
5. Budget подтверждён offline harness 83/83 и live proof: CONFIG=1, ACCESS_CONTROL=1, bounded ledger items=1, claims=2, sends=2, stamps=2.

## Acceptance

Final exactly-once proof PASS: один delivery cycle, две разрешённые доставки и ноль повторов на пяти последующих polls. CONFIG guards=2 reconciled without resend. Operator visual confirmation remains pending.
