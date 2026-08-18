# Forge WordPress — Design-to-CMS Workflow v1

**ID:** FW-S-28  
**Status:** ACTIVE — PRODUCTION-INFORMED  
**Date:** 2026-08-18  
**Companion:** [CMS ARCHITECTURE](FORGE-WORDPRESS-CMS-ARCHITECTURE-STANDARD-v1.md)

```text
FIGMA / PAGE DESIGN CAN BE TRANSLATED INTO A REPEATABLE CMS MODEL
BEFORE IMPLEMENTATION.
```

Do **not** open ACF and “add fields until the mockup is covered.”

Worksheet: [DESIGN-TO-CMS-MAPPING-WORKSHEET](../templates/FORGE-WORDPRESS-DESIGN-TO-CMS-MAPPING-WORKSHEET-v1.md).

---

## Repeatable workflow

### STEP 1 — Mark all visible content elements

Walk the design top to bottom. Include chrome (header/footer/mobile), hidden states (offcanvas, modal), and SEO-only strings if shown in specs.

### STEP 2 — Classify each element

| Class | Meaning |
|-------|---------|
| **STATIC SYSTEM** | Hardcoded / theme invariant |
| **GLOBAL** | Site Settings / chrome SoT |
| **PAGE-LOCAL** | This route/template only |
| **ENTITY** | First-class object |
| **RELATIONSHIP** | Pointer to an object/term |
| **REPEATING** | Parent-owned rows **or** a collection (decide in step 4) |
| **MEDIA** | Attachment vs decorative |
| **CTA** | Typed action |

### STEP 3 — Identify reuse across templates

Same phone? Same CTA band? Same card type on Home and hub? Same specialist on several services? Reuse ⇒ one owner.

### STEP 4 — Choose storage

Apply [CMS ARCHITECTURE](FORGE-WORDPRESS-CMS-ARCHITECTURE-STANDARD-v1.md) §4 and [REPEATER VS ENTITY](FORGE-WORDPRESS-REPEATER-VS-ENTITY-DECISION-MATRIX-v1.md). Fill CONTENT-ENTITY-MAP + FIELD-OWNERSHIP-MAP.

### STEP 5 — Define field schema

Semantic field library ([ACF FIELD MODELING](FORGE-WORDPRESS-ACF-FIELD-MODELING-STANDARD-v1.md)). Conditionals for CTA types. No duplicate alts. No per-template phones.

### STEP 6 — Define frontend contract

One contract per component ([FW-S-27](FORGE-WORDPRESS-COMPONENT-DATA-CONTRACT-STANDARD-v1.md)). Empty states. Variants as enums.

### STEP 7 — Define Admin UX

Menu, groups, list tables, labels, Advanced boundary ([ADMIN IA](FORGE-WORDPRESS-ADMIN-INFORMATION-ARCHITECTURE-STANDARD-v1.md) · [EDITOR UX](FORGE-WORDPRESS-EDITOR-UX-STANDARD-v1.md)).

### STEP 8 — Validate with an editor **before** treating the model as done

Walk the [EDITOR-WORKFLOW-ACCEPTANCE-CHECKLIST](../templates/FORGE-WORDPRESS-EDITOR-WORKFLOW-ACCEPTANCE-CHECKLIST-v1.md). On a new site this may be a **tabletop** review of the maps before code; after Admin exists it must be a real wp-admin walkthrough.

---

## Mapping to Factory artefacts

| Factory / Forge artefact | Role |
|--------------------------|------|
| Frontend block inventory | STEP 1 input |
| BLOCK-TO-WP-MAPPING | Presentation wiring **after** CMS maps exist |
| CONTENT-MODEL (FW-T-04) | Summary of STEP 4 |
| This workflow pack | Ownership that BLOCK-TO-WP cannot invent |

**Rule:** BLOCK-TO-WP-MAPPING must not be the first place a phone or CPT is decided.

---

## Stop conditions

Stop and fix the maps if:

- two owners for one business value;  
- 12 same-class cards with no entity decision;  
- Flexible Content proposed as default page builder;  
- internal links planned as absolute URLs;  
- “make everything editable” with no editor role story.

---

*FW-S-28 v1 — design annotated, then storage, then fields, then Admin.*
