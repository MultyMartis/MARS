# {PROJECT-ID} — Component Data Contract — {component-id}

**Artifact ID:** COMPONENT-DATA-CONTRACT  
**Component ID:**  
**Project:**  
**Date:**  
**Standard:** [FW-S-27](../standards/FORGE-WORDPRESS-COMPONENT-DATA-CONTRACT-STANDARD-v1.md)

---

## Identity

| Slot | Value |
|------|-------|
| Purpose | |
| Owner | page ACF / CPT / Options / hardcoded / mixed |
| Source type | structured template / flex layout / Gutenberg / chrome helper |
| Theme partial | |
| Assembler / helper | |

---

## Data contract

| Field | Type | Required | Owner | Empty behavior |
|-------|------|----------|-------|----------------|
| | | y/n | | hide / fallback / invalid |

---

## Variants

| Enum | Values | Who may set |
|------|--------|-------------|
| | | editor \| theme-only |

---

## Presentation surfaces

| Surface | Fields used |
|---------|-------------|
| Collection card | |
| Single | |
| Admin-only | |

---

## Rendering contract

| Step | Notes |
|------|-------|
| INPUT | |
| NORMALIZATION (owner) | |
| VALIDATION | unpublished related → |
| EMPTY STATE | |
| HTML / a11y | heading level, alt, control type |
| RESPONSIVE | CSS only unless |
| EDITOR SOURCE | Admin path + help sentence |

---

## Accessibility / motion

| Requirement | |
|-------------|--|
| Decorative vs meaningful image | |
| `prefers-reduced-motion` | |

---

*One contract per component. No demo fallback.*
