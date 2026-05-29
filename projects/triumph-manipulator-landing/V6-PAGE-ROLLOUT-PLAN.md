# Triumph V6 — page rollout plan

**Status:** ROUTE ROLLOUT PHASE **COMPLETE** (2026-05-29). Route family frozen — QA phase next.
**Safety lock:** canonical V6 baseline is frozen for rollout work per [`V6-PRODUCTION-BASELINE-LOCK.md`](V6-PRODUCTION-BASELINE-LOCK.md) unless explicit user override.
**Freeze reference:** [`V6-ROUTE-FAMILY-FREEZE.md`](V6-ROUTE-FAMILY-FREEZE.md)

## Base page

| Item | Value |
|------|--------|
| **Workspace** | `workspaces/triumph-manipulator-landing-v6/` |
| **Canonical HTML** | `src/pages/index.html` |
| **Intent** | PPC «Заказать манипулятор» (`ppc-zakaz-manip`) |
| **Partials** | `src/partials/sections/v5-ppc/zakaz/*` + shared `v5-page01/*` |
| **Rules** | [`TRIUMPH-V6-CURRENT-FRONTEND-RULES.md`](TRIUMPH-V6-CURRENT-FRONTEND-RULES.md) |

This page is **production-stable** (mailer MVP). All rollout pages copy its **structure and component markers**, then swap ORCA copy.

---

## Route rollout phase — COMPLETE

All 11 non-index rollout pages plus index baseline are **accepted and frozen**.

| # | ORCA blueprint | Slug / scaffold | Status |
|---|----------------|-------------------|--------|
| — | `01-master-hot-general.md` (index / zakaz) | `v5-ppc/zakaz/` | **FROZEN** |
| 1 | `02-use-case-bytovka.md` | `v5-ppc/bytovki/` | **FROZEN** |
| 2 | `03-use-case-stroymaterialy.md` | `v5-ppc/stroymaterialy/` | **FROZEN** |
| 3 | `04-use-case-oborudovanie.md` | `v5-ppc/oborudovanie/` | **FROZEN** |
| 4 | `05-capability-5-ton.md` | `v5-ppc/5-tonn/` | **FROZEN** |
| 5 | `06-b2b-yurlica.md` | `v5-ppc/yurlic/` | **FROZEN** |
| 6 | `07-capability-6x6-vezdekhod.md` | `v5-ppc/vezdehod/` | **FROZEN** |
| 7 | `08-intercity-krai.md` | `v5-ppc/kray/` | **FROZEN** |
| 8 | `09-use-case-fbs-zhb.md` | `v5-ppc/fbs-zhbi/` | **FROZEN** |
| 9 | `10-use-case-konteynery.md` | `v5-ppc/konteynery/` | **FROZEN** |
| 10 | `11-use-case-armatura.md` | `v5-ppc/armatura/` | **FROZEN** |
| 11 | `12-use-case-kirpich-bloki.md` | `v5-ppc/kirpich-bloki/` | **FROZEN** |

**Route creation phase:** CLOSED. No new routes without explicit charter.

---

## Remaining work (post-rollout / QA phase)

| Task | Status |
|------|--------|
| Image mapping pass | Pending |
| Mobile QA | Pending |
| Desktop QA | Pending |
| Deploy QA | Pending |
| Production freeze | Pending — after QA backlog |

---

## Per-page pass (repeat for each page)

1. **Duplicate safely** — copy zakaz partial set or wire new `src/pages/<slug>.html` + `v5-ppc/<slug>/` from zakaz templates  
2. **ORCA content** — replace headings, body, FAQ, CTAs from handoff / blueprint (no unsupported claims)  
3. **Local layout adapt** — SCSS tweaks only where text length breaks grid; no global token/section redesign  
4. **Forms** — unique `data-form-id` per form; keep mailer endpoint `backend/send-lead.php`  
5. **Build** — `npm run build` in V6 workspace  
6. **QA** — per rules §G in [`TRIUMPH-V6-CURRENT-FRONTEND-RULES.md`](TRIUMPH-V6-CURRENT-FRONTEND-RULES.md)  
7. **REPORT** — files, build, viewport notes, SAFE UNKNOWN  

*Steps 1–6 complete for all routes. Step 7 (full HITL QA REPORT) remains for QA phase.*

---

## Pilot gate

| Gate | Rule | Result |
|------|------|--------|
| **First pilot** | Complete **one** non-zakaz page end-to-end before starting a second | **PASS** (`5-tonn`, `bytovki`) |
| **Second pilot** | Complete **one more** page; compare drift vs zakaz markers | **PASS** |
| **Batch unlock** | Only after **2** pilots pass HITL | **PASS** — full family complete |
| **Route family freeze** | All 12 routes dist-verified + snapshot | **PASS** (2026-05-29) |

---

## 5-tonn calibration lessons (mandatory for next pages)

- 5-tonn exposed a repeatable failure mode: HTML parity can pass while CSS scope parity is still broken.
- Next pages must pass `V6-ROUTE-ROLLOUT-CHECKLIST.md` before rollout is considered complete.
- Existing target-route scaffold partials must not be reused as adaptation base.
- Route rollout starts by copying canonical `v5-ppc/zakaz/` partials, then adapting content.
- CSS scope admission is mandatory for every new route when canonical styles are route-scoped.
- First two routes remain calibration gates before batch rhythm resumes.

## Rollout maturity note (post-bytovki)

- Current calibration maturity improved after bytovki:
  - lower regression count
  - successful CSS scope admission discipline
  - canonical parity discipline holding
  - fewer post-build structural corrections
- Route family freeze (2026-05-29) confirms full-family marker parity and mailer hygiene.

---

## Explicitly out of scope (this plan)

- Creating new route pages (route creation phase closed)  
- Visual redesign, new section types, or breakpoint regime change  
- Production deploy / DNS / ad URL verification (SAFE UNKNOWN until operator confirms)

---

## Related

- Route family freeze: [`V6-ROUTE-FAMILY-FREEZE.md`](V6-ROUTE-FAMILY-FREEZE.md)
- Calibration state: [`V6-CALIBRATION-STATE.md`](V6-CALIBRATION-STATE.md)
- V6 workspace README: `workspaces/triumph-manipulator-landing-v6/README.md`  
- V5 snapshot: `workspaces/_snapshots/snap-20260528-triumph-v5-mailer-mvp-final-stable/`  
- V6 route family snapshot: `workspaces/_snapshots/snap-20260528-triumph-v6-route-family-freeze/`  
- Deprecated rules index: [`V6-RULES-DEPRECATION-INDEX.md`](V6-RULES-DEPRECATION-INDEX.md)
