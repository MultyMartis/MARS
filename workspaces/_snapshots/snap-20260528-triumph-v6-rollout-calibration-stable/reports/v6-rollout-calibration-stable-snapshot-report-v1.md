# V6 rollout calibration stable snapshot report v1

## Scope

- Snapshot path: `workspaces/_snapshots/snap-20260528-triumph-v6-rollout-calibration-stable/`
- Freeze type: operational checkpoint (no redesign, no refactor)
- Calibration routes: `5-tonn`, `bytovki`, `konteynery`

## Route verification (`dist/*.html`)

- Verified pages: `index.html`, `5-tonn.html`, `bytovki.html`, `konteynery.html`
- `id="contacts"`: exactly one on each verified route
- `faq--split-cta`: present on each verified route
- `contact-cta--embedded`: present on each verified route
- Standalone `final-contact-cta`: not found on verified routes
- `.hero__notice`: not found on verified routes
- `data-form-handler="mock"`: not found on verified routes
- Canonical markers present on each verified route:
  - `hero__cargo-action`
  - `machine-showcase__spec-panel`
  - `machine-transport--ops-grid`
  - `pricing-factors--system`
  - `order-steps--process`
- Fixed titles:
  - `Частые вопросы` present on each verified route
  - `Что не перевозим` present on `bytovki`, `konteynery`; missing exact match on `index`, `5-tonn`

## CSS admission verification (`dist/assets/css/style.css`)

- Scope admission present for all target pages:
  - `ppc-zakaz-manip`
  - `ppc-5-tonn`
  - `ppc-bytovki`
  - `ppc-konteynery`
- Required selectors confirmed in scoped CSS:
  - `machine-transport--ops-grid`
  - `machine-showcase__spec-panel`
- V6 shared layout selectors present:
  - `hero__cargo-action`
  - `pricing-factors--system`
  - `order-steps--process`
  - `faq--split-cta`
  - `contact-cta--embedded`
- Breakpoint note:
  - `981px`: not found
  - `980px`: present in compiled CSS (requires baseline comparison to classify as new vs legacy)
- No broad new global pollution detected in this checkpoint pass (manual baseline diff still advised before next rollout lane).

## Backend endpoint check

- `backend/api/forms/send.php`: present in workspace and copied to `dist/backend/api/forms/send.php`
- Status: does not satisfy strict "no send.php" validation item; carry as explicit regression risk for next gate.

## Build verification

- Command: `npm run build`
- Result: PASS
- Dist outputs confirmed:
  - `dist/index.html`
  - `dist/5-tonn.html`
  - `dist/bytovki.html`
  - `dist/konteynery.html`
