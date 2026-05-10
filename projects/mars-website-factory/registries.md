# MARS Website Factory — planned registries (knowledge modules)

**Status:** **planned** — no machine-readable registry files are asserted in this repository for these modules unless added in a future phase.

Each module: **purpose**, **fields** (suggested), **examples**, **anti-patterns**, **relation to agents/workflows**.

---

## 1. Site Type Registry

| Aspect | Content |
|--------|---------|
| **Purpose** | Classify projects (e.g. landing, corporate, catalog-light, lead-gen) to pick default blocks, SEO patterns, and QA checklists. |
| **Fields (suggested)** | `site_type_id`, `description`, `default_sitemap_template`, `allowed_block_categories`, `typical_cta_patterns`, `risk_notes` |
| **Examples** | `lead_gen_service` — hero + trust + offer + FAQ; `event_landing` — schedule + speakers + register |
| **Anti-patterns** | One-size-fits-all blocks for every site type; unversioned “magic” defaults |
| **Relations** | **Site Type Classifier Agent** reads/writes proposals; **Page Blueprint Agent** consumes; **workflow-map** intake → strategy |

---

## 2. Block Registry

| Aspect | Content |
|--------|---------|
| **Purpose** | Canonical list of **content/section blocks** (semantic name, props, allowed variants) for blueprints and frontend implementation. |
| **Fields (suggested)** | `block_id`, `display_name`, `schema` (props), `responsive_notes`, `a11y_requirements`, `scss_module_hint`, `js_behavior` (data-attr contract) |
| **Examples** | `hero_primary`, `feature_grid_3`, `testimonial_carousel`, `pricing_table_simple` |
| **Anti-patterns** | Ad-hoc block names per page without IDs; props that cannot map to static HTML |
| **Relations** | **Page Blueprint Agent** outputs block instances; **Gulp Frontend Agent** implements; **Validator** checks against registry |

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

| Aspect | Content |
|--------|---------|
| **Purpose** | How **src** is structured, build commands, **forbidden** paths (`dist` manual edit), JS scope rules, include/partials conventions. |
| **Fields (suggested)** | `rule_id`, `severity`, `rationale`, `check_method` |
| **Examples** | “Edit `src` only”; “no new global `window.*` without review”; BEM or agreed naming |
| **Anti-patterns** | Framework lock-in contradicting static profile without decision record; global pollution |
| **Relations** | **Gulp Frontend Agent**; **Frontend QA Agent**; **Validator** for secrets and dangerous patterns |

---

## SAFE UNKNOWN

- JSON Schema / YAML location for registries — **not** fixed.
- Whether registries merge into a future **Tool** or **Memory** layer — **unknown**.
