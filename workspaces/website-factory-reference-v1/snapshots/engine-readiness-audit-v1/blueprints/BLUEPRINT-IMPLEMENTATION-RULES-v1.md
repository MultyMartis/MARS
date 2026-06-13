# Website Factory — Blueprint Implementation Rules v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/blueprints/`  
**Статус:** канонические правила использования Blueprint System  
**Не является:** runtime enforcement, CI gate, orchestration

**Связь:** [BLUEPRINT-SYSTEM-v1.md](BLUEPRINT-SYSTEM-v1.md), [SITE-TYPE-IMPLEMENTATION-RULES-v1.md](../registry/SITE-TYPE-IMPLEMENTATION-RULES-v1.md)

---

## Production chain (mandatory order)

Website Factory **обязан** следовать цепочке:

```
Site Type (Registry)
        ↓
Blueprint (canonical per site_type_code)
        ↓
Pages (required_pages + project optional)
        ↓
Blocks (required_blocks + optional_blocks)
        ↓
Design (tokens / components — per complexity)
        ↓
Frontend (reference patterns + project build)
```

**Правило:** ни один downstream этап **не переопределяет** upstream exclusions без reclassification и HITL.

---

## Blueprint is mandatory before

| Stage | Gate rule |
|-------|-----------|
| **SEO strategy / IA SEO** | Blueprint `required_pages` + `seo_requirements` frozen |
| **Design generation / visual contract** | Blueprint `page_structure` + block stack known |
| **Frontend generation / section assembly** | Blueprint `required_blocks` + `exclusions` frozen |

**Halt condition:** работа над SEO, Design или Frontend **без** выбранного и зафиксированного Blueprint = **drift risk**; operator **должен** halt (см. mars-survivability operational patterns).

---

## Site type selection → Blueprint mapping

| Step | Action |
|------|--------|
| 1 | Classify project → `site_type_code` from [SITE-TYPE-REGISTRY-v1.md](../registry/SITE-TYPE-REGISTRY-v1.md) |
| 2 | Confirm Core vs Extended — Extended **нет Blueprint v1** |
| 3 | Load canonical Blueprint from `blueprints/{TYPE}-BLUEPRINT-v1.md` |
| 4 | Instantiate project IA doc referencing Blueprint ID + version |
| 5 | Add optional blocks from Blueprint allow-list only |
| 6 | Freeze before SEO / Design / Frontend |

### Core Type → Blueprint

| site_type_code | Blueprint file |
|----------------|----------------|
| `LANDING` | [LANDING-BLUEPRINT-v1.md](LANDING-BLUEPRINT-v1.md) |
| `PROMO` | [PROMO-BLUEPRINT-v1.md](PROMO-BLUEPRINT-v1.md) |
| `CATALOG` | [CATALOG-BLUEPRINT-v1.md](CATALOG-BLUEPRINT-v1.md) |
| `ECOMMERCE` | [ECOMMERCE-BLUEPRINT-v1.md](ECOMMERCE-BLUEPRINT-v1.md) |
| `CORPORATE` | [CORPORATE-BLUEPRINT-v1.md](CORPORATE-BLUEPRINT-v1.md) |

---

## Pages implementation

| Rule | Description |
|------|-------------|
| **Required pages** | All `required_pages` from Blueprint **must** exist in production or have documented waiver (HITL) |
| **Legal pages** | Generated per Legal Pack v1 FROZEN — **not** from Blueprint content |
| **URL patterns** | Follow Blueprint + Legal canonical URLs |
| **Optional pages** | Operator selects from Blueprint; document in project IA |
| **Hybrid (CORPORATE)** | Subtree pages inherit child Blueprint `required_pages` for that route group |

---

## Blocks implementation

