# MARS Search PPC Production Lifecycle — Operator Decision v1

**Decision ID:** `MARS-SEARCH-PPC-PRODUCTION-LIFECYCLE-OPERATOR-DECISION-v1`  
**Date:** 2026-06-22  
**Status:** `APPROVED — IMPLEMENTATION AUTHORIZED`  
**Wave 1 authorization:** [WAVE-1-OPERATOR-APPROVAL-v1.md](./WAVE-1-OPERATOR-APPROVAL-v1.md)  
**Canonical authority:** [MARS-SEARCH-PPC-PRODUCTION-LIFECYCLE-v1.md](../MARS-SEARCH-PPC-PRODUCTION-LIFECYCLE-v1.md)

---

## Decision summary

Оператору предлагается утвердить **MARS Search PPC Production Lifecycle v1** как обязательную кросс-системную модель создания поисковых рекламных кампаний Яндекс Директа для всех новых проектов MARS.

До утверждения статус остаётся **PROPOSED**. Автоматическое утверждение агентом **запрещено**.

---

## Записываемые решения

### 1. Lifecycle authority

| Item | Decision |
|------|----------|
| Canonical locus | `projects/mars-search-ppc-production/` |
| Primary document | `MARS-SEARCH-PPC-PRODUCTION-LIFECYCLE-v1.md` |
| Machine contract | `contracts/mars-search-ppc-lifecycle-contract-v1.json` |
| Subsystem rule | Одна каноническая authority; локальные docs — ответственность + ссылки, без полного дублирования lifecycle |

**Operator action:** APPROVE / REJECT / REQUEST CHANGES

---

### 2. Twenty-three stages (SPPC-01 … SPPC-23)

Обязательная последовательность от Business Intake до Post-Launch Learning.

| Gate | Rule |
|------|------|
| Advancement | Только при `COMPLETED` или `COMPLETED WITH APPROVED DEGRADATION` предшествующих стадий с зарегистрированными артефактами |
| Blocked behavior | STOP → `BLOCKED` → перечень missing inputs → owning system/role → без подмены данных |
| Report alone | Недостаточен для completion |

**Operator action:** APPROVE stage list / REQUEST stage edits

---

### 3. Full-corpus principle (SPPC-03)

| Allowed | Forbidden |
|---------|-----------|
| Полный предоставленный корпус | 200-phrase P0-I pilot как production corpus |
| Subsets для validation/benchmark/pilot/diagnostics | Удобные ручные срезы, только high-frequency, pre-filtered commercial |

**P0-I pilot status:** `TECHNICAL INTEGRATION EVIDENCE` — [ORCA-P0-I-PILOT-RECLASSIFICATION-DECISION-v1](../../orca/semantic-intelligence/integration/decisions/ORCA-P0-I-PILOT-RECLASSIFICATION-DECISION-v1.md)

**Operator action:** APPROVE full-corpus rule

---

### 4. Demand tiers T1–T5 (SPPC-06)

| Tier | Definition (binding when approved) |
|------|-------------------------------------|
| T1 | Direct high-intent commercial demand |
| T2 | Commercial problem demand |
| T3 | Extended service demand |
| T4 | Additional adjacent demand |
| T5 | Experimental demand |

Частота **не** определяет tier единолично.

**Operator action:** APPROVE tier model

---

### 5. Paid SERP business-hours requirement (SPPC-10)

| Item | Decision |
|------|----------|
| Mandatory MIG mode | `PAID SERP — BUSINESS HOURS` |
| Missing evidence | Strategy reports `BLOCKED OR DEGRADED — PAID COMPETITIVE EVIDENCE MISSING` |
| Continue without full SERP | Только explicit degraded-evidence approval |

**Current repo gap:** MIG mode **MISSING** — repair Wave 2.

**Operator action:** APPROVE requirement; authorize Wave 2 MIG implementation

---

### 6. Dated analytical pack (SPPC-12)

Обязательный пакет с semantic evidence, market evidence и time passport. Strategist не может заявлять полноту evidence при неполном пакете.

**Operator action:** APPROVE pack gate

---

### 7. AI PPC Strategist boundary (SPPC-13)

| Allowed | Forbidden |
|---------|-----------|
| Strategy после analytical gates | Strategy from keywords alone |
| Evidence-based competitor use | Invented competitor information |
| Path SPPC-14 → … → SPPC-19 → SPPC-20 | Jump to Commander Export |

**Operator action:** APPROVE strategist boundary

---

### 8. Manual / automatic bidding branch (SPPC-18)

Общий lifecycle до SPPC-18, затем governed branch:

| Mode | Gate |
|------|------|
| Manual bidding | Initial bid method, limits, review cadence documented |
| Automated bidding | **Blocked** without conversion tracking / analytics readiness |

**Operator action:** APPROVE bidding branch rules

---

### 9. Operator role

