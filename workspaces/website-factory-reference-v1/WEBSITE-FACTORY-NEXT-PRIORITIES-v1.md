# Website Factory — Next Priorities v1



**Версия:** v1 (foundation freeze update 2026-06-01)  

**Область:** `workspaces/website-factory-reference-v1/`  

**Статус:** operator-approved priority register — **documentation only**  

**Дата регистрации:** 2026-05-30



**Контекст:** **Website Factory Foundation v1 FROZEN** (2026-06-01) — [WEBSITE-FACTORY-FOUNDATION-v1-FREEZE.md](WEBSITE-FACTORY-FOUNDATION-v1-FREEZE.md); **Legal Pack v1 FROZEN** (2026-05-30) — [legal/LEGAL-PACK-v1-FREEZE.md](legal/LEGAL-PACK-v1-FREEZE.md); **Architecture Foundation v1** — **ACCEPTED** — [ARCHITECTURE-FOUNDATION-v1.md](ARCHITECTURE-FOUNDATION-v1.md); foundation checkpoint — [WEBSITE-FACTORY-FOUNDATION-CHECKPOINT-v1.md](WEBSITE-FACTORY-FOUNDATION-CHECKPOINT-v1.md); Triumph Legal Pilot Phase 2 complete.



## Current workstream status (2026-06-01)



| Item | Status |

|------|--------|

| **Website Factory Foundation v1** | **FROZEN** — [WEBSITE-FACTORY-FOUNDATION-v1-FREEZE.md](WEBSITE-FACTORY-FOUNDATION-v1-FREEZE.md) |

| **Current active Website Factory workstream** | **NONE** |

| **Next approved workstream** | **SITE-TYPE-SEO-MAPPING-v2** — **QUEUED** (not started) |



---



## Completed / frozen systems (not sequenced priorities)



| System | Location | Status |

|--------|----------|--------|

| **Website Factory Legal Pack v1** | [legal/](legal/) + [legal-entity/](legal-entity/) | **FROZEN** (2026-05-30) — [LEGAL-PACK-v1-FREEZE.md](legal/LEGAL-PACK-v1-FREEZE.md) |

| **Legal Entity Discovery System v1** | [legal-entity/](legal-entity/) | **COMPLETE / FROZEN** (part of Legal Pack v1) |

| **Legal Template Hardening v1.1** | [legal/LEGAL-TEMPLATE-HARDENING-v1.1.md](legal/LEGAL-TEMPLATE-HARDENING-v1.1.md) | **COMPLETE / FROZEN** (part of Legal Pack v1) |

| **Triumph Legal Pilot (Phase 2)** | `workspaces/triumph-manipulator-landing-v6/` | **COMPLETE** (2026-05-30) — validated at freeze |

| **Site Type Registry v1** | [registry/](registry/) | **ACCEPTED** |

| **Site Type Blueprints v1 (Core 5)** | [blueprints/](blueprints/) | **ACCEPTED** — Core Blueprint System v1 |

| **Page Architecture Contracts v1** | [page-architecture/](page-architecture/) | **ACCEPTED** (2026-05-31) |

| **Block Registry Alignment v1** | [block-registry/](block-registry/) | **ACCEPTED** (2026-05-31) |

| **Page → Block Validation v1** | [page-block-validation/](page-block-validation/) | **ACCEPTED** (2026-06-01) |

| **Architecture Foundation v1** | [ARCHITECTURE-FOUNDATION-v1.md](ARCHITECTURE-FOUNDATION-v1.md) | **ACCEPTED** (2026-06-01) |

| **Website Factory Foundation v1** | [WEBSITE-FACTORY-FOUNDATION-v1-FREEZE.md](WEBSITE-FACTORY-FOUNDATION-v1-FREEZE.md) | **FROZEN** (2026-06-01) |



---



## Sequence after foundation v1 freeze



| Phase | Workstream | Status |

|-------|------------|--------|

| **Now** | *(none — foundation frozen)* | **NONE** |

| **Next** | SITE-TYPE-SEO-MAPPING-v2 | **APPROVED — QUEUED** (not started) |

| **Next 1** | DESIGN SYSTEM MAPPING | **APPROVED — QUEUED** |

| **Future** | Content Contracts, Generation Contracts, QA automation evolution | **NOT QUEUED** — charter required |



---



## Priority register



| # | Priority | Scope | Status |

|---|----------|-------|--------|

