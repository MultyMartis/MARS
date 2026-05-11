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
| **Relations** | **Site Type Classifier Agent** reads/writes proposals; **Page Blueprint Agent** consumes; **workflow-map** intake → strategy |

---

## 2. Block Registry

**Delivered (v0):** [block-registry-v0.md](block-registry-v0.md) — normalized rows (commercial / SEO / trust / UX / QA / compatibility), field glossary, and **no** machine schema asserted.

| Aspect | Content |
|--------|---------|
| **Purpose** | Canonical list of **content/section blocks** (`block_id`) for blueprints and frontend planning: roles, constraints, and site-type **compatibility** (documentation only). |
| **Fields (v0)** | See v0 glossary; includes `block_id`, `category`, commercial/SEO/UX fields, `CTA_presence`, `dependencies`, `anti_patterns`, complexity hints, `compatible_site_types` / `incompatible_site_types`. Future artefacts may add `display_name`, props schema, `js_behavior` — **not** fixed in v0. |
| **Examples** | v0 lists `hero`, `trust_block`, `services_grid`, `faq`, `cases`, `reviews`, `pricing`, `process_steps`, `contact_cta`, `calculator`, `comparison`, `geo_trust`, `catalog_grid`, `sticky_cta`, `lead_form`, `final_cta`. |
| **Anti-patterns** | Ad-hoc block names per page without IDs; blocks incompatible with declared **`site_type_id`** without HITL |
| **Relations** | Consumes **`site_type_id`** from [Site Type Registry v0](site-type-registry-v0.md); **Page Blueprint** (planned) outputs instances; **Gulp Frontend Agent** (planned) implements; **Validator** (planned) checks against registry |

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
