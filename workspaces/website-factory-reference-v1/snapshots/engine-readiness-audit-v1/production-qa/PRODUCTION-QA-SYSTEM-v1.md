# Website Factory — Production QA System v1

**Версия:** v1  
**Дата:** 2026-06-01  
**Operator:** APPROVED BY OPERATOR  
**Область:** `workspaces/website-factory-reference-v1/production-qa/`  
**Статус:** Global Production QA Layer — **documentation only**

**Не является:** runtime QA, automated testing, Playwright, visual regression, frontend implementation QA, deployment validation, code review automation, performance testing, accessibility audit tooling, CI pipeline, browser testing, production deploy gate.

---

## 1. Назначение Production QA Layer

Production QA System v1 — **финальный архитектурный слой контроля качества** Website Factory.

Слой отвечает на вопрос:

> **Готов ли проект к передаче во Frontend Layer после завершения всех принятых upstream-слоёв и Generation Contracts — с точки зрения архитектурной целостности, а не runtime-поведения?**

Production QA проверяет **наличие, согласованность и закрытость** accepted architecture artefacts. Не проверяет HTML, CSS, JS, сборку, деплой, скорость, доступность в браузере или качество сгенерированного copy.

---

## 2. Каноническая цепочка (полная)

```text
Legal Pack (FROZEN) + Legal Entity Discovery
        ↓
Site Type Registry
        ↓
   Blueprints
        ↓
Page Architecture
        ↓
 Block Registry
        ↓
Page Block Validation          ← ACCEPTED
        ↓
   SEO Architecture             ← ACCEPTED
        ↓
  Design System Mapping          ← ACCEPTED
        ↓
  Content Contracts              ← ACCEPTED
        ↓
  Content Validation             ← ACCEPTED
        ↓
  Generation Contracts           ← ACCEPTED
        ↓
  Production QA                  ← ACCEPTED (2026-06-04)
        ↓
 Frontend Layer                  ← FUTURE (implementation)
```

**Правило цепочки:** Production QA **потребляет** outcomes upstream gates и generation contract; **не переопределяет** taxonomy (`site_type_code`, `page_type`, `block_id`, `signal_id`, `VF_*`, `gate_id`).

**Gate rule:** Production QA run **не стартует**, если `GATE_GENERATION_READY` ≠ `PASS` или generation contract `status` ∈ { `BLOCKED`, `FAIL` }.

---

## 3. Роль Production QA

| Делает | Не делает |
|--------|-----------|
| Финальный architectural readiness review перед Frontend | Не открывает браузер, не запускает E2E |
| Проверяет completeness accepted layers per scope | Не валидирует compiled assets |
| Агрегирует upstream PASS/FAIL в единый QA contract | Не заменяет layer-specific validation runs |
| Эмитит `PASS` / `PASS_WITH_WARNINGS` / `FAIL` / `BLOCKED` | Не автоматизирует проверки (v1) |
| Блокирует Frontend Handoff без `GATE_PRODUCTION_QA_PASS` | Не одобряет production deploy |
| Ссылается на Core 5, 10 page types, 29 blocks | Не добавляет architecture layers |

---

## 4. Architectural QA vs other QA (boundary)

| Concept | Production QA v1 | Explicitly out of scope |
|---------|------------------|---------------------------|
| **Unit of review** | Project scope + layer artefacts | DOM nodes, components, bundles |
| **Evidence** | Contracts, matrices, gate records | Screenshots, Lighthouse, Core Web Vitals |
| **Pass meaning** | Architecture handoff-ready | Ship-to-production deploy-ready |
| **Operator** | Human-operated checklist + contract | QA bots, Playwright suites |
| **Failure** | Missing layer, gate FAIL, handoff violation | Flaky test, visual diff, bug in code |

См. [PRODUCTION-QA-GAPS-v1.md](PRODUCTION-QA-GAPS-v1.md) для зарегистрированного future work (automation, runtime, visual, etc.).

---

## 5. Dependencies (accepted foundation only)

