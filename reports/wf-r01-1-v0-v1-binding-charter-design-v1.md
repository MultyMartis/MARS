# REPORT — WF-R01.1 V0 → V1 BINDING CHARTER

**Subprogram ID:** WF-R01.1  
**Program parent:** WF-R01 — FOUNDRY Registry Expansion Program  
**Дата:** 2026-06-19  
**Режим:** проектирование charter — **без implementation**  
**База:** [foundry-registry-expansion-program-design-v1.md](foundry-registry-expansion-program-design-v1.md) · [foundry-registry-layer-audit-v1.md](foundry-registry-layer-audit-v1.md) · [foundry-capability-gap-audit-v1.md](foundry-capability-gap-audit-v1.md) · [SITE-TYPE-REGISTRY-v1.md](../workspaces/website-factory-reference-v1/registry/SITE-TYPE-REGISTRY-v1.md) · [site-type-registry-v0.md](../projects/mars-website-factory/site-type-registry-v0.md) · [BLOCK-REGISTRY-v1.md](../workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md) · [block-registry-v0.md](../projects/mars-website-factory/block-registry-v0.md) · [registries.md](../projects/mars-website-factory/registries.md) · [OPERATIONAL-INDEX.md](../projects/mars-website-factory/OPERATIONAL-INDEX.md) · [roadmap.md](../projects/mars-website-factory/roadmap.md)

**Honesty boundary:** WF-R01.1 — **documentation and operator-discipline charter** (human-operated). **Не** runtime, **не** machine-enforced ID linter, **не** automated migration engine, **не** mass retrofit live workspaces.

**Терминология:** **FOUNDRY** = **Website Factory** ecosystem (см. SAFE UNKNOWN в родительских аудитах).

---

## Executive Summary

Аудиты Registry Layer и Capability Gap **единогласно** фиксируют **dual canon** (XD-01, Critical): параллельное существование legacy v0 (`snake_case`, 10 site types, 16 blocks) и канона v1 (`UPPER_SNAKE_CASE`, 8 site types, 29 blocks) при том, что операционные артефакты Wave 4–6 и agent cards **всё ещё цитируют v0**.

WF-R01.1 проектирует **Operational Binding Charter** — единый namespace для **новой** работы:

| Решение | Содержание |
|---------|------------|
| **Канон для новых задач** | v1 = SSOT для `site_type_code`, `block_id`, Blueprint v1, passport LOC-ZONE |
| **v0 статус** | **Legacy archive** — read-only reference; **не** источник новых ID |
| **Mapping** | 10 v0 site types + 16 v0 blocks → v1 codes / composition rules (не claim 1:1 для всех строк) |
| **Cutover** | Human sign-off gate + phased operator policy (banner → STOP rule → zero new v0 IDs) |
| **Non-goals** | Удаление v0 файлов; автоматический retrofit Triumph v6; OCPilot/OpenCart migration без enrollment |

WF-R01.1 — **program entry gate** для WF-R01.2–R01.8. Без binding любое расширение registry **умножает** drift.

---

## v0 Inventory

### Точный объём v0 (канонические реестры)

#### Site Type Registry v0

**Путь:** `projects/mars-website-factory/site-type-registry-v0.md`  
**Статус:** documented — **не канон v1**  
**Версия:** v0 (2026-05-11)

| # | `site_type_id` | category | Ключевые operational fields |
|---|----------------|----------|-------------------------------|
| 1 | `landing` | conversion | SEO_model, CTA_model, trust_model, required_blocks (roles) |
| 2 | `service_landing` | conversion | process_steps, coverage_map, local_pack alignment |
| 3 | `promo_site` | campaign | narrative_sections, countdown optional |
| 4 | `corporate_site` | brand | nav_mega_or_primary, multi-audience CTAs |
| 5 | `catalog_site` | commerce | category_plp, spec_accordion, dealer_locator |
| 6 | `ecommerce` | commerce | plp, pdp, cart, checkout_progress |
| 7 | `geo_landing` | programmatic_seo | local_hero, service_area, doorway risk controls |
| 8 | `seo_landing` | programmatic_seo | article_header, toc, E-E-A-T emphasis |
| 9 | `ai_visibility_page` | brand | entity_definition, fact_table (role names, не block_id) |
| 10 | `hybrid_commercial` | hybrid | subtree inheritance, cannibalization risk |

**Итого:** **10** `site_type_id` · **snake_case** · field glossary **глубже** по operational полям, чем v1 Core rows.

#### Block Registry v0

**Путь:** `projects/mars-website-factory/block-registry-v0.md`  
**Статус:** documented — **не канон v1**  
**Версия:** v0

| # | `block_id` | category | compatible_site_types (v0) |
|---|------------|----------|------------------------------|
| 1 | `hero` | hero | 8+ types |
| 2 | `trust_block` | trust | landing, service_landing, corporate, catalog, ecommerce, geo, hybrid |
| 3 | `services_grid` | services | service_landing, corporate, geo, hybrid |
| 4 | `faq` | content | most types |
| 5 | `cases` | social_proof | service_landing, corporate, catalog, geo, hybrid |
| 6 | `reviews` | social_proof | catalog, ecommerce, corporate, … |
| 7 | `pricing` | commercial | landing, service_landing, promo, corporate, hybrid |
| 8 | `process_steps` | content | landing, service_landing, promo, corporate, geo |
| 9 | `contact_cta` | conversion | most types |
| 10 | `calculator` | interaction | service_landing, corporate, catalog (limited) |
| 11 | `comparison` | content | catalog, ecommerce, seo_landing |
| 12 | `geo_trust` | geo | geo_landing |
| 13 | `catalog_grid` | navigation | catalog_site, ecommerce, hybrid |
| 14 | `sticky_cta` | conversion | landing, service_landing, promo, geo |
| 15 | `lead_form` | conversion | landing, service_landing, promo, corporate, catalog, geo |
| 16 | `final_cta` | conversion | landing, service_landing, promo, geo |

