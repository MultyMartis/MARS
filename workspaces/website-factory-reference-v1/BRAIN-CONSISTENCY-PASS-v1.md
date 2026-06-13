# Website Factory — Brain Consistency Pass v1

**Версия:** v1  
**Дата:** 2026-06-01  
**Operator:** APPROVED BY OPERATOR  
**Область:** `workspaces/website-factory-reference-v1/`  
**Тип:** documentation audit only — **no** new systems, registries, layers, runtime, automation, Design Mapping, or SEO expansion  
**Статус:** **COMPLETE**

**Связанные документы:** [ARCHITECTURE-FOUNDATION-v1.md](ARCHITECTURE-FOUNDATION-v1.md), [WEBSITE-FACTORY-FOUNDATION-v1-FREEZE.md](WEBSITE-FACTORY-FOUNDATION-v1-FREEZE.md), [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md)

---

## Executive summary

Первый полный consistency pass по принятой архитектуре Website Factory Foundation v1 + SEO Architecture Layer v2.

**Вердикт:** цепочка **Site Type → Blueprint → Page Architecture → Block Registry → Validation → SEO** для **Core 5** согласована по матрицам и validation semantics. Критических противоречий, блокирующих Design System Mapping, **не обнаружено**. Обнаружен **документационный drift**: устаревшие указатели на v0/v1 предшественников, отсутствие superseded-баннеров, stale freeze maturity table, non-canonical `block_id` в page architectures, broken snapshot cross-link.

**Design Mapping readiness:** **YES WITH WARNINGS** (см. § Design Mapping readiness).

---

## Audit scope

| Layer / artefact | Path | In scope |
|------------------|------|----------|
| Legal Pack | [legal/](legal/) | Yes (FROZEN — reference integrity only) |
| Legal Entity Discovery | [legal-entity/](legal-entity/) | Yes |
| Site Type Registry | [registry/](registry/) | Yes |
| Blueprints | [blueprints/](blueprints/) | Yes |
| Page Architecture | [page-architecture/](page-architecture/) | Yes |
| Block Registry | [block-registry/](block-registry/) | Yes |
| Page Block Validation | [page-block-validation/](page-block-validation/) | Yes |
| SEO Architecture v2 | [seo-architecture/](seo-architecture/) | Yes |
| Architecture Foundation | [ARCHITECTURE-FOUNDATION-v1.md](ARCHITECTURE-FOUNDATION-v1.md) | Yes |
| Foundation Freeze | [WEBSITE-FACTORY-FOUNDATION-v1-FREEZE.md](WEBSITE-FACTORY-FOUNDATION-v1-FREEZE.md) | Yes |
| Next Priorities | [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md) | Yes |
| Reference `src/` | `src/partials/sections/` | Partial (block partial naming vs `block_id`) |
| Historical checkpoint | [WEBSITE-FACTORY-FOUNDATION-CHECKPOINT-v1.md](WEBSITE-FACTORY-FOUNDATION-CHECKPOINT-v1.md) | Supersession review only |

**Out of scope (per charter):** Design System Mapping, content/generation contracts, runtime/CI, new site/page/block types, governance expansion, registry expansion.

---

## Issue register

