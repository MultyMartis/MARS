# MARS Website Factory — planned registries (knowledge modules)

**Status:** **mixed** — **[Site Type Registry v0](site-type-registry-v0.md)** is **in-repo** as Markdown. Other modules below remain **planned** as first-class files until their v0 deliverables land. **No** machine-enforced registry service is asserted.

Each module: **purpose**, **fields** (suggested), **examples**, **anti-patterns**, **relation to agents/workflows**.

---

## 1. Site Type Registry

**Delivered (v0):** [site-type-registry-v0.md](site-type-registry-v0.md) — normalized rows and field glossary (documentation only).

| Aspect | Content |
|--------|---------|
| **Purpose** | Classify projects (e.g. landing, corporate, catalog, ecommerce, geo/SEO programs) to pick default blocks, SEO patterns, and QA checklists. |
| **Fields (suggested)** | See v0 glossary; includes `site_type_id`, goals, monetization, SEO/CTA/trust/UX models, block **roles**, forbidden patterns, QA focus, HITL. |
| **Examples** | v0 lists `landing`, `service_landing`, `promo_site`, `corporate_site`, `catalog_site`, `ecommerce`, `geo_landing`, `seo_landing`, `ai_visibility_page`, `hybrid_commercial`. |
| **Anti-patterns** | One-size-fits-all blocks for every site type; unversioned “magic” defaults |
| **Relations** | **Site Type Classifier Agent** reads/writes proposals; [Page Blueprint Contract v0](page-blueprint-contract-v0.md) consumes **`site_type_id`**; **workflow-map** intake → strategy |

---

## 2. Block Registry

**Delivered (v0):** [block-registry-v0.md](block-registry-v0.md) — normalized rows (commercial / SEO / trust / UX / QA / compatibility), field glossary, and **no** machine schema asserted.

| Aspect | Content |
|--------|---------|
| **Purpose** | Canonical list of **content/section blocks** (`block_id`) for blueprints and frontend planning: roles, constraints, and site-type **compatibility** (documentation only). |
| **Fields (v0)** | See v0 glossary; includes `block_id`, `category`, commercial/SEO/UX fields, `CTA_presence`, `dependencies`, `anti_patterns`, complexity hints, `compatible_site_types` / `incompatible_site_types`. Future artefacts may add `display_name`, props schema, `js_behavior` — **not** fixed in v0. |
| **Examples** | v0 lists `hero`, `trust_block`, `services_grid`, `faq`, `cases`, `reviews`, `pricing`, `process_steps`, `contact_cta`, `calculator`, `comparison`, `geo_trust`, `catalog_grid`, `sticky_cta`, `lead_form`, `final_cta`. |
| **Anti-patterns** | Ad-hoc block names per page without IDs; blocks incompatible with declared **`site_type_id`** without HITL |
| **Relations** | Consumes **`site_type_id`** from [Site Type Registry v0](site-type-registry-v0.md); [Page Blueprint Contract v0](page-blueprint-contract-v0.md) references **`block_id`** and ordering; [Page Blueprint QA Checklist v0](page-blueprint-qa-checklist-v0.md) validates compatibility; **Gulp Frontend Agent** (planned) implements; **Validator** (planned) checks against registry |

---

## 3. Commercial Pattern Library

**Delivered (v1):** [scroll-process-timeline-pattern-v1.md](scroll-process-timeline-pattern-v1.md) — scroll-driven order-process timeline with track, progress line, branded vehicle, step cards, reverse-on-scroll-up (`pattern_id`: `scroll_process_timeline`; token: `WF-SCROLL-PROCESS-TIMELINE`). Evidence: Triumph Cargo Taxi DEV `/services/gruzovoe-taksi/`.

| Aspect | Content |
|--------|---------|
| **Purpose** | Reusable **marketing/commercial** compositions: offer framing, urgency ethics, social proof placement, **interactive process explanation** (**policy-bound**). |
| **Fields (suggested)** | `pattern_id`, `intent`, `copy_structure`, `ethical_constraints`, `forbidden_claims`, `interaction_model` (for interactive patterns) |
| **Examples** | “Problem–agitation–solution” outline; testimonial + logo strip pairing; **`scroll_process_timeline`** — logistics/service linear process with user-controlled scroll animation |
| **Anti-patterns** | Dark patterns; unverifiable statistics; medical/financial claims without review; **autoplay / loop animation** on process timelines (see scroll-process-timeline UX rule) |
| **Relations** | **Marketing Strategy Agent**; **Conversion QA Agent**; **HITL** for sensitive industries; [frontend-production-invariants-v1.md](frontend-production-invariants-v1.md) §10 for engineering invariants |

