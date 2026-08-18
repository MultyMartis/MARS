# {PROJECT-ID} — Admin Information Architecture v1

**Artifact ID:** ADMIN-INFORMATION-ARCHITECTURE  
**Project:**  
**Date:**  
**Standard:** [FW-S-25](../standards/FORGE-WORDPRESS-ADMIN-INFORMATION-ARCHITECTURE-STANDARD-v1.md)

Complements ADMIN-UX-MAP. This artefact is the **menu + screen structure** plan.

---

## Left menu (client-visible)

| Order | Label | Target | Visible to |
|-------|-------|--------|------------|
| 1 | | CPT/pages | editor |
| | Настройки сайта | options | editor |
| | Advanced / tools | | administrator only |

Hidden from client:  
| Item | Reason |
|------|--------|
| | |

---

## CPT list tables

| CPT | Columns | Hidden default columns | Default sort |
|-----|---------|------------------------|--------------|
| | image, title, type, order, status | comments, date? | menu_order |

---

## Entity edit screens

| Entity | Native shown | Native hidden | ACF groups / tabs (order) | Screen-length notes |
|--------|--------------|---------------|---------------------------|---------------------|
| | title, slug, featured image, status | parent, excerpt, editor | Основное → … → SEO → Дополнительно | |

Permalink: native row only.

---

## Site Settings tabs

| Order | Tab | Caps |
|-------|-----|------|
| last | Advanced code | administrator |

---

## Gutenberg vs ACF by type

| post type | Editor |
|-----------|--------|
| page (curated) | ACF |
| post | |
| {cpt} | ACF |

---

*Business concepts first. Dangerous last.*
