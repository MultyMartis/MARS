# Triumph Manipulator PPC — operational index

**Purpose:** One map for operators and agents working this pack — **not** a full repo inventory.  
**Posture:** Post–Cycle 8 operational-first · Tier 0–3 routing · human-supervised · search-only.

| Tier | Use when |
|------|----------|
| **0** | New to MARS — [README.md](../../../../README.md), [AGENTS.md](../../../../AGENTS.md) |
| **1** | ORCA ecosystem — [projects/orca/README.md](../../README.md) |
| **2** | **This file** — one Core Run per session |
| **3** | Individual landing blueprints, extended architecture notes — on demand |

---

## Canonical entry

- **[README.md](README.md)** — pack identity, boundaries, maturity, MARS/Factory relationships

---

## Core Run (default session)

Open **one row** unless the task explicitly needs Extended.

| Concern | Start here |
|---------|------------|
| **Pack identity / honesty** | [README.md](README.md) |
| **How ORCA should think (doctrine)** | [doctrine/generation-logic-v0.md](doctrine/generation-logic-v0.md) |
| **Intent tiers & launch priority** | [research/intent-groups-v1.md](research/intent-groups-v1.md) |
| **Campaign / landing architecture** | [architecture/system-architecture-v0.md](architecture/system-architecture-v0.md) |
| **Commander export contract** | [export/direct-commander-foundation-v0.md](export/direct-commander-foundation-v0.md) |
| **Landing blueprint for a segment** | [landing-pages/INDEX.md](landing-pages/INDEX.md) → one page file |
| **Commander Excel reference** | [assets/direct-commander-template/README.md](assets/direct-commander-template/README.md) |
| **Future code / automation (hooks only)** | [export/future-implementation-hooks-v0.md](export/future-implementation-hooks-v0.md) |
| **PPC entity schema (Phase 2)** | [schema/README.md](schema/README.md) → [entity-model-overview-v1.md](schema/entity-model-overview-v1.md) |
| **JSON Schema + validation contract (Phase 3)** | [schema/json/README.md](schema/json/README.md) → [orca-ppc-document-v1.schema.json](schema/json/orca-ppc-document-v1.schema.json) |
| **Validation engine foundation (Phase 4)** | [validation/README.md](validation/README.md) → [validation-engine-overview-v1.md](validation/validation-engine-overview-v1.md) |
| **Exporter engine foundation (Phase 5)** | [exporter/README.md](exporter/README.md) → [exporter-engine-overview-v1.md](exporter/exporter-engine-overview-v1.md) |
| **Prompt system foundation (Phase 6)** | [prompts/README.md](prompts/README.md) → [prompt-system-overview-v1.md](prompts/prompt-system-overview-v1.md) |
| **Validation CLI (Phase 7–8)** | [tools/validation-cli/README.md](tools/validation-cli/README.md) — v0.1 hardened · local human-triggered · **not** runtime |
| **Exporter CLI (Phase 9 prototype)** | [tools/exporter-cli/README.md](tools/exporter-cli/README.md) — v0 transport draft · local human-triggered · **not** runtime |
| **Commander template fidelity v0** | [tools/exporter-cli/template-analysis-report.md](tools/exporter-cli/template-analysis-report.md) — introspection + header map · **not** import |
| **Commander template-fill export v0** | [tools/exporter-cli/template-fill-notes-v0.md](tools/exporter-cli/template-fill-notes-v0.md) — `export.js --template-fill` · **not** production import |
| **XLSX integrity hardening v0** | [tools/exporter-cli/xlsx-integrity-notes-v0.md](tools/exporter-cli/xlsx-integrity-notes-v0.md) — exact-cell writes + reopen check · **not** import automation |
| **OOXML workbook forensics v0** | [tools/exporter-cli/ooxml-diff-report-v0.md](tools/exporter-cli/ooxml-diff-report-v0.md) — `ooxml-forensics.js` · Excel vs ExcelJS · **not** exporter fix |
| **Sheet1 ZIP patch export v0** | [tools/exporter-cli/sheet1-patch-notes-v0.md](tools/exporter-cli/sheet1-patch-notes-v0.md) — `sheet1-patch-export.js` · patch **only** sheet1.xml · **not** production import |
| **Commander template cleanup + new entity v0** | [tools/exporter-cli/template-cleanup-rules-v0.md](tools/exporter-cli/template-cleanup-rules-v0.md) — stale-row neutralization · ID isolation · [sample-cleanup-run.md](tools/exporter-cli/sample-cleanup-run.md) · **not** auto-import |

---

## Quick-start routes

### Route A — New Triumph search campaign (human-supervised)

1. [research/intent-groups-v1.md](research/intent-groups-v1.md) — pick tier S/A segments first  
2. [doctrine/generation-logic-v0.md](doctrine/generation-logic-v0.md) — intent purity, headlines, anti-generic  
3. [landing-pages/INDEX.md](landing-pages/INDEX.md) — assign best-fit landing per group  
4. [export/direct-commander-foundation-v0.md](export/direct-commander-foundation-v0.md) — entity model + validation-before-export  
5. Draft in human tools → validate → reference template only at export prep  
6. **STOP** — human imports and launches in Direct

### Route B — Landing / continuation review only

