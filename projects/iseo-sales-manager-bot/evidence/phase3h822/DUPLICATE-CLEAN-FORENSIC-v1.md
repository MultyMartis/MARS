# DUPLICATE CLEAN FORENSIC v1

**Captured:** live read-only proof 2026-08-14 ~13:12 Europe/Moscow  
**No PII** — aliases only.

## Heavy duplicate business leads (from 3H.8.2.1 + live re-proof)

| Alias | CLEAN rows | Statuses across rows | Old first-row selected | Authoritative resolved | Selected = current? |
|---|---|---|---|---|---|
| `LEAD_C3EF8E536C35` | 16 | pending only | pending | pending (`LEADS_CURRENT`) | YES (all copies pending) |
| `LEAD_F4C9D9693444` | 6 | new→pending | pending | pending (`LEADS_CURRENT`) | YES (unanimous pending) |

Additional live observation: `LEAD_FC4257C930FD` appeared with 24 `new/` rows (testish / non-eligible after filters) — duplicate source remains out of scope.

## Why first-row can become wrong

Even when today's snapshot is unanimous pending, if one historical pending copy remains while a later row is `spam`/`processed`, old selector keeps the pending copy (terminal rows never enter the map). New selector uses latest authoritative timestamp across **all** statuses → terminal wins.

## Effect after selector repair

Duplication no longer inflates `pending_count` and cannot keep a stale pending over a later terminal status. Duplicate CLEAN **source** is deferred (`KNOWN FOLLOW-UP — CLEAN DUPLICATE ROW PRODUCTION SOURCE FORENSIC`). No delete / compaction.
