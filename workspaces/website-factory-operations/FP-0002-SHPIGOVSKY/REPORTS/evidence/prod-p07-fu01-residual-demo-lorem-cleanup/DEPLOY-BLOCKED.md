# PROD-P07-FU01 — Deploy blocked

```text
STOP — BEGET SSH/FTP PROTOCOL BANNER TIMEOUT
HTTP + WPilot ping remain 200
```

| Probe | Result |
|-------|--------|
| `GET http://shpigovsky.beget.tech/uslugi/` | 200 |
| `GET /wp-json/wpilot/v1/ping` | 200, `write_enabled=false` |
| TCP `91.106.207.76:22` connect | succeeds |
| SSH banner recv | **TimeoutError** (repeated, including after 3-minute cooldown, IPv4-forced) |
| FTP `:21` banner recv | **TimeoutError** |
| `ssh.beget.com:22` | same banner timeout |

P07 exact-file deploy via the same SSH path **succeeded** earlier today (`deploy-manifest.json` ~09:50 UTC). This continuation cannot complete Layer B download or upload until Beget SSH/FTP speaks again.

No further port-scan retries. Next deploy attempt should be **one** SSH or FTP session to the known host/port only.
