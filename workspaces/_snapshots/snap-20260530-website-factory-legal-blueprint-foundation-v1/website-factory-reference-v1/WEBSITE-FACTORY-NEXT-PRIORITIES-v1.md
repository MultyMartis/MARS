# Website Factory — Next Priorities v1

**Версия:** v1 (sequence update 2026-05-30 — Block Registry alignment)  
**Область:** `workspaces/website-factory-reference-v1/`  
**Статус:** operator-approved priority register — **documentation only**  
**Дата регистрации:** 2026-05-30

**Контекст:** **Website Factory Legal Pack v1 FROZEN** (2026-05-30) — see [legal/LEGAL-PACK-v1-FREEZE.md](legal/LEGAL-PACK-v1-FREEZE.md); Triumph Legal Pilot Phase 2 complete; **SITE-TYPE-BLUEPRINTS-v1** Core system authored; **active workstream: BLOCK REGISTRY ALIGNMENT v1**.

---

## Completed / frozen systems (not sequenced priorities)

| System | Location | Status |
|--------|----------|--------|
| **Website Factory Legal Pack v1** | [legal/](legal/) + [legal-entity/](legal-entity/) | **FROZEN** (2026-05-30) — [LEGAL-PACK-v1-FREEZE.md](legal/LEGAL-PACK-v1-FREEZE.md) |
| **Legal Entity Discovery System v1** | [legal-entity/](legal-entity/) | **COMPLETE / FROZEN** (part of Legal Pack v1) |
| **Legal Template Hardening v1.1** | [legal/LEGAL-TEMPLATE-HARDENING-v1.1.md](legal/LEGAL-TEMPLATE-HARDENING-v1.1.md) | **COMPLETE / FROZEN** (part of Legal Pack v1) |
| **Triumph Legal Pilot (Phase 2)** | `workspaces/triumph-manipulator-landing-v6/` | **COMPLETE** (2026-05-30) — validated at freeze |

---

## Priority register

| # | Priority | Scope | Status |
|---|----------|-------|--------|
| **1** | SITE-TYPE-BLUEPRINTS-v1 | Page blueprints per approved site type | **IN PROGRESS** — Core Blueprint System v1 authored |
| **2** | BLOCK REGISTRY ALIGNMENT v1 | Canonical Block Registry ↔ Blueprints ↔ Site Types | **IN PROGRESS** |
| **3** | SITE-TYPE-SEO-MAPPING-v2 | SEO mapping upgrade (successor to v1 in registry) | **APPROVED — QUEUED** |
| **4** | DESIGN SYSTEM MAPPING | Design tokens / components ↔ site types | **APPROVED — QUEUED** |

**Moved to COMPLETED / FROZEN (2026-05-30):** Legal Pack v1 (templates, entity discovery, generation contract, workflow) + Triumph Legal Pilot Phase 2 — see [legal/LEGAL-PACK-v1-FREEZE.md](legal/LEGAL-PACK-v1-FREEZE.md).

**Примечание:** [SITE-TYPE-LEGAL-MAPPING-v2.md](legal/SITE-TYPE-LEGAL-MAPPING-v2.md) operationalized via Triumph pilot; frozen as part of Legal Pack v1.

---

## Legal Entity Discovery System v1 (COMPLETE)

**Goal:** Standardized discovery, extraction, validation and storage of client legal entity data — primary source for legal pages, footer, contacts, extensions.

**Deliverables:**

- [legal-entity/LEGAL-ENTITY-DISCOVERY-RULES-v1.md](legal-entity/LEGAL-ENTITY-DISCOVERY-RULES-v1.md)
- [legal-entity/LEGAL-ENTITY-CARD-v1.md](legal-entity/LEGAL-ENTITY-CARD-v1.md) + template, workflow, input standard, extraction, validation
- [legal-entity/TRIUMPH-LEGAL-ENTITY-LESSON-v1.md](legal-entity/TRIUMPH-LEGAL-ENTITY-LESSON-v1.md)
- Integration: [LEGAL-PACK-ARCHITECTURE-v1.md](legal/LEGAL-PACK-ARCHITECTURE-v1.md), [LEGAL-INPUT-SHEET-v1.md](legal/LEGAL-INPUT-SHEET-v1.md), [LEGAL-GENERATION-WORKFLOW-v1.md](legal/LEGAL-GENERATION-WORKFLOW-v1.md)

**Per-project input path:** `project-input/legal-entity/`

**Status:** **COMPLETE**

---

## COMPLETED / FROZEN — Legal Pack v1 + Triumph Pilot

**Status:** **FROZEN** — [legal/LEGAL-PACK-v1-FREEZE.md](legal/LEGAL-PACK-v1-FREEZE.md)

**Includes:** Legal Template Hardening v1.1, Legal Entity Discovery v1, Triumph Legal Pilot Phase 2 (V6).

**Pilot validation (2026-05-30):** L1–L4 pages generated; canonical URLs; Footer Rule + Consent Rule PASS; zero forbidden placeholders in legal content.

