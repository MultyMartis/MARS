# V5 Production Hardening Audit v1

**Workspace:** `workspaces/triumph-manipulator-landing-v5/`  
**Baseline commit:** `f86dd59` — `checkpoint: add Triumph landing v5 baseline`  
**Audit date:** 2026-05-24  
**Method:** Read-only Website Factory + MARS Survivability hardening audit (no fixes applied)  
**Page scope:** `src/pages/index.html` → `dist/index.html` (zakaz / page-01 PPC baseline)

---

## Baseline

| Check | Result |
|-------|--------|
| `git rev-parse HEAD` | `f86dd59` (matches declared baseline) |
| `git status -- workspaces/triumph-manipulator-landing-v5/` | **Clean** — no staged/unstaged changes under V5 |
| V5 `src/` vs commit | **Clean** — audit reads committed baseline |
| Unrelated repo drift | **Present** — large dirty tree outside V5 (V4, ORCA, governance, mars-survivability docs, homegateway, etc.); **not** part of this audit scope |
| Local-only (gitignored) | `dist/`, `node_modules/`, `backend/`, `docs/`, `design/` — exist on disk but excluded from baseline commit per `.gitignore` |
| Build evidence | Prior `v5-baseline-audit-v1.md` records `npm run build` PASS; this pass did not re-run build (read-only) |

**Index composition (frozen baseline):**

- Entry: `src/pages/index.html` with `data-page-type="ppc-zakaz-manip"`
- Includes: `v5-ppc/zakaz/*` + shared `v5-page01/*` partials
- **Not built:** 11 other `v5-ppc/*` slug folders (generator leakage — partials only)
- **Not built:** legal page entries (legal partials exist; no `src/pages/*.html` for them)

---

## Survivability preflight

Manual G2/G3/G4 mindset (per `projects/mars-survivability/protocols/safe-execution-layer-v1.md`):

| Gate | Assessment |
|------|------------|
| **Scope lock** | This audit: read-only + single report file under V5 `reports/`. **PASS** |
| **Protected zones** | No edits to `governance/`, `projects/mars-survivability/`, `projects/mars-website-factory/`, V4, ORCA. **PASS** |
| **Snapshot before future fixes** | **Required** — recommend manifest/snapshot of `workspaces/triumph-manipulator-landing-v5/src/` at `f86dd59` (or current HEAD) before Batch A |
| **Risk class (this audit)** | R0 read + R1 single report write in scoped workspace |
| **Future fix batches** | Mostly R1 scoped writes in V5 `src/`; asset pruning R2 (multi-file delete) → human approval; regen `dist/` = R3 deny for agent without explicit instruction |
| **Forbidden ops** | commit, push, reset, clean, generator 12-page rollout, redesign, V4/ORCA/governance edits |
| **Drift hazard** | Heavy unrelated changes in `workspaces/triumph-manipulator-landing-v4/` — future V5 work must not assume V4 dirty tree as SoT |

---

## Website Factory audit

| Rule area | Status | Notes |
|-----------|--------|-------|
| Source structure | **PASS** | `src/pages`, `partials/{layout,sections,components}`, `scss`, `js`, `img` — standard Gulp layout |
| src/dist discipline | **PASS** | Gulp builds `dist/`; `rewriteHtmlAssetPaths()` converts `/assets/` → relative `assets/` |
| No hand-edit dist | **PASS** (policy) | `dist/` gitignored; fixes must target `src/` |
| Generator leakage | **WARN** | 12× `v5-ppc/<slug>/` partial trees + legacy V4 section partials in tree; only `index.html` in `src/pages/` |
| Page source clarity | **PASS** | Single entry; includes explicit |
| Asset source clarity | **PASS** | README + `v5-baseline-audit-v1.md` document hero/second-screen locks |
| shared-assets lock | **PASS** | `hero-bg-final.jpg`, `second-screen-index-baseline.jpg` present in `src/img/` |
| Section order stability | **PASS** | Hero → specs → tasks → steps → pricing factors → trust → b2b → proof → faq → contact → footer |
| Container consistency | **PASS** | `section-shell` + `page-container` mixins; hero uses `hero__shell` |
| Responsive discipline | **PARTIAL** | Breakpoints 1180/760/520/420; **SAFE UNKNOWN** — no live browser matrix in this pass |
| Mobile overflow risks | **WARN** | `white-space: nowrap` on header + spec `dd`; `overflow-wrap: anywhere` on mobile buttons/footer |
| Form/modal risks | **WARN** | Mock submit only; hybrid `href="#contacts"` + `data-modal-open` on anchors |
| CTA consistency | **PASS** | `data-cta-source` pattern; `@@prefix` replaced in dist (`zakaz-header-cta`, etc.) |
| Legal/footer risks | **WARN** | Root-absolute legal URLs (`/privacy-policy/`); placeholder Telegram `https://t.me/` |

