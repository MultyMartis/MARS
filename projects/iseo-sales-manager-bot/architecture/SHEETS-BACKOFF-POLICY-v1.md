# SHEETS BACKOFF POLICY v1

**Phase:** 3E.2.3  
**Status:** DEPLOYED; happy-path live proof PASS; exhaustion behavior covered offline.

## Policy

Критичные Sheets nodes используют bounded retry: до 3 attempts с интервалом 30 seconds.

| Node class | Retry | Error boundary |
|---|---:|---|
| Read LEAD_DELIVERIES | 3 × 30s | fail closed, 0 sends |
| Read ACCESS_CONTROL | 3 × 30s | fail closed, 0 cards; no `continueOnFail` |
| Upsert Claim | 3 × 30s | fail closed for recipient; no `continueOnFail` |

## Ограничения

- Retry ограничен; бесконечный цикл запрещён.
- Backoff не должен умножаться на CONFIG fan-out.
- `alwaysOutputData` на bounded ledger read различает подтверждённое отсутствие строки и техническую ошибку.
- Post-send Sheets failure не запускает resend; результат — `reconciliation_required`.
- Audit-only writes могут иметь отдельную non-blocking policy только там, где это уже явно разрешено fail-closed contract.

## Безопасность

Quota recovery не является разрешением обходить ledger/access/claim. При исчерпании attempts путь останавливается на соответствующей границе.
