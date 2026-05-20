# Triumph Manipulator Landing V2 — Frontend workspace state

## 1. What this note is

A short map of **where the V2 landing files live** in this repo: the normal Gulp workspace folder, project-side design references, build output, and the local Font Awesome checkout. **Not** a MARS subsystem, **not** governance, **not** automation or a “platform”.

## 2. Folders

| Path | Role |
|------|------|
| **`workspaces/triumph-manipulator-landing-v2/`** | **Current** Triumph layout — HTML/SCSS/JS under `src/`. Regular frontend workspace; not a separate architectural layer inside MARS. |
| **`workspaces/triumph-manipulator-landing/`** | **Older / frozen** reference (tag **`triumph-manipulator-v1`** @ `309d81a`). Do not use for new V2 edits. |

## 2.1 NEXT IMPLEMENTATION RULE (validation cycle)

**Normative:** [V2-FRONTEND-SOURCE-OF-TRUTH.md](./V2-FRONTEND-SOURCE-OF-TRUTH.md) — **NEXT IMPLEMENTATION RULE**.

- **Freeze state (2026-05-17):** the current rebuilt homepage Screens `01` through `07` are **READY FOR FREEZE WITH MINOR KNOWN DRIFT**. See [V2-FREEZE-STATE.md](./V2-FREEZE-STATE.md).
- The clean rebuild cycle has completed for `projects/triumph-manipulator-landing/design/v2/01.png`, then `02.png` … `07.png`; future implementation work should be opened as a separate production phase, not as continued polish inside this freeze.
- Do **not** use `design/v1/` as semantic source for V2; do **not** invent copy or change section meaning without operator approval.
- **`equipment-prices`:** **not** on the V2 homepage `index.html`. Isolated on **`validation-equipment-prices.html`** (**EXPERIMENTAL / VALIDATION**) — see [design/v2/validation/equipment-prices-quarantine.md](./design/v2/validation/equipment-prices-quarantine.md) and [V2-CLEANUP-DECISION-LOG.md](./V2-CLEANUP-DECISION-LOG.md).

## 3. Design references

| Path | Role |
|------|------|
| **`projects/triumph-manipulator-landing/design/`** | V2 **visual** exports under `design/v2/`; archived V1 slices under `design/v1/` are **not** V2 implementation sources. Folder roles: [`design/README.md`](./design/README.md); cleanup context: [V2-CLEANUP-DECISION-LOG.md](./V2-CLEANUP-DECISION-LOG.md). **Design version isolation:** [V2-FRONTEND-SOURCE-OF-TRUTH.md](./V2-FRONTEND-SOURCE-OF-TRUTH.md) §4. |
| **`projects/triumph-manipulator-landing/design-system/triumph-manipulator-design-system.md`** | Written design system (linked from the V2 workspace README). |

## 4. Where to edit implementation

| Path | Role |
|------|------|
| **`workspaces/triumph-manipulator-landing-v2/src/`** | **Source** — pages, partials, SCSS, JS, images, SVG inputs, favicon. **Edit here**, not in **`dist/`**. |

**Homepage partials (from `workspaces/triumph-manipulator-landing-v2/src/pages/index.html`):** `hero-conversion`, `machine-specs-transport-lists`, `trust-cases-social-proof`, `segments-applications-grid`, `problem-solution-matrix`, `consultation-lead-form`, then `site-footer-v2` — canonical flow **`01.png`→`07.png`** via **`design/v2/`** (footer = `07`). **`equipment-prices`** is **not** in this chain; it exists only on **`validation-equipment-prices.html`**. **Next work:** separate production phases only; do not treat freeze handoff as continued rebuild polish.

**Freeze summary:** current rebuilt landing is frozen for handoff as **READY FOR FREEZE WITH MINOR KNOWN DRIFT** after physical implementation reset, clean rebuild cycle, Font Awesome delivery / governance fixes, typography rhythm pass, CTA / form rhythm pass, vertical cadence pass, and final rendered visual QA. Known drift and future production phases are recorded in [V2-FREEZE-STATE.md](./V2-FREEZE-STATE.md).

