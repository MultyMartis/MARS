# V2 Cleanup Decision Log

Decision log for **Triumph Manipulator Landing V2** source-of-truth stabilization after audit (lane A — validation / Forge methodology).  
**Date of this pass:** 2026-05-16. **Validation workflow reset (semantic hardening):** same date — implementation proceeded **screen-by-screen** from `design/v2/01.png` per [V2-FRONTEND-SOURCE-OF-TRUTH.md](./V2-FRONTEND-SOURCE-OF-TRUTH.md) **NEXT IMPLEMENTATION RULE**. **Physical implementation reset completed:** homepage Screens 01–07 in `workspaces/triumph-manipulator-landing-v2/src/partials/sections/` and matching SCSS files were reset before clean rebuild. **Freeze update 2026-05-17:** clean rebuild completed; current status is **READY FOR FREEZE WITH MINOR KNOWN DRIFT**. See [V2-FREEZE-STATE.md](./V2-FREEZE-STATE.md).

---

## 1. Purpose

Record what was **removed**, what remains **canonical**, what is **forbidden**, what in the validation workspace shows **semantic drift**, and what is a **quarantine candidate** pending human approval. **No** bulk deletion of workspace sources was performed except the single PDF named below.

---

## 2. Confirmed deleted files

| Path | Action | Reason |
|------|--------|--------|
| `projects/triumph-manipulator-landing/design/TRIUMPH LANDING V2 — DESIGN & FRONTEND RULES.pdf` | **Deleted** | No longer trusted as canonical; risk of mixed semantics, legacy mockup influence, and implementation blending. **Not** recreated in this task; a new PDF may be generated later from the MD stack. |

---

## 3. Canonical sources

| Classification | Path / artifact | Notes |
|----------------|-----------------|-------|
| **Canonical V2 visual** | `projects/triumph-manipulator-landing/design/v2/` | `01.png` … `07.png`, `full.png` — **only** trusted visual implementation reference for V2. |
| **Design folder architecture** | `projects/triumph-manipulator-landing/design/README.md` | Maps `v1/`, `v2/`, `shared-assets/`; complements written isolation rules in `V2-FRONTEND-SOURCE-OF-TRUTH.md` §4. |
| **Canonical written discipline** | `projects/triumph-manipulator-landing/V2-FRONTEND-SOURCE-OF-TRUTH.md` | Classification of sources; process for conflicts. |
| **Canonical section map** | `projects/triumph-manipulator-landing/V2-SECTION-SOURCE-MATRIX.md` | `index.html` includes vs `style.scss` vs section intent. |
| **Canonical visual-to-DOM map** | `projects/triumph-manipulator-landing/V2-VISUAL-SOURCE-MATRIX.md` | `design/v2` screens vs partials; documents known conflicts. |
| **Forge / production rules** | `projects/triumph-manipulator-landing/docs/TRIUMPH-FORGE-V2-FRONTEND-PRODUCTION-RULES.md` | Normative frontend production rules for Forge lane. |
| **Design system (written)** | `projects/triumph-manipulator-landing/design-system/triumph-manipulator-design-system.md` | Tokens / system reference (not a substitute for `design/v2/` layout). |
| **Workspace state map** | `projects/triumph-manipulator-landing/V2-CANONICAL-STATE.md` | Where folders live; implementation edit target. |
| **Active implementation (what is built)** | `workspaces/triumph-manipulator-landing-v2/src/` | Validation/test workspace for AI Frontend Agent / MARS Forge — **not** v1 production delivery. |

**Forge overlay pack (methodology, not project-specific deliverables):** `agents/mars-forge/` (`AGENT.md`, `workflow.md`, `qa-checklist.md`, `README.md`).

**Design version isolation:** normative rules are in [V2-FRONTEND-SOURCE-OF-TRUTH.md](./V2-FRONTEND-SOURCE-OF-TRUTH.md) §4 and [`design/README.md`](./design/README.md).

---

## 4. Forbidden sources (for V2 implementation)

| Path / artifact | Status |
|-----------------|--------|
| `projects/triumph-manipulator-landing/design/v1/` | **FORBIDDEN** as implementation / copy truth for V2 unless **explicitly re-approved** in writing. Archive / historical mockup PNGs only (successor to deprecated `design/mockups/` naming). |
| Deleted V2 rules PDF (see §2) | **Do not** cite or restore as authority. |
| Old V1 **landing-strip** naming and maps when they describe **V1** order | **Not** homepage section order truth for V2. |

---

## 5. Active validation workspace status