**Итого:** **16** `block_id` · **snake_case**.

### v0 role vocabulary (не block_id, но drift-риск)

В Site Type Registry v0 поля `required_blocks` / `optional_blocks` используют **conceptual roles**, не всегда совпадающие с v0 `block_id`:

| Role family | Примеры | Риск |
|-------------|---------|------|
| Hero variants | `hero_primary`, `hero_service`, `hero_campaign`, `hero_brand`, `local_hero` | Оператор может изобрести ID |
| Trust / proof | `social_proof`, `proof_cases`, `proof_logos`, `value_props` | Путаница с `trust_block` / `TRUST` |
| Navigation | `nav_mega_or_primary`, `footer_minimal`, `footer_corporate` | Нет v1 `HEADER_NAV` / `FOOTER` в v0 |
| Catalog | `category_plp`, `product_detail_template`, `comparison_table` | Нет 1:1 с v1 CATALOG blocks |
| Entity / AI | `entity_definition`, `fact_table`, `scope_and_limits` | **Нет** v1 block_id |
| Geo | `service_area`, `map_optional`, `coverage_map` | Composition-only в v1 |

**Итого role names (уникальные, не block_id):** **~35+** across 10 site type rows — требуют **operator label → block_id** map (WF-R01.6), не новые v0 IDs.

### v0 operational surfaces (цитируют v0 namespace)

| Surface | Путь | v0 coupling |
|---------|------|-------------|
| **registries.md §1–2** | `projects/mars-website-factory/registries.md` | Declares v0 as "Delivered"; agents consume `site_type_id` |
| **Page Blueprint Contract v0** | `page-blueprint-contract-v0.md` | `site_type_id` + Block Registry v0 `block_id` |
| **Workflow v0** | `website-factory-workflow-v0.md` | Stages 2–5 cite v0 registries |
| **Curated library index** | `curated-library-index-v1.md` | **9 rows** — v0 `block_id` (`hero`, `lead_form`, …) |
| **Block quality tiers** | `block-quality-tiers-v1.md` | Links to `block-registry-v0.md`; tier checks `data-block-id` |
| **Legacy migration path** | `legacy-migration-path-v1.md` | Migration order uses v0 names (`hero`, `social_proof`, …) |
| **Agent cards (8+)** | `agents/cards/*-v0.md` | Site Type / Block Registry v0 as authority |
| **design-governance-agent** | `agents/design-governance-agent.md` | Block Registry v0 alignment |
| **Case artifact** | `reference-cases/triumph-manipulator-landing/page-blueprint-v0.md` | v0 blueprint instance |
| **QA checklist v0** | `page-blueprint-qa-checklist-v0.md` | v0 compatibility checks |

### v0 summary counts

| Dimension | Count | ID format |
|-----------|-------|-----------|
| Site types | **10** | `snake_case` `site_type_id` |
| Canonical blocks | **16** | `snake_case` `block_id` |
| Conceptual block roles | **~35+** | free-text roles in site type rows |
| Curated library (ops) | **9** | v0 `block_id` |
| Reference partials (filename) | **9** | snake_case filenames; **semantic** overlap with v1 |

---

## v1 Inventory

### Точный объём v1 (канон Foundation stack)

**Корень канона:** `workspaces/website-factory-reference-v1/`  
**Foundation freeze:** 2026-06-01+ (ACCEPTED layers per Registry Layer Audit)

#### Site Type Registry v1

**Путь:** `workspaces/website-factory-reference-v1/registry/SITE-TYPE-REGISTRY-v1.md`  
**Статус:** **ACCEPTED** — canonical classification

| Group | `site_type_code` | Readiness (audit) |
|-------|------------------|-------------------|
| **Core 5** | `LANDING` | Production Ready (doc + reference pilot) |
| | `PROMO` | Partial |
| | `CATALOG` | Partial |
| | `ECOMMERCE` | Partial |
| | `CORPORATE` | Partial |
| **Extended 3** | `SAAS` | Concept Only |
| | `WEB_APPLICATION` | Concept Only |
| | `MARKETPLACE` | Concept Only |

**Итого:** **8** types · **UPPER_SNAKE_CASE** `site_type_code` · Extended explicitly **out of Core Factory defaults**.

**Сопутствующие v1 (site type layer):**

- `SITE-TYPE-MATRIX-v1.md`
- `SITE-TYPE-BLOCK-MATRIX-v2.md` (block-registry/)
- `SITE-TYPE-LEGAL-MAPPING-v2.md` (legal/)
- `SITE-TYPE-SEO-MAPPING-v2.md` (seo-architecture/)

#### Block Registry v1

**Путь:** `workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md`  
**Статус:** **ACCEPTED** — **29** `block_id`

