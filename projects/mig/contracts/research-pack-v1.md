# MIG Research Pack v1 — Makita Pilot Contract

**Status:** **documented** — minimum handoff contract for first commercial MIG → ORCA validation.  
**Pilot target:** Makita.  
**Not:** universal framework, schema, API, automation, governance, or v2 design.

**Upstream:** Research Session (validated MIG MVP layers).  
**Downstream:** ORCA campaign architecture intake (human handoff only).  
**Semantic authority (detail):** [mig-research-pack-contract-v0.md](mig-research-pack-contract-v0.md) · [mig-orca-handoff-contract-v0.md](mig-orca-handoff-contract-v0.md)

---

## 1. Purpose

**Why Research Pack exists**

Research Pack is the **single approved groundtruth product** from a Makita Research Session. It bundles what MIG observed about the market — nothing more.

**Problem it solves**

Without it, ORCA would either re-capture market reality (duplicate work, boundary violation) or build campaign architecture from informal notes (interpretation without evidence discipline).

**Why ORCA consumes it**

ORCA owns interpretation — semantic clustering, route families, ad groups, PPC exports. Campaign architecture **starts from** approved observations, not from raw session folders or draft artifacts. Research Pack is the intake unit ORCA reads after human **Approved By**.

```text
Makita Research Session → Research Pack (approved) → ORCA Intake → Campaign Architecture
```

---

## 2. Minimum Content Model

Sections below map to **validated MIG outputs** only. Each section carries **facts, evidence, or observations** — not strategy.

### Required

| Section | MIG source | Minimum content |
|---------|------------|-----------------|
| **Session identity** | Session manifest | `session_id`, capture date, operator, `mig_phase` |
| **Scope** | Research Request / manifest | Niche, region, city (if applicable), search engine, device |
| **Query set** | Multi-query discovery | Seed queries, executed queries, coverage notes (including failed/missing queries) |
| **Market Surface** | SERP + competitor discovery | SERP summary (organic, ads, aggregators, marketplaces); competitor list with domains and recurrence; cross-query domain frequency |
| **Evidence discipline** | Session grades | Session-level evidence grade; per-section grade where section is present |
| **SAFE UNKNOWN** | Manifest + capture gaps | Explicit gaps — never empty when any section is partial or absent |
| **Artifact pointers** | Session folder | Paths to `session_manifest.json`, `serp_result.json` (or `serp_index.json`), competitor artifacts, snapshots |
| **Human Review Gate** | Operator sign-off | **Approved By** (human id) + approval date — mandatory before ORCA intake |

### Optional (recommended for Makita campaign architecture)

| Section | MIG source | When to include |
|---------|------------|-----------------|
| **Website Intelligence** | Website acquisition pass | When competitor domains were fetched — record success/timeout per domain |
| **Landing Intelligence v2** | Landing analysis pass | Per shortlist domain: offers, pricing signals, delivery promise, trust, CTA, contact model, page structure |
| **Comparison Matrix** | Market-leader matrix | Facts-only side-by-side of shortlist domains — speeds ORCA competitive read |
| **Demand Surface** | Manual Wordstat pass | When `keyword_pass: true` — phrase list with frequency evidence as captured |
| **Keyword Registry** | Keyword pass | Registered demand phrases with provider refs — complements query set for volume-aware architecture |
| **Client site observation** | Landing pass on client URL | When Makita client site is in scope — one landing card + `atlas_website_ref` pointer |

### Out of scope (must not appear in Research Pack)

| Item | Owner |
|------|-------|
| Campaign structure, ad groups, route families | ORCA |
| Semantic clustering, intent tiers, negative keyword strategy | ORCA |
| Bids, budgets, match types, PPC strategy | ORCA |
| Commander / platform export artifacts | ORCA |
| Deep Research synthesis memos | Not in v1 pilot |
| ATLAS entity creation or org-graph restatement | ATLAS |
| Competitor → `ORG-*` promotion | ATLAS attest path — not pack content |

**v1 pilot floor:** A pack with **Required** sections only is valid for ORCA intake. **Optional** sections improve campaign architecture quality but are not blocking for the first Makita handoff test.

---

## 3. Groundtruth Boundary

### Research Pack may contain

- Facts observed at capture time (SERP rows, visible prices, CTA labels)
- Evidence pointers (snapshot paths, artifact refs, capture timestamps)
- Operator observations and market findings (competitor recurrence, aggregator pressure)
- Demand findings (Wordstat rows as exported — no prioritization)
- Keyword findings (registered phrases — no clusters)
- Explicit **SAFE UNKNOWN** entries

### Research Pack must not contain

- Campaign structure
- Ad groups or route families
- Semantic clustering or intent labels
- Bids or PPC strategy
- Export artifacts (XLSX, Commander packages)
- ORCA methodology outputs
- Interpretive conclusions («market leader», «best opportunity», «target segment»)

**Rule:** If it answers *what we should run in ads*, it belongs to ORCA — not the pack.

---

## 4. ATLAS Binding

Research Pack carries **references only**. No ownership transfer. No synchronization. No registry creation.

### Minimum RC-01 references (when Makita is attested in ATLAS)

