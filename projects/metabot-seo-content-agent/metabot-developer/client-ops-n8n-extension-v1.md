# MetaBOT Developer — Client Ops n8n Extension v1

**Status:** KNOWLEDGE EXTENSION (repository-local)
**Contour:** MetaBOT Developer / Cursor programmer
**Target workflow name:** `MARS Client Ops Bridge — bzpm.ru`
**Does not rewrite:** general MetaBOT grammar / live SEO workflow exports

## 1. What Client Ops workflows are

Client Ops workflows intake an already-normalized `mars.client_ops.report` envelope from a site operational exporter (SITE-002 / bzpm.ru first), validate security and schema, optionally dedupe, and later may deliver internal operator Telegram SIMPLE.

They are **not** SEO content generation workflows.

## 2. Differences from SEO generation workflows

| Dimension | SEO Intake/Worker/Admin | Client Ops Bridge |
|-----------|-------------------------|-------------------|
| Trigger | Telegram / internal webhooks | PROFILE_B authenticated webhook |
| Payload | SEO task commands | `mars.client_ops.report` envelope |
| Primary output | SEO text / Sheets memory | Structured accept/reject HTTP response |
| First sandbox Telegram | Often present | **Applied on inactive sandbox (1B-C1)**; production activation still gated |
| Dedupe | Sheets / locks | Deferred in first sandbox |
| Site mutation | None | None (also no SITE-002 monitor changes) |

## 3. Naming

Exact future workflow name:

`MARS Client Ops Bridge — bzpm.ru`

Internal identifiers:

- `site_id`: `SITE-002`
- `event_type`: `site.post_1c_monitor`
- `domain`: `bzpm.ru`
- Transport: `PROFILE_B_REQUIRED`

## 4. Envelope intake

n8n validates the exporter envelope. It must **not**:

- re-read raw SITE-002 artifacts;
- recompute source classification;
- invent metrics.

## 5. Auth boundary

MVP: custom header / Bearer shared secret over TLS, validated before business processing.

- Secret never in workflow JSON / Git / fixtures / responses.
- Failed auth → observed native HTTP **403** (`Authorization data is wrong!`); business nodes not executed.
- Phase 1B-B live create state: **AUTH_BLOCKED_INACTIVE_ONLY**.
- Phase 1B-B1 live state: **AUTH_NATIVE_HEADER_CREDENTIAL_BOUND**.
- Phase 1B-B2 live state: **AUTH_NATIVE_HEADER_CREDENTIAL_CONFIRMED** — temporary activation + synthetic POST matrix; workflow returned inactive; no Telegram.
- Phase 1B-C: dedicated Telegram bot `@monitor_bzpm_metacode_bot` + unbound `telegramApi` credential evidenced; no message send; workflow unchanged.
- Phase 1B-C0: authorized chat-target discovery retry (`getWebhookInfo` + one `getUpdates` without offset) still returned zero updates; no local chat target file; no message send; workflow unchanged.
- Phase 1B-C0R2: final discovery retry after operator-confirmed Start/`/start` returned one private chat update; local ignored `telegram.target.local.env` created; no message send; workflow unchanged.
- Phase 1B-C0S: temporary semantics workflow proved Pattern B (`Respond` then Telegram) on this host; exactly one synthetic Telegram message; temporary workflow deleted; real Client Ops workflow unchanged.
- Phase 1B-C1: controlled apply added one Telegram node on accepted path only; credential `2bIC5376l7ElXb4B` bound; one synthetic delivery verified; workflow returned inactive; executions 24→25.
- Native header-auth credential create payload shape is evidenced (Phase 1B-B1).
- Telegram credential create payload shape is evidenced (Phase 1B-C): `{ name, type: "telegramApi", data: { accessToken } }`.
- Controlled temporary activation + production webhook POST + deactivate-in-finally is evidenced (Phase 1B-B2 / 1B-C1).
- Hardening target: HMAC-SHA256(raw body + timestamp) with replay window (not in first sandbox template).

## 6. Validation boundary

Validate: schema_name, schema major 1, site identity, event_type, normalized_status enum, integer metrics, security flags, UUID event_id, unsafe string scan.

## 7. Dedupe boundary

First sandbox: `DEDUPE_DEFERRED_SANDBOX` / response may advertise `dedupe: "DEFERRED_SANDBOX"` and `DEDUPE_NOT_ENABLED_SANDBOX`.

Phase 1B-D0 decision: durable dedupe is **mandatory before any runtime producer connection**. Preferred store on this install: n8n **Data Table**. Phase 1B-D1 proved **sequential** durable dedupe (FIRST_SEEN / DUPLICATE / EVENT_ID_CONFLICT). Classification remains `DEDUPE_SEQUENTIAL_SAFE_CONCURRENCY_UNPROVEN`. Post-Telegram SENT ledger deferred. Phase 1B-D2 added an **offline** sequential producer (mock/fixture/disabled transports; `push-webhook` blocked as `NETWORK_DISPATCH_NOT_AUTHORIZED_D2`). Phase 1B-D3 proved **one controlled** sequential producer HTTPS path (synthetic FIRST_SEEN + exact replay DUPLICATE_SUPPRESSED) with temporary activation and final inactive workflow; generic live mode remains blocked; no SITE-002 runtime/scheduler connection. Do not claim concurrent-safe dedupe, unattended producer, or production activation.

## 8. Structured response

Deterministic JSON accept/reject contract (see Client Ops programmer extension doc). No secret leakage.

## 9. Sandbox-first rule

Generate local template → offline harness → inactive create → re-GET → Phase 1B-B1 auth binding → Phase 1B-B2 authenticated POST → Phase 1B-C Telegram bot/credential intake → Phase 1B-C0/C0R2 chat-target discovery → Phase 1B-C0S semantics → Phase 1B-C1 Telegram sandbox apply (done) → Phase 1B-C1B evidence baseline (done) → Phase 1B-D0 runtime connection charter (done) → Phase 1B-D1 durable dedupe (done) → Phase 1B-D1B evidence baseline commit → Phase 1B-D2 sequential runtime producer offline (done) → Phase 1B-D3 controlled sequential producer connection + synthetic live POST (done) → Phase 1B-D3B evidence baseline commit (this wave) → Phase 1B-D4 real-source adapter design / manual dry-run (next) → only later production activation under separate charter.

## 10. Telegram sandbox apply (1B-C1)

Telegram Pattern B is applied on the inactive Client Ops workflow (`Telegram Notify Accepted` after `Respond Accepted`). Rejected paths do not send. Production activation remains a separated gate.

## 11. No operator manual node assembly

MetaBOT / Cursor programmer must generate and apply workflow JSON. Manual n8n UI assembly is **NOT ACCEPTED**.

## 12. Experience capture requirement

After first sandbox apply, update `projects/client-ops-reporting-bridge/n8n/experience-pack/` with create/re-GET facts. Phase 1B-B…C1 captured; Phase 1B-D0 captured architecture decisions; Phase 1B-D1 captured durable sequential dedupe + Data Table retention. Production activation still incomplete.

## Remaining gaps (SAFE UNKNOWN)

- Exact n8n application version.
- Data Table workflow node typeVersion / concurrency atomicity of upsert.
- Workflow-level HTTP 413 for oversized bodies (observed native 422 parse before size gate).
- Long-term exporter host placement.
