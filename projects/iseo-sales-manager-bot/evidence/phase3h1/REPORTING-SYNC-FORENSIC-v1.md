# Reporting sync forensic

## Architecture found

- Backend SoT: workbook tabs `LEADS` / events / deliveries (private)
- Human reporting workbook «i-SEO — Учёт лидов и статистика» exists and contains CLIENT_A
- **No active Operational.dev or Admin.dev nodes** write to the reporting workbook on the live contour
- CONFIG key `reporting_sync_enabled` was **ABSENT** before Phase 3H.1
- `/config` honestly showed «выключена» because of absent key + comment «no active reporting sync nodes»

## Classification

**4. MANUAL** — workbook exists; population from Phase 3F.2 controlled migration / manual refresh; **not** continuous event-driven or scheduled sync.

## Failure / retries

Not applicable for continuous sync (none active). Backend intake/delivery must not block on reporting (unchanged contract).
