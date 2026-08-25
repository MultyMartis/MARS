# SITE-002 — Recovery Guide

For each scenario: DETECTION → SAFE ACTION → DATA LOSS RISK → RECOVERY → VALIDATION → ESCALATION

## Import wrapper failure
- **DETECTION:** cron fails; no new terminal
- **SAFE ACTION:** do not enable Windows poller
- **DATA LOSS RISK:** missed import cycle
- **RECOVERY:** restore known-good wrapper; fix PHP errors; re-run under charter
- **VALIDATION:** scheduled or admin run writes terminal
- **ESCALATION:** hosting/PHP if opaque

## Importer failure
- **DETECTION:** terminal FAILURE
- **SAFE ACTION:** preserve logs/files
- **DATA LOSS RISK:** catalog/offers not updated
- **RECOVERY:** fix importer; do not mass-disable products on missing offers
- **VALIDATION:** controlled re-run
- **ESCALATION:** 1C vendor if file corrupt

## Terminal missing
- **DETECTION:** import suspected but no terminal
- **SAFE ACTION:** inspect wrapper after-run hooks
- **DATA LOSS RISK:** silent ops
- **RECOVERY:** repair terminal write; backfill carefully
- **VALIDATION:** terminal appears for new run
- **ESCALATION:** disk permissions

## Completion dispatcher failure
- **DETECTION:** terminal OK, no Telegram
- **SAFE ACTION:** check kill switch first
- **DATA LOSS RISK:** missed alerts (data on site may be fine)
- **RECOVERY:** fix dispatcher/network/secrets non-Git
- **VALIDATION:** SENT + n8n execution
- **ESCALATION:** n8n outage

## n8n inactive
- **DETECTION:** workflow inactive / zero executions
- **SAFE ACTION:** do not spam webhook
- **DATA LOSS RISK:** alert backlog
- **RECOVERY:** activate known-good; verify ~20 nodes
- **VALIDATION:** test/admin event delivers
- **ESCALATION:** n8n platform

## Data Table failure
- **DETECTION:** dedupe errors / conflicts
- **SAFE ACTION:** stop uncontrolled retries
- **DATA LOSS RISK:** duplicate or dropped events
- **RECOVERY:** repair table access; consider DB successor later
- **VALIDATION:** FIRST_SEEN→SENT path
- **ESCALATION:** n8n Data Table limits

## Telegram failure
- **DETECTION:** n8n fails at Telegram node
- **SAFE ACTION:** no token in chat/Git
- **DATA LOSS RISK:** operator blind
- **RECOVERY:** credential/chat id fix in n8n vault
- **VALIDATION:** one factual message
- **ESCALATION:** Telegram API

## Watchdog failure
- **DETECTION:** no alert on true no-import
- **SAFE ACTION:** verify cron + kill switch + freshness
- **DATA LOSS RISK:** silent absence
- **RECOVERY:** fix gateway/cron; avoid stale `_current` skip
- **VALIDATION:** controlled condition proof
- **ESCALATION:** Beget cron

## Beget cron missing/disabled
- **DETECTION:** no scheduled runs
- **SAFE ACTION:** operator recreate cron (API may AUTH_ERROR)
- **DATA LOSS RISK:** no daily import
- **RECOVERY:** restore `0 8 * * *` / `0 9 * * *` Europe/Moscow historically
- **VALIDATION:** next window fires
- **ESCALATION:** hosting support

## Admin manual import failure
- **DETECTION:** button error / lock
- **SAFE ACTION:** check auth + lock
- **DATA LOSS RISK:** low if scheduled OK
- **RECOVERY:** clear stuck lock carefully; fix token
- **VALIDATION:** ADMIN_MANUAL terminal
- **ESCALATION:** admin ACL

## Offers input absence
- **DETECTION:** ATTENTION OFFERS_INPUT_MISSING
- **SAFE ACTION:** treat as ATTENTION not success
- **DATA LOSS RISK:** prices/stock stale
- **RECOVERY:** upstream forensic (OPEN); do not fake success
- **VALIDATION:** honest Telegram
- **ESCALATION:** 1C configuration owner

## Accidental workstation task re-enable
- **DETECTION:** poller/producer enabled
- **SAFE ACTION:** disable immediately
- **DATA LOSS RISK:** duplicate producers / popups
- **RECOVERY:** disable; verify server path
- **VALIDATION:** independence checklist
- **ESCALATION:** none if caught early

## Visible PowerShell popup returns
- **DETECTION:** interactive window
- **SAFE ACTION:** disable interactive task
- **DATA LOSS RISK:** operator disruption
- **RECOVERY:** hidden/noninteractive only; retire poller
- **VALIDATION:** no popups
- **ESCALATION:** Windows task ACL

## Kill switch disabled unexpectedly
- **DETECTION:** dispatch muted while expecting alerts
- **SAFE ACTION:** confirm intentional mute
- **DATA LOSS RISK:** missed Telegram
- **RECOVERY:** re-enable if authorized; audit who changed local config
- **VALIDATION:** next event delivers
- **ESCALATION:** access control on server config
