# TRIUMPH-POLISH-BACKLOG-v1

**Project:** Triumph Manipulator Landing V6  
**Workspace:** `workspaces/triumph-manipulator-landing-v6/`  
**Status:** Preparation-only inventory — **no fixes applied**  
**Date:** 2026-06-01  
**Audit mode:** Full project audit (pages, partials, SCSS, JS, forms, legal, footer, header, hero, cards, FAQ, contacts, CTA, mobile)  
**Build check:** `npm run build` exit **0** (2026-06-01); `verify-final-wave-dist.mjs` → **FAIL** on `5-tonn` only  

**Scope boundary:** V6 only — **v4 / v5 workspaces not touched.**

**Evidence base:** Source audit, existing reports (`v6-visual-qa-audit-report-v1.md`, `v6-production-candidate-freeze-report-v1.md`, `v6-recaptcha-config-check-report-v1.md`, `v6-live-mail-test-report-v1.md`), build verification.

---

## Summary counts

| Priority | Count | Theme |
|----------|------:|-------|
| **P0 — Critical** | 3 | Encoding, reCAPTCHA/deploy config, secret exposure risk |
| **P1 — High** | 12 | SEO/compliance, conversion gaps, parity failures, untested forms |
| **P2 — Medium** | 18 | Visual polish, typography, images, UX edge cases |
| **P3 — Cosmetic** | 10 | Cleanup, consistency, nice-to-have |
| **QUICK WINS** | 8 | Low effort / high impact / low risk |
| **Total backlog items** | 43 | Excluding wave grouping duplicates |

---

## P0 — Critical

### TR-P0-001 — `5-tonn.html` page shell encoding corruption

| Field | Value |
|-------|-------|
| **ID** | TR-P0-001 |
| **Title** | Fix CP1251/UTF-8 mismatch in `5-tonn.html` page shell |
| **Area** | Pages / SEO |
| **Problem** | `src/pages/5-tonn.html` stores Cyrillic in **Windows-1251** bytes while the rest of the project is **UTF-8**. Byte comparison vs `index.html` confirms divergent encoding in the `@@include` title/description string. Built `dist/5-tonn.html` emits corrupted `<title>`, meta description, and OG tags. |
| **Expected result** | `5-tonn.html` saved as UTF-8 with correct Cyrillic title/description matching other PPC routes; dist head tags render correctly in browser and search snippets. |
| **Risk** | **High** — broken SEO/SERP for a primary route; possible brand/trust damage in browser tab and social previews. |

---

### TR-P0-002 — reCAPTCHA server config not loadable

| Field | Value |
|-------|-------|
| **ID** | TR-P0-002 |
| **Title** | Normalize `backend/config.local.php` to valid PHP array format |
| **Area** | Backend / Forms |
| **Problem** | `v6-recaptcha-config-check-report-v1.md` documents that local `config.local.php` exists but is **not** a valid `return [...]` PHP file expected by `triumph_load_config()`. Site key may never reach `site-config.php`; production host requires token when configured. |
| **Expected result** | Server-side `config.local.php` follows `config.local.php.example`; `site-config.php` returns JSON with `recaptchaSiteKey`; form POST succeeds (not HTTP 422) on production. |
| **Risk** | **High** — all production form submissions may fail security check after deploy or config drift. |

---

### TR-P0-003 — Local secrets copied into `dist/` on build

| Field | Value |
|-------|-------|
| **ID** | TR-P0-003 |
| **Title** | Review `copyLocalBackendConfig` deploy safety |
| **Area** | Build / Backend |
| **Problem** | Gulp `copyLocalBackendConfig` copies `backend/config.local.php` → `dist/backend/config.local.php` when present (observed in build log 2026-06-01). If docroot exposes `dist/backend/`, secret keys could become web-accessible. |
| **Expected result** | Deploy checklist ensures `config.local.php` lives outside public docroot or is blocked by server rules; build pipeline documented so operators never upload secrets to a public path. |
| **Risk** | **High** — credential exposure if hosting layout is misconfigured. |

---

## P1 — High

### TR-P1-001 — `5-tonn` fails canonical copy marker check

