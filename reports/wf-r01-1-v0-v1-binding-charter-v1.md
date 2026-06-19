# WF-R01.1 — v0 → v1 Operational Binding Charter v1

**Subprogram ID:** WF-R01.1  
**Program parent:** WF-R01 — FOUNDRY Registry Expansion Program (**CHARTERED**)  
**Version:** v1  
**Date:** 2026-06-19  
**Implementation pass:** [wf-r01-1-accepted-charter-implementation-v1.md](wf-r01-1-accepted-charter-implementation-v1.md)

**Honesty boundary:** WF-R01.1 — **documentation and operator-discipline charter** (human-operated). **Не** runtime, **не** machine-enforced ID linter, **не** automated migration engine, **не** mass retrofit live workspaces.

**Терминология:** **FOUNDRY** = **Website Factory** ecosystem (строка FOUNDRY как отдельный продукт/путь в repo **не найдена**).

**Design basis:** [wf-r01-1-v0-v1-binding-charter-design-v1.md](wf-r01-1-v0-v1-binding-charter-design-v1.md) · **Acceptance pass:** [wf-r01-1-acceptance-pass-v1.md](wf-r01-1-acceptance-pass-v1.md) — **ACCEPT WITH MINOR CHANGES**

---

## Charter sign-off

| Field | Value |
|-------|-------|
| **Status** | **ACCEPTED** |
| **Acceptance state** | Binding charter **content accepted**; cutover **implementation** (phases P2–P5) **not complete** |
| **Authority state** | WF-R01.1 = **ACCEPTED** (subprogram binding authority) · WF-R01 program = **CHARTERED** (program **not ACTIVE** until R01.1 execution P2+ per program charter) |
| **T0** | **2026-06-19** — date of ACCEPTED publication (binding authority effective for new-work namespace policy) |
| **Owner** | Website Factory operator governance (human-operated sign-off via accepted charter implementation pass; **named steward SAFE UNKNOWN** — not fixed in repo) |
| **Prior state** | PROPOSAL — design artifact [wf-r01-1-v0-v1-binding-charter-design-v1.md](wf-r01-1-v0-v1-binding-charter-design-v1.md) |
| **B1 (binding charter ACCEPTED)** | **Satisfied** by this artifact |
| **B2 (mapping table published)** | **Satisfied** — § Mapping Matrix below |
| **B3–B8** | **Not satisfied** — implementation phase; see § ACCEPTED ≠ implementation complete |

**ACCEPTED means:** v1 = SSOT for **new** Factory registry IDs; v0 = read-only legacy archive; mapping, STOP, and cutover **policy** are binding. **Does not** mean banners applied (B5), STOP live in OPERATIONAL-INDEX (B3), onboarding updated (B4), T_cutover recorded (B6), curated-library v2 (B7), or agent card path (B8).

---

## ACCEPTED ≠ implementation complete (B3–B8)

Publication of this ACCEPTED charter **does not** complete subprogram exit criteria B3–B8. Those criteria belong to the **implementation phase** (charter pass P2–P5), separate tasks:

| ID | Criterion | Phase | Status at ACCEPT |
|----|-----------|-------|------------------|
| **B1** | Binding charter **ACCEPTED** | P1 | ✅ **Complete** |
| **B2** | v0→v1 mapping table published | P1 | ✅ **Complete** (this charter) |
| **B3** | STOP rule in OPERATIONAL-INDEX Core Run | P3 (R01.1-STOP) | ⏳ **Pending** |
| **B4** | Onboarding / passport template cites v1 only | Charter pass | ⏳ **Pending** |
| **B5** | Legacy banner on v0 registries | P2 (R01.1-BANNER) | ⏳ **Pending** |
| **B6** | Zero new v0 IDs post-T_cutover on pilots | P5 (R01.1-AUDIT) | ⏳ **Pending** (T_cutover unset) |
| **B7** | Curated library v2 plan or dual-column index | P2 | ⏳ **Pending** |
| **B8** | Agent card authority path documented | Charter pass | ⏳ **Pending** |

**WF-R01.1 subprogram exit** requires B1–B8. **WF-R01.2** remains **forbidden** until authorization gates per program charter (minimum B1 + B3).

---

## Upstream authority — WF-A01 terminology harmonization

**Authority reference only** — this charter **does not amend** [website-factory-production-modes-charter-v1.md](../projects/mars-website-factory/website-factory-production-modes-charter-v1.md) (WF-A01).

