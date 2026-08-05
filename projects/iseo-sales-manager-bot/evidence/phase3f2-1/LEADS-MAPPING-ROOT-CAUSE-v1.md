# /leads MAPPING ROOT CAUSE v1

## Path

`Route Command` → `Read CLEAN for Leads` (sheet **LEADS**) → `Recent Leads` → `Capture Admin Reply` → Telegram.

## Root cause (precise)

1. Phase 3F.2 injected `phase3f2LeadView()` helper but **never called it** from `normalizeLife` / `buildCard`.
2. `normalizeLife` read only `manager_status` (legacy CLEAN). Authoritative LEADS field is `lifecycle_status=processed` → empty manager_status defaulted to **pending**.
3. `buildCard` read `service` / `summary` instead of `resolved_service_label` / `client_comment` → **—**.
4. Received time, actor, source_display were not rendered.

Not a Sheets tab miss (tab already LEADS). Not positional `/`leads reading reporting workbook.