| Field | Value |
|-------|-------|
| **ID** | TR-P1-001 |
| **Title** | Align `5-tonn` FAQ denied-goods wording with charter |
| **Area** | Content / FAQ |
| **Problem** | `verify-final-wave-dist.mjs` fails `5-tonn` for missing exact string **`Что не перевозим`**. Route FAQ uses **«Что вы не перевозите?»** (item 6) instead of canonical fixed title per `TRIUMPH-V6-CURRENT-FRONTEND-RULES.md`. Tasks section has correct `Что не&nbsp;перевозим` heading but verifier scans full HTML. |
| **Expected result** | Dist HTML contains canonical marker; FAQ item title matches charter without changing meaning. |
| **Risk** | **Medium** — rollout parity gate failure; inconsistent qualification copy across routes. |

---

### TR-P1-002 — Hero cargo-card CTA text clips at 1280px

| Field | Value |
|-------|-------|
| **ID** | TR-P1-002 |
| **Title** | Fix `.hero__cargo-action` internal overflow @ 1280px |
| **Area** | Hero / SCSS |
| **Problem** | `v6-visual-qa-audit-report-v1.md`: internal overflow (~9–22px) on `.hero__cargo-action` («Заказать перевозку >») at **1280px** on `index`, `5-tonn`, `konteynery`, `oborudovanie`. Root cause: `max-width: 100px` + fixed font size in `_v5-hero-extensions.scss`. |
| **Expected result** | Action label fully visible at 1280px without card layout break; no clipped text in Playwright/visual pass. |
| **Risk** | **Low code risk** — localized SCSS; **medium UX** — CTA illegibility on common laptop width. |

---

### TR-P1-003 — Review block uses placeholders; misleading CTA

| Field | Value |
|-------|-------|
| **ID** | TR-P1-003 |
| **Title** | Trust/reviews section weak for conversion |
| **Area** | Trust / Conversion |
| **Problem** | `screen-03-trust-reviews.html` shows `review-list--placeholder` cards and rating **4.9** without live widget. Button label **«Читать отзывы клиентов»** links to `#contacts` (lead form), not external review sources — label/action mismatch. |
| **Expected result** | Either connect Yandex/Avito widget **or** adjust CTA label to honest action (e.g. scroll to contact / leave request). Placeholder state clearly marked until widget live. |
| **Risk** | **Medium** — trust erosion if users expect real reviews; conversion friction. |

---

### TR-P1-004 — Cookie/analytics policy vs UI gap

| Field | Value |
|-------|-------|
| **ID** | TR-P1-004 |
| **Title** | No cookie consent UI despite legal copy + Metrika |
| **Area** | Legal / Analytics |
| **Problem** | Legal content (`cookie-files-policy.html`, `privacy-policy.html`) describes cookie use and optional first-visit notice. Site loads Yandex Metrika (`109490539`, webvisor) on all PPC pages but **no cookie banner / consent UI** found in `src/`. |
| **Expected result** | HITL decision: implement consent banner **or** update legal copy to match actual implementation; analytics firing aligned with consent policy. |
| **Risk** | **Medium–High** — compliance gap (operator/legal review required). |

---

### TR-P1-005 — Form live testing incomplete across routes

| Field | Value |
|-------|-------|
| **ID** | TR-P1-005 |
| **Title** | Spot-test all 36 production forms on hosting |
| **Area** | Forms / QA |
| **Problem** | Only `konteynery` hero form confirmed live (`v6-live-mail-test-report-v1.md`). Each PPC page has **3 forms** (hero, FAQ contact, modal callback) × 12 routes = **36** paths; reCAPTCHA + mail not verified per route/CTA source. |
| **Expected result** | Matrix test: each `data-form-id` POST → 200 JSON + email received + Metrika `form-lead` on production (sample or full per charter). |
| **Risk** | **Medium** — silent failure on untested routes. |

---

### TR-P1-006 — Incomplete `data-landing-id` on body tags

| Field | Value |
|-------|-------|
| **ID** | TR-P1-006 |
| **Title** | Add missing `data-landing-id` on PPC pages |
| **Area** | Pages / Analytics |
| **Problem** | `data-landing-id` present on 6 routes (`kray`, `yurlic`, `vezdehod`, `stroymaterialy`, `kirpich-bloki`, `armatura`) but **absent** on `index`, `5-tonn`, `bytovki`, `konteynery`, `oborudovanie`, `fbs-zhbi`. `form.js` falls back to `data-page-type` but mailer attribution less explicit. |
| **Expected result** | All 12 PPC pages set consistent `data-landing-id="<slug>"` on `<body>`. |
| **Risk** | **Low** — attribution noise in lead emails / Metrika debugging. |

