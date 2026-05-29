# ORCA Visual Semantics System v0

## Definition

**Visual semantics** = human-calibrated operational fields that tell Website Factory **what to prioritize in layout**, not what words to write.

ORCA continues to own copy and PPC doctrine. Visual semantics owns:

- hierarchy (what wins attention first)
- zoning (what belongs in hero main vs lower band)
- proof mode (social vs operational vs hybrid)
- density budget (how many competing messages above fold)
- mobile-critical ordering (call vs form when instance is call-first)
- drift class hints (productive vs destructive)

**Not claimed:** automated layout, AI UX, conversion prediction, heatmaps.

## The calibration gap (Triumph v5)

| ORCA produced | Factory still inferred |
|---------------|------------------------|
| H1, lead, 5 capability bullets | Hero grid vs single column |
| Trust strip copy (4.9 ★) | Ops proof strip instead — **ambiguous drift** |
| Qualification line | Removed in v5 — **destructive drift** |
| Use-case chips | 6 interactive cargo cards + micro-CTAs |
| Primary CTA label | Form-in-hero dominance |
| Call-first mobile doctrine | Form stack order on ≤760px |

Source: `projects/orca/calibration/triumph-manipulator/drift-analysis/orca-vs-frontend-drift-v1.md`

## Canonical fields (v0)

Each field: meaning → allowed values → implementation meaning → Factory expectations → mobile → SAFE UNKNOWN.

### `hero_priority`

| | |
|---|---|
| **Meaning** | Which hero sub-zones must win the first 5–10 seconds |
| **Values** | `capability_first` · `cta_first` · `qualification_first` · `balanced` |
| **Implementation** | DOM order, column width ratio, overlay strength |
| **Factory** | Maps to `hero__main` content order vs `hero__aside` |
| **Mobile** | Stack order follows priority (e.g. `cta_first` may elevate tel before form) |
| **SAFE UNKNOWN** | Optimal priority per ad variant without device QA |

**Triumph zakaz (as-built):** `capability_first` — H1 → lead → 5 specs → form.

---

### `proof_priority`

| | |
|---|---|
| **Meaning** | Whether proof competes with capability or defers |
| **Values** | `hero_strip` · `below_fold` · `deferred_reviews_only` |
| **Implementation** | Presence/position of `hero-proof--v5` |
| **Factory** | Max items when `hero_strip` — see `trust_mode` |
| **Mobile** | Strip may collapse to 2 items — **UNKNOWN** optimal count |
| **SAFE UNKNOWN** | Scroll-depth impact of deferred social proof |

**Triumph zakaz:** `hero_strip` (4 ops items) + reviews at P3.

---

### `cta_priority`

| | |
|---|---|
| **Meaning** | Primary conversion surface above fold |
| **Values** | `form` · `call` · `dual_equal` · `messenger_secondary_only` |
| **Implementation** | Aside column, sticky bar, header tel prominence |
| **Factory** | Must match PPC instance `call-first` when set |
| **Mobile** | `mobile_critical` may override stack |
| **SAFE UNKNOWN** | Measured conversion split call vs form |

**Triumph instance:** call-first doctrine; **as-built hero:** `form` dominant — tension documented.

---

### `visual_density`

| | |
|---|---|
| **Meaning** | Count of distinct messages in first screen |
| **Values** | `low` · `medium` · `high` · `overloaded` |
| **Implementation** | Element budget per zone |
| **Factory** | Refuse `overloaded` without operator sign-off |
| **Mobile** | Downgrade one tier on ≤760px unless pack overrides |
| **SAFE UNKNOWN** | Exact element count threshold per viewport |

**Triumph zakaz hero:** `high` (~20+ sub-elements before scroll).

---

### `compactness_level`

| | |
|---|---|
| **Meaning** | Typographic/layout compression vs airy marketing |
| **Values** | `airy` · `standard` · `compact` · `dense` |
| **Implementation** | List vs paragraph features, icon specs, clamp() scale |
| **Factory** | `hero--v5` = compact specs list (productive vs v4 paragraphs) |
| **Mobile** | `dense` risks form below fold |
| **SAFE UNKNOWN** | Readability vs scan speed tradeoff per audience |

**Triumph:** `compact` in main grid; `dense` in lower band.

---

### `mobile_critical`

| | |
|---|---|
| **Meaning** | Elements that must remain reachable without excessive scroll on 390px |
| **Values** | `call` · `form_submit` · `primary_cta` · `qualification_line` · `capability_scan` (multi-select) |
| **Implementation** | Stack order, sticky bar, reduced cargo count |
| **Factory** | SCSS breakpoint behavior + optional sticky |
| **Mobile** | **Primary** consumer of this field |
| **SAFE UNKNOWN** | «Excessive scroll» threshold in px — not measured |

**Triumph gap:** `call` + `qualification_line` not fully satisfied in v5 hero.

---

### `trust_mode`

| | |
|---|---|
| **Meaning** | Hero proof semantics |
| **Values** | `social_proof` · `operational_proof` · `hybrid_proof` |
| **Implementation** | Stars/reviews vs ops facts vs both |
| **Factory** | See [trust-mode-system-v0.md](trust-mode-system-v0.md) |
| **Mobile** | Hybrid max 3 hero items recommended |
| **SAFE UNKNOWN** | Which mode wins for cold «аренда» queries — no A/B data |

**Triumph zakaz:** `operational_proof` (blueprint asked `social_proof`).

---

### `qualification_mode`