| Item | Status |
|------|--------|
| Repository role | `workspaces/triumph-manipulator-landing-v2/` is a **validation / test** workspace for the Forge methodology; **v1** remains the real advertising/production line per operator. |
| Homepage | `src/pages/index.html` includes (in `<main>`, order aligned with **`01.png`→`06.png`**): `hero-conversion` → `machine-specs-transport-lists` → `trust-cases-social-proof` → `segments-applications-grid` → `problem-solution-matrix` → `consultation-lead-form`; after `</main>`: `site-footer-v2` (**`07.png`**). **Clean rebuild completed:** homepage `01` through `07` flow restored and final rendered QA completed. Current status: **READY FOR FREEZE WITH MINOR KNOWN DRIFT**. **`equipment-prices`** is **not** on the homepage — see `validation-equipment-prices.html` ([equipment-prices-quarantine.md](./design/v2/validation/equipment-prices-quarantine.md)). |
| Secondary pages | `service.html`, `about.html` use **starter demo** wiring (`page-intro`, `advantages`, `contacts`, `layout/footer.html`, English titles). They are **not** V2 design-v2 homepage validation targets; they explain `_page-intro` / `_advantages` / `_contacts` in `style.scss`. |
| Nested includes | Components pulled by active partials (e.g. `partials/components/icon.html`, `brand-lockup-inner.html`, `modal` on demo pages) are **ACTIVE** only where reachable from the above; not exhaustively matrix-audited in this log. |

---

## 6. Quarantine candidates (do **not** delete without approval)

| Candidate | Location | Why quarantine / hold |
|-----------|----------|------------------------|
| **`equipment-prices` block (markup + SCSS)** | `partials/sections/equipment-prices.html`, `_equipment-prices.scss` | **EXPERIMENTAL / VALIDATION quarantine** — **removed from homepage** (operator-approved **2026-05-16**). Rendered only via **`src/pages/validation-equipment-prices.html`**. No matching `design/v2` slice between machine and cases; fleet semantics **must not** return to `index.html` without a **new** gate. See [equipment-prices-quarantine.md](./design/v2/validation/equipment-prices-quarantine.md). |
| **Legacy strip partials + SCSS** | `landing-strip-01.html` … `04.html`, `_landing-strip-01.scss` … `_landing-strip-04.scss` | Not in `index.html`. **V1-era naming**; risk of accidental reuse as V2 truth. |
| **Alternate hero / FAQ / trust variants** | `hero.html`, `_hero.scss`; `faq-cta-footer.html`, `_faq-cta-footer.scss`; `trust-reviews.html`, `_trust-reviews.scss` | Not in homepage chain; possible **mockup / fleet / alternate composition** residue. |
| **Starter-template `AGENTS.md` framing** | `workspaces/triumph-manipulator-landing-v2/AGENTS.md` | Declares repo as **canonical gulp-starter template**; conflicts with **actual use** as Triumph V2 validation workspace. **Quarantine as documentation drift** — update scope wording when operator aligns. |
| **`service.html` / `about.html`** | `src/pages/` | Generic English **Gulp starter** content; **not** aligned with Triumph RU V2 brief. Quarantine as **non-canonical** for product validation until explicitly scoped. |

---

## 7. Semantic contamination findings (workspace)

Evidence is **documentation + static review** of `src/` and matrices; **no** pixel diffing of PNGs in this task.

| Finding | Detail |
|---------|--------|
| **Third screen / third `<main>` (homepage)** | **Resolved (2026-05-16):** **Third PNG** (`03.png`) = cases; **third `<main>`** = `trust-cases-social-proof`. Former collision with `equipment-prices` removed from homepage. |
| **Homepage implementation fill** | **Resolved 2026-05-17:** `hero-conversion`, `machine-specs-transport-lists`, `trust-cases-social-proof`, `segments-applications-grid`, `problem-solution-matrix`, `consultation-lead-form`, and `site-footer-v2` completed clean rebuild from Screens `01` through `07`; final rendered QA completed. Current status: **READY FOR FREEZE WITH MINOR KNOWN DRIFT**. |
| **`problem-solution-matrix` structure** | Historical pre-freeze risk retained for traceability. Current freeze status and accepted known drift are governed by [V2-FREEZE-STATE.md](./V2-FREEZE-STATE.md); exact pixel parity is not claimed. |
| **Legacy strip naming** | Presence of `landing-strip-*` files **near** active V2 partials increases risk of **wrong include** or copy-paste from V1 maps. |
| **Historical mockup tree on disk** | Canonical archive path is **`design/v1/`** (see [`design/README.md`](./design/README.md)). If a stray **`design/mockups/`** directory still appears in some working copies, treat it as a **stale duplicate** of the V1 archive — **not** a V2 source (§4). |
| **Header Telegram placeholder** | `href="https://t.me/"` without channel — may be incomplete vs brand; **SAFE UNKNOWN** vs final brief. |

### 7.1 Freeze-state decisions (2026-05-17)

