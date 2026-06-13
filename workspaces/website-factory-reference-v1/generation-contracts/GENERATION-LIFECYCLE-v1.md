# Website Factory — Generation Lifecycle v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/generation-contracts/`  
**Статус:** production lifecycle — **documentation only**  
**Связь:** [GENERATION-GATES-v1.md](GENERATION-GATES-v1.md), [GENERATION-SYSTEM-v1.md](GENERATION-SYSTEM-v1.md)

**Не является:** BPMN diagram executable, state machine code, CI stage list.

---

## 1. Назначение

Generation Lifecycle v1 описывает **последовательность production стадий** от классификации проекта до передачи во Frontend Layer, включая **stop points** и **approval points** (HITL).

---

## 2. Lifecycle diagram

```text
Classify
    ↓  [STOP if unclassifiable / Extended without charter]
Blueprint Select & Freeze
    ↓  [APPROVAL: Blueprint Approved]
Page Architecture Instantiate
    ↓  [APPROVAL: Page Architecture Approved]
Block Selection & Mapping
    ↓
Page Block Validation
    ↓  [GATE: Block Validation PASS] — STOP on FAIL/CRITICAL
SEO Architecture Apply
    ↓  [APPROVAL: SEO Approved]
Design Mapping Apply
    ↓  [APPROVAL: Design Approved]
Content Contracts Bind
    ↓
Content Validation
    ↓  [GATE: Content Validation PASS] — STOP on FAIL/CRITICAL
Legal Pack & Entity Check
    ↓  [GATE: Legal Pack PASS, Entity Card READY when required]
Generation Ready
    ↓  [APPROVAL: Generation Ready — operator sign-off]
Specification Assembly
    ↓
Frontend Handoff
    ↓  [HANDOFF ACK — Frontend Layer owns next]
```

---

## 3. Stage definitions

| Stage ID | Name | Purpose | Primary outputs (refs) |
|----------|------|---------|------------------------|
| **GL-01** | Classify | Resolve `site_type_code`, Core vs Extended, production tier | Registry entry, project brief |
| **GL-02** | Blueprint | Select canonical blueprint; freeze IA intent | `blueprint_ref`, exclusions |
| **GL-03** | Page Architecture | Instantiate page contracts per routes | `page_type` set, PAGE-CONTRACT refs |
| **GL-04** | Block Selection | Map `block_id` stacks per page | PAGE-BLOCK-MAPPING resolve |
| **GL-05** | Validation | Page → block semantic check | VALIDATION-CONTRACT run |
| **GL-06** | SEO | Apply SEO strategy + page SEO contracts | SEO_SPEC inputs |
| **GL-07** | Design | Bind `VF_*` per block/page | DESIGN_SPEC inputs |
| **GL-08** | Content | Bind content signals per contracts | CONTENT_SPEC inputs |
| **GL-09** | Content Validation | Signal architecture check | Content validation run |
| **GL-10** | Legal & Entity | Legal Pack routes + entity card | Legal gates |
| **GL-11** | Generation Ready | Confirm all gates; freeze scope | `generation_id`, GENERATION-CONTRACT `READY` |
| **GL-12** | Specification Assembly | Compile output bundle | GENERATION-OUTPUTS artefacts |
| **GL-13** | Frontend Handoff | Transfer package to Frontend workstream | FRONTEND_HANDOFF_PACKAGE |

---

## 4. Stop points (mandatory halt)

| Stop ID | Trigger | Resume condition |
|---------|---------|------------------|
| **SP-01** | `site_type_code` ambiguous or Extended without charter | Operator classification + charter |
| **SP-02** | No canonical blueprint for Core type | Blueprint delivery or reclassification |
| **SP-03** | Page Block Validation `FAIL` or CRITICAL | Fix stack; re-run validation |
| **SP-04** | SEO unresolved (missing page SEO contract) | Complete SEO profile |
| **SP-05** | Design unresolved (`VF_*` missing for required block) | Complete design mapping |
| **SP-06** | Content Validation `FAIL` or forbidden signal | Fix signal architecture |
| **SP-07** | Legal Pack FAIL or placeholder in legal routes | Legal workflow (FROZEN pack rules) |
| **SP-08** | Entity Card not READY when PII/forms/legal identity required | Entity discovery complete |
| **SP-09** | Generation attempted before GL-11 | Complete upstream gates |

**Rule:** at stop point, `generation contract status` ∈ `{ DRAFT, IN_PROGRESS, BLOCKED }` only.

---

## 5. Approval points (HITL)

| Approval ID | Gate name | Who | Records |
|-------------|-----------|-----|---------|
| **AP-01** | Blueprint Approved | Operator | `blueprint_ref` frozen timestamp |
| **AP-02** | Page Architecture Approved | Operator | Page contract set signed |
| **AP-03** | SEO Approved | Operator | SEO profile complete for scope |
| **AP-04** | Design Approved | Operator | Pattern bindings complete |
| **AP-05** | Content Approved | Operator | Signal bindings complete (pre-validation) |
| **AP-06** | Generation Ready | Operator | All automated/manual gates PASS |
| **AP-07** | Frontend Handoff Ack | Operator + Frontend owner | Handoff package receipt |

Approvals **не** заменяют validation PASS — approval после FAIL **запрещён** без documented exception charter (mars-survivability human authority).

---

## 6. Parallel work (allowed documentation-only)

| Parallel track | Constraint |
|----------------|------------|
| Legal Pack prep during GL-02–GL-04 | Must not bypass Legal Pack PASS before GL-11 |
| Entity discovery during early stages | Entity Card READY required before GL-11 if applicable |
| Reference workspace prototyping | Must not become canon without registry alignment |

**Forbidden parallel:** Frontend implementation before GL-11 for same `generation_id` scope.

---

## 7. Scope slicing

| `scope_type` | Lifecycle note |
|--------------|----------------|
| `FULL_SITE` | All stages GL-01–GL-13 for all blueprint `required_pages` |
| `PAGE_SUBSET` | GL-05–GL-09 per included pages only; handoff marks excluded routes |
| `LEGAL_ONLY` | GL-10 + legal outputs; skips block/design for marketing pages |
| `PHASE_SLICE` | Operator-defined phase; new `generation_id` per phase recommended |

---

## 8. Status mapping (contract ↔ lifecycle)

| Lifecycle position | Suggested `status` |
|--------------------|-------------------|
| Before GL-11 | `DRAFT` or `IN_PROGRESS` |
| Stop point active | `BLOCKED` |
| GL-11 complete | `READY` |
| GL-13 acknowledged | `HANDED_OFF` |
| Unrecoverable upstream violation | `FAILED` |

---

*Generation Lifecycle version: v1.*
