# Website Factory — SEO Architecture System v2

**Версия:** v2  
**Дата:** 2026-06-01  
**Operator:** APPROVED BY OPERATOR  
**Область:** `workspaces/website-factory-reference-v1/seo-architecture/`  
**Статус:** канонический SEO Architecture Layer — **documentation only**

**Не является:** SEO content generation, keyword generation, meta generation, article generation, technical SEO audit, runtime, automation, AI generation, prompts, keyword databases, SERP scraping, MIG integration, ORCA integration, website generation.

**Предшественник:** [registry/SITE-TYPE-SEO-MAPPING-v1.md](../registry/SITE-TYPE-SEO-MAPPING-v1.md) — shallow hints; v2 — полноценный архитектурный слой.

**Foundation:** [ARCHITECTURE-FOUNDATION-v1.md](../ARCHITECTURE-FOUNDATION-v1.md)

---

## 1. Role of the SEO layer

SEO Architecture Layer v2 задаёт **архитектурные решения до контента**:

- какой **Search Intent Model** применим к сайту и страницам;
- какая **SEO Strategy** следует из `site_type_code` и Blueprint;
- какая **Page Strategy** (indexation, depth, signals) для каждого `page_type`;
- какие **Content Requirements** (сигналы, не тексты) должны быть удовлетворены до Design / Frontend.

Слой **не** производит copy, keywords, title/description, schema markup text или audit-отчёты.

---

## 2. Position in architecture

```text
Site Type Registry          ← registry/SITE-TYPE-REGISTRY-v1.md
        ↓
   Blueprints               ← blueprints/{TYPE}-BLUEPRINT-v1.md
        ↓
Page Architecture           ← page-architecture/ (page_type, blocks)
        ↓
Page Block Validation       ← page-block-validation/ (PASS/FAIL blocks)
        ↓
SEO Architecture Layer      ← seo-architecture/ (этот слой) — v2
        ↓
   Design Layer             ← FUTURE — Design System Mapping
        ↓
 Frontend Layer             ← project implementation / reference partials
```

**Правило v2:** SEO Architecture **потребляет** Site Type, Blueprint, Page Architecture и Validation semantics; **не** мутирует Registry, Blueprints, Block Registry или frozen Legal Pack.

**Parallel concern (не слой SEO):** Legal Pack v1 **FROZEN** — trust/compliance signals на страницах согласуются с SEO trust signals, но Legal Pack **не** подменяет SEO Architecture.

---

## 3. Lifecycle

| Phase | Action | Gate / artefact |
|-------|--------|-----------------|
| **1. Classify** | `site_type_code` из Registry | Core 5 для default production mapping |
| **2. Blueprint** | Load canonical Blueprint | `business_goal`, `typical_traffic_sources`, `seo_requirements` scope |
| **3. Site SEO mapping** | [SITE-TYPE-SEO-MAPPING-v2.md](SITE-TYPE-SEO-MAPPING-v2.md) | Primary/secondary SEO goals, intent mix, exclusions |
| **4. Intent model** | [SEARCH-INTENT-MODEL-v1.md](SEARCH-INTENT-MODEL-v1.md) | Assign intent types per money/hub routes |
| **5. SEO strategy contract** | [SEO-STRATEGY-CONTRACT-v1.md](SEO-STRATEGY-CONTRACT-v1.md) | Site-level strategy freeze (documentation) |
| **6. Page matrix check** | [SITE-TYPE-PAGE-MATRIX-v1.md](../page-architecture/SITE-TYPE-PAGE-MATRIX-v1.md) | Only allowed `page_type` receive SEO contracts |
| **7. Page SEO contracts** | [PAGE-SEO-CONTRACT-v1.md](PAGE-SEO-CONTRACT-v1.md) per production route | All contract fields filled |
| **8. Architecture matrix** | [SEO-ARCHITECTURE-MATRIX-v1.md](SEO-ARCHITECTURE-MATRIX-v1.md) | Site Type × Intent × Page Type — no FORBIDDEN cells violated |
| **9. Implementation rules** | [SEO-IMPLEMENTATION-RULES-v1.md](SEO-IMPLEMENTATION-RULES-v1.md) | Operator checklist |
| **10. Block validation** | Page Block Validation v1 (upstream) | PASS before Design |
| **11. Design** | Design System Mapping — **FUTURE** | Visual + component binding |
| **12. Frontend** | Implementation | After SEO + block gates frozen |

**Halt:** Design / Frontend **без** frozen SEO architecture для money/catalog routes = architecture drift risk.

---

## 4. Required inputs

