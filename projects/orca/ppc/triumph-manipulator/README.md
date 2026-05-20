# ORCA Triumph Manipulator — PPC operational pack

**Pack role:** Normalized operational knowledge for **Triumph Manipulator** (Krasnodar, local manipulator / crane-truck service) inside the ORCA PPC lane.  
**Status:** Documentation-first · Phase 2–6 (schema, JSON, validation, exporter, prompts foundations) · **search-only** · human-supervised.  
**Maturity:** Ingested and structured from raw pack (`incoming/orca-triumph-raw-pack/`); **Phase 7–8** adds a hardened local validation CLI (v0.1) only — **no** validator service, exporter runtime, or orchestration in-repo.

Start navigation: **[OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md)**.

---

## What this pack is

A **stable operational subsystem pack** for AI-assisted PPC production on Yandex Search:

- PPC doctrine (intent purity, anti-garbage, Yandex bold-highlight, mobile-first)
- Intent tier research (S / A / B / X)
- Landing page blueprints aligned to intent types (master, use-case, capability, B2B, intercity)
- Direct Commander export **foundation** (entity model, validation-before-export, transport vs SoT)
- Reference Commander Excel template (transport schema only)

ORCA here means: **structure → segment → validate (human) → prepare export → human launch** — not autonomous advertising.

---

## What ORCA PPC does (in this pack)

- Teaches **how to think** in search intent architecture before keywords/headlines
- Defines **one group = one semantic intent**
- Maps **landing continuation** (ad intent → page intent)
- Prioritizes **exact-fit** segments (capability, use-case, B2B) over broad “аренда манипулятора” noise
- Documents **Yandex-specific** relevance behavior (phrase in headline/description, bold highlighting psychology)
- Prepares **implementation-ready** documentation hooks (JSON entities, validation, exporter, prompts, n8n) **without** building them

---

## What this pack is NOT

- Not an autonomous advertiser, auto-launcher, or self-optimizing runtime
- Not a bidding engine, budget optimizer, or campaign manager product
- Not proof that validation/export/n8n **exists** in MARS — only documented targets
- Not RSYA / Master Campaigns / retargeting architecture (current scope: **search only**)
- Not governance expansion for MARS v2 — local operational pack only
- Not Website Factory implementation — related by **landing handoff**, not merged SoT

**Human remains final authority:** review, edit, import, launch.

---

## Current operational status

| Area | Status |
|------|--------|
| Doctrine & architecture docs | **Present** (normalized) |
| Intent research | **Present** |
| Landing blueprints | **Present** (12 pages + master) |
| Commander template asset | **Present** (reference transport) |
| Structured entity schema (markdown v1) | **Present** — [`schema/`](schema/) |
| JSON Schema + draft instances (v1) | **Present** — [`schema/json/`](schema/json/), [`schema/instances/`](schema/instances/) |
| Validation engine | **Foundation documented** (Phase 4) — [`validation/`](validation/) · **CLI v0.1** (Phase 7–8) — [`tools/validation-cli/`](tools/validation-cli/) · **not** a service |
| Exporter engine | **Foundation documented** (Phase 5) — [`exporter/`](exporter/) · **CLI prototype v0** (Phase 9) — [`tools/exporter-cli/`](tools/exporter-cli/) · transport-only · **not** production/Direct API |
| Prompt system | **Foundation documented** (Phase 6) — [`prompts/`](prompts/) · **no runtime** |
| Validation CLI (local) | **Hardened v0.1** (Phase 7–8) — [`tools/validation-cli/`](tools/validation-cli/) · dual schema AJV · golden fixture |
| n8n workflows | **Not implemented** — documented target only (Phase 9+) |

---

## Relationship to MARS

- Lives under **`projects/orca/ppc/triumph-manipulator/`** as an ORCA **project operational pack**
- Complements parent ORCA toolkit: [`projects/orca/README.md`](../../README.md), [`projects/orca/OPERATIONAL-INDEX.md`](../../OPERATIONAL-INDEX.md)
- Follows MARS Phase 1 honesty: [AGENTS.md](../../../../AGENTS.md) — documentation ≠ runtime
- Post–Cycle 8: operational-first; no new governance waves from this pack

---

## Relationship to Website Factory

- Landing blueprints here are **PPC qualification systems** (intent-specific, mobile-first, anti-junk) — inputs for future Factory pages, not Factory SoT
- When Factory builds pages, **intent continuation** and **exact-fit heroes** from this pack should drive acceptance checks
- Factory operational index: [`projects/mars-website-factory/OPERATIONAL-INDEX.md`](../../../mars-website-factory/OPERATIONAL-INDEX.md) — use only when doing cross-lane landing work

---

## Relationship to future exporter / validator

Documented pipeline (target, not built):

1. Internal structured PPC model (campaign → group → keywords → ads → landing route)
2. **Validation before export** (symbols, intent purity, continuation, anti-generic)
3. **Dumb export layer** → Commander Excel (transport only)

See [`exporter/exporter-engine-overview-v1.md`](exporter/exporter-engine-overview-v1.md), [`export/direct-commander-foundation-v0.md`](export/direct-commander-foundation-v0.md), and [`export/future-implementation-hooks-v0.md`](export/future-implementation-hooks-v0.md).

Excel template: [`assets/direct-commander-template/`](assets/direct-commander-template/) — **reference asset**, not source-of-truth.

---

## Search-only scope (current)

In scope: Yandex **Search** campaigns — deterministic intent, validation-friendly training surface.  
Out of scope (for now): RSYA, Master Campaigns, retargeting, autotargeting architecture, performance campaign types.

---

## Future implementation path (documentation hooks only)

| Phase | Focus | Pack status |
|-------|--------|-------------|
| 1 | Doctrine + architecture | **Done** |
| 2 | Entity schema foundation | **Done** — [`schema/`](schema/) |
| 3 | JSON Schema contract | **Done** — [`schema/json/`](schema/json/) |
| 4 | Validation engine foundation | **Done** — [`validation/`](validation/) · no runtime |
| 5 | Exporter engine foundation | **Done** — [`exporter/`](exporter/) · no runtime |
| 6 | Prompt system foundation | **Done** — [`prompts/`](prompts/) · no runtime |
| 7 | Validation CLI prototype (local) | **Done** — initial prototype |
| 8 | Validation CLI hardening v0.1 | **Done** — [`tools/validation-cli/`](tools/validation-cli/) |
| 9 | Exporter CLI prototype v0 | **Done** — [`tools/exporter-cli/`](tools/exporter-cli/) — local transport draft only |
| 10 | n8n workflows | Documented hook |
| 11 | MARS / Factory integration | Documented hook |

Details: [`export/future-implementation-hooks-v0.md`](export/future-implementation-hooks-v0.md).

---

## Source lineage

Ingested from `incoming/orca-triumph-raw-pack/` (2026-05-20 normalization). Raw folder unchanged; this tree is the **operational normalized** copy.

---

## Quick start

1. Read [`OPERATIONAL-INDEX.md`](OPERATIONAL-INDEX.md) — Core Run row for your task  
2. Doctrine: [`doctrine/generation-logic-v0.md`](doctrine/generation-logic-v0.md)  
3. Intent tiers: [`research/intent-groups-v1.md`](research/intent-groups-v1.md)  
4. Pick landing blueprint from [`landing-pages/INDEX.md`](landing-pages/INDEX.md)  
5. Export rules: [`export/direct-commander-foundation-v0.md`](export/direct-commander-foundation-v0.md)  
6. Human review → Commander import (manual)