| Context | Term | Binding rule for **new work** |
|---------|------|-------------------------------|
| WF-A01 TEMPLATE_ART §4.2 (rank 3 SSOT) | `site_type_id` | **Historical field name** in Production Modes charter — refers to Site Type Registry vocabulary |
| v1 canon (SITE-TYPE-REGISTRY-v1, passports) | `site_type_code` | **Canonical token** for new artifacts — `UPPER_SNAKE_CASE` (`LANDING`, `CATALOG`, …) |
| WF-A01 STOP S6 (via binding) | `TEMPLATE_ART` without v1 `site_type_code` | **STOP** — new LOC-ZONE passports and blueprints must use `site_type_code`, not v0 `site_type_id` |

**Harmonization rule:** When reading WF-A01 Production Modes for **new** Factory intake, interpret registry site-type references as **`site_type_code`** per v1 canon. v0 `site_type_id` (`landing`, `service_landing`, …) is **legacy archive only** — map via § Site type mapping.

**Related upstream (unchanged scope):**

- [website-factory-validation-architecture-charter-v1.md](../projects/mars-website-factory/website-factory-validation-architecture-charter-v1.md) (WF-A02) — VL1 consumes v1 registries; binding feeds honest vocabulary
- [website-factory-vl3-domains-charter-v1.md](../projects/mars-website-factory/website-factory-vl3-domains-charter-v1.md) — orthogonal to registry namespace
- [wf-r01-registry-expansion-program-charter-v1.md](wf-r01-registry-expansion-program-charter-v1.md) — parent program CHARTERED

---

## Role map boundary — sample (R01.1) vs full (R01.6)

WF-R01.1 defines **binding-level** role mapping only — enough to resolve namespace drift and STOP mixed IDs. It **does not** claim completeness for all v0 conceptual roles (~35+ across site type rows).

| Artifact | Scope | Owner subprogram | Completeness target |
|----------|-------|------------------|---------------------|
| **Sample role → `block_id` map** (§ Role mapping sample) | Representative rows for operator STOP/remap | **WF-R01.1** (this charter) | Binding minimum — **not** ≥90% |
| **Full operator role → `block_id` map** | All v0 role names in site type rows + disposition for entity/AI/geo roles | **WF-R01.6** — Registry Hygiene | Quality gate **Q1** — ≥90% of v0 roles mapped |

**Operator rule:** If a v0 role is **not** in the R01.1 sample table, **do not invent** a snake_case `block_id`. Escalate to WF-R01.6 hygiene pass or apply HITL composition notes with existing v1 `block_id` tokens only.

---

## Executive Summary

Аудиты Registry Layer и Capability Gap фиксируют **dual canon** (XD-01, Critical): параллельное существование legacy v0 (`snake_case`, 10 site types, 16 blocks) и канона v1 (`UPPER_SNAKE_CASE`, 8 site types, 29 blocks) при том, что операционные артефакты Wave 4–6 и agent cards **всё ещё цитируют v0**.

WF-R01.1 устанавливает **Operational Binding Charter** — единый namespace для **новой** работы:

| Решение | Содержание |
|---------|------------|
| **Канон для новых задач** | v1 = SSOT для `site_type_code`, `block_id`, Blueprint v1, passport LOC-ZONE |
| **v0 статус** | **Legacy archive** — read-only reference; **не** источник новых ID |
| **Mapping** | 10 v0 site types + 16 v0 blocks → v1 codes / composition rules |
| **Cutover** | Human sign-off gate + phased operator policy (banner → STOP rule → zero new v0 IDs) |
| **Non-goals** | Удаление v0 файлов; автоматический retrofit Triumph v6; OCPilot/OpenCart migration без enrollment |

WF-R01.1 — **program entry gate** для WF-R01.2–R01.8. Без binding любое расширение registry **умножает** drift.

---

## v0 Inventory (summary)

### Site Type Registry v0

**Путь:** `projects/mars-website-factory/site-type-registry-v0.md`  
**Итого:** **10** `site_type_id` · **snake_case**

`landing` · `service_landing` · `promo_site` · `corporate_site` · `catalog_site` · `ecommerce` · `geo_landing` · `seo_landing` · `ai_visibility_page` · `hybrid_commercial`

### Block Registry v0

