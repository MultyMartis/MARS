# ORCA Validation Engine — Triumph Manipulator (Phase 4)

**Version:** v1  
**Phase:** 4 — Validation Engine **foundation** (architecture + rule execution model)  
**Status:** Documentation only · **no** validator runtime · **no** daemon · **no** autonomous launch  
**Scope:** Yandex **Search** only · human-supervised

---

## Purpose

This folder defines how the **Validation Engine** will operate when implemented — rule registry, execution flow, severity model, report generation, and survivability gates.

Validation exists to **prevent garbage campaigns before export**, not to auto-correct or launch ads.

| Principle | Rule |
|-----------|------|
| When | After entity assembly, **before** Excel export |
| Excel | Transport only — never SoT |
| Output | `ValidationReport` per [validation-report-v1.schema.json](../schema/json/validation-report-v1.schema.json) |
| Human | Final authority on warnings, export, and launch |

---

## Documents

| File | Role |
|------|------|
| [validation-engine-overview-v1.md](validation-engine-overview-v1.md) | Lifecycle, traversal, stages, severity, blocking vs warn, human review |
| [rule-registry-v1.md](rule-registry-v1.md) | Canonical rule catalog (ST, SY, SE, LM, CM, SV, EX) |
| [rule-execution-flow-v1.md](rule-execution-flow-v1.md) | Execution model, ordering, aggregation, export gate |
| [symbol-validation-rules-v1.md](symbol-validation-rules-v1.md) | SY-* — Yandex field limits, truncation, empty fields |
| [semantic-validation-rules-v1.md](semantic-validation-rules-v1.md) | SE-* — intent purity, anti-garbage, Yandex alignment |
| [landing-continuity-rules-v1.md](landing-continuity-rules-v1.md) | LM-* — ad ↔ landing, blueprint family, fallback |
| [commercial-validation-rules-v1.md](commercial-validation-rules-v1.md) | CM-* — CTA, capability truth, trust, mobile |
| [survivability-validation-rules-v1.md](survivability-validation-rules-v1.md) | SV-* — operability, anti-chaos, human review |
| [validation-report-generation-v1.md](validation-report-generation-v1.md) | Report pipeline, gates, `export_allowed`, `launch_allowed` semantics |
| [future-validator-implementation-notes-v1.md](future-validator-implementation-notes-v1.md) | Future CLI/AJV hooks — **not** implementation |

---

## Upstream contracts (read on demand)

| Area | Path |
|------|------|
| Rule IDs (summary) | [schema/validation-schema-v1.md](../schema/validation-schema-v1.md) |
| JSON report shape | [schema/json/validation-report-v1.schema.json](../schema/json/validation-report-v1.schema.json) |
| PPC document shape | [schema/json/orca-ppc-document-v1.schema.json](../schema/json/orca-ppc-document-v1.schema.json) |
| Draft fixture | [schema/instances/triumph-s-tier-draft-v1.json](../schema/instances/triumph-s-tier-draft-v1.json) |
| Doctrine | [doctrine/generation-logic-v0.md](../doctrine/generation-logic-v0.md) |
| Export contract | [export/direct-commander-foundation-v0.md](../export/direct-commander-foundation-v0.md) |

---

## Operator quick path (today — manual)

1. Build or load structured PPC document (JSON or checklist against schema docs).  
2. Walk rules in [rule-registry-v1.md](rule-registry-v1.md) by class (ST → SY → SE → LM → CM → SV → EX).  
3. Record findings; block export on any `error`.  
4. Resolve warnings or document override reason.  
5. **STOP** — human imports Commander and launches in Direct.

---

## Phase maturity

| Layer | Status |
|-------|--------|
| Validation architecture (this folder) | **Defined** (Phase 4) |
| Validator runtime (CLI, service) | **Not in repo** |
| Autonomous launch / auto-fix | **Forbidden** |

---

## Boundaries

- **No** governance expansion — local Triumph pack only  
- **No** RSYA / Master Campaigns rules in v1  
- **No** runtime claims — documentation describes **target** behavior for a future human-operated validator
