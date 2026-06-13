# Website Factory — Production QA Matrix v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/production-qa/`  
**Статус:** architectural QA coverage matrix — **documentation only**  
**Связь:** [PRODUCTION-QA-CHECKLIST-v1.md](PRODUCTION-QA-CHECKLIST-v1.md), [PRODUCTION-QA-GATES-v1.md](PRODUCTION-QA-GATES-v1.md)

**Не является:** automated test matrix, Playwright project matrix, visual diff grid.

---

## 1. Назначение

Production QA Matrix v1 определяет **какие architecture layers** требуют QA coverage для **Core 5 site types**, **10 page types**, и какие **pass requirements** применяются на уровне проекта.

Матрица отвечает: *«Что должно быть проверено для данного `site_type_code` + `page_type` перед Frontend Handoff?»* — не *«Как страница рендерится в браузере?»*

---

## 2. Dimensions

| Dimension | v1 scope |
|-----------|----------|
| **Site types** | Core 5: `LANDING`, `PROMO`, `CATALOG`, `ECOMMERCE`, `CORPORATE` |
| **Page types** | 10 from [PAGE-TYPE-REGISTRY-v1.md](../page-architecture/PAGE-TYPE-REGISTRY-v1.md) |
| **Architecture layers** | 12 accepted layers (see §3) |
| **QA categories** | 10 from Production QA Contract |
| **Pass unit** | Per `project_scope` + per in-scope `page_type` where applicable |

**Extended Types** (`SAAS`, `WEB_APPLICATION`, `MARKETPLACE`): **NOT IN v1 matrix** — SAFE UNKNOWN until Extended charter.

---

## 3. Accepted architecture layers (columns)

| Layer ID | Source | QA category |
|----------|--------|-------------|
| L1 | Site Type Registry | ARCHITECTURE |
| L2 | Blueprints | ARCHITECTURE |
| L3 | Page Architecture | ARCHITECTURE |
| L4 | Block Registry | ARCHITECTURE |
| L5 | Page Block Validation | ARCHITECTURE / VALIDATION |
| L6 | SEO Architecture v2 | SEO |
| L7 | Design System Mapping | DESIGN |
| L8 | Content Contracts | CONTENT |
| L9 | Content Validation | CONTENT_VALIDATION |
| L10 | Legal Pack (FROZEN) | LEGAL |
| L11 | Legal Entity Discovery | ENTITY |
| L12 | Generation Contracts | GENERATION_READINESS |

**Production QA (L13):** meta-layer — evaluates L1–L12 aggregate, not a duplicate implementation.

---

## 4. Site-type layer requirements (project level)

Legend: **R** = required for FULL_SITE pass | **C** = conditional | **—** = not applicable by default

| Layer | LANDING | PROMO | CATALOG | ECOMMERCE | CORPORATE |
|-------|---------|-------|---------|-----------|-----------|
| L1 Site Type | R | R | R | R | R |
| L2 Blueprint | R | R | R | R | R |
| L3 Page Architecture | R | R | R | R | R |
| L4 Block Registry | R | R | R | R | R |
| L5 Page Block Validation | R | R | R | R | R |
| L6 SEO | R | R | R | R | R |
| L7 Design | R | R | R | R | R |
| L8 Content Contracts | R | R | R | R | R |
| L9 Content Validation | R | R | R | R | R |
| L10 Legal Pack | R | R | R | R | R |
| L11 Entity | C | C | C | C | C |
| L12 Generation | R | R | R | R | R |

**Pass requirement (project):** all **R** layers evidenced; all **C** resolved or `NOT_APPLICABLE` signed; Production QA contract `PASS` or `PASS_WITH_WARNINGS`.

---

## 5. Page-type applicability (Core 5)

| `page_type` | LANDING | PROMO | CATALOG | ECOMMERCE | CORPORATE | Per-page QA depth |
|-------------|---------|-------|---------|-----------|-----------|-------------------|
| `HOME_PAGE` | — | R | R | R | R | Full L3–L9 when in scope |
| `LANDING_PAGE` | R | C | — | — | C | Full L3–L9 |
| `SERVICE_PAGE` | — | R | — | — | R | Full L3–L9 |
| `CATEGORY_PAGE` | — | — | R | R | C | Full L3–L9 |
| `PRODUCT_PAGE` | — | — | C | R | — | Full L3–L9 |
| `ABOUT_PAGE` | — | R | C | C | R | Full L3–L9 |
| `CONTACT_PAGE` | — | R | R | R | R | Full L3–L9 |
| `FAQ_PAGE` | C | C | C | C | C | L3–L9 when in blueprint |
| `REVIEWS_PAGE` | C | C | C | C | C | L3–L9 when in blueprint |
| `LEGAL_PAGE` | R | R | R | R | R | L3–L10 mandatory |

**Rule:** `C` page types require QA only if listed in blueprint `required_pages` or project `included_page_types`.

---

## 6. QA category coverage map

| QA category | Primary layers | Pass requires |
|-------------|----------------|---------------|
| ARCHITECTURE | L1–L5 | Blueprint + pages + blocks + validation evidence |
| LEGAL | L10 | Legal routes + LEGAL_PAGE contracts |
| ENTITY | L11 | Entity Card READY or N/A |
| SEO | L6 | Strategy + per-page SEO for in-scope pages |
| DESIGN | L7 | Pattern bindings for in-scope blocks |
| CONTENT | L8 | Signal bindings for in-scope blocks |
| CONTENT_VALIDATION | L9 | Validation runs PASS |
| GENERATION_READINESS | L12 | Generation contract + GATE_GENERATION_READY |
| HANDOFF_READINESS | L12 outputs | Handoff package + QA pass |
| DOCUMENTATION_INTEGRITY | all | Version pins ACCEPTED/FROZEN; no orphan refs |

---

## 7. Pass requirements (summary)

| Level | Requirement |
|-------|-------------|
| **Per layer** | Artefact exists, correct version, acceptance state ACCEPTED or FROZEN |
| **Per page (in scope)** | PAGE-CONTRACT + block validation + content validation for that route |
| **Per project** | All site-type **R** layers; Production QA gates 1–9; contract status PASS* |
| **Handoff** | Gate 10 + operator approval |

\* `PASS_WITH_WARNINGS` allowed only per severity system with documented waivers.

---

## 8. Matrix usage (operator)

1. Select `site_type_code` row (§4).
2. List blueprint `required_pages` → map to `page_type` (§5).
3. For each in-scope page, confirm L3–L9 cells.
4. Run [PRODUCTION-QA-CHECKLIST-v1.md](PRODUCTION-QA-CHECKLIST-v1.md).
5. Record outcomes in PRODUCTION-QA-CONTRACT.

---

## 9. SAFE UNKNOWN

- Per-block Production QA micro-matrix — **FUTURE** (see [PRODUCTION-QA-GAPS-v1.md](PRODUCTION-QA-GAPS-v1.md)).
- Extended site types — **not scheduled** in v1.
- Automated matrix diff vs registry — **not implemented**.

---

*Production QA Matrix v1 — architecture coverage only.*
