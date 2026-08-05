# LIVE PROFILE SEED DEFECT — Phase 3G.1.1

**Date:** 2026-08-06  
**Classification:** sanitized evidence — no PII, no Telegram IDs, no workbook IDs

## Summary

Phase 3G.1 Sheets sidecar reported **ok** but did **not** create the ACCESS_CONTROL reply-profile columns required by `iseo-recipient-name-v1.0`.

## Observed defect

| Symptom | Detail |
|---------|--------|
| Admin `/reply_profiles` | All profile fields showed `—`; personalization appeared **OFF** for every row |
| Admin Upsert ACCESS_CONTROL | Value mappings for profile fields already existed in workflow schema |
| Live sheet headers | Six required columns **missing** entirely |
| n8n appendOrUpdate | Failed with `Column names were updated after the node's setup` when schema lagged live headers |

## Missing headers (ACCESS_CONTROL)

All six additive profile columns were absent from the live sheet:

1. `reply_sender_name`
2. `reply_sender_enabled`
3. `reply_company_name`
4. `reply_profile_version`
5. `reply_profile_updated_at`
6. `reply_profile_updated_by`

## Seed matching mismatch (secondary)

Initial seed logic used **short display_name exact match** (`Андрей` / `Оля` / `Никита` / exact `Мопс` for MOD_A).

Live ACCESS_CONTROL rows use multi-token or username-shaped display labels:

| Label | Live display shape | Seed match result |
|-------|-------------------|-------------------|
| ADMIN_A | 2-token display | Would match `Андрей` only if columns existed |
| MOD_A | exact `Мопс` token | Would match only if columns existed |
| MOD_B_REVOKED | username-shaped | No match to `Оля` |
| MOD_C_REVOKED | 2-token display | No match to `Никита` |

## Impact

- Personalization pipeline could not read or persist approved sender names.
- Live Telegram cards from exploratory inject batches rendered **empty client copy** (test_suppressed / missing profile path).
- Admin profile commands returned empty or dash values despite Phase 3G.1 workflow patch being active.

## Status

**Closed** in Phase 3G.1.1 repair wave. See `PROFILE-SEED-ROOT-CAUSE-v1.md` and `APPROVED-PROFILE-VALUES-v1.md`.