---

## Typography audit

**In scope:** visible H1–H3, paragraphs, CTA, buttons, labels, FAQ, consent, navigation.  
**Out of scope (unchanged):** meta, alt, JSON-LD, data attributes, href/src.

| Finding | Location | Future fix |
|---------|----------|------------|
| `&nbsp;` density high | Most `v5-ppc/zakaz/*`, `v5-page01/*` partials | Human pass: orphan short words without `&nbsp;` on 320–390px |
| `white-space: nowrap` | `_header.scss` — `.site-header__nav`, `__phone`, `__cta` | Test ≤1180px; allow wrap or shorten CTA on narrow desktop |
| `white-space: nowrap` | `_screen-02-prices.scss` — `.machine-showcase__specs dd` | Risk: «5 т», «14 м» row overflow; consider `nowrap` removal + `min-width: 0` |
| `overflow-wrap: anywhere` | `_landing-footer.scss` (mobile), `_v5-page01-overrides.scss` `.button`, `_screen-02-prices.scss` | Prefer `break-word` on buttons; reserve `anywhere` for long legal tokens only |
| H1 line-height | `_v5-hero-extensions.scss` `.hero--v5 .hero__title` — `line-height: 1.06` | OK (ratio, not px hack) |
| Legacy H1 px lh | `_screen-01-hero.scss` `.hero__title` — `line-height: 90px` | Dead for v5 hero but still in bundle; low priority cleanup |
| px line-height pairs | Many rules use `font-size N` + `line-height N+4` (e.g. 16/20, 14/18, 12/16) | Audit sample **mostly compliant** |
| px line-height mismatch | `_screen-02-prices.scss` `dd`: `clamp(26–38px)` + `line-height: 42px` | Not strict +4; verify mobile 26/42 |
| `_dark-proof-strip.scss` | `line-height: 40px` on large type | Verify paired `font-size` on 760px |
| Section H2 | `_section-headings.scss` — ratio `1.1` / `1.14` | Acceptable; not px+4 rule target |
| Consent text | `_forms.scss` 12/16 | Compliant |
| FAQ text | `v5-ppc/zakaz/screen-04-faq.html` | `&nbsp;` throughout — OK |

---

## CLS/font audit

| Finding | Severity | Detail |
|---------|----------|--------|
| Google Fonts external | **High** | `head-v5-page01.html` lines 15–17: `fonts.googleapis.com` + `fonts.gstatic.com`; blocks offline/file:// font load |
| No self-hosted fonts | **High** | `src/fonts/` exists (empty); gulp `fonts` task copies nothing |
| No `preload` for fonts | **Medium** | Only preconnect to Google; no `font-display` control on self-hosted (N/A until self-host) |
| `display=swap` in Google URL | **Low** | Present in CSS URL; still network-dependent |
| Hero `<img>` dimensions wrong | **High** | HTML: `width="1920" height="1080"`; file: **2560×1440** → CLS until image loads |
| Second screen dimensions | **PASS** | HTML `1696×2528` matches file |
| Hero dual background | **Medium** | `<img class="first-screen__bg-media">` + legacy `.first-screen { background: url(...) }` in `_base.scss` (overridden for `ppc-*` but CSS still ships) |
| Hero `fetchpriority="high"` | **PASS** | Present on hero img |
| Second screen `loading="lazy"` | **PASS** | Present |
| No skeleton | **Low** | Hero uses img+overlay; acceptable if dimensions fixed |
| Montserrat/Roboto fallbacks | **PASS** | `Arial, sans-serif` in tokens |

---

## CSS/layout audit

| Finding | Status | Location |
|---------|--------|----------|
| `border-radius: 0` policy | **Intentional** | `_radius-zero.scss`, tokens `$radius-*: 0` |
| Global `outline: none` | **Risk** | `_reset.scss` `*, *::before, *::after { outline: none }` |
| Compensating `:focus-visible` | **Partial** | Header, form inputs, consent box, modal close — **not** global for all interactives |
| `scrollbar-gutter: stable` | **PASS** | `_reset.scss` on `html` |
| Container width 1600px | **PASS** | `_tokens.scss` `$container` |
| z-index scale | **PASS** | `_layers.scss`: header 120, menu 130/140, modal 200 |
| Mobile drawer portaled to `body` | **PASS** | `header-menu.js` `portalMenuLayers` |
| Modal body lock | **PASS** | `body.site-modal-open`; menu lock cleared before modal open in `modal.js` |
| FAQ animation | **PASS** | `faq-accordion.js` + `_screen-04-faq.scss` max-height transition |
| `body { overflow-x: hidden }` | **WARN** | `_base.scss` — may mask wide children |
| `min-width: 0` on grids | **PASS** | v5 hero, machine-showcase, order-steps overrides |
| Second screen 50/50 | **PASS** | `.machine-showcase` 2-col; `--index-baseline` uses `object-fit: contain` |
| `object-fit` hero bg | **PASS** | `cover` on `.first-screen__bg-media` |
| Fixed header z-index vs modal | **PASS** | Modal 200 > header 120 |
| `100vh` first screen | **WARN** | `.first-screen { min-height: 100vh }`; mobile switches to `auto` at 760px — iOS bar **SAFE UNKNOWN** |