---

### TR-P1-007 — Legal pages `noindex` while linked from indexed PPC

| Field | Value |
|-------|-------|
| **ID** | TR-P1-007 |
| **Title** | Confirm legal pages robots/indexing policy |
| **Area** | Legal / SEO |
| **Problem** | Four legal routes built (`privacy-policy/`, `user-agreement/`, `consent-personal-data/`, `cookie-files-policy/`) with **`robots: noindex,nofollow`**. Footer + form consent links point to them from **`index,follow`** PPC pages. Sitemap excludes legal URLs. |
| **Expected result** | Operator charter: keep legal noindex (typical) **or** switch to indexable with sitemap entries; policy documented. |
| **Risk** | **Low SEO** if intentional; **medium** if legal discoverability required. |

---

### TR-P1-008 — Modal vs `#contacts` CTA pattern ambiguity

| Field | Value |
|-------|-------|
| **ID** | TR-P1-008 |
| **Title** | Clarify mid-page CTA behavior (modal vs scroll) |
| **Area** | CTA / Conversion |
| **Problem** | Widespread pattern: `href="#contacts"` + `data-modal-open="modal-callback"`. `modal.js` `preventDefault` → opens callback modal, **does not scroll** to embedded contact form. Users may expect inline form at `#contacts`. Affects header CTA, specs, tasks, order-steps, pricing CTAs (~40+ triggers). |
| **Expected result** | HITL product decision documented; either keep modal-first (update labels) **or** split behaviors (scroll vs modal) consistently. |
| **Risk** | **Medium** — unexpected UX; possible lower inline-form conversion. |

---

### TR-P1-009 — `5-tonn` route content/style inconsistencies

| Field | Value |
|-------|-------|
| **ID** | TR-P1-009 |
| **Title** | Normalize `5-tonn` partials to zakaz baseline quality |
| **Area** | Content / Hero |
| **Problem** | Beyond encoding: hero specs use hyphen `-` vs em dash `—` (zakaz uses `—`); success messages use `-` not `—`; FAQ has **7 items** vs **6** on zakaz; section-lead missing `&nbsp;` discipline in places. |
| **Expected result** | Visual/typographic parity with canonical zakaz route except intentional copy differences. |
| **Risk** | **Low** — brand consistency. |

---

### TR-P1-010 — Machine showcase images mostly baseline placeholder

| Field | Value |
|-------|-------|
| **ID** | TR-P1-010 |
| **Title** | Route-specific machine images not mapped |
| **Area** | Images / Trust |
| **Problem** | 10 of 12 PPC spec sections use `machine-showcase__media--index-baseline` (same image). Only `yurlic` and `kray` use `--portrait-2x3`. Image mapping pass deferred per V6 image policy. |
| **Expected result** | Per-route semantic images + verified alt text per charter (`V6 ROUTE IMAGE POLICY`). |
| **Risk** | **Medium** — intent mismatch on cargo-specific landing pages. |

---

### TR-P1-011 — Accessibility not audited

| Field | Value |
|-------|-------|
| **ID** | TR-P1-011 |
| **Title** | Run accessibility pass (contrast, focus, SR) |
| **Area** | QA |
| **Problem** | Visual QA explicitly excluded a11y. Forms use `aria-live`, modal focus trap present, but no systematic contrast/focus-order/screen-reader verification. |
| **Expected result** | Documented a11y spot-check or audit report for hero form, modal, FAQ `<details>`, mobile drawer. |
| **Risk** | **Unknown** until tested. |

---

### TR-P1-012 — Footer hash cleanup not browser-verified

| Field | Value |
|-------|-------|
| **ID** | TR-P1-012 |
| **Title** | Live-verify footer/header hash stripping |
| **Area** | JS / Navigation |
| **Problem** | `stripHashFromUrl()` present in `header-menu.js` (source + dist per freeze report) but not manually verified in browser after footer nav click. |
| **Expected result** | Clicking footer `#faq`, `#contacts`, etc. scrolls correctly and URL stays clean (no lingering hash). |
| **Risk** | **Low** — polish/SEO URL hygiene. |

---

## P2 — Medium

### TR-P2-001 — Meta description «Расчет» vs «Расчёт» inconsistency

