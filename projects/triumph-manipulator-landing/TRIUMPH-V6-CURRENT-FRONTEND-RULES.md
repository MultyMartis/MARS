# Triumph Manipulator — V6 current frontend rules

**Status:** canonical for all Triumph V6 production work (2026-05-28).  
**Scope:** `workspaces/triumph-manipulator-landing-v6/` only.  
**Not:** governance expansion, autonomous QA, or pixel-perfect certification.

**Supersedes for active work:** V2/V3/V4/V5 rule docs listed in [`V6-RULES-DEPRECATION-INDEX.md`](V6-RULES-DEPRECATION-INDEX.md).  
**Factory layer (generic):** [`projects/mars-website-factory/`](../mars-website-factory/) — use when this file is silent; **this file wins** for Triumph V6 specifics.
**Temporary safety lock:** canonical baseline freeze notice in [`V6-PRODUCTION-BASELINE-LOCK.md`](V6-PRODUCTION-BASELINE-LOCK.md) (active until explicit user override).

---

## A. Workspace

| Item | Rule |
|------|------|
| **Canonical path** | `X:\AI MARS\workspaces\triumph-manipulator-landing-v6\` |
| **Historical V5** | `workspaces/triumph-manipulator-landing-v5/` — frozen reference; do not use for new pages |
| **Source vs dist** | Edit `src/` only. Run `npm run build`. Never hand-edit `dist/`. |
| **Build command** | `npm run build` (Gulp: `gulp build`) |
| **Backend** | `backend/` at workspace root — copied to `dist/backend/` on build (gitignored locally; must exist on disk for mailer) |
| **Baseline page** | `src/pages/index.html` — zakaz intent (`data-page-type="ppc-zakaz-manip"`) |

---

## A2. Contact system (canonical)

| Layer | Rule |
|-------|------|
| **HTML (active)** | `faq--split-cta` in `screen-04-faq.html` with `aside.contact-cta.contact-cta--embedded#contacts` |
| **Forms on index** | Hero `zakaz-hero-quote`, inline contact `zakaz-contact-quote`, modal `zakaz-callback` |
| **Standalone partial** | `final-contact-cta.html` (any `v5-ppc/<slug>/` or `v5-page01/`) — **legacy artifact**; **not** part of active V6 zakaz page |
| **SCSS** | `_final-contact-cta.scss` — **keep imported**; styles embedded contact and would style standalone block if mistakenly included |

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
| **FAQ + contact (canonical)** | `.faq--split-cta` + `.contact-cta--embedded#contacts` | `v5-ppc/zakaz/screen-04-faq.html` only |
| **Standalone final contact** | `.contact-cta` section root | **LEGACY** — `final-contact-cta.html` (any slug) must **not** be `@@include`d on canonical V6 pages |
| **Contact SCSS file** | `.contact-cta`, `.contact-cta--embedded` | `src/scss/sections/_final-contact-cta.scss` (legacy **filename**; styles are **active**) |
| **Footer** | `v5-page01/landing-footer.html` | Shared footer partial |
| **Modal** | `callback-modal.html` with `@@prefix` | `data-form-id="@@prefix-callback"` |

**SCSS ownership:** matching partials under `src/scss/sections/` (`_v5-hero-extensions.scss`, `_v5-machine-showcase.scss`, `_v5-order-steps.scss`, `_v5-pricing-factors.scss`, `_screen-04-faq.scss`, `_final-contact-cta.scss`, etc.).  
**Naming trap:** `_screen-02-prices.scss` is the **machine-showcase base** file (legacy name) — not the tasks/pricing section alone.

**Active topology map:** [`V6-ACTIVE-STRUCTURE-MAP.md`](V6-ACTIVE-STRUCTURE-MAP.md)  
**Dead / legacy inventory:** [`V6-LEGACY-AND-DEAD-AUDIT.md`](V6-LEGACY-AND-DEAD-AUDIT.md)

---

## B2. Active page stack (zakaz `index.html`, 2026-05-28)

| Zone | Includes |
|------|-----------|
| **First screen** | `head-v5-page01` → `.first-screen` → `header-v5-page01` + `v5-ppc/zakaz/screen-01-hero` |
| **Main** | `screen-02-specs` → `screen-02-tasks` → `screen-02b-order-steps` → `screen-02c-pricing-factors` → `screen-03-trust-reviews` → `screen-03b-b2b` → `dark-proof-strip` → `screen-04-faq` (embeds `#contacts`) |
| **After main** | `landing-footer` → `callback-modal` → `scripts-v5-page01` |

**Anchors in nav:** `#tasks`, `#pricing`, `#reviews`, `#faq`, `#contacts` (header/footer). `#specs` exists but is not in header nav.

---

## B3. Breakpoint system (active only)

