# Website Factory — Project State Model v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/runtime-architecture/`  
**Статус:** canonical state model — **documentation only**  
**Связь:** [STATE-TRANSITION-RULES-v1.md](STATE-TRANSITION-RULES-v1.md), [RUNTIME-GATES-v1.md](RUNTIME-GATES-v1.md)

---

## 1. Назначение

Canonical state model — **14 states** (13 progressive + 1 terminal). Каждое состояние: purpose, inputs, outputs, required gate, allowed transitions, forbidden transitions.

**State storage:** not implemented in v1 — states are **declared discipline** for human-operated tracking.

---

## 2. State catalogue summary

| State | Code | Terminal |
|-------|------|----------|
| New Project | `NEW_PROJECT` | No |
| Classified | `CLASSIFIED` | No |
| Blueprint Ready | `BLUEPRINT_READY` | No |
| Page Ready | `PAGE_READY` | No |
| Block Ready | `BLOCK_READY` | No |
| Validated | `VALIDATED` | No |
| SEO Ready | `SEO_READY` | No |
| Design Ready | `DESIGN_READY` | No |
| Content Ready | `CONTENT_READY` | No |
| Content Validated | `CONTENT_VALIDATED` | No |
| Generation Ready | `GENERATION_READY` | No |
| Production QA Ready | `PRODUCTION_QA_READY` | No |
| Frontend Ready | `FRONTEND_READY` | No |
| Complete | `COMPLETE` | **Yes** |

---

## 3. State definitions

### `NEW_PROJECT`

| Attribute | Value |
|-----------|-------|
| **Purpose** | Project exists in Factory scope; intake recorded; no architecture binding yet |
| **Inputs** | Project charter, operator assignment, optional client brief |
| **Outputs** | `project_id` (logical), intake record, scope tier (`FULL_SITE` / partial per charter) |
| **Required gate** | **Intake Complete** — charter + scope documented |
| **Allowed transitions** | → `CLASSIFIED` |
| **Forbidden transitions** | → any state beyond `CLASSIFIED`; → `COMPLETE` |
| **Terminal** | No |

---

### `CLASSIFIED`

| Attribute | Value |
|-----------|-------|
| **Purpose** | `site_type_code` resolved; Registry rules applied |
| **Inputs** | Intake record, [SITE-TYPE-REGISTRY-v1.md](../registry/SITE-TYPE-REGISTRY-v1.md) |
| **Outputs** | `site_type_code`, Core/Extended flag, production tier |
| **Required gate** | **Classification Complete** |
| **Allowed transitions** | → `BLUEPRINT_READY`; rollback → `NEW_PROJECT` |
| **Forbidden transitions** | → `PAGE_READY` or later without `BLUEPRINT_READY` |
| **Terminal** | No |

---

### `BLUEPRINT_READY`

| Attribute | Value |
|-----------|-------|
| **Purpose** | Canonical blueprint selected and frozen for site type |
| **Inputs** | `site_type_code`, [blueprints/](../blueprints/) |
| **Outputs** | `blueprint_ref`, IA intent, site-level block intent |
| **Required gate** | **Blueprint Approved** (operator) |
| **Allowed transitions** | → `PAGE_READY`; rollback → `CLASSIFIED` |
| **Forbidden transitions** | → `BLOCK_READY` or later without `PAGE_READY` |
| **Terminal** | No |

---

### `PAGE_READY`

| Attribute | Value |
|-----------|-------|
| **Purpose** | Page contracts instantiated for all in-scope routes |
| **Inputs** | Blueprint, [page-architecture/](../page-architecture/) |
| **Outputs** | `page_type` set per route, PAGE-CONTRACT refs |
| **Required gate** | **Page Architecture Approved** (operator) |
| **Allowed transitions** | → `BLOCK_READY`; rollback → `BLUEPRINT_READY` |
| **Forbidden transitions** | → `VALIDATED` without `BLOCK_READY` |
| **Terminal** | No |

---

### `BLOCK_READY`

| Attribute | Value |
|-----------|-------|
| **Purpose** | Block stacks mapped to pages via canonical `block_id` |
| **Inputs** | Page contracts, [block-registry/](../block-registry/) PAGE-BLOCK-MAPPING |
| **Outputs** | Resolved block stacks per page, mapping audit note |
| **Required gate** | **Block Mapping Complete** |
| **Allowed transitions** | → `VALIDATED`; rollback → `PAGE_READY` |
| **Forbidden transitions** | → `SEO_READY` or later without `VALIDATED` |
| **Terminal** | No |

---

### `VALIDATED`

| Attribute | Value |
|-----------|-------|
| **Purpose** | Page → block semantic validation recorded PASS |
| **Inputs** | Block stacks, [page-block-validation/](../page-block-validation/) |
| **Outputs** | Validation run record (PASS), severity log if warnings |
| **Required gate** | **Validation Pass** — no FAIL/CRITICAL |
| **Allowed transitions** | → `SEO_READY`; rollback → `BLOCK_READY` |
| **Forbidden transitions** | → `SEO_READY` while FAIL/CRITICAL open; → `DESIGN_READY` skip |
| **Terminal** | No |

---

### `SEO_READY`

