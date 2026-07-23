# MARS Client Ops Reporting Bridge

**Subsystem name:** MARS Client Ops Reporting Bridge
**Status:** PHASE 0A/0B COMPLETE + PHASE 1A OFFLINE EXPORTER CORE COMPLETE + PROGRAMMER CAPABILITY EXTENSION COMPLETE
**Implementation status:** Phase 1A offline exporter core + fixtures + tests **COMPLETE**; MetaBOT programmer Client Ops extension (template/harness/runbooks) **COMPLETE LOCALLY**; n8n sandbox workflow / webhook / Telegram / Storage publication **NOT STARTED / NOT APPLIED**
**Production state:** UNCHANGED
**Transport decision:** **PROFILE_B_REQUIRED** (authoritative for next sandbox create)
**Future n8n workflow name:** `MARS Client Ops Bridge — bzpm.ru`
**Canonical locus:** `projects/client-ops-reporting-bridge/`
**Registry:** `project_id` **not registered** — programme locus only (registry mutation not authorized)

---

## Purpose

Freeze a shared documentation contract and Phase 0B technical design for a **future** client-site operational reporting chain:

```text
SITE / OCPilot monitor artifacts
  → future read-only exporter
  → sanitized report envelope v1
  → future n8n validation / deduplication
  → future Telegram SIMPLE delivery
  → optional future AI_COMMENT
  → future Hub Gateway consumer
```

Phase 0A freezes the contract. Phase 0B freezes implementation-ready design and acceptance tests so a later Phase 1 charter can build without reopening architecture.

---

## Non-goals (Phase 0A / 0B)

- No exporter implementation or executable stub presented as runtime.
- No n8n workflow create/edit/access.
- No Telegram bot create/edit/send.
- No webhook, public endpoint, or credential addition.
- No OpenRouter / AI API calls.
- No Hub Gateway integration.
- No SITE-002 monitor, scheduler, or baseline mutation.
- No Storage artifact mutation / promoted directory creation.
- No production writes (FTP/SFTP/SSH/DB/REST write).
- No registry, governance, MetaBOT, OCPilot, or HomeGateway edits outside this locus.

---

## Ownership boundaries

| Layer | Owns | Must not own |
|-------|------|----------------|
| **OCPilot / SITE** | Monitor facts; baseline-related facts; factual report producer inputs | Telegram; AI; routing; client chat configuration |
| **Shared contract (this pack)** | Report envelope; source authority; artifact precedence; severity normalization; cross-consumer semantics | Live delivery; credentials; runtime |
| **MetaBOT / n8n (future)** | Intake, validation, deduplication, routing, formatting, delivery, retry, optional AI branch | SITE/monitor truth; baseline authority |
| **Telegram (future)** | Transport and presentation only | Source of truth |
| **AI (future optional)** | Short commentary after immutable SIMPLE facts | Facts, severity, actions, production decisions |
| **Hub Gateway (future optional)** | Secondary consumer of normalized envelope | Phase 0A/0B runtime claim |

---

## Current phase

| Field | Value |
|-------|-------|
| **Phase 0A — Contract freeze** | **COMPLETE** |
| **Phase 0B — Implementation design** | **COMPLETE** (documentation) |
| **Phase 1A — Offline exporter core** | **COMPLETE** (fixture-driven; no production/network) |
| **MetaBOT Programmer Client Ops extension** | **COMPLETE** (local template/harness/runbooks; not applied) |
| **Phase 1B — Transport / publication** | **NOT STARTED** — profile frozen as **PROFILE_B_REQUIRED**; sandbox create pending next charter |
| **n8n Client Ops workflow** | **NOT CREATED** (local inactive template only) |
| **Telegram** | **NOT CONNECTED** |
| **Production** | **UNCHANGED** |
| **Exporter (offline)** | Exists under `src/client_ops_reporting_bridge/` |
| **Exporter (publish/push)** | Does not exist (`push-webhook` not implemented) |
| **AI_COMMENT runtime** | Does not exist |
| **Hub Gateway feed** | Does not exist |
| **PROFILE A vs B** | **PROFILE_B_REQUIRED** frozen for Client Ops Bridge — bzpm.ru |

**Explicit statement:** Phase 1A is offline-only. Programmer extension adds local n8n template/harness only. No live n8n workflow, webhook call, Telegram bot, Storage publication, or production exporter service is claimed. See [PHASE-1A-OFFLINE-EXPORTER-CORE.md](PHASE-1A-OFFLINE-EXPORTER-CORE.md) and [CLIENT-OPS-PROGRAMMER-CAPABILITY-EXTENSION.md](CLIENT-OPS-PROGRAMMER-CAPABILITY-EXTENSION.md).

---

## Document map

### Phase 0A — Contract freeze

