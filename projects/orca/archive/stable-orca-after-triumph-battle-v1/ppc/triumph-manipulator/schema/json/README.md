# ORCA PPC JSON Schema — Triumph Manipulator v1

**Phase:** 3 — formal JSON contract + validation report shape  
**Status:** Schema files + draft fixture only · **no** validator runtime · **no** exporter  
**Scope:** Yandex **Search** only · human-supervised · search-only envelope preserved

---

## Purpose

This folder turns the Phase 2 markdown entity model into a **machine-readable JSON contract** for future:

| Consumer | Uses |
|----------|------|
| Validation engine | Load document → run rules → emit `ValidationReport` |
| Exporter | Map validated graph → Commander Excel (transport only) |
| Prompt-to-entity | Constrained generation with schema guardrails |
| Human review | Draft fixtures, diff review, approval flags |

**Source of truth:** Structured JSON document — **not** Excel. Excel remains transport per [export/direct-commander-foundation-v0.md](../../export/direct-commander-foundation-v0.md).

---

## Files

| File | Role |
|------|------|
| [orca-ppc-document-v1.schema.json](orca-ppc-document-v1.schema.json) | Root PPC project document (campaigns → groups → ads) |
| [validation-report-v1.schema.json](validation-report-v1.schema.json) | Output artifact from a future validation run |

**Example instances:** [`../instances/`](../instances/) — draft fixtures only, not launch-approved.

---

## Document identity

| Field | Convention |
|-------|------------|
| `schema_version` | Literal `"v1"` |
| `project_id` | Stable slug, e.g. `triumph-manipulator-krd-search` |
| `source_pack` | `triumph-manipulator` |
| `search_only_scope` | Must be `true` at root and on every campaign |

Entity IDs (`campaign_id`, `group_id`, `ad_id`) are **internal** until human import into Direct Commander.

---

## Validation policy (preserved from Phase 2)

Rules are **documented** in [validation-schema-v1.md](../validation-schema-v1.md). The root document’s `validation_policy` block records which rule classes apply; execution is **future** — not in this repo.

| Class | `rule_class` value | Focus |
|-------|-------------------|--------|
| Structural | `structural` | Required fields, graph coherence, search-only scope |
| Symbol | `symbol` | Direct field limits (spaces included), truncation risk |
| Semantic | `semantic` | One group = one intent, alignment, anti-garbage, no generic ads |
| Landing | `landing_mismatch` | Ad intent continues on landing blueprint |
| Commercial | `commercial` | CTA coherence, capability truth, mobile readability, trust |
| Survivability | `survivability` | Quality over quantity, human naming, no autonomous launch |
| Export mapping | `export_mapping` | Entity → Commander column mapping sanity (pre-export) |

**Severity mapping (engine future):** schema report uses `status`: `pass` \| `warn` \| `fail` \| `not_checked` \| `safe_unknown`.

---

## Human review contract

Root `human_review` gates export and launch:

| Flag | Meaning |
|------|---------|
| `required` | Document must not be treated as launch-ready without review |
| `approved_for_export` | Human allows Excel export prep |
| `approved_for_commander_import` | Human allows Commander import |
| `approved_for_launch` | Human allows live launch in Direct |

**Draft fixtures** set `required: true` and launch/export flags `false`.

---

## Usage (today)

1. Author or generate JSON matching `orca-ppc-document-v1.schema.json`
2. Compare manually against [validation-schema-v1.md](../validation-schema-v1.md) (checklist)
3. Store drafts under `schema/instances/` — label as **draft**, not approved
4. **Do not** claim validation passed without a future engine + human sign-off

---

## Boundaries

- **No** validator implementation in Phase 3  
- **No** exporter implementation  
- **No** n8n, API, daemon, or runtime claims  
- **No** autonomous launch or optimization language  
- **No** modification to Commander template assets  

---

## Upstream / downstream

| Phase | Artifact |
|-------|----------|
| Phase 2 | Markdown entity schemas in [`../`](../) |
| **Phase 3 (this)** | JSON Schema + instance README + S-tier draft fixture |
| Phase 4 (recommended) | Validation engine consuming both schemas |
| Phase 5 (recommended) | Exporter + prompt constraints |

---

## SAFE UNKNOWN

- Live production URLs for Triumph — fixture uses placeholder hosts; confirm before import  
- Exact duplicate-normalization (ё/е) — define in validation engine  
- Platform limit drift vs template — template + live Direct win over schema defaults
