# Roadmap — MARS Client Ops Reporting Bridge

**Status:** PHASE 0A/0B + PHASE 1A + PROGRAMMER EXTENSION + PHASE 1B-B INACTIVE SANDBOX + PHASE 1B-B1 NATIVE AUTH BINDING COMPLETE
**Current completed phases:** Phase 0A/0B + Phase 1A offline exporter core + MetaBOT programmer Client Ops extension + Phase 1B-B inactive sandbox create + Phase 1B-B1 native webhook auth binding
**Remaining Phase 1B:** authenticated sandbox POST (1B-B2), Telegram, production activation — NOT STARTED

---

## Phase 0A — Contract freeze

| Item | Content |
|------|---------|
| **Goal** | Freeze shared documentation contract (envelope, precedence, severity, SIMPLE, AI restrictions, gates, SITE-002 intake) |
| **Allowed work** | Documentation under `projects/client-ops-reporting-bridge/` |
| **Forbidden work** | Exporter, n8n, Telegram, webhooks, AI calls, production/monitor/baseline/scheduler changes |
| **HITL gate** | Operator accepts Phase 0A pack |
| **Evidence required** | This documentation set present; production mutation counts remain zero |
| **Exit criteria** | Contract docs coherent; blockers listed; no runtime claimed |
| **State** | **COMPLETE** |

---

## Phase 0B — Implementation design

| Item | Content |
|------|---------|
| **Goal** | Convert Phase 0A contract into implementation-ready technical design + deterministic acceptance-test specification |
| **Allowed work** | Design docs under `projects/client-ops-reporting-bridge/`; PROFILE A and B designed without choosing without evidence |
| **Forbidden work** | Exporter code; n8n workflow JSON; Telegram/webhook/credentials; Storage directory creation; production activation; monitor/baseline mutation |
| **HITL gate** | Approve design + test plan; answer remaining operator decisions before implementation transfer work |
| **Evidence required** | Phase 0B design documents referencing Phase 0A contracts; dual-profile design; acceptance matrix |
| **Exit criteria** | Design complete; acceptance tests specified; remaining blockers explicit; **implementation not started** |
| **State** | **COMPLETE (design only)** |

### Phase 0B exit distinctions

| Distinction | State after Phase 0B |
|-------------|----------------------|
| Design complete | **Yes** |
| Implementation started | **No** |
| External credentials present | **No** (absent) |
| Profile A vs B selected | **Pending** n8n Storage access decision |
| Phase 1 ready to activate | **No** |

---

## Phase 1A — Offline exporter core

| Item | Content |
|------|---------|
| **Goal** | Fixture-driven offline normalize / envelope / security / event_id / SIMPLE render + tests |
| **Allowed work** | Code + fixtures + tests under `projects/client-ops-reporting-bridge/` |
| **Forbidden work** | Storage publication; webhook; n8n; Telegram; production/monitor/baseline/scheduler |
| **Evidence required** | Offline unittest pass; synthetic fixtures; no production mutations |
| **Exit criteria** | validate-only + build-envelope offline; contracts honored |
| **State** | **COMPLETE** — see [PHASE-1A-OFFLINE-EXPORTER-CORE.md](PHASE-1A-OFFLINE-EXPORTER-CORE.md) |

---

## Phase 1A-EXT — MetaBOT Programmer Client Ops capability extension

| Item | Content |
|------|---------|
| **Goal** | Repository-local programmer extension: template, harness, gates, runbooks, experience-pack skeleton |
| **Allowed work** | Docs/tools under `projects/client-ops-reporting-bridge/n8n/` + narrow MetaBOT developer knowledge doc |
| **Forbidden work** | Live n8n create/update/delete/activate; webhook POST; credentials; Telegram; Storage; push-webhook |
| **Evidence required** | Offline Node harness PASS; template gates PASS; Python suite still PASS |
| **Exit criteria** | Next charter can generate inactive sandbox workflow JSON without manual UI assembly |
| **State** | **COMPLETE (local only)** — see [CLIENT-OPS-PROGRAMMER-CAPABILITY-EXTENSION.md](CLIENT-OPS-PROGRAMMER-CAPABILITY-EXTENSION.md) |

---

## Phase 1B — Transport / publication (SITE-002 internal SIMPLE path)

| Item | Content |
|------|---------|
| **Goal** | SITE-002 internal operator SIMPLE delivery from normalized envelope |
| **Allowed work** | PROFILE_B authenticated webhook path; sandbox then HITL production n8n path; later internal Telegram SIMPLE |
| **Forbidden work** | Client routing; AI enablement (unless separately approved early — default no); baseline refresh; production site writes; manual n8n UI assembly |
| **HITL gate** | Inactive sandbox create → authenticated POST → Telegram → production activation |
| **Evidence required** | Sanitized envelopes; create/re-GET evidence; isolation tests; unchanged monitor/baseline/scheduler |
| **Exit criteria** | Internal SIMPLE reliable for OK/ATTENTION/FAILED/BLOCKED per send policy (OK always sends during validation) |
| **State** | **PARTIAL** — Phase 1B-B inactive sandbox created + Phase 1B-B1 native Header Auth bound (`AUTH_NATIVE_HEADER_CREDENTIAL_BOUND`); next recommended charter: Phase 1B-B2 — Authenticated Sandbox POST Validation |

---

## Phase 2 — AI_COMMENT

| Item | Content |
|------|---------|
| **Goal** | Optional AI commentary after immutable SIMPLE |
| **Allowed work** | AI branch using safe input shape; strict fallback |
| **Forbidden work** | AI authority over severity/action; raw artifact prompts; client AI copy without approval |
| **HITL gate** | Explicit AI enablement |
| **Evidence required** | Failure/timeout fallback tests; prohibited-behavior checks |
| **Exit criteria** | AI optional; SIMPLE never blocked by AI |

---

## Phase 3 — Client-ready routing

| Item | Content |
|------|---------|
| **Goal** | Separate client templates and routing |
| **Allowed work** | Client-safe templates; approved chat routing |
| **Forbidden work** | Reusing internal templates without approval; exposing internals |
| **HITL gate** | Per-client routing approval |
| **Evidence required** | Template approval record; sanitized delivery evidence |
| **Exit criteria** | Client path isolated from internal operator path |

---

## Phase 4 — Hub Gateway feed

| Item | Content |
|------|---------|
| **Goal** | Optional secondary consumer of normalized envelope |
| **Allowed work** | Feed/display integration design and later implementation under HomeGateway programme rules |
| **Forbidden work** | Making Hub Gateway a control plane; claiming runtime before evidence |
| **HITL gate** | HomeGateway / operator charter |
| **Evidence required** | Consumer contract mapping; no credential leakage |
| **Exit criteria** | Display/consume path documented and evidenced |

---

## Phase 5 — Multi-client template

| Item | Content |
|------|---------|
| **Goal** | Reusable multi-site reporting templates beyond SITE-002 |
| **Allowed work** | Parameterized site identity; shared severity/envelope reuse |
| **Forbidden work** | Assuming all sites share SITE-002 monitor artifact shapes without adapters |
| **HITL gate** | Per-site onboarding into bridge |
| **Evidence required** | Adapter notes; site-specific intake docs |
| **Exit criteria** | Second site proven without breaking SITE-002 |

---

## Non-claims

No phase beyond documentation (0A/0B) is implemented by this pack. Future phases require explicit charters. Phase 0B does **not** create runtime, credentials, workflows, or Storage directories.
