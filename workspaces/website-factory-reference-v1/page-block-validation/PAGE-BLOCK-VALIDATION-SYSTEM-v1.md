# Website Factory — Page Block Validation System v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/page-block-validation/`  
**Статус:** первый validation layer Website Factory — **documentation only**  
**Дата:** 2026-05-31

**Не является:** runtime validator, CLI tool, JSON Schema, design generator, frontend generator, SEO generator, content generator, automation

---

## Назначение

Page Block Validation System v1 — **первый системный слой**, который проверяет, соответствует ли page architecture требуемым блокам для данного `page_type` и `site_type_code`.

Предыдущие слои описывают, **что должно существовать**:

```
Site Type Registry
        ↓
   Blueprints
        ↓
Page Architecture
        ↓
 Block Registry
```

Validation System v1 добавляет **семантику проверки**: как operator или будущий validator определяет PASS / FAIL для block stack страницы.

---

## Scope

### In scope

| Область | Описание |
|---------|----------|
| **Page-level block validation** | Сверка фактического block stack страницы с REQUIRED / OPTIONAL / FORBIDDEN из [PAGE-BLOCK-MAPPING-v1.md](../block-registry/PAGE-BLOCK-MAPPING-v1.md) |
| **Blueprint context** | Валидация выполняется **в контексте** Core Blueprint (`LANDING`, `PROMO`, `CATALOG`, `ECOMMERCE`, `CORPORATE`) |
| **Validation contract** | Канонические поля входа/выхода — [VALIDATION-CONTRACT-v1.md](VALIDATION-CONTRACT-v1.md) |
| **Severity** | Классификация отклонений — [VALIDATION-SEVERITY-SYSTEM-v1.md](VALIDATION-SEVERITY-SYSTEM-v1.md) |
| **Manual validation** | Operator checklist для project IA и pre-Design gate |

### Out of scope

| Область | Статус |
|---------|--------|
| Automated validator implementation | **FUTURE** — см. [VALIDATION-GAPS-v1.md](VALIDATION-GAPS-v1.md) |
| Blueprint-level page existence validation | Отдельный future layer (Blueprint validator) |
| Design / frontend / SEO / content generation | **FORBIDDEN** в этом workstream |
| Extended site types (`SAAS`, `WEB_APPLICATION`, `MARKETPLACE`) | **нет** validation rows без charter |
| ECOMMERCE utility routes (`/cart/`, `/checkout/`) | Reference rules в PAGE-BLOCK-MAPPING; отдельный `page_type` — **FUTURE** |

---

## Lifecycle

```
1. CLASSIFY
   site_type_code + page_type + Blueprint ref
        ↓
2. RESOLVE RULES
   PAGE-BLOCK-MAPPING-v1 + CORE-PAGE-ARCHITECTURES-v1
   + Blueprint block exclusions (if any)
        ↓
3. COLLECT ACTUAL STACK
   Project IA / page contract `required_blocks` + implemented blocks
        ↓
4. VALIDATE
   Apply PAGE-BLOCK-VALIDATION-RULES-v1
        ↓
5. EMIT RESULT
   validation_result → PASS | FAIL | PASS_WITH_WARNINGS
        ↓
6. GATE
   FAIL / CRITICAL → halt before Design / Frontend
   WARNING → document + operator decision
   PASS → proceed
```

**Gate placement:** после Page Architecture + Block Registry alignment, **до** Design System Mapping и Frontend.

---

## Required chain

```
Blueprint
    ↓
Page Architecture  (page_type, page contract, block stack intent)
    ↓
Required Blocks    (authoritative: PAGE-BLOCK-MAPPING-v1)
    ↓
Validation         (this system — manual v1)
    ↓
PASS / FAIL
```

**Правило:** Validation **не переопределяет** Block Registry. Registry и mapping — source of truth; validation **применяет** их.

---

## Relationship to upstream layers

### Blueprints

| Связь | Описание |
|-------|----------|
| **Input** | `site_type_code`, Blueprint `required_pages`, Blueprint block exclusions |
| **Matrix** | [BLUEPRINT-VALIDATION-MATRIX-v1.md](BLUEPRINT-VALIDATION-MATRIX-v1.md) — site-wide block stance + required pages |
| **Rule** | Page validation **не заменяет** Blueprint validation; Blueprint задаёт контекст (например, CATALOG без `CART`) |

**Ссылки:** [blueprints/BLUEPRINT-SYSTEM-v1.md](../blueprints/BLUEPRINT-SYSTEM-v1.md), [block-registry/BLUEPRINT-BLOCK-MAPPING-v1.md](../block-registry/BLUEPRINT-BLOCK-MAPPING-v1.md)

### Page Architecture

| Связь | Описание |
|-------|----------|
| **Input** | `page_type`, Page Contract fields (`required_blocks`, `optional_blocks`, `forbidden_blocks`) |
| **Source stacks** | [CORE-PAGE-ARCHITECTURES-v1.md](../page-architecture/CORE-PAGE-ARCHITECTURES-v1.md) |
| **Rule** | Page Contract **must not** weaken FORBIDDEN stances; validation checks compliance |

**Ссылки:** [page-architecture/PAGE-ARCHITECTURE-SYSTEM-v1.md](../page-architecture/PAGE-ARCHITECTURE-SYSTEM-v1.md), [page-architecture/PAGE-CONTRACT-v1.md](../page-architecture/PAGE-CONTRACT-v1.md)

### Block Registry

