# Website Factory — Generation Outputs v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/generation-contracts/`  
**Статус:** output definitions — **no implementation**  
**Связь:** [GENERATION-CONTRACT-v1.md](GENERATION-CONTRACT-v1.md), [GENERATION-LIFECYCLE-v1.md](GENERATION-LIFECYCLE-v1.md)

**Не является:** generated HTML/CSS/JS, zip bundles, build artefacts, CMS exports.

---

## 1. Назначение

Generation Outputs v1 определяет **типы спецификаций**, которые Production Generation Layer **собирает** при успешном прохождении lifecycle. Каждый output — **структурное описание** для Frontend Layer; не исполняемый код.

---

## 2. Output catalogue

### OUT-01 — Page Build Specification

| Attribute | Value |
|-----------|-------|
| **Purpose** | Per-route production blueprint for frontend assembly |
| **Contains** | `page_id`, URL slug, `page_type`, PAGE-CONTRACT ref, inclusion in scope, legal flags |
| **Consumes** | `page_contracts`, `blueprint`, `generation_scope` |
| **Does not contain** | HTML structure, component imports, CSS |
| **Handoff to** | Frontend Layer page scaffolding |

---

### OUT-02 — Block Stack Specification

| Attribute | Value |
|-----------|-------|
| **Purpose** | Ordered `block_id` list per page with stance metadata |
| **Contains** | Per page: ordered blocks, REQUIRED/OPTIONAL, OR-group notes, validation ref |
| **Consumes** | `block_mapping`, `page_block_validation_results` |
| **Does not contain** | Partial file paths, framework components |
| **Handoff to** | Frontend section assembly |

---

### OUT-03 — SEO Specification

| Attribute | Value |
|-----------|-------|
| **Purpose** | Architecture-level SEO bindings per page |
| **Contains** | Strategy ref, search intent role, PAGE-SEO-CONTRACT fields (architecture slots, not generated meta text) |
| **Consumes** | `seo_profile` |
| **Does not contain** | Keyword lists, generated titles/descriptions, rank guarantees |
| **Handoff to** | Frontend meta slot binding + future SEO text workstream |

---

### OUT-04 — Design Specification

| Attribute | Value |
|-----------|-------|
| **Purpose** | Visual pattern bindings per block |
| **Contains** | `block_id` → `VF_*` pattern ref, page-level overrides, forbidden pattern notes |
| **Consumes** | `design_mapping` |
| **Does not contain** | Colors, typography tokens, CSS, Figma node IDs |
| **Handoff to** | Frontend layout role selection |

---

### OUT-05 — Content Specification

| Attribute | Value |
|-----------|-------|
| **Purpose** | Content signal slots per block/page |
| **Contains** | `signal_id` requirements, forbidden signals, validation ref |
| **Consumes** | `content_contracts`, `content_validation_results` |
| **Does not contain** | Marketing copy, FAQs text, legal prose body |
| **Handoff to** | Frontend slot placeholders + future copy fill |

---

### OUT-06 — Frontend Handoff Package

| Attribute | Value |
|-----------|-------|
| **Purpose** | Single bundle pointer set for Frontend workstream |
| **Contains** | `generation_id`, `site_type_code`, `generation_scope`, refs to OUT-01–OUT-05, gate register snapshot, operator sign-off |
| **Consumes** | All specifications + GENERATION-CONTRACT `READY` |
| **Does not contain** | Build commands, repo branches, deploy config |
| **Handoff to** | Frontend Layer (GL-13) |

---

## 3. Output assembly order (GL-12)

```text
Page Build Specification (OUT-01)
    + Block Stack Specification (OUT-02)
    + SEO Specification (OUT-03)
    + Design Specification (OUT-04)
    + Content Specification (OUT-05)
    → Frontend Handoff Package (OUT-06)
```

**Rule:** OUT-06 **invalid** if any component spec missing for in-scope routes.

---

## 4. Output completeness checklist

| Check | Rule |
|-------|------|
| Route coverage | Every route in `generation_scope.included_routes` has OUT-01 row |
| Block coverage | Every REQUIRED block on route appears in OUT-02 |
| SEO coverage | Non-LEGAL marketing pages have OUT-03 row |
| Design coverage | Every block in OUT-02 with content binding has OUT-04 `VF_*` |
| Content coverage | Every block in OUT-02 with REQUIRED content has OUT-05 signals |
| Gate snapshot | OUT-06 lists all PASS gates |

---

## 5. Versioning

| Field | Rule |
|-------|------|
| `spec_version` | `generation-spec-v1` for this workstream |
| `upstream_pins` | Copy `required_dependencies` from GENERATION-CONTRACT |
| Change control | New upstream acceptance → new `generation_id` or documented re-gate |

---

## 6. Explicit non-outputs

| Item | Registered in |
|------|----------------|
| Compiled frontend | GENERATION-GAPS (Frontend generation) |
| Legal HTML files | Legal workflow (separate from generation specs) |
| AI-generated copy | GENERATION-GAPS (Content generation) |
| Lighthouse reports | GENERATION-GAPS (Production QA) |
| Deploy manifests | Runtime gap |

---

*Generation Outputs version: v1.*
