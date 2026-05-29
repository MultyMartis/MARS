# ORCA ↔ Website Factory Coordination Protocol v1

**Status:** production coordination contract (documentation only)  
**Project:** `triumph-manipulator-krasnodar`  
**Frontend baseline:** `workspaces/triumph-manipulator-landing-v6/`  
**Extends:** [orca-website-factory-semantic-lock-v0.md](../intelligence/orca-website-factory-semantic-lock-v0.md) — this file adds **coordination semantics** for Triumph mass pack generation; it does not replace the lock doc.

---

## A. Role separation

### ORCA — semantic authority

ORCA owns **commercial and qualification meaning** for each route:

| Domain | ORCA authority |
|--------|----------------|
| PPC | Ad ↔ landing continuity, group mapping, negative space |
| Intent | Master / capability / use-case / B2B / geo framing |
| Trust | Trust mode, proof mode, review sources, operational proof vs social proof |
| CTA | Hierarchy (call vs form), labels, surface priority |
| FAQ | Questions, answers, objection handling — no Factory paraphrase |
| Route strategy | Which machine story, which tasks, which denied tasks |
| Pricing framing | «По задаче», factors, forbidden fake hero rates |
| Visual semantics | Density, hero zoning, cargo limits, frontend_priority — not pixel CSS |
| Semantic locks | MODE 1 fields, destructive drift class, claims boundaries |

ORCA **does not** own: gulp pipeline, breakpoint regimes, SCSS architecture, responsive breakpoints policy (see V6 rules), or deploy.

### Website Factory — frontend implementation authority

Factory owns **presentation and build**:

| Domain | Factory authority |
|--------|-------------------|
| HTML structure | Partials, includes, `data-*` markers per V6 conventions |
| SCSS | Spacing, grid, component polish within V6 token discipline |
| Responsive | Stack order, touch targets, overflow fixes |
| Layout | Section composition from **approved** pack + handoff |
| Visual polish | Imagery crop, overlay, typography fit (`&nbsp;`, line breaks) |
| UX implementation | Forms wiring, modals, sticky header — no semantic rewrite |
| Build | `npm run build`, dist output, form IDs per page |

Factory **does not** own: ad copy, intent tier, claim invention, FAQ rewriting, or pricing semantics.

### Human — final operational control

| Decision | Owner |
|----------|--------|
| `approved_for_factory` | Human operator |
| Semantic conflict resolution (ORCA vs Factory report) | Human |
| Drift acceptance (productive vs destructive) | Human |
| Launch / ads / Commander import | Human gates per project container |
| Pack version bump after Factory findings | Human |

**No agent** may silently resolve destructive drift or ship MODE 1 without `approved_for_factory`.

---

## B. What ORCA delivers

ORCA does **not** hand off «текст» or unstructured copy dumps.

ORCA delivers a **production semantic pack** (folder or consolidated MD) containing:

| Artifact class | Contents |
|----------------|----------|
| **Semantic pack** | `pack_id`, route identity, `content_mode: MODE_1`, gates |
| **Slot content** | Per `section_id` copy with locks (hero, specs, tasks, denied, pricing, trust, b2b, faq, final_cta) |
| **Visual semantics** | YAML bundle: `hero_layout_mode`, `visual_density`, `trust_mode`, `cta_priority`, `mobile_critical`, `frontend_priority` |
| **CTA hierarchy** | Primary / secondary labels, surfaces, call-first vs form-first |
| **Trust mode** | e.g. `operational_proof` vs `social_proof` — per route |
| **Proof mode** | What proof appears in hero strip vs trust section |
| **Density limits** | `cargo_cards_max`, hero message budget — see [semantic-density-control-v1.md](semantic-density-control-v1.md) |
| **Route differentiation** | H1, tasks, denied tasks, qualification — **not** master-hot defaults on siblings |
| **Pricing framing** | Factors, anti-fake-rate locks, B2B payment framing where applicable |
| **FAQ logic** | Intent-specific Q&A; link to blueprint FAQ section |
| **Qualification logic** | Denied tasks, anti-evacuation, anti-junk — placement rules |
| **Mobile criticality** | `mobile_critical[]` — Factory checklist, not auto-enforcement |
| **Semantic locks** | `factory/semantic-lock.md`, `factory/forbidden-drift.md`, drift classes |

**Canonical examples:**