| ID | Layer | Severity | Problem | Impact | Recommended correction | Status |
|----|-------|----------|---------|--------|------------------------|--------|
| BCP-001 | Registry | **ERROR** | [registry/SITE-TYPE-BLOCK-MAPPING-v1.md](registry/SITE-TYPE-BLOCK-MAPPING-v1.md) declares canonical `block_id` in `projects/mars-website-factory/block-registry-v0.md` and states Block Registry v1 is "until chartered" — **contradicts** accepted [block-registry/BLOCK-REGISTRY-v1.md](block-registry/BLOCK-REGISTRY-v1.md) | Agents/operators may use v0 snake_case IDs or wrong vocabulary during Design Mapping | Add superseded banner (mirror SITE-TYPE-SEO-MAPPING-v1); point to `block-registry/` + SITE-TYPE-BLOCK-MATRIX-v2; retain file for narrative roles only | **OPEN** |
| BCP-002 | Registry | **WARNING** | [registry/SITE-TYPE-REGISTRY-v1.md](registry/SITE-TYPE-REGISTRY-v1.md) index table lists SITE-TYPE-SEO-MAPPING-v1 and SITE-TYPE-BLOCK-MAPPING-v1 **without** superseded notes | Entry-point drift from canonical SEO v2 and block-registry | Update related-docs table: v2 SEO + block-registry canonical links; mark v1 mappings historical | **OPEN** |
| BCP-003 | Registry | **WARNING** | [registry/SITE-TYPE-IMPLEMENTATION-RULES-v1.md](registry/SITE-TYPE-IMPLEMENTATION-RULES-v1.md) still directs SEO → v1 and blocks → SITE-TYPE-BLOCK-MAPPING-v1 | Implementation rules contradict accepted layers | Patch § cross-links to seo-architecture/ and block-registry/ | **OPEN** |
| BCP-004 | Blueprints | **WARNING** | [blueprints/BLUEPRINT-SYSTEM-v1.md](blueprints/BLUEPRINT-SYSTEM-v1.md), [BLUEPRINT-CONTRACT-v1.md](blueprints/BLUEPRINT-CONTRACT-v1.md), [BLUEPRINT-IMPLEMENTATION-RULES-v1.md](blueprints/BLUEPRINT-IMPLEMENTATION-RULES-v1.md), [BLUEPRINT-GAPS-v1.md](blueprints/BLUEPRINT-GAPS-v1.md) reference SITE-TYPE-SEO-MAPPING-v1 and/or block-registry-v0 as canonical | Blueprint authoring may cite superseded SEO/block sources | Point `seo_requirements` → SITE-TYPE-SEO-MAPPING-v2; blocks → BLOCK-REGISTRY-v1 / BLUEPRINT-BLOCK-MAPPING-v1 | **OPEN** |
| BCP-005 | Blueprints | **INFO** | All five Core Blueprints `seo_requirements` **Source:** still [SITE-TYPE-SEO-MAPPING-v1.md](registry/SITE-TYPE-SEO-MAPPING-v1.md) (LANDING, PROMO, CATALOG, ECOMMERCE, CORPORATE) | Content still valid as hints; canonical path is v2 | Change Source line to SITE-TYPE-SEO-MAPPING-v2 (optional: "derived from v1 hints") | **OPEN** |
| BCP-006 | Page Architecture | **WARNING** | [page-architecture/CORE-PAGE-ARCHITECTURES-v1.md](page-architecture/CORE-PAGE-ARCHITECTURES-v1.md) uses `STICKY_CTA` (required on LANDING_PAGE) — **not** in BLOCK-REGISTRY-v1 (29 ids) | Validation emits WARNING-only (VF-015); Design Mapping may invent duplicate component id | Normalize to `CTA` with sticky variant in notes; remove `STICKY_CTA` from required stack | **OPEN** |
| BCP-007 | Page Architecture | **WARNING** | CORE-PAGE-ARCHITECTURES lists optional `VIDEO` — **no** registry entry | Cannot validate; orphan concept for design tokens | Remove VIDEO, map to HITL media embed, or charter `VIDEO` block_id in registry v1.1 | **OPEN** |
| BCP-008 | Block Registry | **INFO** | HEADER_NAV, FILTERS, SEARCH required in blueprints / CATALOG IA but **absent** from Core 29 `block_id` (documented in BLOCK-GAPS) | Design Mapping must treat as layout chrome, not blocks, until charter | Document explicit "non-block_id chrome" list in Design Mapping charter; or schedule registry v1.1 charter | **OPEN** (by design) |
| BCP-009 | Foundation | **ERROR** | [WEBSITE-FACTORY-FOUNDATION-v1-FREEZE.md](WEBSITE-FACTORY-FOUNDATION-v1-FREEZE.md) §3 maturity: **SEO depth = Shallow (v1), v2 QUEUED** conflicts with §5/§9/§11 (**SEO v2 ACCEPTED**) | Freeze doc contradicts ARCHITECTURE-FOUNDATION and NEXT-PRIORITIES | Align §3 table + §4 exclusions with post-acceptance SEO state (documentation-only patch) | **OPEN** |
| BCP-010 | Foundation | **WARNING** | [WEBSITE-FACTORY-FOUNDATION-v1-FREEZE.md](WEBSITE-FACTORY-FOUNDATION-v1-FREEZE.md) §4 exclusions still list "SEO Mapping v2 **QUEUED — not started**" | Same as BCP-009 — operator confusion at freeze boundary | Mark SEO v2 ACCEPTED; move to accepted systems only | **OPEN** |
| BCP-011 | Foundation | **INFO** | [ARCHITECTURE-FOUNDATION-v1.md](ARCHITECTURE-FOUNDATION-v1.md) §1 purpose still says checkpoint before "**SITE-TYPE-SEO-MAPPING-v2**" | Historical wording after SEO acceptance | Clarify purpose text: post-SEO consolidation; pre-Design Mapping | **OPEN** |
| BCP-012 | Supersession | **WARNING** | [WEBSITE-FACTORY-FOUNDATION-CHECKPOINT-v1.md](WEBSITE-FACTORY-FOUNDATION-CHECKPOINT-v1.md) shows Blueprints/Block Registry **IN PROGRESS**; no historical banner | Readers may treat checkpoint as current state | Add header: **HISTORICAL — superseded by** FOUNDATION FREEZE + ARCHITECTURE-FOUNDATION | **OPEN** |
| BCP-013 | Cross-link | **ERROR** | FOUNDATION-CHECKPOINT links `../_snapshots/snap-20260530-website-factory-legal-blueprint-foundation-v1/` — **path not found** in repo (2026-06-01 scan) | Broken reference | Restore snapshot, repoint link, or mark UNKNOWN + remove broken path | **OPEN** |
| BCP-014 | Registry | **INFO** | [registry/SITE-TYPE-LEGAL-MAPPING-v1.md](registry/SITE-TYPE-LEGAL-MAPPING-v1.md) retained; canonical is [legal/SITE-TYPE-LEGAL-MAPPING-v2.md](legal/SITE-TYPE-LEGAL-MAPPING-v2.md) (LEGAL-PACK-ARCHITECTURE documents supersession) | Low — legal layer uses v2 in blueprints | Add superseded banner on registry v1 (optional hygiene) | **OPEN** |
| BCP-015 | Naming | **INFO** | Duplicate category docs: [BLOCK-CATEGORIES-v1.md](block-registry/BLOCK-CATEGORIES-v1.md) is explicit **alias** to BLOCK-CATEGORY-SYSTEM-v1 | Intentional — not harmful | None required; Design Mapping should use CATEGORY-SYSTEM only | **ACKNOWLEDGED** |
| BCP-016 | Naming | **INFO** | `primary_category` vs `block_category` alias in BLOCK-CONTRACT / BLOCK-REGISTRY entries | Documented alias — minor reader friction | Prefer `block_category` in new artefacts | **ACKNOWLEDGED** |
| BCP-017 | Matrix | **INFO** | ECOMMERCE cart/checkout routes required per Blueprint but **not** rows in SITE-TYPE-PAGE-MATRIX-v1 (noted as utility) | By design — documented in matrix footnote | Design Mapping: treat as route templates outside 10 `page_type` minimum | **ACKNOWLEDGED** |
| BCP-018 | Validation | **INFO** | Validation severity downgrades STICKY_CTA/VIDEO to WARNING per VALIDATION-SEVERITY-SYSTEM | Consistent with gaps; masks page↔registry drift | Resolve via BCP-006/007 before automating validation | **ACKNOWLEDGED** |
| BCP-019 | External | **WARNING** | `projects/mars-website-factory/block-registry-v0.md` and `site-type-registry-v0.md` coexist with v1 workspace | Cross-repo vocabulary mix without charter | Maintain pointer discipline in operator prompts; no merge without charter | **OPEN** |
| BCP-020 | Blueprints | **INFO** | Blueprint `required_blocks` use **human block roles** + partial filenames; BLUEPRINT-BLOCK-MAPPING uses `block_id` | Manual mapping step (documented in BLOCK-REGISTRY-GAPS) | Design Mapping workstream should publish role→`block_id` cheat sheet once | **OPEN** |

