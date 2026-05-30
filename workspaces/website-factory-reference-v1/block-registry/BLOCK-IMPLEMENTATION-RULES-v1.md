# Website Factory — Block Implementation Rules v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/block-registry/`  
**Статус:** канонические правила использования Block Registry  
**Не является:** runtime enforcement, CI gate, block generator, design tool

**Связь:** [../blueprints/BLUEPRINT-IMPLEMENTATION-RULES-v1.md](../blueprints/BLUEPRINT-IMPLEMENTATION-RULES-v1.md), [BLOCK-REGISTRY-v1.md](BLOCK-REGISTRY-v1.md)

---

## Production chain (mandatory order)

Website Factory **обязан** следовать цепочке:

```
Site Type (SITE-TYPE-REGISTRY-v1)
        ↓
Blueprint (canonical per site_type_code)
        ↓
Required Pages (Blueprint required_pages)
        ↓
Required Blocks (SITE-TYPE-BLOCK-MATRIX-v2 + Blueprint)
        ↓
Optional Blocks (Blueprint allow-list + project IA)
        ↓
Design (tokens / components — per complexity)
        ↓
Frontend (reference partials + project build)
```

**Критическое правило:** Blocks **cannot be selected before Blueprint**.

Выбор `block_id` до фиксации Blueprint = **drift risk**; operator **должен** halt.

---

## Gate rules

| Stage | Prerequisite | Block Registry role |
|-------|--------------|---------------------|
| **Site Type** | Project classified | Defines allowed block universe |
| **Blueprint** | Canonical Blueprint loaded | Defines pages + block stacks |
| **Pages** | `required_pages` listed | Blocks attach to pages |
| **Required Blocks** | Matrix v2 REQUIRED satisfied | No FORBIDDEN blocks |
| **Optional Blocks** | Subset from OPTIONAL cells | Document in project IA |
| **Design** | Block list frozen | Map blocks → visual components |
| **Frontend** | Design scope known | Map blocks → partials/sections |

---

## Block selection workflow

| Step | Action |
|------|--------|
| 1 | Confirm `site_type_code` — Core only for default Factory production |
| 2 | Load Blueprint from `blueprints/{TYPE}-BLUEPRINT-v1.md` |
| 3 | List `required_pages` in project IA |
| 4 | For each page, load REQUIRED blocks from Blueprint + [SITE-TYPE-BLOCK-MATRIX-v2.md](SITE-TYPE-BLOCK-MATRIX-v2.md) |
| 5 | Select OPTIONAL blocks from matrix OPTIONAL cells only |
| 6 | Verify no FORBIDDEN blocks — [BLOCK-DEPENDENCY-RULES-v1.md](BLOCK-DEPENDENCY-RULES-v1.md) |
| 7 | Verify legal dependencies — Consent Rule on forms; Legal Pack for `LEGAL_LINKS` |
| 8 | Freeze block list before Design |
| 9 | Map to reference partials where exist — [CORE-BLOCK-LIBRARY-v1.md](CORE-BLOCK-LIBRARY-v1.md) |
| 10 | Frontend assembly — no scope creep (e.g. no CART on CATALOG) |

---

## Blueprint ↔ Registry alignment

| Source | Authority |
|--------|-----------|
| Blueprint `required_blocks` | Page-level block stacks |
| Blueprint `exclusions` | Hard forbidden features |
| SITE-TYPE-BLOCK-MATRIX-v2 | Site-type compatibility per `block_id` |
| BLOCK-REGISTRY-v1 | Canonical `block_id` definitions |
| SITE-TYPE-BLOCK-MAPPING-v1 | **Legacy** — use for narrative; `block_id` from v1 registry |

**Conflict resolution:** Blueprint exclusions and matrix FORBIDDEN **override** optional project requests. Reclassification + HITL required to proceed.

---

## CORPORATE hybrid rules

| Rule | Description |
|------|-------------|
| **Primary matrix** | CORPORATE row for marketing routes |
| **Catalog subtree** | Apply CATALOG matrix blocks on catalog routes |
| **Ecommerce subtree** | Apply ECOMMERCE matrix blocks on shop routes |
| **Document per route group** | Project IA lists Blueprint ID + block set per subtree |

---

## Design & Frontend boundaries

| Rule | Description |
|------|-------------|
| **No design before blocks** | Visual work starts after block list freeze |
| **No frontend before design scope** | Section partials implement frozen blocks |
| **Reference workspace** | LANDING golden pattern — partial mapping in CORE-BLOCK-LIBRARY |
| **Legal independent** | Legal pages from Legal Pack v1 FROZEN — not from Block Registry |
| **No SEO content here** | SEO after Blueprint; blocks inform IA only |

---

## Explicit non-goals (v1)

| Non-goal | Status |
|----------|--------|
| Automatic block assembly | **Not claimed** |
| Block-driven legal HTML | **Forbidden** |
| Block-driven SEO copy | **Not in scope** |
| Runtime block validation | **Not implemented** |
| Extended Type blocks (SAAS, WEB_APP, MARKETPLACE) | **Not in Core Library v1** |

---

## Operator checklist

Before Design / Frontend:

- [ ] `site_type_code` from closed Registry list (Core)
- [ ] Canonical Blueprint referenced in project doc
- [ ] All `required_pages` listed
- [ ] REQUIRED blocks from matrix v2 on correct pages
- [ ] OPTIONAL blocks documented — no FORBIDDEN blocks
- [ ] Dependencies satisfied — [BLOCK-DEPENDENCY-RULES-v1.md](BLOCK-DEPENDENCY-RULES-v1.md)
- [ ] Consent Rule planned for all `LEAD_FORM` / `CHECKOUT` instances
- [ ] Legal Pack v1 alignment for `LEGAL_LINKS` / `FOOTER`
- [ ] Hybrid subtrees documented (if CORPORATE)
- [ ] Gaps reviewed — [BLOCK-GAPS-v1.md](BLOCK-GAPS-v1.md)

---

## SAFE UNKNOWN

- CI gate: Blueprint + Block freeze before branch — **not implemented**
- Registry v1 → v2 migration policy — **FUTURE**

---

*Implementation rules version: v1.*
