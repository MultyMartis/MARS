# PHASE 1B-D0 — Inactive Sandbox Next-Step Decision and Runtime Connection Charter

**Status:** COMPLETE (documentation / decision only)
**Date:** 2026-07-24
**Branch:** `mars/canonical-post-recovery`
**Mode:** NO live mutation · NO implementation · NO activation · NO Telegram send
**Readiness:** `READY_FOR_SELECTED_INACTIVE_IMPLEMENTATION_PHASE`
**Selected next phase:** **Phase 1B-D1 — Durable Dedupe Design and Inactive Sandbox Implementation**

---

## 1. Purpose

Define the exact safe sequence and contracts to move from the verified inactive Telegram-integrated sandbox baseline toward a future controlled runtime connection — without connecting production runtime, changing the live workflow, sending Telegram messages, or activating anything in this phase.

## 2. Accepted baselines (verified ancestors of HEAD)

| Commit | Subject |
|--------|---------|
| `791de1d71485c65440f4da88203b6500b36aa0eb` | feat(client-ops): add reporting bridge offline core |
| `04cd01d1881bccf6fc0dfeebef5b891e378fef37` | feat(client-ops): extend n8n programmer capability |
| `51cfddd8533dbf7e0735929ee03b4005a16ad2f5` | feat(client-ops): add inactive n8n sandbox evidence |
| `5ea609fe064da91ccc0dc3da8501df41fb2d2b8e` | feat(client-ops): bind native webhook auth |
| `8992057c78c771805abcfc5ae76f1e83f825c21d` | test(client-ops): validate authenticated n8n intake |
| `6031557dafed42596cb62046757aa6c5c4581c47` | feat(client-ops): prepare verified telegram sandbox integration |
| `14bc908d75364e07682b58d9ea07b0b0acc20453` | feat(client-ops): apply verified telegram sandbox delivery |

**CURRENT HEAD at D0 session:** recorded in evidence / REPORT (may be later than `14bc908d`; unrelated MARS commits may follow).

## 3. Live workflow reconfirmation (GET-only) — PROVEN

| Field | Expected | Observed |
|-------|----------|----------|
| Name | `MARS Client Ops Bridge — bzpm.ru` | exact-name count=1 |
| ID | `tkM4H0G0gM3q9Foi` | match |
| active | false | false |
| nodes | 10 | 10 |
| executions | 25 | 25 |
| running | 0 | 0 |
| versionId | `900407ad-ca23-45be-9a16-bbd9d88e836f` | match |
| Webhook auth | headerAuth / `WKHmPaw6QBp7WnzP` | match; secret absent from list |
| Telegram | `Telegram Notify Accepted` / `2bIC5376l7ElXb4B` / chat `499423375` | match; token absent from list |
| Pattern B | Respond Accepted → Telegram Notify Accepted | confirmed |
| Rejected → Telegram | false | false |
| Dedupe | deferred sandbox | `DEFERRED_SANDBOX` / `DEDUPE_NOT_ENABLED_SANDBOX` |
| HTTP Request / Sheets / Data Store|Table nodes | 0 | 0 |
| Scheduler / monitor / exporter runtime | disconnected | disconnected |
| Temp semantics workflows | 0 | 0 |

Evidence: `evidence/phase-1b-d0-runtime-connection-charter/LIVE-GET-ONLY-RECONFIRMATION.json`

## 4. Classification discipline

Documents in this phase distinguish **CURRENT / PROVEN / PROPOSED / REQUIRED BEFORE PRODUCTION / SAFE UNKNOWN / DEFERRED / FORBIDDEN WITHOUT NEW CHARTER**. Sandbox evidence is not production readiness.

## 5. Architecture Decision Records

### ADR-1 — Dedupe stage ordering