| # | `block_id` | primary_category | Reference partial |
|---|------------|------------------|-------------------|
| 1 | `HERO` | CONTENT | `hero.html` ✓ |
| 2 | `BENEFITS` | CONTENT | — |
| 3 | `FEATURES` | CONTENT | — |
| 4 | `SERVICES` | COMPANY | — |
| 5 | `CATEGORIES` | CATALOG | — |
| 6 | `CATEGORY_GRID` | CATALOG | — |
| 7 | `PRODUCT_GRID` | CATALOG | — |
| 8 | `PRODUCT_CARD` | CATALOG | — |
| 9 | `PRICING` | CONTENT | `pricing.html` ✓ |
| 10 | `PROCESS` | CONTENT | — |
| 11 | `CASES` | COMPANY | `cases.html` ✓ |
| 12 | `TESTIMONIALS` | TRUST | overlaps `social_proof.html` |
| 13 | `REVIEWS` | TRUST | — |
| 14 | `TRUST` | TRUST | `social_proof.html` ✓ |
| 15 | `CERTIFICATES` | TRUST | — |
| 16 | `TEAM` | COMPANY | — |
| 17 | `ABOUT` | COMPANY | — |
| 18 | `FAQ` | CONTENT | `faq.html` ✓ |
| 19 | `CTA` | CONVERSION | `cta_band.html`, `sticky_cta.html` ✓ |
| 20 | `LEAD_FORM` | CONVERSION | `lead_form.html` ✓ |
| 21 | `CONTACTS` | CONTACT | `contact_block.html` ✓ |
| 22 | `MAP` | CONTACT | — |
| 23 | `PARTNERS` | COMPANY | — |
| 24 | `DELIVERY` | COMMERCE | — |
| 25 | `PAYMENT` | COMMERCE | — |
| 26 | `CHECKOUT` | CONVERSION | — |
| 27 | `CART` | CONVERSION | — |
| 28 | `LEGAL_LINKS` | LEGAL | — |
| 29 | `FOOTER` | SYSTEM | — |

**Reference implementation:** **9/29** partials (~**31%**) — implementation cliff, **не** ослабляет v1 как planning canon.

**OPEN gaps (documented, post-R01.1):** `HEADER_NAV`, `FILTERS`, `SEARCH` — WF-R01.2; не часть v1 Core 29, но **требуются** Blueprints.

#### Page Blueprint Layer v1

| Blueprint | `site_type_code` | Status |
|-----------|------------------|--------|
| LANDING-BLUEPRINT-v1 | `LANDING` | ACCEPTED |
| PROMO-BLUEPRINT-v1 | `PROMO` | ACCEPTED |
| CATALOG-BLUEPRINT-v1 | `CATALOG` | ACCEPTED |
| ECOMMERCE-BLUEPRINT-v1 | `ECOMMERCE` | ACCEPTED |
| CORPORATE-BLUEPRINT-v1 | `CORPORATE` | ACCEPTED |

**Page types:** `PAGE-TYPE-REGISTRY-v1` — 10 minimal + ECOMMERCE utility pages.

#### Adjacent v1 layers (binding scope — cite rules)

| Layer | Path / artifact | Binding role |
|-------|-----------------|--------------|
| SEO Architecture v2 | `seo-architecture/` | **Replaces** planned "SEO Pattern Library" for planning SSOT |
| Production Modes | `website-factory-production-modes-charter-v1.md` | `TEMPLATE_ART` → Block Registry v1 = SSOT |
| Validation Architecture | `website-factory-validation-architecture-charter-v1.md` | VL chain; blueprint validation uses v1 matrices |
| Passport fields | `FP-XXXX-PROJECT-PASSPORT-FIELDS-v1.md` | `production_mode`, `site_type_code` (v1) |
| Commercial pattern (partial) | `scroll-process-timeline-pattern-v1.md` | `pattern_id` separate from `block_id` |

### v1 summary counts

| Dimension | Count | ID format |
|-----------|-------|-----------|
| Site types (total) | **8** | `UPPER_SNAKE_CASE` |
| Site types (Core production) | **5** | Core only for default Factory pipeline |
| Block ids (Core registry) | **29** | `UPPER_SNAKE_CASE` |
| Core blueprints | **5** | Per Core `site_type_code` |
| Reference partials | **9** | snake_case **filenames**; v1 `block_id` in registry rows |
| Structural blocks (v1.1 planned) | **3+** | Not in v1.0 — WF-R01.2 |

---

## Mapping Matrix

### Site type mapping: v0 `site_type_id` → v1 `site_type_code`

