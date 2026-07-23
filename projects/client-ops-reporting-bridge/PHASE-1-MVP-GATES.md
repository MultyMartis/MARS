# Phase 1 MVP Gates

**Status:** DOCUMENTATION-ONLY / PHASE 0B DESIGN COMPLETE  
**Gate actions:** NOT IMPLEMENTED by this pack  
**Phase 1 readiness:** NOT READY until remaining blocking gates are satisfied

---

## 1. Decision register (Phase 0B update)

| # | Question | State | Notes |
|---|----------|-------|-------|
| 1 | Can the n8n host directly read `X:\AI MARS STORAGE`? | **BLOCKING SAFE UNKNOWN** | Primary architecture blocker — selects PROFILE A vs PROFILE B |
| 2 | Dedicated Telegram bot vs existing internal bot? | **RECOMMENDED: dedicated Client Ops bot**; operator approval required before external-system work | Bot does **not** exist yet; no credentials created |
| 3 | Suppress routine OK after initial validation period? | **APPROVED for Phase 1 validation:** OK **always sends**; suppression is a later policy option (not enabled) | Consumer-side policy |
| 4 | Is artifact precedence frozen exactly as documented? | **APPROVED** | See `ARTIFACT-AUTHORITY-AND-PRECEDENCE.md` + Phase 0B algorithm |
| 5 | Is Phase 1 routing confirmed internal-only? | **APPROVED** | No client routing before separate approval |
| — | Freshness SLA 26h (`93600` seconds) | **APPROVED** | `age_seconds = now_utc − observed_at` |
| — | Clock skew tolerance `300` seconds | **APPROVED** | Future `observed_at` → `SOURCE_TIME_INVALID` |

Do **not** re-ask decisions already marked APPROVED.

---

## 2. Primary architecture blocker — n8n ↔ Storage

**Most important remaining architecture blocker:** n8n access to Storage.

| If… | Then… |
|-----|-------|
| Direct access exists **and** is approved | **PROFILE A** — n8n consumes promoted atomic JSON file |
| Direct access does **not** exist | **PROFILE B** — local exporter POSTs authenticated payload to protected n8n webhook |
| Phase 0B | Designs **both**; implements **neither**; does **not** choose without evidence |

SAFE UNKNOWN until operator confirms host topology.

---

## 3. Preconditions

- Phase 0A contract pack accepted.
- Phase 0B design pack present (`IMPLEMENTATION-DESIGN-V1.md` and siblings).
- SITE-002 monitor remains unchanged unless a separate charter says otherwise.
- No production mutation from reporting-bridge work.
- Foreign WIP elsewhere in repo remains untouched.

---

## 4. Approval gates (ordered)

| Gate | Meaning | Evidence required | Rollback expectation |
|------|---------|-------------------|----------------------|
| **Documentation gate** | Contract pack reviewed | Operator acceptance of Phase 0A docs | Docs-only revert; no runtime |
| **Exporter design gate** | Phase 0B design of read-only exporter | Design docs + acceptance test plan (**satisfied as docs**) | No deploy |
| **n8n Storage / profile gate** | Answer question #1; select PROFILE A or B | Operator topology attestation | N/A until implement |
| **n8n sandbox gate** | Sandbox workflow only | Sanitized export / operator attestation; no prod activate | Disable/delete sandbox workflow |
| **Telegram credential gate** | Dedicated bot approval + credential placement | Operator credential placement in n8n only; no secrets in Git | Rotate/revoke token externally |
| **First sandbox message gate** | First SIMPLE message to **approved** internal test chat | Screenshot/transcript sanitized | Stop sending; disable workflow |
| **Production workflow activation gate** | Explicit HITL to activate | Apply manifest + rollback plan (MetaBOT discipline) | Deactivate workflow; preserve SITE monitor |

**No client routing before separate approval.**

**Do not mark Phase 1 ready** until Storage/profile, bot approval, test chat, and production activation gates that apply are satisfied.

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

- Phase 0B readiness: `PHASE-1-IMPLEMENTATION-READINESS.md`
- MetaBOT n8n rules: `projects/metabot-seo-content-agent/n8n-project-development-rules-v1.md`
- MetaBOT integration boundary: `projects/metabot-seo-content-agent/integration-boundary.md`
- MetaBOT production apply/rollback discipline: recent `reports/REPORT-metabot-seo-agent-v14-*-production-apply.md` patterns (reference only; do not mutate MetaBOT in Phase 0B)