**Путь:** `projects/mars-website-factory/block-registry-v0.md`  
**Итого:** **16** `block_id` · **snake_case**

`hero` · `trust_block` · `services_grid` · `faq` · `cases` · `reviews` · `pricing` · `process_steps` · `contact_cta` · `calculator` · `comparison` · `geo_trust` · `catalog_grid` · `sticky_cta` · `lead_form` · `final_cta`

### v0 role vocabulary (drift risk — not block_id)

Site Type Registry v0 `required_blocks` / `optional_blocks` use **conceptual roles** (~35+ unique names). See § Role map boundary — sample in this charter; full map in **WF-R01.6**.

---

## v1 Inventory (summary)

**Корень канона:** `workspaces/website-factory-reference-v1/`

| Layer | Path | Count / status |
|-------|------|----------------|
| Site types | `registry/SITE-TYPE-REGISTRY-v1.md` | **8** codes (Core 5 + Extended 3) — **ACCEPTED** |
| Blocks | `block-registry/BLOCK-REGISTRY-v1.md` | **29** `block_id` — **ACCEPTED** |
| Core blueprints | `page-blueprints/*-BLUEPRINT-v1` | **5** — Core site types |
| Reference partials | `src/partials/blocks/` | **9/29** (~31%) — implementation cliff, **не** ослабляет v1 as planning canon |
| OPEN gaps | HEADER_NAV, FILTERS, SEARCH | **WF-R01.2** — not in v1.0 registry |

---

## Mapping Matrix

### Site type mapping: v0 `site_type_id` → v1 `site_type_code`

| v0 `site_type_id` | v1 primary `site_type_code` | Mapping class | Composition / HITL notes |
|-------------------|----------------------------|---------------|--------------------------|
| `landing` | `LANDING` | **DIRECT** | 1:1 |
| `service_landing` | `LANDING` **or** `PROMO` | **COMPOSITION** | Single URL + process → `LANDING`; multi-page service hub → `PROMO`. **HITL** per project. |
| `promo_site` | `PROMO` | **DIRECT** | Campaign vs brand promo — still `PROMO` |
| `corporate_site` | `CORPORATE` | **DIRECT** | Hybrid subtrees → per-route `site_type_code` in passport |
| `catalog_site` | `CATALOG` | **DIRECT** | RFQ/dealer flows — `LEAD_FORM` + patterns, not new site type |
| `ecommerce` | `ECOMMERCE` | **DIRECT** | Reclassify from `catalog_site` when cart/checkout on-domain |
| `geo_landing` | `LANDING` | **EXTENDED COMPOSITION** | `site_type_code=LANDING` + passport geo program notes. **Не** новый v1 code. |
| `seo_landing` | `LANDING` **or** `PROMO` | **EXTENDED COMPOSITION** | Editorial long-form on promo hub → `PROMO`; single intent URL → `LANDING` |
| `ai_visibility_page` | `LANDING` **or** `CORPORATE` | **EXTENDED COMPOSITION** | Entity sheet — content program notes; **нет** dedicated v1 type |
| `hybrid_commercial` | **Multi** per route group | **MULTI-CODE** | Declare **primary** `site_type_code` per route group. **Не** использовать `hybrid_commercial` as v1 code. |

**Explicit rule:** v0-only types **не** получают новые v1 `site_type_code` в рамках WF-R01.1.

### Block mapping: v0 `block_id` → v1 `block_id`

