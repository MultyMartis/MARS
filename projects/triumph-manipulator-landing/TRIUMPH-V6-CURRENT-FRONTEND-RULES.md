# Triumph Manipulator — V6 current frontend rules

**Status:** canonical for all Triumph V6 production work (2026-05-28).  
**Scope:** `workspaces/triumph-manipulator-landing-v6/` only.  
**Not:** governance expansion, autonomous QA, or pixel-perfect certification.

**Supersedes for active work:** V2/V3/V4/V5 rule docs listed in [`V6-RULES-DEPRECATION-INDEX.md`](V6-RULES-DEPRECATION-INDEX.md).  
**Factory layer (generic):** [`projects/mars-website-factory/`](../mars-website-factory/) — use when this file is silent; **this file wins** for Triumph V6 specifics.

---

## A. Workspace

| Item | Rule |
|------|------|
| **Canonical path** | `C:\AI MARS\workspaces\triumph-manipulator-landing-v6\` |
| **Historical V5** | `workspaces/triumph-manipulator-landing-v5/` — frozen reference; do not use for new pages |
| **Source vs dist** | Edit `src/` only. Run `npm run build`. Never hand-edit `dist/`. |
| **Build command** | `npm run build` (Gulp: `gulp build`) |
| **Backend** | `backend/` at workspace root — copied to `dist/backend/` on build (gitignored locally; must exist on disk for mailer) |
| **Baseline page** | `src/pages/index.html` — zakaz intent (`data-page-type="ppc-zakaz-manip"`) |

---

## B. Layout rules

| Rule | Detail |
|------|--------|
| **Section shell** | Major sections use `.section-shell` inside section roots; preserve landmark structure (`header`, `main`, `footer`). |
| **Main breakpoint** | **1024px** max / **1025px** min for layout stacks — primary responsive law for new SCSS. |
| **Header nav breakpoint** | **1490px** where `$header-nav-break` is used in `src/scss/layout/_header.scss` — header-only; do not repurpose for section layout. |
| **Forbidden for new work** | Ad-hoc **980 / 981** media-query breakpoints. Legacy `max-width: 980px` on some panels is frozen baseline — do not copy to new sections. |
| **First screen** | `.first-screen` wraps hero + header on PPC pages; do not collapse header/hero ownership. |
| **Includes** | Page composition via `@@include` partials under `src/partials/` — one PPC folder per future page slug. |

---

## C. Component rules (zakaz baseline markers)

Implement rollout pages by **replacing content** inside these patterns — not by inventing new section types.

| Block | Root / marker classes | Partial area (zakaz) |
|-------|----------------------|----------------------|
| **Hero** | `.first-screen`, `.hero__cargo-action`, hero form `data-form-id` | `v5-ppc/zakaz/screen-01-hero.html` |
| **Machine parameters** | `.machine-showcase__spec-panel`, specs grid | `v5-ppc/zakaz/screen-02-specs.html` |
| **Tasks cluster** | `.machine-transport--ops-grid` | `v5-ppc/zakaz/screen-02-tasks.html` |
| **Order steps** | `.order-steps--process` | `v5-ppc/zakaz/screen-02b-order-steps.html` |
| **Pricing factors** | `.pricing-factors--system` | `v5-ppc/zakaz/screen-02c-pricing-factors.html` |
| **Trust / proof** | Shared `v5-page01/` trust, B2B, `.dark-proof-strip` | `screen-03-trust-reviews`, `screen-03b-b2b`, `dark-proof-strip` |
| **FAQ + inline CTA** | `.faq--split-cta` | `v5-ppc/zakaz/screen-04-faq.html` |
| **Final contact** | `.contact-cta` / final section | `v5-ppc/zakaz/final-contact-cta.html` |
| **Footer** | `v5-page01/landing-footer.html` | Shared footer partial |
| **Modal** | `callback-modal.html` with `@@prefix` | `data-form-id="@@prefix-callback"` |

**SCSS ownership:** matching partials under `src/scss/sections/` (`_v5-hero-extensions.scss`, `_v5-machine-showcase.scss`, `_v5-order-steps.scss`, `_v5-pricing-factors.scss`, `_screen-04-faq.scss`, etc.).

---

## D. Forms / mailer rules

| Rule | Detail |
|------|--------|
| **Endpoint** | `backend/send-lead.php` — default in `src/js/form.js` (`DEFAULT_FORM_ENDPOINT`) |
| **Dist path** | `dist/backend/send-lead.php` after build |
| **`data-form-id`** | **Required** on every production form (hero, FAQ inline, final CTA, modal) |
| **No mock in HTML** | Do **not** set `data-form-handler="mock"` on production forms |
| **No legacy API** | Do **not** use `backend/api/forms/send.php` or `data-form-endpoint` pointing there |
| **Recipient** | `client.leads@polygon-ws.ru` (see `backend/send-lead.php` / `backend/config.php`) |
| **Honeypot** | `company_url` hidden field — preserve |
| **Behavior** | Do not break submit UX, validation, or success messages when changing copy |

`form.js` retains mock handler code for dev-only explicit `data-form-handler="mock"` — production HTML must not trigger it.

---

## E. Typography rules

| Rule | Detail |
|------|--------|
| **Russian nbsp** | Use `&nbsp;` for prepositions, units, and glued commercial phrases per Factory [`russian-no-word-splitting-typography-v1.md`](../mars-website-factory/russian-no-word-splitting-typography-v1.md) |
| **Headings** | Avoid mid-word breaks; no decorative hyphenation for layout |
| **Numeric units** | Examples: `5&nbsp;т`, `14&nbsp;м`, `2&nbsp;часа` |
| **Known correction** | Spec copy uses **`5&nbsp;т&nbsp;/&nbsp;3&nbsp;т`** (bord / strela) — keep consistent across pages |
| **Title/meta** | `head-v5-page01.html` and page `@@include` args — nbsp discipline applies |

---

## F. Page rollout rules

| Rule | Detail |
|------|--------|
| **Pace** | Generate **one page at a time** from V6 canonical zakaz baseline |
| **ORCA copy** | Replace text/content from ORCA handoffs / blueprints — no fabricated fleet or ops claims |
| **Layout adaptation** | Adjust section **locally** only when text length breaks layout; no global redesign per page |
| **Partial strategy** | Duplicate `v5-ppc/<slug>/` or add new `src/pages/<slug>.html` when routing expands — see [`V6-PAGE-ROLLOUT-PLAN.md`](V6-PAGE-ROLLOUT-PLAN.md) |
| **Batch limit** | Do not batch-generate all 11 remaining pages until **1–2** pilot pages pass build + QA + HITL |
| **PPC partials** | Existing scaffold folders under `v5-ppc/` (bytovki, stroymaterialy, …) are **draft scaffolds** — not production-approved until individually completed |

---

## G. QA rules (minimum per page pass)

1. `npm run build` — **PASS** required  
2. Open `dist/index.html` (or target page) — viewport spot check **320 / 375 / 768 / 1024 / 1440**  
3. **Markers** — hero, machine showcase, tasks grid, order steps, pricing, FAQ split, footer present  
4. **Overflow** — no horizontal scroll at spot widths  
5. **Forms** — submit test; network POST to `backend/send-lead.php` (or documented local PHP)  
6. **Mailer** — confirm recipient policy unchanged unless HITL approves  
7. **REPORT** — changed files, build result, gaps as **SAFE UNKNOWN**

---

## Authority quick reference

| Need | Doc |
|------|-----|
| Rollout order | [`V6-PAGE-ROLLOUT-PLAN.md`](V6-PAGE-ROLLOUT-PLAN.md) |
| Deprecated rules | [`V6-RULES-DEPRECATION-INDEX.md`](V6-RULES-DEPRECATION-INDEX.md) |
| ORCA blueprints | `projects/orca/ppc/triumph-manipulator/landing-pages/` |
| RU typography (generic) | `projects/mars-website-factory/russian-no-word-splitting-typography-v1.md` |

*Human-operated documentation — not runtime enforcement.*
