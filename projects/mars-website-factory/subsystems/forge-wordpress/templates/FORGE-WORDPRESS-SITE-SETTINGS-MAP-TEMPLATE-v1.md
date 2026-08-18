# {PROJECT-ID} — Site Settings Map v1

**Artifact ID:** SITE-SETTINGS-MAP  
**Project:**  
**Date:**  
**Standard:** [FW-S-11](../standards/FORGE-WORDPRESS-SITE-SETTINGS-STANDARD-v1.md) · [FW-S-30](../standards/FORGE-WORDPRESS-GLOBAL-SETTINGS-OWNERSHIP-STANDARD-v1.md)

---

## Options pages / tabs

| # | Tab (editor label) | Responsibility | Fields (names) | Consumers | Visibility / caps | Empty behavior |
|---|--------------------|----------------|----------------|-----------|-------------------|----------------|
| 1 | Общие | | | chrome | editor | |
| 2 | Контакты | | | header/footer/contacts | editor | hide empty tel/mail |
| 3 | Соцсети и мессенджеры | | | header/footer/mobile | editor | no empty icons |
| 4 | SEO и интеграции | | | wp_head | editor / admin | empty → no tag |
| 5 | Modules (search, etc.) | | | if enabled | | |
| 6 | Advanced code | head/body/footer HTML | | hooks | **Administrator only** | empty → no output |

System status: Dashboard widget — **not** a settings tab.

---

## Social / messenger registry (if used)

| Platform type | URL field | Header | Footer | Icon source |
|---------------|-----------|--------|--------|-------------|
| | | y/n | y/n | derived from type |

---

## Global CTA defaults

| Field | Used when page/entity CTA is empty |
|-------|-------------------------------------|
| | |

---

## Out of scope (must not live here)

| Tempting item | Correct owner |
|---------------|---------------|
| | page / CPT |

---

*One SoT. Advanced last. No demo defaults.*