**Historical docs:** [legal/pilots/TRIUMPH-LEGAL-PILOT-PLAN-v1.md](legal/pilots/TRIUMPH-LEGAL-PILOT-PLAN-v1.md), [legal/pilots/TRIUMPH-LEGAL-GAP-REPORT-v1.md](legal/pilots/TRIUMPH-LEGAL-GAP-REPORT-v1.md), [legal/pilots/TRIUMPH-LEGAL-PILOT-EXECUTION-v1.md](legal/pilots/TRIUMPH-LEGAL-PILOT-EXECUTION-v1.md) — superseded by freeze pass for production readiness claims.

---

## Priority 1 — SITE-TYPE-BLUEPRINTS-v1 (IN PROGRESS)

**Goal:** Define canonical page blueprints for each approved Core site type (IA skeleton, required pages, blocks, legal/SEO/conversion requirements, exclusions).

**Inputs:**

- [SITE-TYPE-REGISTRY-v1.md](registry/SITE-TYPE-REGISTRY-v1.md)
- [SITE-TYPE-MATRIX-v1.md](registry/SITE-TYPE-MATRIX-v1.md)
- [SITE-TYPE-BLOCK-MAPPING-v1.md](registry/SITE-TYPE-BLOCK-MAPPING-v1.md)
- [SITE-TYPE-SEO-MAPPING-v1.md](registry/SITE-TYPE-SEO-MAPPING-v1.md)
- [SITE-TYPE-LEGAL-MAPPING-v2.md](legal/SITE-TYPE-LEGAL-MAPPING-v2.md)
- [LEGAL-PACK-ARCHITECTURE-v1.md](legal/LEGAL-PACK-ARCHITECTURE-v1.md)

**Output (delivered):** `blueprints/` — [BLUEPRINT-SYSTEM-v1.md](blueprints/BLUEPRINT-SYSTEM-v1.md) + 5 Core Type Blueprints + contract, matrix, implementation rules, gaps.

**Not in scope:** Runtime page generator; Extended Type Blueprints (SAAS, WEB_APPLICATION, MARKETPLACE).

**Status:** **IN PROGRESS** — Core Blueprint System v1 authored; operator review / COMPLETE gate pending.

---

## Priority 2 — BLOCK REGISTRY ALIGNMENT v1 (IN PROGRESS)

**Goal:** Create canonical Block Registry — production bridge Site Type → Blueprint → Pages → Blocks → Design → Frontend.

**Inputs:**

- [blueprints/](blueprints/) — Core Blueprints v1
- [registry/SITE-TYPE-REGISTRY-v1.md](registry/SITE-TYPE-REGISTRY-v1.md)
- [registry/SITE-TYPE-MATRIX-v1.md](registry/SITE-TYPE-MATRIX-v1.md)
- [registry/SITE-TYPE-BLOCK-MAPPING-v1.md](registry/SITE-TYPE-BLOCK-MAPPING-v1.md)
- Reference workspace sections (`src/partials/sections/`)
- Legal Pack v1 (FROZEN)

**Output (delivered):** `block-registry/` — BLOCK-REGISTRY-v1, categories, core library, SITE-TYPE-BLOCK-MATRIX-v2, dependency rules, conversion roles, implementation rules, gaps.

**Not in scope:** Design generation, frontend implementation, Extended Type blocks, Legal Pack modifications, Triumph workspace changes.

**Status:** **IN PROGRESS** — canonical registry authored; operator COMPLETE gate + mapping v1 cross-link update pending.

---

## Priority 3 — SITE-TYPE-SEO-MAPPING-v2

**Goal:** Successor to [SITE-TYPE-SEO-MAPPING-v1.md](registry/SITE-TYPE-SEO-MAPPING-v1.md) with parity to legal v2 depth (matrix per site type).

**Not in scope:** SEO content generation.

---

## Priority 4 — DESIGN SYSTEM MAPPING

**Goal:** Map design system tokens/components to site types (visual contract alignment).

**Related:** `projects/orca/visual-semantics/contracts/website-factory-visual-contract-v0.md`

---

## Explicit exclusions

| Item | Status |
|------|--------|
| Mobile App Factory | **OUT OF SCOPE** — FUTURE separate factory |
| New site types beyond 8 approved | **FORBIDDEN** without registry charter |
| Governance expansion | **NOT APPROVED** |
| Automatic legal HTML pipeline | **FUTURE** — not in current priority queue |

**Approved site types only:** LANDING, PROMO, CATALOG, ECOMMERCE, CORPORATE, SAAS, WEB_APPLICATION, MARKETPLACE.

---

## SAFE UNKNOWN

- Exact delivery dates per priority — **not scheduled** in this document.
- Triumph production deploy authorization — **UNKNOWN** — legal pages generated; deploy gate not in this document.
- CI automation for legal contract — **FUTURE** — not in current priority queue.

---

*Priorities version: v1 (Legal Pack freeze update 2026-05-30). Canonical location: `workspaces/website-factory-reference-v1/`.*