| Field | Content |
|-------|---------|
| **Decision** | Durable dedupe is **mandatory before any runtime producer connection** (option **A**). |
| **Evidence** | B2: duplicate `event_id` accepted twice; C1: Pattern B Telegram after 202. |
| **Alternatives** | B (before scheduler only); C (one manual E2E without dedupe); D (none). |
| **Tradeoffs** | Delays producer connection; prevents duplicate Telegram. |
| **SAFE UNKNOWN** | None material to ordering. |
| **Consequences** | Next phase = durable dedupe (D1), not runtime POST. |
| **Rollback impact** | N/A for D0; D1 must preserve inactive + stop-producer rule if rolled back. |

### ADR-2 — Preferred runtime producer pattern

| Field | Content |
|-------|---------|
| **Decision** | **R1** Exporter as producer; fallback **R3** pickup adapter. |
| **Evidence** | Phase 1A exporter; PROFILE_B_REQUIRED; n8n must not re-read raw artifacts. |
| **Alternatives** | R2 monitor-direct; R4 n8n pull. |
| **Tradeoffs** | R1 needs `push-webhook` work; lowest coupling. |
| **SAFE UNKNOWN** | Long-term exporter host placement. |
| **Consequences** | Monitor remains unchanged; secrets stay on producer host. |
| **Rollback impact** | Disable POST mode / adapter only. |

### ADR-3 — Secret and endpoint configuration boundary

| Field | Content |
|-------|---------|
| **Decision** | Secrets in ignored `local/client-ops-reporting-bridge/bzpm.ru/secrets.local.env`; endpoint route in ignored local profile; committed site profile may hold non-secret identity only; never commit complete webhook URL. |
| **Evidence** | Existing secret file + key `CLIENT_OPS_WEBHOOK_AUTH_SECRET`; prior B2 runners. |
| **Alternatives** | Env-only; committed route; n8n-owned producer secrets. |
| **Tradeoffs** | Operator must maintain local files. |
| **SAFE UNKNOWN** | Exact ignored endpoint filename convention until producer charter. |
| **Consequences** | Rotation procedure required before production. |
| **Rollback impact** | Restore ignored files; rotate credential if needed. |

### ADR-4 — First connection mode

| Field | Content |
|-------|---------|
| **Decision** | Manual/HITL first; scheduler later; production activation last. First real-source test may use **temporary** activation under HITL, not durable activation. |
| **Evidence** | B2/C1 temporary activate→test→deactivate pattern. |
| **Alternatives** | Durable activate early; schedule-first. |
| **Tradeoffs** | More operator steps; safer containment. |
| **SAFE UNKNOWN** | None. |
| **Consequences** | Ordered progression frozen in scheduler decision doc. |
| **Rollback impact** | Deactivate workflow; stop manual producer. |

### ADR-5 — Retry ownership

| Field | Content |
|-------|---------|
| **Decision** | Producer owns network/POST retries (future, bounded); n8n owns Telegram delivery retries (future, bounded); **no automatic retries enabled in D0**. Ambiguous timeouts require dedupe consultation before repost. |
| **Evidence** | `FAILURE-RETRY-AND-ROLLBACK-V1.md`; Pattern B async delivery. |
| **Alternatives** | n8n-only retries; unlimited retries. |
| **Tradeoffs** | Manual ops until policies verified. |
| **SAFE UNKNOWN** | Final numeric bounds may be tuned with evidence. |
| **Consequences** | D1/D2 must implement before unattended mode. |
| **Rollback impact** | Disable retry flags. |

### ADR-6 — Telegram failure handling

| Field | Content |
|-------|---------|
| **Decision** | Telegram failure does not alter returned webhook response; updates delivery/dedupe state only; duplicates blocked by `SENT`; failed rows retained for manual replay. |
| **Evidence** | C0S/C1 Pattern B; Phase 0B failure catalog. |
| **Alternatives** | Fail webhook if Telegram fails (breaks Pattern B). |
| **Tradeoffs** | 202 ≠ delivered; observability mandatory. |
| **SAFE UNKNOWN** | Exact Telegram error taxonomy mapping. |
| **Consequences** | Operator must inspect execution + dedupe for delivery truth. |
| **Rollback impact** | Cannot unsend messages. |

### ADR-7 — Scheduler ownership

