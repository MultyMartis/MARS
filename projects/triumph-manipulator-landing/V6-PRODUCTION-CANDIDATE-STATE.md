# V6 Production Candidate State

**Project:** Triumph Manipulator Landing (V6)  
**Workspace:** `workspaces/triumph-manipulator-landing-v6`  
**Status:** **Production candidate** (filesystem freeze; not a git release tag)  
**Freeze date:** 2026-05-29  
**Snapshot (polish checkpoint):** `workspaces/_snapshots/snap-20260529-triumph-v6-production-candidate-polish-v1/`  
**Prior snapshot:** `workspaces/_snapshots/snap-20260529-triumph-v6-production-candidate-v1/`

---

## 1. Completed work (this baseline)

| Track | State |
|-------|--------|
| Route rollout | **Complete** — 12 accepted PPC routes |
| Image mapping | **Complete** — hero + second-screen per route family |
| Contacts | **Updated** — canonical phone and email |
| Messenger links | **Updated** — MAX, Telegram, WhatsApp |
| Footer navigation | **Updated** — `.landing-footer__nav` clean-scroll (no URL hash pollution) |
| Hero cleanup | **Complete** — no `.hero__notice` in built 12-route output |
| Typography | **Complete** — Open Sans normalization; legacy Montserrat/Roboto removed from stack |
| Hero polish | **Complete** — cargo readability (`1025–1510px`), proof label (`761px+`) micro-fix |
| Mailer | **Wired** — `backend/send-lead.php` via `form.js`; legacy `api/forms/send.php` excluded from build |

---

## 2. Accepted routes (12)

| Route | Page file |
|-------|-----------|
| `index` | `src/pages/index.html` |
| `5-tonn` | `src/pages/5-tonn.html` |
| `bytovki` | `src/pages/bytovki.html` |
| `konteynery` | `src/pages/konteynery.html` |
| `oborudovanie` | `src/pages/oborudovanie.html` |
| `fbs-zhbi` | `src/pages/fbs-zhbi.html` |
| `armatura` | `src/pages/armatura.html` |
| `kirpich-bloki` | `src/pages/kirpich-bloki.html` |
| `stroymaterialy` | `src/pages/stroymaterialy.html` |
| `vezdehod` | `src/pages/vezdehod.html` |
| `yurlic` | `src/pages/yurlic.html` |
| `kray` | `src/pages/kray.html` |

**Out of scope:** standalone `zakaz` page (content under `index`); legal pages.

---

## 3. Canonical contacts (built output)

| Channel | Value |
|---------|--------|
| Phone (display) | `+7 (918) 991-2-991` |
| Phone (tel) | `tel:+79189912991` |
| Email | `info@manipulator-triumph.ru` |
| MAX | `https://max.ru/u/f9LHodD0cOI8NplZUAfTNT7cDN89_7GhazWQy0u9B3AbC0ktxFkC6JWVPm0` |
| Telegram | `https://t.me/gruzotaxi_triumph` |
| WhatsApp | `https://wa.me/+79189912991` |

---

## 4. Production candidate status

- **Polish checkpoint:** `snap-20260529-triumph-v6-production-candidate-polish-v1` (source-only; `dist/` excluded).
- **Prior candidate freeze:** `snap-20260529-triumph-v6-production-candidate-v1` (if present on disk).
- **Build:** `npm run build` **PASS** at freeze time.
- **Not yet production release:** pending QA stages below; `noindex` policy may still apply per deploy charter.

---

## 5. Pending QA stages (ordered)

1. **Mobile QA** — layout, scroll, forms, modals, tap targets, first-screen crop.
2. **Desktop QA** — hero crop, second-screen column, proof strip, footer.
3. **Form / Lead QA** — all hero + modal forms; live mail spot-check beyond konteynery reference route.
4. **Production Deploy QA** — dist parity on host, backend path, asset paths, cache.
5. **Final production release** — human charter for index policy, tag, handoff.

See also: `V6-QA-STABILIZATION-PLAN.md`.

---

## 6. Rollback references

| Artifact | Role |
|----------|------|
| `snap-20260529-triumph-v6-production-candidate-v1` | **Primary** production-candidate rollback |
| `snap-20260529-triumph-v6-after-image-mapping-v1` | Prior post-mapping checkpoint |
| `snap-20260528-triumph-v5-mailer-mvp-final-stable` | V5 mailer baseline (not V6 route family) |
| Git `ebf4038` | Route family freeze commit |
| Git `dc05c479` | HEAD at production-candidate snapshot capture |

**Restore:** copy snapshot paths → workspace → `npm install` → `npm run build` → verification per `reports/v6-production-candidate-freeze-report-v1.md`.

---

## 7. Known source debts (non-blocking for candidate label)

- Orphan `final-contact-cta.html` partials under `v5-ppc/*/` — must remain **unincluded** in page builds.
- `v5-page01/screen-01-hero.html` still contains `.hero__notice` — **not** used by the 12-route build graph.
- `tools/generate-ppc-rollout.mjs` can reintroduce forbidden patterns if run without review.

---

## 8. References

- `V6-ROUTE-FAMILY-FREEZE.md`
- `V6-IMAGE-MAPPING-PASS.md`
- `V6-QA-STABILIZATION-PLAN.md`
- `workspaces/triumph-manipulator-landing-v6/reports/v6-production-candidate-freeze-report-v1.md`
