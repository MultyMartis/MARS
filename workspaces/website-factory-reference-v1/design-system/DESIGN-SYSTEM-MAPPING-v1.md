# Website Factory — Design System Mapping v1

**Версия:** v1  
**Дата:** 2026-06-01  
**Operator:** APPROVED BY OPERATOR  
**Область:** `workspaces/website-factory-reference-v1/design-system/`  
**Статус:** Design Architecture Layer — **documentation only**

**Не является:** UI mockup generation, Figma output, CSS, typography/color spec, frontend components, runtime design engine, visual asset pipeline.

---

## 1. Назначение Design Layer

Design System Mapping v1 — **архитектурный слой связи** между канонической IA/block/SEO базой Website Factory и будущим Frontend Layer.

Слой отвечает на вопрос: **какой визуальный паттерн (pattern family) допустим для данного `block_id` в контексте `page_type` и `site_type_code`**, без фиксации цветов, шрифтов или кода.

**Production bridge (расширенный):**

```text
Site Type Registry
        ↓
   Blueprints
        ↓
Page Architecture
        ↓
 Block Registry
        ↓
Page Block Validation
        ↓
   SEO Layer              ← ACCEPTED
        ↓
  Design Layer            ← ACCEPTED (2026-06-04)
        ↓
 Frontend Layer           ← FUTURE
```

---

## 2. Позиция в цепочке

| Предшественник | Что передаёт в Design Layer |
|----------------|----------------------------|
| [registry/SITE-TYPE-REGISTRY-v1.md](../registry/SITE-TYPE-REGISTRY-v1.md) | `site_type_code`, цели типа |
| [blueprints/](../blueprints/) | IA intent, required pages, block stacks |
| [page-architecture/](../page-architecture/) | `page_type`, PAGE-CONTRACT, LEGAL-PAGE-CONTRACT |
| [block-registry/BLOCK-REGISTRY-v1.md](../block-registry/BLOCK-REGISTRY-v1.md) | 29 canonical `block_id` |
| [page-block-validation/](../page-block-validation/) | REQUIRED / FORBIDDEN block stances |
| [seo-architecture/](../seo-architecture/) | SEO depth, intent mix, page SEO roles |

| Последователь | Что потребляет от Design Layer |
|---------------|-------------------------------|
| Frontend Layer (future) | Pattern selection per block instance |
| Content Contracts (future) | Content shape hints tied to pattern role |
| Design QA (future) | Pattern compliance checks |

**Внешняя ссылка (не канон v1):** `projects/orca/visual-semantics/contracts/website-factory-visual-contract-v0.md` — legacy/experimental; Design Layer v1 **не импортирует** styling из v0.

---

## 3. Inputs (обязательные)

| Input | Источник | Использование |
|-------|----------|---------------|
| `site_type_code` | Site Type Registry | SITE-TYPE-DESIGN-MAPPING-v1 |
| `blueprint_id` | Core Blueprint | Design follows Blueprint IA |
| `page_type` | Page Type Registry (10) | PAGE-TYPE-DESIGN-MAPPING-v1 |
| `block_id` | Block Registry (29) | BLOCK-VISUAL-MAPPING-v1 |
| Block stance | PAGE-BLOCK-MAPPING, BLUEPRINT-BLOCK-MAPPING | Forbidden patterns when block FORBIDDEN |
| Validation outcome | Page Block Validation | Stop before Design if FAIL/CRITICAL |
| SEO profile | SITE-TYPE-SEO-MAPPING-v2 | Design cannot contradict SEO page role |
| Legal Pack | legal/ (FROZEN) | LEGAL_PAGE inherits project shell only |

---

## 4. Outputs (v1)

