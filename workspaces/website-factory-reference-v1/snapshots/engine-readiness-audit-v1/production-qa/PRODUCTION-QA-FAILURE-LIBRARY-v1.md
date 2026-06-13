# Website Factory — Production QA Failure Library v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/production-qa/`  
**Статус:** catalog of common production QA failures — **documentation only**  
**Связь:** [PRODUCTION-QA-SEVERITY-SYSTEM-v1.md](PRODUCTION-QA-SEVERITY-SYSTEM-v1.md), [PRODUCTION-QA-GATES-v1.md](PRODUCTION-QA-GATES-v1.md)

---

## Назначение

Failure Library v1 документирует **типовые** отклонения production architectural QA. Каждая запись: cause → impact → severity → correction.

**Format:**

| Field | Content |
|-------|---------|
| **ID** | Stable failure code `PQF-###` |
| **Scenario** | Human-readable description |
| **Cause** | Why it happens |
| **Impact** | Downstream / handoff risk |
| **Severity** | INFO / WARNING / ERROR / CRITICAL / BLOCKER |
| **Correction** | Operator action |

---

## Architecture layer gaps

### PQF-001 — Missing architecture layer

| Field | Value |
|-------|-------|
| **Scenario** | Required upstream layer (blueprint, page architecture, block registry, etc.) not evidenced for scope |
| **Cause** | Workstream skipped; partial project bootstrap; wrong site type |
| **Impact** | Frontend receives incomplete spec; cascading rework |
| **Severity** | BLOCKER |
| **Correction** | Complete missing layer per [ARCHITECTURE-FOUNDATION-v1.md](../ARCHITECTURE-FOUNDATION-v1.md); re-run QA from affected gate |

---

### PQF-002 — Blueprint missing or wrong type

| Field | Value |
|-------|-------|
| **Scenario** | No canonical blueprint for `site_type_code`, or blueprint from another type |
| **Cause** | Ad-hoc IA; legacy project without blueprint binding |
| **Impact** | Page/block/SEO matrices invalid |
| **Severity** | BLOCKER |
| **Correction** | Select Core blueprint from [blueprints/](../blueprints/); update `blueprint_ref`; re-validate pages |

---

### PQF-003 — Page contract missing

| Field | Value |
|-------|-------|
| **Scenario** | In-scope route lacks PAGE-CONTRACT instance |
| **Cause** | Route added after architecture pass; blueprint not reconciled |
| **Impact** | Block stack and content bindings undefined |
| **Severity** | ERROR |
| **Correction** | Instantiate PAGE-CONTRACT; map `page_type`; re-run page-block validation |

---

### PQF-004 — Block mapping missing

| Field | Value |
|-------|-------|
| **Scenario** | Page lacks block stack per PAGE-BLOCK-MAPPING / blueprint |
| **Cause** | Design-first wireframe without registry alignment |
| **Impact** | Validation and content layers cannot bind |
| **Severity** | ERROR |
| **Correction** | Document block stack; align to BLOCK-REGISTRY; run validation |

---

## Legal & entity

### PQF-005 — Missing Legal Pack

| Field | Value |
|-------|-------|
| **Scenario** | Project lacks Legal Pack v1 reference or required legal routes |
| **Cause** | Non-RU project assumption; legal deferred to frontend |
| **Impact** | LEGAL_PAGE architecture incomplete; compliance gap at architecture level |
| **Severity** | CRITICAL |
| **Correction** | Apply SITE-TYPE-LEGAL-MAPPING-v2; add LEGAL_PAGE contracts; pin LEGAL-PACK-v1-FREEZE |

---

### PQF-006 — Missing Entity Card

| Field | Value |
|-------|-------|
| **Scenario** | Commercial entity required but Legal Entity Card not READY |
| **Cause** | Entity discovery not run; stale draft card |
| **Impact** | NAP / entity signals cannot bind; legal architecture inconsistent |
| **Severity** | CRITICAL |
| **Correction** | Complete [legal-entity/](../legal-entity/) discovery; mark READY or document N/A with sign-off |

---

## Validation gaps

### PQF-007 — Missing page-block validation

| Field | Value |
|-------|-------|
| **Scenario** | No VALIDATION-CONTRACT run for in-scope page |
| **Cause** | Validation skipped after architecture change |
| **Impact** | Unknown block gaps; content validation unreliable |
| **Severity** | ERROR |
| **Correction** | Run page-block validation per [page-block-validation/](../page-block-validation/); attach evidence |

---

### PQF-008 — Missing content validation

