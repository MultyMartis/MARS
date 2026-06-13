# Website Factory — Generation Inputs v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/generation-contracts/`  
**Статус:** input catalogue — **architecture only, no project data**  
**Связь:** [GENERATION-CONTRACT-v1.md](GENERATION-CONTRACT-v1.md), [GENERATION-SYSTEM-v1.md](GENERATION-SYSTEM-v1.md)

**Не является:** sample project payloads, filled generation manifests, database schema.

---

## 1. Назначение

Каталог **обязательных и условных** inputs для Production Generation Layer. Каждый input — **тип артефакта** и **источник в accepted foundation**, не конкретные значения проекта.

---

## 2. Input catalogue

### IN-01 — `site_type_code`

| Attribute | Value |
|-----------|-------|
| **Type** | Registry classification code |
| **Source** | [registry/SITE-TYPE-REGISTRY-v1.md](../registry/SITE-TYPE-REGISTRY-v1.md) |
| **Required** | Always |
| **Use** | Blueprint selection, all matrices |

---

### IN-02 — `project_brief`

| Attribute | Value |
|-----------|-------|
| **Type** | Human-readable charter (goals, audience, constraints) |
| **Source** | Operator / project workspace (not canon) |
| **Required** | Always |
| **Use** | Scope decisions, optional block picks, HITL context |
| **Rule** | Brief **cannot** override blueprint exclusions |

---

### IN-03 — `entity_card`

| Attribute | Value |
|-----------|-------|
| **Type** | Legal entity identity record |
| **Source** | [legal-entity/](../legal-entity/) discovery outputs |
| **Required** | When forms, PII, or legal identity on site |
| **Use** | NAP signals, FOOTER/CONTACTS, legal disclosures |

---

### IN-04 — `blueprint`

| Attribute | Value |
|-----------|-------|
| **Type** | Canonical blueprint instance |
| **Source** | [blueprints/{TYPE}-BLUEPRINT-v1.md](../blueprints/) |
| **Required** | Always (Core 5) |
| **Fields consumed** | `required_pages`, `required_blocks`, `exclusions`, `seo_requirements` |
| **Ref format** | `blueprint_ref` e.g. `LANDING-BLUEPRINT-v1` |

---

### IN-05 — `page_contracts`

| Attribute | Value |
|-----------|-------|
| **Type** | Per-route page architecture bindings |
| **Source** | [page-architecture/PAGE-CONTRACT-v1.md](../page-architecture/PAGE-CONTRACT-v1.md), CORE-PAGE-ARCHITECTURES |
| **Required** | All routes in `generation_scope` |
| **Use** | Page Build Specification, validation target |

---

### IN-06 — `block_mapping`

| Attribute | Value |
|-----------|-------|
| **Type** | Resolved `block_id` stacks per `page_type` |
| **Source** | [block-registry/PAGE-BLOCK-MAPPING-v1.md](../block-registry/PAGE-BLOCK-MAPPING-v1.md), BLUEPRINT-BLOCK-MAPPING |
| **Required** | All pages in scope |
| **Use** | Block Stack Specification |

---

### IN-07 — `page_block_validation_results`

| Attribute | Value |
|-----------|-------|
| **Type** | VALIDATION-CONTRACT compatible runs |
| **Source** | [page-block-validation/](../page-block-validation/) operator records |
| **Required** | All pages in scope before Content/Generation Ready |
| **Use** | GATE_BLOCK_VALIDATION_PASS evidence |

---

### IN-08 — `seo_profile`

| Attribute | Value |
|-----------|-------|
| **Type** | Strategy + per-page SEO contract set |
| **Source** | [seo-architecture/](../seo-architecture/) |
| **Required** | All marketing/commerce pages in scope |
| **Use** | SEO Specification output |

---

### IN-09 — `design_mapping`

| Attribute | Value |
|-----------|-------|
| **Type** | `VF_*` pattern bindings per block/page |
| **Source** | [design-system/](../design-system/) |
| **Required** | All blocks with REQUIRED stance in scope |
| **Use** | Design Specification output |

---

### IN-10 — `content_contracts`

| Attribute | Value |
|-----------|-------|
| **Type** | Signal requirements per block/page |
| **Source** | [content-contracts/](../content-contracts/) |
| **Required** | All in-scope blocks with content binding |
| **Use** | Content Specification output |

---

### IN-11 — `content_validation_results`

| Attribute | Value |
|-----------|-------|
| **Type** | CONTENT-VALIDATION-CONTRACT compatible runs |
| **Source** | [content-validation/](../content-validation/) |
| **Required** | Same scope as content contracts |
| **Use** | GATE_CONTENT_VALIDATION_PASS evidence |

---

### IN-12 — `legal_pack_ref`

| Attribute | Value |
|-----------|-------|
| **Type** | Frozen Legal Pack version + route mapping |
| **Source** | [legal/LEGAL-PACK-v1-FREEZE.md](../legal/LEGAL-PACK-v1-FREEZE.md), SITE-TYPE-LEGAL-MAPPING |
| **Required** | Full-site and form-bearing scopes |
| **Use** | Legal gate, LEGAL_PAGE specs |

---

### IN-13 — `validation_results` (aggregate)

| Attribute | Value |
|-----------|-------|
| **Type** | Summary of all validation runs in scope |
| **Source** | IN-07 + IN-11 |
| **Required** | Before Generation Ready |
| **Use** | Gate evidence bundle |

---

### IN-14 — `site_type_matrices` (read-only refs)

| Attribute | Value |
|-----------|-------|
| **Type** | Registry matrices (block, SEO, legal hints) |
| **Source** | [registry/](../registry/) |
| **Required** | Implicit via classification |
| **Use** | Cross-check only; superseded by layer-specific v2 docs where marked |

---

## 3. Input readiness states

| State | Meaning |
|-------|---------|
| `MISSING` | Not started |
| `DRAFT` | In progress, not gate-eligible |
| `READY` | Satisfies gate inputs |
| `STALE` | Upstream changed after READY — requires re-gate |

---

## 4. Input dependency matrix

| Input | Depends on |
|-------|------------|
| `page_contracts` | `blueprint`, `site_type_code` |
| `block_mapping` | `page_contracts` |
| `page_block_validation_results` | `block_mapping` |
| `seo_profile` | `blueprint`, `page_contracts` |
| `design_mapping` | `block_mapping`, validation PASS |
| `content_contracts` | `design_mapping`, `seo_profile`, validation PASS |
| `content_validation_results` | `content_contracts` |
| `legal_pack_ref` | `site_type_code`, scope |
| `entity_card` | legal-entity discovery (parallel early) |

---

## 5. Explicit non-inputs (v1)

| Item | Reason |
|------|--------|
| Prompts / LLM configs | Generation Gaps |
| Generated copy / meta text | Content generation gap |
| Source code trees | Frontend gap |
| Figma files | Design tooling gap |
| MIG request JSON | Integration gap |
| API keys, deploy targets | Runtime gap |

---

*Generation Inputs version: v1.*
