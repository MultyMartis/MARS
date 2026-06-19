# REPORT — FOUNDRY REGISTRY LAYER AUDIT

**Дата:** 2026-06-18  
**Режим:** аудит только — исходные документы **не изменялись**  
**Контекст:** WF-A01 и WF-A02 завершены; WF-A03 (Pixel Factory) — **DEFERRED**  
**Область аудита:** Registry Layer Website Factory (`workspaces/website-factory-reference-v1/` — канон v1) + legacy v0 (`projects/mars-website-factory/`) + операционные ссылки из OPERATIONAL-INDEX и roadmap

**Терминология:** строка **FOUNDRY** в репозитории **не найдена** как отдельный продукт или путь. В этом отчёте **FOUNDRY Registry Layer** = документированный слой реестров и blueprint Website Factory (см. SAFE UNKNOWN).

---

## Executive Summary

Registry Layer Website Factory **существует в репозитории** и на уровне **архитектурной документации** прошёл Foundation v1 freeze (2026-06-01) с последующими acceptances (SEO v2, Design System, Content, Generation, Production QA, Runtime — до 2026-06-04). Это **не** runtime, **не** machine-enforced registry service, **не** production-scale автоматическая генерация.

**Главный вывод:** подозрение оператора **подтверждается частично**:

| Слой | Документация | Операционная полнота | Production-scale |
|------|--------------|----------------------|------------------|
| Site Type Registry v1 | **Сильная** (8 типов) | Core 5 — готовы к human-operated planning | Extended 3 — только классификация |
| Block Registry v1 | **Сильная** (29 `block_id`) | Матрицы и контракты — ACCEPTED | Reference code ~**31%** (9/29); критические пробелы HEADER_NAV, FILTERS, SEARCH |
| Commercial Pattern Library | **Слабая** | 1 интерактивный паттерн + разрозненная governance | Не библиотека в смысле каталога pattern_id |
| SEO Pattern Library (как в registries.md §4) | **Не доставлена** как отдельный модуль | Заменена слоем **seo-architecture/** v2 (ACCEPTED) | Архитектура — да; meta/keyword generation — нет |
| Page Blueprint Layer | **Сильная** для Core 5 | 5 канонических blueprint + Page Architecture (10 `page_type`) | Extended types без blueprint; ECOMMERCE legal extension — FUTURE |

**Критический системный риск:** **двойной канон** — v0 (`site-type-registry-v0.md`, `block-registry-v0.md`, snake_case IDs) vs v1 (`website-factory-reference-v1/`, UPPER_SNAKE_CASE). Операционные документы Wave 4–6 (`curated-library-index-v1.md`, `block-quality-tiers-v1.md`) всё ещё ссылаются на **v0** block_id. Без явного charter миграции это **drift**, а не «два равных канона».

**Рекомендация по приоритету (Registry Expansion vs WF-A03):** до charter WF-A03 и отдельного Research Pass — **Registry Expansion (implementation + hygiene)** важнее для режима `TEMPLATE_ART` и для снятия ложной зрелости; WF-A03 (Vision, Visual Diff, Pixel QA Runtime) **не закрывает** пробелы отсутствующих structural blocks и dual-registry drift.

---

## Site Type Registry

### Существование и канон

| Артефакт | Путь | Статус |
|----------|------|--------|
| **Канон v1** | `workspaces/website-factory-reference-v1/registry/SITE-TYPE-REGISTRY-v1.md` | **ACCEPTED** |
| Legacy v0 | `projects/mars-website-factory/site-type-registry-v0.md` | **documented**; явно **не канон v1** |
| Матрица, legal/SEO/block mapping | `registry/SITE-TYPE-MATRIX-v1.md`, `SITE-TYPE-LEGAL-MAPPING-v1.md` (historical), `SITE-TYPE-BLOCK-MAPPING-v1.md` (superseded) | v1 + cross-links к legal v2 и block-registry |

### Объём

- **v1:** **8 типов** — Core 5 (`LANDING`, `PROMO`, `CATALOG`, `ECOMMERCE`, `CORPORATE`) + Extended 3 (`SAAS`, `WEB_APPLICATION`, `MARKETPLACE`)
- **v0:** **10 типов** (`landing`, `service_landing`, `promo_site`, `corporate_site`, `catalog_site`, `ecommerce`, `geo_landing`, `seo_landing`, `ai_visibility_page`, `hybrid_commercial`) — иная таксономия, **без 1:1 mapping** к v1 без charter

### Детализация

**v1 Core types** — для каждого: code, name, description, primary goal, page count, conversion model, traffic sources, included/excluded features, notes. Уровень детализации **достаточен** для intake, blueprint selection и HITL.

**v1 Extended types** — описаны на уровне классификации; явно: *«Website Factory v1 blocks/SEO defaults не применяются без отдельного charter»*.

**v0** — расширенный field glossary (SEO_model, CTA_model, trust_model, QA_focus, HITL_required и т.д.) на **каждую** из 10 строк; глубже по **операционным полям**, но привязан к **устаревшим** `site_type_id`.

### Оценка по типам (v1)

| site_type_code | Группа | Readiness | Обоснование |
|----------------|--------|-----------|-------------|
| `LANDING` | Core | **Production Ready** (documentation + reference pilot) | Blueprint ACCEPTED; reference workspace; Triumph legal pilot; RU QA preset |
| `PROMO` | Core | **Partial** | Blueprint ACCEPTED; нет полноценного reference workspace как эталона PROMO |
| `CATALOG` | Core | **Partial** | Blueprint ACCEPTED; catalog blocks в registry без reference partials; faceted SEO — FUTURE |
| `ECOMMERCE` | Core | **Partial** | Blueprint ACCEPTED; Legal Extension E1–E4 **не доставлен**; checkout/cart — registry only |
| `CORPORATE` | Core | **Partial** | Blueprint ACCEPTED; hybrid-by-design требует HITL per route group; shallow implementation |
| `SAAS` | Extended | **Concept Only** | Классификация; нет blueprint; legal FUTURE |
| `WEB_APPLICATION` | Extended | **Concept Only** | Явно not traditional website; v1 defaults не применяются |
| `MARKETPLACE` | Extended | **Concept Only** | Highest complexity; classification and mapping only |

### v0-only типы (нет прямого v1 аналога)

`service_landing`, `geo_landing`, `seo_landing`, `ai_visibility_page`, `hybrid_commercial` — покрываются **частично** через Core/Extended + project notes, но **не как отдельные** `site_type_code` v1. Для programmatic/geo/AI visibility — **Concept Only** в v1.

---

## Block Registry

### Существование и канон

| Артефакт | Путь | Статус |
|----------|------|--------|
| **Канон v1** | `workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md` | **ACCEPTED** — 29 `block_id` |
| Сопутствующие | BLOCK-CONTRACT, SITE-TYPE-BLOCK-MATRIX-v2, PAGE-BLOCK-MAPPING, BLUEPRINT-BLOCK-MAPPING, BLOCK-DEPENDENCY-RULES, BLOCK-REGISTRY-GAPS, BLOCK-GAPS, BLOCK-REGISTRY-AUDIT | Документированы |
| Legacy v0 | `projects/mars-website-factory/block-registry-v0.md` | **16 блоков**, snake_case — **не канон** |
| Операционная библиотека | `projects/mars-website-factory/curated-library-index-v1.md` | **9 блоков** с v0 именами (`hero`, `lead_form`, …) |

### Объём покрытия

- **29 canonical block_id** (HERO, BENEFITS, FEATURES, … FOOTER) — Core 5 site types
- **Extended site types** — явно **out of Core Library v1**
- **Reference partials:** 9 секций в `website-factory-reference-v1/src/partials/sections/` — **~31%** registry coverage
- **Реализованные:** hero, social_proof, pricing, lead_form, cta_band, contact_block, sticky_cta, faq, cases
- **Не реализованы в reference:** FEATURES, CATEGORY_GRID, REVIEWS, CATALOG/ECOMMERCE commerce chain (CART, CHECKOUT, PAYMENT, DELIVERY), и др.

### Качество описаний

**Сильные стороны:**

- Единая field schema (BLOCK-CONTRACT-v1)
- Conversion roles, categories, dependencies, exclusions
- Трёхуровневые матрицы: site type × block, blueprint × block, page type × block
- Audit и gaps registers с честными OPEN items

**Слабые стороны:**

- 26 из 29 записей — **abbreviated schema** (не все `allowed_page_types` на legacy entries)
- Human labels в Blueprints («Social proof») vs `block_id` — **PARTIAL** operator mapping
- Отсутствующие канонические block_id: **HEADER_NAV**, **FILTERS**, **SEARCH**, breadcrumbs, pagination, thank-you blocks, blog teaser (BLOCK-GAPS-v1)
- `social_proof.html` не разделяет TRUST vs TESTIMONIALS на уровне кода

### Пригодность для Template-Art

По [website-factory-production-modes-charter-v1.md](../projects/mars-website-factory/website-factory-production-modes-charter-v1.md) (WF-A01): в режиме **`TEMPLATE_ART`** реестры (IA, blocks) — **SSOT**; визуал производится внутри Factory foundations.

| Критерий | Оценка |
|----------|--------|
| Планирование страницы по block_id | **Да** — для Core 5 при human-operated discipline |
| Выбор блоков без FIG | **Частично** — vocabulary полный, **визуальные** паттерны — в design-system (VF_*), не в block registry |
| Сборка из curated library | **Только LANDING-подмножество** — 9 блоков, v0 naming; не синхронизировано с UPPER_SNAKE v1 |
| CATALOG / ECOMMERCE / CORPORATE Template-Art | **Нет** — нет reference partials, нет structural blocks (nav, filters) |
| Machine validation | **Нет** — documentation-only PASS/FAIL semantics |

**Вердикт Template-Art:** **Partial** — архитектурно пригоден для **LANDING** и частично **PROMO** при ручной сборке; **не production-scale** для catalog/ecommerce без registry v1.1 (structural blocks) и расширения reference implementation.

---

## Commercial Pattern Library

### Состав (фактический)

| Источник | Что есть |
|----------|----------|
| [registries.md](../projects/mars-website-factory/registries.md) §3 | Заявлен **delivered (v1):** `scroll_process_timeline` — [scroll-process-timeline-pattern-v1.md](../projects/mars-website-factory/scroll-process-timeline-pattern-v1.md) |
| [BLUEPRINT-GAPS-v1.md](../workspaces/website-factory-reference-v1/blueprints/BLUEPRINT-GAPS-v1.md) G5 | **Conversion patterns library — NOT queued**; нет canonical pattern IDs (lead-form-v1, rfq-v1, checkout-guest-v1) |
| [design-system/VISUAL-PATTERN-REGISTRY-v1.md](../workspaces/website-factory-reference-v1/design-system/VISUAL-PATTERN-REGISTRY-v1.md) | **~40+ VF_*** visual pattern families — **архитектура дизайна**, не Commercial Pattern Library |
| Governance рядом | `commercial-density-governance.md`, `commercial-landing-pressure-model.md`, `cta-philosophy-governance.md` — политики, не каталог паттернов |
| ORCA (вне WF canon) | `projects/orca/evolution/commercial-pattern-evolution-v1.md` — отдельный продуктовый контур |

### Completeness

- **Как «библиотека» из registries.md:** **~5%** — один документированный интерактивный паттерн + suggested fields для будущих
- **Как commercial conversion semantics в Blueprints:** conversion requirements **per Blueprint** — есть
- **Как visual composition catalog:** VISUAL-PATTERN-REGISTRY — **Partial** (architecture only, no CSS/Figma)

### Применимость

- `scroll_process_timeline` — **validated** на Triumph Cargo Taxi DEV; применим к service/process verticals с HITL
- PAS, testimonial+logo pairing, urgency framing из registries.md examples — **Concept Only** (нет pattern_id документов)
- Analytics event contract, A/B policy — **отсутствуют** (BLUEPRINT-GAPS G5)

**Вердикт:** Commercial Pattern Library в смысле **отдельного реестра pattern_id** — **Concept Only / Minimal**; единственный production-documented паттерн — **Partial**.

---

## SEO Pattern Library

### Существование

Отдельный файл **«SEO Pattern Library»** из [registries.md](../projects/mars-website-factory/registries.md) §4 **не доставлен** (таблица suggested fields + examples только).

**Фактический канон:** `workspaces/website-factory-reference-v1/seo-architecture/` — **SEO Architecture Layer v2**, **ACCEPTED** 2026-06-01:

| Документ | Роль |
|----------|------|
| SEO-ARCHITECTURE-SYSTEM-v2 | Система слоя |
| SITE-TYPE-SEO-MAPPING-v2 | Профили Core 5 |
| SEARCH-INTENT-MODEL-v1 | 8 intent types |
| PAGE-SEO-CONTRACT-v1 | Контракт страницы |
| SEO-ARCHITECTURE-MATRIX-v1 | site × intent × page_type |
| SEO-STRATEGY-CONTRACT-v1, SEO-IMPLEMENTATION-RULES-v1 | Стратегия и правила |
| SEO-ARCHITECTURE-GAPS-v1 | Пробелы |

### Зрелость

| Аспект | Уровень |
|--------|---------|
| Архитектурные решения до контента (intent, indexation, exclusions) | **Production Ready** (documentation) для Core 5 |
| Связка Site Type → Blueprint → Page → SEO | **Да** — задокументирована |
| Title/meta/schema **templates** | **Отсутствуют** (SEO-ARCHITECTURE-GAPS §3) |
| Keyword architecture, cannibalization | **Отсутствуют** |
| Faceted SEO (CATALOG) | **FUTURE** |
| Extended types SEO parity | **Shallow** — только registry v1 hints |
| Automated validation / CI | **NOT IMPLEMENTED** |

### Пригодность для генерации blueprint

- **Генерация IA / page scope / SEO requirements pointer в Blueprint:** **Да** — operator + agent могут заполнить `seo_requirements` из v2 mapping
- **Генерация конкретных title/description/JSON-LD:** **Нет** — явно out of scope v2
- **Связь с page-blueprint-contract-v0:** v0 ссылается на **SEO Pattern Library (planned)** — **устаревшая** формулировка относительно seo-architecture v2

**Вердикт:** как **SEO Pattern Library** (registries.md) — **Concept Only**; как **SEO Architecture Layer v2** — **Partial → Production Ready** для planning blueprint, **не** для content automation.

---

## Page Blueprint Layer

### Стандартизированные blueprint

**Канон:** `workspaces/website-factory-reference-v1/blueprints/`

| Blueprint | site_type_code | Файл | Статус |
|-----------|----------------|------|--------|
| Landing | `LANDING` | LANDING-BLUEPRINT-v1.md | ACCEPTED |
| Promo | `PROMO` | PROMO-BLUEPRINT-v1.md | ACCEPTED |
| Catalog | `CATALOG` | CATALOG-BLUEPRINT-v1.md | ACCEPTED |
| Ecommerce | `ECOMMERCE` | ECOMMERCE-BLUEPRINT-v1.md | ACCEPTED |
| Corporate | `CORPORATE` | CORPORATE-BLUEPRINT-v1.md | ACCEPTED |

**Система:** BLUEPRINT-SYSTEM-v1, BLUEPRINT-CONTRACT-v1, BLUEPRINT-IMPLEMENTATION-RULES-v1, BLUEPRINT-COMPARISON-MATRIX-v1, BLUEPRINT-GAPS-v1

**Extended types:** blueprint **отсутствуют** (by design v1)

### Page types (связанный слой)

`page-architecture/PAGE-TYPE-REGISTRY-v1.md` — **10 минимальных** `page_type`:

`HOME_PAGE`, `LANDING_PAGE`, `SERVICE_PAGE`, `CATEGORY_PAGE`, `PRODUCT_PAGE`, `ABOUT_PAGE`, `CONTACT_PAGE`, `FAQ_PAGE`, `REVIEWS_PAGE`, `LEGAL_PAGE`

**Расширения (не в минимальном реестре):** `CART_PAGE`, `CHECKOUT_PAGE`, `ORDER_CONFIRMATION_PAGE` — ECOMMERCE only, documented in PAGE-DEPENDENCY-RULES

### Legacy / page-level

- `projects/mars-website-factory/page-blueprint-contract-v0.md` — контракт **уровня страницы** (v0, snake_case, привязка к v0 registries)
- `page-blueprint-qa-checklist-v0.md` — QA slice
- Reference case: `reference-cases/triumph-manipulator-landing/page-blueprint-v0.md` — case artifact, не канон

### Покрытие

| Уровень | Покрытие |
|---------|----------|
| Site type → IA skeleton | **Core 5 — полное** |
| Page type contracts | **10 типов + ECOMMERCE utility** |
| Page → Block validation | **ACCEPTED** (page-block-validation/) |
| Machine Blueprint instance (`project.blueprint.yaml`) | **Нет** (BLUEPRINT-GAPS G6) |
| Automatic full site generation | **Нет** |

**Вердикт Page Blueprint Layer:** **Production Ready** (documentation) для **планирования Core 5**; **Partial** для end-to-end generation и Extended types.

---

## Coverage Matrix

| Registry / Layer | Coverage (документы) | Coverage (implementation) | Quality (описания) | Production Readiness |
|------------------|----------------------|---------------------------|--------------------|----------------------|
| **Site Type Registry v1** | 8/8 типов | N/A (classification) | High (Core), Medium (Extended) | Core 5: **Ready (doc)**; Extended: **Concept** |
| **Site Type Registry v0** | 10/10 типов | Ops docs still cite | High field glossary | **Legacy** — drift risk |
| **Block Registry v1** | 29/29 block_id | ~9/29 partials (~31%) | High structure; gaps documented | **Partial** — LANDING only battle-tested |
| **Block Registry v0** | 16 blocks | 9 curated (v0 names) | Medium-high per block | **Legacy** — use v1 for new work |
| **Commercial Pattern Library** | 1 pattern | 1 DEV-validated case | High for one pattern | **Concept / Minimal** |
| **SEO Pattern Library** (planned) | 0 standalone | — | — | **Absent** |
| **SEO Architecture v2** | Core 5 profiles + matrices | No automation | High architecture | **Ready (planning)** / **Not (generation)** |
| **Page Blueprints v1** | 5/5 Core | LANDING reference only | High | **Ready (doc)** / **Partial (build)** |
| **Page Architecture v1** | 10 page types | Partial ECOMMERCE utility | High | **Accepted** |
| **Visual Pattern Registry** | ~40 VF_* families | No Figma/CSS kit | Architecture-only | **Partial** |
| **Content / Generation contracts** | ACCEPTED 2026-06-04 | No runtime | High | **Documentation only** |

---

## Critical Gaps

### 1. Dual-registry drift (v0 ↔ v1) — **Highest systemic gap**

Два параллельных namespace: `landing` vs `LANDING`, `hero` vs `HERO`, 10 vs 8 site types. Операционные Wave 4–6 артефакты не полностью переведены на v1. Без binding charter любой agent/operator может смешать ID и **ложно зелёный** compatibility.

### 2. Implementation cliff (registry vs reference code)

29 block_id при 9 partials — registry **опережает** Factory implementation на **~69%**. Для `TEMPLATE_ART` и multi-type projects это главный **операционный** пробел, не закрываемый Pixel QA automation alone.

### 3. Missing structural block_id

HEADER_NAV, FILTERS, SEARCH, breadcrumbs, pagination — **требуются Blueprints**, но **отсутствуют** в Core 29. Блокирует честный CATALOG/ECOMMERCE Template-Art и page-block validation на практике.

### 4. Commercial Pattern Library не оформлена

Один паттерн + governance ≠ библиотека. Нет pattern_id catalog, analytics contract, ethical constraint matrix per pattern.

### 5. SEO content layer отсутствует

SEO Architecture v2 сильна для **решений**, но title/meta/schema **templates** и keyword mapping — **не доставлены**. «SEO Pattern Library» из roadmap Phase 1 registries **не существует** как файл.

### 6. ECOMMERCE legal + conversion gap

Legal Pack Extension E1–E4 — **FUTURE**; checkout path — registry/documentation without templates and legal copy generation.

### 7. No machine-readable registry export

JSON Schema / YAML для site types, blocks, blueprints — **SAFE UNKNOWN** / not defined. Блокирует tooling scale без human markdown discipline.

---

## Roadmap Impact

### Текущее состояние roadmap (WF-Axx)

| ID | Status |
|----|--------|
| WF-A01 Production Modes | **Complete** |
| WF-A02 Validation Architecture (+ VL3 Domains Pass 02) | **Complete** |
| WF-A03 Pixel Factory Expansion | **DEFERRED** — требует отдельный Web-GPT Research Pass; forbidden auto-start |

### Registry Expansion vs WF-A03 Pixel Factory

| Фактор | Registry Expansion | WF-A03 Pixel Factory |
|--------|-------------------|----------------------|
| Закрывает dual-registry drift | **Да** (hygiene + binding) | **Нет** |
| Закрывает missing HEADER_NAV / filters | **Да** (registry v1.1 charter) | **Нет** |
| Расширяет reference partials для Template-Art | **Да** | Косвенно (QA после build) |
| Улучшает PIXEL_PERFECT QA | Косвенно | **Да** (Vision, Visual Diff) |
| Зависит от WF-A01/A02 | Нет | **Да** — preconditions met |
| Runtime в repo | **Нет** (оба — documentation) | **Нет** |

**Вывод:** при готовности WF-A01/A02 **следующий высокий ROI** для Factory — **Registry Expansion (implementation + v0→v1 operational binding)**, особенно если ближайшие проекты — `TEMPLATE_ART` (OCPilot Site-001 trajectory, FP-0002 lessons). **WF-A03** оправдан, когда primary bottleneck — **visual verification** в `PIXEL_PERFECT`, а не отсутствие block vocabulary и structural IA.

**Согласование с WEBSITE-FACTORY-NEXT-PRIORITIES-v1:** Foundation layers **ACCEPTED**; active mode — **Operational Design**, не architecture-first expansion. Registry work = **targeted operational gaps**, не новая governance wave.

---

## Risks

| Risk | Severity | Mitigation (documentation-only) |
|------|----------|-------------------------------|
| Agent uses v0 `block_id` on v1 Blueprint | **High** | Explicit charter: v1 canonical; v0 banner in ops docs |
| False «registry complete» narrative | **High** | Treat ACCEPTED as **architecture**, not implementation |
| CATALOG project without FILTERS block_id | **High** | HITL + record OPEN gap; no pretend PLP completeness |
| ECOMMERCE go-live without Legal Extension | **High** | Staging-only with HITL per BLUEPRINT-GAPS G7 |
| WF-A03 started without Research Pass | **Medium** | roadmap.md operator reminder |
| Extended type misclassified as Core | **Medium** | SITE-TYPE-REGISTRY v1 Extended section |

---

## SAFE UNKNOWN

- **FOUNDRY** как именованный продукт/репозиторий в tree — **не обнаружен**; аудит интерпретирован как Website Factory Registry Layer.
- Единый owner миграции v0 → v1 для live projects (Triumph, OCPilot Site-001, FP-0002) — **не зафиксирован** в прочитанных документах.
- Даты COMPLETE gate для Block Registry Alignment operator sign-off — **pending** в BLOCK-REGISTRY-GAPS.
- Будет ли Triumph workspace эталоном PROMO — **UNKNOWN** (BLUEPRINT-GAPS).
- Machine registry service (Tool/Memory layer) — **unknown** (registries.md SAFE UNKNOWN).

---

## Recommended Next Registry Work

### Priority A

1. **v0 → v1 operational binding charter** — один канонический `block_id` / `site_type_code` для новых задач; обновление operational docs **только по explicit charter** (этот аудит документы не меняет).
2. **Registry v1.1 — structural blocks:** charter для `HEADER_NAV`, `FILTERS`, `SEARCH` (+ breadcrumbs/pagination policy).
3. **Reference implementation expansion** — минимум PROMO money-page subset (SERVICES, PROCESS, TEAM) или explicit «LANDING-only Template-Art» policy в passport.
4. **Commercial Pattern Library v0 catalog** — pattern_id registry file: минимум lead-form-v1, rfq-v1, scroll_process_timeline (reuse existing doc).

### Priority B

5. **SEO content pattern slice** — title/description formula templates per page_type (documentation), без generation engine.
6. **BLOCK-REGISTRY hygiene** — full BLOCK-CONTRACT fields на всех 29 entries; resolve TRUST/TESTIMONIALS in reference code or documented variant map.
7. **ECOMMERCE Legal Extension charter** — когда ecommerce project enters production intent.
8. **Blueprint machine schema** — `project.blueprint.yaml` format (documentation only).

### Priority C

9. **Extended Type blueprints** — per-type architecture charter (SAAS, MARKETPLACE).
10. **v0 geo_landing / seo_landing mapping** — explicit v1 composition rules or new Extended types (requires registry charter).
11. **Registry JSON Schema export** — tooling readiness.
12. **WF-A03 Pixel Factory** — после Research Pass; parallel to Priority A only if `PIXEL_PERFECT` portfolio dominates.

---

**STOP — NO IMPLEMENTATION — NO DOCUMENT CHANGES (кроме создания этого отчёта)**

---

*Audit artifact: `reports/foundry-registry-layer-audit-v1.md` · Evidence base: OPERATIONAL-INDEX, roadmap.md, website-factory-reference-v1 foundation stack, mars-website-factory registries.md and v0 registries.*
