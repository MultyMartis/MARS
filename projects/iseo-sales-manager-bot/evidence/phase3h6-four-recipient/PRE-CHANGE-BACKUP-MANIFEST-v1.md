# PRE-CHANGE BACKUP MANIFEST — Phase 3H.6

**Timestamp UTC:** 2026-08-06T17:19:16.056Z

## Workflows

| Workflow | ID | active | nodes | sha256(raw private) |
|---|---|---|---:|---|
| Operational.dev | xSnXPy8cEHoZw6xG | true | 45 | `5b3167db1b70520cc6956386e91c9083f2037a8be25ea19e193fac027114594b` |
| Admin.dev | wLrLp4WQHm1VJmxz | true | 85 | `81a3163dc91b07d77fdfe8bb732d82e062d461c01bd9b794d02e5fd30f553a34` |
| Sales-Manager-v2 | h8I2Tl2yl4uzhUnB | false | 19 | `336814ea96a33c6ae92c8eca38eb3e54f6ea681d68598d2996c0c6ce624c1cf0` |

## Sheets snapshot (sanitized)

- ACCESS_CONTROL active staff: 4 (Андрей, Оля, Михаил, Никита)
- CONFIG `pending_reminder_active_recipients_count`: 3
- LEADS count: 1 · pending: 0

## Storage (outside Git)

`X:\AI MARS STORAGE\git-sync-iseo-sm-phase3h6-four-recipient-20260807-001611\runtime\backups\pre-change\`

Raw exports, Telegram IDs, workbook IDs, and credentials are **not** committed.

## Rollback

1. Deactivate Ops + Admin  
2. PUT pre-change raw exports to same workflow IDs  
3. Re-activate  
4. Never force-push