| **—** | ARCHITECTURE FOUNDATION v1 | Consolidation checkpoint — layer map, accepted/frozen systems, health check | **COMPLETE** (2026-06-01) — [ARCHITECTURE-FOUNDATION-v1.md](ARCHITECTURE-FOUNDATION-v1.md) |

| **1** | SITE-TYPE-BLUEPRINTS-v1 | Page blueprints per approved site type | **ACCEPTED** — Core 5 Blueprints; Extended Types not started |

| **2** | BLOCK REGISTRY ALIGNMENT v1 | Canonical Block Registry ↔ Blueprints ↔ Site Types ↔ Pages | **ACCEPTED** — [block-registry/](block-registry/) aligned 2026-05-31 |

| **3** | PAGE ARCHITECTURE CONTRACTS v1 | Page-level contracts ↔ Blueprints ↔ Block Registry | **ACCEPTED** — [page-architecture/](page-architecture/) |

| **4** | Page → Block Validation v1 | First validation layer: page architecture ↔ required blocks | **ACCEPTED** — [page-block-validation/](page-block-validation/) 2026-06-01 |

| **5** | SITE-TYPE-SEO-MAPPING-v2 | SEO mapping upgrade (successor to v1 in registry) | **APPROVED — QUEUED** (not started) |

| **6** | DESIGN SYSTEM MAPPING | Design tokens / components ↔ site types ↔ blocks | **APPROVED — QUEUED** (after SEO v2) |



**Moved to COMPLETED / FROZEN (2026-05-30):** Legal Pack v1 (templates, entity discovery, generation contract, workflow) + Triumph Legal Pilot Phase 2 — see [legal/LEGAL-PACK-v1-FREEZE.md](legal/LEGAL-PACK-v1-FREEZE.md).



**Moved to ACCEPTED (2026-05-31):** Page Architecture Contracts v1 — [page-architecture/PAGE-ARCHITECTURE-SYSTEM-v1.md](page-architecture/PAGE-ARCHITECTURE-SYSTEM-v1.md); Block Registry Alignment v1 — [block-registry/BLOCK-REGISTRY-v1.md](block-registry/BLOCK-REGISTRY-v1.md).



**Moved to ACCEPTED (2026-06-01):** Page → Block Validation v1 — [page-block-validation/PAGE-BLOCK-VALIDATION-SYSTEM-v1.md](page-block-validation/PAGE-BLOCK-VALIDATION-SYSTEM-v1.md).



**Примечание:** [SITE-TYPE-LEGAL-MAPPING-v2.md](legal/SITE-TYPE-LEGAL-MAPPING-v2.md) operationalized via Triumph pilot; frozen as part of Legal Pack v1.



---



## Priority 2 — BLOCK REGISTRY ALIGNMENT v1 (ACCEPTED)



**Goal:** Create canonical Block Registry — production bridge Site Type → Blueprint → Page Architecture → Blocks → Design → Frontend.



**Inputs:**



- [blueprints/](blueprints/) — Core Blueprints v1

- [page-architecture/](page-architecture/) — Page Architecture v1 (ACCEPTED)

- [registry/SITE-TYPE-REGISTRY-v1.md](registry/SITE-TYPE-REGISTRY-v1.md)

- [registry/SITE-TYPE-MATRIX-v1.md](registry/SITE-TYPE-MATRIX-v1.md)

- Reference workspace sections (`src/partials/sections/`)

- Legal Pack v1 (FROZEN)



**Output (delivered):** `block-registry/` — BLOCK-CONTRACT-v1, BLOCK-REGISTRY-v1 (29 blocks), BLOCK-CATEGORY-SYSTEM-v1, PAGE-BLOCK-MAPPING-v1, BLUEPRINT-BLOCK-MAPPING-v1, BLOCK-REGISTRY-AUDIT-v1, BLOCK-REGISTRY-GAPS-v1, SITE-TYPE-BLOCK-MATRIX-v2, dependency rules, conversion roles, implementation rules, gaps.



**Status:** **ACCEPTED** (2026-05-31). Residual drift items (`STICKY_CTA`, `VIDEO`) tracked in [block-registry/BLOCK-REGISTRY-GAPS-v1.md](block-registry/BLOCK-REGISTRY-GAPS-v1.md) and [page-block-validation/VALIDATION-GAPS-v1.md](page-block-validation/VALIDATION-GAPS-v1.md).



---



## Priority 3 — PAGE ARCHITECTURE CONTRACTS v1 (ACCEPTED)



