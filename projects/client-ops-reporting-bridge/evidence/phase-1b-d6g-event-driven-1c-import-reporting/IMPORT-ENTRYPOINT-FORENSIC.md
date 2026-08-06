# Import Entrypoint Forensic

## Canonical entrypoint

- Beget cron: `0 8 * * *` Europe/Moscow (= 12:00 Barnaul UTC+07)
- Command: HTTP GET `https://bzpm.ru/mars-tools/cron/mars_1c_http_gateway.php?mode=run&token=...`
- Gateway → `/storage/mars-tools/cron/mars_1c_import_wrapper.php`
- Runner invokes Sergey legacy `index.php?route=common/cronjob` twice with DB `cron.active` for commands `1c` then `1c_offers`
- Lock: `/storage/mars-tools/cron/mars_1c_import.lock`
- Reports: `/storage/mars-tools/cron/reports/mars_1c_import_*.txt`
- Run ID format (retained): `mars-YYYYMMDD-HHMMSS-<8hex>`
- XML dir: `/1c_incoming/webdata` (`import0_*.xml`, `offers0_*.xml`)

## Prior reporting chain (timer-based)

1. Import ~12:00 Barnaul (Beget)
2. Monitor task `MARS_SITE_002_Post_1C_Catalog_Monitor` ~12:30
3. Producer task `MARS_SITE_002_Client_Ops_Producer` ~13:00 assumed import finished
4. n8n → Telegram

Defect: producer selected by clock, not by terminal import completion.
