# Reusable Frontend Component Patterns (Phase 02)

**Evidence waves:** E59–E62E, E60 CTA unify, E62C review UID, E62A phone mask / crumbs, E62E search/404

---

## 1. Classification

| Class | Meaning | Safe reuse |
|-------|---------|------------|
| **Safe shared partial** | One include, parameterized | Prefer |
| **Context-specific wrapper** | Same inner partial, different outer shell | Prefer wrappers over forks |
| **Data reuse without nested semantics** | Same data, different card chrome | OK if markup validity preserved |
| **Dangerous markup duplication** | Copy-paste HTML/CSS islands | Avoid — drift magnet |

---

## 2. Shared CTA architecture

- Comfort / Home rehabilitation CTA band and program CTA aligned on shared structure (`.program-cta-band` ↔ Comfort CTA wraps) in E60.
- When embedding CTA **inside** an existing `<section>`, use **`<div class="program-cta-band">`** (E62C: `wrap_section=false` for O-centre who-we-treat).
- Nested `<section class="program-cta-band-section">` inside another section = invalid/confusing semantics (E61 defect → E62C fix).

---

## 3. Shared Founder block

- Prefer single Founder Quote / Founder’s Word partial + ACF ownership.
- Static fallbacks without admin group = temporary debt (flagged in E61; seeding path in E62B).

---

## 4. Breadcrumbs shells and wrappers

Canonical internal wrapper (post E62A / E62E-FIX01):

```text
.internal-page-nav > .container > .breadcrumbs
```

| Context | Pattern |
|---------|---------|
| Generic / Specialist / Search (final) | internal-page-nav wrapper |
| Services with subnav | Keep subnav; crumbs respect toggles |
| Toggle OFF | Omit trail; keep nav shell if subnav needs it |
| Toggle ON but no items | Empty `<nav class="breadcrumbs" data-breadcrumbs-empty="1">` — do not invent |

Do not invent a third crumbs DOM per template without reason.

---

## 5. Home components reused on O-centre

- Reuse Home partials/classes when visual system matches (E61/E62C).
- Prefer ACF fields on O-centre for unique lead/bullets rather than hardcoded spans alone.
- Red-line / span wrappers are presentation helpers — still need content ownership.

---

## 6. Service-name links

- Service titles that navigate should be real permalink anchors (`get_permalink()`), not JS-only click targets (E60).
- Hover classification: card-title links use component rules; do not let global nav hover override.

---

## 7. Review cards — archive vs slider

| Surface | Long-text behavior | Link behavior |
|---------|--------------------|---------------|
| Reviews archive | Expands in place (5-line clamp) | N/A (already on archive) |
| Home/other sliders | Teaser | «Читать весь отзыв» → `/otzyvy[/page/N]/#{review_uid}` |

**Stable review UID** (`review-xxxxxxxx`):

- Element `id` on archive card.
- Does not change on reorder; pagination page may.
- Supersedes index-based `#review-1` (E62B → E62C).

Data model reminder: Options repeater, not CPT (`DOCS/REVIEWS-STABLE-UID-ANCHORS-v1.md`).

---

## 8. Search baseline

Accepted Stable baseline (E62E / FIX01):

- Native WP Search for `post` / `page` / `service`, 12/page.
- Header dropdown trigger: **desktop main header only**.
- Floating header + mobile header bar: **no** `data-search-toggle`.
- Mobile: offcanvas **link** to `/?s=` (navigate), not dropdown toggle.
- Results: cards + pagination; SEO `noindex,follow`.
- Empty query: ready-to-search state, not “0 results.”
- Advanced relevance / custom-field indexing: **deferred**.

---

## 9. 404 implementation

- Figma PNG metrics drive typography/spacing/button geometry (E62A/E62D).
- Operator decor asset `404-decor.png` owns cutout visuals (E62E); remove superseded decoys from active use.
- Keep 404 route in release smoke (E63: expected 404 among route matrix).

---

## 10. Telephone mask

- Reused Triumph Manipulator v6 vanilla mask: `+7 (XXX) XXX-XX-XX` (E62A).
- Scope to phone inputs; do not pull unrelated Triumph theme CSS.

---

## 11. Responsive and accessibility

- Stable viewport set used in closeout: **1440 / 1024 / 480 / 370**.
- Reduced-motion: lifebuoy freezes at fixed progress (E57).
- Focus-visible outlines retained when changing hover colors (E60 classification notes).
- Component-specific hover must win over global accent-hover sweeps (E60 → E60-FIX01 breadcrumbs).

---

## 12. Checklist for new shared UI

- [ ] Is there already a partial?
- [ ] Will this nest a `<section>` inside a `<section>`?
- [ ] Is public identity index-based? If yes → design stable ID.
- [ ] Does hover belong to nav, card, or crumb component?
- [ ] Does admin ownership exist for every editable string?
- [ ] Exact-file delivery list includes CSS + partials + any JS?