| Artefact | Файл | Содержание |
|----------|------|------------|
| Pattern contract schema | [VISUAL-PATTERN-CONTRACT-v1.md](VISUAL-PATTERN-CONTRACT-v1.md) | Поля паттерна |
| Pattern registry | [VISUAL-PATTERN-REGISTRY-v1.md](VISUAL-PATTERN-REGISTRY-v1.md) | Initial pattern families |
| Block → pattern map | [BLOCK-VISUAL-MAPPING-v1.md](BLOCK-VISUAL-MAPPING-v1.md) | `block_id` → families |
| Site type design profile | [SITE-TYPE-DESIGN-MAPPING-v1.md](SITE-TYPE-DESIGN-MAPPING-v1.md) | Core 5 |
| Page type design profile | [PAGE-TYPE-DESIGN-MAPPING-v1.md](PAGE-TYPE-DESIGN-MAPPING-v1.md) | 10 page types |
| Rules | [DESIGN-SYSTEM-RULES-v1.md](DESIGN-SYSTEM-RULES-v1.md) | Architecture gates |
| Gaps | [DESIGN-SYSTEM-GAPS-v1.md](DESIGN-SYSTEM-GAPS-v1.md) | Future work register |

**Не выходят из v1:** tokens, components, CSS, Figma files, generated HTML.

---

## 5. Dependencies

| Dependency | Обязательность | При нарушении |
|------------|----------------|---------------|
| Frozen foundation | Hard | Halt — no Design expansion without charter |
| Block Registry v1 (29 ids) | Hard | No new `block_id` in Design workstream |
| Page Type Registry v1 (10 types) | Hard | No new `page_type` |
| Core 5 site types for profiles | Hard for mapping tables | Extended types → SAFE UNKNOWN |
| Validation PASS (manual) | Soft gate | Documented stop — see §6 |
| SEO Architecture v2 | Hard | Design subordinate to SEO page roles |
| Legal Pack v1 FROZEN | Hard | LEGAL_PAGE pattern restrictions |

---

## 6. Stop conditions

| Condition | Action |
|-----------|--------|
| Page Block Validation **FAIL** or **CRITICAL** | **STOP** — resolve block stack before pattern binding |
| `block_id` FORBIDDEN on page/blueprint | **STOP** — no pattern selection for that block |
| `page_type` not allowed for `site_type_code` | **STOP** — reclassify site or page |
| Request for new site type / page type / block id | **STOP** — registry charter required |
| Request for colors, fonts, CSS, components | **OUT OF SCOPE** — register in DESIGN-SYSTEM-GAPS-v1 |
| Legal placeholder gate open | **STOP** generation downstream (incl. visual binding on legal routes) |
| Operator requests styling implementation | **DEFER** — Frontend / tokens charter |

---

## 7. Layer artefact index

| # | File | Task |
|---|------|------|
| 1 | DESIGN-SYSTEM-MAPPING-v1.md | Architecture (this document) |
| 2 | VISUAL-PATTERN-CONTRACT-v1.md | Pattern field contract |
| 3 | VISUAL-PATTERN-REGISTRY-v1.md | Initial families |
| 4 | BLOCK-VISUAL-MAPPING-v1.md | Block → pattern |
| 5 | SITE-TYPE-DESIGN-MAPPING-v1.md | Site type profiles |
| 6 | PAGE-TYPE-DESIGN-MAPPING-v1.md | Page type profiles |
| 7 | DESIGN-SYSTEM-RULES-v1.md | Rules |
| 8 | DESIGN-SYSTEM-GAPS-v1.md | Gaps |

---

## 8. Maturity

| Dimension | v1 status |
|-----------|-----------|
| Pattern vocabulary | **Defined** — architectural families only |
| Per-block binding | **Defined** — BLOCK-VISUAL-MAPPING-v1 |
| Site/page profiles | **Defined** — Core 5 + 10 page types |
| Tokens / components | **NOT STARTED** — gaps |
| Automation | **NOT IMPLEMENTED** |

**Label:** Design Architecture Layer v1 — documentation + human-operated pattern selection.

---

## 9. SAFE UNKNOWN

- Optimal count of pattern variants per family on Frontend — **UNKNOWN** until Content/Frontend charters.
- Parity of Design profiles for Extended site types (SAAS, WEB_APPLICATION, MARKETPLACE) — **FUTURE**.
- Automated pattern validator — **FUTURE** (see gaps).

---

*Design System Mapping version: v1. Canonical location: `workspaces/website-factory-reference-v1/design-system/`.*
