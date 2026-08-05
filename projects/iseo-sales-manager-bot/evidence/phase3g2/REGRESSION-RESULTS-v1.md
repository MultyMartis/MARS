# Regression results — Phase 3G.2

**Phase:** 3G.2  
**Status:** FILLED  
**Sanitized labels only:** ADMIN_A · MOD_A · MOD_B_REVOKED · MOD_C_REVOKED  
**Forbidden in this file:** Telegram IDs, workbook IDs, secrets, emails, phones.

## Prior baselines retained

| Baseline | Status |
|----------|--------|
| Phase 3G.1 harness 100/100 | retained (historical) |
| Phase 3G.1.1 fail-closed band 9/9 | retained (historical) |
| Exactly-once delivery / LEAD_DELIVERIES | unchanged by this phase |
| Parser 3.3 / first-contact templates | unchanged |
| OpenRouter disabled | unchanged |
| Sales-Manager-v2 inactive | unchanged |
| Sole Gmail intake (`Gmail Fetch Leads`) | preserved |
| Stats epoch 05.08.2026 | preserved |
| Reminders OFF | preserved |
| AI OFF | preserved |

## 3G.2 deltas (additive only)

- Immutable `reply_profile_number` seed 1–4
- Number-based Admin profile commands
- Explicit role-aware help/start/AI/stats/config/reminder/unknown text refresh
- PROFILE_EVENTS tab + Append PROFILE_EVENTS node (Admin 84→85)
- Prepare Access Upsert flattens reply fields
- Offline harness band **42/42 PASS**

## Non-regressions confirmed

| Counter | Value |
|---------|------:|
| workflows created | 0 |
| access roles changed by name commands | 0 |
| historical reply snapshots modified | 0 |
| renumbered existing profiles | 0 |
| duplicate profile numbers | 0 |

## Result

- [x] Regression posture documented; no production contour breakage claimed beyond additive Admin node