**Counts:** CRITICAL 0 · ERROR 3 · WARNING 11 · INFO 8 · ACKNOWLEDGED 4

---

## Task 1 — Layer consistency audit

### Chain verification (Core 5)

| Step | Authority | Downstream consumers | Verdict |
|------|-----------|----------------------|---------|
| Site Type | SITE-TYPE-REGISTRY-v1 (8 types; Core 5 production) | All matrices | **PASS** |
| Blueprint | BLUEPRINT-SYSTEM + 5 Core Blueprints | Page matrix, block mapping, validation | **PASS** |
| Page Architecture | PAGE-TYPE-REGISTRY (10 types), SITE-TYPE-PAGE-MATRIX | PAGE-BLOCK-MAPPING, validation | **PASS** |
| Block Registry | BLOCK-REGISTRY-v1 (29 ids), SITE-TYPE-BLOCK-MATRIX-v2 | Validation, SEO block awareness | **PASS WITH WARNINGS** (BCP-006/007/008) |
| Validation | PAGE-BLOCK-VALIDATION-SYSTEM, BLUEPRINT/PAGE matrices | Operator gate | **PASS** |
| SEO | SEO-ARCHITECTURE-SYSTEM-v2, SEO-ARCHITECTURE-MATRIX | PAGE-SEO-CONTRACT | **PASS** |