| Breakpoint | Use |
|------------|-----|
| **1024px / 1025px** | Primary section responsive law (hero, showcase, order steps, pricing, FAQ split, footer, modal) |
| **1490px** | Header nav (`$header-nav-break`) + selective trust/showcase tweaks |
| **1380px**, **810px** | Header-only compact / drawer mid |
| **760px / 1180px** | Container horizontal padding (`_container.scss`) |
| **980px** | Legacy **inner max-width** values on some panels — frozen on baseline; **do not** add new `@media (max-width: 980px)` rules |
| **981px** | Not used in V6 SCSS (2026-05-28) |

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
| **Allowlist** | Duplicate **only** partials in [`V6-ACTIVE-STRUCTURE-MAP.md`](V6-ACTIVE-STRUCTURE-MAP.md) closure; do not `@@include` `final-contact-cta.html` |
| **Unique IDs** | One `id="contacts"` per page; unique `data-form-id` per form |
| **Contact pattern** | Copy `screen-04-faq.html` embedded contact — not standalone `final-contact-cta.html` |
| **Rollout discipline** | Never adapt existing target-route partials; always copy canonical `v5-ppc/zakaz/` partials first, then adapt content |
| **Tasks parity gate** | For each new route, copy `screen-02-tasks.html` from canonical zakaz first and verify section/class parity before text adaptation |
| **Tasks forensic parity (mandatory)** | Rollout parity checks must include HTML structure parity, body/page data-attribute parity, CSS scope parity, and computed-style source parity (not class names only) |
| **Scoped-style inclusion rule** | If canonical tasks styles are scoped to `data-page-type`, a new route must either use approved shared V6 PPC scope or be explicitly added to the scoped selector group |
| **5-tonn failure cause (2026-05-28)** | `screen-02-tasks` markup was aligned but canonical ops-grid styles in `_v5-machine-showcase.scss` were scoped to `body[data-page-type='ppc-zakaz-manip']`; `body[data-page-type='ppc-5-tonn']` missed this scope and rendered legacy-like |
| **Legacy tasks drift marker** | `<section class="prices section-light" id="tasks">` blocks without current `.machine-transport--ops-grid` structure are legacy drift and forbidden |
| **Copy boundary** | ORCA operational/system wording must never appear in production landing copy |
| **Fixed titles** | Keep canonical titles unchanged: `Что не перевозим`, `Частые вопросы` |
| **Hero notice** | `.hero__notice` is deprecated and forbidden on rollout pages |

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
| Active topology | [`V6-ACTIVE-STRUCTURE-MAP.md`](V6-ACTIVE-STRUCTURE-MAP.md) |
| Legacy / dead audit | [`V6-LEGACY-AND-DEAD-AUDIT.md`](V6-LEGACY-AND-DEAD-AUDIT.md) |
| Deprecated rules | [`V6-RULES-DEPRECATION-INDEX.md`](V6-RULES-DEPRECATION-INDEX.md) |
| ORCA blueprints | `projects/orca/ppc/triumph-manipulator/landing-pages/` |
| RU typography (generic) | `projects/mars-website-factory/russian-no-word-splitting-typography-v1.md` |

*Human-operated documentation — not runtime enforcement.*

---

## V6 ROUTE ROLLOUT HARDENING RULES

- **A. Canonical source rule**
  - Never adapt existing target-route partials.
  - Always copy canonical `v5-ppc/zakaz/` partials first.
  - Apply route content from ORCA only after canonical copy is in place.
- **B. CSS scope admission rule**
  - New route is not complete after HTML copy.
  - Every new route must be admitted into canonical CSS scopes.
  - If selectors are scoped by `body[data-page-type]`, add the new route to selector groups (or approved shared V6 PPC scope).
  - Verify `body[data-page-type]` for each route page before QA.
- **C. Required parity gates (before adaptation)**
  - Page include chain parity.
  - Partial structure parity.
  - Body/page data-attribute parity.
  - CSS scope parity.
  - Marker parity.
  - Computed-style source parity when visual mismatch appears.
- **D. Fixed title rules**
  - Do not change: `Что не перевозим`.
  - Do not change: `Частые вопросы`.
- **E. Forbidden legacy blocks**
  - `.hero__notice` is forbidden.
  - Standalone `final-contact-cta.html` is forbidden when `faq--split-cta` exists.
- **F. ORCA copy rules**
  - Use only final website copy from ORCA pack.
  - Separate and exclude ORCA operational/system/internal wording from production text.
  - Forbidden production wording: `capability-first`, `qualification-first`, `semantic`, `calibration`, `route`, `slot architecture`, `hierarchy`, `proof logic`, `intent layer`, `operational layer`, `Template B`, `internal notes`.
- **G. Contact/form rules**
  - Exactly one `id="contacts"` per page.
  - Exactly one contact form per FAQ split route.
  - `data-form-handler="mock"` is forbidden in production markup.
  - `backend/api/forms/send.php` is forbidden.
  - Form IDs and CTA sources must be route-specific.

---

## V6 ROUTE IMAGE POLICY

1. `machine-showcase__media--index-baseline` is a route-specific asset layer.
2. During rollout/calibration, temporary reuse of canonical baseline image is allowed.
3. After all rollout pages are created, execute a dedicated image mapping pass.
4. Image mapping pass responsibilities:
   - route -> semantic image mapping
   - correct image asset assignment
   - alt text verification
   - sizing consistency
   - mobile QA
5. Image replacement is NOT part of structural rollout calibration.
6. Do not block rollout waiting for perfect route image assignment.
