# Website Factory — Foundation v1 FREEZE

**Версия:** v1  
**Дата freeze:** 2026-06-01  
**Operator:** APPROVED BY OPERATOR  
**Область:** `workspaces/website-factory-reference-v1/`  
**Статус:** **FROZEN FOUNDATION**

**Не является:** runtime Website Factory, CI-валидатором, orchestration product, production deploy authorization, SEO/content/design generator.

**Связанные документы:** [ARCHITECTURE-FOUNDATION-v1.md](ARCHITECTURE-FOUNDATION-v1.md), [WEBSITE-FACTORY-FOUNDATION-CHECKPOINT-v1.md](WEBSITE-FACTORY-FOUNDATION-CHECKPOINT-v1.md), [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md)

---

## 1. Purpose

Официальный freeze checkpoint для **завершённой** Website Factory Foundation v1.

Документ фиксирует архитектурную базу **до** переключения фокуса на Triumph Manipulator landing improvements и **до** старта SITE-TYPE-SEO-MAPPING-v2.

**Checkpoint only** — без новой архитектуры, реестров, mappings, SEO, Design System или расширения validation.

---

## 2. Freeze date

**2026-06-01**

---

## 3. Current maturity

| Dimension | Level | Evidence |
|-----------|-------|----------|
| **Classification** | Production-ready (documentation) | Site Type Registry v1 — 8 типов |
| **IA planning** | Production-ready (Core 5) | 5 Core Blueprints + Blueprint System v1 |
| **Page contracts** | Production-ready (Core) | 10 `page_type`, PAGE-CONTRACT, matrices |
| **Block vocabulary** | Production-ready (Core) | 29 `block_id`, SITE-TYPE-BLOCK-MATRIX-v2 |
| **Validation semantics** | Production-ready (manual) | Page Block Validation v1 — documentation-only |
| **Legal baseline** | Frozen / pilot-validated | Legal Pack v1 + Triumph V6 Phase 2 |
| **SEO depth** | Shallow (v1) | SITE-TYPE-SEO-MAPPING-v1 — successor v2 **QUEUED** |
| **Design binding** | Partial / reference only | Reference workspace LANDING subset |
| **Automation** | Not implemented | VALIDATION-GAPS, BLUEPRINT-GAPS, BLOCK-GAPS |

**Maturity label:** **Foundation v1 — documentation + human-operated gates**. Не заявляет о shipped Website Factory runtime.

---

## 4. Foundation scope

### In scope (frozen foundation)

| Область | Путь |
|---------|------|
| Site Type Registry | [registry/](registry/) |
| Site Type Blueprints | [blueprints/](blueprints/) |
| Page Architecture | [page-architecture/](page-architecture/) |
| Block Registry | [block-registry/](block-registry/) |
| Page Block Validation | [page-block-validation/](page-block-validation/) |
| Legal Pack + Entity Discovery | [legal/](legal/), [legal-entity/](legal-entity/) |
| Architecture Foundation | [ARCHITECTURE-FOUNDATION-v1.md](ARCHITECTURE-FOUNDATION-v1.md) |
| Reference implementation | `workspaces/website-factory-reference-v1/src/`, Triumph V6 pilot |

### Explicit exclusions (post-freeze until new charter)

| Область | Статус |
|---------|--------|
| SEO Mapping v2 | **QUEUED** — not started |
| Design System Mapping | **QUEUED** |
| Content / Generation contracts | **NOT STARTED** |
| Runtime validator CLI / CI gates | **FUTURE** |
| Extended Type Blueprints | **NOT STARTED** |
| Legal Pack modifications | **FORBIDDEN** — FROZEN |
| New architecture / registries / mappings | **FORBIDDEN** |

---

## 5. Accepted systems