| Field | Required when | Meaning |
|-------|---------------|---------|
| `atlas_client_org_ref` | Client org attested | Primary subject anchor (`ORG-*`) |
| `atlas_project_ref` | PPC initiative attested | Structural project the research serves (`PRJ-*`) |

### Optional RC-01 references

| Field | When |
|-------|------|
| `atlas_website_ref` | Session scoped to Makita client site (`WEB-*`) |
| `atlas_domain_ref` | Hostname identity matters independently (`DOM-*`) |

### Rules

- Use full ATLAS id strings — not brand slugs or domains alone.
- Do not restate legal name, INN, or org graph in the pack.
- If Makita has **no** attested ATLAS ids yet → record **SAFE UNKNOWN** in ATLAS context block; do not invent ids.
- `session_id` / `pack_id` remain **MIG-owned**; ORCA `project_id` remains **ORCA-owned** — never alias to `PRJ-*`.

**Placement:** Pack front matter or operator bind note (human-maintained). Manifest may mirror refs; manifest is not the binding SoT.

---

## 5. ORCA Consumption Test

**Question:** Can ORCA begin campaign architecture work using only this Research Pack?

**Answer:** **Yes** — when all **Required** sections are present, **Approved By** is recorded, and ATLAS refs are set or explicitly marked SAFE UNKNOWN.

ORCA can then:

1. Define Search campaign mode scope from **Scope** + **Query set**.
2. Map competitive landscape from **Market Surface** + optional **Landing Intelligence**.
3. Draft intent-tier hypotheses (ORCA-owned) grounded in observed offers/CTAs/pricing — not pack content.
4. Preserve **SAFE UNKNOWN** through architecture — flag gaps that block export decisions.

### Not blocking (ORCA may proceed with gaps declared)

- Partial query coverage (missing queries listed in SAFE UNKNOWN)
- Absent Keyword Registry (architecture proceeds from query set; volume assumptions marked SAFE UNKNOWN)
- Single-domain acquisition failures (competitor row = SAFE UNKNOWN)
- Absent Comparison Matrix (landing cards in pack suffice)

### Would block ORCA intake

| Missing item | Why |
|--------------|-----|
| **Approved By** | Handoff contract hard gate |
| **Scope** (region, niche) | Cannot bound campaign geography or vertical |
| **Query set** (seed list) | No observation triggers for architecture |
| **Market Surface** (SERP + competitors) | No supply-side groundtruth |
| **SAFE UNKNOWN** (when gaps exist) | Silent omission violates handoff discipline |
| **Evidence grade** | ORCA cannot calibrate trust in observations |

---

## 6. Makita Pilot Readiness

**Verdict:** **PARTIAL**

| Ready | Not ready |
|-------|-----------|
| Contract defines minimum handoff | Makita **not registered** in ATLAS (no `ORG-*` / `PRJ-*` in repo) |
| Validated MIG layers exist on reference market (Triumph / Краснодар) | **No Makita Research Session** executed |
| Draft pack generation proven | **No `research_pack.approved.md`** in evidence — approval workflow not exercised |
| ORCA handoff minimum fields mapped | Demand Surface / Keyword Registry **not yet observed** with `keyword_pass: true` on any session |
| Makita LRL pilot docs exist (separate track) | Makita ORCA project folder may not exist |

**Reasoning:** The **contract** is sufficient to charter the first Makita commercial handoff. **Execution** is blocked until: (1) Makita ATLAS registration, (2) Makita Research Session with human approval, (3) operator-delivered approved pack bundle.

**Expected sequence:**

```text
Makita Registration in ATLAS
  → Makita Research Session
  → First Research Pack (approved)
  → ORCA Intake
  → Campaign Architecture
```

---

## Handoff bundle (operator checklist)

Human-delivered folder or zip — no mandated transport:

1. `research_pack.approved.md` (or approved export satisfying §2 Required)
2. `session_manifest.json` with approval recorded
3. Referenced artifacts: SERP, competitors, snapshots (as applicable)
4. ATLAS context block with RC-01 refs or SAFE UNKNOWN
5. Optional: comparison matrix, keyword registry files — if produced

ORCA **rejects** draft or review packs for production campaign architecture.

---

## Related

| Document | Role |
|----------|------|
| [mig-research-pack-contract-v0.md](mig-research-pack-contract-v0.md) | Full domain object semantics |
| [mig-orca-handoff-contract-v0.md](mig-orca-handoff-contract-v0.md) | ORCA minimum fields |
| [groundtruth-ownership-rule-v1.md](../../../shared/contracts/groundtruth-ownership-rule-v1.md) | MIG / ORCA boundary |
| [atlas-context-binding-rule-v1.md](../../../shared/contracts/atlas-context-binding-rule-v1.md) | RC-01 binding discipline |
| [MIG-MVP-VALIDATION-FREEZE-v1.md](../reports/MIG-MVP-VALIDATION-FREEZE-v1.md) | Proven layers evidence |
| [makita-lrl-pilot-v1.md](../../orca/pilots/makita-lrl-pilot-v1.md) | Related ORCA pilot (LRL — not a substitute for MIG handoff) |

---

*Research Pack v1 · Makita Pilot Contract · documentation only · no commit by default*
