# Website Factory — Content System v1

**Версия:** v1  
**Дата:** 2026-06-01  
**Operator:** APPROVED BY OPERATOR  
**Область:** `workspaces/website-factory-reference-v1/content-contracts/`  
**Статус:** Content Architecture Layer — **documentation only**

**Не является:** copywriting, SEO text generation, prompt library, article/landing generation, CMS content pipeline, runtime content engine, MIG/ORCA automation.

---

## 1. Назначение Content Layer

Content System v1 — **архитектурный слой связи** между канонической IA/block/SEO/Design базой Website Factory и будущим Frontend Layer.

Слой отвечает на вопрос: **какие семантические content signals обязаны присутствовать (или запрещены) для данного `block_id` / `page_type` / `site_type_code`**, без фиксации маркетингового текста, формулировок или сгенерированного copy.

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
  Design Layer            ← ACCEPTED (pattern families)
        ↓
  Content Layer           ← THIS WORKSTREAM (v1)
        ↓
 Frontend Layer           ← FUTURE
```

**Связь с Design:** Content signals **не заменяют** visual patterns (`VF_*`). Паттерн задаёт структурную роль; content contract задаёт **обязательные семантические слоты** внутри блока.

---

## 2. Каноническая цепочка (Content)

| Шаг | Артефакт | Роль для Content |
|-----|----------|------------------|
| 1 | `site_type_code` | [SITE-TYPE-CONTENT-MAPPING-v1.md](SITE-TYPE-CONTENT-MAPPING-v1.md) — приоритеты trust/conversion |
| 2 | Blueprint | IA intent, required pages, block stacks → scope сигналов |
| 3 | `page_type` | [PAGE-CONTENT-CONTRACTS-v1.md](PAGE-CONTENT-CONTRACTS-v1.md) |
| 4 | `block_id` | [BLOCK-CONTENT-CONTRACTS-v1.md](BLOCK-CONTENT-CONTRACTS-v1.md) |
| 5 | Visual pattern (`VF_*`) | Design Layer — layout role; content binds **after** pattern selected |
| 6 | Content contract | [CONTENT-CONTRACT-v1.md](CONTENT-CONTRACT-v1.md) + signal registry |
| 7 | Frontend (future) | Slot fill, localization, rendering — **out of v1** |

---

## 3. Inputs (обязательные)

| Input | Источник | Использование |
|-------|----------|---------------|
| `site_type_code` | [registry/SITE-TYPE-REGISTRY-v1.md](../registry/SITE-TYPE-REGISTRY-v1.md) | SITE-TYPE-CONTENT-MAPPING-v1 |
| `blueprint_id` | [blueprints/](../blueprints/) | Content follows Blueprint IA and exclusions |
| `page_type` | [page-architecture/PAGE-TYPE-REGISTRY-v1.md](../page-architecture/PAGE-TYPE-REGISTRY-v1.md) (10) | PAGE-CONTENT-CONTRACTS-v1 |
| `block_id` | [block-registry/BLOCK-REGISTRY-v1.md](../block-registry/BLOCK-REGISTRY-v1.md) (29) | BLOCK-CONTENT-CONTRACTS-v1 |
| Block stance | PAGE-BLOCK-MAPPING, BLUEPRINT-BLOCK-MAPPING | No signals for FORBIDDEN blocks |
| Validation outcome | [page-block-validation/](../page-block-validation/) | Stop before Content binding if FAIL/CRITICAL |
| SEO profile | [seo-architecture/](../seo-architecture/) | Content subordinate to search intent / page SEO role |
| Design pattern | [design-system/](../design-system/) | Pattern family must not contradict required signals |
| Legal Pack | [legal/](../legal/) (FROZEN) | LEGAL_PAGE + form-adjacent signals |
| Legal Entity Card | [legal-entity/](../legal-entity/) | NAP, entity identity signals on CONTACTS/FOOTER |

---

## 4. Outputs (v1)

| Artefact | Файл | Содержание |
|----------|------|------------|
| Content system (this doc) | CONTENT-SYSTEM-v1.md | Layer role, chain, gates |
| Content contract schema | [CONTENT-CONTRACT-v1.md](CONTENT-CONTRACT-v1.md) | Mandatory fields |
| Signal registry | [CONTENT-SIGNAL-REGISTRY-v1.md](CONTENT-SIGNAL-REGISTRY-v1.md) | Architectural signal definitions |
| Block content map | [BLOCK-CONTENT-CONTRACTS-v1.md](BLOCK-CONTENT-CONTRACTS-v1.md) | `block_id` → signals |
| Page content map | [PAGE-CONTENT-CONTRACTS-v1.md](PAGE-CONTENT-CONTRACTS-v1.md) | 10 `page_type` profiles |
| Site type content profile | [SITE-TYPE-CONTENT-MAPPING-v1.md](SITE-TYPE-CONTENT-MAPPING-v1.md) | Core 5 |
| Rules | [CONTENT-RULES-v1.md](CONTENT-RULES-v1.md) | Architecture gates |
| Gaps | [CONTENT-GAPS-v1.md](CONTENT-GAPS-v1.md) | Future work register |

**Не выходят из v1:** финальный copy, headlines, meta descriptions, prompts, generated paragraphs, FAQ Q&A text, review bodies.

---

## 5. Dependencies

| Dependency | Обязательность | При нарушении |
|------------|----------------|---------------|
| Frozen foundation | Hard | Halt — no Content expansion without charter |
| Block Registry v1 (29 ids) | Hard | No new `block_id` in Content workstream |
| Page Type Registry v1 (10 types) | Hard | No new `page_type` |
| Core 5 site types for profiles | Hard for mapping tables | Extended types → SAFE UNKNOWN |
| Page Block Validation PASS (manual) | Soft gate | Documented stop — see §6 |
| SEO Architecture v2 | Hard | Content subordinate to SEO page roles |
| Design System Mapping v1 | Hard | Content aligns with pattern structural role |
| Legal Pack v1 FROZEN | Hard | LEGAL_PAGE, consent-adjacent blocks |
| Legal Entity Discovery v1 | Hard | Entity/NAP signals on contact surfaces |

---

## 6. Stop conditions

| Condition | Action |
|-----------|--------|
| Page Block Validation **FAIL** or **CRITICAL** | **STOP** — resolve block stack before content binding |
| `block_id` FORBIDDEN on page/blueprint | **STOP** — no content contract for that block instance |
| `page_type` not allowed for `site_type_code` | **STOP** — reclassify site or page |
| Request for new site type / page type / block id | **STOP** — registry charter required |
| Request for marketing copy, SEO text, prompts, generation | **OUT OF SCOPE** — register in CONTENT-GAPS-v1 |
| Unsupported factual claims without HITL evidence | **STOP** — see CONTENT-RULES-v1 |
| Legal placeholder gate open | **STOP** downstream content fill on legal routes |
| Operator requests copywriting / generation | **DEFER** — Generation Contracts charter |

---

## 7. Layer artefact index

| # | File | Task |
|---|------|------|
| 1 | CONTENT-SYSTEM-v1.md | Architecture (this document) |
| 2 | CONTENT-CONTRACT-v1.md | Contract field schema |
| 3 | CONTENT-SIGNAL-REGISTRY-v1.md | Signal vocabulary |
| 4 | BLOCK-CONTENT-CONTRACTS-v1.md | Block → signals |
| 5 | PAGE-CONTENT-CONTRACTS-v1.md | Page type profiles |
| 6 | SITE-TYPE-CONTENT-MAPPING-v1.md | Site type profiles |
| 7 | CONTENT-RULES-v1.md | Rules |
| 8 | CONTENT-GAPS-v1.md | Gaps |

---

## 8. Maturity

| Dimension | v1 status |
|-----------|-----------|
| Signal vocabulary | **Defined** — architectural slots only |
| Per-block binding | **Defined** — 29 `block_id` |
| Per-page binding | **Defined** — 10 `page_type` |
| Site type profiles | **Defined** — Core 5 |
| Copywriting / generation | **NOT STARTED** — gaps |
| Content validation automation | **NOT IMPLEMENTED** |

**Label:** Content Architecture Layer v1 — documentation + human-operated signal checklist.

---

## 9. SAFE UNKNOWN

- Optimal signal cardinality per block on Frontend — **UNKNOWN** until Generation/Frontend charters.
- Parity of Content profiles for Extended site types (SAAS, WEB_APPLICATION, MARKETPLACE) — **FUTURE**.
- Automated content-signal validator — **FUTURE** (see CONTENT-GAPS-v1).
- Localization / tone-of-voice systems — **FUTURE**.

---

*Content System version: v1. Canonical location: `workspaces/website-factory-reference-v1/content-contracts/`.*
