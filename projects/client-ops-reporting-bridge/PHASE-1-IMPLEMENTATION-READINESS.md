# Phase 1 Implementation Readiness

**Status:** PHASE 1A + PROGRAMMER EXTENSION + PHASE 1B-B INACTIVE SANDBOX + PHASE 1B-B1 NATIVE AUTH BINDING COMPLETE / AUTH POST PENDING
**Phase 0A:** COMPLETE
**Phase 0B:** COMPLETE (documentation)
**Phase 1A:** COMPLETE (offline exporter core + fixtures + tests)
**Programmer extension:** COMPLETE
**Phase 1B-B inactive sandbox:** COMPLETE — see [PHASE-1B-B-INACTIVE-SANDBOX-WORKFLOW.md](PHASE-1B-B-INACTIVE-SANDBOX-WORKFLOW.md)
**Phase 1B-B1 native webhook auth binding:** COMPLETE — see [PHASE-1B-B1-NATIVE-WEBHOOK-AUTH-BINDING.md](PHASE-1B-B1-NATIVE-WEBHOOK-AUTH-BINDING.md)
**Phase 1B authenticated POST / Telegram / activation:** NOT STARTED — next charter is **Phase 1B-B2 Authenticated Sandbox POST Validation**; auth is now `AUTH_NATIVE_HEADER_CREDENTIAL_BOUND`

---

## 1. Current readiness state

| Area | State |
|------|-------|
| Phase 0A contract freeze | **COMPLETE** |
| Phase 0B implementation design + acceptance tests | **COMPLETE** (docs only) |
| Phase 1A offline exporter core | **COMPLETE** |
| MetaBOT Programmer Client Ops extension | **COMPLETE** (local only) |
| Workflow template | **CREATED LOCALLY** + used as create source |
| Offline n8n harness | **PASS** |
| Exporter transport / publication | **NOT STARTED** |
| n8n Client Ops workflow | **CREATED INACTIVE + AUTH BOUND** (`tkM4H0G0gM3q9Foi`; `AUTH_NATIVE_HEADER_CREDENTIAL_BOUND`) |
| Telegram Client Ops bot | **DOES NOT EXIST** / **NOT CONNECTED** |
| Profile A/B selection | **PROFILE_B_REQUIRED** (authoritative) |
| External credentials | **Local secret prepared** (gitignored); **n8n `httpHeaderAuth` credential created and bound** |
| Phase 1 production activation | **NOT APPROVED** |
| Production | **UNCHANGED** |

---

## 2. Completed prerequisites

- Shared envelope `mars.client_ops.report` v1 frozen.
- Artifact precedence frozen.
- Severity model frozen.
- SIMPLE templates frozen.
- AI_COMMENT restrictions frozen (Phase 2).
- SITE-002 intake assumptions documented.
- Phase 0B technical design pack created.
- Phase 1A offline exporter + 59 tests baseline.
- PROFILE_B decision frozen for Client Ops Bridge — bzpm.ru.
- Programmer extension: template, harness, gates, runbooks, experience-pack skeleton, MetaBOT knowledge doc.

---

## 3. Unresolved blockers (practical)

| Blocker | State |
|---------|-------|
| Auth secret binding syntax in live n8n Code@2 / native webhook header auth | **AUTH_NATIVE_HEADER_CREDENTIAL_BOUND** (native Webhook Header Auth; Code-level shared-secret comparison removed) |
| Exact n8n application version | **SAFE UNKNOWN** |
| Durable dedupe store for production | **OPEN** (sandbox = deferred) |
| Dedicated Client Ops Telegram bot approval | **Required before Telegram gate** |
| Exact internal test chat approval | **Required before Telegram send** |
| Future production activation approval | **Required before production** |

---

## 4. Operator decisions

### Already approved (do not re-ask)

| # | Decision | State |
|---|----------|-------|
| 3 | OK sends during Phase 1 validation period | **APPROVED** (design default) |
| 4 | Artifact precedence freeze | **APPROVED** |
| 5 | Phase 1 internal-only routing | **APPROVED** |
| — | Freshness SLA 26h (`93600`) | **APPROVED** |
| — | Clock skew tolerance `300` seconds | **APPROVED** |
| — | Transport profile for bzpm Bridge | **PROFILE_B_REQUIRED** |
| — | Manual n8n UI assembly | **NOT ACCEPTED** |

### Remaining

| # | Decision | State |
|---|----------|-------|
| — | Auth credential binding method in n8n | **AUTH_NATIVE_HEADER_CREDENTIAL_BOUND** — dedicated `httpHeaderAuth` credential created and bound; POST validation still pending |
| — | Approve dedicated Client Ops Telegram bot? | **RECOMMENDED** — approval required before external work |
| — | Approve exact internal test chat | Blocking before sandbox send |
| — | Approve production workflow activation | Blocking before L6 |
| — | Production dedupe store | Open after sandbox |

---

## 5. Recommended implementation profile

**PROFILE_B_REQUIRED** for `MARS Client Ops Bridge — bzpm.ru`.

Local exporter on operator workstation remains temporary. Long-term runtime must move toward n8n host, bzpm.ru hosting, or a justified split.

---

## 6. Files / modules

### Phase 1A (exists — offline only)

- `src/client_ops_reporting_bridge/`
- Synthetic `fixtures/`
- Offline `tests/`
- [PHASE-1A-OFFLINE-EXPORTER-CORE.md](PHASE-1A-OFFLINE-EXPORTER-CORE.md)

### Programmer extension (exists — local only)

- [CLIENT-OPS-PROGRAMMER-CAPABILITY-EXTENSION.md](CLIENT-OPS-PROGRAMMER-CAPABILITY-EXTENSION.md)
- `n8n/templates/`, `n8n/harness/`, `n8n/runbooks/`, `n8n/experience-pack/`, `n8n/runners/`

### Phase 1B (still future)

- Phase 1B-B inactive sandbox create completed (workflow `tkM4H0G0gM3q9Foi`, active=false)
- Next: Phase 1B-B1 auth binding intake (not yet started)
- Auth binding HITL
- Authenticated POST tests
- Telegram (separate gate)
- `push-webhook` exporter command (not in this extension)

---

## 7. Final readiness checklist

| Check | Ready? |
|-------|--------|
| Phase 0A docs accepted | Yes |
| Phase 0B design docs present | Yes |
| Phase 1A offline exporter + fixtures + tests | **Yes** |
| Profile selected | **Yes — PROFILE_B_REQUIRED** |
| Programmer extension local | **Yes** |
| Offline harness PASS | **Yes** |
| Sandbox workflow created | **Yes** (inactive; `tkM4H0G0gM3q9Foi`; `AUTH_NATIVE_HEADER_CREDENTIAL_BOUND`) |
| Auth binding resolved | **No** — next: Phase 1B-B1 Native Webhook Auth Binding Intake and Controlled Apply |
| Dedicated bot approved | **No** |
| Test chat approved | **No** |
| Production activation approved | **No** |
| Transport/publication implemented | **No** |

**Verdict:** Phase 1B-B inactive sandbox create is **COMPLETE**. Ready for **Phase 1B-B1 — Native Webhook Auth Binding Intake and Controlled Apply**. **Not** ready for authenticated POST validation, production activation, or Telegram.
