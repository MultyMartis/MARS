# Phase 1 Implementation Readiness

**Status:** PHASE 1A OFFLINE CORE COMPLETE + PROGRAMMER EXTENSION COMPLETE / PHASE 1B SANDBOX CREATE PENDING
**Phase 0A:** COMPLETE
**Phase 0B:** COMPLETE (documentation)
**Phase 1A:** COMPLETE (offline exporter core + fixtures + tests)
**Programmer extension:** COMPLETE (local template/harness/runbooks; not applied)
**Phase 1B:** NOT STARTED — **PROFILE_B_REQUIRED** frozen; inactive sandbox create is next charter

---

## 1. Current readiness state

| Area | State |
|------|-------|
| Phase 0A contract freeze | **COMPLETE** |
| Phase 0B implementation design + acceptance tests | **COMPLETE** (docs only) |
| Phase 1A offline exporter core | **COMPLETE** |
| MetaBOT Programmer Client Ops extension | **COMPLETE** (local only) |
| Workflow template | **CREATED LOCALLY, NOT APPLIED** |
| Offline n8n harness | **PASS** |
| Exporter transport / publication | **NOT STARTED** |
| n8n Client Ops workflow | **DOES NOT EXIST** / **NOT CREATED** |
| Telegram Client Ops bot | **DOES NOT EXIST** / **NOT CONNECTED** |
| Profile A/B selection | **PROFILE_B_REQUIRED** (authoritative) |
| External credentials | **ABSENT** from this programme (HITL binding pending) |
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
| Auth secret binding syntax in live n8n Code@2 | **HITL_REQUIRED / SAFE UNKNOWN** |
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
| — | Auth credential binding method in n8n | **HITL_REQUIRED** |
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

- Inactive sandbox create via Cursor programmer (next charter)
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
| Sandbox workflow created | **No** |
| Auth binding resolved | **No** |
| Dedicated bot approved | **No** |
| Test chat approved | **No** |
| Production activation approved | **No** |
| Transport/publication implemented | **No** |

**Verdict:** Programmer capability extension is **COMPLETE** locally. Ready for **Phase 1B-B Inactive Sandbox Workflow Generation** charter. **Not** ready for production activation or Telegram.