| Level | Scope |
|-------|-------|
| SPPC-01 | Business scope and authority approval |
| SPPC-21 | Campaign/strategy abstraction approval — **not** every keyword |
| Phrase-level review | Policy conflicts, sampled QA, critical disagreements, explicit request only |
| Degraded evidence | Explicit approval per `DEGRADED-EVIDENCE-MODE-v1.md` |
| Launch authority | SPPC-22 — not inferred from export |

**Operator action:** APPROVE operator boundary

---

### 10. Web-GPT constraints

Каждый Web-GPT чат по search PPC проекту обязан:

1. Идентифицировать project ID  
2. Читать lifecycle state (manifest)  
3. Работать только в allowed stage  
4. Не объявлять stage complete без evidence  
5. Отвечать `BLOCKED — LIFECYCLE REQUIREMENT NOT MET` при missing inputs  

Contract: [WEB-GPT-SEARCH-PPC-EXECUTION-CONTRACT-v1.md](../web-gpt/WEB-GPT-SEARCH-PPC-EXECUTION-CONTRACT-v1.md)

**Operator action:** APPROVE Web-GPT contract for sync pack publication

---

### 11. Lifecycle validator

| Item | Value |
|------|-------|
| Script | `validators/validate-search-ppc-lifecycle.mjs` |
| Status | Implemented v1 — **opt-in** until Wave 1 wiring |
| Synthetic tests | blocked + pre-strategy fixtures PASS |

**Operator action:** APPROVE validator as mandatory gate (Wave 1)

---

### 12. Gap audit result

Document: [MARS-SEARCH-PPC-LIFECYCLE-GAP-AUDIT-v1.md](../reports/MARS-SEARCH-PPC-LIFECYCLE-GAP-AUDIT-v1.md)

| Finding | Count |
|---------|------:|
| OPERATIONAL stages | 0 |
| CRITICAL missing capability | SPPC-10 MIG mode |
| UNSAFE BYPASS EXISTS | SPPC-03, 10, 13 |
| Triumph Commander | Project-specific (DUPLICATED) |

**Operator action:** ACKNOWLEDGE gap audit

---

### 13. Proposed repair roadmap

Document: [MARS-SEARCH-PPC-LIFECYCLE-REPAIR-ROADMAP-v1.md](../roadmap/MARS-SEARCH-PPC-LIFECYCLE-REPAIR-ROADMAP-v1.md)

| Wave | Focus |
|------|-------|
| 1 | Lifecycle authority and enforcement |
| 2 | MIG evidence (incl. paid SERP) |
| 3 | ORCA full semantic production |
| 4 | Analytical pack + strategist |
| 5 | Campaign production + QA |
| 6 | Commander + launch |
| 7 | Post-launch learning |

**Operator action:** APPROVE roadmap / REQUEST reprioritization

---

## Corvonero disposition

| Status | Rule |
|--------|------|
| Current | `FROZEN PENDING SEARCH PPC PRODUCTION LIFECYCLE IMPLEMENTATION AND GAP CLOSURE` |
| Preserve | Business intake, MIG evidence, source corpus, diagnostic artifacts |
| Prohibited until unfreeze | Semantic rerun, paid SERP, strategy, campaigns, Commander files |

**Operator action:** CONFIRM freeze continues

---

## P0-I / P0-D disposition

| Item | Status |
|------|--------|
| P0-I runtime `1fcf3d2` | APPROVED — CHECKPOINTED (admission core) |
| P0-I 200-phrase pilot | DIAGNOSTIC EVIDENCE ONLY |
| P0-I workbook | OPTIONAL DIAGNOSTIC / EMERGENCY REVIEW TOOL |
| P0-D | ON HOLD |

---

## Approval record (to be completed by operator)

| Field | Value |
|-------|-------|
| Reviewed by | _pending_ |
| Decision date | _pending_ |
| Outcome | `APPROVED — IMPLEMENTATION AUTHORIZED` |
| Wave 1 | Authorized per W1-D2 (2026-06-22) |
| Notes | |

**Outcomes when signed:**

- `APPROVED` — lifecycle status advances to CANONICAL APPROVED; Wave 1 execution authorized  
- `APPROVED WITH CONDITIONS` — list conditions; blocked items remain PROPOSED  
- `REJECTED` — lifecycle remains PROPOSED; no production enforcement  

---

## Related artifacts

- Lifecycle: [MARS-SEARCH-PPC-PRODUCTION-LIFECYCLE-v1.md](../MARS-SEARCH-PPC-PRODUCTION-LIFECYCLE-v1.md)
- Gap audit: [MARS-SEARCH-PPC-LIFECYCLE-GAP-AUDIT-v1.md](../reports/MARS-SEARCH-PPC-LIFECYCLE-GAP-AUDIT-v1.md)
- Bypass audit: [MARS-SEARCH-PPC-BYPASS-FAILURE-AUDIT-v1.md](../reports/MARS-SEARCH-PPC-BYPASS-FAILURE-AUDIT-v1.md)
- Placement: [PLACEMENT-DECISION-v1.md](../architecture/PLACEMENT-DECISION-v1.md)