**Goal:** Page-level architecture contracts bridging Blueprints, Block Registry, and frontend page structure.



**Output:** `page-architecture/` — PAGE-ARCHITECTURE-SYSTEM-v1, PAGE-CONTRACT-v1, PAGE-TYPE-REGISTRY-v1, CORE-PAGE-ARCHITECTURES-v1, SITE-TYPE-PAGE-MATRIX-v1, PAGE-DEPENDENCY-RULES-v1, LEGAL-PAGE-CONTRACT-v1, PAGE-IMPLEMENTATION-RULES-v1, PAGE-GAPS-v1.



**Status:** **ACCEPTED** (2026-05-31).



---



## Priority 4 — Page → Block Validation v1 (ACCEPTED)



**Goal:** Define first validation layer — verify page architecture complies with required blocks per PAGE-BLOCK-MAPPING-v1 and Blueprint context.



**Inputs:**



- [page-architecture/CORE-PAGE-ARCHITECTURES-v1.md](page-architecture/CORE-PAGE-ARCHITECTURES-v1.md)

- [block-registry/PAGE-BLOCK-MAPPING-v1.md](block-registry/PAGE-BLOCK-MAPPING-v1.md)

- [block-registry/BLUEPRINT-BLOCK-MAPPING-v1.md](block-registry/BLUEPRINT-BLOCK-MAPPING-v1.md)

- [block-registry/BLOCK-REGISTRY-GAPS-v1.md](block-registry/BLOCK-REGISTRY-GAPS-v1.md)



**Output (delivered):** `page-block-validation/` — PAGE-BLOCK-VALIDATION-SYSTEM-v1, VALIDATION-CONTRACT-v1, PAGE-BLOCK-VALIDATION-RULES-v1, PAGE-TYPE-VALIDATION-MATRIX-v1, BLUEPRINT-VALIDATION-MATRIX-v1, VALIDATION-SEVERITY-SYSTEM-v1, VALIDATION-FAILURE-LIBRARY-v1, VALIDATION-GAPS-v1, VALIDATION-ROADMAP-v1.



**Not in scope:** Runtime validator CLI, design/SEO generation, automation.



**Status:** **ACCEPTED** (2026-06-01). Foundation gate: [ARCHITECTURE-FOUNDATION-v1.md](ARCHITECTURE-FOUNDATION-v1.md).



---



## Priority 5 — SITE-TYPE-SEO-MAPPING-v2 (QUEUED)



**Goal:** Successor to [SITE-TYPE-SEO-MAPPING-v1.md](registry/SITE-TYPE-SEO-MAPPING-v1.md) with parity to legal v2 depth (matrix per site type) and block_id awareness.



**Not in scope:** SEO content generation.



**Status:** **APPROVED — QUEUED** (authorized after Foundation v1 FREEZE; **not started**).



---



## Priority 6 — DESIGN SYSTEM MAPPING



**Goal:** Map design system tokens/components to site types and block_id (visual contract alignment).



**Related:** `projects/orca/visual-semantics/contracts/website-factory-visual-contract-v0.md`



**Status:** **APPROVED — QUEUED** (after SEO v2).



---



## Explicit exclusions



| Item | Status |

|------|--------|

| Mobile App Factory | **OUT OF SCOPE** — FUTURE separate factory |

| New site types beyond 8 approved | **FORBIDDEN** without registry charter |

| Governance expansion | **NOT APPROVED** |

| Automatic legal HTML pipeline | **FUTURE** — not in current priority queue |

| Architecture Foundation re-expansion | **FORBIDDEN** — foundation FROZEN; use SEO v2 workstream when started |



**Approved site types only:** LANDING, PROMO, CATALOG, ECOMMERCE, CORPORATE, SAAS, WEB_APPLICATION, MARKETPLACE.



---



## SAFE UNKNOWN



- Exact delivery dates per priority — **not scheduled** in this document.

- Triumph production deploy authorization — **UNKNOWN** — legal pages generated; deploy gate not in this document.

- CI automation for block/page contract — **FUTURE** — see [page-block-validation/VALIDATION-ROADMAP-v1.md](page-block-validation/VALIDATION-ROADMAP-v1.md).

- Calendar for SEO Mapping v2 completion — **not scheduled**.



---



*Priorities version: v1 (Foundation Freeze update 2026-06-01). Canonical location: `workspaces/website-factory-reference-v1/`.*

