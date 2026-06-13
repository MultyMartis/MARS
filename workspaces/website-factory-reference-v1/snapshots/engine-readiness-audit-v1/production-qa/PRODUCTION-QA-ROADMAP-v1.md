# Website Factory — Production QA Roadmap v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/production-qa/`  
**Статус:** maturity path — **documentation only**  
**Связь:** [PRODUCTION-QA-GAPS-v1.md](PRODUCTION-QA-GAPS-v1.md), [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](../WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md)

---

## Назначение

Roadmap v1 описывает **эволюцию** Production QA Layer от human-operated architecture review к возможным future capabilities. **Не** является commitment schedule.

---

## Maturity levels

| Level | Name | Characteristics | Status |
|-------|------|-----------------|--------|
| **L0** | — | No production QA layer | Superseded |
| **L1** | Architecture QA (v1) | Contract, gates, matrix, checklist, failure library, severity — human-operated | **CURRENT** (this workstream) |
| **L2** | Assisted QA | Checklist tooling, contract templates, evidence bundling — still human sign-off | FUTURE |
| **L3** | Aggregated validators | Auto-collect upstream PASS/FAIL into QA contract draft — no browser | FUTURE |
| **L4** | Extended matrix | Extended site types + per-block micro-matrix | FUTURE |
| **L5+** | Out of band | Runtime, visual, deploy, Playwright — **separate products** per GAPS | NOT Production QA core |

---

## Phase plan (documentation)

### Phase 1 — Production QA Architecture v1 (2026-06-01)

**Deliverables:**

- `production-qa/` — 9 artefacts (SYSTEM, CONTRACT, GATES, MATRIX, CHECKLIST, FAILURE-LIBRARY, SEVERITY, GAPS, ROADMAP)
- Priority register update — IN PROGRESS

**Exit criteria (operator acceptance):**

- Operator confirms architectural-only boundary
- Pilot project completes one full PRODUCTION-QA-CONTRACT run (human-operated)

---

### Phase 2 — Operator tooling (NOT QUEUED)

**Scope:** L2 — template generator for `qa_run_id`, checklist PDF/markdown export, evidence folder structure.

**Not in scope:** CI, Playwright, deploy gates.

**Charter:** required before start.

---

### Phase 3 — Upstream aggregation (NOT QUEUED)

**Scope:** L3 — read validation + content validation + generation contract statuses into draft QA contract.

**Not in scope:** New validation rules; browser tests.

---

### Phase 4 — Factory Runtime Architecture (NOT QUEUED)

**Scope:** Separate workstream — runtime orchestration, possible execution of generation (still not claimed in MARS repo today).

**Relationship:** Runtime **may consume** Production QA PASS as handoff gate; Production QA **does not** implement runtime.

See [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](../WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md).

---

### Phase 5 — Frontend Layer (NOT QUEUED)

**Scope:** Implementation binding after `GATE_FRONTEND_HANDOFF_APPROVED`.

**Relationship:** Frontend QA (PQA-G04) remains **separate** from Production QA.

---

## Recommended sequence (after v1 acceptance)

```text
Production QA v1 ACCEPTED
        ↓
Generation Contracts v1 ACCEPTED (if not already)
        ↓
[Operator pilot: 1× full QA run on reference project]
        ↓
Factory Runtime Architecture — charter required (NOT QUEUED)
        ↓
Frontend Layer — charter required (NOT QUEUED)
```

---

## Success metrics (human-operated)

| Metric | L1 target |
|--------|-----------|
| Checklist completion rate on pilot | 100% sections attempted |
| BLOCKER findings before handoff | 0 on accepted pilot |
| Confusion with runtime QA | 0 — documented exclusions used |
| Orphan architecture refs at QA | 0 |

---

## SAFE UNKNOWN

- Date for L2 tooling — **not scheduled**.
- Whether L3 aggregation lives in MARS repo or external bridge — **UNKNOWN**.
- Pilot project selection (Triumph vs reference workspace) — **operator choice**.

---

*Production QA Roadmap v1 — maturity documentation only.*