| Field | Value |
|-------|-------|
| **Scenario** | Content contracts exist but no CONTENT-VALIDATION-CONTRACT run |
| **Cause** | Assumption that contracts imply pass |
| **Impact** | Signal architecture errors undetected |
| **Severity** | ERROR |
| **Correction** | Run content validation for scope; resolve ERROR/CRITICAL |

---

## SEO, design, content

### PQF-011 — Missing SEO profile

| Field | Value |
|-------|-------|
| **Scenario** | No SEO strategy or site-type SEO mapping for project |
| **Cause** | SEO treated as copy task; v1 registry used without v2 |
| **Impact** | Page SEO roles undefined; intent drift |
| **Severity** | ERROR |
| **Correction** | Apply SEO Architecture v2; create PAGE-SEO-CONTRACT per page |

---

### PQF-012 — Missing design mapping

| Field | Value |
|-------|-------|
| **Scenario** | Required blocks lack `VF_*` / visual pattern binding |
| **Cause** | Design layer skipped; reference CSS used as canon |
| **Impact** | Frontend handoff lacks pattern spec |
| **Severity** | ERROR |
| **Correction** | Complete DESIGN-SYSTEM-MAPPING and BLOCK-VISUAL-MAPPING for scope |

---

### PQF-013 — Missing content contract

| Field | Value |
|-------|-------|
| **Scenario** | Block/page lacks content signal binding where required |
| **Cause** | Copywriting started before content architecture |
| **Impact** | Generation/content specs incomplete |
| **Severity** | ERROR |
| **Correction** | Bind signals per CONTENT-CONTRACT; re-run content validation |

---

## Generation & handoff violations

### PQF-009 — Generation attempted before readiness

| Field | Value |
|-------|-------|
| **Scenario** | Generation contract marked READY while upstream gate FAIL or layer missing |
| **Cause** | Pressure to deliver; manual gate override |
| **Impact** | Invalid handoff package; Frontend builds on broken architecture |
| **Severity** | BLOCKER |
| **Correction** | Halt generation; fix upstream; reset generation contract status; re-run gates |

---

### PQF-010 — Handoff before QA pass

| Field | Value |
|-------|-------|
| **Scenario** | Frontend Handoff approved without `GATE_PRODUCTION_QA_PASS` |
| **Cause** | QA conflated with deploy approval; parallel workstreams |
| **Impact** | Implementation starts without architectural closure |
| **Severity** | BLOCKER |
| **Correction** | Revoke handoff approval; complete Production QA run; re-approve with evidence |

---

## Documentation & quality signals

### PQF-014 — Placeholder leakage in architecture

| Field | Value |
|-------|-------|
| **Scenario** | TBD, Lorem, `{{unresolved}}`, or draft markers in contracts/specs bound for production |
| **Cause** | Draft artefacts promoted without review |
| **Impact** | Ambiguous Frontend spec; false PASS signals |
| **Severity** | ERROR |
| **Correction** | Replace placeholders with architecture decisions or explicit deferred flags outside production scope |

---

### PQF-015 — Unresolved upstream failures

| Field | Value |
|-------|-------|
| **Scenario** | Open FAIL/CRITICAL in validation, content validation, or generation contracts |
| **Cause** | Waiver not documented; partial fix |
| **Impact** | Aggregate QA cannot honestly PASS |
| **Severity** | CRITICAL |
| **Correction** | Resolve failures or downgrade with documented operator waiver per severity system |

---

### PQF-016 — Superseded documentation reference

| Field | Value |
|-------|-------|
| **Scenario** | QA evidence cites SEO v1 only, legacy block mapping, or non-frozen legal |
| **Cause** | Stale project docs; copy-paste from old pilot |
| **Impact** | Wrong requirements applied |
| **Severity** | WARNING |
| **Correction** | Update refs to ACCEPTED/FROZEN canon; re-verify checklist I2 |

---

### PQF-017 — Extended site type without charter

| Field | Value |
|-------|-------|
| **Scenario** | `site_type_code` ∈ Extended Types but QA uses Core-only matrix |
| **Cause** | Registry expansion without blueprint charter |
| **Impact** | Coverage unknown; false confidence |
| **Severity** | BLOCKER |
| **Correction** | Obtain Extended charter or reclassify to Core 5; extend matrix when approved |

---

## Index by severity

| Severity | IDs |
|----------|-----|
| BLOCKER | PQF-001, PQF-002, PQF-009, PQF-010, PQF-017 |
| CRITICAL | PQF-005, PQF-006, PQF-015 |
| ERROR | PQF-003, PQF-004, PQF-007, PQF-008, PQF-011, PQF-012, PQF-013, PQF-014 |
| WARNING | PQF-016 |
| INFO | — (use warnings array; no catalogue entry required) |

---

*Production QA Failure Library v1 — architectural failures only.*
