# Architecture — MARS Client Ops Reporting Bridge

**Status:** DOCUMENTATION-ONLY / PHASE 0A  
**Implementation:** NOT IMPLEMENTED

---

## 1. Purpose

Define producer / contract / consumer boundaries for a future reporting chain from SITE/OCPilot monitor artifacts to Telegram (SIMPLE), optional AI commentary, and optional Hub Gateway.

---

## 2. Architecture diagram (ASCII)

```text
+---------------------+     +------------------------+     +---------------------------+
| OCPilot / SITE      |     | Shared contract (docs) |     | MetaBOT / n8n (FUTURE)    |
| factual producer    |     | envelope + severity    |     | validate / normalize      |
| monitor artifacts   |---->| precedence + codes     |---->| dedupe / format / deliver |
| baseline facts      |     | (THIS PACK)            |     | retry / optional AI       |
+---------------------+     +------------------------+     +-------------+-------------+
         |                                                         |
         | NO Telegram / AI / routing ownership                    |
         v                                                         v
+---------------------+                               +---------------------------+
| Storage scheduled   |   Preferred MVP intake        | Telegram (FUTURE)         |
| monitor folder      |------------------------------>| transport + presentation  |
| (read-only source)  |   via future exporter         | NOT source of truth       |
+---------------------+                               +---------------------------+
                                                                  |
                                                                  v
                                                      +---------------------------+
                                                      | AI_COMMENT (FUTURE OPT)   |
                                                      | commentary only           |
                                                      | no severity authority     |
                                                      +---------------------------+
                                                                  |
                                                                  v
                                                      +---------------------------+
                                                      | Hub Gateway (FUTURE OPT)  |
                                                      | secondary consumer        |
                                                      | NO Phase 0A runtime claim |
                                                      +---------------------------+
```

**Alternative future flow (if n8n cannot read Storage):**

```text
scheduled monitor folder
  → future local read-only exporter
  → authenticated POST to protected n8n webhook
  → same validation / normalize / SIMPLE path
```

Phase 0A implements **neither** preferred file intake nor webhook intake.

---

## 3. Layer boundaries

| Layer | Responsibility |
|-------|----------------|
| **OCPilot / SITE** | Produce monitor facts and baseline-related facts. Must not own Telegram, AI, routing, or client chat configuration. |
| **Shared contract** | Own report envelope, source authority, artifact precedence, severity normalization, cross-consumer semantics. |
| **MetaBOT / n8n** | Future intake, validation, normalization, deduplication, routing, formatting, delivery, retry, optional AI branch. |
| **Telegram** | Transport and presentation only. |
| **AI** | Optional commentary after immutable SIMPLE facts. |
| **Hub Gateway** | Future optional secondary consumer. |

---

## 4. Preferred MVP intake flow

1. Scheduled SITE monitor writes artifacts under Storage scheduled-monitors tree (existing SITE-002 pattern).
2. **Future** read-only exporter reads required artifacts, validates completeness/freshness, normalizes to `mars.client_ops.report` v1.
3. Exporter writes **sanitized atomic JSON** to a promoted location readable by n8n **or** (alternative) posts authenticated payload to a protected webhook.
4. **Future** n8n validates schema, deduplicates by `event_id`, maps SIMPLE template, sends internal Telegram.
5. Optional AI branch runs only after SIMPLE facts are ready; AI failure must not block SIMPLE.
6. Optional Hub Gateway later consumes the same normalized envelope.

---

## 5. Hard architectural rules

| Rule | Meaning |
|------|---------|
| **No direct production DB** | Reporting chain must not read production CMS DB for MVP site status. |
| **No site dependency on Telegram/AI** | SITE/monitor must remain useful if Telegram or AI is down. |
| **site_status first** | Determined before delivery and AI handling. |
| **Failure isolation** | Telegram failure → `delivery_status` only. AI failure → `ai_status` only. Neither mutates `site_status`. |
| **Sanitized envelope only** | No secrets, absolute artifact paths, raw logs, or stack traces in distributable payload. |
| **Consumer extensibility** | Additional consumers may attach downstream without changing SITE producer ownership. |

---

## 6. Status separation

| Status family | Vocabulary | Owner of truth |
|---------------|------------|----------------|
| **site_status** | OK, ATTENTION, FAILED, BLOCKED | Derived from source artifacts + shared severity rules |
| **delivery_status** | NOT_ATTEMPTED, SENT, RETRYING, FAILED | Consumer/runtime (n8n/Telegram path) |
| **ai_status** | DISABLED, NOT_REQUESTED, SUCCESS, FAILED | Consumer/runtime (optional AI path) |

Minimal SITE/exporter payload must **not** pretend Telegram or AI already executed. Downstream may extend envelope with delivery/AI fields after attempts; those fields are **not** required MVP producer fields.

See [SEVERITY-MODEL.md](SEVERITY-MODEL.md).

---

## 7. Maturity and non-claims

| Claim | Phase 0A truth |
|-------|----------------|
| Shared contract docs exist | **Yes** (this pack) |
| Exporter exists | **No** |
| Client Ops n8n workflow exists | **No** |
| Client Ops Telegram bot exists | **No** |
| AI_COMMENT path exists | **No** |
| Hub Gateway feed exists | **No** |
| SITE-002 production changed by this pack | **No** |

---

## 8. References

- MetaBOT execution boundary: `projects/metabot-seo-content-agent/integration-boundary.md`
- MetaBOT n8n discipline: `projects/metabot-seo-content-agent/n8n-project-development-rules-v1.md`
- SITE-002 monitor runbook: `projects/ocpilot/sites/site-002/runbooks/SITE-002-POST-1C-MONITOR-AUTOMATION-RUNBOOK.md`
- SITE-002 artifact hardening: `projects/ocpilot/sites/site-002/reports/SITE-002-POST-1C-MONITOR-ARTIFACTS-HARDENING-01.md`
- HomeGateway planned consumer posture: `projects/homegateway-v4-ai/OPERATIONAL-INDEX.md`
