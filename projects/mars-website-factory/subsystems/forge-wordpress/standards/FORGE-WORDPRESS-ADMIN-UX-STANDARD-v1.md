# Forge WordPress Admin UX Standard v1

**Document type:** Editorial UX standard (L7)  
**Version:** v1.1  
**Date:** 2026-06-22; production addendum 2026-08-18  
**Stage:** FW-02 + FP-0002 production proven  
**Rules source:** R-UX-01–04; [FORGE-WORDPRESS-ARCHITECTURAL-DECISIONS-v1.md](../FORGE-WORDPRESS-ARCHITECTURAL-DECISIONS-v1.md); [knowledge hub](../knowledge/README.md)

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

- [FORGE-WORDPRESS-CMS-ARCHITECTURE-STANDARD-v1.md](FORGE-WORDPRESS-CMS-ARCHITECTURE-STANDARD-v1.md)
- [FORGE-WORDPRESS-ADMIN-INFORMATION-ARCHITECTURE-STANDARD-v1.md](FORGE-WORDPRESS-ADMIN-INFORMATION-ARCHITECTURE-STANDARD-v1.md)
- [FORGE-WORDPRESS-EDITOR-UX-STANDARD-v1.md](FORGE-WORDPRESS-EDITOR-UX-STANDARD-v1.md)
- [FORGE-WORDPRESS-ACF-ARCHITECTURE-STANDARD-v1.md](FORGE-WORDPRESS-ACF-ARCHITECTURE-STANDARD-v1.md)
- [templates/FORGE-WORDPRESS-EDITABLE-REGIONS-MAP-TEMPLATE-v1.md](../templates/FORGE-WORDPRESS-EDITABLE-REGIONS-MAP-TEMPLATE-v1.md)
- [templates/FORGE-WORDPRESS-EDITOR-WORKFLOW-ACCEPTANCE-CHECKLIST-v1.md](../templates/FORGE-WORDPRESS-EDITOR-WORKFLOW-ACCEPTANCE-CHECKLIST-v1.md)

---

## 10. Production addendum (FP-0002 → WP Forge)

Admin must be **editor-oriented**, localized to the project locale (Russian editors → Russian chrome), technically clean, free of irrelevant page/CPT fields, free of developer notices on every screen, free of raw Options/debug screens, and grouped logically.

### 10.1 Site Settings

See [SITE-SETTINGS-STANDARD](FORGE-WORDPRESS-SITE-SETTINGS-STANDARD-v1.md) and [GLOBAL-SETTINGS-OWNERSHIP](FORGE-WORDPRESS-GLOBAL-SETTINGS-OWNERSHIP-STANDARD-v1.md). One SoT for contacts/socials. Advanced raw-code fields: capability-gated, last, not mixed with ordinary editor settings.

### 10.2 Custom CPT editor

Hide Classic editor / excerpt / revisions / parent when ACF owns the entity. List columns: photo, title, role, order — not generic Date-only. Help text and ACF instructions in the editor locale.

### 10.3 System status

**SYSTEM INFORMATION BELONGS IN ONE OPERATIONS WIDGET, NOT GLOBAL ADMIN NOTICES** (AP-005).

Suggested widget fields: project, environment, live domain, WordPress/PHP versions, domain/DNS/HTTPS (actual), core version, WPilot write state, latest production wave, source/prod parity, backup pointer, indexing OPEN/CLOSED, mail/SMTP **state** (configured is not verified), sender `noreply@…`, lead registry, open launch tails, last verification. No secrets. No mailbox password. No “future host” after the live domain is already in `home`/`siteurl`.

After major production waves the widget **must** be updated in the same wave ([DoD](FORGE-WORDPRESS-DEFINITION-OF-DONE-v1.md)). Indexing control: [SEARCH-INDEXING-CONTROL](FORGE-WORDPRESS-SEARCH-INDEXING-CONTROL-STANDARD-v1.md).

### 10.4 Dangerous / Admin-only

Visibility flags, raw head/body injection, Options dump, migration tools — Administrators only. Activity Log and DOCX importer: editor-capable roles as chartered, never public.

### 10.5 Proven Admin surfaces (pattern, not brand)

Specialists CPT cleanup; SEO & Integrations; Social/Messengers; Smart Search settings; Activity Log; DOCX importer; MetaCODE Dashboard; **Почта и формы** (one SMTP/forms owner); **Заявки** (business lead list, not a raw DB viewer).

### 10.6 Acceptance extras

| # | Check |
|---|--------|
| 11 | Locale packs loaded for plugin + theme |
| 12 | No global LOCAL/MARS/debug notices |
| 13 | Native permalink row only on public CPTs |
| 14 | Empty settings do not render FE leftovers |
| 15 | [EDITOR-WORKFLOW-ACCEPTANCE-CHECKLIST](../templates/FORGE-WORDPRESS-EDITOR-WORKFLOW-ACCEPTANCE-CHECKLIST-v1.md) tabletop or wp-admin PASS |
| 16 | New Admin feature is **visible** in the intended left-menu parent (not only registered / direct URL) |

### 10.7 Discoverability

**AN ADMIN FEATURE IS NOT DONE BECAUSE ITS PAGE OR BACKEND EXISTS.**

It is done only when the intended editor can discover, open, use, save and revisit it through the normal Admin information architecture.

Required sequence: REGISTERED → VISIBLE → ACCESSIBLE → EDITABLE → SAVE/RELOAD → OPERATOR DISCOVERABLE.

When attaching a custom `add_submenu_page()` under an ACF options parent with `redirect => true`, use the **resolved visible** WordPress parent slug (first child), and register **after** ACF’s `admin_menu` (typically priority 99). Do not treat `acf_get_options_page($logical)['menu_slug']` as the visible parent — inspect `acf_get_options_pages()` / `$menu` after ACF runs (AP-029).

---

### 10.8 Repeating configuration lists (mail recipients)

For bounded business lists such as form email recipients:

- Render rows (value + optional label) with **Add** and **Remove**.
- New rows get unique input indexes and remain keyboard-usable before save.
- Do not ask the operator to edit serialized/JSON blobs.
- Save/reload must persist the resulting list without wiping unrelated secrets.

| # | Check |
|---|--------|
| 17 | Repeating settings lists have Add/Remove, server validation, and do not expose raw storage |

---

*Admin UX standard v1.3 — curated editor + production dashboard/SoT + discoverability DoD + repeating mail recipients. CMS pack: [EDITOR UX](FORGE-WORDPRESS-EDITOR-UX-STANDARD-v1.md).*