---

## 4. SEO Pattern Library

| Aspect | Content |
|--------|---------|
| **Purpose** | On-page patterns: title/h1/meta conventions, FAQ schema usage (**where allowed**), internal linking templates. |
| **Fields (suggested)** | `pattern_id`, `applies_to_site_types`, `title_formula`, `snippet_guidance`, `schema_notes` |
| **Examples** | One primary intent per page; FAQ block only when content genuinely FAQ |
| **Anti-patterns** | Keyword stuffing; fake aggregate ratings; doorway-style thin pages |
| **Relations** | **SEO Strategy Agent**; **SEO QA Agent**; optional cross-ref **MetaBOT** SEO pack for **content** workflows (**separate** product boundary) |

---

## 5. Design System Rules

| Aspect | Content |
|--------|---------|
| **Purpose** | Tokens, type scale, spacing, color usage, component states — human- and agent-readable. |
| **Fields (suggested)** | `token_group`, `rules`, `do_dont`, `breakpoint_behavior` |
| **Examples** | Max line length; contrast minimums; focus ring requirements |
| **Anti-patterns** | Hard-coded one-off hex in every section; inconsistent spacing scale |
| **Relations** | **AI Designer Agent**, **Design QA Agent**; handoff to **frontend-production-model** |

---

## 6. Frontend Production Rules

**Delivered (v0):** [frontend-production-rules-v0.md](frontend-production-rules-v0.md) — compact operator rules (documentation only; **not** runtime enforcement).