| Document | Role |
|----------|------|
| [ARCHITECTURE.md](ARCHITECTURE.md) | Boundaries, flows, failure isolation |
| [REPORT-CONTRACT-V1.md](REPORT-CONTRACT-V1.md) | Frozen sanitized report envelope v1 |
| [ARTIFACT-AUTHORITY-AND-PRECEDENCE.md](ARTIFACT-AUTHORITY-AND-PRECEDENCE.md) | Source artifact authority and conflict rules |
| [SEVERITY-MODEL.md](SEVERITY-MODEL.md) | OK / ATTENTION / FAILED / BLOCKED |
| [TELEGRAM-SIMPLE-TEMPLATES.md](TELEGRAM-SIMPLE-TEMPLATES.md) | Deterministic SIMPLE rendering |
| [AI-COMMENT-CONTRACT.md](AI-COMMENT-CONTRACT.md) | Optional AI commentary restrictions |
| [PHASE-1-MVP-GATES.md](PHASE-1-MVP-GATES.md) | Blockers and approval gates |
| [SITE-002-MVP-INTAKE.md](SITE-002-MVP-INTAKE.md) | SITE-002 evidence and assumptions |
| [ROADMAP.md](ROADMAP.md) | Phased implementation roadmap |

### Phase 0B — Implementation design

| Document | Role |
|----------|------|
| [IMPLEMENTATION-DESIGN-V1.md](IMPLEMENTATION-DESIGN-V1.md) | End-to-end Phase 1 technical design; PROFILE A/B |
| [EXPORTER-DESIGN-V1.md](EXPORTER-DESIGN-V1.md) | Future read-only exporter design |
| [PROMOTED-ARTIFACT-PROTOCOL-V1.md](PROMOTED-ARTIFACT-PROTOCOL-V1.md) | Promoted Storage layout and atomicity |
| [NORMALIZATION-ALGORITHM-V1.md](NORMALIZATION-ALGORITHM-V1.md) | Deterministic normalization algorithm |
| [EVENT-ID-AND-DEDUPE-V1.md](EVENT-ID-AND-DEDUPE-V1.md) | Deterministic event_id and dedupe |
| [N8N-WORKFLOW-DESIGN-V1.md](N8N-WORKFLOW-DESIGN-V1.md) | Future isolated n8n workflow design |
| [ACCEPTANCE-TEST-PLAN-V1.md](ACCEPTANCE-TEST-PLAN-V1.md) | L0–L7 acceptance tests (not executed in 0B) |
| [TEST-FIXTURES-SPEC-V1.md](TEST-FIXTURES-SPEC-V1.md) | Fixture specification (no raw prod copies) |
| [FAILURE-RETRY-AND-ROLLBACK-V1.md](FAILURE-RETRY-AND-ROLLBACK-V1.md) | Failure, retry, disable/rollback |
| [PHASE-1-IMPLEMENTATION-READINESS.md](PHASE-1-IMPLEMENTATION-READINESS.md) | Readiness and remaining decisions |

### Phase 1A — Offline exporter core

| Document / path | Role |
|-----------------|------|
| [PHASE-1A-OFFLINE-EXPORTER-CORE.md](PHASE-1A-OFFLINE-EXPORTER-CORE.md) | Phase 1A scope, CLI, tests, limitations |
| `src/client_ops_reporting_bridge/` | Offline Python exporter core |
| `fixtures/` | Sanitized synthetic fixtures |
| `tests/` | Offline unittest suite |

### Programmer capability extension (local, not applied)

| Document / path | Role |
|-----------------|------|
| [CLIENT-OPS-PROGRAMMER-CAPABILITY-EXTENSION.md](CLIENT-OPS-PROGRAMMER-CAPABILITY-EXTENSION.md) | Extension status, decisions, next charter |
| `n8n/templates/` | Inactive sandbox workflow template (not applied) |
| `n8n/harness/` | Offline Node validation harness |
| `n8n/runbooks/` | Pre-create gates, create design, apply/rollback |
| `n8n/experience-pack/` | Skeleton experience pack |
| `n8n/runners/` | Greenfield create runner skeleton (not executed) |
| MetaBOT knowledge | `projects/metabot-seo-content-agent/metabot-developer/client-ops-n8n-extension-v1.md` |

---

## Related programmes (reference only)

| Programme | Path | Relationship |
|-----------|------|----------------|
| OCPilot | `projects/ocpilot/` | SITE monitor producer lane |
| SITE-002 | `projects/ocpilot/sites/site-002/` | First MVP site evidence |
| MetaBOT | `projects/metabot-seo-content-agent/` | Future n8n / Telegram / AI patterns |
| HomeGateway | `projects/homegateway-v4-ai/` | Future optional Hub Gateway consumer (planned / draft) |
| Shared contracts | `shared/contracts/` | Sibling shared-rule pattern (ATLAS/groundtruth) |

Do **not** treat related programme docs as proof that Client Ops Reporting Bridge runtime exists.

---

## Honesty boundary

- **Documented architecture:** Phase 0A pack.
- **Documented implementation design:** Phase 0B pack.
- **Implemented offline core:** Phase 1A — fixture validate/build only; not production runtime.
- **Planned transport:** Phase 1B+ (publication, n8n, Telegram) — **not** started.
- **Legacy / external:** MetaBOT live n8n and SITE-002 monitor tooling exist in their own lanes; this bridge does **not** wrap them yet.
