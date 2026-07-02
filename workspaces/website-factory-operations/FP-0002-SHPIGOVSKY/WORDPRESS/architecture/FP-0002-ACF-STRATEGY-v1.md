# FP-0002 ACF Strategy v1

**Task:** V9-06A.1 | **Date:** 2026-07-03  
**Operator decision:** OD-001 — **ACF Pro REQUIRED FOR FP-0002**

---

## 1. OD-001 resolution

| Decision ID | Status | Value |
|-------------|--------|-------|
| OD-001 | **APPROVED** | ACF Pro required for FP-0002 |

**Primary FP-0002 implementation path:** ACF Pro  
**Custom BoundedMeta repeater framework:** **REJECTED_FOR_FP0002** (historical V9-06A design retained as research reference only — see §8)

---

## 2. ACF Pro use cases (approved)

| Use case | Allowed |
|----------|:-------:|
| Bounded Repeaters | yes |
| Relationship fields | yes |
| Options Page | yes |
| Structured field groups | yes |
| Deterministic conditional logic | yes |

## 3. Forbidden even with Pro

| Pattern | Status |
|---------|--------|
| Flexible Content | **FORBIDDEN** |
| Clone-based generic page builders | **FORBIDDEN** |
| Nested arbitrary layouts | **FORBIDDEN** |
| Editor-defined section ordering | **FORBIDDEN** |
| Unrestricted repeaters | **FORBIDDEN** |
| Generic blocks CPT | **FORBIDDEN** |

---

## 4. Options Page

**Admin label:** `Настройки сайта`  
**Owner:** Shpigovsky Core + ACF Pro Options Page  
**Implementation phase:** V9-06C (requires ACF Pro package prerequisite)

| Group | Fields (bounded) |
|-------|------------------|
| Contacts | phones (repeater max 3), email, address, opening hours |
| Social | social links actually present in V9 (url + label) |
| Modal | default title, default CTA label |
| Global CTA | default button labels where not page-specific |
| Legal org | organisation legal name, identifiers for legal templates |
| Map | map embed URL or coordinates where required |

**Excluded from options:** secrets, API keys, analytics credentials, SMTP passwords, arbitrary HTML, generic global blocks.

---

## 5. Repeater bounds (ACF Pro + server validation)

Validation ownership: **ACF field configuration** + **`shpigovsky-core` validation hook** where row count or required subfields must be enforced server-side.

| Group | Field name | Location | Min | Max | Required row fields | Empty state | Render owner |
|-------|------------|----------|-----|-----|---------------------|-------------|--------------|
| FG-HOME | `fp02_hero_slides` | front-page | 0 | 5 | image, title | hide section | theme |
| FG-HOME | `fp02_faq_items` | front-page | 0 | 15 | question, answer | hide section | theme |
| FG-HOME | `fp02_program_items` | front-page | 0 | 6 | title | hide section | theme |
| FG-SERVICE-* | `fp02_signs_items` | service | 0 | 12 | text | hide section | theme |
| FG-SERVICE-* | `fp02_stages_items` | service / o-centre | 0 | 8 | title | hide section | theme |
| FG-SERVICE-* | `fp02_program_items` | service | 0 | 6 | title | hide section | theme |
| FG-SERVICE-* | `fp02_faq_items` | service | 0 | 15 | question, answer | hide section | theme |
| FG-REVIEWS | `fp02_reviews_items` | reviews page | 0 | 50 | author, text | show empty notice | theme |
| FG-BLOG-POST | `fp02_sources_items` | post | 0 | 12 | title, url | hide block | theme |
| FG-O-CENTRE | `fp02_infrastructure_g0_g5` | o-centre hub | 6 | 6 | fixed G0–G5 groups | required structure | theme |

---

## 6. Intake group audit (13 groups — unchanged scope)

All 13 conceptual groups retained. Repeaters implemented as **ACF Pro Repeater fields** with bounds above — not BoundedMeta.

| Group ID | Repeater transport |
|----------|-------------------|
| FG-SITE-OPTIONS | ACF Pro options scalars |
| FG-HOME | ACF Pro repeaters |
| FG-SERVICES-HUB | ACF Pro repeaters (bounded) |
| FG-SERVICE-* | ACF Pro on `service` CPT |
| FG-O-CENTRE | ACF Pro fixed groups |
| FG-CONTACTS | ACF Pro scalars |
| FG-REVIEWS | ACF Pro repeater max 50 |
| FG-BLOG-POST | ACF Pro repeater + relationship |
| FG-LEGAL | ACF Pro scalars |
| FG-MODAL | ACF Pro options |
| FG-PLACEHOLDER | ACF Pro minimal |

---

## 7. JSON sync

| Path | Role |
|------|------|
| `WORDPRESS/acf-json/` | Canonical ACF Pro JSON export |
| Runtime | Sync via `shpigovsky-core` load/save hooks |

---

## 8. BoundedMeta historical note

V9-06A proposed ACF Free + custom BoundedMeta companion.

**V9-06A.1 reconciliation:**

| Item | Classification |
|------|----------------|
| BoundedMeta as primary FP-0002 path | **REJECTED_FOR_FP0002** |
| BoundedMeta as Website Factory research | **DEFERRED_AS_WEBSITE_FACTORY_RESEARCH** |
| V9-06B / V9-06C BoundedMeta implementation | **NOT AUTHORIZED** |

**Scalar native meta helper:** A small `register_post_meta` helper in Shpigovsky Core for simple scalars (e.g. layout enum) may remain — **distinct from** a custom repeater framework.

---

## 9. V9-06C ACF Pro operational prerequisite

V9-06C **NOT READY** until:

- [ ] Approved ACF Pro package/source available locally
- [ ] Local-only license handling documented
- [ ] Git exclusion of license keys verified
- [ ] Package provenance recorded
- [ ] Version pinned
- [ ] Checkpoint before install
- [ ] Local install/activation validated
- [ ] No automatic updates without operator approval
- [ ] Production licensing decision recorded separately

**V9-06B** theme/core skeleton **may proceed** without ACF Pro install if no ACF-dependent runtime functionality executes.

---

## 10. Result

```text
ACF Pro:              REQUIRED FOR FP-0002
Flexible Content:     FORBIDDEN
BoundedMeta primary:  REJECTED_FOR_FP0002
Options Page:         Настройки сайта (V9-06C)
V9-06C prerequisite:  ACF Pro package — NOT SATISFIED
```

---

*No ACF installation or field group creation in V9-06A.1.*
