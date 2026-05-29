# ORCA Semantic Pack Generation System v1

**Status:** human-operated pipeline definition  
**Output:** production-ready structured landing content per route — **not** HTML, **not** auto-build

---

## Definition

A **production semantic pack** is the ORCA-side SoT for one landing route: marketing semantics, locks, visual semantics, and Factory hints — independent of `workspaces/triumph-manipulator-landing-v6/` implementation.

| Property | Value |
|----------|--------|
| Audience | Operator, ORCA author, Factory implementer |
| SoT under MODE 1 | Approved pack + signed handoff |
| Anti-pattern | Pack = final HTML; pack = design system spec |

**Canonical structure:** `projects/orca/content-packs/content-pack-system-v0.md` (10 sections).

**Reference implementations:**

- Master hot (draft): `content-packs/examples/triumph-manipulyator-zakaz-pack-v1/`
- Capability (template): `content-packs/examples/triumph-manipulyator-5-tonn-pack-v0.md`

---

## Pipeline stages

```text
research → intent → route differentiation → visual semantics
    → slot generation → semantic lock → production semantic pack → Factory handoff
```

Each stage is **human-reviewed**. No stage auto-approves the next.

---

### 1. Research

**Inputs:**

- PPC validated pack: `projects/orca/ppc/triumph-manipulator/`
- SERP / competitor notes (graded evidence — no copied claims)
- Calibration: `projects/orca/calibration/triumph-manipulator/`
- Route registry: `projects/orca/projects/triumph-manipulator-krasnodar/landing-route-registry.json`

**Outputs:**

- Intent tier confirmation (master / capability / use-case / B2B / geo)
- Evidence gaps → `SAFE UNKNOWN` entries (must not be invented in slots)
- Blueprint pointer: `landing-pages/0N-*.md`

**Gate:** research informs pack; does not unlock Factory alone.

---

### 2. Intent

**Actions:**

- Map `group_id` + ads slice from campaign instance JSON
- Set `page_intent` / `landing_type` (e.g. `use_case_bytovka`, `capability_5t`)
- Define primary ad variant for H1 continuity (`primary_ad_variant`)
- Document negative space (anti-junk, anti-evacuation, anti-fleet)

**Outputs:**

- `ppc/intent-continuity.md` in pack
- `ppc/ad-alignment.md` — H1 ↔ headline table

**Gate:** intent must match blueprint PAGE PURPOSE — no merging routes.

---

### 3. Route differentiation

**Actions:**

- Derive route-specific H1, lead, tasks, denied tasks from blueprint — **not** zakaz copy-paste
- Set machine locks (5/3/14 for standard KMU; 6×6 for vezdehod; B2B fields for yurlic)
- Set FAQ strategy from blueprint FAQ block
- Set trust emphasis (operational vs documents vs geo)

**Outputs:**

- Differentiation table in pack README
- `calibration/productive-drift.md` — what may vary vs zakaz baseline

**Anti-pattern:** Copy master hot H1 «Аренда» onto capability pages (see `visual-semantics/next-evolution/scaling-rules-for-11-pages-v2.md`).

---

### 4. Visual semantics

**Actions:**

- Author `visual-semantics/*.md` or YAML bundle per route
- Set `hero_layout_mode`, `visual_density`, `trust_mode`, `cta_priority`, `cargo_cards_max`
- Set `frontend_priority[]` — section scan order for Factory
- Set `mobile_critical[]` per `visual-semantics/mobile-criticality-rules-v0.md`

**Outputs:**

- Bundle aligned to [visual-semantic-injection-rules-v1.md](visual-semantic-injection-rules-v1.md)
- Example canonical: `visual-semantics/examples/triumph-zakaz-hero-visual-semantics-v1.md`

**Rule:** Visual semantics ≠ CSS generation. They constrain **what** appears **where**, not token values.

---

### 5. Slot generation

**Actions:**

- Fill 10 canonical sections (`hero` … `final_cta`) under `content/`
- Mark copy locks with 🔒 in tables
- Link each slot to V6 partial path in `factory/frontend-hints.md`
- Encode denied tasks and pricing framing in dedicated slots

**Outputs:**

- `content/hero.md`, `content/specs.md`, `content/tasks.md`, …
- `factory/implementation-priority.md` — P0–P4 if needed

**Density:** apply [semantic-density-control-v1.md](semantic-density-control-v1.md) before locking hero.

---

### 6. Semantic lock

**Actions:**

- Write `factory/semantic-lock.md` — MODE 1 activation preconditions
- Write `factory/forbidden-drift.md` + `factory/allowed-drift.md`
- Cross-check [orca-website-factory-semantic-lock-v0.md](../intelligence/orca-website-factory-semantic-lock-v0.md)
- Record `drift_acceptance.destructive: []` in visual bundle

**Outputs:**

- `semantic_lock: active` only when operator sets `approved_for_factory`
- `content_mode: MODE_1`

---

### 7. Production semantic pack

**Actions:**

- Complete [production-pack-readiness-checklist-v1.md](production-pack-readiness-checklist-v1.md)
- Set `PACK-METADATA.md` / `PACK-STATUS.md`
- Set `artifact_state: approved` (human)
- Update [remaining-routes-status-matrix-v1.md](remaining-routes-status-matrix-v1.md)

**Pack location convention:**

```text
projects/orca/content-packs/production/triumph-manipulator/<route_id>/
```

(or remain under `examples/` until operator promotes — **process choice**, not automated).

---

### 8. Factory handoff

**Actions:**

- Generate handoff from `content-packs/templates/website-factory-handoff-template-v0.md`
- Satisfy [factory-handoff-minimum-contract-v1.md](factory-handoff-minimum-contract-v1.md)
- Point workspace: `workspaces/triumph-manipulator-landing-v6/`
- Reference V6 partial paths (`v5-ppc/<slug>/`)

**Outputs:**

- `*-handoff.md` in `ppc/triumph-manipulator/handoff/` or project handoff folder
- Operator session: Factory implements **one route** per pilot gate

---

## Pack folder anatomy (normative)

```text
<pack-id>/
  PACK-METADATA.md
  PACK-STATUS.md
  APPROVALS.md
  content/           # slot copy
  ppc/               # continuity, CTA, geo
  visual-semantics/  # injection rules
  factory/           # lock, hints, forbidden drift
  calibration/       # drift class notes
  exports/           # readiness only (no auto DOCX here)
  SAFE-UNKNOWN.md
```

---

## What this system is not

| Not | Because |
|-----|---------|
| HTML generator | Factory builds from handoff |
| Orchestration | No job queue, no agent swarm |
| Commander exporter | Separate PPC tooling — out of scope |
| Auto-approval | Human gates on every promotion |

---

## Triumph v6 alignment

| Item | Rule |
|------|------|
| Structure | Clone zakaz **section order** from `V6-ACTIVE-STRUCTURE-MAP.md` |
| Partials | `v5-ppc/<slug>/` + shared `v5-page01/*` |
| Baseline page | `src/pages/index.html` (zakaz) — new routes get own `src/pages/...` when chartered |
| Scaffold | V6 already contains partial folders for 11 slugs — **content** swap only after pack |

---

## Related

- [route-pack-generation-rules-v1.md](route-pack-generation-rules-v1.md)
- [orca-factory-coordination-protocol-v1.md](orca-factory-coordination-protocol-v1.md)