| Rule | Description |
|------|-------------|
| **Required blocks** | Must appear on specified pages per Blueprint |
| **Optional blocks** | Subset selection documented in project IA |
| **Excluded blocks** | **Forbidden** — triggers reclassification review |
| **Reference partials** | LANDING golden pattern: `workspaces/website-factory-reference-v1/src/partials/sections/` |
| **Block Mapping** | Cross-check [BLUEPRINT-BLOCK-MAPPING-v1.md](../block-registry/BLUEPRINT-BLOCK-MAPPING-v1.md), [BLOCK-REGISTRY-v1.md](../block-registry/BLOCK-REGISTRY-v1.md); role hints: [SITE-TYPE-BLOCK-MAPPING-v1.md](../registry/SITE-TYPE-BLOCK-MAPPING-v1.md) (superseded) |

---

## Design implementation

| Rule | Description |
|------|-------------|
| **After Blueprint freeze** | Design work starts only when page + block list is known |
| **Complexity** | Use [SITE-TYPE-MATRIX-v1.md](../registry/SITE-TYPE-MATRIX-v1.md) for effort estimation |
| **Design System mapping** | **FUTURE** priority — until mapped, use reference workspace tokens for LANDING |
| **Visual contract** | `projects/orca/visual-semantics/contracts/website-factory-visual-contract-v0.md` — alignment **manual** in v1 |

---

## Frontend implementation

| Rule | Description |
|------|-------------|
| **After Design scope** | Section partials map to Blueprint blocks |
| **No scope creep** | Do not add cart to CATALOG frontend without ECOMMERCE reclassification |
| **Legal footer** | [LEGAL-IMPLEMENTATION-RULES.md](../legal/LEGAL-IMPLEMENTATION-RULES.md) — independent of Blueprint generation |
| **QA** | RU landing QA preset for LANDING: `projects/mars-website-factory/ru-landing-qa-preset-v1.md` |

---

## Legal & SEO (downstream of Blueprint)

| Layer | Rule |
|-------|------|
| **Legal** | Blueprint declares requirements; generation uses Legal Pack v1 — **do not modify Legal Pack** |
| **SEO** | Blueprint declares architecture requirements; meta/content generation **separate** and **after** Blueprint |
| **Conversion** | Blueprint `conversion_requirements` inform form/checkout wiring, not copy |

---

## Extended Types — no Blueprint v1

| site_type_code | Rule |
|----------------|------|
| `SAAS` | Architecture charter required; no canonical Blueprint |
| `WEB_APPLICATION` | Not a traditional website; public shell may borrow PROMO/LANDING Blueprint for marketing routes only |
| `MARKETPLACE` | Charter + legal extension; no canonical Blueprint |

---

## Operator checklist

Before SEO / Design / Frontend:

- [ ] `site_type_code` selected from closed Registry list
- [ ] Canonical Blueprint loaded and referenced in project doc
- [ ] All [BLUEPRINT-CONTRACT-v1.md](BLUEPRINT-CONTRACT-v1.md) fields acknowledged
- [ ] `required_pages` and `required_blocks` listed in project IA
- [ ] `exclusions` understood by all contributors
- [ ] Legal mapping v2 reviewed for site type
- [ ] SEO mapping v1 reviewed for site type
- [ ] Hybrid subtrees documented (if CORPORATE)
- [ ] Blueprint gaps reviewed — [BLUEPRINT-GAPS-v1.md](BLUEPRINT-GAPS-v1.md)

---

## Explicit non-goals (v1)

| Non-goal | Status |
|----------|--------|
| Automatic page generation from Blueprint | **Not claimed** |
| Automatic block assembly | **Not claimed** |
| Blueprint-driven legal HTML | **Forbidden** — Legal Pack separate |
| Blueprint-driven SEO content | **Not in scope** |

---

## SAFE UNKNOWN

- CI gate enforcing Blueprint freeze before branch work — **not implemented**
- Blueprint versioning migration (v1 → v2) policy — **FUTURE**

---

*Implementation rules version: v1.*
