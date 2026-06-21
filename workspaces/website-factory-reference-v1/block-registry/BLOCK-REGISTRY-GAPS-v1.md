# Website Factory — Block Registry Gaps v1

**Версия:** v1.1 *(WF-R01.2 Gate 2 — Tier A gap closure)*  
**Область:** `workspaces/website-factory-reference-v1/block-registry/`  
**Статус:** cross-layer alignment — Tier A structural gaps **CLOSED** (WF-R01.2 Gate 2)  
**Дата:** 2026-06-19 (Gate 2 execution pass)  
**Связь:** [BLOCK-REGISTRY-AUDIT-v1.md](BLOCK-REGISTRY-AUDIT-v1.md), [BLOCK-GAPS-v1.md](BLOCK-GAPS-v1.md), [../page-architecture/PAGE-GAPS-v1.md](../page-architecture/PAGE-GAPS-v1.md)

**Scope:** Validation chain Site Type Registry → Blueprint → Page Architecture → Block Registry. Implementation/design gaps remain in BLOCK-GAPS-v1.

---

## Validation chain status

```
Site Type Registry (registry/)
        ↓  ALIGNED (Core 5 types)
Blueprint (blueprints/)
        ↓  ALIGNED via BLUEPRINT-BLOCK-MAPPING-v1
Page Architecture (page-architecture/)
        ↓  PARTIAL — see gaps below
Block Registry (block-registry/)
        ↓  ALIGNED — **32** canonical block_id (29 Core + 3 structural Tier A)
Design / Frontend
        ↓  OUT OF SCOPE — not started
```

---

## 1. Site Type Registry → Block Registry

| Check | Status | Gap |
|-------|--------|-----|
| Core site types in BLOCK-REGISTRY `allowed_site_types` | **PASS** | LANDING, PROMO, CATALOG, ECOMMERCE, CORPORATE only |
| SITE-TYPE-BLOCK-MATRIX-v2 covers all 32 blocks | **PASS** | v2.1 — WF-R01.2 Gate 2 structural rows |
| registry/SITE-TYPE-BLOCK-MAPPING-v1 superseded | **CLOSED** (2026-06-01) | [HYGIENE-PASS-v1.md](../HYGIENE-PASS-v1.md) — banner + block-registry/ pointers |
| Extended Types (SAAS, WEB_APPLICATION, MARKETPLACE) | **OUT OF SCOPE** | No block rows in Core matrix v2 |

---

## 2. Blueprint → Block Registry

| Check | Status | Gap |
|-------|--------|-----|
| 5 Core Blueprints mapped | **PASS** | [BLUEPRINT-BLOCK-MAPPING-v1.md](BLUEPRINT-BLOCK-MAPPING-v1.md) |
| Blueprint `required_blocks` human labels → block_id | **PARTIAL** | Blueprints use "Social proof" — operator maps to TRUST/TESTIMONIALS |
| LANDING sticky CTA → block_id | **RESOLVED** | Maps to `CTA` (sticky = variant in notes) |
| CATALOG "Filters / Search" → block_id | **CLOSED** (2026-06-19) | `FILTERS`, `SEARCH` — WF-R01.2 Gate 2 |
| Header/nav → block_id | **CLOSED** (2026-06-19) | `HEADER_NAV` — WF-R01.2 Gate 2 |

---

## 3. Page Architecture → Block Registry

| Check | Status | Gap |
|-------|--------|-----|
| PAGE-BLOCK-MAPPING-v1 for 10 page types | **PASS** | Created in alignment pass |
| CORE-PAGE-ARCHITECTURES-v1 mobile sticky CTA | **RESOLVED** (2026-06-04) | Canonical `CTA`; sticky = implementation variant |
| CORE-PAGE-ARCHITECTURES-v1 embedded video | **RESOLVED** (2026-06-04) | Media embed note — not a `block_id` |
| CORE-PAGE-ARCHITECTURES implicit FEATURES on PDP | **RESOLVED** | `FEATURES` block_id added |
| REVIEWS_PAGE → block_id | **RESOLVED** | `REVIEWS` + `TESTIMONIALS` mapped in PAGE-BLOCK-MAPPING-v1 |
| ECOMMERCE utility pages (cart/checkout) | **PARTIAL** | Documented in PAGE-BLOCK-MAPPING; not in PAGE-TYPE-REGISTRY minimum |
| LEGAL_PAGE marketing blocks forbidden | **PASS** | Aligned with LEGAL-PAGE-CONTRACT-v1 |

