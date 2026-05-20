# Foundation Lite checklist (Wave 3)

**When:** Forge **Lite** or **Standard** slice touching `foundations/`, `js/core/`, or `data-module` / `data-section`.  
**QA routing (Wave 5):** [operational-qa-entry-v1.md](../../projects/mars-website-factory/operational-qa-entry-v1.md) — default session entry.  
**Not:** full Forge catalog; **not** governance expansion.

**Reference:** [website-factory-reference-v1](../../workspaces/website-factory-reference-v1/) · [foundation-systems/README.md](../../projects/mars-website-factory/foundation-systems/README.md).

Record failures as **`FOUNDATION FINDINGS`** in REPORT (max 5 bullets).

---

## Checks

- [ ] **Tokens:** section SCSS uses semantic tokens / variables — no stray `#hex` or raw `24px` for spacing rhythm without reason.
- [ ] **Z-index:** no literal `z-index: 999` (or similar) in section files — use `_layers.scss` tokens.
- [ ] **Overflow:** 375px spot check — no new horizontal scroll on touched page.
- [ ] **Lifecycle:** `data-module` nodes have single owner; `destroySection` (or equivalent) planned before partial swap; no duplicate submit/modal bind after re-init.
- [ ] **Replacement:** section root keeps `data-section` + `data-block-id`; global `foundations/*` change called out as Critical in REPORT.
- [ ] **Modal:** openers use `button[type=button]` + `data-modal-open`; ESC/body lock not broken by slice.
- [ ] **Form:** labels/`for`, error regions, submit lock during async — no color-only errors.

---

## Lite scope rule

If none of the above apply (copy-only, no hooks/foundations), **skip** this checklist — do not run for trivia.

*Wave 3 — Forge Lite foundation surface.*
