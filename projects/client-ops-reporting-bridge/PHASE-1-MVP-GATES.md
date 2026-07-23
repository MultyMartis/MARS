# Phase 1 MVP Gates

**Status:** DOCUMENTATION + PROGRAMMER EXTENSION / PHASE 1B SANDBOX CREATE PENDING
**Gate actions:** live n8n / Telegram / webhook actions **NOT EXECUTED** by this pack
**Phase 1 production readiness:** NOT READY until remaining activation gates are satisfied

---

## 1. Decision register (updated)

| # | Question | State | Notes |
|---|----------|-------|-------|
| 1 | Can the n8n host directly read `X:\AI MARS STORAGE`? | **SUPERSEDED for Bridge path** | Client Ops Bridge — bzpm.ru frozen as **PROFILE_B_REQUIRED**; Storage access remains independently relevant for optional PROFILE A / audit mirrors |
| 2 | Dedicated Telegram bot vs existing internal bot? | **RECOMMENDED: dedicated Client Ops bot**; operator approval required before external-system work | Bot does **not** exist yet; no credentials created; **not** in first sandbox |
| 3 | Suppress routine OK after initial validation period? | **APPROVED for Phase 1 validation:** OK **always sends**; suppression is a later policy option (not enabled) | Consumer-side policy |
| 4 | Is artifact precedence frozen exactly as documented? | **APPROVED** | See `ARTIFACT-AUTHORITY-AND-PRECEDENCE.md` + Phase 0B algorithm |
| 5 | Is Phase 1 routing confirmed internal-only? | **APPROVED** | No client routing before separate approval |
| — | Freshness SLA 26h (`93600` seconds) | **APPROVED** | `age_seconds = now_utc − observed_at` |
| — | Clock skew tolerance `300` seconds | **APPROVED** | Future `observed_at` → `SOURCE_TIME_INVALID` |
| — | Transport profile for bzpm Bridge | **PROFILE_B_REQUIRED** | Authenticated webhook intake |
| — | Manual n8n UI assembly | **NOT ACCEPTED** | Cursor/MetaBOT programmer generates JSON |
| — | First sandbox dedupe | **DEDUPE_DEFERRED_SANDBOX** | No false durable claims |
| — | Auth MVP | **Custom header/Bearer + HITL binding** | Placeholder until live bind |

Do **not** re-ask decisions already marked APPROVED / FROZEN.

---

## 2. Primary architecture path — PROFILE B

Client Ops Bridge for bzpm.ru uses **PROFILE_B_REQUIRED**:

- local exporter (temporary workstation runtime) builds sanitized envelope;
- authenticated POST to protected n8n webhook (future);
- n8n validates independently and responds with structured JSON;
- Telegram remains a later separated gate.

---

## 3. Preconditions

- Phase 0A contract pack accepted.
- Phase 0B design pack present.
- Phase 1A offline exporter complete.
- Programmer extension local artifacts present (`CLIENT-OPS-PROGRAMMER-CAPABILITY-EXTENSION.md`).
- SITE-002 monitor remains unchanged unless a separate charter says otherwise.
- No production mutation from reporting-bridge work.
- Foreign WIP elsewhere in repo remains untouched.

---

## 4. Approval gates (ordered)

| Gate | Meaning | Evidence required | Rollback expectation |
|------|---------|-------------------|----------------------|
| **Documentation gate** | Contract pack reviewed | Operator acceptance of Phase 0A docs | Docs-only revert; no runtime |
| **Exporter design gate** | Phase 0B design of read-only exporter | Design docs + acceptance test plan (**satisfied as docs**) | No deploy |
| **Programmer extension gate** | Local template/harness/runbooks ready | Harness PASS + template gates PASS | Docs/tools only |
| **Auth binding gate** | Resolve HITL secret binding | Operator credential/env placement; no secrets in Git | Rotate secret externally |
| **n8n inactive sandbox create gate** | Create inactive workflow via programmer | Sanitized create/re-GET evidence; no activate | Abandon inactive or HITL delete |
| **Authenticated POST gate** | First protected webhook tests | Synthetic envelopes only | Disable webhook / leave inactive |
| **Telegram credential gate** | Dedicated bot approval + credential placement | Operator credential placement in n8n only; no secrets in Git | Rotate/revoke token externally |
| **First sandbox message gate** | First SIMPLE message to **approved** internal test chat | Screenshot/transcript sanitized | Stop sending; disable workflow |
| **Production workflow activation gate** | Explicit HITL to activate | Apply manifest + rollback plan (MetaBOT discipline) | Deactivate workflow; preserve SITE monitor |

**No client routing before separate approval.**
**No manual n8n node assembly.**

---

## 5. Acceptance evidence (Phase 1)

Minimum evidence set when Phase 1 is later executed:

- Sanitized sample envelopes for OK / ATTENTION / FAILED / BLOCKED
- Proof SIMPLE counts match envelope
- Proof Telegram/AI failures do not mutate site_status
- Proof SOURCE_ARTIFACT_CONFLICT → BLOCKED
- Proof stale → BLOCKED / `SOURCE_REPORT_STALE`
- Proof security rejection prevents publication/send
- Proof no secrets/paths in messages
- Proof SITE monitor/scheduler/baseline unchanged by bridge work
- Proof same `event_id` across delivery retries

See `ACCEPTANCE-TEST-PLAN-V1.md`.

---

## 6. References for future implementers

- Programmer extension: `CLIENT-OPS-PROGRAMMER-CAPABILITY-EXTENSION.md`
- Phase 0B readiness: `PHASE-1-IMPLEMENTATION-READINESS.md`
- MetaBOT Client Ops knowledge: `projects/metabot-seo-content-agent/metabot-developer/client-ops-n8n-extension-v1.md`
- MetaBOT n8n rules: `projects/metabot-seo-content-agent/n8n-project-development-rules-v1.md`
- MetaBOT integration boundary: `projects/metabot-seo-content-agent/integration-boundary.md`
