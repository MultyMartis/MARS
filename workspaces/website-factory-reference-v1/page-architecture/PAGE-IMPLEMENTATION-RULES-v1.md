# Website Factory — Page Implementation Rules v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/page-architecture/`  
**Статус:** канонические правила использования Page Architecture layer — **documentation only**  
**Не является:** runtime enforcement, CI gate, page generator

**Связь:** [PAGE-ARCHITECTURE-SYSTEM-v1.md](PAGE-ARCHITECTURE-SYSTEM-v1.md), [BLUEPRINT-IMPLEMENTATION-RULES-v1.md](../blueprints/BLUEPRINT-IMPLEMENTATION-RULES-v1.md), [BLOCK-IMPLEMENTATION-RULES-v1.md](../block-registry/BLOCK-IMPLEMENTATION-RULES-v1.md), [../frontend-rules/WF-GRID-DISCIPLINE-v1.md](../frontend-rules/WF-GRID-DISCIPLINE-v1.md), [../frontend-rules/WF-LAYOUT-DISCIPLINE-v1.md](../frontend-rules/WF-LAYOUT-DISCIPLINE-v1.md)

---

## Production chain (mandatory order)

Website Factory **обязан** следовать цепочке:

```
Site Type          (SITE-TYPE-REGISTRY-v1)
        ↓
Blueprint          (canonical {TYPE}-BLUEPRINT-v1)
        ↓
Page Architecture  (page-architecture/ — this layer)
        ↓
Blocks             (block_id per page — BLOCK-REGISTRY-v1)
        ↓
Design             (tokens / components — FUTURE mapping)
        ↓
Frontend           (partials / project build)
```

**Критическое правило v1:** **No page may be generated before page architecture exists.**

«Generated» = Design scope, Frontend assembly, or production HTML for a route — **не** относится к Legal Pack Markdown generation, которая следует Legal workflow, но legal **routes** всё равно требуют `LEGAL_PAGE` contract перед Frontend shell attach.

---

## Gate rules

| Stage | Prerequisite | Page Architecture role |
|-------|--------------|------------------------|
| **Site Type** | `site_type_code` classified | Defines page type universe via matrix |
| **Blueprint** | Canonical Blueprint loaded | Supplies `required_pages` roles |
| **Page Architecture** | Matrix + per-route Page Contract | **Blocks cannot be selected before this** |
| **Blocks** | `required_blocks` per page frozen | MATRIX v2 + page `forbidden_blocks` |
| **Design** | Block list per page frozen | Map blocks → components (**FUTURE**) |
| **Frontend** | Design scope known | Assemble sections per page contract |

---

## Page architecture workflow

| Step | Action |
|------|--------|
| 1 | Confirm `site_type_code` — Core only for default Factory production |
| 2 | Load Blueprint from `blueprints/{TYPE}-BLUEPRINT-v1.md` |
| 3 | Open [SITE-TYPE-PAGE-MATRIX-v1.md](SITE-TYPE-PAGE-MATRIX-v1.md) — list REQUIRED / OPTIONAL / FORBIDDEN page types |
| 4 | Map Blueprint `required_pages` → `page_type` ([PAGE-TYPE-REGISTRY-v1.md](PAGE-TYPE-REGISTRY-v1.md)) |
| 5 | For each production URL, instantiate [PAGE-CONTRACT-v1.md](PAGE-CONTRACT-v1.md) fields |
| 6 | Apply block stack from [CORE-PAGE-ARCHITECTURES-v1.md](CORE-PAGE-ARCHITECTURES-v1.md) |
| 7 | Verify [PAGE-DEPENDENCY-RULES-v1.md](PAGE-DEPENDENCY-RULES-v1.md) |
| 8 | `LEGAL_PAGE` → [LEGAL-PAGE-CONTRACT-v1.md](LEGAL-PAGE-CONTRACT-v1.md) + Legal Pack gate |
| 9 | Freeze page contract list in project IA |
| 10 | **Then** select/confirm blocks per page ([BLOCK-IMPLEMENTATION-RULES-v1.md](../block-registry/BLOCK-IMPLEMENTATION-RULES-v1.md)) |
| 11 | Freeze block list → Design → Frontend |

---

## Blueprint ↔ Page Architecture alignment

| Source | Authority |
|--------|-----------|
| Blueprint `required_pages` | Which routes must exist |
| SITE-TYPE-PAGE-MATRIX-v1 | Which `page_type` allowed per site type |
| CORE-PAGE-ARCHITECTURES-v1 | Default block stacks per `page_type` |
| PAGE-CONTRACT (project) | Per-URL overrides (optional blocks, canonical_url) |
| BLOCK-REGISTRY + MATRIX v2 | `block_id` validity |

**Conflict resolution:** Matrix FORBIDDEN page types and Blueprint `exclusions` **override** project requests. Reclassification + HITL to proceed.

---

## CORPORATE hybrid rules

| Route group | Page architecture source |
|-------------|--------------------------|
| Marketing routes | CORPORATE matrix + CORPORATE Blueprint |
| Catalog subtree | Inherit CATALOG page types + [CATALOG-BLUEPRINT-v1.md](../blueprints/CATALOG-BLUEPRINT-v1.md) |
| Ecommerce subtree | Inherit ECOMMERCE page types + [ECOMMERCE-BLUEPRINT-v1.md](../blueprints/ECOMMERCE-BLUEPRINT-v1.md) |

Document subtree boundary in project IA **before** block freeze.

---

## Halt conditions

| Condition | Action |
|-----------|--------|
| Frontend work without page contract for route | **Halt** — drift risk |
| Block selected before page contract | **Halt** — update BLOCK flow: Page Architecture precedes block selection |
| FORBIDDEN `page_type` in IA | **Halt** — reclassify site type |
| `LEGAL_PAGE` without LEGAL-PAGE-CONTRACT | **Halt** |
| Design generation before page+block freeze | **Halt** (per Blueprint rules) |

---

## Updates to downstream docs (reference)

Block Implementation Rules v1 state «Required Pages (Blueprint)» before blocks. **Authoritative order after Page Architecture v1:**

`Blueprint required_pages` → **Page Contract per URL** → **blocks per page**.

Operators should apply PAGE-IMPLEMENTATION-RULES as superseding sequencing detail; Block Registry narrative update — **FUTURE** consistency pass (brain polishing).

---

## SAFE UNKNOWN

- CI enforcement of page contract completeness — **FUTURE**
- Single project IA template file format — **not standardized** in v1

---

*Page Implementation Rules version: v1.*
