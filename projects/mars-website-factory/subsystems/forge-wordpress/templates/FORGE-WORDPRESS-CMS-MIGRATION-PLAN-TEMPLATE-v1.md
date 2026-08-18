# {PROJECT-ID} — CMS Migration Plan v1

**Artifact ID:** CMS-MIGRATION-PLAN  
**Project:**  
**Date:**  
**Trigger:** field rename / move / repeater→CPT / relationship change / Page→CPT  
**Standard:** [CMS ARCHITECTURE](../standards/FORGE-WORDPRESS-CMS-ARCHITECTURE-STANDARD-v1.md) §21 · [FW-S-10](../standards/FORGE-WORDPRESS-CONTENT-MODEL-CPT-STANDARD-v1.md) §3

Use when data already exists. Greenfield: write “N/A — no production content.”

---

## 0. Case study pattern (anonymized)

Specialists as child Pages → CPT: keep IDs; `post_parent=0`; preserve `post_name`; move ACF location; delete leftover `_wp_page_template`; flush rewrite once; retarget search + sitemap; keep user-visible search group label stable.

---

## Stages

| # | Stage | Plan / evidence | Done |
|---|-------|-----------------|------|
| 1 | Inventory | objects, meta keys, URLs, relations | ☐ |
| 2 | Mapping | old owner → new owner | ☐ |
| 3 | Dry-run | counts, sample permalinks | ☐ |
| 4 | Backup | named files+DB | ☐ |
| 5 | Create / retarget objects | post_type / new posts | ☐ |
| 6 | Copy fields | ACF names, galleries as IDs | ☐ |
| 7 | Preserve slugs/URLs | `post_name`, rewrite | ☐ |
| 8 | Update relationships | IDs not URLs | ☐ |
| 9 | Update queries / search / sitemap | no duplicate Page hits | ☐ |
| 10 | Verify | Admin list, singles, chrome, SEO | ☐ |
| 11 | Retire old owner | remove fields/locations; no dual SoT | ☐ |
| 12 | Rollback plan | restore backup; rewrite flush | ☐ |

---

## Mapping table

| Old (post type / field) | New | Transform | URL impact |
|-------------------------|-----|-----------|------------|
| | | | none / preserve |

---

## Dual-write window

| Allowed? | Max duration | Who may edit |
|----------|--------------|--------------|
| no (default) | | |

---

## Rollback

| Step | Command / SOP |
|------|----------------|
| | [BACKUP-ROLLBACK](../runbooks/FORGE-WORDPRESS-BACKUP-ROLLBACK-STANDARD-v1.md) |

---

*Do not silently orphan ACF meta.*