| Attribute | Value |
|-----------|-------|
| **Purpose** | SEO architecture applied for all in-scope pages |
| **Inputs** | Validated architecture, [seo-architecture/](../seo-architecture/) |
| **Outputs** | SEO strategy ref, PAGE-SEO-CONTRACT per page |
| **Required gate** | **SEO Approved** (operator) |
| **Allowed transitions** | → `DESIGN_READY`; rollback → `VALIDATED` |
| **Forbidden transitions** | → `SEO_READY` from pre-`VALIDATED`; → `CONTENT_READY` skip |
| **Terminal** | No |

---

### `DESIGN_READY`

| Attribute | Value |
|-----------|-------|
| **Purpose** | Visual pattern families bound to blocks/pages |
| **Inputs** | SEO-ready architecture, [design-system/](../design-system/) |
| **Outputs** | `VF_*` bindings per required block/page |
| **Required gate** | **Design Approved** (operator) |
| **Allowed transitions** | → `CONTENT_READY`; rollback → `SEO_READY` |
| **Forbidden transitions** | → `CONTENT_READY` before `DESIGN_READY`; → `DESIGN_READY` before `VALIDATED` |
| **Terminal** | No |

---

### `CONTENT_READY`

| Attribute | Value |
|-----------|-------|
| **Purpose** | Content signals bound per Content Contracts |
| **Inputs** | Design-ready architecture, [content-contracts/](../content-contracts/) |
| **Outputs** | Signal bindings per block/page (`signal_id` refs) |
| **Required gate** | **Content Approved** (operator) |
| **Allowed transitions** | → `CONTENT_VALIDATED`; rollback → `DESIGN_READY` |
| **Forbidden transitions** | → `CONTENT_VALIDATED` before content binding complete |
| **Terminal** | No |

---

### `CONTENT_VALIDATED`

| Attribute | Value |
|-----------|-------|
| **Purpose** | Content signal architecture validation PASS |
| **Inputs** | Content bindings, [content-validation/](../content-validation/) |
| **Outputs** | Content validation run (PASS) |
| **Required gate** | **Content Validation Pass** |
| **Allowed transitions** | → `GENERATION_READY`; rollback → `CONTENT_READY` |
| **Forbidden transitions** | → `GENERATION_READY` on FAIL/CRITICAL |
| **Terminal** | No |

---

### `GENERATION_READY`

| Attribute | Value |
|-----------|-------|
| **Purpose** | All upstream gates satisfied; Legal gates PASS; scope frozen for generation package |
| **Inputs** | All prior outputs, Legal Pack, [generation-contracts/](../generation-contracts/) |
| **Outputs** | `generation_id`, GENERATION-CONTRACT READY marker, spec assembly started |
| **Required gate** | **Generation Ready** (operator + Legal Complete when required) |
| **Allowed transitions** | → `PRODUCTION_QA_READY`; rollback → `CONTENT_VALIDATED` (charter) |
| **Forbidden transitions** | → `FRONTEND_READY` skip Production QA |
| **Terminal** | No |

---

### `PRODUCTION_QA_READY`

| Attribute | Value |
|-----------|-------|
| **Purpose** | Global Production QA architectural review PASS |
| **Inputs** | Generation package, all layer artefacts, [production-qa/](../production-qa/) |
| **Outputs** | Production QA run (PASS), checklist completion |
| **Required gate** | **Production QA Pass** |
| **Allowed transitions** | → `FRONTEND_READY`; rollback → `GENERATION_READY` |
| **Forbidden transitions** | → `FRONTEND_READY` on Production QA FAIL |
| **Terminal** | No |

---

### `FRONTEND_READY`

| Attribute | Value |
|-----------|-------|
| **Purpose** | Frontend Handoff package delivered and acknowledged |
| **Inputs** | [GENERATION-OUTPUTS-v1.md](../generation-contracts/GENERATION-OUTPUTS-v1.md) handoff bundle |
| **Outputs** | Handoff ack record, Frontend workstream ownership transfer |
| **Required gate** | **Frontend Handoff Approved** (operator) |
| **Allowed transitions** | → `COMPLETE`; rollback → `PRODUCTION_QA_READY` |
| **Forbidden transitions** | → `COMPLETE` without Handoff Approved |
| **Terminal** | No |

---

### `COMPLETE`

| Attribute | Value |
|-----------|-------|
| **Purpose** | Website Factory architecture track closed for project |
| **Inputs** | `FRONTEND_READY`, operator closure sign-off |
| **Outputs** | Closure record; no further Factory state advances |
| **Required gate** | **Project Complete** (operator) |
| **Allowed transitions** | **None** |
| **Forbidden transitions** | Any outbound transition |
| **Terminal** | **Yes** |

---

## 4. State diagram (simplified)

```text
NEW_PROJECT → CLASSIFIED → BLUEPRINT_READY → PAGE_READY → BLOCK_READY
    → VALIDATED → SEO_READY → DESIGN_READY → CONTENT_READY
    → CONTENT_VALIDATED → GENERATION_READY → PRODUCTION_QA_READY
    → FRONTEND_READY → COMPLETE
```

---

*Project State Model v1 — 2026-06-01.*
