# MARS Website Factory — Design Handoff Contract v0

**Status:** **documented** — human-readable **design-layer input** contract. **Not** a JSON Schema, **not** runtime validation, **not** a claim that any pipeline in this repo produces designs or Figma files automatically.

---

## Purpose

- Converts an approved **page blueprint** into **visual production requirements**: what design must express so UX, marketing, and SEO decisions stay traceable in pixels and tokens.
- Connects **UX / marketing / SEO** decisions (from the blueprint and upstream layers) with **design execution** (layout, hierarchy, trust surfaces, CTA staging).
- Defines the **artifact set** expected from the design layer before **frontend production** (wireframes, direction, tokens, section-level visual intent — format **TBD** per project).
- Does **not** imply **automated Figma generation**, plugin export, or design-to-code in MARS v0; those remain **planned** or **SAFE UNKNOWN** until separately specified.

---

## Relation to Page Blueprint Contract v0

[Page Blueprint Contract v0](page-blueprint-contract-v0.md) is the **authoritative upstream** for **`source_blueprint_id`**, **`site_type_id`**, section/block intent (**`required_sections`**, **`section_order`**, **`block_mapping`**), CTA and trust strategy, and page-level **QA_requirements** / **HITL_required**. The design handoff **narrows** blueprint prose into **visual and experiential obligations**; it must **not** silently change commercial, SEO, or legal claims. Conflicts → escalate via **HITL_required** and **SAFE_UNKNOWN_notes**.

---

## Relation to Design System Rules

