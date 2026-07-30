# SCHEDULER-WRAPPER-CONTRACT

- PS1: `...\runtime-state\client-ops-site-002-producer\tmp\run-client-ops-site-002-producer-scheduled.ps1`
- MJS: `...\tmp\run-client-ops-site-002-producer-scheduled.mjs`
- Action: powershell.exe -NoProfile -ExecutionPolicy Bypass -File `<PS1>`
- WorkingDirectory: dedicated producer runtime repo
- Pin check: HEAD == e1d2a178...; porcelain empty; A/B/C/E/D ancestry
- Kill switch: require DRY_RUN; reject ENABLED
- Invokes committed `runUnattendedProducer` from pinned checkout libs
- No secrets on command line

**Post-run correction (no second scheduled invocation):** wrapper previously passed *parsed* kill-switch object into producer (missing site_id → KILL_SWITCH_SITE_MISMATCH). Corrected to pass RAW kill-switch JSON. Correction not re-proven via scheduler in D6D3.

Token: D6D3_TASK_ACTION_BOUND_TO_PINNED_RUNTIME

