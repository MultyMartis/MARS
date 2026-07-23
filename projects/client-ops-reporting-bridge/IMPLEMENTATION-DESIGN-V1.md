# Implementation Design v1 — MARS Client Ops Reporting Bridge

**Status:** DESIGN ONLY / PHASE 0B COMPLETE  
**Implementation:** NOT STARTED  
**Runtime:** does not exist  
**Depends on:** Phase 0A contract freeze (`REPORT-CONTRACT-V1.md`, `ARTIFACT-AUTHORITY-AND-PRECEDENCE.md`, `SEVERITY-MODEL.md`, related)

---

## 1. Purpose

Convert the Phase 0A frozen contract into an implementation-ready technical design for the future Phase 1 chain:

```text
SITE-002 existing scheduled monitor artifacts
  → future separate read-only exporter
  → sanitized atomic report envelope v1
  → future n8n intake
  → validation
  → normalization trust boundary (envelope-only)
  → deduplication
  → Telegram SIMPLE
  → optional later AI_COMMENT
```

This document must allow a later implementation charter to build the exporter and n8n workflow **without reopening** architectural decisions frozen in Phase 0A and approved design freezes in Phase 0B.

---

## 2. Scope

| In scope (design) | Out of scope (this phase) |
|-------------------|---------------------------|
| Common Phase 1 technical flow | Executable exporter / CLI |
| PROFILE A (file pull) and PROFILE B (authenticated push) | Choosing PROFILE A vs B without operator evidence |
| Exporter / promoted artifact / n8n / Telegram responsibilities | Live n8n workflow JSON |
| Failure isolation and configuration boundaries | Telegram bot creation or credentials |
| Implementation order and acceptance boundary | SITE-002 production / monitor / baseline changes |
| Hub Gateway transport-neutral compatibility notes only | Hub Gateway implementation |

---

## 3. Non-goals

- No production connection, FTP/SFTP/SSH, DB, or REST write.
- No monitor execution, 1C import, scheduler or baseline mutation.
- No exporter code, validator executables, n8n workflow, webhook, or Telegram send.
- No client chat routing, client-safe templates, or public reports in Phase 1.
- No AI enablement in Phase 1 (attachment point only).
- No invention of project IDs, ATLAS IDs, workflow IDs, bot identities, or endpoints as live resources.

---

## 4. System boundaries

| Layer | Owns | Must not own |
|-------|------|----------------|
| **OCPilot / SITE** | Source facts; monitor observations; baseline facts | Telegram, AI, routing, delivery status, client chat config |
| **Shared contract** | Envelope semantics, artifact authority, precedence, validation, normalization, severity | Live delivery, credentials |
| **Future read-only exporter** | Read immutable monitor artifacts; validate/normalize; emit sanitized atomic envelope | Production writes; monitor/scheduler/baseline writes |
| **MetaBOT / n8n (future)** | Envelope validation, dedupe, SIMPLE format, route/deliver, optional later AI | Recomputing site facts from raw monitor artifacts |
| **Telegram** | Transport only | Source of truth |
| **AI (future optional)** | Non-authoritative commentary | Facts, severity, actions |
| **Hub Gateway (future)** | Secondary consumer of same envelope | Phase 0B/1 control plane |

---

## 5. Component diagram (ASCII)

```text
+---------------------------+
| SITE-002 scheduled        |
| monitor run folder        |
| (immutable source)        |
+-------------+-------------+
              | read-only
              v
+---------------------------+
| Future exporter           |
| discover → validate →     |
| precedence → normalize →  |
| envelope → event_id →     |
| atomic publish / push     |
+------+-------------+------+
       |             |
       | PROFILE A   | PROFILE B
       v             v
+--------------+  +------------------+
| Promoted     |  | Authenticated    |
| Storage JSON |  | n8n webhook POST |
+------+-------+  +--------+---------+
       |                   |
       +---------+---------+
                 v
       +-------------------+
       | Future n8n        |
       | validate/dedupe/  |
       | SIMPLE/Telegram   |
       +---------+---------+
                 v
       +-------------------+
       | Internal Telegram |
       | (transport only)  |
       +-------------------+
```

---

## 6. Sequence diagram (common)

