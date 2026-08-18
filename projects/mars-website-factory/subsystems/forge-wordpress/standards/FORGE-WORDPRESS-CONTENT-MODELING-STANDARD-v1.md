# Forge WordPress Content Modeling Standard v1

**Document type:** Architecture standard (L4)  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-02  
**Rules source:** R-TF-02; [FORGE-WORDPRESS-ARCHITECTURAL-DECISIONS-v1.md](../FORGE-WORDPRESS-ARCHITECTURAL-DECISIONS-v1.md)

**Artifact:** [FORGE-WORDPRESS-CONTENT-MODEL-TEMPLATE-v1.md](../templates/FORGE-WORDPRESS-CONTENT-MODEL-TEMPLATE-v1.md)

---

## 1. Purpose

Define how Forge WordPress projects choose between WordPress content primitives. Prevents automatic CPT proliferation and theme-dependent business entities.

---

## 2. Content primitive selection

| Primitive | Use when |
|-----------|----------|
| **page** | Static route; single URL; no archive; editorial shell |
| **child page** | Hierarchy under parent; breadcrumbs; no separate archive need |
| **CPT** | Independent lifecycle; own URL/archive; filtering; reuse; API need |
| **taxonomy** | Real classification, filtering, archive, or URL segmentation |
| **native WP fields** | Title, excerpt, featured image sufficient |
| **post meta** | Single-value attributes tied to one post |
| **term meta** | Attributes on taxonomy terms |
| **options** | Site-wide globals (phone, address, social) |
| **repeater** | Ordered repeating sub-fields (ACF or equivalent) |
| **relationship** | Explicit links between entities |
| **reusable block** | Editor-managed fragment in hybrid zones (Mode B) |
| **pattern** | Locked layout template in block editor |
| **fixed template content** | Non-editable markup in theme — Factory-frozen regions |

---

## 3. CPT rules

**CPT is not created automatically for every repeated entity.**

Evaluate before CPT:

| Criterion | Question |
|-----------|----------|
| Independent lifecycle | Can items be added/removed without page edits? |
| Separate URL | Does each item need its own permalink? |
| Archive | Is a list/archive page required? |
| Filtering | Taxonomy or faceted browse? |
| Reuse | Same entity on multiple pages? |
| Independent editing | Different editor role or workflow? |
| API need | REST/headless consumption? |

**If majority = no** → prefer page + repeater, fixed template, or options — document in CONTENT-MODEL.

**Production expansion (2026-08-18):** full CPT checklist — [FORGE-WORDPRESS-CONTENT-MODEL-CPT-STANDARD-v1.md](FORGE-WORDPRESS-CONTENT-MODEL-CPT-STANDARD-v1.md) (FW-S-10).

**CMS / editable architecture (2026-08-18):** deterministic Page/Post/CPT/taxonomy/Options/repeater/Flexible Content/relationship decisions, field ownership, and design-to-CMS workflow — [FORGE-WORDPRESS-CMS-ARCHITECTURE-STANDARD-v1.md](FORGE-WORDPRESS-CMS-ARCHITECTURE-STANDARD-v1.md) (FW-S-22). Repeater vs entity: [FW-S-24](FORGE-WORDPRESS-REPEATER-VS-ENTITY-DECISION-MATRIX-v1.md). Do not use generic Pages for staff-like public entities (AP-001 / AP-CMS-001).

**§7 matrix note:** “Team cards on one page → repeater” and “nested services → child page” are **first-pass hints only**. Production: public people/services with URLs → CPT (FW-S-10 + FW-S-24). This older table does not override FW-S-22.

---

## 4. Taxonomy rules

Create taxonomy **only** when there is:

- real classification need;
- archive or filter UX;
- URL segment value;
- editorial grouping.

**Do not** create taxonomies as mere "categories for one CPT" without archive/filter benefit.

---

## 5. Theme independence

Persistent business/content entities **must not** depend on active theme without WAD justification.

| Belongs in functionality plugin | Belongs in theme |
|--------------------------------|------------------|
| CPT / taxonomy registration | Template presentation |
| Portable field registrations | Visual layout |
| Business hooks | Asset enqueue for presentation |

Violation: **BLOCKER** at WV1 — R-TF-02.

---

## 6. SEO and URL

Content model must document:

| Concern | Required in CONTENT-MODEL |
|---------|---------------------------|
| URL structure | Slugs, prefixes, trailing rules |
| Hierarchy | Parent/child, breadcrumbs source |
| Indexability | noindex pages, thin archives |
| Archive value | Whether archive pages are public |
| Duplicates | Canonical behavior for similar content |
| Breadcrumbs | Data source |
| Canonical behavior | Plugin dependency (e.g. SEO plugin) |

---

## 7. Decision matrix

| Need | page | child | CPT | taxonomy | repeater | options |
|------|------|-------|-----|----------|----------|---------|
| Single corporate page | ● | | | | | |
| Nested services tree | | ● | | | | |
| News/blog with archives | | | ● | ● | | |
| Team cards on one page | | | | | ● | |
| Site phone/address | | | | | | ● |
| Product catalog | | | ● | ● | | |
| FAQ accordion content | ● | | | | ● | |

● = typical first choice — WAD may override with justification.

---

## 8. Anti-patterns

| Anti-pattern | Severity | Remediation |
|--------------|----------|-------------|
| CPT for every card grid on a landing | MAJOR | Repeater or fixed template |
| Taxonomy with one term | WARNING | Remove or merge |
| Business data only in theme options | BLOCKER | Functionality plugin |
| Duplicate URL for same content | BLOCKER | Canonical + model fix |
| "Posts" used as generic CPT | WARNING | Register proper CPT |
| Flexible content as default page model | MAJOR | See ACF standard |

---

## Related documents

- [FORGE-WORDPRESS-CMS-ARCHITECTURE-STANDARD-v1.md](FORGE-WORDPRESS-CMS-ARCHITECTURE-STANDARD-v1.md)
- [FORGE-WORDPRESS-ACF-ARCHITECTURE-STANDARD-v1.md](FORGE-WORDPRESS-ACF-ARCHITECTURE-STANDARD-v1.md)
- [FORGE-WORDPRESS-FUNCTIONALITY-PLUGIN-STANDARD-v1.md](FORGE-WORDPRESS-FUNCTIONALITY-PLUGIN-STANDARD-v1.md)
- [templates/FORGE-WORDPRESS-CPT-TAXONOMY-MAP-TEMPLATE-v1.md](../templates/FORGE-WORDPRESS-CPT-TAXONOMY-MAP-TEMPLATE-v1.md)
- [templates/FORGE-WORDPRESS-CONTENT-ENTITY-MAP-TEMPLATE-v1.md](../templates/FORGE-WORDPRESS-CONTENT-ENTITY-MAP-TEMPLATE-v1.md)

---

*Content modeling standard v1 — L4; not implementation.*
