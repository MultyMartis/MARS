# V6 route family freeze

**Date:** 2026-05-29  
**Status:** FROZEN — route creation phase closed; QA phase next  
**Workspace:** `workspaces/triumph-manipulator-landing-v6/`  
**Snapshot:** `workspaces/_snapshots/snap-20260528-triumph-v6-route-family-freeze/`  
**Baseline commit (pre-freeze):** `be0409e72feb1f43b44de8ed91188eb89a47126a`

This document freezes the current V6 route family state. **Not a rollout.** No new routes, no content generation, no redesign, no structure changes beyond this freeze charter.

---

## SECTION A — Accepted routes

These routes are **accepted and locked** for freeze. Read-only verification allowed; content edits require explicit HITL override.

| Route | Page file | Partial prefix |
|-------|-----------|----------------|
| `index` | `src/pages/index.html` | `v5-ppc/zakaz/` |
| `5-tonn` | `src/pages/5-tonn.html` | `v5-ppc/5-tonn/` |
| `bytovki` | `src/pages/bytovki.html` | `v5-ppc/bytovki/` |
| `konteynery` | `src/pages/konteynery.html` | `v5-ppc/konteynery/` |
| `oborudovanie` | `src/pages/oborudovanie.html` | `v5-ppc/oborudovanie/` |
| `fbs-zhbi` | `src/pages/fbs-zhbi.html` | `v5-ppc/fbs-zhbi/` |
| `armatura` | `src/pages/armatura.html` | `v5-ppc/armatura/` |
| `kirpich-bloki` | `src/pages/kirpich-bloki.html` | `v5-ppc/kirpich-bloki/` |
| `stroymaterialy` | `src/pages/stroymaterialy.html` | `v5-ppc/stroymaterialy/` |
| `vezdehod` | `src/pages/vezdehod.html` | `v5-ppc/vezdehod/` |
| `yurlic` | `src/pages/yurlic.html` | `v5-ppc/yurlic/` |
| `kray` | `src/pages/kray.html` | `v5-ppc/kray/` |

**Hard lock:** `src/pages/index.html` and all accepted route pages listed above — do not modify without explicit override.

---

## SECTION B — Route inventory

### Page shell (shared across all routes)

Each route page includes:

- `partials/layout/head-v5-page01.html`
- `partials/layout/header-v5-page01.html`
- Route-specific `screen-01-hero.html`
- Route-specific `screen-02-specs.html`, `screen-02-tasks.html`, `screen-02b-order-steps.html`, `screen-02c-pricing-factors.html`
- Shared `v5-page01/screen-03-trust-reviews.html`, `screen-03b-b2b.html`, `dark-proof-strip.html`
- Route-specific `screen-04-faq.html` (split FAQ + embedded contact CTA)
- Shared `v5-page01/landing-footer.html`, `callback-modal.html`, `scripts-v5-page01.html`

### Partial sets per route (`v5-ppc/<slug>/`)

| Slug | Partials count | `final-contact-cta.html` |
|------|---------------:|--------------------------|
| `zakaz` (index) | 7 active + 1 orphan | orphan — not included in page |
| `5-tonn` | 7 active + 1 orphan | orphan |
| `bytovki` | 7 active + 1 orphan | orphan |
| `konteynery` | 7 active + 1 orphan | orphan |
| `oborudovanie` | 7 active + 1 orphan | orphan |
| `fbs-zhbi` | 7 active + 1 orphan | orphan |
| `armatura` | 7 active + 1 orphan | orphan |
| `kirpich-bloki` | 7 active + 1 orphan | orphan |
| `stroymaterialy` | 7 active + 1 orphan | orphan |
| `vezdehod` | 7 active + 1 orphan | orphan |
| `yurlic` | 7 active + 1 orphan | orphan |
| `kray` | 7 active + 1 orphan | orphan |

Additional orphan partials (not wired to any page):

- `src/partials/sections/final-contact-cta.html`
- `src/partials/sections/v5-page01/final-contact-cta.html`

### Second-screen image assets (`src/img/v5/second-screen/`)

Assets present for: index-baseline, zakaz, 5-tonn, bytovki, konteynery, oborudovanie, fbs-zhbi, armatura, kirpich-bloki, stroymaterialy, vezdehod, yurlic, kray (+ test-01). Full route→image binding QA **not complete**.

