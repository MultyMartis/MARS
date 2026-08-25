# REPRODUCE-1C-CLIENT-OPS-FOR-NEW-SITE.md

Project-neutral playbook for OpenCart/ocStore + 1C + n8n + Telegram.

Derived from SITE-002 / bzpm.ru accepted server-side generation.

## Phase 0 — intake / platform forensic

- **OBJECTIVE:** Confirm OpenCart/ocStore version, hosting, 1C exchange path, timezone
- **INPUTS:** Site identity, inventory, risks
- **OUTPUTS:** Platform known; exchange path found
- **ACCEPTANCE GATES:** Platform known; exchange path found; evidence saved; no secrets in Git
- **COMMON FAILURE MODES:** Wrong platform assumptions
- **DO-NOT:** Do not invent importer

## Phase 1 — 1C exchange contract

- **OBJECTIVE:** Define filename families + ownership
- **INPUTS:** Contract doc
- **OUTPUTS:** import0/offers0 documented
- **ACCEPTANCE GATES:** import0/offers0 documented; evidence saved; no secrets in Git
- **COMMON FAILURE MODES:** Literal offer.xml assumption
- **DO-NOT:** Do not skip offers contract

## Phase 2 — canonical import runner

- **OBJECTIVE:** One runner for scheduled+manual
- **INPUTS:** Wrapper+runner
- **OUTPUTS:** Singleton lock works
- **ACCEPTANCE GATES:** Singleton lock works; evidence saved; no secrets in Git
- **COMMON FAILURE MODES:** Dual code paths
- **DO-NOT:** Do not fork runners

## Phase 3 — terminal state model

- **OBJECTIVE:** Authoritative terminal fields
- **INPUTS:** Terminal schema
- **OUTPUTS:** run_id+classification written
- **ACCEPTANCE GATES:** run_id+classification written; evidence saved; no secrets in Git
- **COMMON FAILURE MODES:** Silent failures
- **DO-NOT:** Do not skip terminal

## Phase 4 — scheduled import

- **OBJECTIVE:** Cron entry
- **INPUTS:** Beget/cron proof
- **OUTPUTS:** Natural scheduled run
- **ACCEPTANCE GATES:** Natural scheduled run; evidence saved; no secrets in Git
- **COMMON FAILURE MODES:** Wrong TZ
- **DO-NOT:** Do not use workstation scheduler as primary

## Phase 5 — admin manual trigger

- **OBJECTIVE:** Admin button → same runner
- **INPUTS:** Admin UI+POST
- **OUTPUTS:** Manual run terminal ADMIN_MANUAL
- **ACCEPTANCE GATES:** Manual run terminal ADMIN_MANUAL; evidence saved; no secrets in Git
- **COMMON FAILURE MODES:** Bypass runner
- **DO-NOT:** Do not claim it triggers 1C upload

## Phase 6 — completion dispatch

- **OBJECTIVE:** Server outbound on terminal
- **INPUTS:** Dispatcher+secrets non-Git
- **OUTPUTS:** SENT proof
- **ACCEPTANCE GATES:** SENT proof; evidence saved; no secrets in Git
- **COMMON FAILURE MODES:** Workstation poller
- **DO-NOT:** Do not couple to workstation

## Phase 7 — dedupe/event model

- **OBJECTIVE:** FIRST_SEEN/SENT + new-run events
- **INPUTS:** Data Table or DB
- **OUTPUTS:** Replay safe; daily new event
- **ACCEPTANCE GATES:** Replay safe; daily new event; evidence saved; no secrets in Git
- **COMMON FAILURE MODES:** Over-dedupe
- **DO-NOT:** Do not use Sheets by default

## Phase 8 — Telegram formatter

- **OBJECTIVE:** Russian operator UX
- **INPUTS:** Formatter nodes
- **OUTPUTS:** Accepted message types
- **ACCEPTANCE GATES:** Accepted message types; evidence saved; no secrets in Git
- **COMMON FAILURE MODES:** Raw enums/secrets
- **DO-NOT:** Do not leak secrets

## Phase 9 — kill switch

- **OBJECTIVE:** CLIENT_OPS_DISPATCH_ENABLED
- **INPUTS:** Local config+admin status
- **OUTPUTS:** Mute outbound; import continues
- **ACCEPTANCE GATES:** Mute outbound; import continues; evidence saved; no secrets in Git
- **COMMON FAILURE MODES:** Coupled mute-import
- **DO-NOT:** Do not put secrets in Git

## Phase 10 — no-import watchdog

- **OBJECTIVE:** Server watchdog+cron
- **INPUTS:** Watchdog proof
- **OUTPUTS:** Natural no-import alert
- **ACCEPTANCE GATES:** Natural no-import alert; evidence saved; no secrets in Git
- **COMMON FAILURE MODES:** Stale _current skip
- **DO-NOT:** Do not trust stale pointers

## Phase 11 — concurrency/locking

- **OBJECTIVE:** Import=1 Report=1
- **INPUTS:** Locks documented
- **OUTPUTS:** Overlap safe
- **ACCEPTANCE GATES:** Overlap safe; evidence saved; no secrets in Git
- **COMMON FAILURE MODES:** Parallel imports
- **DO-NOT:** Do not raise concurrency casually

## Phase 12 — observability

- **OBJECTIVE:** Terminal+n8n+Telegram traces
- **INPUTS:** Runbook checks
- **OUTPUTS:** Diagnose missing message
- **ACCEPTANCE GATES:** Diagnose missing message; evidence saved; no secrets in Git
- **COMMON FAILURE MODES:** Blind retries
- **DO-NOT:** Do not spam retries

## Phase 13 — acceptance tests

- **OBJECTIVE:** Scheduled/manual/watchdog/Telegram
- **INPUTS:** Evidence pack
- **OUTPUTS:** Gates green
- **ACCEPTANCE GATES:** Gates green; evidence saved; no secrets in Git
- **COMMON FAILURE MODES:** Synthetic-only acceptance
- **DO-NOT:** Do not skip natural proof

## Phase 14 — workstation-independence cutover

- **OBJECTIVE:** Retire poller/producer
- **INPUTS:** Disabled tasks+server proof
- **OUTPUTS:** Reporting without PC
- **ACCEPTANCE GATES:** Reporting without PC; evidence saved; no secrets in Git
- **COMMON FAILURE MODES:** Leaving poller enabled
- **DO-NOT:** Do not delete before proof

## Phase 15 — stable freeze

- **OBJECTIVE:** Freeze accepted generation
- **INPUTS:** Readiness flags
- **OUTPUTS:** Production-ready declaration
- **ACCEPTANCE GATES:** Production-ready declaration; evidence saved; no secrets in Git
- **COMMON FAILURE MODES:** Silent drift
- **DO-NOT:** Do not mutate without charter

## Phase 16 — upstream offers forensic if needed

- **OBJECTIVE:** Root-cause offers absence
- **INPUTS:** Forensic report
- **OUTPUTS:** OPEN/RESOLVED honest
- **ACCEPTANCE GATES:** OPEN/RESOLVED honest; evidence saved; no secrets in Git
- **COMMON FAILURE MODES:** Fake closure
- **DO-NOT:** Do not claim fixed without STOP CONDITIONS
