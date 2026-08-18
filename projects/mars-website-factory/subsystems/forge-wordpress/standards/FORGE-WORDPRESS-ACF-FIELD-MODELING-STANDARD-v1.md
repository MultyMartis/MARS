# Forge WordPress — ACF Field Modeling Standard v1

**ID:** FW-S-23  
**Status:** ACTIVE — PRODUCTION-INFORMED  
**Date:** 2026-08-18  
**Extends:** [FW-S-02 ACF Architecture](FORGE-WORDPRESS-ACF-ARCHITECTURE-STANDARD-v1.md)  
**Companion:** [CMS ARCHITECTURE](FORGE-WORDPRESS-CMS-ARCHITECTURE-STANDARD-v1.md)

ACF is the preferred pragmatic field layer when selected in the WAD. This document is the **field-level** modeling standard: library, naming, conditionals, required policy, sanitization, source control, versioning. It does not replace FW-S-02 (Local JSON, group scope, blocking violations).

---

## 1. Do not start here

Field groups are step 5+, not step 1. See CMS Architecture modeling sequence. Creating fields before the entity/ownership maps is AP-CMS-011 adjacent: schema without a model.

---

## 2. Standard field-pattern catalog

Use **semantic roles**. Machine names follow §3. Labels follow [EDITOR UX](FORGE-WORDPRESS-EDITOR-UX-STANDARD-v1.md).

### TEXT

| Role | Typical ACF type | Notes |
|------|------------------|-------|
| heading | text | Often optional override of native title |
| subtitle / lead | textarea | Not WYSIWYG |
| eyebrow / kicker | text | Optional; hide when empty |
| description | textarea or basic WYSIWYG | WYSIWYG only if lists/links required |
| short label | text | Buttons, badges |

### MEDIA

| Role | Type | Store |
|------|------|-------|
| image | image | Attachment ID |
| gallery | gallery | Attachment IDs, order = gallery order |
| video | oEmbed or URL | Prefer oEmbed for known providers |
| file | file | Attachment ID |

### CTA

| Role | Type |
|------|------|
| label | text |
| action type | select (internal / external / form / modal / tel / mailto) |
| target | Post Object **or** URL **or** form selector — **conditional** |
| variant | select enum if design allows |
| new tab | true/false, typically only if type=external |

### CONTACT

| Role | Owner |
|------|-------|
| phone / email / messenger | **Site Settings** unless page-owned extra location |
| address | Site Settings or Location entity |

Do not re-declare contact fields on header/footer groups.

### ENTITY

| Role | Type |
|------|------|
| relationship | relationship or post_object |
| taxonomy | taxonomy |
| order | native `menu_order` (page-attributes) unless proven insufficient |

### SECTION

| Role | Type |
|------|------|
| enabled | true_false — only if editors need hide-without-delete |
| variant | select |
| items | repeater **or** relationship |

### SEO

| Role | Type | Owner |
|------|------|-------|
| seo_title | text | public entity group — one owner |
| meta_description | textarea | same |

Do not duplicate SEO between generic Page settings and a module settings screen (AP-017). Fallback: title ← post title; description ← excerpt/lead truncated. See [SEO STANDARD](FORGE-WORDPRESS-SEO-AND-SITEMAP-STANDARD-v1.md).

---

## 3. Machine naming

### Field names

Prefer `<context>_<field>` or `<entity>_<field>` when the group location already scopes context.

| Good | Bad |
|------|-----|
| `hero_eyebrow` | `txt1` |
| `hero_title_override` | `desc2` |
| `specialist_role` | `block_new` |
| `phone_primary` | `foo` |
| `cta_action_type` | `content_left` |

Avoid **unnecessary massive prefixes** if the group is already `group_service_hero` and location is `post_type == service`. Do not invent a second prefix system that disagrees with existing JSON.

Project prefix on **keys** is fine and proven: `group_fp02_*` / `field_fp02_*` as a collision-avoidance strategy. Next site: use a short project prefix in **keys**, keep **names** semantic and portable where data may migrate.

### Field keys

- Stable `field_<project>_<semantic>` **or** ACF-generated `field_*` — pick one project policy in ACF-SCHEMA and keep it.
- **Do not** hand-edit keys after data exists.
- Renaming a field **name** requires a migration plan (FW-S-02 §8).

### Groups

Human title: editor language (`Специалист — профиль`, `Hero страницы услуги`).  
Machine key: `group_<context>_<entity>`.  
One group per logical editorial unit. Tabs inside a group beat mega-flat forms (AP-CMS-007).

---

## 4. Conditional field UX

Use ACF conditional logic aggressively when it **removes** irrelevant fields.

```text
CTA type = internal  → page / post object
CTA type = external  → URL (+ optional new tab)
CTA type = form      → form / action selector
```

Do not show all three at once. Document conditionals in ADMIN-UX-MAP / Admin IA.

---

## 5. Required field policy

Required means: **without this value the entity/component is invalid.**

Do not mark every field required “for completeness.”

| Field | Typical rule |
|-------|----------------|
| Native title | Required (WP) for named entities |
| URL / slug | Native permalink; uniqueness in data layer if needed |
| Image | Required only if the card/single is invalid without it (staff card with photo in the design) |
| CTA | Rarely required; hide component if empty |
| Body | Required for articles; optional for landing sections |
| SEO | Optional with programmatic fallback |

Client-side ACF validation is **convenience**. Server-side (ACF `acf/validate_value`, `wp_insert_post_data`, capability checks) is **authoritative**. Never trust Admin-only JS as the integrity layer.