| v0 `site_type_id` | v1 primary `site_type_code` | Mapping class | Composition / HITL notes |
|-------------------|----------------------------|---------------|--------------------------|
| `landing` | `LANDING` | **DIRECT** | 1:1 |
| `service_landing` | `LANDING` **or** `PROMO` | **COMPOSITION** | Single URL + process → `LANDING`; multi-page service hub → `PROMO`. **HITL** per project. |
| `promo_site` | `PROMO` | **DIRECT** | Campaign vs brand promo — still `PROMO`; time-bound notes in passport |
| `corporate_site` | `CORPORATE` | **DIRECT** | Hybrid subtrees → per-route `site_type_code` in passport |
| `catalog_site` | `CATALOG` | **DIRECT** | RFQ/dealer flows — `LEAD_FORM` + patterns, not new site type |
| `ecommerce` | `ECOMMERCE` | **DIRECT** | Reclassify from `catalog_site` when cart/checkout on-domain |
| `geo_landing` | `LANDING` | **EXTENDED COMPOSITION** | `site_type_code=LANDING` + passport **geo program** notes (SEO_model local_pack, uniqueness rules). **Не** новый v1 code. |
| `seo_landing` | `LANDING` **or** `PROMO` | **EXTENDED COMPOSITION** | Editorial long-form on promo hub → `PROMO`; single intent URL → `LANDING`. SEO program notes required. |
| `ai_visibility_page` | `LANDING` **or** `CORPORATE` | **EXTENDED COMPOSITION** | Entity sheet on corp/docs → `CORPORATE` subtree or `LANDING` campaign. Content program notes; **нет** dedicated v1 type. |
| `hybrid_commercial` | **Multi** per route group | **MULTI-CODE** | Pattern from `CORPORATE` hybrid-by-design: declare **primary** `site_type_code` per route group in passport/blueprint. **Не** использовать `hybrid_commercial` as v1 code. |

**Explicit rule:** v0-only types **не** получают новые v1 `site_type_code` в рамках WF-R01.1. Расширение таксономии (9-й Core type, Manufacturer, Auto) — **отдельный registry charter** (post-R01).

### Block mapping: v0 `block_id` → v1 `block_id`

| v0 `block_id` | v1 `block_id` | Mapping class | Notes |
|---------------|---------------|---------------|-------|
| `hero` | `HERO` | **DIRECT** | Partial `hero.html` |
| `trust_block` | `TRUST` | **DIRECT** | Partial `social_proof.html` (logos/metrics) |
| `services_grid` | `SERVICES` | **DIRECT** | Grid → SERVICES block |
| `faq` | `FAQ` | **DIRECT** | Partial `faq.html` |
| `cases` | `CASES` | **DIRECT** | Partial `cases.html` |
| `reviews` | `REVIEWS` **or** `TESTIMONIALS` | **SPLIT (HITL)** | UGC/ratings → `REVIEWS`; curated quotes → `TESTIMONIALS` |
| `pricing` | `PRICING` | **DIRECT** | Partial `pricing.html` |
| `process_steps` | `PROCESS` | **DIRECT** | Pattern `scroll_process_timeline` = **pattern_id**, not block split |
| `contact_cta` | `CTA` **and/or** `CONTACTS` | **COMPOSITION** | Band CTA → `CTA`; contact hub → `CONTACTS` |
| `calculator` | — | **NO V1 EQUIVALENT** | Archive v0 row; new work: `FEATURES` variant **or** project-local with HITL — **не** new v0/v1 id without charter |
| `comparison` | `FEATURES` **or** `PRODUCT_CARD` | **PARTIAL** | Comparison table on PLP/PDP — page-context HITL |
| `geo_trust` | `TRUST` + `MAP` + notes | **COMPOSITION** | Local proof decomposed to v1 blocks + geo passport notes |
| `catalog_grid` | `PRODUCT_GRID` **or** `CATEGORY_GRID` | **CONTEXT** | Category tiles → `CATEGORY_GRID`; SKU grid → `PRODUCT_GRID` |
| `sticky_cta` | `CTA` | **SUB-VARIANT** | Registry id `CTA`; partial `sticky_cta.html` |
| `lead_form` | `LEAD_FORM` | **DIRECT** | Partial `lead_form.html` |
| `final_cta` | `CTA` | **SUB-VARIANT** | Bottom band → `cta_band.html` under `CTA` |

### v0 role → v1 `block_id` (operator label map — sample)

| v0 role (site type row) | v1 `block_id` | Class |
|-------------------------|---------------|-------|
| `hero_primary`, `hero_service`, `local_hero` | `HERO` | DIRECT |
| `value_props` | `BENEFITS` | DIRECT |
| `social_proof`, `proof_logos` | `TRUST` | DIRECT |
| `proof_cases` | `CASES` | DIRECT |
| `primary_cta`, `cta_booking_or_form` | `CTA` + `LEAD_FORM` | COMPOSITION |
| `process_steps` (role) | `PROCESS` | DIRECT |
| `nav_mega_or_primary` | `HEADER_NAV` (**v1.1**) | **PENDING** — OPEN gap; interim: layout policy + HITL |
| `footer_minimal`, `footer_corporate` | `FOOTER` + `LEGAL_LINKS` | COMPOSITION |
| `category_plp` | `PRODUCT_GRID` + `CATEGORIES` | COMPOSITION |
| `product_detail_template` | `PRODUCT_CARD` | DIRECT |
| `comparison_table` | `FEATURES` or PDP section | PARTIAL |
| `spec_accordion` | `FEATURES` or `PRODUCT_CARD` | PARTIAL |
| `dealer_locator` | `MAP` + pattern notes | COMPOSITION — vertical profile post-R01 |
| `entity_definition`, `fact_table` | — | **PROJECT NOTES** — no v1 block; **FORBIDDEN** as new snake_case block_id |
| `plp`, `pdp`, `cart`, `checkout_progress` | `PRODUCT_GRID`, `PRODUCT_CARD`, `CART`, `CHECKOUT` | DIRECT (ecommerce path) |

### Filename / ops index mapping (curated library)

