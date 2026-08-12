# Watchdog Command Validation (Redacted)

## Expected / accepted redacted shape

```text
wget -q -O - "https://bzpm.ru/mars-tools/cron/mars_1c_watchdog_http_gateway.php?token=***" >> /home/a/assum/bzpm.ru/storage/mars-tools/cron/logs/beget_watchdog_stdout.log 2>&1
```

## Checks

| Check | Result |
|------|--------|
| HTTPS host `bzpm.ru` | expected / accepted |
| Gateway path `mars_1c_watchdog_http_gateway.php` | expected / gateway file exists on server |
| `token=` parameter present | yes (redacted; never printed/committed) |
| stdout log destination under cron logs | expected `beget_watchdog_stdout.log` |
| Shell syntax | no corruption indicators in accepted shape |
| Gateway file present | YES (`GATEWAY` hash captured in PRESTATE) |

## Security

Token not printed. Token not committed. Screenshots must remain operator-side or redacted.

Gate: `D6G1B_WATCHDOG_COMMAND_VALIDATED_REDACTED`