[Design System Rules](registries.md#5-design-system-rules) (planned module in [registries.md](registries.md)) supply **token groups**, type scale, spacing scale, color roles, component states, and **do/don’t** boundaries. This contract’s **`typography_direction`**, **`color_direction`**, **`spacing_system`**, and **`component_variants`** must **reference** or **embed** those rules where they exist; where the design system is incomplete, record gaps in **SAFE_UNKNOWN_notes** — do **not** invent token names as if they were build-time truth.

---

## Relation to AI Designer Agent

The **AI Designer Agent** (planned; see [design-layer-model.md](design-layer-model.md), [agent-map.md](agent-map.md)) is a **candidate producer** of this handoff’s content: **`visual_direction`**, token-aligned **`typography_direction`** / **`color_direction`**, **`section_visual_map`**, and **`component_variants`**. v0 does **not** assert tool I/O, prompts, or storage paths for that agent. Human or hybrid authoring of the same fields is equally valid.

---

## Relation to Design Governance Layer / Canonical Design Implementation Pack

After design approval (and ideally **before** or **during** frontend handoff authoring), operators may attach a **[Canonical Design Implementation Pack](canonical-implementation-pack-architecture.md)** ([Design Governance Layer](design-governance-layer.md)): versioned **`semantics/`** + **`implementation-pack/`** + **`validation/`** under **`projects/<project>/design/vN/`**, produced under human supervision by the **[Design Governance Agent](../../agents/design-governance-agent.md)** (**planned**).

- This contract remains the **experiential/visual obligations** artifact; the pack narrows **interpretation drift** (section meaning, counts, CTAs, archive isolation) — **documentation-first**, **not** automatic enforcement.
- The pack **must not** contradict the **Page Blueprint Contract v0** (commercial, SEO, legal, **`block_mapping`**) without **HITL** resolution.
- **`exports/`** in the pack support QA; **canonical structure** remains in **`semantics/`** plus **`implementation-pack/`** per [canonical-implementation-pack-architecture.md §1](canonical-implementation-pack-architecture.md).

---

## Relation to Wireframe Generator Agent and Full Design Generator Agent

- **Wireframe Generator Agent** (planned) typically precedes or overlaps **full** visual lock: low-fidelity **`section_visual_map`** and **`responsive_behavior`** intent may originate there; this contract may **reference** wireframe artifact IDs in **SAFE_UNKNOWN_notes** until a wire ID field is standardized.
- **Full Design Generator Agent** (planned) produces high-fidelity comps or exports; output **must** satisfy **`forbidden_visual_patterns`**, **accessibility_notes**, and **QA_requirements** here. **HITL** before any “approved for build” state.

---

## Relation to Design QA Agent and Conversion QA Agent

- **Design QA Agent** (planned): checks consistency with blueprint blocks, design system rules, and this contract’s **QA_requirements**.
- **Conversion QA Agent** (planned): checks that **`conversion_goals`** and blueprint **CTA_strategy** / **conversion_points** remain legible and honest in the visual layout (no hidden friction, no misleading emphasis).

---

## Relation to future Figma / artifact generation

Figma (or another tool) as **source of truth** is **not assumed** ([design-layer-model.md](design-layer-model.md)). Future **artifact generation** (files, exports, design tokens JSON) may attach to **`design_handoff_id`** as out-of-band assets; v0 **does not** define URLs, plugin APIs, or folder layouts. Anything not specified → **SAFE_UNKNOWN_notes**.

---

## Non-runtime boundary

This contract is **documentation and human/agent authoring guidance** only. It is **not** executed by `mars-runtime`, **not** an API payload, and **not** evidence of orchestration. No field here implies a running **MARS** pipeline unless separate implementation exists in-repo.

---

## Required fields (v0)

Each design handoff is a **logical document** (one Markdown section per page or handoff instance). Fields are **required** unless marked optional. Use **`n/a`** only when consciously inapplicable **and** **SAFE_UNKNOWN_notes** explains why.

| Field | Role |
|--------|------|
| **design_handoff_id** | Stable ID for this handoff instance (project-scoped; pairs with one primary page or canonical variant). |
| **source_blueprint_id** | **`blueprint_id`** from [Page Blueprint Contract v0](page-blueprint-contract-v0.md). |
| **site_type_id** | From [Site Type Registry v0](site-type-registry-v0.md); must match blueprint unless divergence is documented in **SAFE_UNKNOWN_notes**. |
| **visual_direction** | Overall look/feel: density, imagery vs type, key references (links or internal mood IDs in prose). |
| **brand_context** | Logo usage, voice, competitive differentiation, **must-not** brand moves. |
| **moodboard_notes** | Themes, palette seeds, photography style — **not** a substitute for **color_direction** / tokens. |
| **design_goals** | What “good” looks like for this page (clarity, trust, speed-to-CTA, etc.). |
| **conversion_goals** | Visual support for blueprint **conversion_points** (primary/secondary emphasis, repetition, urgency **without** dark patterns). |
| **SEO_visibility_constraints** | H1/H2 treatment, FAQ visibility, schema-related **on-page** truth (no decorative fake FAQ). |
| **typography_direction** | Roles (display, body, UI), scale intent, max line length — aligned with Design System Rules where present. |
| **color_direction** | Semantic roles (primary, surface, danger, success), contrast intent — aligned with tokens. |
| **spacing_system** | Vertical rhythm, section padding intent, card internal spacing — aligned with scale or **SAFE UNKNOWN**. |
| **section_visual_map** | Per **`block_id`** (from blueprint): layout intent, imagery, key components, hierarchy vs siblings. |
| **component_variants** | States needed: default, hover, focus, disabled, error, loading — per interactive blocks. |
| **responsive_behavior** | Mobile vs desktop priorities, collapses, sticky behavior, **sticky_cta** rules vs blueprint. |
| **motion_guidelines** | Allowed motion (none / subtle / rich), reduced-motion respect — **optional** if **`n/a`** and explained. |
| **asset_requirements** | Photos, icons, illustrations, fonts — format hints, aspect ratios, **license** notes. |
| **accessibility_notes** | Focus order highlights, contrast targets, non-color cues, motion sensitivity. |
| **forbidden_visual_patterns** | e.g. fake urgency, stock “trust” clichés if brand forbids, low-contrast text on CTAs. |
| **QA_requirements** | Design-layer checks beyond blueprint (e.g. all states designed, alt text prompts for devs). |
| **HITL_required** | `rare` \| `selective` \| `often` \| `yes` — before **frontend handoff** or build. |
| **SAFE_UNKNOWN_notes** | Tooling gaps, unresolved brand decisions, token TBDs. |

---

## Example — `service_landing` design handoff

| Field | Example value |
|--------|----------------|
| **design_handoff_id** | `dh_svc_roof_inspection_moscow_v1` |
| **source_blueprint_id** | `svc_roof_inspection_moscow_v1` |
| **site_type_id** | `service_landing` |
| **visual_direction** | Confident, local craftsperson tone; photography-led hero; minimal decorative chrome; single-column mobile, two-column only where proof (cases) benefits. |
| **brand_context** | Primary green from brand kit; no “storm chaser” alarmist imagery; helmet/roof shots authentic only. |
| **moodboard_notes** | “Quiet competence” refs: matte surfaces, daylight, hands-on detail; avoid generic stock families. |
| **design_goals** | Scan-and-act: problem → proof → process → quote; hero readable in under 3s on 375px width. |
| **conversion_goals** | Primary **lead_form** visually dominant after **process_steps**; tap targets ≥44px; **sticky_cta** mirrors hero label only (no competing copy). |
| **SEO_visibility_constraints** | One clear H1 in **hero**; FAQ accordion **full text** on-page for FAQ schema honesty; no hidden tab-only answers. |
| **typography_direction** | Strong condensed display for H1 (within licensed family); 16px body min; UI labels sentence case. |
| **color_direction** | Primary CTA solid fill; destructive never used for primary CTA; focus ring 2px brand-secondary. |
| **spacing_system** | 8px base; section vertical rhythm 64/96 desktop, 48 mobile; cards 24px internal padding. |
| **section_visual_map** | **hero:** full-bleed image left 50% desktop; **trust_block:** icon row + 3 proof chips; **process_steps:** horizontal stepper desktop, vertical mobile; **faq:** accordion with visible first answer. |
| **component_variants** | **lead_form:** empty, validating, error summary, success thank-you; **accordion:** open/closed + focus within. |
| **responsive_behavior** | **sticky_cta** after first scroll on viewports below 768px only; hero image crop center-weighted. |
| **motion_guidelines** | Subtle 200ms ease on accordion; **prefers-reduced-motion:** instant open/close. |
| **asset_requirements** | Hero 2400×1600 WebP source; case before/after pairs; license doc for font + stock. |
| **accessibility_notes** | Accordion headers are buttons; form errors linked with `aria-describedby`; review contrast on green CTA with white text. |
| **forbidden_visual_patterns** | Fake countdown timers; unverifiable star ratings; “100% satisfaction” badges without policy link. |
| **QA_requirements** | All blueprint **required_sections** have desktop + mobile frames; focus states visible; no text in images for body copy. |
| **HITL_required** | `selective` — client sign-off on photography and pricing-adjacent UI. |
| **SAFE_UNKNOWN_notes** | Final Figma component library version **TBD**; export token JSON path **unknown** until design ops defines it. |

---

*Contract version: v0 — documentation only; last updated 2026-05-11.*