| Curated library `block_id` (v0 name) | Canonical v1 `block_id` | Partial file |
|--------------------------------------|-------------------------|--------------|
| `hero` | `HERO` | `hero.html` |
| `lead_form` | `LEAD_FORM` | `lead_form.html` |
| `cta_band` | `CTA` | `cta_band.html` |
| `pricing` | `PRICING` | `pricing.html` |
| `social_proof` | `TRUST` (variant; split `TESTIMONIALS` per R01.6) | `social_proof.html` |
| `sticky_cta` | `CTA` | `sticky_cta.html` |
| `contact_block` | `CONTACTS` | `contact_block.html` |
| `faq` | `FAQ` | `faq.html` |
| `cases` | `CASES` | `cases.html` |

### Coverage gap matrix (v1 blocks without v0 ancestor)

| v1 `block_id` | v0 ancestor | WF-R01.1 disposition |
|---------------|-------------|----------------------|
| `BENEFITS` | role `value_props` only | **v1-native** — use directly |
| `FEATURES` | partial `comparison` | **v1-native** |
| `CATEGORIES`, `CATEGORY_GRID`, `PRODUCT_GRID`, `PRODUCT_CARD` | `catalog_grid` (partial) | **v1-native** decomposition |
| `SERVICES` | `services_grid` | mapped |
| `TESTIMONIALS` | `reviews` / `trust_block` | split policy |
| `REVIEWS` | `reviews` | mapped |
| `CERTIFICATES`, `TEAM`, `ABOUT`, `PARTNERS` | corporate roles | **v1-native** |
| `MAP` | `geo_trust` / roles | composition |
| `CART`, `CHECKOUT`, `PAYMENT`, `DELIVERY` | ecommerce roles | **v1-native** |
| `LEGAL_LINKS`, `FOOTER` | footer roles | **v1-native** |
| `HEADER_NAV`, `FILTERS`, `SEARCH` | nav/filter roles | **WF-R01.2** — not in v1.0 registry |

---

## Cutover Policy

### Principles

1. **v1 canon forward** — все **новые** Factory artifacts используют v1 IDs.
2. **v0 read-only legacy** — v0 файлы **сохраняются**; не удаляются в R01.1.
3. **No automatic retrofit** — live workspaces (Triumph v6, ISBD, OCPilot) **не** мигрируют автоматически.
4. **Human-operated gates** — cutover = operator sign-off + REPORT evidence, **не** CI.

### Phased cutover

| Phase | ID | Trigger | Operator actions | Artifact outputs |
|-------|-----|---------|------------------|------------------|
| **P0 — Charter design** | R01.1-DESIGN | WF-R01 approved | This document | Design v1 (this file) |
| **P1 — Charter ACCEPTED** | R01.1-ACCEPT | Human sign-off on binding charter | Publish binding charter; record ACCEPTED date = **T0** | `wf-r01-1-v0-v1-binding-charter-v1.md` (future accepted artifact) |
| **P2 — Banner pass** | R01.1-BANNER | P1 complete | Add legacy banners to v0 registries + high-traffic ops docs **via explicit charter pass** (not silent edit) | Banner on v0 files; curated-library **v2** index plan |
| **P3 — STOP rule live** | R01.1-STOP | P2 complete | OPERATIONAL-INDEX Core Run row: mixed v0/v1 on v1 Blueprint = **blocking defect** | STOP rule visible to operators |
| **P4 — New-work cutover** | R01.1-CUTOVER | P3 complete | **T_cutover** = date; zero **new** artifacts with v0 IDs | Passport / onboarding cite v1 only |
| **P5 — Pilot audit** | R01.1-AUDIT | 30 days post T_cutover | REPORT audit on pilot intake (FP new rows, greenfield) | B6 evidence |

### T_cutover rules

| Work class | Rule at T_cutover |
|------------|-------------------|
| **New greenfield** (LOC-ZONE, new passport) | **v1 only** — `site_type_code`, `block_id`, Blueprint v1 |
| **New blueprint instances** | Must reference v1 Blueprint + v1 `block_id` |
| **New curated library rows** | **v1 `block_id`** in index (curated-library v2) |
| **Agent card updates** | New versions cite v1; v0 cards **archived** (read-only) |
| **Existing frozen workspaces** | **Grandfathered** — v0 IDs in legacy HTML `data-block-id` tolerated until explicit extraction/enrollment |
| **OCPilot / OpenCart delivery** | **Out of cutover** unless Factory enrollment charter |
| **Case artifacts (doc simulation)** | Remain v0-labeled as **historical**; new case docs use v1 |

### Grandfathering boundary

| Asset | Grandfathered? | Condition |
|-------|----------------|-----------|
| Triumph v6 built HTML | **Yes** | Until section replacement per legacy-migration-path |
| `page-blueprint-v0.md` (Triumph case) | **Yes** | Historical reference case |
| Curated library v1 index | **Yes** until v2 | Transitional dual-label table allowed in charter pass |
| New REPORT rows / passports | **No** | v1 required post T_cutover |

### Rollback

Binding charter rollback requires **explicit operator charter** — revert to dual canon **documented** as incident, not silent. **SAFE UNKNOWN:** rollback owner — not fixed in repo.

---

## No-New-v0 Rule

### Statement

**После T_cutover** операторы, агенты (human-executed) и Cursor tasks **ЗАПРЕЩЕНО** создавать **новые** артефакты, использующие:

