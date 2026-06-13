# Website Factory — Block Registry Audit v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/block-registry/`  
**Статус:** audit report — Block Registry Alignment v1  
**Дата:** 2026-05-31  
**Не является:** remediation plan, automated diff tool output

**Scope:** All files in `block-registry/` plus predecessor references in `registry/`, `projects/mars-website-factory/`, and cross-layer docs in `page-architecture/`, `blueprints/`.

---

## 1. Inventory — existing block-registry files

| File | Role | Alignment status (pre-pass) |
|------|------|----------------------------|
| [BLOCK-REGISTRY-v1.md](BLOCK-REGISTRY-v1.md) | Canonical block entries | **Partial** — 26 blocks; missing operator minimum set items |
| [BLOCK-CATEGORIES-v1.md](BLOCK-CATEGORIES-v1.md) | Primary category taxonomy | **Aligned** — 10 categories match charter |
| [CORE-BLOCK-LIBRARY-v1.md](CORE-BLOCK-LIBRARY-v1.md) | Library overview + placement | **Partial** — same 26-block set |
| [SITE-TYPE-BLOCK-MATRIX-v2.md](SITE-TYPE-BLOCK-MATRIX-v2.md) | Site type × block stance | **Partial** — no FEATURES / CATEGORY_GRID / REVIEWS rows |
| [BLOCK-DEPENDENCY-RULES-v1.md](BLOCK-DEPENDENCY-RULES-v1.md) | Hard/soft deps | **Partial** — missing page-type deps |
| [BLOCK-CONVERSION-ROLES-v1.md](BLOCK-CONVERSION-ROLES-v1.md) | Conversion classes | **Partial** — same 26-block set |
| [BLOCK-IMPLEMENTATION-RULES-v1.md](BLOCK-IMPLEMENTATION-RULES-v1.md) | Factory usage flow | **Aligned** |
| [BLOCK-GAPS-v1.md](BLOCK-GAPS-v1.md) | Implementation/design gaps | **Aligned** — honesty register |

**Missing (charter-required, created in this pass):**

| File | Purpose |
|------|---------|
| BLOCK-CONTRACT-v1.md | Formal field contract |
| BLOCK-CATEGORY-SYSTEM-v1.md | Canonical category system (supersedes naming drift) |
| BLOCK-REGISTRY-AUDIT-v1.md | This document |
| PAGE-BLOCK-MAPPING-v1.md | Page type × block stance |
| BLUEPRINT-BLOCK-MAPPING-v1.md | Blueprint × block stance |
| BLOCK-REGISTRY-GAPS-v1.md | Cross-layer alignment gaps |

---

## 2. Duplicates

| Duplicate pattern | Locations | Resolution |
|-------------------|-----------|------------|
| Block field schema | BLOCK-REGISTRY-v1 §Field schema; implied in CORE-BLOCK-LIBRARY | **Extract** → [BLOCK-CONTRACT-v1.md](BLOCK-CONTRACT-v1.md) |
| Category taxonomy | BLOCK-CATEGORIES-v1; category tables inside BLOCK-REGISTRY-v1 | **Canonical** → [BLOCK-CATEGORY-SYSTEM-v1.md](BLOCK-CATEGORY-SYSTEM-v1.md); BLOCK-CATEGORIES-v1 retained as alias pointer |
| Site type × block matrix | SITE-TYPE-BLOCK-MATRIX-v2; summary tables in CORE-BLOCK-LIBRARY-v1 | **Authoritative** matrix v2; library shows placement only |
| Page × block stacks | CORE-PAGE-ARCHITECTURES-v1 (page-architecture/); partial overlap with blueprints `required_blocks` | **Split:** page stance → PAGE-BLOCK-MAPPING-v1; blueprint stance → BLUEPRINT-BLOCK-MAPPING-v1 |
| Gaps register | BLOCK-GAPS-v1 (implementation); PAGE-GAPS-v1 (page layer) | **Add** BLOCK-REGISTRY-GAPS-v1 for cross-layer alignment only |
| Predecessor registry | `registry/SITE-TYPE-BLOCK-MAPPING-v1.md`; `projects/mars-website-factory/block-registry-v0.md` | **Superseded** for Core `block_id` by block-registry/ — do not merge vocabularies |

### Semantic duplicates (same intent, different block_id)

| Pair | Issue | Resolution |
|------|-------|------------|
| `TRUST` ↔ `TESTIMONIALS` | Reference `social_proof.html` maps to TRUST; testimonials overlap | **Split:** TRUST = logos/metrics/badges; TESTIMONIALS = curated quotes |
| `TRUST` ↔ `REVIEWS` | ECOMMERCE "Reviews" in v1 mapping vs TESTIMONIALS in registry | **Add** `REVIEWS` — UGC ratings/list; TESTIMONIALS = editorial quotes |
| `CATEGORIES` ↔ `CATEGORY_GRID` | v1 mapping "Category grid" vs registry `CATEGORIES` only | **Split:** CATEGORIES = taxonomy/nav; CATEGORY_GRID = visual category tile grid |
| `BENEFITS` ↔ `FEATURES` | PDP "features list" in CORE-PAGE-ARCHITECTURES vs no FEATURES block_id | **Add** `FEATURES` — capability/spec highlights |
| `CTA` ↔ `STICKY_CTA` | CORE-PAGE-ARCHITECTURES lists `STICKY_CTA`; registry uses single `CTA` | **Keep** `CTA` only; sticky = implementation variant (document in notes) |

---

## 3. Overlaps