| | |
|---|---|
| **Meaning** | How anti-junk filtering appears visually |
| **Values** | `hero_notice` · `hero_lower_band` · `tasks_section_only` · `denied_tasks_only` |
| **Implementation** | `hero__notice` vs tasks block |
| **Factory** | Blueprint master hot: `hero_notice` — v5 uses `tasks_section_only` → drift |
| **Mobile** | Notice above cargo if restored |
| **SAFE UNKNOWN** | Lead quality impact of relocation |

**Triumph v5:** `tasks_section_only` (destructive vs blueprint).

---

### `hero_layout_mode`

| | |
|---|---|
| **Meaning** | Structural pattern |
| **Values** | `grid_form_aside` · `stacked` · `split_media` · `legacy_clutter` (forbidden) |
| **Implementation** | `hero--v5` shell zones |
| **Factory** | `grid_form_aside` = v5 PPC default |
| **Mobile** | `grid_form_aside` → stack at 760px |
| **SAFE UNKNOWN** | Alternate layouts for B2B-only routes |

**Triumph:** `grid_form_aside` + `hero__lower` band.

---

### `proof_visibility`

| | |
|---|---|
| **Meaning** | Visual weight of proof (not copy) |
| **Values** | `prominent` · `subtle` · `hidden_hero` |
| **Implementation** | Icon size, contrast, position in scan path |
| **Factory** | Ops strip = `prominent`; 4.9 ★ absent = social `hidden_hero` |
| **Mobile** | Collapse to 2 items when `subtle` |
| **SAFE UNKNOWN** | Star rating click-through |

---

### `cta_weight`

| | |
|---|---|
| **Meaning** | Visual dominance of primary vs secondary CTAs |
| **Values** | `primary_dominant` · `shared` · `secondary_noise` (warning) |
| **Implementation** | Button style: solid red vs outline |
| **Factory** | 6 cargo «Заказать перевозку» = borderline `secondary_noise` |
| **Mobile** | Single red focal point rule |
| **SAFE UNKNOWN** | Cargo micro-CTA conversion contribution |

**Triumph:** `primary_dominant` in form; cargo row risks `secondary_noise`.

---

### `semantic_focus`

| | |
|---|---|
| **Meaning** | Single semantic lane hero must communicate |
| **Values** | `one_machine` · `use_case_fit` · `price_calc` · `speed_dispatch` · `b2b_payment` |
| **Implementation** | Copy + spec selection |
| **Factory** | Must not mix `one_machine` with fleet visuals |
| **Mobile** | Same focus, fewer elements |
| **SAFE UNKNOWN** | Multi-focus routes without calibration |

**Triumph:** `one_machine` + `use_case_fit` (cargo).

---

### `conversion_intent_weight`

| | |
|---|---|
| **Meaning** | PPC group commercial temperature |
| **Values** | `hot` · `warm` · `research` |
| **Implementation** | Form prominence, pricing block elevation |
| **Factory** | grp_fc12 = `hot` → inline form justified |
| **Mobile** | `hot` elevates `mobile_critical` for call+form |
| **SAFE UNKNOWN** | Intent tier per keyword without live data |

---

### `visual_noise_risk`

| | |
|---|---|
| **Meaning** | Predicted focal-point competition |
| **Values** | `low` · `medium` · `high` · `critical` |
| **Implementation** | Count of red accents, CTAs, competing headlines |
| **Factory** | Block build if `critical` without zoning plan |
| **Mobile** | Often one tier higher than desktop |
| **SAFE UNKNOWN** | Automated detection — human sets field |

**Triumph lower band:** `high` (4 proof + 6 cargo).

---

### `frontend_priority`

| | |
|---|---|
| **Meaning** | Ordered implementation attention for Factory |
| **Values** | JSON array of zone IDs: `hero_main`, `hero_aside`, `hero_lower`, `specs`, `tasks`, … |
| **Implementation** | Build order, QA focus, partial completeness |
| **Factory** | Contract in [frontend-priority-contract-v0.md](contracts/frontend-priority-contract-v0.md) |
| **Mobile** | Same order; mobile overrides as hints |
| **SAFE UNKNOWN** | Per-route priority swaps without calibration |

**Triumph:** P0 hero → P1 specs/tasks → P3 trust.

## Bundle example (zakaz v5 as-built)

```yaml
hero_priority: capability_first
proof_priority: hero_strip
cta_priority: form
visual_density: high
compactness_level: compact
mobile_critical: [form_submit, capability_scan]
trust_mode: operational_proof
qualification_mode: tasks_section_only
hero_layout_mode: grid_form_aside
proof_visibility: prominent
cta_weight: primary_dominant
semantic_focus: [one_machine, use_case_fit]
conversion_intent_weight: hot
visual_noise_risk: high
frontend_priority: [hero_main, hero_aside, hero_lower, specs, tasks, pricing_factors, trust_reviews]
```

Full worked example: [examples/triumph-zakaz-hero-visual-semantics-v1.md](examples/triumph-zakaz-hero-visual-semantics-v1.md).

## Drift vocabulary

| Class | ORCA action |
|-------|-------------|
| **productive** | Encode in pack; Factory may keep |
| **destructive** | Block `approved_for_factory` until fixed |
| **ambiguous** | Operator decision + document in pack |
| **neutral** | Presentation only |

See [triumph-calibration/productive-drift-findings-v1.md](triumph-calibration/productive-drift-findings-v1.md) and [destructive-drift-findings-v1.md](triumph-calibration/destructive-drift-findings-v1.md).