Examples to validate: URL, email, numeric, repeater min/max, relationship existence, required fields.

---

## 6. Defaults

Defaults may improve speed. They must **not** create visible fake content or irreversible assumptions.

**GOOD:** `enabled = true` where the section is part of the template; breadcrumb visibility default on.  
**BAD:** Lorem ipsum; demo phone; demo social URL; placeholder image ID from another environment.

### 6.1 true_false three-state (mandatory)

ACF/WordPress booleans have **three** semantic states:

| State | Typical storage | Meaning |
|-------|-----------------|---------|
| unset | key missing | Apply schema default / migration fallback |
| false | `0` / `'0'` / boolean false | Editor **explicitly off** |
| true | `1` / `'1'` / boolean true | Editor **explicitly on** |

```text
DEFAULTS APPLY ONLY TO MISSING/UNINITIALIZED STATE,
NOT TO EXPLICIT USER FALSE.
```

**Forbidden** when false is valid:

- `$value ?: $default`
- `empty($value) ? $default : $value` for flags stored as `'0'`
- treating `get_field()` `false` as “missing”
- `(bool) '0'` (PHP: non-empty string is true)

**Required:** `metadata_exists()` (or equivalent) to distinguish unset from stored `0`. Frontend must not hardcode a warning that an Admin checkbox claims to control.

Evidence: FP-0002 P18A legal `legal_demo_marker` — Admin OFF, banner still rendered because the template ignored the field.

---

## 7. WYSIWYG policy

**GOOD:** article body; long editorial content; generic content page body.  
**BAD:** card title; phone; button label; structured feature row; SEO title.

Toolbar: only formats the design system supports. Typical allowlist: bold, italic, lists, links. Heading levels: only those the component CSS implements. No random colors/font sizes unless explicitly required (then Advanced / Admin-only).

Proven pattern: `toolbar: basic`, `media_upload: 0` on profile text blocks; empty → not rendered.

---

## 8. Gutenberg coexistence

| Mode | When |
|------|------|
| **A. Disabled** | Highly structured CPT / PIXEL_PERFECT templates; ACF owns the body |
| **B. Articles only** | `post` uses block editor; CPTs stay ACF |
| **C. Restricted blocks** | Hybrid zones; `allowed_block_types` |
| **D. Full editor** | Charter: page-building project |

Do not default blindly. Mode A is the WP Forge default for curated service sites. See [ADMIN UX](FORGE-WORDPRESS-ADMIN-UX-STANDARD-v1.md) §6.

Hide Classic editor / excerpt / revisions / parent on CPTs when ACF owns the entity.

---

## 9. Presentation variants and color

If editors choose visual variants: **controlled enums** (`theme: light \| dark`, `alignment: left \| center`).

Do **not** expose raw CSS classes or arbitrary style values to client editors (AP-CMS-006).

Brand colors, fonts, and margins are **theme-owned**. Semantic variants only when product requirements justify them.

---

## 10. Sanitization and escaping

| Direction | Rule |
|----------|------|
| **INPUT** | Sanitize by field type (`sanitize_text_field`, `esc_url_raw`, `absint`, email, `wp_kses_post` for rich) |
| **OUTPUT** | Escape by context |

| Output context | Function |
|----------------|----------|
| text | `esc_html` |
| attribute | `esc_attr` |
| URL | `esc_url` |
| controlled rich HTML | `wp_kses_post` |
| textarea display | `esc_textarea` |

Do not apply one generic escape everywhere. Align with [CODING AND SECURITY](FORGE-WORDPRESS-CODING-AND-SECURITY-STANDARD-v1.md). Advanced head/body code: capability-gated, stored separately, output only for Administrators’ configured hooks — still kses/capability reviewed.

---

## 11. ACF JSON / source control (canonical WP Forge)

**Preferred model (proven):** Local JSON in the **functionality plugin** (`acf-json/`), committed with code. DB is not schema source of truth (R-ACF-01, R-VC-06).

| Topic | Policy |
|-------|--------|
| GUI edits on DEV | Allowed; **sync JSON back to Git** in the same change set |
| GUI edits on production | Forbidden as schema SoT — AP-CMS-011 |
| PHP-registered groups | Allowed when WAD chooses code-first; still versioned; do not mix undocumented dual registration |
| Environment sync | Pull JSON → Admin “Sync available” on DEV; deploy JSON with code |
| Local vs prod | Schema must match; **content** (options/postmeta) is environment-specific |

**GUI vs code:** current evidence supports **GUI + Local JSON** as the production-proven path. PHP-registered groups remain valid for small portable modules. Dual SoT without a written owner is a defect.

**NEEDS SECOND PROJECT VALIDATION (J):** whether a shared extracted ACF library (clone groups across sites) is maintainable. Do not invent a conflicting system in this wave.

---

## 12. Field schema versioning

Track production schema changes:

- renamed field;
- field moved between groups;
- repeater → CPT;
- relationship object type changed.

Each change needs: inventory of existing meta, mapping, dry-run, rollback. Avoid silently orphaning ACF data.

---

## 13. Data access on the frontend

Prefer a component assembler / helper that:

1. reads fields;  
2. normalizes (phone, URL, typography owner);  
3. applies empty-state rules;  
4. returns a typed array/object for the template.

Templates should not duplicate fallback chains. One normalization owner per cross-cutting concern.

---

*FW-S-23 v1.1 — field modeling. Schema in Git. Editors see labels, not keys. Boolean three-state in §6.1.*
