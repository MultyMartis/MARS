# V6 — Legacy and dead structure audit

**Status:** audit + safe-prep only (2026-05-28). **No** mass deletion performed.  
**Workspace:** `workspaces/triumph-manipulator-landing-v6/`  
**Active map:** [`V6-ACTIVE-STRUCTURE-MAP.md`](V6-ACTIVE-STRUCTURE-MAP.md)

---

## A. Dead partials (not in `index.html` closure)

**Total partials:** 117 HTML files under `src/partials/`  
**Unreferenced from index:** 102 files

### Category 1 — V2/V3 root orphans (`partials/sections/*.html`)

| File | Notes | Disposition |
|------|--------|-------------|
| `sections/screen-01-hero.html` | Pre-v5 hero | historical — safe to quarantine later |
| `sections/screen-02-prices.html` | Old prices screen | historical |
| `sections/screen-03-trust-reviews.html` | Superseded by `v5-page01/` | historical |
| `sections/screen-04-faq.html` | Non-split FAQ | historical |
| `sections/final-contact-cta.html` | Standalone contact (V2 pattern) | historical |
| `sections/dark-proof-strip.html` | Duplicate of `v5-page01/` | historical |
| `sections/landing-footer.html` | Duplicate of `v5-page01/` | historical |

### Category 2 — V2 layout / components

| File | Disposition |
|------|-------------|
| `layout/head.html`, `header.html`, `scripts.html` | historical |
| `layout/head-legal.html`, `scripts-legal.html` | historical (legal routes not built) |
| `components/modal-shell.html` | historical — callback-modal is canonical |

### Category 3 — V5 page01 duplicate stack (unused on index)

Full alternate page01 set not wired on zakaz index:

- `v5-page01/screen-01-hero.html` … `screen-04-faq.html`, `final-contact-cta.html`, etc.

**Disposition:** historical reference — **risky-remove** (may be copied during early rollout experiments).

### Category 4 — PPC scaffolds (`v5-ppc/<slug>/`, 11 non-zakaz slugs + zakaz legacy)

Each scaffold folder typically contains 8 partials including **`final-contact-cta.html`**.

| Risk | Detail |
|------|--------|
| **Duplicate `#contacts`** | Every `final-contact-cta.html` defines `id="contacts"` — **must not** be included alongside `screen-04-faq.html` |
| **Duplicate forms** | Same `data-form-id="zakaz-contact-quote"` pattern copied in scaffolds — rollout must assign **unique** IDs per page |
| **Stale copy** | Scaffold text still references zakaz / generic placeholders |

**Disposition:** rollout-required drafts — **do not delete**; **do not @@include** `final-contact-cta.html` on canonical pages.

### Category 5 — Legal partials

`sections/legal/*` — no `src/pages` legal HTML in build.

**Disposition:** historical / future routes — keep until legal pages chartered.

### Zakaz-only legacy artifact

| File | Status |
|------|--------|
| `v5-ppc/zakaz/final-contact-cta.html` | **LEGACY** — marked with HTML comment (2026-05-28); not in build |

---

## B. Dead SCSS

### Misnamed but **active** (do not remove)

| File | Reality |
|------|---------|
| `_screen-02-prices.scss` | Powers `.machine-showcase` on index (specs section) |
| `_final-contact-cta.scss` | Powers `.contact-cta--embedded` in FAQ aside |

### Imported, no matching page HTML

| File | Disposition |
|------|-------------|
| `_legal-pages.scss` | risky-remove — footer links assume future legal pages |

### Selector-level dead candidates (active import files)

| Selector / block | File | Disposition |
|------------------|------|-------------|
| `.faq__grid` | `_screen-04-faq.scss` | risky-remove — unused on index |
| `.prices` as **section** layout | `_screen-02-prices.scss` | legacy-but-still-used — tasks section still uses `class="prices"` wrapper |

### Duplicate layout systems

| System A | System B | Notes |
|----------|----------|-------|
| `_screen-02-prices.scss` `.machine-showcase` base | `_v5-machine-showcase.scss` zakaz overrides | **Intentional layering** — not duplicate ownership error |
| `v5-page01` partial duplicates | `v5-ppc/zakaz` active set | HTML duplication only — SCSS shared |

### Obsolete 980px usage

Not used as `@media (max-width: 980px)` in scanned SCSS; **980px appears as `max-width` property** on inner panels (pricing, order-steps, specs). Still affects live layout — **historical pattern**, frozen on baseline.

### safe-remove (this pass)

**None** — no selector met 100% unreferenced + zero rollout coupling proof.

---

## C. Legacy semantics

| Topic | Finding |
|-------|---------|
| **`.prices` on tasks section** | `screen-02-tasks.html` uses `class="prices"` for historical reasons; content is tasks grid — naming drift |
| **`#specs` vs nav** | Specs section uses `id="specs"`; header nav has no `#specs` link (tasks/pricing/reviews/faq/contacts only) |
| **Dual contact systems** | Standalone `.contact-cta` section partials vs embedded `.contact-cta--embedded` — only embedded is canonical on V6 index |
| **CTA / modal** | `data-modal-open="modal-callback"` + `data-cta-source` pattern — canonical |
| **Form endpoint** | `backend/send-lead.php` via `form.js` — no `api/forms/send.php` in active HTML |
| **V4 docs in workspace** | `docs/V4-*.md` — reconstruction notes; not build inputs |

---

## D. Rollout risks (11 remaining pages)

| Risk | Severity | Mitigation |
|------|----------|------------|
| Including `final-contact-cta.html` + `screen-04-faq.html` | **High** — duplicate `#contacts` | Rollout checklist: FAQ split only |
| Reused `data-form-id` across pages | **High** — mailer attribution conflation | Unique per form per page |
| Copying scaffold without updating `data-page-type` | Medium | Per-slug `data-page-type` |
| Assuming `v5-page01/screen-04-faq.html` (non-split) | Medium | Start from **zakaz** `screen-04-faq.html` |
| Header `@@prefix` / modal `data-form-id` mismatch | Medium | Keep prefix consistent per slug |
| Shared SCSS `body[data-page-type='ppc-zakaz-manip']` | Medium | Add new page types or scope overrides when cloning |
| `data-link-todo` messenger URLs | Low | HITL before production |
| Legal URLs in footer without legal HTML build | Low | Separate charter |
| 102 orphan partials confuse agents | Medium | Use [`V6-ACTIVE-STRUCTURE-MAP.md`](V6-ACTIVE-STRUCTURE-MAP.md) as allowlist |

### Hidden dependencies

- `polygon-copyright.html` only via footer include
- Hero cargo cards require `modal.js` + `callback-modal.html`
- FAQ accordion expects `.faq-item` on `<details>`
- Consent checkboxes link to `/privacy-policy/` paths (not built in V6 dist)

---

## E. Recommended quarantine (future pass, not executed)

Target folder (proposal): `src/_legacy-unused/v2-v3-orphans/`  
**Candidates:** Category 1 + Category 2 only, after second human review.

**Do not quarantine:** `v5-ppc/*` scaffolds (rollout drafts).

---

*Human-operated audit — not automated dead-code elimination.*
