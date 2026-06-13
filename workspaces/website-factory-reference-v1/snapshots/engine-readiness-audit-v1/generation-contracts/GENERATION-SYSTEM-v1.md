# Website Factory — Generation System v1

**Версия:** v1  
**Дата:** 2026-06-01  
**Operator:** APPROVED BY OPERATOR  
**Область:** `workspaces/website-factory-reference-v1/generation-contracts/`  
**Статус:** Production Generation Layer — **documentation only**

**Не является:** runtime orchestration, workflow engine, AI agent layer, prompt generation, content generation, frontend/code generation, MIG automation, CI pipeline, CMS export.

---

## 1. Назначение Generation Layer

Generation System v1 — **production orchestration layer** Website Factory.

Слой отвечает на вопрос:

> **Как оператор (или будущий human-operated pipeline) собирает все принятые upstream-артефакты в единый production-ready пакет для передачи во Frontend Layer — без выполнения генерации, без runtime и без реализации сборщика?**

Generation Layer описывает:

- production workflow (последовательность стадий);
- обязательные inputs и outputs;
- formal gates и stop points;
- dependencies и handoffs между слоями.

**Generation = orchestration contract only.** Не execution.

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
  Design System Mapping          ← ACCEPTED (pattern families)
        ↓
  Content Contracts              ← ACCEPTED (signals only)
        ↓
  Content Validation             ← ACCEPTED (signal architecture)
        ↓
  Generation Layer               ← THIS WORKSTREAM (v1)
        ↓
 Frontend Layer                  ← FUTURE (implementation)
```

**Правило цепочки:** каждый downstream слой **потребляет** frozen/approved upstream; Generation **не переопределяет** taxonomy (`site_type_code`, `page_type`, `block_id`, `signal_id`, `VF_*`).

---

## 3. Роль Generation Layer

| Делает | Не делает |
|--------|-----------|
| Определяет production lifecycle и stop points | Не запускает build, deploy, compile |
| Фиксирует mandatory generation contract fields | Не содержит prompts, model instructions, tool calls |
| Собирает **спецификации** (Page Build, Block Stack, SEO, Design, Content, Handoff) | Не генерирует HTML, CSS, React, Figma |
| Требует upstream gates PASS перед `Generation Ready` | Не валидирует copy quality или legal facts в runtime |
| Описывает Frontend Handoff Package (structure only) | Не реализует frontend partials |
| Ссылается на Core 5, 29 blocks, 10 page types | Не добавляет taxonomy без registry charter |

---

## 4. Orchestration vs execution (boundary)

| Concept | Generation v1 | Out of scope |
|---------|---------------|--------------|
| **Workflow** | Documented stages, approvals, halt rules | Automated scheduler, DAG runner |
| **Inputs** | Typed references to accepted artefacts | Live API fetch, CMS sync |
| **Outputs** | Specification documents / contract bundles | Generated source trees |
| **Gates** | Human-operated PASS markers | CI webhooks, blocking bots |
| **Handoff** | Frontend Handoff Package schema | Scaffold CLI, codegen |

**Halt discipline:** любой upstream FAIL / CRITICAL / unresolved legal → **STOP** до исправления; Generation stage **не стартует** (см. [GENERATION-GATES-v1.md](GENERATION-GATES-v1.md)).

---

## 5. Dependencies (accepted foundation only)

| Layer | Location | Generation uses |
|-------|----------|-----------------|
| Legal Pack v1 | [legal/](../legal/) | Legal routes, template refs, compliance gates |
| Legal Entity Discovery | [legal-entity/](../legal-entity/) | Entity Card READY gate |
| Site Type Registry | [registry/](../registry/) | `site_type_code`, Core vs Extended |
| Blueprints | [blueprints/](../blueprints/) | IA, required pages/blocks, exclusions |
| Page Architecture | [page-architecture/](../page-architecture/) | `page_type`, page contracts |
| Block Registry | [block-registry/](../block-registry/) | `block_id`, mappings |
| Page Block Validation | [page-block-validation/](../page-block-validation/) | Block stack PASS |
| SEO Architecture v2 | [seo-architecture/](../seo-architecture/) | Strategy + page SEO contracts |
| Design System Mapping | [design-system/](../design-system/) | `VF_*` pattern bindings |
| Content Contracts | [content-contracts/](../content-contracts/) | Signal requirements |
| Content Validation | [content-validation/](../content-validation/) | Signal architecture PASS |

**Не использовать как canon:** legacy registry SEO v1 hints без v2 supersession banner; Extended Types без Core blueprint; reference `src/` as sole truth for non-LANDING types.

---

## 6. Artefacts (this workstream)

| File | Role |
|------|------|
| [GENERATION-SYSTEM-v1.md](GENERATION-SYSTEM-v1.md) | Layer role, chain, boundaries (this doc) |
| [GENERATION-CONTRACT-v1.md](GENERATION-CONTRACT-v1.md) | Canonical generation contract fields |
| [GENERATION-LIFECYCLE-v1.md](GENERATION-LIFECYCLE-v1.md) | Production stages, stop/approval points |
| [GENERATION-GATES-v1.md](GENERATION-GATES-v1.md) | Formal gate definitions |
| [GENERATION-INPUTS-v1.md](GENERATION-INPUTS-v1.md) | Required input catalogue |
| [GENERATION-OUTPUTS-v1.md](GENERATION-OUTPUTS-v1.md) | Output specification definitions |
| [GENERATION-FAILURE-LIBRARY-v1.md](GENERATION-FAILURE-LIBRARY-v1.md) | Failure taxonomy |
| [GENERATION-GAPS-v1.md](GENERATION-GAPS-v1.md) | Future work register |

---

## 7. Operator model (v1)

1. **Classify** project → `site_type_code`.
2. **Walk lifecycle** per [GENERATION-LIFECYCLE-v1.md](GENERATION-LIFECYCLE-v1.md).
3. **Record gates** per [GENERATION-GATES-v1.md](GENERATION-GATES-v1.md).
4. **Instantiate** [GENERATION-CONTRACT-v1.md](GENERATION-CONTRACT-v1.md) when scope frozen.
5. **Emit specifications** per [GENERATION-OUTPUTS-v1.md](GENERATION-OUTPUTS-v1.md).
6. **Hand off** Frontend Handoff Package — human or future tooling; **no auto-build in v1**.

---

## 8. Связанные документы

- [ARCHITECTURE-FOUNDATION-v1.md](../ARCHITECTURE-FOUNDATION-v1.md) — foundation map (update via hygiene when Generation accepted)
- [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](../WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md) — priority register
- [content-contracts/CONTENT-GAPS-v1.md](../content-contracts/CONTENT-GAPS-v1.md) — CG-08 superseded by this layer charter

---

*Generation System version: v1.*