- `equipment-prices` quarantine remains active; it must not return to the homepage without a new written gate.
- Homepage `01` through `07` flow is restored.
- Clean rebuild completed for the current V2 homepage.
- Final rendered QA completed.
- Current status is **READY FOR FREEZE WITH MINOR KNOWN DRIFT**.
- Known drift and next production phases are recorded in [V2-FREEZE-STATE.md](./V2-FREEZE-STATE.md).

### 7.2 Orphan SCSS (not imported in `style.scss`)

Per [V2-SECTION-SOURCE-MATRIX.md](./V2-SECTION-SOURCE-MATRIX.md) §5.2 — still accurate:

- `_landing-strip-01.scss` … `_landing-strip-04.scss`
- `_faq-cta-footer.scss`
- `_hero.scss`
- `_trust-reviews.scss`

### 7.3 Orphan section partials (not in `index.html`)

Per matrix §5.1 — still accurate: `landing-strip-01.html` … `04`, `faq-cta-footer.html`, `hero.html`, `page-intro.html`, `advantages.html`, `contacts.html`, `trust-reviews.html`.

**Note:** `page-intro`, `advantages`, `contacts` partials **are** used on `service.html` / `about.html`, so they are **not** orphans for the whole workspace — only for the **homepage**.

### 7.4 `index.html` includes vs canonical matrix

Homepage **`index.html`** matches [V2-SECTION-SOURCE-MATRIX.md](./V2-SECTION-SOURCE-MATRIX.md) §4.1 for **six** `<main>` sections + footer + layout includes. **`equipment-prices`** is **excluded** from the homepage chain and documented as **validation-only** (`validation-equipment-prices.html`).

---

## 8. Files to preserve (audit / validation / Forge)

| Path | Role |
|------|------|
| `V2-FRONTEND-SOURCE-OF-TRUTH.md` | Updated: PDF retired; V1 archive (`design/v1/`) explicitly forbidden for V2 implementation; design version isolation §4. |
| `V2-SECTION-SOURCE-MATRIX.md` | Updated: PDF references removed from process; row 5 risk points to visual matrix. |
| `V2-VISUAL-SOURCE-MATRIX.md` | Updated: PDF retirement note; document control clarifies non-canonical PDF. |
| `V2-CANONICAL-STATE.md` | Updated: homepage partial list **without** homepage `equipment-prices`; validation page documented. |
| `docs/TRIUMPH-FORGE-V2-FRONTEND-PRODUCTION-RULES.md` | Preserved — Forge production rules. |
| `agents/mars-forge/*` | Preserved — methodology overlay. |

**Note:** A separate file named `*FRONTEND*SOURCE*AUDIT*` was **not** found under `projects/triumph-manipulator-landing/`; audit findings live in the V2 matrix / source-of-truth docs above.

---

## 9. Recommended next cleanup actions (human-gated)

1. **`equipment-prices`:** homepage removal + validation page — **done** (2026-05-16); any **return** to `index.html` needs a **new** gate.
2. **Triage legacy partials/SCSS** — move to `_legacy/` folder **only after approval**, or delete in a scoped PR; until then, keep quarantine labels in docs.
3. **Reconcile `AGENTS.md`** with «validation workspace» reality so agents do not assume pure starter template.
4. **Optional:** regenerate a **new** rules PDF **from** MD sources after text is frozen (out of scope here).
5. **Optional:** add dedicated `*AUDIT*.md` if the operator wants a single named audit file (currently absent).

---

## 10. SAFE UNKNOWN

| Item | Reason |
|------|--------|
| Pixel-exact copy match | No line-by-line OCR or pixel diff was run in this task between `design/v2/*.png` and live HTML. |
| Every bullet in `hero-conversion` vs `01.png` | Documented possible drift in [V2-VISUAL-SOURCE-MATRIX.md](./V2-VISUAL-SOURCE-MATRIX.md); not re-verified here. |
| Human-chosen fate for **`equipment-prices`** (which of the four approved options) | **Resolved 2026-05-16:** **(a)** removed from homepage + **(b)** isolated on **`validation-equipment-prices.html`** (validation / experimental). **(c)/(d)** rewrite or expanded experimental scope remain **future options** with new written approval. |
| Whether `t.me/` and other social URLs are final | Placeholder or incomplete links — not validated. |
| Full component-level matrix | Nested `@@include` inside sections not exhaustively listed in this log. |
| Whether **other** handoff files (e.g. `V2-HANDOFF.md`, `frontend-workspace.md`, `README.md` under `projects/triumph-manipulator-landing/`) still mention the retired PDF | **Spot-check** — `workspaces/triumph-manipulator-landing-v2/README.md` was updated in this pass; other docs may remain stale. |

---

## Document control

- **Companion:** [V2-FRONTEND-SOURCE-OF-TRUTH.md](./V2-FRONTEND-SOURCE-OF-TRUTH.md)  
- **No** commit, push, or `git add` performed as part of this task by agent instruction.