| Aspect | Content |
|--------|---------|
| **Purpose** | How **src** is structured, build commands, **forbidden** paths (`dist` manual edit), JS scope rules, include/partials conventions. |
| **Fields (suggested)** | `rule_id`, `severity`, `rationale`, `check_method` |
| **Examples** | “Edit `src` only”; “no new global `window.*` without review”; BEM or agreed naming |
| **Anti-patterns** | Framework lock-in contradicting static profile without decision record; global pollution |
| **Relations** | **Gulp Frontend Agent**; **Frontend QA Agent**; **Validator** for secrets and dangerous patterns |
| **RU typography (authority)** | [russian-no-word-splitting-typography-v1.md](russian-no-word-splitting-typography-v1.md) |
| **RU landing QA preset** | [ru-landing-qa-preset-v1.md](ru-landing-qa-preset-v1.md) — mandatory widths for Russian commercial landings |
| **Section spacing (operational)** | [frontend-section-spacing-rule-v1.md](frontend-section-spacing-rule-v1.md) |
| **Shell-first start gate** | [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md) |
| **Canonical Clean Shell** | [canonical-clean-shell-v1.md](canonical-clean-shell-v1.md) — mandatory empty shell before Layout Spec |
| **Production Standards governance** | [production-standards-governance-v1.md](production-standards-governance-v1.md) |
| **Visual Foundation Contract** | [frontend-visual-foundation-contract-v1.md](frontend-visual-foundation-contract-v1.md) |
| **Design Calibration stage** | [frontend-design-calibration-stage-v1.md](frontend-design-calibration-stage-v1.md) |
| **Precision governance** | [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) — spacing scales, line-height law, normalization |
| **Frontend authority order** | [frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md) — canonical decision hierarchy; Approved Operator Laws OL-01–OL-07 |
| **Layout pattern requirement** | [frontend-layout-pattern-library-requirement-v1.md](frontend-layout-pattern-library-requirement-v1.md) |
| **Design source → frontend mapping** | [design-source-to-frontend-mapping-governance-v1.md](design-source-to-frontend-mapping-governance-v1.md) — multi-source extraction, layout chain, Mapping QA gate |
| **Figma inspection authority** | [figma-inspection-authority-rules-v1.md](figma-inspection-authority-rules-v1.md) — FIGMA-VISIBLE-CONTENT-AUTHORITY, hidden-layer exclusion, layer-name conflict, audit contract |
| **WF-GRID discipline (container layer)** | [WF-GRID-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-GRID-DISCIPLINE-v1.md) — section ≠ container; page grid contract |
| **WF-LAYOUT discipline (inner zones)** | [WF-LAYOUT-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-LAYOUT-DISCIPLINE-v1.md) — hero/card/trust zones; fr/minmax authority |
| **Foundation QA (pre–Home gate)** | [frontend-foundation-qa-governance-v1.md](frontend-foundation-qa-governance-v1.md) — consolidated checklist; shell-first Phase 5 |
| **Design completeness** | [frontend-design-completeness-governance-v1.md](frontend-design-completeness-governance-v1.md) — entity presence audit before fidelity QA |
| **Frontend Design QA Matrix** | [frontend-design-qa-matrix-v1.md](frontend-design-qa-matrix-v1.md) — DQ-01–DQ-12 fidelity domains; Production PASS gate |
| **Pixel fidelity audit** | [pixel-fidelity-audit-rules-v1.md](pixel-fidelity-audit-rules-v1.md) — numeric variance rules per PF-* domain |
| **Frontend QA reporting** | [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) — Production Verdict rollup; gate vocabulary |
| **Enforcement Pack** | [website-factory-enforcement-pack-v1.md](website-factory-enforcement-pack-v1.md) — Operator Law, Compiled CSS, Inline Style, ROOT COMPLIANCE |
| **Compliance Decision Model** | [frontend-compliance-decision-model-v1.md](frontend-compliance-decision-model-v1.md) — RAW VIOLATION → gate verdict route |
| **Failure Attribution Model** | [frontend-failure-attribution-model-v1.md](frontend-failure-attribution-model-v1.md) — FAILURE EVENT → Expected Gate → Attribution Verdict |
| **Operator Visual Approval Law** | [operator-visual-approval-law-v1.md](operator-visual-approval-law-v1.md) — TECHNICAL PASS ≠ OPERATOR APPROVAL; mandatory operator visual review after visual stages |
| **Layout Spec Law** | [layout-spec-law-v1.md](layout-spec-law-v1.md) — mandatory composition artifact before HTML/CSS; operator APPROVED |
| **Group Decomposition Law** | [group-decomposition-law-v1.md](group-decomposition-law-v1.md) — discrete GROUP-IDs per ROW before Layout Spec; operator APPROVED |
| **FP-0002 Group Decomposition lesson** | [FP-0002-group-decomposition-lesson-v1.md](FP-0002-group-decomposition-lesson-v1.md) — CONTACT BLOCK aggregation in JPG test |
| **FP-0002 Clean Shell lesson** | [FP-0002-clean-shell-lesson-v1.md](FP-0002-clean-shell-lesson-v1.md) — beautiful starter vs empty shell |
| **CSS multicol masonry browser lesson** | [css-multicol-masonry-browser-compatibility-lesson-v1.md](css-multicol-masonry-browser-compatibility-lesson-v1.md) — Chrome/Firefox column group `display`; WPilot footer incident |
| **Scroll Process Timeline pattern** | [scroll-process-timeline-pattern-v1.md](scroll-process-timeline-pattern-v1.md) — scroll-driven order-process block; Triumph Cargo Taxi `/services/gruzovoe-taksi/` |
| **Inline style allowlist** | [frontend-inline-style-allowlist-v1.md](frontend-inline-style-allowlist-v1.md) |
| **Factory Failure Classes** | [failures/asset-identity-collision-v1.md](failures/asset-identity-collision-v1.md) and peer classes — see [§7](#7-factory-failure-classes) |

---

## 7. Factory Failure Classes

**Purpose:** Canonical **documented** failure classes for Website Factory production escapes — human-operated taxonomy and mitigation; **not** a runtime failure engine.

| Token / Class ID | Document | Domain |
|------------------|----------|--------|
| `VISUAL INTERPRETATION WITHOUT LAYOUT SPEC` | [layout-spec-law-v1.md](layout-spec-law-v1.md) §7 | Composition without Layout Spec |
| `PRE-LAYOUT-SPEC STARTER RESIDUE` | [canonical-clean-shell-v1.md](canonical-clean-shell-v1.md) | Starter demo before Clean Shell |
| `GROUP AGGREGATION BEFORE DECOMPOSITION` | [group-decomposition-law-v1.md](group-decomposition-law-v1.md) §2 | Grouping before decomposition register |
| `ASSET_IDENTITY_COLLISION` | [failures/asset-identity-collision-v1.md](failures/asset-identity-collision-v1.md) | Wrong brand mark from multi-brand FIG / first-image heuristic |

**Investigation route:** [frontend-failure-attribution-model-v1.md](frontend-failure-attribution-model-v1.md) — FAILURE EVENT → Expected Gate → Attribution Verdict.

**Anti-pattern:** Do **not** register the same class twice under different tokens. Asset wrongness at DQ-08/PF-07 may be **symptom** of `ASSET_IDENTITY_COLLISION` when upstream selection used **first image = logo**.

---

## SAFE UNKNOWN

- JSON Schema / YAML location for registries — **not** fixed.
- Whether registries merge into a future **Tool** or **Memory** layer — **unknown**.
