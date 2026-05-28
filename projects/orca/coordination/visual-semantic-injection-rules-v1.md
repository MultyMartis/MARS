# Visual Semantic Injection Rules v1

**Purpose:** define how ORCA visual semantics reach Website Factory **without CSS generation**  
**Canonical example:** `projects/orca/visual-semantics/examples/triumph-zakaz-hero-visual-semantics-v1.md`  
**Contract:** visual semantics constrain **content placement and priority**; Factory SCSS implements within V6 rules

---

## Core principle

```text
ORCA visual semantics  →  slot priorities + copy structure + Factory hints
                              ↓
Factory HTML partials  →  existing BEM / section markers
                              ↓
Factory SCSS           →  spacing, responsive, polish (no new semantic claims)
```

**Forbidden path:** ORCA generating CSS, token files, or autopatching `_v5-hero-extensions.scss` as «semantic delivery».

---

## Injection channels

### 1. Slot priorities (`frontend_priority`)

Ordered list in `visual_semantics.fields.frontend_priority`:

| Priority position | Factory behavior |
|-------------------|------------------|
| First items | Must remain above fold on desktop where physically possible |
| `hero_main` before `hero_aside` | Content column before form when stacked |
| `trust_reviews` after `pricing_factors` | Do not reorder sections without pack bump |

**Injection:** `factory/implementation-priority.md` maps P0–P4 to partials.

---

### 2. Hierarchy (scan path)

| Field | Injects into |
|-------|----------------|
| `hero_priority` | H1 → lead → specs before proof/cargo |
| `cta_priority` | Form-aside vs call-link prominence |
| `proof_priority` | Hero strip vs deferred trust section |
| `cta_weight` | Primary button vs secondary cargo micro-CTAs |

**Factory rule:** Do not add competing H2 above H1 zone. Do not insert rate block above specs (v4 destructive pattern).

---

### 3. CTA ordering

| Field | HTML manifestation |
|-------|---------------------|
| `cta_priority: form` | Hero aside form = primary conversion surface |
| `cta_priority: call` | Early `tel:` in header / hero — document in `mobile_critical` |
| `cta_surface_priority[]` | Order of buttons in FAQ aside, modal triggers |

**Injection:** locked labels in `content/hero.md` + `ppc/cta-alignment.md` — Factory uses exact strings.

---

### 4. Proof placement

| `trust_mode` | Placement |
|--------------|-----------|
| `operational_proof` | `hero__lower` strip — ops facts, not fake ★ |
| `social_proof` | Primarily `screen-03-trust-reviews.html` |
| `deferred` | No hero stars; reviews section only |

**Injection:** which proof **lines** appear in `hero.md` vs `trust.md` — not CSS stars.

---

### 5. Density control

| Field | Injection |
|-------|-----------|
| `visual_density` | Caps for simultaneous elements — see [semantic-density-control-v1.md](semantic-density-control-v1.md) |
| `cargo_cards_max` | Number of `hero__cargo-action` cards in partial |
| `compactness_level` | Spec list vs paragraph features |

**Factory:** may hide cards on mobile per pack — **not** delete denied-task semantics.

---

### 6. Cargo limits

| Rule | Injection |
|------|-----------|
| `cargo_cards[]` in pack | Card titles + micro-CTA labels — ordered |
| Use-case routes | Replace zakaz 6-card generic list with route-specific 4–5 |
| Capability routes | Tasks echo specs — no unrelated cargo types |

**Partial:** `screen-01-hero.html` lower band + `screen-02-tasks.html`.

---

### 7. Hero zoning

| `hero_layout_mode` | Structure |
|--------------------|-----------|
| `grid_form_aside` | `.hero__main` + `.hero__aside` (form) |
| `hero__lower` | Proof strip + cargo block — **separate scan phase** |

**Why zoning matters:** v4 failed because all messages competed in one unstructured band. v6 zakaz succeeds because zones separate capability scan → proof → cargo qualification.

**Injection:** `visual-semantics/hero-visual-semantics.md` describes zones; Factory must not collapse zones into single paragraph block.

---

## Field bundle (minimum)

```yaml
visual_semantics:
  version: v1
  route_id: <registry route_id>
  group_id: <ppc group>
  fields:
    hero_priority: capability_first | use_case_first | b2b_first | geo_first
    proof_priority: hero_strip | section_only
    cta_priority: form | call
    visual_density: low | medium | medium-high | high
    compactness_level: compact | standard
    mobile_critical: []
    trust_mode: operational_proof | social_proof | documents
    qualification_mode: hero_lower | tasks_section_only
    hero_layout_mode: grid_form_aside
    proof_visibility: prominent | standard
    cta_weight: primary_dominant | balanced
    semantic_focus: []
    cargo_cards_max: <int>
    frontend_priority: []
  drift_acceptance:
    productive: []
    destructive: []
    ambiguous: []
```

---

## Factory read order

1. `visual-semantics/*.md` (bundle)
2. `content/hero.md` (locked copy)
3. `factory/frontend-hints.md` (partial paths)
4. `factory/forbidden-drift.md`
5. `TRIUMPH-V6-CURRENT-FRONTEND-RULES.md` (breakpoints, forms)

---

## Anti-patterns

| Anti-pattern | Why |
|--------------|-----|
| «Just copy zakaz SCSS» for vezdehod | Specs/content wrong even if pretty |
| Generate new hero component per route | Violates V6 rollout — swap content in existing partials |
| Inject semantics via inline `style=` | Bypasses review; breaks density discipline |
| Skip visual bundle because blueprint exists | Blueprint ≠ visual semantics SoT |

---

## Related

- [semantic-density-control-v1.md](semantic-density-control-v1.md)
- `projects/orca/visual-semantics/contracts/visual-semantic-lock-rules-v0.md`
