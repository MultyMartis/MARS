# Forge WordPress — Component Data Contract Standard v1

**ID:** FW-S-27  
**Status:** ACTIVE — PRODUCTION-INFORMED  
**Date:** 2026-08-18  
**Companion:** [CMS ARCHITECTURE](FORGE-WORDPRESS-CMS-ARCHITECTURE-STANDARD-v1.md) · [DESIGN-TO-CMS](FORGE-WORDPRESS-DESIGN-TO-CMS-WORKFLOW-v1.md)

This is the shared language between Figma/design, CMS model, PHP, and frontend CSS/JS.

```text
ONE COMPONENT = ONE DATA CONTRACT = ONE EMPTY-STATE RULE.
```

---

## 1. Component registry model

Every frontend component that consumes editable (or global) data documents:

| Slot | Meaning |
|------|---------|
| component ID | kebab-case, stable (`hero-service`, `card-specialist`) |
| purpose | one sentence |
| data contract | fields + types |
| owner | page ACF / CPT / Options / hardcoded / mixed |
| source type | structured template / flex layout / Gutenberg / chrome helper |
| required fields | invalid without these |
| optional fields | hide when empty |
| supported variants | enums only |
| empty-state behavior | hide component / hide row / global fallback / block publish |
| responsive behavior | design note; not extra CMS fields by default |
| accessibility | heading level, alt, button vs link, reduced motion |
| editor instructions | where it is edited |

Template: [COMPONENT-DATA-CONTRACT](../templates/FORGE-WORDPRESS-COMPONENT-DATA-CONTRACT-TEMPLATE-v1.md).

This registry is what makes Figma → WordPress schema mapping repeatable.

---

## 2. Rendering contract (canonical)

For each component, implement in this order:

1. **INPUT DATA** — from the assembler, not ad-hoc template lookups  
2. **NORMALIZATION** — one owner (phone, typography, URL, social icon, SEO fallback, reading time)  
3. **VALIDATION** — skip invalid related objects  
4. **EMPTY STATE** — explicit  
5. **HTML** — theme partial  
6. **ACCESSIBILITY**  
7. **RESPONSIVE** — CSS; no extra editor knobs unless designed  
8. **EDITOR SOURCE** — documented Admin path  

Templates must not reimplement fallback/normalization.

---

## 3. Empty-state frontend contract

Every component answers: **what happens if data is empty?**

| Option | When |
|--------|------|
| Hide component | Optional section; no meaningful content |
| Hide row | Repeater/relation item invalid or empty |
| Use global fallback | Designed chain (CTA label) |
| Block publishing | Required entity (rare; prefer Admin validation) |

**No accidental blank UI.** No empty cards, empty icons, blank headings, placeholder Lorem, demo fallback (AP-CMS-010 / AP-009).

---

## 4. Three presentation contracts per entity

Do not dump the Admin record into the card.

| Contract | Typical fields |
|----------|----------------|
| ADMIN RECORD | full schema |
| COLLECTION CARD | image, title, role/type, short text, permalink |
| SINGLE PAGE | card fields + body sections + gallery + SEO (output) |

---

## 5. Variants

Controlled selects only. Theme owns color/type/spacing. See ACF Field Modeling §9.

---

## 6. Mixed sources

A component may combine:

- page-local heading;  
- global phone;  
- related CPT cards.

The contract lists **each field’s owner**. The partial still receives one normalized array so the template does not know about three ACF locations.

---

*FW-S-27 v1 — contracts before markup.*