| Field | Value |
|-------|-------|
| **ID** | TR-P2-001 |
| **Title** | Unify ё/е spelling in meta descriptions |
| **Area** | Content / SEO |
| **Problem** | Several routes use **«Расчет»** (`bytovki`, `fbs-zhbi`, `armatura`, `kirpich-bloki`, `stroymaterialy`, `vezdehod`, `oborudovanie`) while `index`, `kray`, `yurlic` use **«Расчёт»**. |
| **Expected result** | Consistent orthography per brand/SEO guideline (prefer `Расчёт` with ё). |
| **Risk** | **Low** |

---

### TR-P2-002 — Tasks heading nbsp inconsistency

| Field | Value |
|-------|-------|
| **ID** | TR-P2-002 |
| **Title** | Apply nbsp to «Что не перевозим» in all tasks partials |
| **Area** | Typography |
| **Problem** | `zakaz` / `5-tonn` use `Что не&nbsp;перевозим`; 10 other slugs use plain spaces (`Что не перевозим`). |
| **Expected result** | Uniform `&nbsp;` per Factory typography rules. |
| **Risk** | **Low** — word-break/layout |

---

### TR-P2-003 — `white-space: nowrap` pressure points

| Field | Value |
|-------|-------|
| **ID** | TR-P2-003 |
| **Title** | Audit nowrap selectors on narrow viewports |
| **Area** | SCSS / Mobile |
| **Problem** | `nowrap` in `_screen-04-faq.scss`, `_screen-02-prices.scss`, `_modal.scss`. Visual QA found no overflow yet; `body { overflow-x: hidden }` may mask edge cases. |
| **Expected result** | Confirm no clip/overflow at 320–430px on FAQ summaries, price labels, modal titles. |
| **Risk** | **Low–Medium** on small phones |

---

### TR-P2-004 — Modal layout not visually QA'd at all breakpoints

| Field | Value |
|-------|-------|
| **ID** | TR-P2-004 |
| **Title** | Visual QA callback + phone modals |
| **Area** | Modal / Mobile |
| **Problem** | Visual audit did not open modals. `modal-phone` opens desktop-only via `data-desktop-modal-open` (≥1025px); mobile uses direct `tel:`. |
| **Expected result** | Modal open/close/focus/scroll-lock verified at 390, 768, 1024, 1440. |
| **Risk** | **Low–Medium** |

---

### TR-P2-005 — Lazy-load empty machine frame before scroll

| Field | Value |
|-------|-------|
| **ID** | TR-P2-005 |
| **Title** | Review lazy-load UX for showcase images |
| **Area** | Images / Performance |
| **Problem** | Full-page captures at 1280px may show empty white media frame before lazy images enter viewport; in-viewport load confirmed OK. |
| **Expected result** | Decision: keep lazy (acceptable) **or** prioritize above-fold image with `fetchpriority` / eager load for LCP. |
| **Risk** | **Low** — perceived quality |

---

### TR-P2-006 — Legal pages missing Metrika (intentional?)

| Field | Value |
|-------|-------|
| **ID** | TR-P2-006 |
| **Title** | Decide analytics on legal routes |
| **Area** | Legal / Analytics |
| **Problem** | `scripts-legal.html` loads only `main.js` (no Metrika). Legal pages isolated from conversion tracking. |
| **Expected result** | Documented choice: no tracking on legal **or** add lightweight Metrika for compliance funnels. |
| **Risk** | **Low** |

---

### TR-P2-007 — Legal header/footer asset path depth

| Field | Value |
|-------|-------|
| **ID** | TR-P2-007 |
| **Title** | Verify legal nested paths after deploy |
| **Area** | Legal / Build |
| **Problem** | Legal pages live at `dist/<slug>/index.html`; gulp rewrites `/assets/` to `../assets/`. Must verify CSS/JS/logo paths on hosting (not re-verified in this pass). |
| **Expected result** | All 4 legal routes render styled content with working back-link and footer on production CDN. |
| **Risk** | **Medium** if rewrite broken on server |

---

### TR-P2-008 — Sass legacy JS API deprecation

| Field | Value |
|-------|-------|
| **ID** | TR-P2-008 |
| **Title** | Plan Sass API migration |
| **Area** | Build |
| **Problem** | Build emits Dart Sass legacy JS API deprecation warning. |
| **Expected result** | Toolchain updated before Sass 2.0 removal (non-blocking today). |
| **Risk** | **Low** now; **Medium** future |

