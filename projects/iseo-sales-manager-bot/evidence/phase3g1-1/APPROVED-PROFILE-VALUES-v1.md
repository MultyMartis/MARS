# APPROVED PROFILE VALUES — Phase 3G.1.1

**Version:** `iseo-recipient-name-v1.0`  
**Company default:** `INTLSEO`  
**Columns:** ACCESS_CONTROL Q–V (live seeded)

## Active eligible profiles

| Label | Client-facing name | Enabled | Access | Recipient cards |
|-------|-------------------|---------|--------|-----------------|
| ADMIN_A | Андрей | true | active | yes |
| MOD_A | Михаил | true | active | yes |

## Prepared / revoked (disabled, ineligible)

| Label | Client-facing name | Enabled | Access | Recipient cards |
|-------|-------------------|---------|--------|-----------------|
| MOD_B_REVOKED | Оля | false | revoked | no |
| MOD_C_REVOKED | Никита | false | revoked | no |

## Seed method

- Headers created via Sheets API `values.update` on row 1 (columns Q–V).
- Values written via `values.batchUpdate` (24 cells total across four rows).
- Matching: **label-aware** row identification (not brittle short display_name exact match).
- MOD_A mapped from internal display token `Мопс` → client name **Михаил** (nickname never used in client copy).

## Invariants preserved

- No role changes
- No status changes (revoked remain revoked)
- No Telegram ID or workbook ID recorded in this artifact

## Contract fields per row

Each seeded row includes:

- `reply_sender_name`
- `reply_sender_enabled`
- `reply_company_name` = `INTLSEO`
- `reply_profile_version` = `iseo-recipient-name-v1.0`
- `reply_profile_updated_at` (ISO timestamp at seed)
- `reply_profile_updated_by` = operator repair label (sanitized)