### Reference integrity

| Check | Result |
|-------|--------|
| Missing layer folders | **None** — all accepted paths exist |
| Broken internal links (sample: checkpoint snapshot) | **FAIL** — BCP-013 |
| Outdated canonical pointers (registry v1 mappings, blueprint SEO source) | **PARTIAL** — BCP-001–005 |
| Duplicate competing canonicals (v0 block registry vs v1) | **PARTIAL** — BCP-001, BCP-019 |
| Orphan concepts (VIDEO, STICKY_CTA) | **YES** — BCP-006, BCP-007 |
| SEO v1 supersession banner | **PASS** — SITE-TYPE-SEO-MAPPING-v1 has banner |
| Block mapping v1 supersession banner | **FAIL** — BCP-001 |

---

## Task 2 — Naming audit

| Finding | Types affected | Severity |
|---------|----------------|----------|
| `STICKY_CTA` vs `CTA` | LANDING page architecture, validation | WARNING |
| `VIDEO` as pseudo-block_id | Page architecture | WARNING |
| Human labels ("Social proof", "Sticky CTA") vs `TRUST`, `CTA` | Blueprints | INFO |
| v0 snake_case (`hero`, `lead_form`) vs v1 `HERO`, `LEAD_FORM` | projects/mars-website-factory legacy | WARNING |
| SITE-TYPE-BLOCK-MAPPING-v1 vs SITE-TYPE-BLOCK-MATRIX-v2 | Registry vs block-registry | WARNING |
| SITE-TYPE-SEO-MAPPING v1 vs v2 | registry vs seo-architecture | INFO (v1 banner OK) |
| SITE-TYPE-LEGAL-MAPPING v1 (registry) vs v2 (legal/) | registry vs legal | INFO |
| Extended types in registry without blueprint rows | SAAS, WEB_APPLICATION, MARKETPLACE | By design — not drift |

**No v2 Blueprint system conflict detected** — only single BLUEPRINT-SYSTEM-v1 + per-type v1 blueprints.

---

## Task 3 — Matrix consistency audit (Core 5)

Compared: SITE-TYPE-REGISTRY · BLUEPRINT-COMPARISON-MATRIX · SITE-TYPE-PAGE-MATRIX · SITE-TYPE-BLOCK-MATRIX-v2 · BLUEPRINT-BLOCK-MAPPING · BLUEPRINT-VALIDATION-MATRIX · SEO-ARCHITECTURE-MATRIX.

