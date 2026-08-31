# SITE-002 / BZPM — Agent Brain (Client Ops generation)

**Read this before operating SITE-002 1C / Client Ops.**

## Identity

- **SITE-002** · https://bzpm.ru/ · OpenCart / ocStore 3.0.3.9
- MARS container: `X:\AI MARS\projects\ocpilot\sites\site-002\`
- Start-here: `client-ops/FINAL-HANDOFF.md`

## Runtime authority (memorize)

- Normal reporting is **server-side**.
- Beget import cron → wrapper → canonical runner → terminal → completion dispatcher → n8n → Data Table → Telegram.
- Watchdog is server-side (cron historically `0 9 * * *` Europe/Moscow).
- Admin: Система → Обмен с 1С → Запустить импорт 1С → **same runner**.
- Workstation **not** required for production reporting.
- Windows completion poller: **RETIRED / disabled**.
- Old local producer: **RETIRED / disabled**.
- Post_1C monitor: **OPTIONAL_HYGIENE** (`POST_1C_MONITOR_KEEP_OPTIONAL_HYGIENE`) — not Client Ops authority.

## n8n / dedupe / Telegram

- Workflow: `MARS Client Ops Bridge — bzpm.ru` · id `tkM4H0G0gM3q9Foi` · ~20 nodes · **active**
- Dedupe: n8n Data Table `MARS Client Ops Dedupe — bzpm.ru` · `H6VYhwz7RXZCBMmu`
- **Not Google Sheets**
- Bot: «Монитор bzpm.ru — MetaCODE»

## Import contract

- Catalog: `import0_*.xml`
- Offers: `offers0_*.xml`
- Not `offer.xml`
- Missing offers → ATTENTION / `OFFERS_INPUT_MISSING` — **OPEN** upstream forensic
- Concurrency: import=1, report=1

## Kill switch

- `CLIENT_OPS_DISPATCH_ENABLED` in non-Git local config
- Blocks outbound only; terminal still records

## Git / MARS authority

- Canonical Git repo: `X:\AI MARS` on branch `mars/canonical-post-recovery`.
- Client Ops knowledge authority: `client-ops/` in that repo (not deleted STORAGE `git-sync-*` / `git-reconcile-*` contours).
- Historical STORAGE git-sync worktrees were **disposable promotion aids**; post–2026-08 hygiene they are gone. Use main repo or a **new** clean worktree under `X:\AI MARS STORAGE\git-sync-<task>\repo` — never assume an old git-sync path still exists.
- Closeout: `client-ops/storage-hygiene/POST-STORAGE-HYGIENE-LOSS-AUDIT-2026-08-31.md`

## Boundaries

- Do not mutate live importer/reporting without charter
- Do not delete workstation components without cleanup charter + manifest
- Do not touch dirty MAIN foreign WIP
- Do not commit secrets / tokens
- Do not use workstation as normal production runtime
- Prefer clean worktree for Git canonicalization

## Canonical pack

`X:\AI MARS\projects\ocpilot\sites\site-002\client-ops\`
