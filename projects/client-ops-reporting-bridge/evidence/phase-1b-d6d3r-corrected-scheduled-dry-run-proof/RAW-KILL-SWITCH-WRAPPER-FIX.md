# RAW Kill-Switch Wrapper Fix

## Bug (D6D3)

```text
wrapper: ks = parseKillSwitch(raw)   // returns {ok, mode, reason, permits_*} — NO site_id
producer: parseKillSwitch(ks)        // looks for site_id → KILL_SWITCH_SITE_MISMATCH
```

## Correction (runtime-state, non-Git)

```text
wrapper: validate via parseKillSwitchStrict(raw)
wrapper: killSwitchRaw = JSON.parse(readFileSync(kill-switch.json))  // RAW shape WITH site_id
producer: kill_switch: killSwitchRaw
```

## Contract comparison (sanitized)

| Field | Former (bug) | Corrected |
|-------|--------------|-----------|
| Passed to producer | parsed `{ok,mode,reason,permits_*}` | raw `{schema_version,site_id,producer_identity,mode,...}` |
| `site_id` on object | absent | `SITE-002` |
| Producer re-parse | SITE_MISMATCH | DRY_RUN accepted |

Token: `D6D3R_RAW_KILL_SWITCH_WRAPPER_FIX_RECONFIRMED`

Phase tags in wrapper updated to `1B-D6D3R` for receipt distinguishability (contract shape unchanged).
