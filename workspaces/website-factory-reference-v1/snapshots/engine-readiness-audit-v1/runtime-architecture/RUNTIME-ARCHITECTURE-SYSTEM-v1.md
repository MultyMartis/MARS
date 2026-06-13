# Website Factory — Runtime Architecture System v1

**Версия:** v1  
**Дата:** 2026-06-01  
**Operator:** APPROVED BY OPERATOR  
**Область:** `workspaces/website-factory-reference-v1/runtime-architecture/`  
**Статус:** Factory Runtime Architecture Layer — **documentation only**

**Не является:** workflow engine, orchestration software, agent runtime, n8n, automation platform, CI pipeline, project database, queue system, code generation, frontend build, MIG execution.

---

## 1. Назначение Runtime Layer

Runtime Architecture v1 отвечает на вопрос:

> **Как Website Factory проект *движется* через принятые архитектурные слои — какие состояния, переходы, gates, handoffs и stop conditions применяются — без какого-либо execution engine?**

Runtime Layer — **дисциплина движения** (movement discipline):

- фиксирует **project lifecycle** и **canonical project states**;
- определяет **когда** разрешён переход между слоями;
- связывает **runtime gates** с upstream layer contracts;
- описывает **handoffs** producer → consumer;
- регистрирует **failure modes** при нарушении порядка.

**Runtime = control of movement. Not execution. Not generation. Not automation.**

---

## 2. Границы ответственности

| Runtime Layer **делает** | Runtime Layer **не делает** |
|--------------------------|-----------------------------|
| State model и transition rules | Выполнение валидации (CLI, CI, scripts) |
| Gate definitions и pass/fail semantics | Генерация HTML, контента, SEO-текста |
| Handoff contracts (артефакты, блокеры) | Orchestration agents, n8n, MIG runs |
| Stop conditions и approval points (HITL) | Хранение состояния проекта в БД |
| Ссылка на accepted layer docs | Изменение frozen Legal Pack architecture |

---

## 3. Принятая foundation (только accepted systems)

Runtime v1 **потребляет** только operator-accepted / frozen системы:

| System | Location | Runtime role |
|--------|----------|--------------|
| Legal Pack v1 | [legal/](../legal/) | Parallel gate track — FROZEN |
| Legal Entity Discovery v1 | [legal-entity/](../legal-entity/) | Entity gate when required |
| Site Type Registry v1 | [registry/](../registry/) | Classification → `site_type_code` |
| Site Type Blueprints v1 | [blueprints/](../blueprints/) | Blueprint state + handoff |
| Page Architecture v1 | [page-architecture/](../page-architecture/) | Page contracts per route |
| Block Registry v1 | [block-registry/](../block-registry/) | Block mapping state |
| Page Block Validation v1 | [page-block-validation/](../page-block-validation/) | VALIDATED gate |
| SEO Architecture v2 | [seo-architecture/](../seo-architecture/) | SEO_READY gate |
| Design System Mapping v1 | [design-system/](../design-system/) | DESIGN_READY gate |
| Content Contracts v1 | [content-contracts/](../content-contracts/) | CONTENT_READY gate |
| Content Validation v1 | [content-validation/](../content-validation/) | CONTENT_VALIDATED gate |
| Generation Contracts v1 | [generation-contracts/](../generation-contracts/) | GENERATION_READY gate |
| Production QA v1 | [production-qa/](../production-qa/) | PRODUCTION_QA_READY gate |

**Не использует** как runtime truth: governance expansion, Mobile App Factory, unapproved site types, workflow engine drafts.

---

## 4. Каноническая цепочка (Runtime view)

```text
Intake
    ↓
Classification          (Site Type Registry)
    ↓
Blueprint               (Blueprints)
    ↓
Page Architecture       (Page Architecture)
    ↓
Blocks                  (Block Registry)
    ↓
Validation              (Page Block Validation)
    ↓
SEO                     (SEO Architecture)
    ↓
Design                  (Design System Mapping)
    ↓
Content                 (Content Contracts)
    ↓
Content Validation      (Content Validation)
    ↓
Generation Ready        (Generation Contracts)
    ↓
Production QA           (Production QA)
    ↓
Frontend Handoff        (Generation → Frontend boundary)
    ↓
Complete
```

**Parallel track (не пропускается для FULL_SITE / PII):**

```text
Legal Pack + Legal Entity Discovery
    → gates bound at Legal Complete / Entity Verified
    → must PASS before GENERATION_READY (see RUNTIME-GATES-v1.md)
```

---

## 5. Mapping: Runtime states ↔ Architecture layers

