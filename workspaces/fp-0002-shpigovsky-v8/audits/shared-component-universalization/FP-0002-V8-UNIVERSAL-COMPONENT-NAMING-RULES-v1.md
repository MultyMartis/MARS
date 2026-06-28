# FP-0002 V8 — Universal Component Naming Rules v1

**Date:** 2026-06-28  
**Authority:** Operator decision CF-003 + V8 consolidation charter  
**Status:** DOCUMENTATION ONLY

---

## 1. Global shared components

A component used on two or more page templates **must not** receive a page prefix in:

- partial filename
- root CSS class family
- section wrapper class (unless wrapper is genuinely unique layout shell)

Forbidden prefixes for shared components: `home-`, `page-home-`, `service-`, `service-leaf-`, `service-subdivision-`, `services-` (when function is global), `page-uslugi-`, `about-`, `o-centre-`.

## 2. Name describes function or visual pattern

Names must describe **what the block does** or **what it looks like**, not where it first appeared.

Examples:

| Wrong (page-named) | Right (neutral) |
|---|---|
| `home-founder-quote` | **`founder-quote`** (CF-004 COMPLETE) |
| `home-specialists` | `specialists` (COMPLETE) |
| `home-comfort` | `comfort-gallery` / `facility-comfort` (operator to decide) |

## 3. One component = one partial

- One visual block → one `@@include` partial
- No HTML copy between pages
- No parallel partial clones for the same visual block

## 4. One class family = one CSS source

- One neutral root class family
- One SCSS block (scoped children allowed)
- No page-body activation for shared geometry
- No duplicate responsive rule sets under page wrappers

## 5. Modifiers

Modifiers (`--variant-b`, `--subdivision`) are allowed **only** for proven visual variation.

Content differences (copy, ids, images, links) are **not** a reason for a new component class.

## 6. Include over copy

Pages pass **data parameters** to shared includes. Pages do not embed block HTML.

## 7. New class gate

Before creating any new root component class, verify:

1. No existing shared partial can be reused
2. Visual pattern is not already covered by a `home-*` misnamed block
3. Operator wave is chartered

## 8. Page-specific exceptions

A block may remain page-specific only when:

- It appears on exactly one template **and**
- Reuse is not planned on canonical roadmap **and**
- `REUSE_IMPOSSIBILITY_PROVEN` is documented

Otherwise classify as `SHARED_BUT_PAGE_NAMED` and schedule universalization.

---

## CF-003 reference implementation

```
ONE VISUAL BLOCK
→ ONE SHARED INCLUDE (internal-page-nav.html)
→ ONE HTML STRUCTURE
→ ONE NEUTRAL CLASS (.internal-page-nav)
→ ONE CSS SOURCE
→ ONE RESPONSIVE BEHAVIOR
```

All future waves must follow this pattern.
