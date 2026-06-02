# ORCA Landing Readiness Layer v1

## Status

**ARCHITECTURE FOUNDATION** — documentation only (2026-05-30).

Approved after Triumph Search Battle v1, Commander import PASS, ORCA operational audit, and ORCA ↔ Website Factory review.

**Not** runtime. **Not** automation. **Not** a Website Factory dependency. **Not** launch approval.

## Purpose

Define the **Landing Readiness Layer (LRL)** — a source-agnostic operational domain inside ORCA that answers one question before PPC and launch work:

> Is there a **verified, deployable landing** whose **live copy and URLs** are ready to align with ads?

LRL sits between semantic preparation and PPC transport. It does not replace Research or Semantic layers. It does not implement pages.

---

## Problem Statement

Before Triumph Search Battle v1, ORCA treated **semantic packs** and **Factory handoff** as sufficient preconditions for PPC export. Battle proved a gap:

| Assumption | Battle reality |
|------------|----------------|
| Approved semantic pack = landing truth for ads | Deployed page copy often differs after Factory layout, visual semantics, and frontend constraints |
| Website Factory is the only landing path | Many clients already have live sites — ORCA must operate without Factory |
| URL registry sync once = stable | Every deployment can change paths, slugs, or hero copy |
| PPC JSON can derive from semantic intent alone | Ad ↔ landing continuity requires **approved deployed copy**, not draft semantics |

**Core failure mode:** PPC exported against semantic intent while clicks land on pages whose hero, CTA, or URL no longer match — breaking qualification and wasting import cycles.

---

## Battle Lessons (Triumph Search v1)

Source: [freeze/battle-pilot-triumph-search-v1/ORCA-LESSONS-LEARNED-v1.md](../freeze/battle-pilot-triumph-search-v1/ORCA-LESSONS-LEARNED-v1.md)

1. **Semantic pack ≠ final landing copy** — semantic preparation defines intent, positioning, qualification, and Factory constraints; it is not the deployed page.
2. **Final copy vs deployed page gate was implicit** — battle flagged this as P0; LRL formalizes it.
3. **164 URL replacements** — registry, PPC JSON, and exporter mapping must stay aligned; URL truth belongs in Landing Readiness, not exporter-only edits.
4. **Factory can ship while PPC calibrates** — implementation and ad transport are parallel tracks; LRL is the reconciliation layer.
5. **Export READY ≠ Launch READY** — landing readiness is a separate gate from Commander import structural PASS.

**Mandatory rule from battle:**

> Semantic pack → (optional Factory / existing site) → **Final Website Copy Pack** → Landing Ready Contract → PPC JSON generation.

No PPC export should treat semantic pack alone as landing SoT.

---

## Why LRL Exists

ORCA produces strong **semantic authority** (intent tiers, route differentiation, trust mode, CTA hierarchy). That authority is necessary but **insufficient** for PPC and launch because:

- Landing pages may come from **many sources**, not only Website Factory.
- **Deployed reality** (live URL, live hero, live forms) is the click destination — not the pack file.
- PPC alignment requires a **human-verified contract** that binds URL, copy, CTA, and ad continuity in one place.

LRL provides that contract layer without coupling ORCA to any single build pipeline.

---

## Architecture Position

### ORCA domain model (v1)

```text
ORCA
├─ Research          — evidence, SERP, competitors, market pressure
├─ Semantic          — intent, packs, route strategy, semantic locks
├─ Landing Readiness — deployed landing truth, URL/copy/CTA verification
├─ PPC               — JSON, export, Commander transport, validation
└─ Launch            — post-import settings, tracking, operator sign-off
```

### LRL boundaries

| LRL owns | LRL does not own |
|----------|------------------|
| Landing Ready Contract (human-readable) | HTML, SCSS, build pipelines |
| Final Website Copy Pack approval gate | Semantic pack authoring |
| Source-agnostic landing provenance | Commander XLSX transport |
| Readiness status before PPC cites landing | Automated crawlers or runtime checks |
| URL/copy/CTA alignment evidence expectations | Website Factory implementation |

### Position in workflow

```text
Research → Semantic (pack / brief)
              ↓
         [landing source: any]
              ↓
    Final Website Copy Pack (approved deployed copy)
              ↓
    Landing Ready Contract
              ↓
         PPC JSON / export
              ↓
         Launch gates
```

---

## Relationship with ORCA

LRL **extends** existing Intelligence Foundation contracts; it does not replace them.