| Runtime state | Primary layer | Entry document |
|---------------|---------------|----------------|
| `NEW_PROJECT` | Intake | — (project charter) |
| `CLASSIFIED` | Site Type Registry | [SITE-TYPE-REGISTRY-v1.md](../registry/SITE-TYPE-REGISTRY-v1.md) |
| `BLUEPRINT_READY` | Blueprints | [BLUEPRINT-SYSTEM-v1.md](../blueprints/BLUEPRINT-SYSTEM-v1.md) |
| `PAGE_READY` | Page Architecture | [PAGE-ARCHITECTURE-SYSTEM-v1.md](../page-architecture/PAGE-ARCHITECTURE-SYSTEM-v1.md) |
| `BLOCK_READY` | Block Registry | [BLOCK-REGISTRY-v1.md](../block-registry/BLOCK-REGISTRY-v1.md) |
| `VALIDATED` | Page Block Validation | [PAGE-BLOCK-VALIDATION-SYSTEM-v1.md](../page-block-validation/PAGE-BLOCK-VALIDATION-SYSTEM-v1.md) |
| `SEO_READY` | SEO Architecture | [SEO-ARCHITECTURE-SYSTEM-v2.md](../seo-architecture/SEO-ARCHITECTURE-SYSTEM-v2.md) |
| `DESIGN_READY` | Design System Mapping | [DESIGN-SYSTEM-MAPPING-v1.md](../design-system/DESIGN-SYSTEM-MAPPING-v1.md) |
| `CONTENT_READY` | Content Contracts | [CONTENT-SYSTEM-v1.md](../content-contracts/CONTENT-SYSTEM-v1.md) |
| `CONTENT_VALIDATED` | Content Validation | [CONTENT-VALIDATION-SYSTEM-v1.md](../content-validation/CONTENT-VALIDATION-SYSTEM-v1.md) |
| `GENERATION_READY` | Generation Contracts | [GENERATION-SYSTEM-v1.md](../generation-contracts/GENERATION-SYSTEM-v1.md) |
| `PRODUCTION_QA_READY` | Production QA | [PRODUCTION-QA-SYSTEM-v1.md](../production-qa/PRODUCTION-QA-SYSTEM-v1.md) |
| `FRONTEND_READY` | Frontend Handoff | [GENERATION-OUTPUTS-v1.md](../generation-contracts/GENERATION-OUTPUTS-v1.md) |
| `COMPLETE` | Terminal | Operator sign-off |

---

## 6. Relationship to Generation / Production QA

| Layer | Question answered | Runtime relationship |
|-------|-------------------|----------------------|
| **Generation Contracts** | *What* goes into production package? | Runtime **requires** `GENERATION_READY` state before Production QA |
| **Production QA** | *Is* architecture ready for Frontend? | Runtime **requires** `PRODUCTION_QA_READY` before `FRONTEND_READY` |
| **Runtime Architecture** | *When* may project advance? | **Meta-layer** — does not replace layer-specific gates |

Runtime gates **reference** layer gates ([GENERATION-GATES-v1.md](../generation-contracts/GENERATION-GATES-v1.md), [PRODUCTION-QA-GATES-v1.md](../production-qa/PRODUCTION-QA-GATES-v1.md)); не дублируют их семантику проверки.

---

## 7. Operator model (human-operated)

1. Operator (or delegated role) **declares** project state after layer work completes.
2. Each advance requires **documented gate PASS** (checklist / sign-off record — format out of scope v1).
3. **FAIL / CRITICAL** upstream → **mandatory halt** — no skip-forward transitions.
4. **HITL approval points** — explicit operator sign-off at Blueprint, Page Architecture, SEO, Design, Content, Generation Ready, Frontend Handoff, Complete.

**No automated state mutation** is claimed or defined in v1.

---

## 8. Artefact index (Runtime Layer v1)

| Document | Purpose |
|----------|---------|
| [PROJECT-LIFECYCLE-v1.md](PROJECT-LIFECYCLE-v1.md) | End-to-end lifecycle phases |
| [PROJECT-STATE-MODEL-v1.md](PROJECT-STATE-MODEL-v1.md) | Canonical states — purpose, I/O, gates |
| [STATE-TRANSITION-RULES-v1.md](STATE-TRANSITION-RULES-v1.md) | Allowed / forbidden transitions |
| [RUNTIME-GATES-v1.md](RUNTIME-GATES-v1.md) | Runtime gate catalogue |
| [RUNTIME-HANDOFFS-v1.md](RUNTIME-HANDOFFS-v1.md) | Layer-to-layer handoffs |
| [RUNTIME-FAILURE-LIBRARY-v1.md](RUNTIME-FAILURE-LIBRARY-v1.md) | Movement failures |
| [RUNTIME-GAPS-v1.md](RUNTIME-GAPS-v1.md) | Future work only |
| [RUNTIME-ROADMAP-v1.md](RUNTIME-ROADMAP-v1.md) | Runtime layer evolution |

---

## 9. Validation statement (architecture only)

| Check | Result |
|-------|--------|
| Agents / AI orchestration | **ABSENT** |
| Runtime engine / state machine code | **ABSENT** |
| n8n / workflow automation | **ABSENT** |
| Code / CLI in `runtime-architecture/` | **ABSENT** |
| Generation implementation | **ABSENT** — references Generation Contracts only |
| Orchestration product claims | **NONE** |

---

## SAFE UNKNOWN

- Standard project manifest file path for state persistence — **NOT DEFINED** (see RUNTIME-GAPS-v1.md).
- Post-freeze layer acceptance — **ACCEPTED** 2026-06-04 per [FOUNDATION-FINALIZATION-PASS-v1.md](../FOUNDATION-FINALIZATION-PASS-v1.md) and [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](../WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md).
- Integration with MIG / incoming queues — **FUTURE** — not in v1 scope.

---

*Runtime Architecture System v1 — 2026-06-01. Movement discipline only. Canonical location: `workspaces/website-factory-reference-v1/runtime-architecture/`.*