- v0 `site_type_id` (`landing`, `service_landing`, …) в **новых** blueprints, passports, REPORT tables
- v0 `block_id` (`hero`, `lead_form`, …) в **новых** blueprint stacks, curated library rows, extraction REPORTs targeting Factory canon
- **Новые** snake_case pseudo-IDs для blocks or site types

### Allowed exceptions (HITL-documented)

| Exception | Condition | Documentation |
|-----------|-----------|---------------|
| **Historical citation** | Quoting legacy workspace in forensic/audit REPORT | Label `legacy-v0` in REPORT section |
| **Grandfathered workspace edit** | Touching existing Triumph/ISBD section without replacement | No **new** block_id rows in registry artifacts |
| **Explicit waiver charter** | Operator-signed waiver for named project + timebox | Waiver doc in `reports/` |
| **v0 file maintenance** | Typo fix in v0 registry with **no new IDs** | Changelog note; banner preserved |

### STOP conditions (blocking)

| # | Condition | Operator action |
|---|-----------|-----------------|
| S1 | v0 `block_id` in **new** page blueprint targeting v1 Core Blueprint | **STOP** — remap via matrix |
| S2 | Mixed `hero` + `HERO` in same blueprint `section_order` | **STOP** — blocking defect |
| S3 | v0 `site_type_id` in new LOC-ZONE passport `site_type_code` field | **STOP** — use v1 code + composition notes |
| S4 | New curated library row with snake_case `block_id` | **STOP** — use v1 |
| S5 | Agent output proposes new v0 registry row | **STOP** — escalate registry charter |
| S6 | `TEMPLATE_ART` passport without v1 `site_type_code` | **STOP** — WF-A01 gate |

### Enforcement model

| Layer | R01.1 enforcement |
|-------|-------------------|
| Runtime / CI | **NOT IMPLEMENTED** — documentation-only |
| Operator discipline | STOP rules + REPORT audit |
| Agent cards | Updated to cite v1 (post charter pass) |
| Future | Machine linter — **post-WF-R01** (Priority C) |

---

## Drift Detection Rules

### Drift classes

| Class ID | Name | Detection signal | Severity |
|----------|------|------------------|----------|
| **XD-01** | Dual namespace mix | Same artifact contains v0 + v1 IDs | **Critical** |
| **XD-02** | Ops doc stale authority | Wave 4–6 doc cites v0 registry as **authority** for new work | **Critical** |
| **XD-03** | False compatibility | v0 block on v1 Blueprint without mapping notes | **High** |
| **XD-04** | Curated library drift | Library index v0 names without v1 canonical column | **High** |
| **XD-05** | Agent card drift | `*-agent-v0.md` used for **new** intake without v1 override | **High** |
| **XD-06** | Filename vs registry drift | Partial filename snake_case but `data-block-id` wrong vs v1 | **Medium** |
| **XD-07** | Role invention | New conceptual role in blueprint without v1 `block_id` map | **Medium** |
| **XD-08** | Extended type false Core | `SAAS`/`MARKETPLACE` treated as Core production default | **Medium** |
| **XD-09** | SEO library phantom | New doc claims "SEO Pattern Library" as delivered module | **Medium** |
| **XD-10** | Implementation false-green | REPORT claims registry complete while reference < 31% | **Critical** (capability) |

### Detection procedures (human-operated)

| Procedure | Frequency | Scope | Output |
|-----------|-----------|-------|--------|
| **D1 — Intake passport review** | Per new LOC-ZONE row | `site_type_code`, `production_mode`, blueprint refs | PASS / XD-03 / XD-06 |
| **D2 — Blueprint stack audit** | Per new blueprint artifact | All `block_id` tokens vs BLOCK-REGISTRY-v1 | PASS / XD-01 |
| **D3 — REPORT grep sweep** | Monthly post T_cutover | `reports/` for new `site_type_id` snake_case | PASS / XD-01 |
| **D4 — Ops doc spot check** | Per WF-R01 phase gate | OPERATIONAL-INDEX, curated-library, agent cards | PASS / XD-02 |
| **D5 — Curated library sync** | Per new library row | registry-sync-discipline + v1 column | PASS / XD-04 |
| **D6 — Execution case enrollment** | Per R01.8 row | Case lesson tables use v1 vocabulary | PASS / XD-07 |

### Drift response matrix

| Class | First response | Escalation |
|-------|----------------|------------|
| XD-01 | STOP task; remap via matrix | Registry hygiene REPORT |
| XD-02 | Charter pass to update authority links | WF-R01.6 |
| XD-03 | HITL remap or waiver | Blueprint amendment |
| XD-04 | Publish curated-library v2 row | R01.3 reference wave |
| XD-05 | Route agents to v1 docs in prompt | Agent card revision charter |
| XD-10 | Correct REPORT wording; cite M2 metric | Capability audit refresh |

### Positive signals (non-drift)

- snake_case **partial filenames** (`hero.html`) with v1 `block_id` in registry row — **allowed**
- Historical v0 case artifacts unchanged — **allowed**
- `pattern_id` (`scroll_process_timeline`) alongside v1 `block_id` — **allowed** (separate namespace)

---

## Acceptance Criteria

### Binding charter completion (WF-R01.1 exit)

