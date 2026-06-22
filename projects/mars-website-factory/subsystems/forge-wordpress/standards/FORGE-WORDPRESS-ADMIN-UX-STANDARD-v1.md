# Forge WordPress Admin UX Standard v1

**Document type:** Editorial UX standard (L7)  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-02  
**Rules source:** R-UX-01–04; [FORGE-WORDPRESS-ARCHITECTURAL-DECISIONS-v1.md](../FORGE-WORDPRESS-ARCHITECTURAL-DECISIONS-v1.md)

**Principle:** `Curated editor, not unrestricted editor.`

---

## 1. Purpose

Define how WordPress admin presents editable content to clients and editors — minimal surface, clear labels, protected structure.

**Artifact:** [FORGE-WORDPRESS-ADMIN-UX-MAP-TEMPLATE-v1.md](../templates/FORGE-WORDPRESS-ADMIN-UX-MAP-TEMPLATE-v1.md)

---

## 2. Core rules

| Rule | ID |
|------|-----|
| Only declared fields/sections editable | R-UX-01 |
| Structure and visual constraints protected | R-UX-02 |
| Editor freedom is opt-in per WAD | R-UX-03 |
| Handoff includes frozen vs editable map | R-UX-04 |

---

## 3. Field presentation

| Element | Standard |
|---------|----------|
| **Labels** | Plain language; match client vocabulary |
| **Instructions** | Dimensions, limits, examples under each field |
| **Grouping** | Logical sections — tabs or accordions for 8+ fields |
| **Image fields** | Recommended px dimensions and aspect ratio |
| **Required fields** | Mark required; validate on save |
| **Conditional fields** | Hide irrelevant fields — document logic |
| **Error messages** | Specific ("Hero image must be at least 1920×800") |

---

## 4. WordPress UI curation

| Technique | Use when |
|-----------|----------|
| Hide irrelevant metaboxes | Classic editor clutter |
| Remove unused menu items | Client role simplification |
| Custom menu order | Prioritize content tasks |
| CPT menu icons | Distinct content types |
| Options page for globals | Phone, address, social |
| Block locking | Mode B — frozen patterns |
| `allowed_block_types` | Restrict block inserter |
| Disallow custom CSS in editor | PIXEL_PERFECT protection |

---

## 5. Role limitations

| Role | Typical access |
|------|----------------|
| **Administrator** | Full — operator only on production |
| **Editor** | Curated CPT/pages per map |
| **Author** | Rare — charter only |
| **Client custom role** | WAD-defined — minimal |

Default client role: **cannot** install plugins, edit theme files, or access Site Editor (unless Mode B chartered).

---

## 6. Gutenberg and hybrid zones

| Zone type | Editor experience |
|-----------|-------------------|
| **Frozen** | No block inserter; or locked pattern |
| **Bounded** | Whitelist blocks only |
| **Open** | Charter opt-in — document risk |

Mode A default: **ACF-first** — block editor secondary or disabled on curated templates.

---

## 7. Preview expectations

| Expectation | Detail |
|-------------|--------|
| Preview matches front | WV6 dependency |
| Staging URL documented | If preview requires staging |
| Known preview gaps | Listed in ADMIN-UX-MAP |

---

## 8. Destructive action protection

| Action | Protection |
|--------|------------|
| Delete CPT item | Confirm dialog; trash not bypass |
| Bulk delete | Restrict role |
| Plugin install | Admin only — not client |
| Theme switch | Blocked on production via policy |

---

## 9. Admin UX acceptance checklist

| # | Check | Pass |
|---|-------|------|
| 1 | ADMIN-UX-MAP complete | ☐ |
| 2 | All editable fields have labels + instructions | ☐ |
| 3 | No undeclared Gutenberg freedom | ☐ |
| 4 | Client role cannot install plugins | ☐ |
| 5 | Globals on options page (not scattered) | ☐ |
| 6 | CPT menus ordered and named clearly | ☐ |
| 7 | Editor simulation walkthrough completed | ☐ |
| 8 | Frozen regions verified non-editable | ☐ |
| 9 | WV7 report filed | ☐ |
| 10 | Operator sign-off | ☐ |

**WV7 blocks** if checklist fails items 3, 4, or 8.

---

## Related documents

- [FORGE-WORDPRESS-ACF-ARCHITECTURE-STANDARD-v1.md](FORGE-WORDPRESS-ACF-ARCHITECTURE-STANDARD-v1.md)
- [templates/FORGE-WORDPRESS-EDITABLE-REGIONS-MAP-TEMPLATE-v1.md](../templates/FORGE-WORDPRESS-EDITABLE-REGIONS-MAP-TEMPLATE-v1.md)

---

*Admin UX standard v1 — curated editor principle.*