| Dimension | LANDING | PROMO | CATALOG | ECOMMERCE | CORPORATE | Aligned? |
|-----------|---------|-------|---------|-----------|-----------|----------|
| In Registry Core 5 | ✓ | ✓ | ✓ | ✓ | ✓ | **YES** |
| Blueprint exists | ✓ | ✓ | ✓ | ✓ | ✓ | **YES** |
| Required pages (validation matrix) | LANDING_PAGE | HOME+SERVICE+ABOUT+CONTACT | HOME+CAT+PRODUCT+CONTACT | HOME+CAT+PRODUCT+CONTACT+cart/checkout | HOME+ABOUT+CONTACT | **YES** |
| Forbidden commerce on LANDING/PROMO/CATALOG | ✓ | ✓ | ✓ (cart) | — | subtree rules | **YES** |
| Required blocks (validation ↔ block matrix v2) | HERO,BENEFITS,PROCESS,TRUST,FAQ,LEAD_FORM,CTA,… | HERO,SERVICES,ABOUT,… | CATEGORIES,PRODUCT_GRID,PRODUCT_CARD,… | CART,CHECKOUT,PAYMENT,… | HERO,SERVICES,ABOUT,TRUST,… | **YES** |
| SEO intent vs page matrix forbidden rows | LANDING_PAGE only | Multi-page intents | No TRANSACTIONAL site-level | TRANSACTIONAL on PDP | Hub-and-spoke | **YES** |

**Matrix consistency verdict:** **PASS** for Core 5 production semantics. ECOMMERCE utility routes intentionally outside PAGE-TYPE-REGISTRY minimum (BCP-017).

---

## Task 4 — Block registry audit

| Check | Result |
|-------|--------|
| Canonical count | **29** `block_id` in BLOCK-REGISTRY-v1 — consistent across SITE-TYPE-BLOCK-MATRIX-v2, BLUEPRINT-BLOCK-MAPPING, PAGE-BLOCK-MAPPING |
| Missing block_id for blueprint-required chrome | HEADER_NAV, FILTERS, SEARCH — **documented OPEN** (BCP-008) |
| Orphan block_id in page layer | `STICKY_CTA`, `VIDEO` (BCP-006, BCP-007) |
| STICKY_CTA drift | Registry resolves to `CTA`; page layer not updated |
| VIDEO drift | Not in blueprints grep; only CORE-PAGE-ARCHITECTURES |
| Mapping BLUEPRINT-BLOCK ↔ MATRIX v2 | **Aligned** (REQ/OPT/FORB codes match) |
| Predecessor SITE-TYPE-BLOCK-MAPPING-v1 | **Stale canonical claim** (BCP-001) |

---

## Task 5 — Foundation audit

| Document | Matches accepted systems? | Notes |
|----------|---------------------------|-------|
| ARCHITECTURE-FOUNDATION-v1 | **Mostly YES** | Lists all accepted layers including SEO v2; minor stale purpose wording (BCP-011); health check still says "sufficient for SEO v2 start" — should read "post-SEO / pre-Design" |
| WEBSITE-FACTORY-FOUNDATION-v1-FREEZE | **PARTIAL** | §3–§4 stale vs SEO acceptance (BCP-009, BCP-010); §5–§11 correct |
| WEBSITE-FACTORY-NEXT-PRIORITIES-v1 | **YES** | Design Mapping QUEUED; SEO v2 ACCEPTED; aligns with operator charter |

**Freeze vs roadmap:** NEXT-PRIORITIES and FREEZE §6 ACTIVE workstream agree — **Design System Mapping NEXT**. Freeze maturity table is the **only** material contradiction.

---

## Task 6 — Supersession audit