---

### TR-P2-009 — `form.js` cache-buster query string

| Field | Value |
|-------|-------|
| **ID** | TR-P2-009 |
| **Title** | Review hardcoded `?v=metrika-goal-debug-v1` |
| **Area** | JS / Deploy |
| **Problem** | `scripts-v5-page01.html` loads `form.js?v=metrika-goal-debug-v1` — debug-era version string may confuse cache policy. |
| **Expected result** | Production cache strategy documented; version bump process defined. |
| **Risk** | **Low** |

---

### TR-P2-010 — Legacy `final-contact-cta.html` artifacts in repo

| Field | Value |
|-------|-------|
| **ID** | TR-P2-010 |
| **Title** | Guard against duplicate `#contacts` on rollout |
| **Area** | Partials / Architecture |
| **Problem** | 12 slugs retain standalone `final-contact-cta.html` (each defines `id="contacts"`). Not included in active pages but high agent confusion risk (`V6-LEGACY-AND-DEAD-AUDIT.md`). |
| **Expected result** | Rollout checklist enforced; optional quarantine/README markers expanded. |
| **Risk** | **High if mistakenly included** — duplicate IDs/forms |

---

### TR-P2-011 — Orphan partials volume (102 unreferenced)

| Field | Value |
|-------|-------|
| **ID** | TR-P2-011 |
| **Title** | Reduce agent drift from dead partials |
| **Area** | Architecture |
| **Problem** | 102/117 partials not in `index.html` closure — v2/v3 duplicates, v5-page01 alternate stack, PPC scaffolds. |
| **Expected result** | Future quarantine pass (human-approved) or stronger pointer docs in active map. |
| **Risk** | **Medium** — wrong partial copied during edits |

---

### TR-P2-012 — `#specs` section not in header nav

| Field | Value |
|-------|-------|
| **ID** | TR-P2-012 |
| **Title** | Evaluate adding specs to navigation |
| **Area** | Navigation |
| **Problem** | Machine specs section uses `id="specs"` but header/footer nav lists only `#tasks`, `#pricing`, `#reviews`, `#faq`, `#contacts`. |
| **Expected result** | Product decision: add link **or** document intentional omission. |
| **Risk** | **Low** |

---

### TR-P2-013 — Duplicate mobile drawer messenger/CTA blocks

| Field | Value |
|-------|-------|
| **ID** | TR-P2-013 |
| **Title** | Simplify header drawer contact redundancy |
| **Area** | Header / Mobile |
| **Problem** | `header-v5-page01.html` drawer has messenger + CTA in **both** `drawer-mid` and `drawer-contact` sections. |
| **Expected result** | Single coherent contact cluster in mobile menu. |
| **Risk** | **Low** — visual clutter |

---

### TR-P2-014 — Inconsistent legacy form IDs in unused partials

| Field | Value |
|-------|-------|
| **ID** | TR-P2-014 |
| **Title** | Align legacy artifact form IDs |
| **Area** | Forms |
| **Problem** | Unused `final-contact-cta.html` files: e.g. `5tonn-contact-quote` vs active `5-tonn-contact-quote`; `kirpich-contact-quote` vs `kirpich-bloki-contact-quote`; `fbs-contact-quote` vs `fbs-zhbi-contact-quote`. |
| **Expected result** | If artifacts kept, IDs match active naming to prevent copy-paste mistakes. |
| **Risk** | **Low** unless legacy included |

---

### TR-P2-015 — `hero__notice` in orphan partial only

| Field | Value |
|-------|-------|
| **ID** | TR-P2-015 |
| **Title** | Remove or quarantine deprecated hero notice |
| **Area** | Hero / Legacy |
| **Problem** | `.hero__notice` remains in unused `v5-page01/screen-01-hero.html` — not in dist (verified) but forbidden on rollout. |
| **Expected result** | Quarantined or deleted in future cleanup pass. |
| **Risk** | **Low** |

---

### TR-P2-016 — B2B strip shared across all routes

| Field | Value |
|-------|-------|
| **ID** | TR-P2-016 |
| **Title** | Review B2B block relevance per intent |
| **Area** | Content |
| **Problem** | All 12 routes share identical `screen-03b-b2b.html` — may be correct for universal offer, but cargo-specific pages might need route-tuned B2B copy (HITL). |
| **Expected result** | Operator confirms shared block OK **or** schedules per-route copy adaptation. |
| **Risk** | **Low** — message fit |