| System | Status | Entry document |
|--------|--------|----------------|
| **Legal Pack v1** | **FROZEN** | [legal/LEGAL-PACK-v1-FREEZE.md](legal/LEGAL-PACK-v1-FREEZE.md) |
| **Legal Entity Discovery v1** | **ACCEPTED** | [legal-entity/](legal-entity/) |
| **Site Type Registry v1** | **ACCEPTED** | [registry/SITE-TYPE-REGISTRY-v1.md](registry/SITE-TYPE-REGISTRY-v1.md) |
| **Site Type Blueprints v1** | **ACCEPTED** (Core 5) | [blueprints/BLUEPRINT-SYSTEM-v1.md](blueprints/BLUEPRINT-SYSTEM-v1.md) |
| **Page Architecture Contracts v1** | **ACCEPTED** | [page-architecture/PAGE-ARCHITECTURE-SYSTEM-v1.md](page-architecture/PAGE-ARCHITECTURE-SYSTEM-v1.md) |
| **Block Registry Alignment v1** | **ACCEPTED** | [block-registry/BLOCK-REGISTRY-v1.md](block-registry/BLOCK-REGISTRY-v1.md) |
| **Page Block Validation v1** | **ACCEPTED** | [page-block-validation/PAGE-BLOCK-VALIDATION-SYSTEM-v1.md](page-block-validation/PAGE-BLOCK-VALIDATION-SYSTEM-v1.md) |
| **Architecture Foundation v1** | **ACCEPTED** | [ARCHITECTURE-FOUNDATION-v1.md](ARCHITECTURE-FOUNDATION-v1.md) |

---

## 6. Frozen status

### FROZEN

| System | Freeze date | Document |
|--------|-------------|----------|
| **Legal Pack v1** (включая Legal Entity Discovery, templates, generation contract, SITE-TYPE-LEGAL-MAPPING-v2, hardening v1.1) | 2026-05-30 | [legal/LEGAL-PACK-v1-FREEZE.md](legal/LEGAL-PACK-v1-FREEZE.md) |
| **Website Factory Foundation v1** (architectural chain Registry → Validation) | 2026-06-01 | this document |

### ACCEPTED

| System | Status |
|--------|--------|
| Legal Entity Discovery v1 | ACCEPTED (frozen with Legal Pack) |
| Site Type Registry v1 | ACCEPTED |
| Site Type Blueprints v1 (Core 5) | ACCEPTED |
| Page Architecture Contracts v1 | ACCEPTED |
| Block Registry Alignment v1 | ACCEPTED |
| Page Block Validation v1 | ACCEPTED |
| Architecture Foundation v1 | ACCEPTED |

### ACTIVE

| Workstream | Status |
|------------|--------|
| Website Factory active workstream | **NONE** |

Operator focus may shift to Triumph Manipulator landing improvements — **outside** Website Factory foundation scope.

### QUEUED

| Workstream | Status |
|------------|--------|
| **SITE-TYPE-SEO-MAPPING-v2** | **QUEUED** — next approved workstream; **not started** |
| **DESIGN SYSTEM MAPPING** | **QUEUED** — after SEO v2 |
| **CONTENT CONTRACTS** | **NOT STARTED** — charter required |
| **GENERATION CONTRACTS** | **NOT STARTED** — charter required |

---

## 7. Do Not Modify Without Explicit Architecture Review

Следующие системы **не изменяются** без explicit operator architecture review и charter:

| System | Location |
|--------|----------|
| **Legal Pack** | [legal/](legal/) + [legal-entity/](legal-entity/) |
| **Legal Entity Discovery** | [legal-entity/](legal-entity/) |
| **Site Type Registry** | [registry/SITE-TYPE-REGISTRY-v1.md](registry/SITE-TYPE-REGISTRY-v1.md) |
| **Blueprint Core Types** | [blueprints/](blueprints/) — LANDING, PROMO, CATALOG, ECOMMERCE, CORPORATE |
| **Page Type Registry** | [page-architecture/PAGE-TYPE-REGISTRY-v1.md](page-architecture/PAGE-TYPE-REGISTRY-v1.md) |
| **Block Registry Canonical IDs** | [block-registry/BLOCK-REGISTRY-v1.md](block-registry/BLOCK-REGISTRY-v1.md) — 29 `block_id` |
| **Validation Severity System** | [page-block-validation/VALIDATION-SEVERITY-SYSTEM-v1.md](page-block-validation/VALIDATION-SEVERITY-SYSTEM-v1.md) |