| Field | Content |
|-------|---------|
| **Decision** | Future Client Ops producer uses a **dedicated Windows Task Scheduler** task; not the SITE-002 monitor task; not n8n Schedule Trigger for first connection. |
| **Evidence** | SITE-002 monitor task exists separately; Bridge is webhook-driven. |
| **Alternatives** | Piggyback monitor schedule; n8n cron; other runtime job systems. |
| **Tradeoffs** | Extra task to manage. |
| **SAFE UNKNOWN** | Exact task name/XML until scheduler charter. |
| **Consequences** | Scheduler only after manual E2E. |
| **Rollback impact** | Disable Client Ops task only. |

### ADR-8 — Runtime checkout requirement

| Field | Content |
|-------|---------|
| **Decision** | Scheduled/runtime jobs must not run from dirty `X:\AI MARS`; use clean checkout under `X:\AI MARS STORAGE\runtime-checkouts\...` when created under future charter. D0 creates none. |
| **Evidence** | Universal MARS Git/runtime rule in task charter; SITE-002 monitor historically referenced `X:\AI MARS` working directory (debt — must not copy for Client Ops). |
| **Alternatives** | Continue dirty-main scheduling (rejected). |
| **Tradeoffs** | Requires Storage checkout procedure later. |
| **SAFE UNKNOWN** | Exact checkout layout for Client Ops exporter. |
| **Consequences** | Scheduler charter must prove clean checkout. |
| **Rollback impact** | Stop task; leave dirty main untouched. |

### ADR-9 — Observability retention

| Field | Content |
|-------|---------|
| **Decision** | Mandatory sanitized fields per attempt; retain in ignored local runtime evidence + committed milestone packs; no raw payloads/secrets in Git; Telegram carries SIMPLE only. |
| **Evidence** | Existing phase evidence pack pattern. |
| **Alternatives** | Dashboard-first; Git-full traces. |
| **Tradeoffs** | Operator manages local evidence. |
| **SAFE UNKNOWN** | Future dashboard layer. |
| **Consequences** | Producer must emit redacted evidence writer. |
| **Rollback impact** | Preserve evidence; do not delete for convenience. |

### ADR-10 — Production activation sequence

| Field | Content |
|-------|---------|
| **Decision** | Activation is last after all gates in `PRODUCTION-ACTIVATION-GATES.md`; D0 authorizes none. |
| **Evidence** | Workflow inactive; production disconnected. |
| **Alternatives** | Activate for convenience (rejected). |
| **Tradeoffs** | Longer path to unattended ops. |
| **SAFE UNKNOWN** | None for the prohibition itself. |
| **Consequences** | Multiple HITL gates remain. |
| **Rollback impact** | Deactivate; snapshot required pre-activation. |

## 6. Durable dedupe recommendation (summary)

- **Primary (PROPOSED):** n8n **Data Table** (OpenAPI-proven on this install; upsert documented; list GET count=0).
- **Fallback:** producer-side durable ledger (ignored local).
- **Reject:** Google Sheets; staticData-as-sole-SoT; assumed legacy Data Store (not in OpenAPI).

## 7. HITL gates (remaining)

| Gate | Before |
|------|--------|
| Approve D1 durable dedupe charter | Dedupe implementation |
| Approve Data Table create / workflow inactive mutation | D1 apply |
| Approve producer POST capability charter | Runtime producer connection |
| Approve temporary activation + live-source test | First E2E |
| Approve scheduler task (disabled then enable) | Scheduler connection |
| Approve all production activation gates | Production activation |

## 8. Forbidden without new charter

Workflow update/activate; webhook POST; Telegram API/send; credential mutation; exporter/monitor/scheduler/Storage/runtime-checkout changes; AI APIs; git stage/commit/push; foreign WIP.

## 9. Evidence pack

`projects/client-ops-reporting-bridge/evidence/phase-1b-d0-runtime-connection-charter/`

## 10. Final verdict line

**COMPLETE — INACTIVE SANDBOX NEXT-STEP AND RUNTIME CONNECTION CHARTER DEFINED**
