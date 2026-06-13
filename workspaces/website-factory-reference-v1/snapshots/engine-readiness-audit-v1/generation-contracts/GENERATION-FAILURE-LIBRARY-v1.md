# Website Factory — Generation Failure Library v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/generation-contracts/`  
**Статус:** failure taxonomy — **documentation only**  
**Связь:** [GENERATION-CONTRACT-v1.md](GENERATION-CONTRACT-v1.md), [GENERATION-GATES-v1.md](GENERATION-GATES-v1.md)

**Не является:** automated error codes, Sentry taxonomy, CI exit codes.

---

## Severity legend

| Level | Meaning |
|-------|---------|
| **CRITICAL** | Halt — no Generation Ready; may set contract `FAILED` |
| **ERROR** | Must fix before Generation Ready |
| **WARNING** | Document operator exception; may proceed with `PASS_WITH_WARNINGS` upstream only |

---

## Failure catalogue

### GEN-F01 — Missing blueprint

| Field | Value |
|-------|-------|
| **Cause** | No `blueprint_ref` for `site_type_code` or wrong blueprint type |
| **Impact** | Cannot define pages, blocks, or downstream specs |
| **Severity** | CRITICAL |
| **Correction** | Select canonical Core blueprint or reclassify; Extended requires charter |

---

### GEN-F02 — Missing page contract

| Field | Value |
|-------|-------|
| **Cause** | Route in scope without PAGE-CONTRACT / `page_type` |
| **Impact** | Page Build Specification incomplete |
| **Severity** | CRITICAL |
| **Correction** | Instantiate page architecture per blueprint `required_pages` |

---

### GEN-F03 — Block validation fail

| Field | Value |
|-------|-------|
| **Cause** | Page Block Validation `FAIL` or CRITICAL missing/forbidden blocks |
| **Impact** | Block Stack Specification unreliable |
| **Severity** | CRITICAL |
| **Correction** | Fix stack; re-run VALIDATION-CONTRACT; achieve PASS |

---

### GEN-F04 — SEO unresolved

| Field | Value |
|-------|-------|
| **Cause** | Missing PAGE-SEO-CONTRACT or strategy gap for in-scope page |
| **Impact** | SEO Specification cannot be assembled |
| **Severity** | ERROR |
| **Correction** | Complete SEO profile per seo-architecture rules |

---

### GEN-F05 — Design unresolved

| Field | Value |
|-------|-------|
| **Cause** | Required block lacks `VF_*` binding or pattern conflicts with forbidden block |
| **Impact** | Design Specification incomplete |
| **Severity** | ERROR |
| **Correction** | Complete design mapping; remove conflicting pattern |

---

### GEN-F06 — Missing content signals

| Field | Value |
|-------|-------|
| **Cause** | Required `signal_id` not declared for in-scope block |
| **Impact** | Content Specification incomplete |
| **Severity** | ERROR |
| **Correction** | Bind signals per CONTENT-CONTRACT; re-approve Content gate |

---

### GEN-F07 — Content validation fail

| Field | Value |
|-------|-------|
| **Cause** | Content Validation `FAIL`, forbidden signal, or architecture mismatch |
| **Impact** | GATE_CONTENT_VALIDATION_PASS blocked |
| **Severity** | CRITICAL |
| **Correction** | Fix signal architecture per CONTENT-VALIDATION-RULES |

---

### GEN-F08 — Placeholder leakage

| Field | Value |
|-------|-------|
| **Cause** | Placeholder markers in legal, entity, or production-bound signals (e.g. `{{ENTITY_NAME}}` in non-draft gate) |
| **Impact** | False Generation Ready; production integrity risk |
| **Severity** | CRITICAL |
| **Correction** | Replace placeholders; re-run legal and content validation |

---

### GEN-F09 — Legal failure

| Field | Value |
|-------|-------|
| **Cause** | Missing legal route, Legal Pack drift, unapproved template change |
| **Impact** | GATE_LEGAL_PACK_PASS blocked |
| **Severity** | CRITICAL |
| **Correction** | Apply FROZEN Legal Pack workflow; operator legal review |

---

### GEN-F10 — Entity not verified

| Field | Value |
|-------|-------|
| **Cause** | Entity Card incomplete when PII/forms/legal identity required |
| **Impact** | GATE_ENTITY_CARD_READY blocked |
| **Severity** | CRITICAL |
| **Correction** | Complete Legal Entity Discovery; refresh entity card |

---

### GEN-F11 — Generation attempted before readiness

| Field | Value |
|-------|-------|
| **Cause** | Specification assembly or Frontend Handoff before GATE_GENERATION_READY |
| **Impact** | Downstream rework; drift from canon |
| **Severity** | CRITICAL |
| **Correction** | Halt handoff; complete gates GL-01–GL-11 |

---

### GEN-F12 — Scope drift

| Field | Value |
|-------|-------|
| **Cause** | Routes/blocks added after gate PASS without re-validation |
| **Impact** | Specs stale vs production intent |
| **Severity** | ERROR |
| **Correction** | New `generation_id` or re-run affected gates (inputs `STALE`) |

---

### GEN-F13 — Upstream dependency not accepted

| Field | Value |
|-------|-------|
| **Cause** | Layer marked PENDING (e.g. design/content not operator-accepted) |
| **Impact** | `required_dependencies` invalid |
| **Severity** | ERROR |
| **Correction** | Operator acceptance or document exception charter |

---

### GEN-F14 — Extended type without charter

| Field | Value |
|-------|-------|
| **Cause** | `site_type_code` ∈ Extended without blueprint/validation matrix |
| **Impact** | Generation scope SAFE UNKNOWN |
| **Severity** | CRITICAL |
| **Correction** | Reclassify to Core 5 or approve Extended charter |

---

### GEN-F15 — Handoff package incomplete

| Field | Value |
|-------|-------|
| **Cause** | OUT-06 missing one of OUT-01–OUT-05 for in-scope route |
| **Impact** | Frontend Layer blocked |
| **Severity** | ERROR |
| **Correction** | Complete specification assembly per GENERATION-OUTPUTS checklist |

---

## Mapping failures → contract status

| Severity mix | `status` |
|--------------|----------|
| Any CRITICAL open | `FAILED` or `BLOCKED` |
| ERROR open, no CRITICAL | `BLOCKED` |
| WARNING only, documented | `IN_PROGRESS` → may reach `READY` with operator note |
| All resolved | Proceed to `READY` |

---

*Generation Failure Library version: v1.*