| Layer | Location | Production QA uses |
|-------|----------|-------------------|
| Legal Pack v1 | [legal/](../legal/) | Legal completeness gate |
| Legal Entity Discovery | [legal-entity/](../legal-entity/) | Entity Card verification |
| Site Type Registry | [registry/](../registry/) | `site_type_code`, Core vs Extended |
| Blueprints | [blueprints/](../blueprints/) | IA, required pages/blocks |
| Page Architecture | [page-architecture/](../page-architecture/) | Page contracts, 10 `page_type` |
| Block Registry | [block-registry/](../block-registry/) | `block_id`, mappings |
| Page Block Validation | [page-block-validation/](../page-block-validation/) | Block stack PASS evidence |
| SEO Architecture v2 | [seo-architecture/](../seo-architecture/) | Strategy + page SEO |
| Design System Mapping | [design-system/](../design-system/) | `VF_*` bindings |
| Content Contracts | [content-contracts/](../content-contracts/) | Signal requirements |
| Content Validation | [content-validation/](../content-validation/) | Signal architecture PASS |
| Generation Contracts | [generation-contracts/](../generation-contracts/) | Generation Ready + handoff package |

**Не использовать как sole canon:** reference `src/` without architecture contracts; Extended Types without Core blueprint charter; legacy SEO v1 without v2 supersession.

---

## 6. QA categories (summary)

Канонический набор — [PRODUCTION-QA-CONTRACT-v1.md](PRODUCTION-QA-CONTRACT-v1.md) § `qa_categories`:

| Category | Scope |
|----------|-------|
| `ARCHITECTURE` | Site type, blueprint, page architecture, block registry alignment |
| `LEGAL` | Legal Pack, legal routes, template refs |
| `ENTITY` | Legal Entity Card when applicable |
| `SEO` | SEO architecture contracts per scope |
| `DESIGN` | Design system mapping completeness |
| `CONTENT` | Content contracts binding |
| `CONTENT_VALIDATION` | Content validation outcomes |
| `GENERATION_READINESS` | Generation contract + gates |
| `HANDOFF_READINESS` | Frontend handoff package structure |
| `DOCUMENTATION_INTEGRITY` | Version pins, acceptance states, no orphan refs |

---

## 7. Artefacts (this workstream)

| File | Role |
|------|------|
| [PRODUCTION-QA-SYSTEM-v1.md](PRODUCTION-QA-SYSTEM-v1.md) | Layer role, chain, boundaries (this doc) |
| [PRODUCTION-QA-CONTRACT-v1.md](PRODUCTION-QA-CONTRACT-v1.md) | Canonical QA run fields |
| [PRODUCTION-QA-GATES-v1.md](PRODUCTION-QA-GATES-v1.md) | Formal QA gate definitions |
| [PRODUCTION-QA-MATRIX-v1.md](PRODUCTION-QA-MATRIX-v1.md) | Core 5 × page types × layer coverage |
| [PRODUCTION-QA-CHECKLIST-v1.md](PRODUCTION-QA-CHECKLIST-v1.md) | Master readiness checklist |
| [PRODUCTION-QA-FAILURE-LIBRARY-v1.md](PRODUCTION-QA-FAILURE-LIBRARY-v1.md) | Typed failure catalog |
| [PRODUCTION-QA-SEVERITY-SYSTEM-v1.md](PRODUCTION-QA-SEVERITY-SYSTEM-v1.md) | INFO–BLOCKER + status mapping |
| [PRODUCTION-QA-GAPS-v1.md](PRODUCTION-QA-GAPS-v1.md) | Future work register |
| [PRODUCTION-QA-ROADMAP-v1.md](PRODUCTION-QA-ROADMAP-v1.md) | Maturity path |

---

## 8. Halt discipline

| Condition | Action |
|-----------|--------|
| Any upstream layer missing for scope | `BLOCKED` — complete layer first |
| Any required gate `FAIL` | `FAIL` — no Frontend Handoff |
| Any `BLOCKER` severity finding | `BLOCKED` until resolved |
| Any `CRITICAL` without waiver | `FAIL` |
| `PASS_WITH_WARNINGS` | Frontend Handoff **allowed** only if operator documents waiver per [PRODUCTION-QA-SEVERITY-SYSTEM-v1.md](PRODUCTION-QA-SEVERITY-SYSTEM-v1.md) |
| Generation attempted before readiness | `BLOCKED` — see PQF-009 |

---

## 9. Связанные документы

| Документ | Назначение |
|----------|------------|
| [ARCHITECTURE-FOUNDATION-v1.md](../ARCHITECTURE-FOUNDATION-v1.md) | Layer map |
| [GENERATION-SYSTEM-v1.md](../generation-contracts/GENERATION-SYSTEM-v1.md) | Immediate upstream |
| [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](../WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md) | Priority register |

---

*Production QA v1 — architecture-only final review. No runtime proof claimed.*
