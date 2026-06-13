# Website Factory — Generation Gaps v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/generation-contracts/`  
**Статус:** future work register — **no implementation**

**Не является:** commitment schedule, charter approval, delivery dates.

---

## 1. Назначение

Регистр workstreams **явно вне** Generation Contracts v1 (orchestration documentation). Записи **не** меняют канон registries и **не** разрешают runtime claims.

---

## 2. Gap register

| Gap ID | Workstream | Description | Depends on | Status |
|--------|------------|-------------|------------|--------|
| GG-01 | **Prompt systems** | LLM prompt libraries, model routing — separate from generation contract | Generation Contracts ACCEPTED | NOT STARTED |
| GG-02 | **AI generation** | Automated copy, layout suggestions, asset generation | GG-01, Content Contracts | NOT STARTED |
| GG-03 | **Frontend generation** | Scaffold partials, section HTML, component trees from specs | Generation ACCEPTED, Frontend charter | NOT STARTED |
| GG-04 | **Code generation** | Source code emitters (React, static HTML pipelines) | GG-03 | NOT STARTED |
| GG-05 | **Figma generation** | Design file emit from Design Specification | Design System evolution | NOT STARTED |
| GG-06 | **QA automation** | Automated checks beyond documentation gates | Production QA Architecture | NOT STARTED |
| GG-07 | **Runtime orchestration** | DAG runner, CI gates, scheduled pipelines | All GG-01–GG-06 policy | NOT STARTED |
| GG-08 | **MIG integration** | `incoming/mig/` request → generation scope bridge | Generation ACCEPTED, MIG charter | NOT STARTED |
| GG-09 | **Agent layer** | Multi-agent orchestration over generation | MARS runtime (not in repo) | NOT STARTED |
| GG-10 | **Workflow engine** | Executable BPMN/state machine for GL stages | GG-07 | NOT STARTED |
| GG-11 | **Production QA Architecture** | Post-handoff quality architecture (Lighthouse, a11y, cross-browser policy) | Frontend handoff charter | **NOT QUEUED** |
| GG-12 | **CMS export** | Specification → CMS schema mapping | GG-03 | NOT STARTED |
| GG-13 | **Deploy automation** | Build, staging, production promote | Runtime + survivability charter | NOT STARTED |
| GG-14 | **JSON Schema export** | Machine-readable GENERATION-CONTRACT schema | Generation ACCEPTED | NOT STARTED |
| GG-15 | **Extended site types** | Full generation matrix for SAAS, WEB_APPLICATION, MARKETPLACE | Site Type charter | NOT STARTED |

---

## 3. Explicitly out of scope (v1)

| Item | Rationale |
|------|-----------|
| Runtime Website Factory | No implementation in reference workspace |
| Prompt / AI instructions in contracts | GG-01, GG-02 |
| Automated gate enforcement | GG-07 |
| Content/copy generation | Content Gaps CG-01+ |
| Legal HTML auto-pipeline | Legal Pack workflow (FROZEN) |
| ORCA/MIG execution | GG-08 |

---

## 4. Promotion criteria (documentation)

Workstream may graduate from GAP → charter when:

1. Generation Contracts v1 **ACCEPTED** by operator.
2. Frontend Handoff Package used in at least one pilot (evidence).
3. No new taxonomy without registry charter.
4. Survivability / Factory enforcement docs referenced for destructive ops.

---

## 5. Relation to Content Gaps

| Content Gap | Generation resolution |
|-------------|----------------------|
| CG-08 Generation Contracts | **Addressed** by `generation-contracts/` v1 (this deliverable) |
| CG-09 MIG Integration | Remains GG-08 |

---

## 6. SAFE UNKNOWN

- Priority order among GG-01–GG-15 — **not scheduled** in this document.
- Production QA Architecture (GG-11) scope depth — **UNKNOWN** until charter.
- Resource ownership — **UNKNOWN**.

---

*Generation Gaps version: v1.*
