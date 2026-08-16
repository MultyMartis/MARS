# Admin UX and ACF Ownership Patterns (Phase 02)

**Builds on:** Phase 1 `ADMIN-UX-GUIDELINES-FOR-FORGE-PROGER.md`, `ACF-SOT-GUIDELINES.md`  
**Evidence waves:** E55, E59–E59-FIX01, E61, E62B–E62D, E62C, E63 ACF disposition

---

## 1. Core ownership principle

| Content kind | Preferred owner | Anti-pattern |
|--------------|-----------------|--------------|
| Page-unique copy/media | Page (or CPT) field group | Duplicating same text on Blog page + Site Settings |
| Shared band used on many templates | Reusable block / options group | Copy-pasting identical field sets per page |
| Visibility of automated blocks | Toggle/settings fields | Re-implementing content fields for auto-sourced lists |
| Obsolete legacy groups | `active:false` + admin filter | Deleting groups/meta mid-project |

---

## 2. Lessons by surface (FP-0002)

### Site Settings UX (E55)

- Options screens use different DOM (`.postbox`) than post edit (`.acf-postbox`).
- Enqueue admin CSS for `fp02-block-*` options + `body.fp02-site-settings-admin`.
- Future IA rebuild still deferred: `DOCS/FUTURE-TASK-SITE-SETTINGS-ADMIN-IA-AUDIT-AND-RU-UX-REBUILD-v1.md`.

### Contacts (E59 / E59-FIX01 / E61)

- Map ownership moved to page repeater `contacts_locations` (validated embeds).
- Obsolete fields (`contacts_address`, `contacts_map_url`, `contacts_blocks`) removed from admin group; **legacy postmeta left dormant**.
- Multi-phone + messengers + heading order matter for Olga.
- Empty breadcrumb shell when toggle ON but no trail (do not invent crumbs).

### Comfort / CTA bands (E59)

- Reusable Comfort block gained `cta_lead_text` wired to FE lead.
- Program CTA markup unified with Home Comfort CTA structure (E60) — ownership stays block/partial, not duplicated CSS islands.

### Blog archive (E61 / E62B)

- Simplify page admin: avoid duplicate content ownership vs posts themselves.
- `posts_per_page` + pagination SEO are settings; demo posts are **temporary proof**, not SoT forever (`DOCS/DEMO-CONTENT-CLEANUP-BACKLOG-v1.md`).

### Reviews (E61 / E62B / E62C)

- Model: ACF Options repeater `reviews_items` on `fp02-reviews` — **not a CPT**.
- Archive: 5-line expand in place.
- Slider: link to archive anchor (stable `review_uid` after E62C).
- `reviews_per_page` + service relationship field.
- Stable UID field readonly; ensure helper idempotent.

### Founder’s Word / Founder Quote

- Prefer dedicated reusable-block ownership + seed; static fallbacks are debt (E61 gap → E62B seed path).

### Treatment Program cards (E62D → V9-07A01)

- Child pages (`page_parent==13`) own **title**, **permalink**, and `treatment_program_short_description`.
- Shared helper `shpigovsky_get_program_direction_items()` must query live children — no hardcoded title/slug/URL/description snapshots.
- O-centre `about_program_items` and service `programme_items` card titles are **dormant** for frontend (postmeta retained).
- Ownership doc: `DOCS/TREATMENT-PROGRAM-AUTO-SOURCE-OWNERSHIP-v1.md`.

### O-centre (E61 / E62C)

- Reuse Home component partials where markup matches.
- Prefer additive fields (bullets) over span hacks alone.
- Nested CTA must not create nested `<section>` (wrapper flag / div band).

### Service admin hide (E62C)

- Hide Structured Sections + Relationships for Service CPT: PHP `active => false` + always-hide filter.
- JSON `active:false` in source-only files; **do not broadly sync** to runtime.
- Retain registration for field-key / frontend compatibility.

### Classic Editor

- Hide Classic Editor only on screens where ACF is the editor (service CPT pattern from Phase 1 / E46+); do not globally remove for all post types without charter.

---

## 3. Visibility toggles vs content fields

| Use toggle when | Use content field when |
|-----------------|------------------------|
| Block is auto-built from query/relationship | Editor must write unique copy/media |
| Default should be show/hide without deleting data | Empty means hide (Phase 1 empty-hide contract) |
| Global chrome (breadcrumbs on/off by context) | Page-specific heading/lead/body |

E61 breadcrumb toggles (`show_breadcrumbs_pages` / `show_breadcrumbs_services`) are the global chrome example.

---

## 4. ACF JSON vs PHP registration

Stable v1 disposition (`REPORTS/STABLE-V1/ACF-SOURCE-RUNTIME-DISPOSITION-FP-0002-V9-STABLE-V1.md`):

- **23** synced JSON groups present source+runtime.
- **8** source-only groups retained; PHP registration owns runtime where listed in `FieldGroups.php`.
- **0** runtime-only product JSON after closeout.
- Do **not** broadly copy source-only JSON into runtime as a “fix.”

**SAFE UNKNOWN:** full ACF Extended / DB-stored duplicate inventory beyond filesystem JSON (noted in disposition).

---

## 5. Safe idempotent seeding

| Rule | Why |
|------|-----|
| Seed only empty or explicitly chartered fields | Avoid clobbering operator edits |
| Record write log / evidence CSV | Auditability |
| Reversible edit/empty tests where risk high | E62D mini-desc tests |
| Demo content tagged for later cleanup | E61/E62B demos |

---

## 6. Stable identifiers inside repeaters

| Bad | Good |
|-----|------|
| Public `#review-1` by row index | `review_uid` = `review-xxxxxxxx` |
| Anchor breaks on reorder | UID stable; page number may change |

See `DOCS/REVIEWS-STABLE-UID-ANCHORS-v1.md`.

---

## 7. Informational admin notices

- Prefer notices that link to the **actual ownership screen** (reusable block / options / related page).
- Do not present template demo or Home as normal SoT (Phase 1 lesson; reinforced when removing hardcoded program texts).

---

## 8. Reusable ownership matrix template

Copy per project:

| Surface | FE partial(s) | Field group / location | Owner type (page/block/options/CPT) | Toggle fields | Content fields | Hidden/legacy | Seed policy | Notes |
|---------|---------------|------------------------|--------------------------------------|---------------|----------------|---------------|-------------|-------|
| Example: Reviews archive | `reviews-*.php` | `fp02-reviews` options | options repeater | `reviews_per_page` | `reviews_items.*` | — | idempotent UID ensure | not CPT |
| | | | | | | | | |

Fill during admin-parity design **before** mass seed.

---

## 9. Human supervision

- Choosing page vs block ownership for new bands.
- Deleting vs deactivating field groups.
- Production demo cleanup.
- Site Settings IA rebuild (future task).
