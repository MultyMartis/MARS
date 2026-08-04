# LIVE FOUR-RECIPIENT NO-DUPLICATE ACCEPTANCE v1

## A — Affected-lead dry run (internal, no-send)

| Check | Result |
|---|---|
| Stable lead recognized | PASS |
| Four recipients already delivered | PASS |
| sends attempted | **0** |
| Gmail finalized/excluded | PASS |

## B — Post-activate natural poll monitor (no new Gmail test)

Per Task K: **no new Gmail test immediately after activation.**

Monitored ≥3 poll intervals after Operational.dev reactivation:

| Exec | Time (UTC) | Sends | Last node |
|---|---|---:|---|
| 20654 | 13:24:30 | 0 | Apply Runtime State CONFIG |
| 20655 | 13:25:00 | 0 | Apply Runtime State CONFIG |
| 20656 | 13:25:30 | 0 | Apply Runtime State CONFIG |
| 20657 | 13:26:00 | 0 | Apply Runtime State CONFIG |

**total_telegram_sends = 0** — PASS (loop stopped for reconciled lead / empty intake).

## C — Dedicated new synthetic fixture

**PENDING operator** — requires unique synthetic lead + confirmation that Андрей / Оля / Мопс / Никита each receive **exactly one** new card, then ≥3 polls with zero additional cards.

## D — Operator live confirmation (Task M)

| Recipient | Exactly one **new** card after next synthetic | Status |
|---|---|---|
| Андрей | — | PENDING |
| Оля | — | PENDING |
| Мопс | — | PENDING |
| Никита | — | PENDING |

Do not sync-test buttons until Task M confirms card counts.
