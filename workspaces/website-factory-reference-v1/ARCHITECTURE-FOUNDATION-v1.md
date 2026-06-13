# Website Factory — Architecture Foundation v1

**Версия:** v1  
**Дата:** 2026-06-01  
**Operator:** APPROVED BY OPERATOR  
**Область:** `workspaces/website-factory-reference-v1/`  
**Статус:** **FROZEN FOUNDATION** — consolidation checkpoint; post-freeze layers **ACCEPTED** 2026-06-04 — [FOUNDATION-FINALIZATION-PASS-v1.md](FOUNDATION-FINALIZATION-PASS-v1.md)  
**Связанные документы:** [WEBSITE-FACTORY-FOUNDATION-CHECKPOINT-v1.md](WEBSITE-FACTORY-FOUNDATION-CHECKPOINT-v1.md), [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md) (**authoritative status register**), [WEBSITE-FACTORY-RUNTIME-FOUNDATION-SNAPSHOT-v1.md](WEBSITE-FACTORY-RUNTIME-FOUNDATION-SNAPSHOT-v1.md), [seo-architecture/SEO-ARCHITECTURE-SYSTEM-v2.md](seo-architecture/SEO-ARCHITECTURE-SYSTEM-v2.md)

**Не является:** runtime Website Factory, CI-валидатором, orchestration product, production deploy authorization, юридической экспертизой, SEO/content/design generator.

---

## 1. Purpose

Architecture Foundation v1 — **формальная точка консолидации** текущей архитектурной базы Website Factory.

Документ фиксирует **что уже принято оператором**, **что заморожено**, **какие слои связаны**, **какие пробелы уже задокументированы**, и **куда разрешена следующая эволюция** — без добавления новых систем, реестров, blueprint-слоёв или валидаторов.

**Цель checkpoint:**

- Снять неоднозначность «где мы сейчас» после acceptance полного documentation stack (Registry → Runtime Architecture v1).
- Запретить архитектурное расширение frozen-слоёв (кроме bugfix / documentation hygiene по charter).
- Дать единую карту ответственности слоёв для operator, agent и downstream workstreams.

---

## 2. Scope

### In scope (v1 foundation)

| Область | Путь | Роль в foundation |
|---------|------|-------------------|
| Site Type Registry | [registry/](registry/) | Классификация `site_type_code` |
| Site Type Blueprints | [blueprints/](blueprints/) | IA и block stacks на уровне типа сайта |
| Page Architecture | [page-architecture/](page-architecture/) | Контракты страниц (`page_type`) |
| Block Registry | [block-registry/](block-registry/) | Канонические `block_id` и матрицы |
| Page Block Validation | [page-block-validation/](page-block-validation/) | Семантика PASS/FAIL для block stack |
| SEO Architecture Layer v2 | [seo-architecture/](seo-architecture/) | **ACCEPTED** (2026-06-01) — intent, strategy, page SEO contracts, Core 5 profiles |
| Design System Mapping v1 | [design-system/](design-system/) | **ACCEPTED** (2026-06-04) — visual pattern architecture |
| Content Contracts v1 | [content-contracts/](content-contracts/) | **ACCEPTED** (2026-06-04) — content signals |
| Content Validation v1 | [content-validation/](content-validation/) | **ACCEPTED** (2026-06-04) — signal architecture validation |
| Generation Contracts v1 | [generation-contracts/](generation-contracts/) | **ACCEPTED** (2026-06-04) — production orchestration contracts |
| Production QA Architecture v1 | [production-qa/](production-qa/) | **ACCEPTED** (2026-06-04) — Frontend handoff gate |
| Factory Runtime Architecture v1 | [runtime-architecture/](runtime-architecture/) | **ACCEPTED** (2026-06-04) — movement discipline |
| Legal Pack + Entity Discovery | [legal/](legal/), [legal-entity/](legal-entity/) | Core Legal Pack L1–L4 (FROZEN) |
| Reference implementation | `workspaces/website-factory-reference-v1/src/`, Triumph V6 pilot | Battle-tested partials, не канон всех типов |

### Out of scope (explicit)

