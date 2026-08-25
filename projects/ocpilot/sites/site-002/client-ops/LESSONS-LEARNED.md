# SITE-002 — Lessons Learned Index

### webhook secret key-name mismatch

- **SYMPTOM:** Dispatch/webhook auth failed or miswired
- **ROOT CAUSE:** Inconsistent secret key names / aliases
- **FIX:** Align exact secret key names end-to-end; never invent aliases ad hoc
- **REUSABLE RULE:** Exact secret key names are part of the contract

### stale oldest-first backlog selection

- **SYMPTOM:** Wrong/old event selected for delivery
- **ROOT CAUSE:** Backlog picker preferred oldest without freshness semantics
- **FIX:** Separate source status vs delivery freshness; prefer validated current terminal
- **REUSABLE RULE:** Do not use naive oldest-first as production selector

### completion poller FTP secret parser failure

- **SYMPTOM:** No Telegram after import; poller failed
- **ROOT CAUSE:** Windows poller could not parse FTP secret
- **FIX:** Retire workstation poller; server-side dispatch
- **REUSABLE RULE:** Do not rely on workstation FTP secret parsing for production

### completion poller terminal-not-visible

- **SYMPTOM:** Import ran but poller saw no terminal
- **ROOT CAUSE:** Polling visibility / path mismatch
- **FIX:** Write terminal authoritatively; dispatch from server after terminal
- **REUSABLE RULE:** Terminal must be server-visible to dispatcher

### visible PowerShell popup

- **SYMPTOM:** Interactive PowerShell windows on operator PC
- **ROOT CAUSE:** Interactive Scheduled Task / visible host
- **FIX:** Hidden noninteractive tasks only; retire interactive poller
- **REUSABLE RULE:** Never use visible interactive tasks for production

### stale `_current` causing watchdog false skip

- **SYMPTOM:** Watchdog skipped when it should alert
- **ROOT CAUSE:** Stale current pointer treated as fresh truth
- **FIX:** Validate freshness; do not trust stale `_current`
- **REUSABLE RULE:** Validate pointers before skip decisions

### server-side completion dispatch replacing poller

- **SYMPTOM:** Architecture cutover
- **ROOT CAUSE:** Workstation dependency for reporting
- **FIX:** Implement `mars_1c_completion_dispatch.php`
- **REUSABLE RULE:** Server dispatch is production authority

### old local producer retirement

- **SYMPTOM:** Duplicate/local producer risk
- **ROOT CAUSE:** Windows producer was prior path
- **FIX:** Disable task; classify RETIRED
- **REUSABLE RULE:** One authoritative producer path only

### hidden/noninteractive hygiene monitor

- **SYMPTOM:** Task XML Hidden ACL issues
- **ROOT CAUSE:** Could not mutate Hidden via XML ACL
- **FIX:** Self-hide runner; keep as optional hygiene
- **REUSABLE RULE:** Hygiene ≠ Client Ops authority

### Beget API auth limitation

- **SYMPTOM:** Could not create cron via API
- **ROOT CAUSE:** API AUTH_ERROR
- **FIX:** Operator-created cron accepted
- **REUSABLE RULE:** Document operator path; do not block on API

### operator-created watchdog cron

- **SYMPTOM:** Watchdog schedule needed
- **ROOT CAUSE:** API create failed
- **FIX:** Operator created `0 9 * * *`
- **REUSABLE RULE:** Cron existence is ops truth

### repeated daily attention must create new events

- **SYMPTOM:** Same offers-missing day after day must alert
- **ROOT CAUSE:** Over-aggressive dedupe risk
- **FIX:** New run_id / new day = new event
- **REUSABLE RULE:** Replay ≠ new run

### offers missing is ATTENTION not success

- **SYMPTOM:** Misleading success messaging
- **ROOT CAUSE:** Treating partial exchange as OK
- **FIX:** Classify OFFERS_INPUT_MISSING / ATTENTION
- **REUSABLE RULE:** Partial ≠ success

### scheduled/manual share one runner

- **SYMPTOM:** Divergent importer logic risk
- **ROOT CAUSE:** Separate code paths
- **FIX:** Single canonical runner
- **REUSABLE RULE:** One runner, two triggers

### workstation not required for reporting

- **SYMPTOM:** Ops fragility
- **ROOT CAUSE:** Poller on operator PC
- **FIX:** Server-side chain only
- **REUSABLE RULE:** Workstation independence

### secrets must not enter Git/reports

- **SYMPTOM:** Leak risk
- **ROOT CAUSE:** Tokens in docs/screenshots
- **FIX:** Non-Git local config; redact reports
- **REUSABLE RULE:** Never commit secrets

### kill switch separates terminal from dispatch

- **SYMPTOM:** Need mute without stopping import
- **ROOT CAUSE:** Coupled outbound+terminal
- **FIX:** `CLIENT_OPS_DISPATCH_ENABLED`
- **REUSABLE RULE:** Record terminal even when muted