1. [doctrine/generation-logic-v0.md](doctrine/generation-logic-v0.md) — landing continuation doctrine  
2. One blueprint from [landing-pages/](landing-pages/)  
3. Parent ORCA: [projects/orca/landing-match/](../../landing-match/) if cross-checking mismatch patterns

### Route C — Export / Commander prep (no runtime)

1. [schema/entity-model-overview-v1.md](schema/entity-model-overview-v1.md) — internal entity graph  
2. [validation/validation-engine-overview-v1.md](validation/validation-engine-overview-v1.md) — validation lifecycle + gates  
3. [validation/rule-registry-v1.md](validation/rule-registry-v1.md) — rule IDs (ST/SY/SE/LM/CM/SV/EX)  
4. [schema/validation-schema-v1.md](schema/validation-schema-v1.md) — rule summary (Phase 2–3)  
5. [export/direct-commander-foundation-v0.md](export/direct-commander-foundation-v0.md)  
6. [schema/export-mapping-schema-v1.md](schema/export-mapping-schema-v1.md)  
7. [exporter/export-preconditions-v1.md](exporter/export-preconditions-v1.md) — export gates  
8. [exporter/entity-to-commander-mapping-v1.md](exporter/entity-to-commander-mapping-v1.md)  
9. [assets/direct-commander-template/README.md](assets/direct-commander-template/README.md)

---

## Recommended reading order (first pass)

1. [README.md](README.md)  
2. [doctrine/generation-logic-v0.md](doctrine/generation-logic-v0.md)  
3. [research/intent-groups-v1.md](research/intent-groups-v1.md)  
4. [architecture/system-architecture-v0.md](architecture/system-architecture-v0.md)  
5. [export/direct-commander-foundation-v0.md](export/direct-commander-foundation-v0.md)  
6. [landing-pages/01-master-hot-general.md](landing-pages/01-master-hot-general.md)  
7. One intent-specific landing (from [landing-pages/INDEX.md](landing-pages/INDEX.md))

---

## Doctrine docs

| Doc | Role |
|-----|------|
| [doctrine/generation-logic-v0.md](doctrine/generation-logic-v0.md) | Intent-first generation, Yandex bold-highlight, anti-garbage, mobile-first, human review |
| [doctrine/README.md](doctrine/README.md) | Doctrine folder index |

---

## Implementation foundation docs

| Doc | Role |
|-----|------|
| [architecture/system-architecture-v0.md](architecture/system-architecture-v0.md) | Layered ORCA flow (intake → export → human); survivability; **no runtime claimed** |
| [export/direct-commander-foundation-v0.md](export/direct-commander-foundation-v0.md) | Entity model, validation-before-export, Commander transport |
| [export/future-implementation-hooks-v0.md](export/future-implementation-hooks-v0.md) | JSON schema, validation, exporter, prompts, n8n — **targets only** |
| [schema/](schema/) | **Phase 2–3** — markdown entity schemas + JSON Schema contract; **no validator/exporter runtime** |
| [schema/json/](schema/json/) | **Phase 3** — `orca-ppc-document-v1.schema.json`, `validation-report-v1.schema.json` |
| [schema/instances/](schema/instances/) | **Phase 3** — draft fixtures (e.g. S-tier draft) — not launch-approved |
| [validation/](validation/) | **Phase 4** — validation engine architecture, rule registry, execution model — **no runtime** |
| [exporter/](exporter/) | **Phase 5** — exporter architecture, mapping, blocking, template contract — **no runtime** |
| [prompts/](prompts/) | **Phase 6** — prompt lifecycle, JSON-first generation, review gates — **no runtime** |
| [tools/validation-cli/](tools/validation-cli/) | **Phase 7–8** — validation CLI v0.1 (dual AJV, deterministic report, golden fixture) — **not** service/daemon |
| [tools/exporter-cli/](tools/exporter-cli/) | **Phase 9** — exporter CLI prototype v0 (precheck → mapping → XLSX draft) — **not** service/Direct API |

---

## Research

| Doc | Role |
|-----|------|
| [research/intent-groups-v1.md](research/intent-groups-v1.md) | Tier S/A/B/X intent groups, launch strategy, reject list |

---

## Landing pages

Full index: [landing-pages/INDEX.md](landing-pages/INDEX.md)

---

## Export & assets

| Path | Role |
|------|------|
| [export/](export/) | Commander foundation + future hooks |
| [assets/direct-commander-template/](assets/direct-commander-template/) | Reference Excel — **not** SoT |

---

## Future implementation notes (honest)

- Structured internal model should replace Excel-native thinking before any automation  
- Validation **before** export is mandatory in doctrine — full engine **not** in repo; **Phase 7–8** human-operated CLI v0.1 ([tools/validation-cli/](tools/validation-cli/)) — self-validating report, no launch automation  
- Exporter must stay “dumb transport” — no PPC logic in export layer  
- n8n / prompts: experimental future lane — isolate from governance truth  

---

## STOP cues

- STOP when one campaign architecture decision is clear enough for human draft  
- STOP when three findings exist for a review session  
- STOP before opening every landing blueprint “just in case”  
- Mark **SAFE UNKNOWN** when live SERP/platform behavior needs human confirmation  

---

## Boundaries

This pack does **not** bid, launch, optimize, validate automatically, or orchestrate campaigns. Parent ORCA boundaries: [projects/orca/OPERATIONAL-INDEX.md](../../OPERATIONAL-INDEX.md).
