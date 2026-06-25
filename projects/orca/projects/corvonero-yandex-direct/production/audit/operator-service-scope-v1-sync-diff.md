# operator-service-scope-v1.json — Authority Sync Diff

**Generated:** 2026-06-22  
**Scope:** Six stale HOLD records synchronized to v7 production truth

---

## Summary

| Metric | Value |
|--------|------:|
| Services updated | 6 |
| Production dataset changes | 0 |
| Group ownership changes | 0 |
| Landing mapping changes | 0 |
| Protected seed changes | 0 |

---

## Per-service changes

### SVC-04 — внедрение 1С (CORV-G01-04)

| Field | Before | After |
|-------|--------|-------|
| current_group_status | HOLD — NO VALID COMMERCIAL DEMAND | ACTIVE NARROW |
| recovery_required | true | false |

### SVC-06 — обслуживание 1С (CORV-G01-06)

| Field | Before | After |
|-------|--------|-------|
| current_group_status | HOLD — NO VALID COMMERCIAL DEMAND | ACTIVE |
| recovery_required | true | false |

### SVC-20 — расчёт себестоимости (CORV-G04-01)

| Field | Before | After |
|-------|--------|-------|
| current_group_status | HOLD — NO VALID COMMERCIAL DEMAND | ACTIVE NARROW |
| recovery_required | true | false |

### SVC-21 — планирование закупок (CORV-G04-02)

| Field | Before | After |
|-------|--------|-------|
| current_group_status | HOLD — NO VALID COMMERCIAL DEMAND | ACTIVE NARROW |
| recovery_required | true | false |

### SVC-22 — платёжный календарь (CORV-G04-03)

| Field | Before | After |
|-------|--------|-------|
| current_group_status | HOLD — NO VALID COMMERCIAL DEMAND | ACTIVE NARROW |
| recovery_required | true | false |

### SVC-28 — перенос данных / миграция (CORV-G05-06)

| Field | Before | After |
|-------|--------|-------|
| current_group_status | HOLD — NO VALID COMMERCIAL DEMAND | ACTIVE NARROW |
| recovery_required | true | false |

---

## Unchanged (explicit)

- Service names and IDs
- `advertising_status` (MUST REPRESENT IN CAMPAIGN)
- Group ownership (`current_group`)
- Landing IDs
- All v7 keywords, ads, negatives, bids, URLs
- Campaign count and architecture