---

## SECTION C — Route status table

Dist verification after `npm run build` (2026-05-29):

| Route | File exists | `#contacts`=1 | Split FAQ | Embedded CTA | No hero notice | No mock | No legacy send.php | Canonical markers | Status |
|-------|:-----------:|:-------------:|:---------:|:------------:|:--------------:|:-------:|:------------------:|:-----------------:|:------:|
| index | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **FROZEN** |
| 5-tonn | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **FROZEN** |
| bytovki | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **FROZEN** |
| konteynery | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **FROZEN** |
| oborudovanie | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **FROZEN** |
| fbs-zhbi | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **FROZEN** |
| armatura | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **FROZEN** |
| kirpich-bloki | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **FROZEN** |
| stroymaterialy | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **FROZEN** |
| vezdehod | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **FROZEN** |
| yurlic | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **FROZEN** |
| kray | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **FROZEN** |

Canonical markers: `hero__cargo-action`, `machine-showcase__spec-panel`, `machine-transport--ops-grid`, `pricing-factors--system`, `order-steps--process`.

---

## SECTION D — Known technical debt

Document only — **not fixed** in this freeze.

| Item | Detail |
|------|--------|
| Orphan `final-contact-cta` partials | 14 files under `src/partials/sections/` — none referenced by `src/pages/*.html`; active contact UX lives in `screen-04-faq.html` (`contact-cta--embedded`) |
| Image mapping incomplete | Second-screen JPGs exist per route; full visual binding and hero/section image QA not done |
| MAX placeholder links | Header, FAQ, footer, callback modal use `href="#contacts"` + `data-link-todo="max-url-required"` |
| Telegram placeholder links | Same pattern with `data-link-todo="telegram-url-required"`; some orphan partials use bare `https://t.me/` |
| Responsive QA pending | No mobile breakpoint HITL pass recorded |
| Production QA pending | No deploy-environment smoke test recorded |

---

## SECTION E — QA backlog

Priority order for post-freeze work:

1. **Mobile QA** — all 12 routes, key breakpoints, form submit UX, sticky header, FAQ accordion
2. **Desktop QA** — typography, grid overflow, section spacing parity vs index baseline
3. **Image mapping pass** — confirm each route uses correct second-screen / hero imagery
4. **Messenger URL wiring** — replace MAX/Telegram placeholders with production URLs
5. **Deploy QA** — build artifact upload, PHP mailer path, form POST on staging/production
6. **Orphan partial cleanup** — optional deprecation/removal of unused `final-contact-cta.html` files (separate charter)
7. **Production freeze** — final lock after QA sign-off

---

## SECTION F — Production readiness notes

| Area | State |
|------|-------|
| Build pipeline | `npm run build` PASS (~1.5s) |
| Mailer endpoint | `dist/backend/send-lead.php` present; legacy `dist/backend/api/forms/send.php` absent |
| Route markers | All 12 routes pass automated dist checks |
| Content lock | Accepted routes frozen; index locked |
| Browser QA | **Not done** — blocker for production freeze |
| Deploy | **SAFE UNKNOWN** — operator must confirm hosting path and ad URLs |
| SEO / indexing | All routes `noindex,nofollow` at freeze time |

**Next phase:** QA and stabilization (see [`V6-CALIBRATION-STATE.md`](V6-CALIBRATION-STATE.md), [`V6-PAGE-ROLLOUT-PLAN.md`](V6-PAGE-ROLLOUT-PLAN.md)).

---

## Related

- Snapshot manifest: `workspaces/_snapshots/snap-20260528-triumph-v6-route-family-freeze/SNAPSHOT-MANIFEST.md`
- Snapshot report: `workspaces/_snapshots/snap-20260528-triumph-v6-route-family-freeze/reports/v6-route-family-freeze-snapshot-report-v1.md`
- Rollout checklist: [`V6-ROUTE-ROLLOUT-CHECKLIST.md`](V6-ROUTE-ROLLOUT-CHECKLIST.md)
- Production baseline lock: [`V6-PRODUCTION-BASELINE-LOCK.md`](V6-PRODUCTION-BASELINE-LOCK.md)
