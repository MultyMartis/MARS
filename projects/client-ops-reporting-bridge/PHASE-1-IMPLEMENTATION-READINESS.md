# Phase 1 Implementation Readiness

**Status:** PHASE 1A OFFLINE CORE COMPLETE / PHASE 1B BLOCKED  
**Phase 0A:** COMPLETE  
**Phase 0B:** COMPLETE (documentation)  
**Phase 1A:** COMPLETE (offline exporter core + fixtures + tests)  
**Phase 1B:** NOT STARTED / BLOCKED pending remaining operator/external decisions

---

## 1. Current readiness state

| Area | State |
|------|-------|
| Phase 0A contract freeze | **COMPLETE** |
| Phase 0B implementation design + acceptance tests | **COMPLETE** (docs only) |
| Phase 1A offline exporter core | **COMPLETE** |
| Exporter transport / publication | **NOT STARTED** |
| n8n Client Ops workflow | **DOES NOT EXIST** / **NOT CREATED** |
| Telegram Client Ops bot | **DOES NOT EXIST** / **NOT CONNECTED** |
| Profile A/B selection | **PENDING** n8n Storage access evidence |
| External credentials | **ABSENT** from this programme |
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
- Phase 0B technical design pack created:
  - implementation design
  - exporter design
  - promoted artifact protocol
  - normalization algorithm
  - event id / dedupe
  - n8n workflow design
  - acceptance tests
  - fixture spec
  - failure/retry/rollback

---

## 3. Unresolved blockers (practical)

| Blocker | State |
|---------|-------|
| Can n8n read `X:\AI MARS STORAGE`? | **BLOCKING SAFE UNKNOWN** |
| Dedicated Client Ops Telegram bot approval (+ later credential creation) | **Recommended; operator approval required** |
| Exact internal test chat approval | **Required before L5** |
| Future production activation approval | **Required before L6** |

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

### Remaining

| # | Decision | State |
|---|----------|-------|
| 1 | Can n8n read `X:\AI MARS STORAGE`? | **BLOCKING** — selects PROFILE A vs B |
| 2 | Approve dedicated Client Ops Telegram bot? | **RECOMMENDED** — approval required before external work |
| — | Approve exact internal test chat | Blocking before sandbox send |
| — | Approve production workflow activation | Blocking before L6 |

---

## 5. Recommended implementation profile

| If | Then |
|----|------|
| n8n has approved direct Storage access | **PROFILE A** preferred |
| n8n cannot read Storage | **PROFILE B** preferred |
| Unknown | **Do not implement transfer layer yet**; may still begin offline exporter normalize against fixtures |

Both profiles share envelope + normalization. Neither modifies SITE-002 production/monitor.

---

## 6. Files / modules

### Phase 1A (exists — offline only)

- `src/client_ops_reporting_bridge/` — validate-only / build-envelope
- Normalization implementing `NORMALIZATION-ALGORITHM-V1.md` (offline)
- Synthetic `fixtures/` tree
- Offline `tests/` suite
- [PHASE-1A-OFFLINE-EXPORTER-CORE.md](PHASE-1A-OFFLINE-EXPORTER-CORE.md)

### Phase 1B (still future — not started)

- Profile-required `publish-file` / `push-webhook`
- Isolated test promoted folder (not production root until approved)
- Separate n8n workflow (sandbox then production)
- Sanitized exports/evidence under programme reports (future)

---

## 7. External-system work expected (after approvals)

- Confirm n8n host topology / Storage mount.
- Create dedicated Telegram bot **only after approval**.
- Place credentials in n8n credential store only.
- Create sandbox workflow; later HITL production apply per MetaBOT rules.
- PROFILE B only: create protected webhook **after** design approval.

---

## 8. Required credential categories (no values)

- Telegram Bot token (Client Ops)
- Telegram destination (internal / test) as credential field — never in Git
- PROFILE B: webhook authentication secret
- No OpenRouter for Phase 1

---

## 9. Acceptance gates

See `PHASE-1-MVP-GATES.md` and `ACCEPTANCE-TEST-PLAN-V1.md` L0–L7.

Phase 1 is **not** ready until remaining blocking gates are satisfied.

---

## 10. Rollback readiness

Documented in `FAILURE-RETRY-AND-ROLLBACK-V1.md`. Must be accepted before L6.

---

## 11. Implementation order (recommended)

1. ~~Fixtures + L1 normalization.~~ **DONE (Phase 1A)**
2. ~~Exporter validate-only / build-envelope.~~ **DONE (Phase 1A)**
3. L3 isolated atomic publish — **Phase 1B**
4. Operator Storage/n8n decision → select profile — **BLOCKING**
5. L4 n8n sandbox intake — **Phase 1B**
6. Bot + test chat approvals → L5 — **Phase 1B**
7. L6 HITL production activation — **Phase 1B**
8. L7 multi-day observation (OK always sends during validation) — **Phase 1B**

---

## 12. No-go conditions

- Any requirement to mutate SITE-002 production/monitor/baseline/scheduler to “make reporting work”.
- Missing profile decision when attempting transfer integration.
- Credentials committed to Git.
- Client routing requested inside Phase 1 charter.
- Claiming Hub Gateway / AI runtime as Phase 1 deliverables without separate charter.

---

## 13. Final readiness checklist

| Check | Ready? |
|-------|--------|
| Phase 0A docs accepted | Yes (contract freeze) |
| Phase 0B design docs present | Yes |
| Phase 1A offline exporter + fixtures + tests | **Yes** |
| n8n Storage access answered | **No** |
| Profile selected | **No** |
| Dedicated bot approved | **No** |
| Test chat approved | **No** |
| Production activation approved | **No** |
| Transport/publication implemented | **No** |
| Workflow exists | **No** |

**Verdict:** Phase 1A offline core is **COMPLETE**. Ready for **operator profile decisions** before any Phase 1B charter. **Not** ready for production activation or Telegram/n8n work.