- `projects/orca/content-packs/examples/triumph-manipulyator-zakaz-pack-v1/`
- `projects/orca/content-packs/examples/triumph-manipulyator-5-tonn-pack-v0.md`
- Handoff pattern: `projects/orca/ppc/triumph-manipulator/handoff/triumph-manipulator-v5-page-01-manipulyator-5-tonn-handoff.md`

**Handoff MD** is derived from pack — see [factory-handoff-minimum-contract-v1.md](factory-handoff-minimum-contract-v1.md).

---

## C. What Factory returns

After implementation (human-operated build + QA), Factory lane produces an **implementation report** for operator review:

| Return type | Description |
|-------------|-------------|
| **Implementation report** | Files touched, build result, page URL path in workspace |
| **Visual drift findings** | Presentation changes that may affect scan hierarchy |
| **Responsive findings** | Breakpoint stack issues (1024/1025, 1490 header per V6 rules) |
| **Overflow findings** | Horizontal scroll, clipped cargo grid, FAQ column break |
| **Mobile findings** | Fold safety vs `mobile_critical` — device QA notes |
| **Semantic conflicts** | Copy that could not fit without meaning change — **stop**, do not improvise |
| **Slot overflows** | Text length breaking grid — propose typography fit only |
| **Typography constraints** | RU line length, `&nbsp;` needs, H1 wrap |

Factory reports feed **pack revision** or **operator waiver** — not autonomous ORCA sync.

---

## D. Factory forbidden actions

Under MODE 1 (active semantic lock), Factory **must not**:

| Category | Forbidden |
|----------|-----------|
| **Semantics** | Rewrite H1, lead, specs numbers, denied tasks, FAQ answers |
| **PPC** | Break ad ↔ hero continuity; change capability tonnage without pack bump |
| **Pricing** | Add fake hero hourly rate; invent «от X ₽» |
| **CTA** | Invert call-first vs form-first strategy from pack |
| **Trust / proof** | Invent fleet, years on market, review counts, star ratings without source |
| **Claims** | Nationwide coverage, «любой груз», second machine, 10+ т on 5 т route |
| **Process** | Ship copy edits without pack version + operator approval |

**Historical destructive patterns (never restore):**

- v4 index hero: `hero__rate`, fleet `hero__features`, «5–10 т», «свой автопарк»
- Six primary-red CTAs in one viewport
- Hero carousel competing with qualification

Source: `calibration/triumph-manipulator/ux-observations/hero-evolution-v1.md`, pack `forbidden-drift.md`.

---

## E. Allowed Factory adaptation

Factory **may** adapt presentation without pack bump when meaning is preserved:

| Allowed | Examples |
|---------|----------|
| Spacing | Section padding, grid gaps |
| Responsive | Mobile stack order **if** `mobile_critical` still satisfied |
| Visual grouping | Cargo 2×3 → 2×2 on small screens (card count cap per pack) |
| Typography fit | Font size, line-height, hyphenation — **not** claim text change |
| Overflow fixes | `overflow-x`, flex min-width, FAQ column wrap |
| Layout polish | Overlay strength, image crop, icon alignment |
| UI refinement | Button size, consent link layout, modal triggers |

**Rule:** If adaptation requires **deleting** a qualification line or **softening** a denial → stop → ORCA pack update.

---

## F. Coordination workflow (human-operated)

```text
ORCA research / PPC pack (validated)
        ↓
Semantic pack authoring (this layer)
        ↓
production-pack-readiness-checklist
        ↓
Operator: approved_for_factory
        ↓
Handoff MD (minimum contract)
        ↓
Factory → V6 workspace (one route per pilot gate)
        ↓
Factory implementation report
        ↓
PPC landing QA + matrix update
        ↓
approved_for_ads / launch gates (separate)
```

**Pilot gate (V6):** complete **one** non-zakaz page end-to-end before starting a second; second pilot before batch remainder — see `V6-PAGE-ROLLOUT-PLAN.md`.

---

## G. Lane boundaries (no runtime)

| Claim | Truth |
|-------|--------|
| «Coordination protocol enforces automatically» | **false** — human + checklist only |
| «ORCA pushes to Factory API» | **false** — files in repo + operator session |
| «Factory validates semantics» | **partial** — Factory reports conflicts; ORCA/operator adjudicates |

---

## Related documents

- [semantic-pack-generation-system-v1.md](semantic-pack-generation-system-v1.md)
- [factory-handoff-minimum-contract-v1.md](factory-handoff-minimum-contract-v1.md)
- [pack-to-factory-workflow-v0.md](../content-packs/workflows/pack-to-factory-workflow-v0.md)