---

## 4. Block Registry internal completeness

| Check | Status | Gap |
|-------|--------|-----|
| Operator minimum 32 block_id set | **PASS** | 29 Core + HEADER_NAV, FILTERS, SEARCH (Tier A) |
| BLOCK-CONTRACT-v1 fields on every entry | **PARTIAL** | Full contract on 6 newer blocks (3 alignment + 3 structural); legacy entries abbreviated |
| BLOCK-CATEGORY-SYSTEM-v1 assignment | **PASS** | 32 blocks assigned; NAVIGATION populated |
| BLOCK-CONVERSION-ROLES-v1 assignment | **PASS** | 32 blocks assigned |
| BLOCK-DEPENDENCY-RULES closure | **PASS** | Commerce chain + structural section (WF-R01.2 Gate 2) |

---

## 5. Legal Pack → Block Registry

| Check | Status | Gap |
|-------|--------|-----|
| LEGAL_LINKS → Legal Pack v1 FROZEN | **PASS** | Hard dependency documented |
| LEAD_FORM / CHECKOUT → Consent Rule | **PASS** | |
| ECOMMERCE Legal Extension E1–E4 blocks | **FUTURE** | Not in Core Pack v1 |
| DELIVERY block → legal extension E3 | **NOTED** | Block exists; legal copy FUTURE |

---

## 6. Reference workspace → Block Registry

| Check | Status | Gap |
|-------|--------|-----|
| Partial coverage (9 section partials) | **EXPECTED** | Architecture-only pass |
| social_proof.html → TRUST vs TESTIMONIALS | **PARTIAL** | Code does not split trust variants |
| New blocks FEATURES, CATEGORY_GRID, REVIEWS | **NOT IMPLEMENTED** | Registry-only |

---

## 7. Downstream layers (not in scope)

| Layer | Status |
|-------|--------|
| Page → Block automated validation | **NEXT** (queued after this pass) |
| SEO Mapping v2 block awareness | **ACCEPTED** (seo-architecture/ 2026-06-01) |
| Design System Mapping | **ACCEPTED** (2026-06-04) |
| JSON Schema export | **NOT DEFINED** |
| CI matrix / dependency checks | **NOT IMPLEMENTED** |

---

## Recommended resolution order

| # | Gap | Owner lane |
|---|-----|------------|
| 1 | Update SITE-TYPE-BLOCK-MAPPING-v1 pointer to block-registry/ | **DONE** — Hygiene Pass v1 (2026-06-01) |
| 2 | CORE-PAGE-ARCHITECTURES: STICKY_CTA/VIDEO drift | **DONE** — Foundation Finalization Pass v1 (2026-06-04) |
| 3 | Page → Block Validation (automated or checklist) | Next priority |
| 4 | HEADER_NAV, FILTERS, SEARCH block_id charter | **DONE** — WF-R01.2 Gate 2 (2026-06-19) |
| 5 | Expand BLOCK-REGISTRY-v1 entries with full contract fields | Registry hygiene |

---

## SAFE UNKNOWN

- Operator COMPLETE gate date for Block Registry Alignment v1 — **pending**
- Whether BLOCK-CATEGORIES-v1.md is retired or kept as alias — **operator decision**
- Triumph workspace block_id retrofit — **out of scope**

---

*Registry gaps version: v1.1 (WF-R01.2 Gate 2 Tier A closure). Canonical location: `workspaces/website-factory-reference-v1/block-registry/`.*
