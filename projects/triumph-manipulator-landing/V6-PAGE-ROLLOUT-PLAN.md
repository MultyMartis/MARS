# Triumph V6 — page rollout plan

**Status:** preparation (2026-05-28). **Do not** batch-build all pages in one session.

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

## Remaining pages (11)

Aligned to ORCA [`landing-pages/INDEX.md`](../orca/ppc/triumph-manipulator/landing-pages/INDEX.md). **Homepage / master hot** may share zakaz baseline or need a dedicated route — confirm URL map before implementation.

| # | ORCA blueprint | Suggested slug / scaffold | Status |
|---|----------------|---------------------------|--------|
| 1 | `02-use-case-bytovka.md` | `v5-ppc/bytovki/` | Scaffold only — rollout pending |
| 2 | `03-use-case-stroymaterialy.md` | `v5-ppc/stroymaterialy/` | Scaffold only |
| 3 | `04-use-case-oborudovanie.md` | `v5-ppc/oborudovanie/` | Scaffold only |
| 4 | `05-capability-5-ton.md` | `v5-ppc/5-tonn/` | Scaffold only |
| 5 | `06-b2b-yurlica.md` | `v5-ppc/yurlic/` | Scaffold only |
| 6 | `07-capability-6x6-vezdekhod.md` | `v5-ppc/vezdehod/` | Scaffold only |
| 7 | `08-intercity-krai.md` | `v5-ppc/kray/` | Scaffold only |
| 8 | `09-use-case-fbs-zhb.md` | `v5-ppc/fbs-zhbi/` | Scaffold only |
| 9 | `10-use-case-konteynery.md` | `v5-ppc/konteynery/` | Scaffold only |
| 10 | `11-use-case-armatura.md` | `v5-ppc/armatura/` | Scaffold only |
| 11 | `12-use-case-kirpich-bloki.md` | `v5-ppc/kirpich-bloki/` | Scaffold only |

**Note:** `01-master-hot-general.md` (homepage) is **not** in the 11 above; treat as separate charter when homepage is in scope.

---

## Per-page pass (repeat for each page)

1. **Duplicate safely** — copy zakaz partial set or wire new `src/pages/<slug>.html` + `v5-ppc/<slug>/` from zakaz templates  
2. **ORCA content** — replace headings, body, FAQ, CTAs from handoff / blueprint (no unsupported claims)  
3. **Local layout adapt** — SCSS tweaks only where text length breaks grid; no global token/section redesign  
4. **Forms** — unique `data-form-id` per form; keep mailer endpoint `backend/send-lead.php`  
5. **Build** — `npm run build` in V6 workspace  
6. **QA** — per rules §G in [`TRIUMPH-V6-CURRENT-FRONTEND-RULES.md`](TRIUMPH-V6-CURRENT-FRONTEND-RULES.md)  
7. **REPORT** — files, build, viewport notes, SAFE UNKNOWN  

---

## Pilot gate

| Gate | Rule |
|------|------|
| **First pilot** | Complete **one** non-zakaz page end-to-end before starting a second |
| **Second pilot** | Complete **one more** page; compare drift vs zakaz markers |
| **Batch unlock** | Only after **2** pilots pass HITL — optional batch for remaining pages (still one REPORT per page recommended) |

---

## Explicitly out of scope (this plan)

- Creating all 11 HTML pages in one agent session  
- Visual redesign, new section types, or breakpoint regime change  
- Production deploy / DNS / ad URL verification (SAFE UNKNOWN until operator confirms)

---

## Related

- V6 workspace README: `workspaces/triumph-manipulator-landing-v6/README.md`  
- V5 snapshot: `workspaces/_snapshots/snap-20260528-triumph-v5-mailer-mvp-final-stable/`  
- Deprecated rules index: [`V6-RULES-DEPRECATION-INDEX.md`](V6-RULES-DEPRECATION-INDEX.md)
