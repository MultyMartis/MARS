# ORCA Exporter Engine — Triumph Manipulator (Phase 5)

**Version:** v1  
**Phase:** 5 — Exporter Engine **foundation** (architecture + mapping design)  
**Status:** Documentation only · **no** exporter runtime · **no** autonomous export · **no** launch system  
**Scope:** Yandex **Search** only · human-supervised

---

## Purpose

This folder defines how the **Exporter Engine** will map a **validated** PPC entity graph into **Direct Commander Excel** — a **dumb transport layer** only.

| Principle | Rule |
|-----------|------|
| Input | `OrcaPpcDocument` + `ValidationReport` |
| Output | Commander-compatible `.xlsx` from [template](../assets/direct-commander-template/) |
| Excel | **Not** source-of-truth |
| Validation | **Before** export — exporter does not fix failures |
| Launch | **Human** in Direct — never automatic |

---

## Documents

| File | Role |
|------|------|
| [exporter-engine-overview-v1.md](exporter-engine-overview-v1.md) | Lifecycle, layers, boundaries, human review |
| [entity-to-commander-mapping-v1.md](entity-to-commander-mapping-v1.md) | Campaign / group / keyword / ad / extension / negative mapping |
| [export-preconditions-v1.md](export-preconditions-v1.md) | Gates: report, `export_allowed`, schema, template |
| [row-generation-rules-v1.md](row-generation-rules-v1.md) | Ordering, parent-child rows, extensions, dedup |
| [draft-export-rules-v1.md](draft-export-rules-v1.md) | Active vs draft ads and mixed states |
| [field-normalization-rules-v1.md](field-normalization-rules-v1.md) | Whitespace, UTF-8, URLs — **no silent truncation** |
| [export-blocking-rules-v1.md](export-blocking-rules-v1.md) | Refusal conditions and operator actions |
| [commander-template-contract-v1.md](commander-template-contract-v1.md) | Template role, version, drift, verification |
| [future-exporter-implementation-notes-v1.md](future-exporter-implementation-notes-v1.md) | Future CLI/xlsx hooks — **not** implementation |

---

## Upstream contracts

| Area | Path |
|------|------|
| Mapping summary (Phase 2) | [schema/export-mapping-schema-v1.md](../schema/export-mapping-schema-v1.md) |
| PPC document JSON | [schema/json/orca-ppc-document-v1.schema.json](../schema/json/orca-ppc-document-v1.schema.json) |
| Validation report JSON | [schema/json/validation-report-v1.schema.json](../schema/json/validation-report-v1.schema.json) |
| Export gate | [validation/validation-report-generation-v1.md](../validation/validation-report-generation-v1.md) |
| EX rules | [validation/rule-registry-v1.md](../validation/rule-registry-v1.md) (EX-01–EX-06) |
| Export doctrine | [export/direct-commander-foundation-v0.md](../export/direct-commander-foundation-v0.md) |
| Template asset | [assets/direct-commander-template/](../assets/direct-commander-template/) |

---

## Operator quick path (today — manual)

1. Validate document → obtain `ValidationReport` with `export_allowed: true`.  
2. Read [export-preconditions-v1.md](export-preconditions-v1.md) checklist.  
3. Map entities using [entity-to-commander-mapping-v1.md](entity-to-commander-mapping-v1.md) + template.  
4. Human review workbook → import in Commander.  
5. **STOP** — launch only in Direct UI.

---

## Phase maturity

| Layer | Status |
|-------|--------|
| Exporter architecture (this folder) | **Defined** (Phase 5) |
| Exporter runtime (CLI, xlsx writer) | **Not in repo** |
| Autonomous export / launch | **Forbidden** |

---

## Boundaries

- **No** semantic rewriting in export layer  
- **No** governance expansion — local Triumph pack only  
- **No** round-trip Excel → entities in v1 (one-way export first)
