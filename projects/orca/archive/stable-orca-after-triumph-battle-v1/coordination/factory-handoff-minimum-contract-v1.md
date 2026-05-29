# Factory Handoff Minimum Contract v1

**Purpose:** minimum payload Website Factory **must** receive before MODE 1 implementation in V6  
**Extends:** [website-factory-handoff-template-v0.md](../content-packs/templates/website-factory-handoff-template-v0.md) — this file is the **required field set**, not full template prose  
**Not:** an API schema or runtime validator

---

## Delivery form

| Form | Requirement |
|------|-------------|
| **Handoff MD** | Human-authored `*-handoff.md` with sections below |
| **Source pack** | Linked folder or monolithic pack MD — paths explicit |
| **MODE** | `content_mode: MODE_1` |
| **Lock** | `semantic_lock: active` + `approved_for_factory: true` |

Factory session reads handoff + pack + [orca-website-factory-semantic-lock-v0.md](../intelligence/orca-website-factory-semantic-lock-v0.md) + `TRIUMPH-V6-CURRENT-FRONTEND-RULES.md`.

---

## Required fields (minimum)

### Traceability

| Field | Required | Notes |
|-------|----------|-------|
| `handoff_id` | yes | Unique per issuance |
| `handoff_version` | yes | Bump on semantic change |
| `date` | yes | ISO date |
| `source_pack_id` | yes | |
| `source_pack_path` | yes | Repo-relative |
| `route_id` | yes | Registry ID |
| `workspace` | yes | `workspaces/triumph-manipulator-landing-v6/` |
| `approved_for_factory` | yes — **must be true** | Human gate |

---

### Page identity

| Field | Required | Notes |
|-------|----------|-------|
| `route_id` | yes | e.g. `manipulyator-5-tonn` |
| `canonical_url` | yes | Full URL |
| `page_slug` / HTML path | yes | e.g. `src/pages/manipulyator-5-tonn/index.html` or charter |
| `data-page-type` | yes | PPC marker for QA |
| `blueprint_path` | yes | `landing-pages/0N-*.md` |

---

### Hero block

| Field | Required | Notes |
|-------|----------|-------|
| `H1` | yes | Locked RU string 🔒 |
| `hero_lead` | yes | Subhead / lead paragraph |
| `hero_specs` | yes | Ordered list (борт, стрела, вылет, …) |
| `hero_proof` | yes | Items for `hero__lower` strip — or explicit «none» |
| `hero_cargo` | yes | Card list with labels + micro-CTA intent; respect `cargo_cards_max` |

---

### Tasks and qualification

| Field | Required | Notes |
|-------|----------|-------|
| `tasks` | yes | Allowed tasks section copy / structure |
| `denied_tasks` | yes | Anti-junk, anti-evacuation, route denials |
| `qualification_line` | conditional | Required when pack sets `qualification_line_required` |

---

### Pricing

| Field | Required | Notes |
|-------|----------|-------|
| `pricing_framing` | yes | Factors, min order, «по задаче» — **no fake hero rate** |
| `pricing_section_ref` | yes | Pack `content/pricing.md` anchor |

---

### FAQ

| Field | Required | Notes |
|-------|----------|-------|
| `FAQ` | yes | Full Q&A pairs or pack link with 🔒 |
| `faq_strategy` | recommended | Objection focus note for Factory QA |

---

### CTA and trust

| Field | Required | Notes |
|-------|----------|-------|
| `CTA_hierarchy` | yes | Primary / secondary; form vs call; exact labels |
| `trust_mode` | yes | e.g. `operational_proof` |
| `proof_mode` | yes | Hero strip vs section-only |
| `trust_section_ref` | yes | Reviews / sources |

---

### Visual semantics

| Field | Required | Notes |
|-------|----------|-------|
| `visual_semantics` | yes | Full YAML bundle or `visual-semantics/` folder path |
| Key fields inside bundle | yes | `hero_layout_mode`, `visual_density`, `cargo_cards_max`, `frontend_priority`, `mobile_critical` |

See [visual-semantic-injection-rules-v1.md](visual-semantic-injection-rules-v1.md).

---

### Semantic locks

| Field | Required | Notes |
|-------|----------|-------|
| `semantic_locks` | yes | Reference `factory/semantic-lock.md` + `forbidden-drift.md` |
| `claims_forbidden[]` | yes | Minimum: fleet, fake price, invented metrics |
| `drift_acceptance.destructive` | yes | Must be empty or explicitly waived |
| `SAFE_UNKNOWN[]` | yes | Factory must not invent |

---

### Factory implementation hints

| Field | Required | Notes |
|-------|----------|-------|
| `factory_hints.partial_paths` | yes | Map `section_id` → `v5-ppc/<slug>/…` |
| `shared_partials` | yes | `v5-page01/*` list |
| `form_ids` | yes | Unique per route per V6 rules |

---

## Optional but recommended

| Field | Purpose |
|-------|---------|
| `primary_ad_variant` | H1 continuity |
| `screenshot_refs` | Calibration only — not SoT |
| `ppc_qa_checklist` | Pre-filled continuity checks |
| `previous_handoff_id` | When bumping version |

---

## Minimum JSON-shaped summary (illustrative)

Handoff may include a machine-readable block for operator tools — **not** consumed by runtime in repo:

```yaml
handoff_minimum:
  route_id: manipulyator-5-tonn
  H1: "…"
  hero_lead: "…"
  hero_specs: ["…", "…"]
  hero_proof: ["…"]
  hero_cargo: [{ title: "…", cta_intent: "…" }]
  tasks: { … }
  denied_tasks: ["…"]
  pricing_framing: { mode: by_task, … }
  FAQ: [{ q: "…", a: "…" }]
  CTA_hierarchy: { primary: form, labels: { … } }
  trust_mode: operational_proof
  proof_mode: hero_strip
  visual_semantics: { path: "…/visual-semantics/" }
  semantic_locks: { path: "…/factory/semantic-lock.md" }
```

---

## Rejection criteria (Factory must STOP)

| Condition | Action |
|-----------|--------|
| Missing `denied_tasks` | Request pack fix |
| Missing `visual_semantics` | Request pack fix |
| `approved_for_factory: false` | MODE 2 only or halt |
| Destructive drift class open | Escalate operator |
| Handoff contradicts pack | Pack wins — fix handoff |

---

## Triumph reference handoffs

| Route | Path |
|-------|------|
| 5-tonn (v5-era) | `projects/orca/ppc/triumph-manipulator/handoff/triumph-manipulator-v5-page-01-manipulyator-5-tonn-handoff.md` |
| zakaz (to author) | Pattern above + `triumph-manipulyator-zakaz-pack-v1` |

**Action:** clone 5-ton handoff structure; update all paths to V6 workspace and partials.

---

## Related

- [production-pack-readiness-checklist-v1.md](production-pack-readiness-checklist-v1.md)
- [orca-factory-coordination-protocol-v1.md](orca-factory-coordination-protocol-v1.md)
- [pack-to-factory-workflow-v0.md](../content-packs/workflows/pack-to-factory-workflow-v0.md)
