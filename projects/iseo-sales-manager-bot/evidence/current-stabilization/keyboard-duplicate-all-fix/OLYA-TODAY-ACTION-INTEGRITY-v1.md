# OLYA-TODAY-ACTION-INTEGRITY-v1

## Scope day

Production calendar day of repair (Europe/Moscow wall + UTC timestamps on 2026-08-27).

## Actor mapping

Handle Callback Action uses:

`u:` + `sha256hex('actor:' + telegramUserId).slice(0, 12)`

MOD_B / Olya maps to sanitized actor prefix `u:48ad…` (full map private, not committed).

## Identified Olya real lead actions today

`olya_today_count = 7` (all matched MOD_B actor; `unmatched_today = 0`).

Sanitized sample (no contacts):

| lead_hash | status (authoritative) | updated_at (UTC) | event_count_rows | actor |
|-----------|------------------------|------------------|------------------|-------|
| c0fe096e5df8 | spam | 2026-08-27T07:23:03.709Z | 5 | MOD_B |
| 08c4cf248f93 | spam | 2026-08-27T07:21:27.716Z | 5 | MOD_B |
| 783f242bc20f | spam | 2026-08-27T07:19:17.076Z | 5 | MOD_B |
| (+ 4 more) | … | … | … | MOD_B |

Full private list: worktree `private/forensic/olya-today-integrity.json`.

## Repair impact invariants

| Counter | Value |
|---------|------:|
| Olya real leads processed today identified | **7** |
| Olya real leads mutated by repair | **0** |
| Olya status regressions | **0** |
| duplicate Olya action events caused by repair | **0** |
| Olya processed leads lost | **0** |

## Method note

Keyboard repair changed Admin.dev Code/Telegram keyboard nodes only. CLEAN rows / LEAD_EVENT appends were not written by patch scripts. Integrity = re-read authoritative current status after deploy; no reopen/revert observed.