---

### TR-P2-017 — Pricing-factors CTA copy uses «расчeta» variant spellings

| Field | Value |
|-------|-------|
| **ID** | TR-P2-017 |
| **Title** | Normalize «расчета/расчёта» in pricing CTAs |
| **Area** | Content |
| **Problem** | Several pricing-factor buttons use **«расчeta»** without ё (`stroymaterialy`, `kirpich-bloki`, `armatura`, `fbs-zhbi`, `oborudovanie`). |
| **Expected result** | Consistent Russian orthography. |
| **Risk** | **Low** |

---

### TR-P2-018 — Metrika goal firing pre/post deploy unknown

| Field | Value |
|-------|-------|
| **ID** | TR-P2-018 |
| **Title** | Verify `form-lead` goal in Metrika UI |
| **Area** | Analytics |
| **Problem** | Goal wired in `form.js` (`109490539`, `form-lead`, production mode only) but Metrika reporting UI not verified in this pass. Debug logging still in source (`metrika-goal-debug-v1`). |
| **Expected result** | Production submit triggers goal visible in Metrika; debug version string retired when stable. |
| **Risk** | **Medium** — blind conversion optimization |

---

## P3 — Cosmetic

### TR-P3-001 — V4 docs clutter in `docs/`

| Field | Value |
|-------|-------|
| **ID** | TR-P3-001 |
| **Title** | Archive or relocate V4 reconstruction docs |
| **Area** | Docs |
| **Problem** | 11× `V4-*.md` files in V6 `docs/` — not build inputs; may confuse operators. |
| **Expected result** | Moved to archive or indexed in deprecation doc. |
| **Risk** | **Low** |

---

### TR-P3-002 — `.prices` class name on tasks section

| Field | Value |
|-------|-------|
| **ID** | TR-P3-002 |
| **Title** | Legacy class naming on tasks section |
| **Area** | HTML semantics |
| **Problem** | `screen-02-tasks.html` uses `class="prices"` wrapper for historical reasons — naming drift vs tasks content. |
| **Expected result** | Optional rename in dedicated refactor (low priority). |
| **Risk** | **Low** — dev confusion only |

---

### TR-P3-003 — Button arrow uses ASCII `->`

| Field | Value |
|-------|-------|
| **ID** | TR-P3-003 |
| **Title** | Review `button--arrow` glyph |
| **Area** | Buttons |
| **Problem** | `_button.scss` uses ASCII `->` not typographic arrow (`→`). Used on reviews CTA. |
| **Expected result** | Consistent brand arrow styling if desired. |
| **Risk** | **None** |

---

### TR-P3-004 — FAQ first item always `open`

| Field | Value |
|-------|-------|
| **ID** | TR-P3-004 |
| **Title** | FAQ default open state |
| **Area** | FAQ |
| **Problem** | First `<details class="faq-item" open>` on all routes — accordion JS closes others on toggle. Default open may vary by route intent. |
| **Expected result** | Optional: all closed by default for cleaner fold. |
| **Risk** | **Low** |

---

### TR-P3-005 — Polygon copyright footer line

| Field | Value |
|-------|-------|
| **ID** | TR-P3-005 |
| **Title** | Confirm polygon-copyright visibility/styling |
| **Area** | Footer |
| **Problem** | `polygon-copyright.html` included in landing footer — verify styling matches footer dark theme on all breakpoints. |
| **Expected result** | Visually integrated, not broken on mobile. |
| **Risk** | **Low** |

---

### TR-P3-006 — Legal entity address not in footer

| Field | Value |
|-------|-------|
| **ID** | TR-P3-006 |
| **Title** | Legal address display gap |
| **Area** | Footer / Legal |
| **Problem** | Footer shows «Краснодар, Россия» only; `LEGAL-ENTITY-CARD-v1.md` marks full address as **unknown**. |
| **Expected result** | Operator supplies address **or** documents intentional omission. |
| **Risk** | **Low** legal display |

---

### TR-P3-007 — Hero cargo cards use `>` not `→`

| Field | Value |
|-------|-------|
| **ID** | TR-P3-007 |
| **Title** | Cargo card action chevron style |
| **Area** | Hero / Cards |
| **Problem** | Action text «Заказать перевозку >» uses ASCII greater-than. |
| **Expected result** | Optional typographic polish. |
| **Risk** | **None** |