| Связь | Описание |
|-------|----------|
| **Input** | Canonical `block_id` keys — [BLOCK-REGISTRY-v1.md](../block-registry/BLOCK-REGISTRY-v1.md) |
| **Stance matrix** | [PAGE-BLOCK-MAPPING-v1.md](../block-registry/PAGE-BLOCK-MAPPING-v1.md) |
| **Rule** | Unknown `block_id` in stack → validation ERROR |

**Ссылки:** [block-registry/BLOCK-CONTRACT-v1.md](../block-registry/BLOCK-CONTRACT-v1.md)

### Site Type Registry

| Связь | Описание |
|-------|----------|
| **Input** | `site_type_code` ∈ Core Types for v1 validation |
| **Page compatibility** | [SITE-TYPE-PAGE-MATRIX-v1.md](../page-architecture/SITE-TYPE-PAGE-MATRIX-v1.md) |
| **Rule** | FORBIDDEN `page_type` for site type → validation FAIL before block check |

**Ссылки:** [registry/SITE-TYPE-REGISTRY-v1.md](../registry/SITE-TYPE-REGISTRY-v1.md)

### Legal Pack

| Связь | Описание |
|-------|----------|
| **Input** | `LEGAL_PAGE` contract, Footer Rule, `LEGAL_LINKS` on marketing routes |
| **Rule** | Legal routes: marketing blocks FORBIDDEN; `LEGAL_LINKS` REQUIRED on all other production pages when Legal Pack applies |

**Ссылки:** [legal/LEGAL-IMPLEMENTATION-RULES.md](../legal/LEGAL-IMPLEMENTATION-RULES.md), [page-architecture/LEGAL-PAGE-CONTRACT-v1.md](../page-architecture/LEGAL-PAGE-CONTRACT-v1.md)

---

## Relationship to future validators

| Future component | Role | v1 status |
|------------------|------|-----------|
| Manual operator checklist | Human applies rules from this folder | **ACTIVE** (v1 delivery) |
| Semi-automatic diff checker | Compare IA doc block list vs mapping | **FUTURE** |
| CLI validator | Read project manifest → emit VALIDATION-CONTRACT | **FUTURE** |
| Blueprint validator | Required pages + site-wide block stance | **FUTURE** |
| Frontend / page scanner | DOM or template scan vs contract | **FUTURE** |
| Runtime QA layer | Production monitoring | **FUTURE** |

Evolution path: [VALIDATION-ROADMAP-v1.md](VALIDATION-ROADMAP-v1.md)

---

## Document map (this folder)

| Document | Purpose |
|----------|---------|
| [VALIDATION-CONTRACT-v1.md](VALIDATION-CONTRACT-v1.md) | Canonical input/output fields |
| [PAGE-BLOCK-VALIDATION-RULES-v1.md](PAGE-BLOCK-VALIDATION-RULES-v1.md) | Validation logic |
| [PAGE-TYPE-VALIDATION-MATRIX-v1.md](PAGE-TYPE-VALIDATION-MATRIX-v1.md) | Per `page_type` rules + severity |
| [BLUEPRINT-VALIDATION-MATRIX-v1.md](BLUEPRINT-VALIDATION-MATRIX-v1.md) | Per Blueprint critical points |
| [VALIDATION-SEVERITY-SYSTEM-v1.md](VALIDATION-SEVERITY-SYSTEM-v1.md) | INFO / WARNING / ERROR / CRITICAL |
| [VALIDATION-FAILURE-LIBRARY-v1.md](VALIDATION-FAILURE-LIBRARY-v1.md) | Common failures + corrections |
| [VALIDATION-GAPS-v1.md](VALIDATION-GAPS-v1.md) | Known missing capabilities |
| [VALIDATION-ROADMAP-v1.md](VALIDATION-ROADMAP-v1.md) | Future evolution |

---

## Alignment verification (v1 pass)

Cross-layer check performed at authoring time — details in [VALIDATION-GAPS-v1.md](VALIDATION-GAPS-v1.md) and task REPORT.

| Layer | Alignment status |
|-------|------------------|
| Site Type Registry → Blueprints | **ALIGNED** (Core Types) |
| Blueprints → Page Architecture | **ALIGNED** with noted drift items |
| Page Architecture → Block Registry | **ALIGNED** — mobile sticky `CTA` + media embed notes resolved (2026-06-04) |
| Block Registry → Validation System | **ALIGNED** — validation references PAGE-BLOCK-MAPPING as authority |

**Known inconsistencies (document, do not auto-fix in validation v1):**

1. `STICKY_CTA` — REQUIRED in CORE-PAGE-ARCHITECTURES `LANDING_PAGE`; **not** in BLOCK-REGISTRY-v1 → treat as **WARNING** until registry charter
2. `VIDEO` — optional in CORE-PAGE-ARCHITECTURES; **not** in BLOCK-REGISTRY-v1 → ignore or HITL
3. OR-groups (`TRUST` or `TESTIMONIALS`; `BENEFITS` or `FEATURES`) — validation rules in [PAGE-BLOCK-VALIDATION-RULES-v1.md](PAGE-BLOCK-VALIDATION-RULES-v1.md)
4. `LEGAL_PAGE` — no marketing `required_blocks`; `LEGAL_LINKS` validated on **other** routes, not on legal body

---

## SAFE UNKNOWN

- Operator COMPLETE gate for Block Registry Alignment v1 — **pending** (validation authored in parallel)
- Exact JSON manifest format for future CLI — **not defined**
- Automated OR-group detection — **manual v1 only**

---

*Page Block Validation System version: v1. Canonical location: `workspaces/website-factory-reference-v1/page-block-validation/`.*