---

## Forms/JS audit

| Finding | Severity | Detail |
|---------|----------|--------|
| `data-form-handler="mock"` | **Critical** | Hero, contact, modal forms — no live POST to `backend/api/forms/send.php` |
| `DEFAULT_FORM_ENDPOINT` unused | **Medium** | `form.js` defines path; `runSubmitHandler` only supports `mock` |
| Double-submit guard | **PASS** | `submitLock` + disabled submit while loading |
| Consent visual state | **PASS** | Custom checkbox `:checked + .site-form__consent-box` |
| Modal open/close/ESC/focus trap | **PASS** | `modal.js` |
| Phone mask | **PASS** | `bindPhoneMask` on tel fields |
| `console.error` in gulp only | **PASS** | `gulpfile.js` plumber — not in site JS |
| No `console.log` in `src/js` | **PASS** | Verified by search |
| Mobile menu | **PASS** | Drawer + overlay; closes before modal |
| FAQ | **PASS** | Custom accordion; `preventDefault` on summary; one-open-at-a-time |
| Messenger links | **High** | MAX → `#contacts`; Telegram → `https://t.me/` (placeholder) |
| CTA `data-cta-source` | **PASS** | Populated; modal bridge on open |
| Anchor + modal on same element | **Medium** | e.g. `machine-showcase__cta` `<a href="#contacts" data-modal-open="...">` — verify click doesn't jump before modal |

**Backend:** `backend/` exists locally but is **gitignored** — not part of `f86dd59` baseline; production wiring **SAFE UNKNOWN**.

---

## Schema/SEO readiness

| Item | Readiness | Notes |
|------|-----------|-------|
| `<title>` / `<meta description>` | **Present** | Uses `&nbsp;` in meta (acceptable per audit scope) |
| `robots` | **Blocked** | `noindex,nofollow` on index — correct for staging, **must change** for production |
| H1 uniqueness | **PASS** | 1× H1 in dist (`hero__title`) |
| Canonical | **Missing** | Add when production URL frozen |
| OG tags | **Partial** | title/description/type; no `og:url` / image |
| LocalBusiness schema | **Not present** | Readiness: NAP in footer (phone, email, city) — need `@type`, `address`, `telephone` |
| FAQ schema | **Readiness OK** | 6 FAQ items in HTML — map to `FAQPage` when indexing allowed |
| Service schema | **Readiness partial** | Service described in copy; needs dedicated JSON-LD block |
| Breadcrumbs | **N/A** | Single-page PPC |
| AggregateRating | **Do not add** | UI shows «4.9» + stars without evidence block — **no** `AggregateRating` until verified source URLs |
| Legal pages | **Not in build** | Links point to `/privacy-policy/` etc. — pages not in `src/pages/` |

---

## Asset audit

| Asset | Status |
|-------|--------|
| `src/img/hero/hero-bg-final.jpg` | **LOCKED** — matches design pack path per README |
| `src/img/hero/hero-bg-final.png` | **Unused duplicate** — not referenced in HTML/CSS for ppc index |
| `src/img/v5/second-screen/second-screen-index-baseline.jpg` | **LOCKED** — 1696×2528 |
| Other `second-screen-*.jpg` (13 files) | **Unused** for index-only — copied for future PPC pages |
| `second-screen-test-01.jpg` | **Remove candidate** — test artifact |
| `src/img/reconstruction/*` (5 PNG) | **Unused** in index build |
| Font Awesome vendor | **PASS** — self-hosted woff/woff2 + `screen-icons.css` subset |
| Duplicate FA webfonts | **Low** | Both `fa-solid-900` and `free-fa-solid-900` in vendor folder |
| Relative paths in dist | **PASS** — 0× `/assets/` in built `index.html` (29× `assets/`) |
| Absolute legal hrefs | **WARN** | `/privacy-policy/` — breaks pure file:// legal navigation |
| `file://` preview | **Partial** | Assets relative; fonts need network; legal links fail locally |

---

## Critical fixes

