# V6 calibration state

**Last updated:** 2026-05-29 — route family freeze

## Phase status

| Phase | Status |
|-------|--------|
| Route family | **COMPLETED** — all 12 routes accepted and frozen |
| Rollout phase | **COMPLETED** — see [`V6-ROUTE-FAMILY-FREEZE.md`](V6-ROUTE-FAMILY-FREEZE.md) |
| Route creation phase | **CLOSED** — no new routes without explicit charter |
| Next phase | **QA and stabilization** (mobile/desktop QA, image mapping, deploy QA, production freeze) |

---

## 1) Successful calibration routes

- `index`
- `5-tonn`
- `bytovki`
- `konteynery`
- `oborudovanie`
- `fbs-zhbi`
- `armatura`
- `kirpich-bloki`
- `stroymaterialy`
- `vezdehod`
- `yurlic`
- `kray`

**Note:** Route family freeze (2026-05-29); snapshot `snap-20260528-triumph-v6-route-family-freeze`.

---

## 2) What stabilized

- Canonical parity discipline between route structure and shared section contracts.
- CSS scope admission discipline for route-specific selectors in V6 PPC context.
- Split FAQ/contact architecture (`faq--split-cta` + embedded contact CTA).
- Route isolation (no cross-route scaffold reuse leakage in calibrated paths).
- No scaffold reuse policy respected for calibrated rollout routes.
- ORCA wording filtering kept within approved operational framing.
- Rollout QA gates enforced before freeze checkpoint.
- Full route family (12 pages) builds clean with unified marker contract.

---

## 3) Remaining high-risk areas

- Scoped selector admission remains sensitive to future route additions (route creation now closed).
- Image mapping remains deferred and can introduce perception drift.
- Browser visual QA remains human-in-the-loop mandatory — **not yet performed post-final-wave**.
- MAX/Telegram messenger URLs still placeholder — production wiring pending.
- Orphan `final-contact-cta.html` partials create maintenance confusion if accidentally re-wired.

---

## 4) Operational lessons learned

- Wrong-workspace incident during `oborudovanie` rollout was caught before freeze; work was recovered in V6 and V5 was restored clean for this scope.
- Font Awesome icon subset discipline: semantically correct classes may be missing from `screen-icons.css`; verify subset membership before choosing route icons (discovered during `oborudovanie` icon correction).
- Future route pages must confirm every `fas fa-*` class exists in `src/assets/vendor/fontawesome/css/screen-icons.css` before rollout freeze.
- Copy-first rollout reduces structural noise in route adaptation.
- Structure-first adaptation is required before cosmetic polishing.
- STOP-gates prevented unsafe continuation under partial parity.
- HTML parity alone is insufficient without CSS scope parity.
- Fixed-title QA must normalize entity variants (` ` and `&nbsp;`) before exact comparison; `Что не перевозим` and `Что не&nbsp;перевозим` are parity-equivalent forms.
- Legacy endpoint hygiene should be enforced at build-copy level: keep `backend/send-lead.php` authoritative and exclude `backend/api/forms/send.php` from `dist` to prevent false-positive route checks.
- Final-wave routes (`armatura`, `stroymaterialy`, `vezdehod`, `yurlic`, `kray`) completed without reopening index or earlier accepted routes.

---

## 5) Current rollout maturity assessment

- Maturity level: **route family frozen — QA phase entry**.
- Evidence basis: successful build on all 12 routes, dist marker parity, mailer endpoint hygiene, snapshot `snap-20260528-triumph-v6-route-family-freeze`.
- Open constraints before production freeze:
  - complete mobile and desktop HITL visual QA on all 12 routes;
  - complete image mapping pass;
  - wire MAX/Telegram production URLs;
  - run deploy QA on target hosting;
  - keep legacy endpoint exclusion (`backend/api/forms/send.php`) in build pipeline;
  - perform production freeze only after QA backlog cleared (see `V6-ROUTE-FAMILY-FREEZE.md` Section E).
