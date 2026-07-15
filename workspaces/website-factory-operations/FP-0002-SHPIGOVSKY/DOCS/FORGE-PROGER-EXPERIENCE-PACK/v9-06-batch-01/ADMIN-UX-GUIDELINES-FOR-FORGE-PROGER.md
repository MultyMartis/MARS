# Admin UX Guidelines — Forge Proger (from FP-0002)

**Audience:** future Forge Proger playbooks  
**Status:** experience documentation only — not active brain rules

---

## Principles

1. **Admin UI is a product surface** — equal in acceptance weight to frontend for editor-managed sites.
2. **One screen must be understandable to a non-developer editor (Olga)** without reading PHP or ACF JSON.
3. **Thematic blocks need visual card/section structure** — not a flat infinite field list.
4. **Internal separators inside blocks should not dominate** — ACF default grey field borders often must be muted.
5. **Major block separation must remain** — section titles (e.g. `.fp02-acf-section-title` ~20px) keep orientation.
6. **Helper text should explain source of repeated/automatic blocks** — e.g. “pulled from child services” / “Site Settings”, with edit links when useful.
7. **Labels in Russian** (for RU editor projects) — no English leftover keys as primary labels.
8. **Avoid technical names in editor-facing controls** — hide `service_layout_variant` style jargon behind Раздел/Услуга/Заглушка.
9. **Toggles and placeholder controls must be obvious** — placement near top; clear consequences explained.
10. **Real admin save must be tested** — screenshot + Update click path, not only CLI meta writes.

---

## Practical CSS/enqueue lessons (E53)

- Scope admin CSS with a body class (e.g. `body.fp02-acf-admin`).
- Enqueue for **all** page templates that edit ACF — including generic pages (easy to miss).
- Keep alias files if older enqueue paths exist (`admin-home-acf.css` → import unified file).
- Do not strip input chrome needed for usability; only reduce visual noise.

---

## Acceptance checklist (suggested)

| Check | Pass when |
|-------|-----------|
| Scanability | Editor can find block N without scrolling guessing |
| Noise | Internal field lines do not compete with section titles |
| Language | Primary labels/instructions in editor language |
| Controls | Layout/placeholder toggles visible and named plainly |
| Save | Real Update keeps intended values |
| Regression | Frontend unchanged for admin-only CSS tasks |