| Overlap | Systems involved | Risk |
|---------|------------------|------|
| Block selection | Blueprint `required_blocks` · SITE-TYPE-BLOCK-MATRIX-v2 · CORE-PAGE-ARCHITECTURES-v1 | Drift if updated in one layer only |
| Trust blocks | TRUST · TESTIMONIALS · REVIEWS · CASES | Operator may stack redundant proof |
| Catalog blocks | CATEGORIES · CATEGORY_GRID · PRODUCT_GRID · PRODUCT_CARD | IA must define hierarchy |
| Conversion path | CTA · LEAD_FORM · CONTACTS · CHECKOUT | Multiple PRIMARY_CONVERSION candidates |
| Legal surface | LEGAL_LINKS · FOOTER · LEGAL_PAGE content | Footer Rule vs legal page body |
| Commerce | CART · CHECKOUT · PAYMENT · DELIVERY | Subtree vs global placement |

---

## 4. Naming conflicts

| Conflict | Detail | Canonical choice |
|----------|--------|------------------|
| snake_case vs UPPER_SNAKE | block-registry-v0 uses `hero`, `lead_form`; v1 uses `HERO`, `LEAD_FORM` | **UPPER_SNAKE_CASE** `block_id` in v1 |
| Block role vs block_id | SITE-TYPE-BLOCK-MAPPING-v1 "Hero · Benefits" vs `HERO`, `BENEFITS` | **block_id** only in new artifacts |
| "Social proof" label | Maps to TRUST in v1; v0 undifferentiated | **TRUST** for logos/metrics; **TESTIMONIALS** / **REVIEWS** for quotes/ratings |
| `block_category` vs `primary_category` | Registry uses `primary_category`; charter says `block_category` | **block_category** in contract; registry field aliased in BLOCK-CONTRACT-v1 |
| Page type vs site type | `LANDING` site type vs `LANDING_PAGE` page type | **Never** interchange — page mapping uses page_type codes only |

---

## 5. Missing fields (pre-alignment)

| Field | Required by charter | Pre-pass status |
|-------|---------------------|-----------------|
| `block_id` | Yes | Present |
| `block_name` | Yes | Present |
| `block_category` | Yes | Present as `primary_category` only |
| `purpose` | Yes | Present |
| `conversion_role` | Yes | Present |
| `allowed_site_types` | Yes | Present |
| `allowed_page_types` | Yes | **Missing** from BLOCK-REGISTRY-v1 |
| `required_or_optional` | Yes | Present (registry default) |
| `dependencies` | Yes | Present |
| `exclusions` | Yes | Present |
| `notes` | Yes | **Partial** — embedded in prose, not structured |

**Missing block_id entries (operator minimum set):**

| block_id | Pre-pass |
|----------|----------|
| `FEATURES` | **Absent** |
| `CATEGORY_GRID` | **Absent** (conflated with CATEGORIES) |
| `REVIEWS` | **Absent** (conflated with TESTIMONIALS) |

All other minimum-set blocks were present (29 required → 26 existed + 3 added in alignment pass).

---

## 6. Registry drift

| Drift vector | Observation | Severity |
|--------------|-------------|----------|
| registry/SITE-TYPE-BLOCK-MAPPING-v1 | Superseded banner + block-registry/ pointers (2026-06-01); Extended Types rows | **Low** — historical roles only |
| page-architecture/CORE-PAGE-ARCHITECTURES-v1 | Uses `STICKY_CTA`, `VIDEO` (non-canonical block_id) | **Medium** |
| Blueprint block roles | Human labels ("Social proof") vs block_id | **Low** — mapping docs resolve |
| Reference partials | 9/29 blocks implemented | **Expected** — architecture only |
| SITE-TYPE-BLOCK-MATRIX-v2 | No rows for new canonical blocks | **High** — fixed in alignment pass |
| BLOCK-REGISTRY count | Declared 26 → 29 after alignment | **Fixed** |

### Cross-layer chain drift (Site Type → Blueprint → Page → Block)

| Link | Status |
|------|--------|
| Site Type Registry → Blueprint | **Aligned** — 5 Core blueprints |
| Blueprint → Block (site-level) | **Partial** — BLUEPRINT-BLOCK-MAPPING-v1 created |
| Page Architecture → Block (page-level) | **Partial** — PAGE-BLOCK-MAPPING-v1 created |
| Page CORE-PAGE-ARCHITECTURES ↔ Block Registry | **Drift** — STICKY_CTA, FEATURES implicit |
| Legal Pack → LEGAL_LINKS / forms | **Aligned** — FROZEN |

---

## 7. Audit conclusions

| Finding | Action |
|---------|--------|
| block-registry/ directory existed with substantial v1 content | **Audit + align**, not blind recreate |
| 3 block_id gaps vs operator minimum set | **Added** FEATURES, CATEGORY_GRID, REVIEWS |
| No formal BLOCK-CONTRACT | **Created** BLOCK-CONTRACT-v1.md |
| No page-level or blueprint-level block mapping docs | **Created** PAGE-BLOCK-MAPPING-v1, BLUEPRINT-BLOCK-MAPPING-v1 |
| Category doc naming drift | **Created** BLOCK-CATEGORY-SYSTEM-v1.md as canonical name |
| Cross-layer validation undocumented | **Created** BLOCK-REGISTRY-GAPS-v1.md |

---

## SAFE UNKNOWN

- Automated audit re-run on file change — **not implemented**
- Whether BLOCK-CATEGORIES-v1.md should be deleted vs alias — **operator decision**; v1 keeps alias pointer
- Triumph / v0 project retrofits — **out of scope**

---

*Audit version: v1. Canonical location: `workspaces/website-factory-reference-v1/block-registry/`.*