| Область | Статус |
|---------|--------|
| Factory Engine Architecture v1 (Stages 1–6) | **COMPLETE** (documentation) — [FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md](FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md); RT-G09 **implementation** — **NOT STARTED** |
| Post-Engine doctrine (Manifest, Registry, Tracking Surface) | **COMPLETE** (charters) — `FACTORY-*-CHARTER-v1.md` |
| Runtime validator CLI / CI gates | **FUTURE** |
| Extended Type Blueprints (SAAS, WEB_APPLICATION, MARKETPLACE) | **NOT STARTED** |
| Legal Pack modifications | **FORBIDDEN** — FROZEN |
| Mobile App Factory | **OUT OF SCOPE** |
| Governance expansion | **NOT APPROVED** |

**Approved site types (Registry v1):** `LANDING`, `PROMO`, `CATALOG`, `ECOMMERCE`, `CORPORATE`, `SAAS`, `WEB_APPLICATION`, `MARKETPLACE` — Core production targets: первые пять; Extended — без полной blueprint/validation матрицы в v1.

---

## 3. Current maturity level

| Dimension | Level | Evidence |
|-----------|-------|----------|
| **Classification** | **Production-ready (documentation)** | Site Type Registry v1 — 8 типов, матрицы v1 |
| **IA planning** | **Production-ready (Core 5)** | 5 Core Blueprints + Blueprint System v1 |
| **Page contracts** | **Production-ready (Core)** | 10 `page_type`, PAGE-CONTRACT, matrices |
| **Block vocabulary** | **Production-ready (Core)** | 29 `block_id`, SITE-TYPE-BLOCK-MATRIX-v2 |
| **Validation semantics** | **Production-ready (manual)** | Page Block Validation v1 — documentation-only |
| **Legal baseline** | **Frozen / pilot-validated** | Legal Pack v1 + Triumph V6 Phase 2 |
| **SEO depth** | **Production-ready (Core 5, documentation)** | [seo-architecture/](seo-architecture/) — v1 registry hints superseded |
| **Design binding** | **Partial / reference only** | Reference workspace LANDING subset; visual contract v0 external |
| **Automation** | **Not implemented** | VALIDATION-GAPS, BLUEPRINT-GAPS, BLOCK-GAPS |

**Maturity label:** **Foundation v1 — documentation + human-operated gates**. Не заявляет о shipped Website Factory runtime.

---

## 4. Production direction

Website Factory v1 направлена на **human-operated, documentation-first** production:

1. **Classify** проект → `site_type_code` (Registry).
2. **Select Blueprint** → freeze IA и block intent (Blueprints).
3. **Instantiate page contracts** → per-route architecture (Page Architecture).
4. **Map blocks** → canonical `block_id` (Block Registry).
5. **Validate** block stack → manual checklist / VALIDATION-CONTRACT (Page Block Validation).
6. **Apply Legal Pack** (FROZEN) при production / full-site / PII collection.
7. **Apply accepted downstream:** Design → Content → Generation → Production QA → Runtime movement model (documentation gates).
8. **Architecture v1 closed (documentation):** Factory Engine + post-Engine doctrine **COMPLETE**; **current mode:** Operational Design — [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md).

**Production gate discipline:** FAIL / CRITICAL validation → halt before Design / Frontend. Legal placeholder gate → STOP generation. Frozen Legal Pack → no architectural expansion.

**Reference workspaces:** `workspaces/website-factory-reference-v1/` (LANDING blocks), `workspaces/triumph-manipulator-landing-v6/` (legal pilot).

---

## 5. Layer map (canonical chain)

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
   SEO Layer          ← ACCEPTED (2026-06-01)
        ↓
  Design Layer        ← ACCEPTED (2026-06-04)
        ↓
 Content Contracts    ← ACCEPTED (2026-06-04)
        ↓
 Content Validation   ← ACCEPTED (2026-06-04)
        ↓
 Generation Contracts ← ACCEPTED (2026-06-04)
        ↓
  Production QA        ← ACCEPTED (2026-06-04)
        ↓
 Runtime Architecture ← ACCEPTED (2026-06-04)
        ↓
 Factory Engine       ← COMPLETE (documentation, 2026-06-04)
        ↓
 Post-Engine charters ← COMPLETE (Manifest, Registry, Tracking — doctrine)
        ↓
 Operational Design   ← ACTIVE (human playbooks, binding — not new SYSTEM layers)
        ↓
 Frontend Layer       ← FUTURE (implementation + partial contracts)