**Allowed without architecture review:** typo/clarity fixes without semantic drift; cross-link updates pointing **into** frozen docs — только по explicit operator instruction.

---

## 8. Unfreeze conditions

Foundation may be modified only when:

1. **Critical contradiction discovered** — documented conflict between accepted layers that blocks production use.
2. **Real project exposes architecture failure** — pilot or client project demonstrates foundation insufficiency with operator evidence.
3. **Operator approved architecture evolution** — explicit charter naming scope, layers affected, and validation path.
4. **New factory layer officially started** — e.g. SEO Mapping v2, Design System Mapping, Content/Generation contracts — each requires its own workstream charter; does not implicitly unfreeze upstream layers.

---

## 9. Foundation summary (one-page chain)

```text
Site Type
    ↓
Blueprint
    ↓
Page Architecture
    ↓
Block Registry
    ↓
Page Block Validation
    ↓
Future SEO Layer          ← QUEUED (SITE-TYPE-SEO-MAPPING-v2)
    ↓
Future Design Layer       ← QUEUED (Design System Mapping)
    ↓
Future Frontend Layer     ← implementation + partial contracts
```

| Layer | Location | Responsibility |
|-------|----------|----------------|
| Site Type | [registry/](registry/) | Канонические `site_type_code`, цели типа, матрицы v1 |
| Blueprint | [blueprints/](blueprints/) | IA сайта: страницы, block stacks на уровне типа |
| Page Architecture | [page-architecture/](page-architecture/) | Контракт страницы: `page_type`, required/forbidden blocks |
| Block Registry | [block-registry/](block-registry/) | Канонические `block_id`, категории, матрицы |
| Page Block Validation | [page-block-validation/](page-block-validation/) | PASS/FAIL semantics, severity, failure library |
| Future SEO Layer | [registry/SITE-TYPE-SEO-MAPPING-v1.md](registry/SITE-TYPE-SEO-MAPPING-v1.md) → v2 | Per-site-type SEO architecture — **QUEUED** |
| Future Design Layer | external + future mapping | Tokens/components ↔ site types ↔ blocks — **QUEUED** |
| Future Frontend Layer | reference `src/`, client workspaces | HTML/partials/SCSS/JS — per project charter |

**Dependency rule:** upstream слой не переписывается downstream workstream без operator charter.

---

## 10. Validated pilot reference

**Triumph Manipulator V6** — Legal Pilot Phase 2 **COMPLETE** (2026-05-30).

Workspace: `workspaces/triumph-manipulator-landing-v6/`

Validation: Footer Rule, Consent Rule, canonical URLs, zero forbidden placeholders — **PASS**. Build **PASS**.

---

## 11. Freeze verdict

**Website Factory Foundation v1: FROZEN**

- Legal Pack v1 — **FROZEN** (2026-05-30)
- Architectural foundation chain — **FROZEN** (2026-06-01)
- Active Website Factory workstream — **NONE**
- Next approved workstream — **SITE-TYPE-SEO-MAPPING-v2** — **QUEUED, not started**

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Exact calendar for SEO Mapping v2 delivery | **not scheduled** |
| Triumph production deploy authorization | **UNKNOWN** |
| CI automation for legal placeholder / block validation | **FUTURE** — no implementation proof in-repo |
| Operator decision on `STICKY_CTA` vs `CTA` canonical merge | **pending** optional pass — non-blocking |
| Whether Extended Type Blueprints precede or follow Design Mapping | **requires charter** if scope changes |

---

*Foundation Freeze v1 — 2026-06-01. Checkpoint only; no new systems. Canonical location: `workspaces/website-factory-reference-v1/`.*