| ID | Criterion | Verification method | Owner |
|----|-----------|---------------------|-------|
| **B1** | Binding charter document **ACCEPTED** (human sign-off) | Accepted artifact in `reports/` or `projects/mars-website-factory/` | Operator |
| **B2** | v0→v1 mapping table **published** covering **10** site types + **16** blocks + role map sample | This design → accepted charter | Documentation |
| **B3** | STOP rule in **OPERATIONAL-INDEX** Core Run row | Visible STOP on mixed IDs | Charter pass |
| **B4** | New task / onboarding template cites **v1 only** for registry IDs | onboarding-flow / passport guidance updated | Charter pass |
| **B5** | Legacy banner on v0 registries: «legacy — do not use for new work» | Banner present on v0 files | Charter pass (explicit) |
| **B6** | Zero **new** artifacts using v0 IDs **post-T_cutover** on pilot projects | D3 REPORT grep + passport review | REPORT audit |
| **B7** | Curated library **v2 plan** or dual-column index published | v1 `block_id` canonical column | R01.1 banner pass |
| **B8** | Agent card authority path documented (v0 archived / v1 primary) | agents/registry or card revision note | Charter pass |

### Quality gates (non-blocking but tracked)

| ID | Gate | Target |
|----|------|--------|
| **Q1** | Role → `block_id` operator map completeness | ≥ 90% of v0 roles in site type rows |
| **Q2** | Execution cases have v1 vocabulary row in lesson index | ≥ 4 cases (R01.8 kickoff) |
| **Q3** | XD-01 incidents post-T_cutover | **0** on greenfield intake |

### Explicit non-acceptance (out of scope)

- 100% reference partial coverage
- HEADER_NAV / FILTERS / SEARCH in registry (WF-R01.2)
- Triumph v6 full ID retrofit
- Machine JSON Schema export
- OCPilot auto-enrollment

---

## Execution Case Impact

### Summary matrix

| Case | Current v0/v1 state | R01.1 impact | Binding action | Retrofit? |
|------|---------------------|--------------|----------------|-----------|
| **Triumph** | v6 workspace: legacy selectors + partial v0 `data-block-id`; case doc `page-blueprint-v0.md` | **High** — reference extractions feed curated library with v0 names | New extractions use v1 IDs; passport new rows v1; case artifact **grandfathered** | **No** auto; per-section on replacement |
| **ISBD** | Client #2; lighter Factory binding; care vertical `LANDING` | **Medium** | New artifacts v1; freeze records may note legacy IDs | **No** until adoption charter |
| **BZPM** | No Factory workspace; OCPilot SITE-002; live catalog OpenCart | **High** vocabulary; **Low** workspace | Lesson index uses v1 (`CATALOG`); delivery path **not** Factory canon | **No** — OCPilot boundary |
| **OCPilot** | SITE-001 Sibcar (auto); SITE-002 BZPM; WF CSS direction | **Medium** — enrollment **SAFE UNKNOWN** | Factory binding only on explicit enrollment; `site_type_code` unverified today | **No** without enrollment charter |

### Triumph (`triumph-manipulator-landing`)

| Dimension | Detail |
|-----------|--------|
| Workspace | `workspaces/triumph-manipulator-landing-v6/` — highest live evidence |
| Registry coupling | Curated library extractions (`faq`, `pricing`, `cases`) indexed as v0 `block_id` |
| Blueprint | `page-blueprint-v0.md` — historical; uses `service_landing`-class semantics |
| v1 mapping | Primary production class → `LANDING` / `PROMO` (multi-page); blocks → matrix § Block mapping |
| R01.1 rules | **S1–S6 apply** to **new** Triumph-track REPORTs and extractions; v6 HTML grandfathered |
| Feeds | R01.3 W1/W3 reference waves; R01.4 `scroll_process_timeline` pattern |
| Risk | Triumph mistaken as full **PROMO** reference without v1 binding — mitigated by enrollment scope |

### ISBD (`isbd-care-landing`)

| Dimension | Detail |
|-----------|--------|
| Workspace | `workspaces/isbd-care-landing/` — client delivery #2 |
| Registry coupling | Care vertical landing; adoption/freeze pattern |
| v1 mapping | `LANDING` + vertical notes in passport |
| R01.1 rules | New LOC-ZONE amendments → v1 `site_type_code`; WPilot follow-on docs cite v1 |
| Feeds | R01.3 W7 (FEATURES/REVIEWS); adoption validation template |
| Risk | Low ID drift today; **medium** if new blocks added with v0 names |

### BZPM (`bzpm-catalog-redesign` / OCPilot SITE-002)

| Dimension | Detail |
|-----------|--------|
| Delivery | Live TEST `zpm.new-site.space`; OpenCart stack — **not** Factory workspace |
| Registry coupling | Audit vocabulary: filters, megamenu, PLP/PDP — **no** v1 structural blocks yet |
| v1 mapping | Operational class → `CATALOG` (+ manufacturer **composition**: CATALOG + CORPORATE notes) |
| R01.1 rules | Factory canon references in **new** docs → v1 only; live OpenCart HTML **out of scope** |
| Feeds | R01.2 structural blocks; R01.3 W4–W5; R01.8 lesson index |
| Risk | BZPM delivery **misread** as Factory catalog readiness — separate delivery vs canon pipeline |
| **SAFE UNKNOWN** | W3 blueprint delivery date |

### OCPilot (SITE-001 Sibcar + program)

