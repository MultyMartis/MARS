# V6 QA & Stabilization Plan

**Project:** Triumph Manipulator Landing (V6)  
**Workspace:** `workspaces/triumph-manipulator-landing-v6`  
**Branch:** `mars/post-cycle8-live-tests`  
**Freeze commit:** `ebf4038` — freeze triumph v6 route family  
**Phase start:** 2026-05-29

---

## 1. Current status

| Item | State |
|------|--------|
| Route rollout | **Complete** — 12 accepted PPC routes built and frozen |
| Route family freeze | **Committed** (`ebf4038`) and pushed to `origin/mars/post-cycle8-live-tests` |
| Active work | **QA / Stabilization** — no new routes, no redesign, no route content edits in this phase unless explicitly chartered |
| Next deliverable | **Image Mapping Pass** (inventory + planned swaps; markup changes in a follow-up pass only) |

---

## 2. QA stages (ordered)

1. **Image Mapping Pass** — per-route hero + second-screen semantic alignment; alt text review; use dedicated assets where inventory exists (`V6-IMAGE-MAPPING-PASS.md`).
2. **Mobile QA** — visual, scroll, forms, modals, tap targets, first-screen crop.
3. **Desktop QA** — layout, hero crop, second-screen portrait column, proof strip, footer.
4. **Form / Lead QA** — all hero + modal forms → `send-lead.php`; consent, validation, success/error UX; live mail spot-check per route class.
5. **Production Deploy QA** — dist parity, backend path, asset paths, `noindex` policy until release charter.
6. **Final Production Freeze** — tag baseline, lock admission map, handoff report.

---

## 3. Accepted routes (12)

| Route slug | Page file | Notes |
|------------|-----------|--------|
| `index` | `src/pages/index.html` | Uses `zakaz` partial prefix internally |
| `5-tonn` | `src/pages/5-tonn.html` | |
| `bytovki` | `src/pages/bytovki.html` | |
| `konteynery` | `src/pages/konteynery.html` | Live mail test confirmed on hero form (reference route) |
| `oborudovanie` | `src/pages/oborudovanie.html` | |
| `fbs-zhbi` | `src/pages/fbs-zhbi.html` | |
| `armatura` | `src/pages/armatura.html` | |
| `kirpich-bloki` | `src/pages/kirpich-bloki.html` | |
| `stroymaterialy` | `src/pages/stroymaterialy.html` | |
| `vezdehod` | `src/pages/vezdehod.html` | |
| `yurlic` | `src/pages/yurlic.html` | |
| `kray` | `src/pages/kray.html` | |

**Out of scope for this family:** `zakaz` as standalone page (content lives under `index`); legal pages; orphan `final-contact-cta` partials.

---

## 4. Known debts (carry into QA)

- **Route-specific images** — many routes share `hero-bg-final.jpg` and `second-screen-index-baseline.jpg`; dedicated `src/img/v5/second-screen/second-screen-<route>.jpg` files exist but are not wired on all routes.
- **Hero alt text** — all 12 pages use `alt=""` on decorative first-screen background (`aria-hidden` on wrapper); semantic alt may be needed if policy changes.
- **Mobile visual QA** — not yet executed systematically.
- **Desktop visual QA** — not yet executed systematically.
- **MAX / Telegram** — social placeholders; not production-final.
- **Live mail** — only **konteynery** hero form live test confirmed; other routes need spot-check before production freeze.
- **Orphan partials** — route-level `final-contact-cta.html` files under `v5-ppc/*/` must **remain unconnected** (single contacts anchor via shared footer flow).

---

## 5. Constraints (this phase)

- Do **not** create new routes.
- Do **not** redesign layout or copy.
- Do **not** edit route content except image `src` / `alt` in a dedicated mapping pass after inventory sign-off.
- Do **not** hand-edit `dist/`.
- Regenerate via `npm run build` only.

---

## 6. References

- `V6-ROUTE-FAMILY-FREEZE.md`
- `V6-IMAGE-MAPPING-PASS.md`
- `V6-CSS-SCOPE-ADMISSION-MAP.md`
- `TRIUMPH-V6-CURRENT-FRONTEND-RULES.md`