---

### TR-P3-008 — `5-tonn` FAQ item count (7 vs 6)

| Field | Value |
|-------|-------|
| **ID** | TR-P3-008 |
| **Title** | FAQ count parity across routes |
| **Area** | FAQ |
| **Problem** | `5-tonn` has 7 FAQ items; zakaz has 6. Extra «Как быстро заказать» may be intentional. |
| **Expected result** | HITL confirms keep **or** harmonize count. |
| **Risk** | **Low** |

---

### TR-P3-009 — Shared trust/reviews/B2B/dark-proof across routes

| Field | Value |
|-------|-------|
| **ID** | TR-P3-009 |
| **Title** | Shared v5-page01 blocks identical on all PPC |
| **Area** | Content |
| **Problem** | `screen-03-trust-reviews`, `screen-03b-b2b`, `dark-proof-strip` shared without route customization. |
| **Expected result** | Accept as baseline **or** schedule route-specific trust copy. |
| **Risk** | **Low** |

---

### TR-P3-010 — Build copies `config.local.php` console warning noise

| Field | Value |
|-------|-------|
| **ID** | TR-P3-010 |
| **Title** | Operator build log clarity |
| **Area** | DX |
| **Problem** | Every build logs secret-copy warning — useful but noisy for CI/logs. |
| **Expected result** | Optional flag to suppress when not deploying. |
| **Risk** | **None** |

---

## QUICK WINS

Items: **small effort**, **high impact**, **low risk**.

| ID | Title | Area | Why quick win |
|----|-------|------|----------------|
| **QW-001** | Fix `5-tonn.html` UTF-8 encoding (TR-P0-001) | Pages | Single-file save-as-UTF-8; immediate SEO fix |
| **QW-002** | Add `data-landing-id` to 6 missing PPC pages (TR-P1-006) | Pages | One attribute per `*.html` body tag |
| **QW-003** | Rename `5-tonn` FAQ item 6 to include «Что не перевозим» (TR-P1-001) | FAQ | Single summary string; fixes verify script |
| **QW-004** | Normalize «Расчет» → «Расчёт» in meta descriptions (TR-P2-001) | SEO | Page head strings only |
| **QW-005** | Add `&nbsp;` to «Что не перевозим» in 10 tasks partials (TR-P2-002) | Typography | One heading per file |
| **QW-006** | Relax `.hero__cargo-action` max-width @ 1280 (TR-P1-002) | SCSS | ~3–5 lines in `_v5-hero-extensions.scss` |
| **QW-007** | Rename reviews CTA «Читать отзывы» → honest label (TR-P1-003) | Conversion | Single anchor text change |
| **QW-008** | Format `config.local.php` from example (TR-P0-002) | Backend | Ops task, unblocks all forms |

---

## IMPLEMENTATION WAVES

### Wave 1 — Critical fixes

**Goal:** Restore production correctness and security baseline.

| Items |
|-------|
| TR-P0-001, TR-P0-002, TR-P0-003 |
| TR-P1-001 (charter marker) |
| TR-P1-005 (minimal: re-test hero form on `index` + modal on `index` after P0 fixes) |

**Exit criteria:** `verify-final-wave-dist.mjs` all PASS; `5-tonn` title readable; one successful production form POST with reCAPTCHA; deploy checklist for secrets signed off.

---

### Wave 2 — UX + conversion

**Goal:** Improve lead capture clarity and trust.

| Items |
|-------|
| TR-P1-003, TR-P1-004, TR-P1-008 |
| TR-P1-005 (full 36-form matrix or agreed sample) |
| TR-P1-006, TR-P1-012 |
| TR-P2-018 |
| QW-007 |

**Exit criteria:** CTA behavior documented; cookie/consent HITL decision applied; Metrika goal confirmed; review CTA honest; footer hash verified live.

---

### Wave 3 — Visual polish

**Goal:** Layout, typography, imagery consistency.

| Items |
|-------|
| TR-P1-002, TR-P1-009, TR-P1-010 |
| TR-P2-001, TR-P2-002, TR-P2-003, TR-P2-004, TR-P2-005, TR-P2-017 |
| TR-P2-013 |
| QW-004, QW-005, QW-006 |

