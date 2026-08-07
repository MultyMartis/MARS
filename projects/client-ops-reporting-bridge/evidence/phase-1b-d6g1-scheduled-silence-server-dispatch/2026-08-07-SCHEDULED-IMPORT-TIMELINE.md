# 2026-08-07 Scheduled Import Timeline

All times labeled explicitly.

| Step | Time | TZ | Evidence |
|------|------|----|----------|
| Expected Beget cron | 08:00 | Europe/Moscow | Accepted D6G: `0 8 * * *` |
| Equivalent local | 12:00 | Asia/Barnaul (+07) | Operator contour |
| Wrapper start | 2026-08-07T08:00:02+03:00 | Moscow (+03 server) | `mars_1c_import_20260807.log` |
| Catalog phase complete | 2026-08-07T08:00:07+03:00 | Moscow | same log |
| Offers phase complete | 2026-08-07T08:00:07+03:00 | Moscow | same log |
| Terminal written | 2026-08-07T08:00:07+03:00 | Moscow | `runs/mars-20260807-080002-5bbdaf1c/terminal.json` |
| Inbox queued | 2026-08-07T08:00:07+03:00 | Moscow | `dispatch-inbox/...json` status PENDING |
| Beget cron stdout JSON | ~08:00:07 | Moscow | `beget_cron_stdout.log` |
| Windows poller window | 11:50–14:50 | +07 | Task repetition PT2M / PT3H |
| Poller last result today | repeatedly `1` | +07 | FTP secrets parse failure |
| Local terminal mirror today | absent | +07 | only prior `mars-20260806-160514-5d2cdb3b` |
| Watchdog task last run | 2026-08-07T13:28:28+07:00 | +07 | `MARS_SITE_002_Client_Ops_Producer` |
| Watchdog local false skip | after fix proven | +07 | stale `_current` from 2026-08-06 |
| Operator incident note | 2026-08-07T15:17:00+07:00 | +07 | no Telegram |
| Server recovery dispatch | 2026-08-07T11:36:30+03:00 | Moscow | SENT / n8n `24966` |

## Run identity

- `run_id`: `mars-20260807-080002-5bbdaf1c`
- `trigger_source`: `SCHEDULED`
- `final_status`: `ATTENTION_OFFERS_INPUT_MISSING`
- `report_dispatch_status` after import: `QUEUED` (Windows path never completed)

## Classification of silence

Primary: Windows completion poller failed to fetch terminal (`COMPLETION_POLLER_FAILED` / `COMPLETION_POLLER_TERMINAL_NOT_VISIBLE`).

Contributing: watchdog false-skip on stale `_current` (`WATCHDOG_FALSE_SKIP`).

Latent: architecture depended on workstation for normal delivery.
