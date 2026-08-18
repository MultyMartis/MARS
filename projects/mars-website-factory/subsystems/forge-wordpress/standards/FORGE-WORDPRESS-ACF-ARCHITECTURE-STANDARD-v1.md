# Forge WordPress ACF Architecture Standard v1

**Document type:** Architecture standard (L4/L6)  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-02  
**Rules source:** R-ACF-01–04; [FORGE-WORDPRESS-ARCHITECTURAL-DECISIONS-v1.md](../FORGE-WORDPRESS-ARCHITECTURAL-DECISIONS-v1.md)

**Position:** ACF = **preferred pragmatic layer**, **not** mandatory for every project.

---

## 1. When ACF is used

| Condition | Requirement |
|-----------|-------------|
| ACF selected in WAD | Full standard applies |
| No ACF | Document alternative in WAD (core meta, block attributes) |
| ACF Pro features | Repeater, Flexible Content, Options Page, Clone — declare in PLUGIN-REGISTER |

---

## 2. ACF Pro requirement conditions

ACF Pro required when project uses:

- Repeater or Flexible Content at scale
- Options Pages for globals
- Clone fields for DRY field groups
- ACF Blocks (Mode A/B hybrid)

Free ACF acceptable for trivial field sets — document in WAD.

---

## 3. Local JSON policy

| Rule | ID |
|------|-----|
| Local JSON **required** when ACF is used | R-ACF-01 |
| JSON path declared in IMPLEMENTATION-SPEC | — |
| JSON committed to Git with code | R-ACF-02 |
| Sync on deploy documented | — |
| DB is not schema SoT | R-VC-06 |

Typical path: `{functionality-plugin}/acf-json/` or theme-declared path **only** if WAD justifies.

---

## 4. Naming model

### Field names

Format: `<context>_<entity>_<field>`

| Good | Bad |
|------|-----|
| `home_hero_title` | `field_1` |
| `service_card_icon` | `text_2` |
| `global_contact_phone` | `new_block` |
| `about_team_member_name` | `content_left` |
| | `data`, `value` |

### Field group names

Format: `<scope> — <entity>` (human label); machine key: `group_<context>_<entity>`

Examples:

- `group_home_hero`
- `group_service_landing_sections`
- `group_global_site_options`

### Field keys

- Let ACF generate `field_*` keys — **do not** hand-edit keys after first save
- Renaming field **name** requires migration plan — WV3 blocks silent renames

---

## 5. Field group scope

| Scope | Location rule |
|-------|---------------|
| Page-specific | Location rules: Page Template or specific page |
| CPT | Location: Post Type = `{cpt}` |
| Taxonomy | Location: Taxonomy = `{tax}` |
| Global | Options Page — functionality plugin registered |
| User | Rare — charter only |

One group per logical editorial unit — avoid mega-groups without tabs.

---

## 6. Structural field policies

| Field type | Policy |
|------------|--------|
| **Repeater** | Prefer over Flexible Content for uniform lists; max depth documented |
| **Flexible Content** | **Not** default page builder; each layout named and mapped in TEMPLATE-MAP; max layouts per project documented |
| **Clone** | Use for shared field sets — source group documented |
| **Relationship** | Prefer for entity links over post ID text fields |
| **Gallery** | Image size recommendations in instructions |
| **WYSIWYG** | Restricted toolbar where curated editor applies |

**Flexible Content blocking rule:** If Flexible Content replaces entire page structure without WAD section map → **BLOCKER** WV1.

---

## 7. Editorial quality

| Element | Requirement |
|---------|-------------|
| **Labels** | Human-readable Russian or project locale |
| **Instructions** | Image dimensions, character limits, examples |
| **Validation** | Required fields where business-critical |
| **Conditional logic** | Document in ADMIN-UX-MAP |
| **Default values** | Safe defaults only — no lorem in production |
| **REST exposure** | Explicit per field if headless/API — default off |

---

## 8. Schema changes and migrations

| Change type | Process |
|-------------|---------|
| New field | JSON commit + WV3 sync check |
| Rename field | Migration script or manual remap — document |
| Remove field | Deprecation note; data export if needed |
| Environment sync | Pull JSON → Sync available in admin on DEV |

**Drift prevention:** ACF UI edits on production without JSON commit → **MAJOR** violation.

---

## 9. Blocking violations

| Violation | Severity |
|-----------|----------|
| ACF used without Local JSON in Git | **BLOCKER** |
| Generic field names (`field_1`, `data`) | **BLOCKER** |
| Flexible Content as universal page builder | **BLOCKER** |
| Field groups registered only in theme | **BLOCKER** |
| ACF Pro dependency undeclared | **BLOCKER** |
| JSON out of sync with DB on release | **BLOCKER** WV3 |
| Missing instructions on image fields | **MAJOR** |
| REST expose on sensitive fields | **BLOCKER** WV4 |

---

## Related documents

- [FORGE-WORDPRESS-CMS-ARCHITECTURE-STANDARD-v1.md](FORGE-WORDPRESS-CMS-ARCHITECTURE-STANDARD-v1.md)
- [FORGE-WORDPRESS-ACF-FIELD-MODELING-STANDARD-v1.md](FORGE-WORDPRESS-ACF-FIELD-MODELING-STANDARD-v1.md)
- [FORGE-WORDPRESS-CONTENT-MODELING-STANDARD-v1.md](FORGE-WORDPRESS-CONTENT-MODELING-STANDARD-v1.md)
- [FORGE-WORDPRESS-ADMIN-UX-STANDARD-v1.md](FORGE-WORDPRESS-ADMIN-UX-STANDARD-v1.md)
- [templates/FORGE-WORDPRESS-ACF-SCHEMA-TEMPLATE-v1.md](../templates/FORGE-WORDPRESS-ACF-SCHEMA-TEMPLATE-v1.md)

---

*ACF architecture standard v1 — conditional application; not mandatory system law.*
