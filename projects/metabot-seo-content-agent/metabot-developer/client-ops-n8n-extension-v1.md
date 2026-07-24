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
| First sandbox Telegram | Often present | **Forbidden** |
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
- Native header-auth credential create payload shape is evidenced (Phase 1B-B1).
- Controlled temporary activation + production webhook POST + deactivate-in-finally is evidenced (Phase 1B-B2).
- Hardening target: HMAC-SHA256(raw body + timestamp) with replay window (not in first sandbox template).

## 6. Validation boundary

Validate: schema_name, schema major 1, site identity, event_type, normalized_status enum, integer metrics, security flags, UUID event_id, unsafe string scan.

## 7. Dedupe boundary

First sandbox: `DEDUPE_DEFERRED_SANDBOX` / response may advertise `dedupe: "DEFERRED_SANDBOX"` and `DEDUPE_NOT_ENABLED_SANDBOX`.

Do not claim production-grade durable dedupe yet.

## 8. Structured response

Deterministic JSON accept/reject contract (see Client Ops programmer extension doc). No secret leakage.

## 9. Sandbox-first rule

Generate local template → offline harness → inactive create → re-GET → Phase 1B-B1 auth binding → Phase 1B-B2 authenticated POST → only later Telegram / production activation under separate charters.

## 10. No Telegram in first create

Telegram is a separated gate.

## 11. No operator manual node assembly

MetaBOT / Cursor programmer must generate and apply workflow JSON. Manual n8n UI assembly is **NOT ACCEPTED**.

## 12. Experience capture requirement

After first sandbox apply, update `projects/client-ops-reporting-bridge/n8n/experience-pack/` with create/re-GET facts. Phase 1B-B captured inactive-create experience; Phase 1B-B1 captured native auth binding; Phase 1B-B2 captured authenticated POST / activation containment; Telegram remains incomplete.

## Remaining gaps (SAFE UNKNOWN)

- Exact n8n application version.
- Data Store availability.
- Workflow-level HTTP 413 for oversized bodies (observed native 422 parse before size gate).
- Production durable dedupe store choice.
