# SITE-002 / BZPM — Master Overview

**MARS identity:** SITE-002  
**Production URL:** https://bzpm.ru/  
**Platform:** OpenCart / ocStore 3.0.3.9  
**Container:** `X:\AI MARS\projects\ocpilot\sites\site-002\`  
**Client Ops pack:** `X:\AI MARS\projects\ocpilot\sites\site-002\client-ops\`  
**Stability (accepted generation):** server-side Client Ops production-ready; unattended reporting authorized for SITE-002 connection.

## What SITE-002 is

Client ecommerce site (bzpm.ru) operated under OCPilot / MARS as **SITE-002**. Primary operational contour for this pack: **1C CommerceML exchange → OpenCart catalog/offers import → Client Ops Telegram reporting**.

## Current 1C import architecture (accepted)

1. Upstream 1C uploads exchange files to the site exchange area.
2. **Beget cron** (Europe/Moscow, historically `0 8 * * *`) invokes canonical server import wrapper:
   - `/storage/mars-tools/cron/mars_1c_import_wrapper.php` (repo copy under `tools/`; historical version advanced to **v1.3.1**).
3. Wrapper runs **canonical import runner** (catalog phase then offers phase) with **singleton lock** (`MAX_SAFE_IMPORT_CONCURRENCY=1`).
4. Terminal run state is written (run_id, trigger_source, classifications, timestamps).
5. **Server completion dispatcher** (`mars_1c_completion_dispatch.php`) posts outbound event when dispatch enabled.
6. **n8n** workflow `MARS Client Ops Bridge — bzpm.ru` (`tkM4H0G0gM3q9Foi`, ~20 nodes, **active**) dedupes via **n8n Data Table** and delivers Telegram.

Manual path: OpenCart admin → **Система → Обмен с 1С → Запустить импорт 1С** → same runner → same dispatch chain. Manual launch processes files **already on the server**; it does **not** by itself force 1C to generate/upload files.

## Current Client Ops architecture

| Layer | Role |
|-------|------|
| Server wrapper + runner | AUTHORITATIVE import execution |
| Terminal state | AUTHORITATIVE run truth |
| Completion dispatcher | AUTHORITATIVE outbound production dispatch |
| Watchdog (`mars_1c_no_import_watchdog.php` + HTTP gateway) | AUTHORITATIVE no-import alerting |
| n8n workflow | Orchestration + Telegram delivery |
| n8n Data Table `MARS Client Ops Dedupe — bzpm.ru` (`H6VYhwz7RXZCBMmu`) | CURRENT durable dedupe/state |
| Telegram «Монитор bzpm.ru — MetaCODE» | Operator-facing delivery |
| Kill switch `CLIENT_OPS_DISPATCH_ENABLED` | Blocks outbound dispatch only (non-Git local config) |

**Google Sheets is NOT current BZPM operational memory.**

## Server-side authority / workstation independence

Declared (D6G1B evidence):

- `SITE002_NORMAL_REPORTING_SERVER_SIDE=YES`
- `SITE002_REPORTING_REQUIRES_OPERATOR_WORKSTATION=NO`
- `SITE002_WINDOWS_COMPLETION_POLLER_RETIRED=YES`
- `SITE002_WINDOWS_OLD_PRODUCER_RETIRED=YES`
- `CLIENT_OPS_UNATTENDED_PRODUCTION_READY=YES`
- `CLIENT_OPS_AUTOMATIC_SITE002_CONNECTION_AUTHORIZED=YES`

## Upstream offers issue

Canonical expected families: `import0_*.xml` (catalog), `offers0_*.xml` (offers). Literal `offer.xml` is **not** the contract.

When `import0_*.xml` arrives and `offers0_*.xml` is absent: catalog may PASS; offers phase runs with no input; prices/stock may not update; classification **OFFERS_INPUT_MISSING** / ATTENTION — **not** full success. Importer must not disable products merely because offers input is absent.

**Root-cause forensic remains OPEN** (see `OFFERS-INPUT-CURRENT-STATE.md`). Natural ATTENTION days historically observed (e.g. 2026-08-08..12); later healthchecks may show intermittent presence of `offers0_1.xml` without proving upstream root cause closed.

## Known non-blockers (for this pack)

- Post_1C Windows monitor as optional hygiene (not Client Ops authority).
- Beget API auth limitation for cron create (operator-created cron accepted).
- Future PostgreSQL successor (documented, not migrated).

## Canonical docs / runbooks / evidence

Start: [FINAL-HANDOFF.md](FINAL-HANDOFF.md). Hierarchy: [DOC-AUTHORITY-HIERARCHY.md](DOC-AUTHORITY-HIERARCHY.md). Evidence index: [evidence-index/README.md](evidence-index/README.md).

## Future roadmap (docs only)

1. Controlled workstation cleanup (manifest ready; no deletes in this phase).
2. Deep-research backlog for next-generation architecture.
3. Optional D6G2 offers forensic.
4. Optional DB-first / PostgreSQL successor (no big-bang).