1. **Switch forms from `mock` to production handler** — wire `data-form-handler` + POST to `backend/api/forms/send.php` (or agreed endpoint); HITL for server config.
2. **Remove `noindex,nofollow`** when human approves go-live (currently intentional staging).
3. **Fix hero `<img width height>`** to **2560×1440** (or CSS `aspect-ratio` + sized container).
4. **Self-host Montserrat/Roboto** — drop Google Fonts dependency; fill `src/fonts/` + preload/`font-display: swap`.
5. **Replace placeholder messenger URLs** — real MAX deep link; full Telegram channel/bot URL.

---

## High priority fixes

1. Resolve **dual hero background** — remove dead `url()` from `.first-screen` for PPC or strip from bundle scope.
2. Legal/consent links: use **relative** paths for static export (`privacy-policy/index.html`) or document hosting base URL.
3. Header `nowrap` cluster — visual QA at 1024–1180px for overflow/clip.
4. `.machine-showcase__specs dd { white-space: nowrap }` — test on 320px.
5. Replace `overflow-wrap: anywhere` on `.button` (mobile) with `break-word`.
6. Global `outline: none` — audit all focusable elements for `:focus-visible` ring.
7. Prune or quarantine **unused PPC second-screen JPEGs** + reconstruction PNGs + `hero-bg-final.png` + test image (after human list approval).

---

## Medium priority fixes

1. Add `og:url`, `og:image` when production URL/asset frozen.
2. Prepare **canonical** link tag.
3. Document/deploy gitignored `backend/` or move send script into scope with secrets policy.
4. FAQ/section anchor: nav «Цены» → `#pricing` skips `#specs` block — confirm intended IA.
5. Review hybrid CTA anchors (`href` + `data-modal-open`).
6. Empty `src/fonts/` + noop gulp fonts task — implement or remove task.
7. Local `docs/` (V4-named) — not in baseline; delete or relocate outside workspace (human approval).

---

## Low priority fixes

1. Remove legacy `.hero__title { line-height: 90px }` if v4 hero unused.
2. Deduplicate Font Awesome webfont files in vendor.
3. `prefers-reduced-motion` — verify FAQ/header transitions.
4. Add `scroll-margin-top` on `#tasks`, `#pricing`, etc. for sticky header offset.
5. Review rating UI copy vs schema policy before any structured data wave.

---

## What must NOT be changed

- Operator-accepted **visual baseline** (hero composition, dark first screen, zero-radius system, red accent DNA).
- **shared-assets** source locks for hero + index second screen (provenance paths in README).
- **Single-page index-only** scope until explicit 12-page charter (no generator rollout in hardening pass).
- **Section order** on `index.html` as committed.
- Gulp **`/assets/` → relative `assets/`** rewrite behavior (file:// compatibility).
- `data-page-type="ppc-zakaz-manip"` and zakaz partial wiring.
- Z-index scale ordering (modal above menu above header).

---

## SAFE UNKNOWN

- Live browser QA (375 / 390 / 768 / 1024 / 1280 / 1440) — **not run** in this audit.
- iOS Safari `100vh` / sticky / address-bar behavior.
- Real MAX messenger URL and Telegram business link.
- Production hosting path prefix (subdir vs domain root) for legal URLs and form endpoint.
- `backend/` mail config and spam protection — local folder not in git baseline.
- Whether `01.png` exists in design pack (README cites `01.jpg` only).
- Lighthouse / CLS field metrics.
- Human sign-off on «4.9» rating evidence for future schema.

---

## Recommended fix batches

| Batch | Focus | Files (primary) | Risk |
|-------|--------|-----------------|------|
| **A — Production blockers** | Fonts self-host, hero dimensions, robots meta, form handler, messenger URLs | `head-v5-page01.html`, `index.html`, `form.js`, `src/fonts/`, partials CTAs | Medium — HITL for URLs + mail |
| **B — Typography/mobile** | nowrap, overflow-wrap, line-height pairs on specs | `_header.scss`, `_screen-02-prices.scss`, `_v5-page01-overrides.scss`, `_landing-footer.scss` | Low |
| **C — Asset hygiene** | Remove unused images (listed), drop PNG duplicate | `src/img/**` | Medium — R2 delete needs approval |
| **D — SEO readiness** | canonical, OG url/image, robots; schema **notes only** until HITL | `head-v5-page01.html`, new partial optional | Low–medium |
| **E — CSS debt** | dual hero bg, focus outline policy, legal relative paths | `_base.scss`, `_reset.scss`, footer/consent partials | Low |

**Suggested order:** Snapshot → **A** → rebuild `dist/` → human browser check → **B** → **C** (with manifest) → **D** → **E**.

---

*Audit v1 — read-only. No source fixes applied.*