```text
Exporter                Promoted/Transfer           n8n                 Telegram
   |                          |                      |                     |
   | discover completed run   |                      |                     |
   | validate artifacts       |                      |                     |
   | normalize + event_id     |                      |                     |
   | publish/push envelope -->|                      |                     |
   |                          |---- intake --------->|                     |
   |                          |                      | validate/dedupe     |
   |                          |                      | format SIMPLE       |
   |                          |                      |---- send ---------->|
   |                          |                      | record delivery     |
   |                          |                      |  (not site_status)  |
```

No step mutates the source run folder.

---

## 7. Common flow (frozen order)

1. Discover candidate monitor run.
2. Confirm run folder is complete and not in progress.
3. Read required artifacts.
4. Validate completeness.
5. Parse JSON.
6. Apply source authority and precedence.
7. Detect contradictions.
8. Normalize site status.
9. Calculate freshness (`age_seconds = now_utc − observed_at`).
10. Build sanitized envelope.
11. Validate envelope (schema + security).
12. Generate deterministic `event_id`.
13. Publish atomically (by-run immutable file).
14. Transfer to n8n using selected profile.
15. Validate again in n8n.
16. Deduplicate.
17. Format SIMPLE.
18. Send to internal Telegram.
19. Record delivery result separately (`delivery_status` only).

---

## 8. PROFILE A — File pull

**Applicability:** n8n runs on or securely mounts approved Storage and may read the promoted path.

| Step | Owner | Behavior |
|------|-------|----------|
| Publish | Exporter | Atomic write under promoted Storage (see `PROMOTED-ARTIFACT-PROTOCOL-V1.md`) |
| Intake | n8n | Poll promoted `latest` / by-run path on schedule |
| Transfer secrets | Minimal | Filesystem ACL / host mount; no webhook auth |
| Dedupe | n8n + optional promoted `state/` | Same `event_id` rules |

**Not selected in Phase 0B** without operator evidence that n8n can read `X:\AI MARS STORAGE`.

---

## 9. PROFILE B — Authenticated push

**Applicability:** n8n cannot directly read Storage.

| Step | Owner | Behavior |
|------|-------|----------|
| Publish local | Exporter | Same atomic envelope locally (and/or promoted path for audit) |
| Transfer | Exporter | HTTPS POST to protected n8n webhook |
| Auth | Operator-configured credential reference | Reject unauthenticated requests |
| Intake | n8n webhook | Size limit, content-type check, replay/dedupe protection |

**Not selected in Phase 0B** without operator evidence. No webhook is created in Phase 0B.

---

## 10. Profile comparison (required)

| Dimension | PROFILE A — File pull | PROFILE B — Authenticated push |
|-----------|----------------------|--------------------------------|
| Host topology | n8n colocated with / mounts Storage | Exporter host can reach n8n over network |
| Storage accessibility | Required for n8n read of promoted path | Not required for n8n; exporter needs source Storage |
| Secret needs | Filesystem permissions | Webhook auth secret + TLS |
| Network exposure | Low (local FS) | Webhook surface (must be protected) |
| Scheduler impact | Exporter schedule + n8n poll | Exporter schedule; n8n event-driven |
| Exporter complexity | Publish file | Publish + HTTP client + retry |
| n8n trigger complexity | File poll | Webhook + auth gates |
| Retry | Re-read same file / re-poll | Idempotent POST with same `event_id` |
| Dedupe | Same envelope `event_id` | Same envelope `event_id` |
| Auditability | Strong (immutable by-run files) | Needs request/response evidence store |
| Portability | Tied to Storage mount | More host-flexible |
| Security | ACL-centric | Auth + size + schema gates |
| Operational failure modes | Mount loss, poll lag | Network/auth outage, webhook downtime |
| Recommended use | **Preferred when** n8n has approved Storage access | **Preferred when** direct access unavailable |

**Shared components (both profiles):** normalization algorithm, envelope schema, `event_id`, SIMPLE templates, severity rules, security rejection, delivery isolation.

**Conditional choice rule:** PROFILE A preferred when n8n has approved direct access to promoted Storage; otherwise PROFILE B. Both use the same envelope and normalization. Neither modifies SITE-002 production or the current monitor.

---

## 11. Responsibility summary