## 5. Build output

| Path | Role |
|------|------|
| **`workspaces/triumph-manipulator-landing-v2/dist/`** | **Generated** by `npm run build` / Gulp. Not a hand-editing target. At the **repo root** this tree is **not** on the V2 allow-list — keep it **out** of normal source commits. |

## 6. Shared folder (icons)

| Path | Role |
|------|------|
| **`shared/`** | Local shared files (e.g. Font Awesome checkout). See repo [`README.md`](../../README.md) and [`shared/README.md`](../../shared/README.md). **Not** `mars-runtime/`, **not** governance. |
| **`shared/assets/icon-libraries/`** | Font Awesome Pro tree + [`fontawesome-pro-5.15.4-usage.md`](../../shared/assets/icon-libraries/fontawesome-pro-5.15.4-usage.md). |

## 7. Font Awesome Pro

**Path:** `shared/assets/icon-libraries/Font Awesome Pro 5.15.4/`

- **Use:** local icon name/style reference; copy **selected** SVGs into the project `src/` when needed.  
- **Licensing:** your Font Awesome agreement applies; this note **does not** grant redistribution rights.  
- **Not:** governance, not runtime code, **not** an instruction to commit the whole vendor tree.

More detail: [`shared/assets/icon-libraries/fontawesome-pro-5.15.4-usage.md`](../../shared/assets/icon-libraries/fontawesome-pro-5.15.4-usage.md). Example project note: [`notes/icon-source-policy.md`](notes/icon-source-policy.md).

## 8. Legacy strip partials

**`landing-strip-*`** under `workspaces/.../src/` — **continuity** with early mockup-strip scaffolding; **not** today’s main V2 homepage wiring.

**`design/frontend-section-map.md`** — continuity map for mockup → strip placeholders (may still mention the V1 workspace path); read its **Scope** line first.

## 9. Website Factory documentation

**`projects/mars-website-factory/`** is **Markdown-only** process documentation here. It does **not** run this workspace. Use it as vocabulary for handoff; **paths in this file** stay the practical map for files on disk.

## 10. Do not treat as sole truth

- **`web-gpt-sources/chat-migration/*`** — old snapshots; paths may be wrong or stale.  
- Other docs that say “never commit `dist/`” — for V2, root **`.gitignore`** keeps **`dist/`** off the allow-list; use this file + `.gitignore` for what is trackable.  
- Any claim that MARS **automatically** builds or verifies this site — incorrect; work is **local** Gulp + human review.

## 11. Quick answers

| Question | Answer |
|----------|--------|
| Where do I edit the live V2 page? | **`workspaces/triumph-manipulator-landing-v2/src/`** |
| Where are mockups / rules? | **`projects/triumph-manipulator-landing/design/v2/`** (visual). Folder roles: [`design/README.md`](./design/README.md). Written rules: MD stack in project root + `docs/`. Retired PDF: see [V2-CLEANUP-DECISION-LOG.md](./V2-CLEANUP-DECISION-LOG.md). |
| Where is Font Awesome Pro on disk? | **`shared/assets/icon-libraries/Font Awesome Pro 5.15.4/`** |
| Where does `npm run build` write? | **`workspaces/.../dist/`** (regenerate locally) |
| Is `shared/` random clutter? | **No** — see [`shared/README.md`](../../shared/README.md). |

## 12. SAFE UNKNOWN

- Whether built pages load FA **webfonts** from `dist/` or rely mostly on the **SVG sprite** — inspect built HTML/CSS when it matters for weight or licensing.  
- Whether every design asset has a twin under `src/img/` — not enumerated here.

## 13. Keeping this file honest

Update this note when paths or the real partial list change. Edits here **do not** change the Gulp pipeline by themselves.

---

*Documentation only — V2 frontend workspace paths.*