| Dimension | Detail |
|-----------|--------|
| SITE-001 | Автосалон СИБКАР — auto dealer TEST; WF visual direction CSS-only |
| Registry coupling | **Не verified** — `production_mode` and v1 `site_type_code` binding |
| v1 mapping | Auto vertical → `CATALOG` composition + vertical profile doc (not new site type) |
| R01.1 rules | Enrollment decision **post-R01.2**; until enrolled, OCPilot reports **parallel track** |
| Feeds | R01.7 Template-Art trajectory; R01.8 auto vertical profile |
| Risk | SITE-001 Template-Art claim before structural blocks — **blocked** by R01.7 interim LANDING-only policy for Factory passport |
| Boundary | OCPilot/OpenCart **не мигрируют** в Factory canon без enrollment decision (WF-R01 program scope) |

### Cross-case operator rules (post-binding)

1. **Execution case registry** rows may keep case `id` snake_case — **не** путать с `site_type_code`.
2. **Lesson index** (R01.8) normalizes to v1 `block_id` / `site_type_code` — HITL per row.
3. **No case auto-canonicalizes** v6 or live OpenCart into reference-v1 without extraction/enrollment charter.
4. **FP-0002** (PIXEL_PERFECT) — documents **v0 artifact risk** in binding; **not** primary block source for R01.1.

---

## Risks

| Risk | Severity | Mitigation in R01.1 design |
|------|----------|---------------------------|
| v0 ID creep during R01 waves | **Critical** | No-New-v0 Rule + T_cutover + B6 audit |
| False «registry complete» after ACCEPTED v1 labels | **Critical** | XD-10; separate implementation metrics (M2) |
| Operator ignores STOP without enforcement | **High** | REPORT audit; onboarding explicit; future linter deferred |
| Curated library v0 names confuse agents | **High** | Dual-column v2 + B7 |
| Triumph v6 retrofit scope creep | **High** | Grandfathering + per-section migration only |
| BZPM/Sibcar lessons never enter v1 vocabulary | **High** | R01.8 lesson index + enrollment charters |
| Premature Template-Art on CATALOG | **Critical** | R01.7 interim policy; structural blocks R01.2 |
| Banner pass without charter discipline | **Medium** | Explicit charter pass — no silent edits |
| Extended types used as Core defaults | **Medium** | XD-08; SITE-TYPE-REGISTRY v1 Extended section |
| Governance bloat from binding prose | **Low** | Single OPERATIONAL-INDEX Core Run row (B3) |

---

## SAFE UNKNOWN

| Item | Status |
|------|--------|
| **FOUNDRY** as named product/path in repo | **Not found** — Website Factory scope |
| **Human owner** WF-R01.1 sign-off | **Not fixed** in repo |
| **T_cutover** calendar date | **Pending** P1 ACCEPTED |
| **OCPilot SITE-001** `production_mode` + v1 binding | **Not verified** in audits |
| **BZPM W3** blueprint delivery | **UNKNOWN** |
| **VL3 adoption** on Triumph v6 / ISBD | **Not audited** |
| **HEADER_NAV / FILTERS / SEARCH** as block_id | **WF-R01.2** — operator decision pending for breadcrumbs/pagination |
| **MEGA_MENU** — variant vs separate id | **Operator decision pending** |
| **Manufacturer / Auto** as future Extended `site_type_code` | **Undecided** — composition rules only in R01.1 |
| **Registry JSON Schema** export timeline | **Not defined** |
| **Machine ID linter** automation | **Post-R01** Priority C |
| **Rollback owner** for binding charter | **Not fixed** |
| **Knowledge Center** mirror freshness | **UNKNOWN** (out-of-git) |
| **curated-library v2** exact filename/path | **To be fixed** in charter pass |

---

## Appendix — Document disposition summary

| v0 entity class | Disposition | Rationale |
|-----------------|-------------|-----------|
| v0 registry files (site + block) | **PRESERVE + ARCHIVE** | Historical + field glossary value; banner «legacy» |
| v0 `site_type_id` rows | **LINK → v1** via composition | No new v1 codes in R01.1 |
| v0 `block_id` rows | **LINK → v1** or **ARCHIVE** (`calculator`) | Matrix § Block mapping |
| v0 role names | **LINK → v1** via operator map | WF-R01.6 hygiene |
| v0 workflow / blueprint contract | **PRESERVE + ARCHIVE** | Historical pipeline; new work uses v1 blueprints |
| v0 agent cards | **ARCHIVE** (read-only) | New agent guidance cites v1 |
| Ops docs with v0 authority | **LINK + UPDATE** (charter pass) | curated-library v2, block-quality-tiers link target |
| New v0 IDs | **FORBIDDEN** post-T_cutover | No-New-v0 Rule |
| Mixed IDs on v1 Blueprint | **FORBIDDEN** | STOP S2 |
| Live workspace legacy HTML | **PRESERVE** (grandfather) | Until explicit replacement |

---

**STOP AFTER REPORT — NO IMPLEMENTATION — NO DOCUMENT CHANGES (кроме этого артефакта)**

---

*Design artifact: `reports/wf-r01-1-v0-v1-binding-charter-design-v1.md`*  
*Parent program: `reports/foundry-registry-expansion-program-design-v1.md` (WF-R01.1)*  
*Next step (out of scope): human ACCEPTED → publish `wf-r01-1-v0-v1-binding-charter-v1.md` + charter pass P2–P5*
