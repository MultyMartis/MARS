# SHEETS COLUMN MAPPING REFRESH v1

## Result

**PASS.** Schema/value mappings were refreshed for the active Phase 3B.2 sandbox contour.

## Mapping scope

| Store | Mapping state |
|---|---|
| RAW | 29 columns refreshed |
| CLEAN | 52 columns refreshed |
| DEDUP | refreshed |
| EVENTS | refreshed |
| ERRORS | refreshed |
| CONFIG | refreshed |

Native append nodes are enabled in the `.dev` graph. Historical tabs remain untouched.

## CONFIG binding

`environment=dev`, `ai_enabled=false`, and `health_ai_probe_enabled=false` are bound. Telegram destinations and `admin_user_ids` are configured only in the external sandbox state; no raw identifiers appear here.