| Document | Should be legacy? | Superseded notice? |
|----------|-------------------|-------------------|
| registry/SITE-TYPE-SEO-MAPPING-v1 | Historical hints | **YES** — banner present |
| registry/SITE-TYPE-BLOCK-MAPPING-v1 | Historical roles | **NO** — BCP-001 |
| registry/SITE-TYPE-LEGAL-MAPPING-v1 | Historical | **PARTIAL** — noted in legal pack only |
| WEBSITE-FACTORY-FOUNDATION-CHECKPOINT-v1 | Historical snapshot | **NO** — BCP-012 |
| projects/mars-website-factory/*-v0 | Legacy external | Documented in implementation rules — discipline only |
| seo-architecture/ (v2 layer) | Current SEO canonical | N/A |

---

## Task 8 — Architecture health summary

| Category | Verdict | Rationale |
|----------|---------|-----------|
| **Layer Consistency** | **PASS WITH WARNINGS** | Core chain intact; stale registry/blueprint pointers |
| **Naming Consistency** | **PASS WITH WARNINGS** | STICKY_CTA, VIDEO, v0/v1 vocabulary |
| **Registry Consistency** | **PASS WITH WARNINGS** | Canonical block-registry accepted; registry folder indexes lag |
| **Matrix Consistency** | **PASS** | Core 5 aligned across page/block/validation/SEO matrices |
| **Cross-Link Consistency** | **PASS WITH WARNINGS** | Broken snapshot link; blueprint SEO sources v1 |
| **Documentation Hygiene** | **PASS WITH WARNINGS** | FREEZE table stale; checkpoint unmarked historical |

**Overall:** **PASS WITH WARNINGS**

---

## Task 9 — Design Mapping readiness

**Answer: YES WITH WARNINGS**

Design System Mapping **may begin** under current operator charter. Core 5 matrices and `block_id` vocabulary are stable enough to map tokens/components.

### Warnings (non-blocking but should be tracked in Mapping charter)

1. **BCP-006** — Resolve `STICKY_CTA` → `CTA` in page contracts before locking component IDs.
2. **BCP-007** — Decide fate of `VIDEO` (embed pattern vs new block_id).
3. **BCP-008** — HEADER_NAV / FILTERS / SEARCH are **not** `block_id`; map as layout/chrome or defer.
4. **BCP-001–005** — Operators should use **block-registry/** and **seo-architecture/** as canonical, not registry v1 mapping files.
5. **BCP-020** — Publish blueprint role → `block_id` mapping aid for designers.

### Would block Mapping (none found)

- No CRITICAL matrix contradictions across Core 5.
- Legal Pack FROZEN — Design Mapping must not expand legal architecture (expected).
- No missing Core 5 blueprint or page architecture system doc.

---

## Task 10 — Roadmap

**No update required** to [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md) — priorities already state Design System Mapping **QUEUED / NEXT** and SEO v2 **ACCEPTED**.

**Follow-up:** [HYGIENE-PASS-v1.md](HYGIENE-PASS-v1.md) (2026-06-01) closed BCP-001–005, BCP-009–010, BCP-012–014 documentation patches. Residual OPEN items: BCP-006/007 (page layer), BCP-019 (external v0), BCP-020 (design cheat sheet).

---

## Validation (charter compliance)

| Rule | Compliant? |
|------|------------|
| No new systems | **YES** |
| No new layers | **YES** |
| No runtime | **YES** |
| No automation | **YES** |
| No Design Mapping artefacts | **YES** |
| No SEO expansion | **YES** |
| No Website Factory scope expansion | **YES** |
| No commit / push | **YES** (audit artefact only) |

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Whether `_snapshots/snap-20260530-*` ever existed outside this repo clone | **UNKNOWN** — path missing locally (BCP-013) |
| Operator schedule for documentation hygiene sprint (BCP-001–013) | **not scheduled** |
| Triumph production deploy authorization | **UNKNOWN** (unchanged from foundation docs) |
| Automated matrix/validator implementation | **FUTURE** — no in-repo proof |
| Whether Design Mapping will charter HEADER_NAV as block_id v1.1 | **requires charter** |

---

*Brain Consistency Pass v1 — 2026-06-01. Documentation audit only. Canonical location: `workspaces/website-factory-reference-v1/BRAIN-CONSISTENCY-PASS-v1.md`.*