| v0 `block_id` | v1 `block_id` | Mapping class | Notes |
|---------------|---------------|---------------|-------|
| `hero` | `HERO` | **DIRECT** | Partial `hero.html` |
| `trust_block` | `TRUST` | **DIRECT** | Partial `social_proof.html` |
| `services_grid` | `SERVICES` | **DIRECT** | |
| `faq` | `FAQ` | **DIRECT** | Partial `faq.html` |
| `cases` | `CASES` | **DIRECT** | Partial `cases.html` |
| `reviews` | `REVIEWS` **or** `TESTIMONIALS` | **SPLIT (HITL)** | UGC/ratings → `REVIEWS`; curated quotes → `TESTIMONIALS` |
| `pricing` | `PRICING` | **DIRECT** | Partial `pricing.html` |
| `process_steps` | `PROCESS` | **DIRECT** | Pattern `scroll_process_timeline` = **pattern_id**, not block split |
| `contact_cta` | `CTA` **and/or** `CONTACTS` | **COMPOSITION** | Band CTA → `CTA`; contact hub → `CONTACTS` |
| `calculator` | — | **NO V1 EQUIVALENT** | Archive v0 row; **не** new id without charter |
| `comparison` | `FEATURES` **or** `PRODUCT_CARD` | **PARTIAL** | Page-context HITL |
| `geo_trust` | `TRUST` + `MAP` + notes | **COMPOSITION** | |
| `catalog_grid` | `PRODUCT_GRID` **or** `CATEGORY_GRID` | **CONTEXT** | Category tiles → `CATEGORY_GRID`; SKU grid → `PRODUCT_GRID` |
| `sticky_cta` | `CTA` | **SUB-VARIANT** | Partial `sticky_cta.html` |
| `lead_form` | `LEAD_FORM` | **DIRECT** | Partial `lead_form.html` |
| `final_cta` | `CTA` | **SUB-VARIANT** | Bottom band → `cta_band.html` under `CTA` |

### Role mapping sample (binding-level only — full map: WF-R01.6)

| v0 role (site type row) | v1 `block_id` | Class |
|-------------------------|---------------|-------|
| `hero_primary`, `hero_service`, `local_hero` | `HERO` | DIRECT |
| `value_props` | `BENEFITS` | DIRECT |
| `social_proof`, `proof_logos` | `TRUST` | DIRECT |
| `proof_cases` | `CASES` | DIRECT |
| `primary_cta`, `cta_booking_or_form` | `CTA` + `LEAD_FORM` | COMPOSITION |
| `process_steps` (role) | `PROCESS` | DIRECT |
| `nav_mega_or_primary` | `HEADER_NAV` (**v1.1**) | **PENDING** — WF-R01.2 |
| `footer_minimal`, `footer_corporate` | `FOOTER` + `LEGAL_LINKS` | COMPOSITION |
| `category_plp` | `PRODUCT_GRID` + `CATEGORIES` | COMPOSITION |
| `product_detail_template` | `PRODUCT_CARD` | DIRECT |
| `comparison_table` | `FEATURES` or PDP section | PARTIAL |
| `spec_accordion` | `FEATURES` or `PRODUCT_CARD` | PARTIAL |
| `dealer_locator` | `MAP` + pattern notes | COMPOSITION |
| `entity_definition`, `fact_table` | — | **PROJECT NOTES** — **FORBIDDEN** as new snake_case block_id |
| `plp`, `pdp`, `cart`, `checkout_progress` | `PRODUCT_GRID`, `PRODUCT_CARD`, `CART`, `CHECKOUT` | DIRECT |

### Curated library mapping (v0 name → v1 canonical)

| Curated library `block_id` (v0) | v1 `block_id` | Partial |
|----------------------------------|---------------|---------|
| `hero` | `HERO` | `hero.html` |
| `lead_form` | `LEAD_FORM` | `lead_form.html` |
| `cta_band` | `CTA` | `cta_band.html` |
| `pricing` | `PRICING` | `pricing.html` |
| `social_proof` | `TRUST` | `social_proof.html` |
| `sticky_cta` | `CTA` | `sticky_cta.html` |
| `contact_block` | `CONTACTS` | `contact_block.html` |
| `faq` | `FAQ` | `faq.html` |
| `cases` | `CASES` | `cases.html` |

---

## Cutover Policy

### Principles

1. **v1 canon forward** — все **новые** Factory artifacts используют v1 IDs.
2. **v0 read-only legacy** — v0 файлы **сохраняются**; не удаляются в R01.1.
3. **No automatic retrofit** — live workspaces **не** мигрируют автоматически.
4. **Human-operated gates** — cutover = operator sign-off + REPORT evidence, **не** CI.

### Phased cutover

| Phase | ID | Trigger | Status at T0 |
|-------|-----|---------|--------------|
| **P0 — Charter design** | R01.1-DESIGN | WF-R01 approved | ✅ Done |
| **P1 — Charter ACCEPTED** | R01.1-ACCEPT | Human sign-off | ✅ **Done** (T0 = 2026-06-19) |
| **P2 — Banner pass** | R01.1-BANNER | P1 complete | ⏳ Pending (B5) |
| **P3 — STOP rule live** | R01.1-STOP | P2 complete | ⏳ Pending (B3) |
| **P4 — New-work cutover** | R01.1-CUTOVER | P3 complete | ⏳ Pending — **T_cutover** unset |
| **P5 — Pilot audit** | R01.1-AUDIT | 30 days post T_cutover | ⏳ Pending (B6) |

