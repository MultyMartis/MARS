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

| Aspect | Content |
|--------|---------|
| **Purpose** | Reusable **marketing/commercial** compositions: offer framing, urgency ethics, social proof placement (**policy-bound**). |
| **Fields (suggested)** | `pattern_id`, `intent`, `copy_structure`, `ethical_constraints`, `forbidden_claims` |
| **Examples** | “Problem–agitation–solution” outline; testimonial + logo strip pairing |
| **Anti-patterns** | Dark patterns; unverifiable statistics; medical/financial claims without review |
| **Relations** | **Marketing Strategy Agent**; **Conversion QA Agent**; **HITL** for sensitive industries |

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
| **Production Standards governance** | [production-standards-governance-v1.md](production-standards-governance-v1.md) |
| **Visual Foundation Contract** | [frontend-visual-foundation-contract-v1.md](frontend-visual-foundation-contract-v1.md) |
| **Design Calibration stage** | [frontend-design-calibration-stage-v1.md](frontend-design-calibration-stage-v1.md) |
| **Precision governance** | [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) — spacing scales, line-height law, normalization |
| **Frontend authority order** | [frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md) — canonical decision hierarchy; Approved Operator Laws OL-01–OL-07 |
| **Layout pattern requirement** | [frontend-layout-pattern-library-requirement-v1.md](frontend-layout-pattern-library-requirement-v1.md) |
| **Design source → frontend mapping** | [design-source-to-frontend-mapping-governance-v1.md](design-source-to-frontend-mapping-governance-v1.md) — multi-source extraction, layout chain, Mapping QA gate |
| **WF-GRID discipline (container layer)** | [WF-GRID-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-GRID-DISCIPLINE-v1.md) — section ≠ container; page grid contract |
| **WF-LAYOUT discipline (inner zones)** | [WF-LAYOUT-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-LAYOUT-DISCIPLINE-v1.md) — hero/card/trust zones; fr/minmax authority |
| **Foundation QA (pre–Home gate)** | [frontend-foundation-qa-governance-v1.md](frontend-foundation-qa-governance-v1.md) — consolidated checklist; shell-first Phase 5 |
| **Design completeness** | [frontend-design-completeness-governance-v1.md](frontend-design-completeness-governance-v1.md) — entity presence audit before fidelity QA |
| **Frontend Design QA Matrix** | [frontend-design-qa-matrix-v1.md](frontend-design-qa-matrix-v1.md) — DQ-01–DQ-12 fidelity domains; Production PASS gate |
| **Pixel fidelity audit** | [pixel-fidelity-audit-rules-v1.md](pixel-fidelity-audit-rules-v1.md) — numeric variance rules per PF-* domain |
| **Frontend QA reporting** | [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) — Production Verdict rollup; gate vocabulary |

---

## SAFE UNKNOWN

- JSON Schema / YAML location for registries — **not** fixed.
- Whether registries merge into a future **Tool** or **Memory** layer — **unknown**.
