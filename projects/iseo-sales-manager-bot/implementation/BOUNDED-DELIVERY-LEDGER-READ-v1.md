# BOUNDED DELIVERY LEDGER READ v1

**Phase:** 3E.2.3  
**Target:** `Read LEAD_DELIVERIES`.

## Query contract

- Filter key: exact `stable_lead_ref` текущего lead.
- Full-tab read запрещён для delivery gate.
- `alwaysOutputData=true` обязателен, чтобы empty result был явным успешным состоянием.
- Retry: максимум 3 attempts, delay 30 seconds.
- Snapshot переиспользуется downstream; дополнительный ledger read для recipient expansion запрещён.

## Result classification

| Result | Action |
|---|---|
| matching delivered row | skip recipient |
| matching claimed/uncertain row | `reconciliation_required`, no resend |
| confirmed empty | разрешить claim path |
| read error / quota / poisoned output | 0 sends |

## Fallback

Expand переиспользует snapshot `Read CONFIG`; дополнительный Sheets call для `tg_delivered:*` fallback не выполняется. Normalize CONFIG обязан пропускать `tg_delivered:*` и `tg_attempts:*` keys.

## Proof status

Patch contract deployed while workflow inactive. Query selectivity and call count require final live execution evidence.