### T_cutover rules (effective at P4 — not yet active)

| Work class | Rule at T_cutover |
|------------|-------------------|
| **New greenfield** (LOC-ZONE, new passport) | **v1 only** |
| **New blueprint instances** | v1 Blueprint + v1 `block_id` |
| **New curated library rows** | v1 `block_id` |
| **Agent card updates** | New versions cite v1; v0 cards archived |
| **Existing frozen workspaces** | **Grandfathered** |
| **OCPilot / OpenCart delivery** | **Out of cutover** unless Factory enrollment charter |

---

## No-New-v0 Rule

**После T_cutover** операторы и Cursor tasks **ЗАПРЕЩЕНО** создавать **новые** артефакты с v0 `site_type_id`, v0 `block_id`, или новыми snake_case pseudo-IDs.

### STOP conditions (blocking)

| # | Condition | Action |
|---|-----------|--------|
| S1 | v0 `block_id` in **new** page blueprint targeting v1 Core Blueprint | **STOP** |
| S2 | Mixed `hero` + `HERO` in same blueprint `section_order` | **STOP** |
| S3 | v0 `site_type_id` in new LOC-ZONE passport `site_type_code` field | **STOP** |
| S4 | New curated library row with snake_case `block_id` | **STOP** |
| S5 | Agent output proposes new v0 registry row | **STOP** |
| S6 | `TEMPLATE_ART` passport without v1 `site_type_code` | **STOP** — WF-A01 gate |

**Enforcement:** documentation + operator discipline only — **not** CI/runtime (post-R01 Priority C for machine linter).

---

## Drift Detection (summary)

| Class | Name | Severity |
|-------|------|----------|
| **XD-01** | Dual namespace mix | **Critical** |
| **XD-02** | Ops doc stale authority (v0 as authority for new work) | **Critical** |
| **XD-03** | False compatibility | **High** |
| **XD-04** | Curated library drift | **High** |
| **XD-05** | Agent card drift | **High** |
| **XD-10** | Implementation false-green | **Critical** |

Full taxonomy (XD-01–XD-10), procedures D1–D6, and response matrix: [wf-r01-1-v0-v1-binding-charter-design-v1.md](wf-r01-1-v0-v1-binding-charter-design-v1.md) § Drift Detection Rules.

---

## Execution Case Impact (summary)

| Case | R01.1 impact | Retrofit? |
|------|--------------|-----------|
| **Triumph** | New extractions v1; v6 HTML grandfathered | **No** auto |
| **ISBD** | New artifacts v1 | **No** until adoption charter |
| **BZPM** | Factory canon refs v1; OpenCart **out of scope** | **No** |
| **OCPilot** | Parallel track until enrollment | **No** without enrollment charter |

Full matrix: design artifact § Execution Case Impact.

---

## Explicit non-goals (WF-R01.1 ACCEPTED)

- WF-R01.2 structural blocks (HEADER_NAV, FILTERS, SEARCH)
- New `block_id` / new site types
- Registry expansion / reference partial waves
- Pixel Factory (WF-A03)
- Runtime / automation / machine ID linter
- Triumph v6 full ID retrofit
- OCPilot auto-enrollment

---

## SAFE UNKNOWN

| Item | Status |
|------|--------|
| **Named owner** (steward identity) | **Not fixed** in repo |
| **T_cutover** calendar date | **Pending** P4 implementation |
| **Rollback owner** | **Not fixed** |
| **curated-library v2** exact path | **To be fixed** in P2 (B7) |
| **RV-01 / RV-02 / RV-03** research artifacts | **Not found** in repo — proxy audits only |
| **OCPilot SITE-001** v1 binding | **Not verified** |
| **BZPM W3** blueprint delivery | **UNKNOWN** |
| **FOUNDRY** as named product/path | **Not found** — Website Factory scope |

---

*Accepted charter artifact: `reports/wf-r01-1-v0-v1-binding-charter-v1.md`*  
*Design source: `reports/wf-r01-1-v0-v1-binding-charter-design-v1.md`*  
*Parent program: `reports/wf-r01-registry-expansion-program-charter-v1.md` (CHARTERED)*
