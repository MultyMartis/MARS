# ORCA PPC Entity Schema — Triumph Manipulator

**Version:** v1  
**Phase:** 2 (markdown) + **Phase 3** (JSON Schema)  
**Status:** Markdown + JSON contract · **no** validator runtime · **no** exporter code  
**Scope:** Yandex **Search** only · human-supervised

---

## Purpose

This folder defines the **internal structured PPC entity model** for Triumph Manipulator — the layer that will later feed validation, export, prompts, and workflow automation.

| Principle | Rule |
|-----------|------|
| Source of truth | Structured entities + pack doctrine — **not** Excel |
| Excel | Transport/export only ([`../export/direct-commander-foundation-v0.md`](../export/direct-commander-foundation-v0.md)) |
| Validation | **Before** export ([`validation-schema-v1.md`](validation-schema-v1.md)) |
| Exporter | Dumb field mapping only ([`export-mapping-schema-v1.md`](export-mapping-schema-v1.md)) |

---

## Entity graph (v1)

```
Campaign
  └── Group[]          (one semantic intent per group)
        ├── keyword_cluster
        ├── negatives
        ├── landing_route   → Landing routing schema
        └── Ad[]            (one or more ads per group)
```

Validation and export are **cross-cutting layers** on the full graph, not child entities.

---

## Schema documents

| File | Role |
|------|------|
| [entity-model-overview-v1.md](entity-model-overview-v1.md) | Graph, IDs, lifecycle, relationships |
| [campaign-entity-schema-v1.md](campaign-entity-schema-v1.md) | Campaign container fields |
| [group-entity-schema-v1.md](group-entity-schema-v1.md) | Group, keywords, intent purity |
| [ad-entity-schema-v1.md](ad-entity-schema-v1.md) | Headlines, extensions, Yandex alignment |
| [landing-routing-schema-v1.md](landing-routing-schema-v1.md) | Landing type, use-case/capability/B2B/intercity routing |
| [validation-schema-v1.md](validation-schema-v1.md) | Structural, symbol, semantic, commercial checks |
| [export-mapping-schema-v1.md](export-mapping-schema-v1.md) | Entity → Commander Excel column mapping |
| [future-json-model-notes-v1.md](future-json-model-notes-v1.md) | Superseded for shape by Phase 3 JSON — historical notes |
| [json/README.md](json/README.md) | **Phase 3** — formal JSON Schema + validation report contract |
| [json/orca-ppc-document-v1.schema.json](json/orca-ppc-document-v1.schema.json) | Root PPC document JSON Schema |
| [json/validation-report-v1.schema.json](json/validation-report-v1.schema.json) | Validation report JSON Schema |
| [instances/README.md](instances/README.md) | Draft instance fixtures (not launch-approved) |

---

## Upstream references (read on demand)

| Area | Path |
|------|------|
| Doctrine | [`../doctrine/generation-logic-v0.md`](../doctrine/generation-logic-v0.md) |
| Intent tiers | [`../research/intent-groups-v1.md`](../research/intent-groups-v1.md) |
| Architecture | [`../architecture/system-architecture-v0.md`](../architecture/system-architecture-v0.md) |
| Export contract | [`../export/direct-commander-foundation-v0.md`](../export/direct-commander-foundation-v0.md) |
| Commander template | [`../assets/direct-commander-template/`](../assets/direct-commander-template/) |
| Landing blueprints | [`../landing-pages/INDEX.md`](../landing-pages/INDEX.md) |

---

## Phase maturity

| Layer | v1 status |
|-------|-----------|
| Entity schema (markdown, this folder) | **Defined** |
| JSON Schema contract ([json/](json/)) | **Defined** (Phase 3) |
| JSON draft instances ([instances/](instances/)) | **Present** — draft only |
| Validation engine | **Not in repo** — rules + report schema documented |
| Exporter | **Not in repo** — mapping documented |
| Autonomous launch/optimize | **Out of scope** |

---

## Operator quick path

1. [entity-model-overview-v1.md](entity-model-overview-v1.md) — understand graph  
2. Build or review entities using campaign → group → ad docs  
3. Assign landing via [landing-routing-schema-v1.md](landing-routing-schema-v1.md)  
4. Run checks from [validation-schema-v1.md](validation-schema-v1.md) (manual today)  
5. Map to Excel only when exporting — [export-mapping-schema-v1.md](export-mapping-schema-v1.md)  
6. **STOP** — human imports in Commander

---

## Boundaries

- **No** RSYA, Master Campaigns, retargeting fields in v1  
- **No** autonomous optimization or bid automation entities  
- **No** governance expansion — local pack schema only
