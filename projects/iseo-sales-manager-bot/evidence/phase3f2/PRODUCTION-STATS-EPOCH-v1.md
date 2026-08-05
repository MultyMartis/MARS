# PRODUCTION STATS EPOCH v1 — Phase 3F.2

## Epoch definition

| Field | Value |
|---|---|
| Display date | **05.08.2026** |
| Exact epoch (UTC) | `2026-08-05T13:02:57.000Z` (Клиент A Gmail `internalDate`) |
| Business time | 05.08.2026 16:02:57 Europe/Moscow |
| Reason | `operator_clean_baseline` |
| Generation | `v2` |
| Legacy mode | `archive_excluded` |
| Test policy | `real-only-v1` |

## Live CONFIG

Keys written into operational CONFIG (HTTP rewrite, Phase 3F.2):

- `production_stats_epoch`
- `production_stats_epoch_timezone=Europe/Moscow`
- `production_stats_epoch_reason`
- `production_stats_epoch_lead_ref` (safe ref only; not printed here)
- `production_data_generation=v2`
- `legacy_data_mode=archive_excluded`
- `production_test_policy_version=real-only-v1`
- `pending_reminders_enabled=false` (forced)

## Status

| Item | Status |
|---|---|
| Epoch definition | **PASS** |
| CONFIG keys live | **PASS** |
| Reporting `Справка` / `Статистика` seeded with epoch | **PASS** |
| Operator visual acceptance of stats view | **PENDING OPERATOR** |

*Related: [EVGENIY-LEAD-FORENSIC-v1.md](EVGENIY-LEAD-FORENSIC-v1.md), [REPORTING-WORKBOOK-CREATION-v1.md](REPORTING-WORKBOOK-CREATION-v1.md).*
