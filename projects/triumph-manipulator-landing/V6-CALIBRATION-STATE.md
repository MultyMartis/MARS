# V6 calibration state

## 1) Successful calibration routes

- `index`
- `5-tonn`
- `bytovki`
- `konteynery`
- `oborudovanie`
- `fbs-zhbi`
- `kirpich-bloki`

**Note:** `kirpich-bloki` accepted freeze (2026-05-29); snapshot `snap-20260528-triumph-v6-kirpich-bloki-accepted`.

## 2) What stabilized

- Canonical parity discipline between route structure and shared section contracts.
- CSS scope admission discipline for route-specific selectors in V6 PPC context.
- Split FAQ/contact architecture (`faq--split-cta` + embedded contact CTA).
- Route isolation (no cross-route scaffold reuse leakage in calibrated paths).
- No scaffold reuse policy respected for calibrated rollout routes.
- ORCA wording filtering kept within approved operational framing.
- Rollout QA gates enforced before freeze checkpoint.

## 3) Remaining high-risk areas

- Scoped selector admission remains sensitive to future route additions.
- Future route drift risk if copy/markup parity gates are bypassed.
- Image mapping remains deferred and can introduce perception drift.
- Browser visual QA remains human-in-the-loop mandatory.

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

## 5) Current rollout maturity assessment

- Maturity level: **stabilized calibration checkpoint**.
- Evidence basis: successful build, route marker parity on active set, and scoped CSS admission for target PPC bodies.
- Open constraints before next route:
  - keep normalized fixed-title checks active for `index`, `5-tonn`, `oborudovanie`, and new routes;
  - keep legacy endpoint exclusion (`backend/api/forms/send.php`) in build pipeline and verify authority of `backend/send-lead.php` during rollout QA;
  - run icon subset QA gate (`screen-icons.css` membership) before choosing route icons;
  - perform full browser visual QA pass as mandatory HITL gate.
