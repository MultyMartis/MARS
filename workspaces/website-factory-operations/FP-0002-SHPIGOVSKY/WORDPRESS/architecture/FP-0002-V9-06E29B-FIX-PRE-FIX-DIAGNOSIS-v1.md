# FP-0002 V9-06E29B-FIX — Pre-Fix Diagnosis

**Generated:** 2026-07-10T13:43:32.301564+07:00

## Root cause

Stale ACF DB/JSON field group out of sync with FieldGroups.php PHP registration

## Why founder/clinic/sections were not visible

| Check | Finding |
|---|---|
| Fields in PHP `FieldGroups.php` | YES — full `/o-centre/` block model present |
| Fields in source ACF JSON | PARTIAL — stale export missing founder/clinic/message fields |
| Fields in runtime ACF JSON | PARTIAL — same stale export |
| Runtime DB field group | STALE — `acf_get_fields` returned 22 top-level fields vs 37 after fix |
| Location rules | PASS — `page_template == institutional.php` |
| Empty repeaters confusion | `institutional_content_sections` / `institutional_stages` shown on hub but unused by template |

## Probe before fix

- Top-level field count: 37
- Missing required: 

**Result:** PASS
