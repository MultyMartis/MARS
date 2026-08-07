# Watchdog Scheduling Forensic

## Contour

- Authoritative scheduler for SITE-002 1C import: **Beget panel/API cron** (not SSH `crontab`)
- SSH `crontab`: **unavailable** (`command not found`) — proven again in D6G1A
- Import schedule evidence: daily `0 8 * * *` Europe/Moscow (real run `mars-20260807-080002-5bbdaf1c`)
- Preferred watchdog schedule: `0 9 * * *` Europe/Moscow ≈ 13:00 +07 (1h after import start; margin after ~seconds–minutes import duration)

## Cursor update path

- Beget API `cron/getList` + `cron/add` is the safe automation path **when credentials authenticate**
- D6G1A probe result: **AUTH_ERROR** (`Username/password incorrect`) for all stored Hosting Panel / SSH / derived login combinations
- Conclusion: Cursor **cannot currently** mutate Beget cron with secrets on disk; operator panel action (or refreshed API password) required

## Duplicate check

- API list unavailable due AUTH_ERROR → cannot prove absence/presence via API
- No watchdog lines found in `beget_cron_stdout.log` grep
- Watchdog HTTP gateway + PHP present on server (D6G1 deploy)

## Required operator cron (redacted)

```
0 9 * * *
wget -q -O - "https://bzpm.ru/mars-tools/cron/mars_1c_watchdog_http_gateway.php?token=<run_token>" >> /home/a/assum/bzpm.ru/storage/mars-tools/cron/logs/beget_watchdog_stdout.log 2>&1
```

Token: from non-Git `mars_1c_wrapper.local.php` `run_token` (not in evidence).

Captured: 2026-08-07T09:39:42+00:00