```

### Layer responsibilities

| Layer | Location | Responsibility | Downstream consumes |
|-------|----------|----------------|---------------------|
| **Site Type Registry** | [registry/](registry/) | Канонические `site_type_code`, цели типа, матрицы v1 (legal/SEO/block hints), implementation rules | Blueprints, Legal Mapping, все матрицы |
| **Blueprints** | [blueprints/](blueprints/) | IA сайта: обязательные страницы, block stacks на уровне типа, conversion/legal/SEO **scope** (не контент) | Page Architecture, Block Registry mapping |
| **Page Architecture** | [page-architecture/](page-architecture/) | Контракт **страницы**: `page_type`, goals, required/forbidden blocks на уровне route | Block Registry PAGE-BLOCK-MAPPING, Validation |
| **Block Registry** | [block-registry/](block-registry/) | Канонические `block_id`, категории, dependency rules, site-type × block matrix | Validation, Design (future), Frontend partials |
| **Page Block Validation** | [page-block-validation/](page-block-validation/) | Семантика проверки: severity, matrices, failure library, manual PASS/FAIL | Operator gate before Design; future CLI |
| **SEO Layer** | [seo-architecture/SEO-ARCHITECTURE-SYSTEM-v2.md](seo-architecture/SEO-ARCHITECTURE-SYSTEM-v2.md) (**ACCEPTED**) | Per-site-type SEO architecture, block_id awareness | Content / Generation layers |
| **Design Layer** | [design-system/DESIGN-SYSTEM-MAPPING-v1.md](design-system/DESIGN-SYSTEM-MAPPING-v1.md) (**ACCEPTED**) | Visual pattern families ↔ blocks/pages/types | Content Contracts, Frontend |
| **Content Layer** | [content-contracts/CONTENT-SYSTEM-v1.md](content-contracts/CONTENT-SYSTEM-v1.md) (**ACCEPTED**) | Content signals ↔ blocks/pages | Content Validation, Generation |
| **Content Validation** | [content-validation/CONTENT-VALIDATION-SYSTEM-v1.md](content-validation/CONTENT-VALIDATION-SYSTEM-v1.md) (**ACCEPTED**) | Signal architecture PASS/FAIL | Generation Contracts |
| **Generation Layer** | [generation-contracts/GENERATION-SYSTEM-v1.md](generation-contracts/GENERATION-SYSTEM-v1.md) (**ACCEPTED**) | Production package orchestration contract | Production QA, Runtime |
| **Production QA** | [production-qa/PRODUCTION-QA-SYSTEM-v1.md](production-qa/PRODUCTION-QA-SYSTEM-v1.md) (**ACCEPTED**) | Architectural readiness before Frontend | Runtime gates, Frontend charter |
| **Runtime Layer** | [runtime-architecture/RUNTIME-ARCHITECTURE-SYSTEM-v1.md](runtime-architecture/RUNTIME-ARCHITECTURE-SYSTEM-v1.md) (**ACCEPTED**) | Project states, transitions, gates (movement only) | Factory Engine (reference) |
| **Factory Engine** | [FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md](FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md) (**COMPLETE** doc) | Per-project coordination semantics | Operational binding, implementation |
| **Post-Engine doctrine** | `FACTORY-*-CHARTER-v1.md` (**COMPLETE** doc) | Entry, portfolio catalog, operator visibility roles | Implementation charters |
| **Frontend Layer** | reference `src/`, client workspaces | HTML/partials/SCSS/JS implementation | Deploy / QA |

**Dependency rule:** upstream слой **не** переписывается downstream workstream без operator charter. Validation v1 **references** mappings; не мутирует Registry/Blueprints/Page Architecture/Block Registry.

---

## 6. Accepted systems

| System | Status | Purpose |
|--------|--------|---------|
| **Legal Pack v1** | **FROZEN** | Core Legal Pack L1–L4: templates, generation contract, workflow, production rules — [legal/LEGAL-PACK-v1-FREEZE.md](legal/LEGAL-PACK-v1-FREEZE.md) |
| **Legal Entity Discovery v1** | **ACCEPTED** (frozen with Legal Pack) | Discovery юрлица, Legal Entity Card, priority rules, conflict reports — [legal-entity/](legal-entity/) |
| **Site Type Registry v1** | **ACCEPTED** | 8 `site_type_code`, матрицы, implementation rules — [registry/SITE-TYPE-REGISTRY-v1.md](registry/SITE-TYPE-REGISTRY-v1.md) |
| **Site Type Blueprints v1** | **ACCEPTED** (Core 5) | Blueprint System + LANDING, PROMO, CATALOG, ECOMMERCE, CORPORATE — [blueprints/BLUEPRINT-SYSTEM-v1.md](blueprints/BLUEPRINT-SYSTEM-v1.md); Extended Types — not started |
| **Page Architecture Contracts v1** | **ACCEPTED** | Page contracts, 10 page types, matrices, legal page specialization — [page-architecture/PAGE-ARCHITECTURE-SYSTEM-v1.md](page-architecture/PAGE-ARCHITECTURE-SYSTEM-v1.md) |
| **Block Registry Alignment v1** | **ACCEPTED** | 29 `block_id`, mappings, audit, gaps register — [block-registry/BLOCK-REGISTRY-v1.md](block-registry/BLOCK-REGISTRY-v1.md) |
| **Page Block Validation v1** | **ACCEPTED** | First validation layer: rules, matrices, severity, failure library — [page-block-validation/PAGE-BLOCK-VALIDATION-SYSTEM-v1.md](page-block-validation/PAGE-BLOCK-VALIDATION-SYSTEM-v1.md) |
| **SEO Architecture Layer v2** | **ACCEPTED** (2026-06-01) | [seo-architecture/SEO-ARCHITECTURE-SYSTEM-v2.md](seo-architecture/SEO-ARCHITECTURE-SYSTEM-v2.md) |
| **Design System Mapping v1** | **ACCEPTED** (2026-06-04) | [design-system/DESIGN-SYSTEM-MAPPING-v1.md](design-system/DESIGN-SYSTEM-MAPPING-v1.md) |
| **Content Contracts v1** | **ACCEPTED** (2026-06-04) | [content-contracts/CONTENT-SYSTEM-v1.md](content-contracts/CONTENT-SYSTEM-v1.md) |
| **Content Validation v1** | **ACCEPTED** (2026-06-04) | [content-validation/CONTENT-VALIDATION-SYSTEM-v1.md](content-validation/CONTENT-VALIDATION-SYSTEM-v1.md) |
| **Generation Contracts v1** | **ACCEPTED** (2026-06-04) | [generation-contracts/GENERATION-SYSTEM-v1.md](generation-contracts/GENERATION-SYSTEM-v1.md) |
| **Production QA Architecture v1** | **ACCEPTED** (2026-06-04) | [production-qa/PRODUCTION-QA-SYSTEM-v1.md](production-qa/PRODUCTION-QA-SYSTEM-v1.md) |
| **Factory Runtime Architecture v1** | **ACCEPTED** (2026-06-04) | [runtime-architecture/RUNTIME-ARCHITECTURE-SYSTEM-v1.md](runtime-architecture/RUNTIME-ARCHITECTURE-SYSTEM-v1.md) |

**Supporting accepted (not separate architecture layers):**

- Triumph Legal Pilot Phase 2 — `workspaces/triumph-manipulator-landing-v6/` — **COMPLETE**
- Legal Template Hardening v1.1 — part of frozen Legal Pack
- SITE-TYPE-LEGAL-MAPPING-v2 — operationalized via Triumph; frozen

---

## 7. Frozen systems

| System | Freeze date | Document |
|--------|-------------|----------|
| **Legal Pack v1** (включая Legal Entity Discovery, templates, generation contract, SITE-TYPE-LEGAL-MAPPING-v2, hardening v1.1) | 2026-05-30 | [legal/LEGAL-PACK-v1-FREEZE.md](legal/LEGAL-PACK-v1-FREEZE.md) |

### Why frozen systems must not receive architecture expansion

1. **Pilot validation cost** — Triumph V6 Phase 2 прошёл Footer Rule, Consent Rule, canonical URLs, placeholder gate, build PASS. Расширение архитектуры Legal Pack **инвалидирует** freeze baseline без нового pilot charter.
2. **Operator authority** — freeze = explicit operator decision. Новые legal page types, extension packs (ECOMMERCE/SAAS/MARKETPLACE corporate), automatic HTML pipeline — **FORBIDDEN** без нового charter.
3. **Layer separation** — Legal Pack **не** должен поглощать Blueprint/SEO/Design concerns; обратное также верно.
4. **Allowed changes only:** bugfix (ошибки в шаблонах/правилах, не меняющие контракт freeze), typo/clarity без semantic drift, cross-link updates pointing **into** frozen docs — по explicit operator instruction.

**Post-freeze forbidden (until charter):** new legal page generation, Legal Pack structural modifications, Triumph visual redesign in legal scope.

---

## 8. Lessons learned

### Triumph Legal Pilot

- Полная Factory-сборка с PII **требует** legal pages до production; partial/design-only work — исключение по [LEGAL-IMPLEMENTATION-RULES.md](legal/LEGAL-IMPLEMENTATION-RULES.md).
- Pilot Phase 1 выявил **UNKNOWN** `company_name` / `legal_name` при неявном discovery → **STOP GENERATION** корректен.
- Phase 2 после Entity Discovery + operator verification → **PASS** на layout, URLs, placeholders, build.
- Урок: footer-сигналы **недостаточны** как единственный источник юрлица (см. Triumph lesson).

### Legal Entity Discovery

- Обязательный путь: sources → Legal Entity Card → conflict report → operator VERIFIED → Legal Input Sheet → generation.
- Priority rules (ЕГРЮЛ P1 vs footer P4) предотвращают silent merge конфликтующих наименований.
- `card_status = NOT_READY` — явная остановка вместо смешанного audit.

### Legal Layout Rules

- Legal pages **inherit** project content layout and typography (Legal Content Layout Rule) — не отдельный «legal micro-site».
- Footer Rule + Consent Rule — production gates, не рекомендации.
- Placeholder gate в Generation Contract — блокирует недопустимые подстановки.

### Blueprint → Page → Block model

- Blueprint задаёт **site-level** IA и intent; без Page Architecture оставался разрыв «какая страница что требует».
- Page Architecture Contracts v1 закрыли разрыв между Blueprint block stacks и per-route contracts.
- Block Registry Alignment v1 дал стабильные `block_id` (29) и PAGE-BLOCK-MAPPING / BLUEPRINT-BLOCK-MAPPING.
- Residual label drift (human labels в Blueprints; legacy `STICKY_CTA`/`VIDEO` pseudo-ids) — **resolved** для page architecture (2026-06-04); Blueprint label mapping — manual.

### Validation model

- Validation — **отдельный слой** после описательных контрактов; не смешивать с Registry authoring.
- v1 = documentation + manual operator checklist; automated CLI/CI — **FUTURE** ([VALIDATION-ROADMAP-v1.md](page-block-validation/VALIDATION-ROADMAP-v1.md)).
- Severity + failure library дают предсказуемый halt before Design/Frontend.

### SITE-001 WF-V3 — grid discipline (2026-06-13)

- Конфликт ролей **section** vs **container** (`<section class="wf-v3-container">`) вызвал разъезд ширин header/hero/body/footer при визуально сильном дизайне.
- Урок промoted в Foundation: [frontend-rules/WF-GRID-DISCIPLINE-v1.md](frontend-rules/WF-GRID-DISCIPLINE-v1.md) — **MANDATORY** для всех будущих Factory frontend surfaces.
- Promotion report: [reports/WF-GRID-DISCIPLINE-PROMOTION-v1.md](reports/WF-GRID-DISCIPLINE-PROMOTION-v1.md).

---

## 9. Current gaps (consolidated — no new gaps)

Источники: [blueprints/BLUEPRINT-GAPS-v1.md](blueprints/BLUEPRINT-GAPS-v1.md), [page-architecture/PAGE-GAPS-v1.md](page-architecture/PAGE-GAPS-v1.md), [block-registry/BLOCK-REGISTRY-GAPS-v1.md](block-registry/BLOCK-REGISTRY-GAPS-v1.md), [block-registry/BLOCK-GAPS-v1.md](block-registry/BLOCK-GAPS-v1.md), [page-block-validation/VALIDATION-GAPS-v1.md](page-block-validation/VALIDATION-GAPS-v1.md).

### Cross-layer / documentation

| Gap | Severity | Source |
|-----|----------|--------|
| Mobile sticky `CTA` / embedded video media | **CLOSED** (2026-06-04) | FOUNDATION-FINALIZATION-PASS-v1 |
| Blueprint human labels → `block_id` mapping manual | Low | BLOCK-REGISTRY-GAPS |
| `registry/SITE-TYPE-BLOCK-MAPPING-v1` superseded pointer | **CLOSED** (hygiene 2026-06-01) | [HYGIENE-PASS-v1.md](HYGIENE-PASS-v1.md) |
| HEADER_NAV, FILTERS, SEARCH, breadcrumbs — not in Core 29 | Medium (planning) | BLOCK-GAPS |
| ECOMMERCE utility pages (cart/checkout) — deferred page_type | Medium | PAGE-GAPS, VALIDATION-GAPS |
| Extended site types — no blueprint/validation rows | By design | Registry charter required |
| Cross-links / brain polishing | Low | PAGE-GAPS § cross-layer |

### Downstream (accepted architecture; implementation gaps remain)

| Gap | Target workstream |
|-----|-------------------|
| Design token / component mapping | Design System GAPS (DG-01+) — **FUTURE** |
| Copywriting / content QA automation | Content GAPS — **NOT STARTED** |
| Prompt / codegen / workflow engine | Generation GAPS, Runtime GAPS — **NOT STARTED** |
| Automated validation / CI | VALIDATION-ROADMAP phases |
| Factory Engine Architecture v1 | **COMPLETE** (documentation, 2026-06-04) — implementation **NOT STARTED** |
| ECOMMERCE Legal Extension | Legal Pack extension — FUTURE |
| Reference partials beyond LANDING subset | Implementation charter per project |

### Implementation / automation

| Gap | Status |
|-----|--------|
| Validator CLI, JSON Schema, CI integration | NOT IMPLEMENTED |
| Blueprint-level page existence validator | NOT IMPLEMENTED |
| Project manifest standard path | NOT DEFINED |
| Machine schema for Blueprints | NOT DEFINED |

---

## 10. Next evolution path (approved)

| Order | Workstream | Status | Closes (primarily) |
|-------|------------|--------|---------------------|
| **—** | **SITE-TYPE-SEO-MAPPING-v2** | **ACCEPTED** (2026-06-01) | SEO layer |
| **—** | **Design System Mapping v1** | **ACCEPTED** (2026-06-04) | Design layer |
| **—** | **Content Contracts / Validation v1** | **ACCEPTED** (2026-06-04) | Content architecture |
| **—** | **Generation Contracts v1** | **ACCEPTED** (2026-06-04) | Production package contract |
| **—** | **Production QA Architecture v1** | **ACCEPTED** (2026-06-04) | Frontend handoff gate |
| **—** | **Factory Runtime Architecture v1** | **ACCEPTED** (2026-06-04) | Movement model |
| **—** | **Factory Engine Architecture v1** | **COMPLETE** (documentation) | Stages 1–6 + System Boundary |
| **—** | **Post-Engine doctrine charters** | **COMPLETE** (documentation) | RT-G05/10/12 role definitions |
| **1** | **Operational Design** | **ACTIVE** | Human playbooks, manifest/registry/tracking binding — [WEBSITE-FACTORY-ARCHITECTURE-CONSOLIDATION-REVIEW-v1.md](WEBSITE-FACTORY-ARCHITECTURE-CONSOLIDATION-REVIEW-v1.md) |
| **2** | **QA / validation automation** | FUTURE | Manual → semi-auto → automated ([VALIDATION-ROADMAP-v1.md](page-block-validation/VALIDATION-ROADMAP-v1.md)) |

**Explicit non-path:** governance expansion, new site types, Mobile App Factory, automatic legal HTML pipeline (without charter).

---

## 11. Architecture health check

| Criterion | Verdict | Notes |
|-----------|---------|-------|
| **Consistency** | **PASS WITH WARNINGS** | Core chain + downstream layers aligned; Blueprint human label mapping manual; chrome gaps (HEADER_NAV) |
| **Duplication** | **PARTIAL** | `SITE-TYPE-BLOCK-MAPPING-v1` vs v2 matrix; v0 block-registry in `projects/mars-website-factory/` — pointer discipline required |
| **Layer separation** | **PASS** | Registry / Blueprint / Page / Block / Validation / Legal — distinct folders and contracts |
| **Dependency clarity** | **PASS** | Downstream references upstream; validation does not mutate registry |
| **Documentation maturity** | **PASS** | System docs + gaps + roadmap per layer; [HYGIENE-PASS-v1.md](HYGIENE-PASS-v1.md) closed BCP documentation drift (2026-06-01) |

**Overall foundation health:** **PASS WITH WARNINGS** — full documentation stack accepted; not sufficient for full automated generation or Factory Engine implementation.

---

## 12. Factory Engine status (post-governance synchronization)

**Answer: COMPLETE (documentation)** — see [FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md](FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md), [WEBSITE-FACTORY-GOVERNANCE-SYNCHRONIZATION-PASS-v1.md](WEBSITE-FACTORY-GOVERNANCE-SYNCHRONIZATION-PASS-v1.md)

**Reasoning:**

1. **Foundation + Runtime + Engine + post-Engine doctrine** — documentation-complete per [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md).
2. **RT-G09 implementation** (runtime product) — **NOT STARTED** — [runtime-architecture/RUNTIME-GAPS-v1.md](runtime-architecture/RUNTIME-GAPS-v1.md).
3. **Current workstream:** Operational Design — not architecture-first expansion.
4. **Residual warnings (non-blocking):** chrome blocks, gate namespaces, v0 pointer discipline — RW-01–RW-03 in [FOUNDATION-FINALIZATION-PASS-v1.md](FOUNDATION-FINALIZATION-PASS-v1.md).

**Historical:** Engine readiness pre-charter — [ENGINE-READINESS-AUDIT-v1.md](ENGINE-READINESS-AUDIT-v1.md) (superseded for status; audit record retained).

---

## 13. Canonical index

| Layer | Entry document |
|-------|----------------|
| Foundation (this doc) | ARCHITECTURE-FOUNDATION-v1.md |
| **Status register (authoritative)** | WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md |
| Runtime inventory snapshot | WEBSITE-FACTORY-RUNTIME-FOUNDATION-SNAPSHOT-v1.md |
| Finalization pass | FOUNDATION-FINALIZATION-PASS-v1.md |
| Checkpoint (historical) | WEBSITE-FACTORY-FOUNDATION-CHECKPOINT-v1.md |
| Registry | [registry/SITE-TYPE-REGISTRY-v1.md](registry/SITE-TYPE-REGISTRY-v1.md) |
| Blueprints | [blueprints/BLUEPRINT-SYSTEM-v1.md](blueprints/BLUEPRINT-SYSTEM-v1.md) |
| Page Architecture | [page-architecture/PAGE-ARCHITECTURE-SYSTEM-v1.md](page-architecture/PAGE-ARCHITECTURE-SYSTEM-v1.md) |
| Block Registry | [block-registry/BLOCK-REGISTRY-v1.md](block-registry/BLOCK-REGISTRY-v1.md) |
| Validation | [page-block-validation/PAGE-BLOCK-VALIDATION-SYSTEM-v1.md](page-block-validation/PAGE-BLOCK-VALIDATION-SYSTEM-v1.md) |
| SEO Architecture (accepted) | [seo-architecture/SEO-ARCHITECTURE-SYSTEM-v2.md](seo-architecture/SEO-ARCHITECTURE-SYSTEM-v2.md) |
| Design / Content / Generation / QA / Runtime | см. §6 Accepted systems |
| Legal (frozen) | [legal/LEGAL-PACK-v1-FREEZE.md](legal/LEGAL-PACK-v1-FREEZE.md) |
| Frontend grid discipline (mandatory) | [frontend-rules/WF-GRID-DISCIPLINE-v1.md](frontend-rules/WF-GRID-DISCIPLINE-v1.md) |

---

## SAFE UNKNOWN

- Factory Engine **implementation** calendar — **not scheduled** (documentation **COMPLETE**).
- Whether Extended Type Blueprints precede Engine implementation — **requires charter** if scope changes.
- Triumph production deploy authorization — **UNKNOWN** (legal generated; deploy gate external).
- CI automation for legal placeholder / block validation — **FUTURE** — no implementation proof in-repo.

---

*Architecture Foundation v1 — 2026-06-01. Consolidation only; no new systems. Canonical location: `workspaces/website-factory-reference-v1/`.*
