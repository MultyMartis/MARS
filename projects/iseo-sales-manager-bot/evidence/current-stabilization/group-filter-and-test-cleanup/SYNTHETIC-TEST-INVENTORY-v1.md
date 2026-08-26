# SYNTHETIC-TEST-INVENTORY-v1

## Scope

CLEAN sheet `lead_clean_v2` snapshot via reminder/callback reads (exec-backed). No mutation during inventory.

| Metric | Value |
|--------|------:|
| CLEAN rows | 155 |
| Unique lead_id | 112 |
| PROVEN_SYNTHETIC (row-level inventory) | 80 |
| PROVEN_TEST | 0 (rolled into PROVEN_SYNTHETIC when marker/`lead_synth_`/`msg_synth_` proven) |
| PRODUCTION_REAL | 62 |
| SAFE_UNKNOWN | 12–13 |
| Proven pending unique (pre-cleanup dry) | 49 |

## Surfaces

| Surface | Role |
|---------|------|
| CLEAN | authoritative current-state for reminder + group_open |
| RAW | not bulk-mutated this wave |
| LEAD_EVENTS | historical; fixtures archived via CLEAN status, events not mass-deleted |
| Reminder claims | not mutated |

## Notable pollution

- `lead_synth_p3b1_c01` — many CLEAN copies (≈24), drove ambiguous verify.
- Named fixtures with `SYNTHETIC_TEST` body provenance (e.g. C02 SEO).
- Probe IDs (`PROBE_phase3e22-…`).

Full sanitized row list: local forensic `SYNTHETIC-INVENTORY-FROM-EXEC.json` (not committed if oversized; summary + matrix in Git).
