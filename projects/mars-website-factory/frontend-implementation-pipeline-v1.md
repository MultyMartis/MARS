# Website Factory Frontend Implementation Pipeline v1

**Status:** **documented** — canonical gate chain from source authority through correction loop.  
**Not:** runtime orchestration, workflow engine, or autonomous agent router.

**Purpose:** Repair the documented gap where workflows jumped `JPG Audit → Structure Lock → HTML` without mandatory foundation and specification layers.

**Supersedes (interpretation):** Implicit shortcuts that skip normalization or Site-Wide Style Foundation. Does **not** replace [website-factory-workflow-v0.md](website-factory-workflow-v0.md) S01–S15 narrative — **extends** frontend path.

**Registry:** [registries.md §6](registries.md#6-frontend-production-rules).

---

## Canonical sequence

```text
INTAKE
  → SOURCE AUTHORITY
  → VISUAL AUDIT
  → GROUNDING REVIEW
  → DESIGN FOUNDATION EXTRACTION
  → PRACTICAL VALUE NORMALIZATION
  → SITE-WIDE STYLE FOUNDATION
  → OPERATOR FOUNDATION APPROVAL
  → PAGE IMPLEMENTATION SPECIFICATION
  → BLOCK IMPLEMENTATION SPECIFICATION
  → HTML
  → HTML REVIEW
  → SCSS
  → VISUAL QA
  → CORRECTION LOOP
```

**Greenfield shell path** (non–JPG-only): after OPERATOR FOUNDATION APPROVAL, may run [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md) Visual Foundation demo **in parallel discipline** — demo page proves tokens; Home blocks still require Block Implementation Specification.

---

## Gate table

| Gate | ID | Input | Output | Role | Approval | STOP if | Next authorized |
|------|-----|-------|--------|------|----------|---------|-----------------|
| Intake | G-INT | Brief, production mode | Passport, scope | PM / operator | production_mode declared | mode undeclared | Source Authority |
| Source Authority | G-SRC | Design files | Source manifest, hash, policy | Operator | source list locked | forbidden source used | Visual Audit |
| Visual Audit | G-AUD | Source JPG/export | Raw observations, geometry, components | Audit agent / operator | audit artefact complete | no hash match | Grounding Review |
| Grounding Review | G-GRD | Raw audit | Grounded sections, PARTIAL/FAIL/PASS | Operator + reviewer | grounding verdict | FAIL unrecovered | Design Foundation Extraction |
| Design Foundation Extraction | G-EXT | Grounded audit | Observed families (no production px) | Engineering | extraction doc | skipped extraction | Normalization |
| Practical Value Normalization | G-NRM | Extraction + OL-01 | Traceability table, token proposals | Engineering | normalization doc | no traceability row | Style Foundation draft |
| Site-Wide Style Foundation | G-FND | Normalization | Foundation MD + JSON proposal | Engineering | `foundation_status` | values without evidence | Operator Foundation Approval |
| Operator Foundation Approval | G-OPF | Foundation proposal | `implementation_authorized` flags | **Operator (Андрей)** | APPROVED / PARTIAL | PARTIAL blocks scoped work | Page Spec |
| Page Implementation Specification | G-PGS | Foundation + grounded map | Page section binding map | Engineering | page spec | missing section list | Block Spec |
| Block Implementation Specification | G-BLS | Foundation + page spec + layout/group specs | Per-block binding doc | Engineering | block spec per section | unbound tokens | HTML |
| HTML | G-HTM | Approved block spec | Structure-only markup | Forge / gulp agent | `html_structure_authorized` | spec missing | HTML Review |
| HTML Review | G-HTR | HTML | Review PASS / fix list | Operator | visual structure ack | FAIL | SCSS |
| SCSS | G-SCS | HTML + foundation | Scoped styles | Forge / gulp agent | `scss_authorized` | pre-SCSS checklist FAIL | Visual QA |
| Visual QA | G-VQA | Build + source | QA report | Operator + QA docs | OPERATOR VISUAL REVIEW | FAIL | Correction or PASS |
| Correction Loop | G-COR | QA defect class | Updated spec/foundation/audit/code | Responsible layer | defect routed | local magic-number fix | Re-enter at routed gate |

---

## Layer contracts

| Layer transition | Contract document |
|------------------|-------------------|
| Extraction → Normalization | [practical-value-normalization-contract-v1.md](practical-value-normalization-contract-v1.md) |
| Normalization → Foundation | [site-wide-style-foundation-contract-v1.md](site-wide-style-foundation-contract-v1.md) |
| Foundation → Block work | [block-implementation-specification-contract-v1.md](block-implementation-specification-contract-v1.md) |
| Composition before HTML | [group-decomposition-law-v1.md](group-decomposition-law-v1.md) · [layout-spec-law-v1.md](layout-spec-law-v1.md) |
| SCSS pre-flight | [frontend-pre-scss-validation-checklist-v1.md](frontend-pre-scss-validation-checklist-v1.md) |
| QA | [operational-qa-entry-v1.md](operational-qa-entry-v1.md) · [pixel-fidelity-audit-rules-v1.md](pixel-fidelity-audit-rules-v1.md) |

---

## Cross-layer gap closure (2026-06-22 audit)

| Prior gap | Repair |
|-----------|--------|
| JPG Audit → HTML | Insert EXT → NRM → FND → BLS gates |
| No normalization contract | [practical-value-normalization-contract-v1.md](practical-value-normalization-contract-v1.md) |
| Production Standards assumed before JPG-only pilot | Foundation contract allows JPG-derived proposal until promoted |
| FP-0002 v3 px in section-spacing rule §4 | Marked LEGACY for V6 — not visual authority |
| Structure lock treated as implementation structure | Grounding review + foundation separation |

---

## SAFE UNKNOWN routing

When grounding or foundation is **PARTIAL**:

- Document in foundation SAFE UNKNOWN
- Set `header_implementation_authorized: false` (or scoped false)
- Block Implementation Specification for affected block **withheld**
- Do not infer Y-boundaries from algorithmic blocks

---

## Honesty boundary

This pipeline is **human-operated documentation**. No claim of automated gate enforcement unless a project adds explicit tooling.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-06-22 | v1 — Cross-layer audit repair; connects audit through correction loop |