| Component | Responsibility |
|-----------|----------------|
| **Exporter** | Discover completed runs; read-only normalize; validate; atomic publish/push; structured internal logs; never mutate source |
| **Promoted artifacts** | Immutable by-run envelopes; latest pointer/file; failed/archive/state layouts |
| **n8n** | Independent envelope validation; dedupe; SIMPLE; internal Telegram; delivery status; failure branches |
| **Telegram** | Deliver rendered text; transport failures → `delivery_status` only |

---

## 12. Source truth isolation

- Source run folder under existing SITE-002 scheduled-monitor path remains authoritative for **monitor facts**.
- Exporter never writes into the source run folder.
- Envelope never embeds absolute source paths.
- n8n must not recompute site facts from raw monitor artifacts.

---

## 13. Failure isolation

| Failure class | Affects | Must not affect |
|---------------|---------|-----------------|
| Source/artifact trust | `site_status` / summary codes | Telegram existence |
| Telegram send | `delivery_status` | `site_status` |
| AI (future) | `ai_status` | `site_status`, SIMPLE delivery |
| Storage/n8n infra after envelope built | delivery/publication outcome | Rewriting already-normalized site facts |

---

## 14. Configuration boundaries

| Config class | Examples | Location (design) |
|--------------|----------|-------------------|
| Site identity | `site_id`, display name, domain | Exporter config (non-secret) |
| Freshness | `stale_after_seconds = 93600` | Shared policy constant |
| Clock skew | `max_future_skew_seconds = 300` | Shared policy constant |
| Display timezone | `Europe/Moscow` for SITE-002 Phase 1 render | n8n / formatter config |
| Routing | Internal chat destination | n8n credential store only |
| Profile mode | A or B | Operator decision gate |

---

## 15. Secret boundaries

- No tokens, chat IDs, webhook secrets, or credential IDs in Git docs as live values.
- Credentials live only in n8n credential store / host secret store.
- Distributable envelope must have `security.contains_secrets=false` and `security.redacted=true`.

---

## 16. Runtime assumptions (DESIGN ONLY)

- SITE-002 scheduled monitor continues to produce hardened artifacts independently.
- Exporter is a **separate** future process (not inlined into the monitor).
- Phase 1 target is **internal operator Telegram only**.
- During Phase 1 validation period: OK, ATTENTION, FAILED, BLOCKED **always send**.
- Routine OK suppression is a **later policy option**, not enabled in Phase 1 design.
- Dedicated Client Ops Telegram bot is the **recommended** assumption; requires operator approval before external-system work. Bot does **not** exist because of this document.

---

## 17. Startup / preflight assumptions (future exporter)

Future exporter preflight (when implemented) must verify:

- Config present and profile selected.
- Source root readable.
- Promoted root writable (PROFILE A / local publish) without writing into source root.
- Clock usable (UTC).
- Dry-run mode available.

No Windows Task Scheduler task is authorized by Phase 0B.

---

## 18. Disable / rollback concepts

- Disable n8n workflow.
- Stop exporter task (when one exists).
- Leave source monitor untouched.
- Preserve last published envelope.
- Do not roll back baseline.
- Do not modify SITE-002 production.
- Restore previous workflow export only through accepted MetaBOT apply/rollback procedure.

Details: `FAILURE-RETRY-AND-ROLLBACK-V1.md`.

---

## 19. Implementation order (future)

1. Offline fixtures + normalization unit acceptance.
2. Exporter validate-only / build-envelope against fixtures.
3. Atomic publish into **isolated test** Storage folder.
4. n8n sandbox intake without Telegram.
5. n8n sandbox Telegram to approved internal test chat.
6. Controlled production activation (HITL).
7. Multi-day observation.

See `ACCEPTANCE-TEST-PLAN-V1.md` levels L0–L7. Phase 0B executes **none**.

---

## 20. Acceptance boundary

Phase 0B is complete when design docs exist and operator decisions remaining are explicitly listed. Phase 1 is **not** ready until remaining blocking gates in `PHASE-1-IMPLEMENTATION-READINESS.md` are satisfied.

---

## 21. Hub Gateway compatibility (transport-neutral)

Future Hub Gateway may consume the same `mars.client_ops.report` envelope as a secondary reader. Phase 0B does **not** design Hub Gateway integration beyond: same sanitized envelope; no SITE ownership change; no Phase 1 delivery dependency on Hub Gateway.