**Exit criteria:** Visual re-pass at 390/768/1024/1280/1440; no cargo-card clip; route images mapped or baseline documented per route; typography parity.

---

### Wave 4 — Nice-to-have

**Goal:** Cleanup, architecture hygiene, optional enhancements.

| Items |
|-------|
| TR-P1-007, TR-P1-011 |
| TR-P2-006, TR-P2-007, TR-P2-008, TR-P2-009, TR-P2-010, TR-P2-011, TR-P2-012, TR-P2-014, TR-P2-015, TR-P2-016 |
| TR-P3-001 through TR-P3-010 |

**Exit criteria:** Legacy quarantine plan approved; a11y spot report filed; legal indexing policy closed; toolchain deprecation tracked.

---

## AUDIT INVENTORY — AREA CHECKLIST

| Area | Files / scope | Status | Notes |
|------|---------------|--------|-------|
| **Pages** | 12 PPC + 4 legal | Reviewed | Legal built to `dist/<slug>/index.html` |
| **Partials** | 117 HTML | Reviewed | 102 orphan — see TR-P2-011 |
| **SCSS** | 32 files | Reviewed | Breakpoints 1024/1025 primary; 1490 header |
| **JS** | 5 modules + main | Reviewed | form, modal, header-menu, faq-accordion |
| **Forms** | 3 per PPC page | Reviewed | `backend/send-lead.php`; honeypot `company_url` |
| **Legal** | 4 routes + content partials | Reviewed | noindex; no cookie UI |
| **Footer** | `landing-footer.html` | Reviewed | Canonical contacts/messengers OK per freeze |
| **Header** | `header-v5-page01.html` | Reviewed | Drawer redundancy TR-P2-013 |
| **Hero** | `screen-01-hero.html` × 12 | Reviewed | Cargo clip TR-P1-002 |
| **Cards** | trust, cargo, tasks | Reviewed | Placeholder reviews TR-P1-003 |
| **FAQ** | `screen-04-faq.html` × 12 | Reviewed | Split-cta + embedded `#contacts` canonical |
| **Contacts** | FAQ aside + channels | Reviewed | Phone/email/messengers canonical |
| **CTA** | Modal + inline forms | Reviewed | Modal-first pattern TR-P1-008 |
| **Mobile** | Visual QA 390–1024 | Partial | Modals not opened TR-P2-004 |

---

## RECOMMENDED FIRST WAVE

**Start with Wave 1** — specifically **QW-001 + QW-008 + TR-P0-003** in immediate sequence:

1. Re-encode/fix `5-tonn.html` (UTF-8) — unblocks SEO on a live sitemap URL.  
2. Fix `config.local.php` format on server/local — unblocks all production forms.  
3. Confirm deploy path does not expose `config.local.php` — closes security gap.  
4. Fix `5-tonn` «Что не перевозим» marker — green `verify-final-wave-dist.mjs`.

These are smallest diffs with highest production impact before any visual polish.

---

## SAFE UNKNOWN

| Item | Status |
|------|--------|
| Live production state vs this workspace snapshot | **UNKNOWN** — audit is source + build based |
| Full browser QA at all breakpoints after latest edits | **UNKNOWN** — visual QA dated 2026-05-29 |
| reCAPTCHA Google `siteverify` with current keys | **UNKNOWN** — not live-tested this session |
| Metrika `form-lead` in reporting UI | **UNKNOWN** |
| Email deliverability (SPF/DKIM) under volume | **UNKNOWN** |
| Legal pages on production host (styled, linked) | **UNKNOWN** — built locally to dist |
| Cookie consent legal requirement interpretation | **UNKNOWN** — needs operator/legal HITL |
| Whether modal-first CTA is intentional product design | **UNKNOWN** — needs operator confirmation |
| Accessibility (contrast, SR) | **UNKNOWN** |
| CDN cache invalidation after deploy | **UNKNOWN** |
| Whether `5-tonn` encoding corruption already fixed on production | **UNKNOWN** — verify live `view-source` |

---

## RELATED REPORTS (not modified)

- `reports/v6-visual-qa-audit-report-v1.md`
- `reports/v6-production-candidate-freeze-report-v1.md`
- `reports/v6-recaptcha-config-check-report-v1.md`
- `reports/v6-live-mail-test-report-v1.md`

---

*End of TRIUMPH-POLISH-BACKLOG-v1 — preparation only, no implementation.*