| Input | Source | Used for |
|-------|--------|----------|
| `site_type_code` | [SITE-TYPE-REGISTRY-v1.md](../registry/SITE-TYPE-REGISTRY-v1.md) | Site-level SEO goals, depth, exclusions |
| Blueprint | [BLUEPRINT-SYSTEM-v1.md](../blueprints/BLUEPRINT-SYSTEM-v1.md), Core 5 blueprints | Traffic alignment, `required_pages`, site-level SEO scope |
| `page_type` + Page Contract | [PAGE-TYPE-REGISTRY-v1.md](../page-architecture/PAGE-TYPE-REGISTRY-v1.md), [PAGE-CONTRACT-v1.md](../page-architecture/PAGE-CONTRACT-v1.md) | Per-route SEO contract instantiation |
| Site Type × Page matrix | [SITE-TYPE-PAGE-MATRIX-v1.md](../page-architecture/SITE-TYPE-PAGE-MATRIX-v1.md) | Forbidden page types |
| Block context (awareness) | [BLOCK-REGISTRY-v1.md](../block-registry/BLOCK-REGISTRY-v1.md) | Content/trust **signals** via blocks — not block authoring |
| Validation status | [PAGE-BLOCK-VALIDATION-SYSTEM-v1.md](../page-block-validation/PAGE-BLOCK-VALIDATION-SYSTEM-v1.md) | Gate before Design |
| Legal mapping (read-only) | [SITE-TYPE-LEGAL-MAPPING-v2.md](../legal/SITE-TYPE-LEGAL-MAPPING-v2.md) | Trust signals alignment — **no** Legal Pack changes |

**Explicit non-inputs:** keywords, SERP data, generated meta, MIG, ORCA, AI prompts.

---

## 5. Produced outputs

| Output | Document | Consumer (future / current) |
|--------|----------|----------------------------|
| Site-level SEO strategy | [SEO-STRATEGY-CONTRACT-v1.md](SEO-STRATEGY-CONTRACT-v1.md) | Project IA, operator gate |
| Site type SEO profile | [SITE-TYPE-SEO-MAPPING-v2.md](SITE-TYPE-SEO-MAPPING-v2.md) | Page SEO contracts |
| Intent classification | [SEARCH-INTENT-MODEL-v1.md](SEARCH-INTENT-MODEL-v1.md) | Page SEO contracts, matrix |
| Per-page SEO contract | [PAGE-SEO-CONTRACT-v1.md](PAGE-SEO-CONTRACT-v1.md) | Fills `seo_requirements` in Page Contract |
| Compatibility matrix | [SEO-ARCHITECTURE-MATRIX-v1.md](SEO-ARCHITECTURE-MATRIX-v1.md) | Validation / operator review |
| Implementation discipline | [SEO-IMPLEMENTATION-RULES-v1.md](SEO-IMPLEMENTATION-RULES-v1.md) | Human-operated production |
| Known gaps register | [SEO-ARCHITECTURE-GAPS-v1.md](SEO-ARCHITECTURE-GAPS-v1.md) | Roadmap — no solutions in v2 |

---

## 6. Canonical chain (detailed)

```text
Site Type
  → defines SEO priority band, typical intent mix, global exclusions
Blueprint
  → defines traffic sources (PPC vs organic), required_pages, site-level seo_requirements scope
Page Architecture
  → defines page_type per route, page_goal, block stacks
SEO Architecture (v2)
  → Search Intent Model + SEO Strategy + Page SEO Contract + Content Requirements (signals)
Design (FUTURE)
  → tokens/components; must not contradict frozen SEO page strategy
Frontend
  → HTML/partials; meta/schema implementation — FUTURE contracts, not v2
```

### Mapping: Page Contract ↔ SEO

Поле `seo_requirements` в [PAGE-CONTRACT-v1.md](../page-architecture/PAGE-CONTRACT-v1.md) **детализируется** через [PAGE-SEO-CONTRACT-v1.md](PAGE-SEO-CONTRACT-v1.md). v2 **не** заменяет Page Contract; расширяет семантику SEO-поля.

---

## 7. Artefact index (seo-architecture/)

| File | Role |
|------|------|
| SEO-ARCHITECTURE-SYSTEM-v2.md | Этот документ — system entry |
| SEO-STRATEGY-CONTRACT-v1.md | Site-level strategy fields |
| SITE-TYPE-SEO-MAPPING-v2.md | Core 5 site type SEO profiles |
| SEARCH-INTENT-MODEL-v1.md | Canonical intent types |
| PAGE-SEO-CONTRACT-v1.md | Page-level SEO contract fields |
| SEO-ARCHITECTURE-MATRIX-v1.md | Site Type × Intent × Page Type |
| SEO-IMPLEMENTATION-RULES-v1.md | Per-type production rules |
| SEO-ARCHITECTURE-GAPS-v1.md | Documented future gaps only |

---

## 8. Boundaries (hard)

| Forbidden in v2 | Reason |
|-----------------|--------|
| New `site_type_code` | Registry charter only |
| New Blueprints | Blueprint charter only |
| Runtime / CLI / CI SEO validator | Not implemented |
| Content / keyword / meta generation | Downstream charters |
| Prompts, automation, AI | Out of architecture scope |
| MIG / ORCA coupling | Explicit exclusion |
| Legal Pack structural change | FROZEN |

---

## SAFE UNKNOWN

- `registry/SITE-TYPE-SEO-MAPPING-v1.md` supersession banner — **CLOSED** (acceptance 2026-06-01).
- Automated cross-check SEO matrix vs PAGE-BLOCK-VALIDATION — **FUTURE**.
- Extended types (SAAS, WEB_APPLICATION, MARKETPLACE) SEO rows — **not in Core v2 scope**; see gaps.

---

*SEO Architecture System v2 — documentation only. Canonical folder: `workspaces/website-factory-reference-v1/seo-architecture/`.*
