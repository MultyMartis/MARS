# Website Factory — Generation Gates v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/generation-contracts/`  
**Статус:** formal production gates — **documentation only**  
**Связь:** [GENERATION-LIFECYCLE-v1.md](GENERATION-LIFECYCLE-v1.md), [GENERATION-CONTRACT-v1.md](GENERATION-CONTRACT-v1.md)

**Не является:** CI job definitions, automated policy engine, deploy approval system.

---

## 1. Назначение

Generation Gates v1 — **формальные контрольные точки** production pipeline. Каждый gate: **purpose**, **inputs**, **pass criteria**, **failure condition**.

**Minimum gate set** (required in every `FULL_SITE` generation contract):

1. `GATE_BLUEPRINT_APPROVED`
2. `GATE_PAGE_ARCHITECTURE_APPROVED`
3. `GATE_BLOCK_VALIDATION_PASS`
4. `GATE_SEO_APPROVED`
5. `GATE_DESIGN_APPROVED`
6. `GATE_CONTENT_APPROVED`
7. `GATE_CONTENT_VALIDATION_PASS`
8. `GATE_LEGAL_PACK_PASS`
9. `GATE_ENTITY_CARD_READY` (conditional)
10. `GATE_GENERATION_READY`

---

## 2. Gate catalogue

### GATE_BLUEPRINT_APPROVED

| Attribute | Value |
|-----------|-------|
| **Purpose** | IA skeleton and block intent frozen per `site_type_code` |
| **Inputs** | `site_type_code`, canonical blueprint doc, project charter |
| **Pass** | `blueprint_ref` matches Core canonical; exclusions documented; operator sign-off |
| **Failure** | Missing blueprint; wrong type; exclusions violated without reclassification |

---

### GATE_PAGE_ARCHITECTURE_APPROVED

| Attribute | Value |
|-----------|-------|
| **Purpose** | All production routes have valid `page_type` and PAGE-CONTRACT |
| **Inputs** | Blueprint `required_pages`, PAGE-TYPE-REGISTRY, instantiated page contracts |
| **Pass** | Every required route mapped; LEGAL_PAGE contracts when applicable |
| **Failure** | Missing page contract; orphan route; illegal `page_type` |

---

### GATE_BLOCK_VALIDATION_PASS

| Attribute | Value |
|-----------|-------|
| **Purpose** | Block stacks satisfy PAGE-BLOCK-MAPPING and blueprint context |
| **Inputs** | VALIDATION-CONTRACT runs per page in scope, BLOCK-REGISTRY refs |
| **Pass** | All in-scope pages: `status` = `PASS` or `PASS_WITH_WARNINGS` (no CRITICAL) |
| **Failure** | `FAIL`; missing required blocks; FORBIDDEN blocks present |

---

### GATE_SEO_APPROVED

| Attribute | Value |
|-----------|-------|
| **Purpose** | SEO architecture applied — intent, strategy, page SEO roles |
| **Inputs** | SEO-STRATEGY-CONTRACT, PAGE-SEO-CONTRACT per page, SITE-TYPE-SEO-MAPPING-v2 |
| **Pass** | No unresolved SEO gaps for scope; operator approval |
| **Failure** | Missing page SEO contract; intent mismatch with blueprint |

---

### GATE_DESIGN_APPROVED

| Attribute | Value |
|-----------|-------|
| **Purpose** | Visual pattern families bound per block/page |
| **Inputs** | DESIGN-SYSTEM-MAPPING, BLOCK-VISUAL-MAPPING, `VF_*` selections |
| **Pass** | Required blocks have pattern; no pattern contradicts forbidden blocks |
| **Failure** | Missing `VF_*` for required block; pattern implies forbidden block |

---

### GATE_CONTENT_APPROVED

| Attribute | Value |
|-----------|-------|
| **Purpose** | Content signal bindings complete per CONTENT-CONTRACT |
| **Inputs** | BLOCK-CONTENT-CONTRACTS, PAGE-CONTENT-CONTRACTS, signal registry |
| **Pass** | Required signals declared for in-scope blocks (architecture, not copy) |
| **Failure** | Missing signal binding; signals on FORBIDDEN blocks |

---

### GATE_CONTENT_VALIDATION_PASS

| Attribute | Value |
|-----------|-------|
| **Purpose** | Signal architecture validated against contracts |
| **Inputs** | CONTENT-VALIDATION-CONTRACT runs, upstream block validation PASS |
| **Pass** | Content validation `status` = `PASS` or `PASS_WITH_WARNINGS` (no CRITICAL) |
| **Failure** | FAIL; forbidden signal; placeholder signal leakage |

---

### GATE_LEGAL_PACK_PASS

| Attribute | Value |
|-----------|-------|
| **Purpose** | Legal routes and templates align with FROZEN Legal Pack v1 |
| **Inputs** | Legal mapping, template refs, LEGAL_PAGE architecture |
| **Pass** | Required L1–L4 routes present when mapping requires; no placeholder legal HTML in production gate |
| **Failure** | Missing legal route; template drift; unapproved legal modification |

---

### GATE_ENTITY_CARD_READY

| Attribute | Value |
|-----------|-------|
| **Purpose** | Legal entity identity verified for NAP / disclosure signals |
| **Inputs** | Legal Entity Discovery artefacts, entity card checklist |
| **Pass** | Entity card complete when site collects PII, runs forms, or displays regulated identity |
| **Failure** | Entity not verified; stale entity; missing mandatory fields |
| **Conditional** | **SKIP** only when operator documents no PII/forms/legal identity requirement |

---

### GATE_GENERATION_READY

| Attribute | Value |
|-----------|-------|
| **Purpose** | All upstream gates satisfied; scope frozen for specification assembly |
| **Inputs** | Full gate register, GENERATION-CONTRACT draft |
| **Pass** | Gates 1–9 PASS (or 9 SKIP documented); contract fields complete |
| **Failure** | Any required gate FAIL; scope drift; generation before readiness |

---

## 3. Gate dependency order

```text
GATE_BLUEPRINT_APPROVED
    → GATE_PAGE_ARCHITECTURE_APPROVED
    → GATE_BLOCK_VALIDATION_PASS
    → GATE_SEO_APPROVED
    → GATE_DESIGN_APPROVED
    → GATE_CONTENT_APPROVED
    → GATE_CONTENT_VALIDATION_PASS
    → GATE_LEGAL_PACK_PASS
    → GATE_ENTITY_CARD_READY (parallel with legal when applicable)
    → GATE_GENERATION_READY
```

**SEO / Design / Content binding** must not contradict an earlier PASS gate (e.g. SEO cannot require blocks forbidden at validation).

---

## 4. Gate record format (operator)

| Field | Required |
|-------|----------|
| `gate_id` | Yes |
| `status` | `PASS` \| `FAIL` \| `SKIP` |
| `evidence_ref` | Path or artefact ID |
| `operator` | Human identifier |
| `timestamp` | ISO date recommended |

---

*Generation Gates version: v1.*
