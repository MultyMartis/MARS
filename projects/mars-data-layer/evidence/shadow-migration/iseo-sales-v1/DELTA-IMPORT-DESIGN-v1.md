# Delta-import design (pre-cutover) — ISEO Sales shadow

## Goal

Support:
`initial import` → `incremental reconciliation` → `final delta at cutover`
without relying on Sheet row numbers.

## Snapshot / cutoff

Every import records:

- `snapshot_id` / `cutoff_utc`
- Spreadsheet IDs + tab inventories
- Collapsed identity sets (`gmail_message_id`, `lead_id`)

Live Sheets growth after T0 is **not** a migration failure.

## Primary keys for delta

| Domain | Delta key | Detect change via |
|---|---|---|
| inbound | `(source_system, source_id)` = gmail message id | presence in PG; new RAW ids after cutoff |
| leads | `lead_id` | `updated_at` / status / assigned_to vs shadow |
| events | deterministic `event_id` (sheet-derived hash) | new LEAD_EVENTS rows with new hashes |
| deliveries | `delivery_key` / synthesized `delivery_id` | new delivery_key values |
| access | `principal_key` = `tg:{telegram_user_id}` | status/role fields |
| config | `key` | value hash |
| dedup | `dedup_key` | re-synth from current lead set |

## Algorithm (safe)

1. Re-read Sheets RO at Tn.
2. Build transform set (same tool, dry-run).
3. Classify each identity:
   - `UNCHANGED`
   - `NEW`
   - `UPDATED`
   - `REMOVED_FROM_ACTIVE` (do not auto-delete PG without operator charter)
4. Apply only NEW/UPDATED upserts in APPLY mode.
5. Emit reconcile matrix vs Sheets Tn and vs previous shadow.

## Cutover final delta

Immediately before SoT switch (future wave):

1. Freeze Sheets writers OR accept short dual-write window (operator decision).
2. Run APPLY delta with fresh cutoff.
3. Prove reconcile residuals = 0 for active business domains.
4. Only then candidate workflow may read PG.

## Non-goals (this wave)

- No bidirectional sync
- No PG → Sheets
- No Operational.v3.dev
