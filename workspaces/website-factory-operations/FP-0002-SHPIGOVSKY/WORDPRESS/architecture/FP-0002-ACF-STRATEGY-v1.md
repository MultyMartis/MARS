# FP-0002 ACF Strategy v1

**Task:** V9-06A | **Date:** 2026-07-03  
**Installed baseline:** ACF Free 6.8.4 (active)

---

## 1. OD-ACF-PRO resolution

| Decision ID | Status | Recommendation |
|-------------|--------|----------------|
| OD-ACF-PRO | **MIXED** | ACF Free for scalars/groups/options; bounded repeaters via `shpigovsky-core` BoundedMeta API |

**Can architecture be implemented with ACF Free 6.8.4 alone?**

**PARTIAL — not sufficient as-is** for the intake pack's 13 groups if all repeaters remain ACF Repeater fields (Pro-only).

**Sufficient path without Pro purchase:**

1. Retain ACF Free for: options page, text/textarea/image/url/link/group fields, post object relationships (within Free limits).
2. Move all repeating structures to plugin-registered bounded list meta with deterministic admin UI (`shpigovsky-core/src/Fields/BoundedList/`).
3. Store as validated JSON in post meta; theme reads via helper API.

**Alternative path (operator choice):**

- **ACF Pro** — simplifies editor UX for repeaters; purchase decision deferred to implementation.

---

## 2. Intake group audit (13 groups)

| Group ID | Location | Keep | Change | Remove | Free? | Notes |
|----------|----------|:----:|:------:|:------:|:-----:|-------|
| FG-SITE-OPTIONS | options | ✓ | — | — | yes | Scalars |
| FG-HOME | front-page | ✓ | split repeaters → plugin | — | partial | hero_slides, faq → BoundedMeta |
| FG-SERVICES-HUB | hub template | ✓ | split repeaters | — | partial | category_sections |
| FG-SERVICE-SUBDIVISION | service | ✓ | relocate to CPT | — | partial | |
| FG-SERVICE-LEAF | service | ✓ | relocate to CPT | — | partial | |
| FG-SERVICE-LEAF-ALCOHOL | alcohol layout | ✓ | layout meta trigger | — | partial | extends leaf |
| FG-O-CENTRE | institutional | ✓ | G0-G5 bounded | — | partial | no G6 |
| FG-CONTACTS | contacts | ✓ | — | — | yes | |
| FG-REVIEWS | reviews page | ✓ | repeater → BoundedMeta | — | partial | |
| FG-BLOG-POST | post | ✓ | sources → BoundedMeta | — | partial | relationship stays ACF |
| FG-LEGAL | legal | ✓ | — | — | yes | |
| FG-MODAL | options | ✓ | — | — | yes | |
| FG-PLACEHOLDER | placeholder | ✓ | merge into layout meta | — | yes | |

**Summary:** 13 retained conceptually; 8 changed (repeater transport); 0 removed; 0 arbitrary additions.

---

## 3. Repeater policy

| Structure | Strategy |
|-----------|----------|
| FAQ | BoundedMeta max 15 |
| Reviews | BoundedMeta max 50 |
| Hero slides | BoundedMeta max 5 |
| Program items | BoundedMeta max 6 |
| Infrastructure G0-G5 | Fixed 6 groups, each BoundedMeta |
| Article sources | BoundedMeta max 12 |
| Flexible Content | **FORBIDDEN** |

---

## 4. JSON sync

| Path | Role |
|------|------|
| `WORDPRESS/acf-json/` | Canonical ACF export (scalars/groups only) |
| Runtime | Sync via `shpigovsky-core` load/save hooks |

BoundedMeta schemas live in plugin PHP + JSON schema files — not ACF JSON.

---

## 5. Operator decision

| Question | Default recommendation |
|----------|------------------------|
| Purchase ACF Pro? | **Not required** if BoundedMeta path approved |
| Accept plugin-managed repeaters? | **Yes** — preserves Free license |

If operator prefers pure ACF UX → **ACF_PRO_REQUIRED** at V9-06C.

---

## 6. Result

```text
ACF Free: SUFFICIENT with BoundedMeta companion (MIXED architecture)
ACF Pro: OPTIONAL convenience — not mandatory for V9 scope
```

---

*No ACF groups created or modified in V9-06A.*
