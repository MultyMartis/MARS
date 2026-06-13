# Website Factory — Validation Roadmap v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/page-block-validation/`  
**Статус:** future evolution path — **documentation only**  
**Связь:** [VALIDATION-GAPS-v1.md](VALIDATION-GAPS-v1.md), [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](../WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md)

---

## Назначение

Validation Roadmap v1 описывает **планируемую эволюцию** от documentation-only validation (v1) к runtime QA. **Не является** commitment schedule или implementation proof.

---

## Evolution path

```
Documentation          ← v1 (CURRENT)
        ↓
Manual Validation      ← operator checklist + VALIDATION-CONTRACT
        ↓
Semi-Automatic Validation
        ↓
Automated Validation
        ↓
Runtime QA Layer
```

---

## Phase 0 — Documentation (CURRENT — v1)

**Status:** **IN PROGRESS** → operator acceptance pending

**Deliverables:**

| Artifact | Status |
|----------|--------|
| PAGE-BLOCK-VALIDATION-SYSTEM-v1 | **DELIVERED** |
| VALIDATION-CONTRACT-v1 | **DELIVERED** |
| PAGE-BLOCK-VALIDATION-RULES-v1 | **DELIVERED** |
| PAGE-TYPE-VALIDATION-MATRIX-v1 | **DELIVERED** |
| BLUEPRINT-VALIDATION-MATRIX-v1 | **DELIVERED** |
| VALIDATION-SEVERITY-SYSTEM-v1 | **DELIVERED** |
| VALIDATION-FAILURE-LIBRARY-v1 | **DELIVERED** |
| VALIDATION-GAPS-v1 | **DELIVERED** |
| VALIDATION-ROADMAP-v1 | **DELIVERED** |

**Exit criteria:**

- Operator marks Page → Block Validation v1 **ACCEPTED**
- Cross-layer inconsistencies documented in VALIDATION-GAPS-v1
- No false claims of automated validation

---

## Phase 1 — Manual Validation

**Status:** **NEXT** (immediate use of v1 docs)

**Goal:** Operators apply validation rules during project IA review and pre-Design gate.

**Activities:**

- Collect `actual_blocks` from Page Contract / IA document
- Fill VALIDATION-CONTRACT fields manually
- Apply PAGE-BLOCK-VALIDATION-RULES-v1
- Record PASS / FAIL in project report
- Reference VALIDATION-FAILURE-LIBRARY for corrections

**Not in scope:** Scripts, CI, schema

**Exit criteria:**

- ≥1 pilot project validated manually with documented outcome
- Failure library extended with real project entries (optional)

---

## Phase 2 — Semi-Automatic Validation

**Status:** **FUTURE**

**Goal:** Helper compares structured IA manifest against PAGE-BLOCK-MAPPING without full frontend scan.

**Planned capabilities:**

| Capability | Description |
|------------|-------------|
| JSON Schema | VALIDATION-CONTRACT-v1 + Page Contract fields |
| CLI validator (read-only) | Input: project manifest YAML/JSON → output: validation_result |
| Blueprint validator | Required pages list + site-wide FORBIDDEN sweep |
| Diff report | missing_blocks / unexpected_blocks as markdown |
| OR-group resolver | Automated TRUST|TESTIMONIALS etc. |

**Dependencies:**

- Block Registry gaps closed (`STICKY_CTA`, etc.) or explicit ignore list
- Standard project manifest location

**Not in scope:** DOM parsing, design generation

---

## Phase 3 — Automated Validation

**Status:** **FUTURE**

**Goal:** Validation integrated into Factory build path; fail build on CRITICAL/ERROR.

**Planned capabilities:**

| Capability | Description |
|------------|-------------|
| CI gate | Run CLI validator on PR / pre-Design job |
| Frontend validator | Scan templates/partials for `block_id` presence |
| Batch site validation | Full IA in one run |
| Validation report artifact | Committed or CI-uploaded |

**Dependencies:**

- Phase 2 CLI stable
- Frontend block markers or partial naming convention

**Not in scope:** Runtime monitoring, A/B testing

---

## Phase 4 — Runtime QA Layer

**Status:** **FUTURE**

**Goal:** Post-deploy checks that live pages match contracts.

**Planned capabilities:**

| Capability | Description |
|------------|-------------|
| Page scanner | HTTP fetch + structural heuristics |
| Legal link checker | L1–L4 reachable from footer |
| Conversion path probe | LANDING form present; ECOMMERCE cart path |
| Drift alert | Contract vs production mismatch |

**Dependencies:**

- Stable URL conventions
- Operator authorization for production scans

**Not in scope:** Autonomous remediation

---

## Relationship to Website Factory priorities

| Factory priority | Validation phase |
|------------------|------------------|
| Page → Block Validation v1 | Phase 0 (Documentation) |
| SITE-TYPE-SEO-MAPPING-v2 | Parallel track — SEO validation **FUTURE** |
| DESIGN SYSTEM MAPPING | May add design-level validation **FUTURE** |

Sequence after v1 acceptance:

1. **ACCEPT** Page Block Validation v1
2. **BEGIN** Manual Validation on reference/pilot projects
3. **QUEUE** SEO Mapping v2 (per WEBSITE-FACTORY-NEXT-PRIORITIES-v1)
4. **LATER** Semi-Automatic Validation (no date)

---

## Anti-patterns (do not skip phases)

| Anti-pattern | Risk |
|--------------|------|
| Build CLI before contract stable | Rework, false PASS |
| Claim runtime validation exists | Governance drift |
| Auto-fix FORBIDDEN blocks without reclassification | Wrong Blueprint |
| Validation without Page Contract | Un reproducible runs |

---

## SAFE UNKNOWN

- Phase 2–4 delivery dates — **not scheduled**
- Tooling location (`tools/` vs external package) — **UNKNOWN**
- Integration with mars-survivability validators — **FUTURE** optional

---

*Validation Roadmap version: v1. Canonical location: `workspaces/website-factory-reference-v1/page-block-validation/`.*
