# Migration / backfill plan (dry-run only)

All SQL in this folder is marked DRY RUN ONLY — DO NOT APPLY.

## Steps (future apply)

1. Backup DB (full + exact tables).
2. Create mapping table (`dry-run-schema.sql`).
3. Backfill known GUIDs (`dry-run-backfill.sql`) after HITL review of hub-vs-leaf targets.
4. Deploy importer change using mapping table first.
5. Dry-run / controlled import.
6. Only later: create missing tech leaves and remappoint leaf GUIDs from hubs to leaves.

## Collision guard list

Do not leaf-name-match into: 154 (Мясорубки legacy), 159 (Пилы для мяса legacy), 165 (Хлеборезки legacy)
when 1C parent chain is under tech root GUID `e0fd5c42-a3b8-11ea-8152-a85e4515c4f4`.