| Existing ORCA artifact | Relationship to LRL |
|------------------------|---------------------|
| Semantic content pack | **Upstream input** — defines intent before landing exists or is captured |
| [landing-route-registry-contract-v0.md](landing-route-registry-contract-v0.md) | **URL section** of Landing Ready Contract must align with registry when registry exists |
| [ppc-landing-qa-contract-v0.md](ppc-landing-qa-contract-v0.md) | **QA evidence** feeds readiness status; LRL contract summarizes pass/fail for PPC gate |
| [orca-website-factory-semantic-lock-v0.md](orca-website-factory-semantic-lock-v0.md) | Applies when source = Website Factory; LRL verifies lock survived deployment |
| PPC JSON instance | **Downstream consumer** — must reference Landing Ready Contract, not semantic pack alone |
| [artifacts/orca-artifact-system-v0.md](../artifacts/orca-artifact-system-v0.md) | Final Website Copy Pack is a new artifact type (see [final-website-copy-pack-v1.md](final-website-copy-pack-v1.md)) |

LRL is **human-operated**. Operators capture, verify, and approve. AI may assist extraction; humans sign readiness status.

---

## Relationship with Website Factory

Website Factory is **one landing source type**, not a prerequisite for ORCA.

| Scenario | LRL behavior |
|----------|--------------|
| Factory builds from semantic pack | Semantic pack → Factory MODE 1 → deployed page → Final Website Copy Pack → Landing Ready Contract |
| Existing client website | Operator captures live copy from deployed site → Final Website Copy Pack → Landing Ready Contract |
| Factory not used | Full LRL path still applies; Factory handoff steps are **skipped**, not replaced |
| Factory and live site diverge | Landing Ready Contract reflects **deployed** truth; semantic pack is traceability only |

**Explicit statement:**

> **Website Factory is not required.** ORCA may operate entirely with existing client websites, existing landing pages, WordPress, Tilda, manual HTML, or future WPilot-managed sites. Factory coordination docs remain valid **when** Factory is the chosen source — they are not universal ORCA dependencies.

Factory retains **implementation authority** when engaged. LRL retains **readiness authority** regardless of source.

---

## Source-Agnostic Philosophy

Supported landing sources (v1 vocabulary — detailed taxonomy deferred post-pilot):

| Source type | Description |
|-------------|-------------|
| `website_factory` | ORCA semantic pack → Website Factory build |
| `existing_client_website` | Client-owned site already live |
| `existing_landing_page` | Standalone landing URL not full site |
| `wordpress` | WordPress-managed site or page |
| `wpilot` | WPilot-managed site (**future** — treat as SAFE UNKNOWN until pilot confirms) |
| `tilda` | Tilda-published page |
| `manual_html` | Hand-maintained HTML project |

**Principle:** LRL cares about **what the user clicks to**, not **how it was built**.

Each Landing Ready Contract records `landing_source` in provenance. Source type determines **capture method** (Factory QA vs manual page review), not **contract shape**.

---

## Key Artifacts (this layer)

| Doc | Role |
|-----|------|
| [landing-ready-contract-v1.md](landing-ready-contract-v1.md) | Human-readable contract — URL, copy, CTA, PPC alignment, readiness status |
| [final-website-copy-pack-v1.md](final-website-copy-pack-v1.md) | Approved deployed copy artifact — gate between semantic and PPC |

Deferred until post-pilot validation: source-type registry doc, approval-gates expansion, triumph migration spec, JSON schemas, examples, automation specs.

---

## Future Evolution Notes

Post–Makita pilot (existing client website), consider **only if evidence supports**:

- Formal `landing_source` taxonomy doc
- Approval gate checklist dedicated to LRL
- Triumph route migration from implicit to explicit Landing Ready Contracts
- Machine-readable schema (optional — human contract remains SoT)
- Helper scripts for copy capture (human-invoked, not autonomous)

**Do not expand architecture before first pilot validates:**

- `landing_source = existing_client_website`
- One Landing Ready Contract end-to-end
- One Final Website Copy Pack approved against live site
- PPC JSON cites contract, not semantic pack alone

---

## SAFE UNKNOWN

- Automated copy diff (semantic pack vs live page) — not defined in v1
- Mobile performance / form E2E — separate Factory or operator QA; may remain UNKNOWN at LRL gate
- WPilot integration semantics — future source; no contract assumptions
- Multi-route family batch readiness — Triumph-scale patterns deferred

---

## Related Documents

- [ORCA-LESSONS-LEARNED-v1.md](../freeze/battle-pilot-triumph-search-v1/ORCA-LESSONS-LEARNED-v1.md) — battle source
- [landing-ready-contract-v1.md](landing-ready-contract-v1.md) — contract definition
- [final-website-copy-pack-v1.md](final-website-copy-pack-v1.md) — copy pack artifact
- [orca-factory-bridge-index-v0.md](orca-factory-bridge-index-v0.md) — Factory path when source = `website_factory`
- [OPERATIONAL-INDEX.md](../OPERATIONAL-INDEX.md) — ORCA entry point

## Boundary

Documentation-only architecture foundation. **No** runtime, **no** automation, **no** exporter or validation-cli changes in this package.
