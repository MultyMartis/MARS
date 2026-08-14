# OLD FIRST-ROW SELECTOR v1

**Classification:** `CURRENT_SELECTOR_FIRST_ROW_DEPENDENT = YES`

## Live pre-patch Reminder Build Claims (Admin.dev)

Input dataset: `$('Read CLEAN for Reminder')` → `lead_clean_v2` `A1:ZZ500`  
Plus ACCESS_CONTROL + REMINDER_DELIVERIES (recipients/claims only).

### Filtering order

1. Skip if `life(r) !== 'pending'` (`manager_status`/`lifecycle_status` terminal → exclude row).
2. Skip probable tests unless `include_tests`.
3. Require business key (`stable_lead_ref` / `lead_id` / `source_message_id`).
4. Dedupe: **first array occurrence wins** — `if (!best.has(key)) best.set(key, r)`.
5. `pending_count = best.size`.

### Row-order dependence

**YES.** Later CLEAN rows for the same `lead_id` are ignored once the first pending row is stored.

### Status source

Only the **first pending CLEAN row** for the key. Terminal CLEAN rows never enter `best`, so a later spam/processed copy on the same key cannot override an earlier pending copy.

### Later rows ignored

**YES** — after first key insert.

### Archive

CONFIG `pending_reminder_include_archive` was displayed elsewhere; old Build Claims did not apply archive columns (often absent on CLEAN).

Code hash pre-patch: `30A8B93AA50EBBAF`.
