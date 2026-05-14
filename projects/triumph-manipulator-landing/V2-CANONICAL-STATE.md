# Triumph Manipulator V2 — Canonical Operational State

## 1. Purpose

Single **operator-facing** snapshot of **where truth lives today** for Triumph Manipulator **Landing V2** inside this repo: workspaces, design pack paths, build output role, and shared icon reference. **Anti-drift:** reduces wrong-folder edits and mistaken “authoritative” paths. **Not** a legal review, **not** a refactor plan, **not** a migration checklist.

## 2. Current canonical workspace

| Workspace | Role |
|-----------|------|
| **`workspaces/triumph-manipulator-landing-v2/`** | **Current active frontend workspace** — Gulp static site; all ongoing V2 HTML/SCSS/JS/asset edits go here unless a task explicitly says otherwise. |
| **`workspaces/triumph-manipulator-landing/`** | **Historical / frozen reference** — do not use for new V2 work. V2 README pins V1 at git tag **`triumph-manipulator-v1`** (commit `309d81a`). |

## 3. Design source of truth

| Path | Role |
|------|------|
| **`projects/triumph-manipulator-landing/design/`** | **Visual design SoT** — mockup rasters (e.g. `design/mockups/`, `design/v2/`), PDF rules, and design-side Markdown indexes/maps. |
| **`projects/triumph-manipulator-landing/design-system/triumph-manipulator-design-system.md`** | **Written design system** — tokens and rules referenced from the V2 workspace README. |

Implementation must **align** with these sources; it does **not** replace them as the place to revise approved layout intent.

## 4. Frontend implementation source of truth

| Path | Role |
|------|------|
| **`workspaces/triumph-manipulator-landing-v2/src/`** | **Implementation SoT** — pages, partials, SCSS, JS, curated `src/svg/`, images under `src/img/**`, fonts, favicon. **Edit here, not in `dist/`.** |

**Current homepage composition (fact check: `src/pages/index.html`):** `hero-conversion`, `machine-specs-transport-lists`, `trust-cases-social-proof`, `segments-applications-grid`, `problem-solution-matrix`, `consultation-lead-form`, plus `site-footer-v2` — not the older `landing-strip-*` chain as the primary page skeleton.

## 5. Generated artifacts

| Path | Role |
|------|------|
| **`workspaces/triumph-manipulator-landing-v2/dist/`** | **Generated checkpoint artifact** — output of the Gulp build (HTML, CSS, JS, images, sprite, vendor copies as configured by the existing pipeline). **Not** a manual editing source. |

This workspace’s `.gitignore` documents that **`dist/` may be tracked** from the repo root as an **explicit allow-list exception**; other MARS docs may still say “do not commit `dist/`” by default — **both can be true** if you treat Triumph V2 as a **documented exception**. This file does **not** change pipeline or git rules.

## 6. Shared asset layer

| Path | Role |
|------|------|
| **`shared/`** | **Controlled shared asset layer** — see repo root [`README.md`](../../README.md) and [`shared/README.md`](../../shared/README.md). **Not** governance truth, **not** MARS JavaScript runtime. |
| **`shared/assets/icon-libraries/`** | Home for the **Font Awesome Pro 5.15.4** tree (see below) and the usage note alongside it. |

## 7. Font Awesome Pro classification

**Path:** `shared/assets/icon-libraries/Font Awesome Pro 5.15.4/`

| Property | Statement |
|----------|-----------|
| Intent | **Intentional** local, trusted **icon reference** for name/style lookup and operator-controlled export workflows. |
| Licensing | **Licensing-sensitive** — operator obligations follow **your** Font Awesome agreement; this document adds **no** redistribution grant. |
| Not | **Not** governance source of truth, **not** `mars-runtime/`, **not** a product “platform,” **not** a substitute for project-local shipped SVGs where policy requires selective use. |

Operational detail: [`shared/assets/icon-libraries/fontawesome-pro-5.15.4-usage.md`](../../shared/assets/icon-libraries/fontawesome-pro-5.15.4-usage.md). Project policy note: [`notes/icon-source-policy.md`](notes/icon-source-policy.md).

## 8. Legacy continuity layers

| Artifact | Role |
|----------|------|
| **`landing-strip-*`** partials / SCSS under `workspaces/triumph-manipulator-landing-v2/src/` | **Legacy continuity layer** — placeholder / deprecated segments tied to older mockup-strip mapping; **not** the primary active structure for the current `index.html` main flow. |
| **`projects/.../design/frontend-section-map.md`** | May still describe **V1** starter mapping (`workspaces/triumph-manipulator-landing/` + `landing-strip-*`); treat as **historical handoff** unless updated in a separate doc task. |

## 9. Website Factory relationship

**`projects/mars-website-factory/`** is a **documentation-first** website production direction in MARS — contracts, runbooks, and reference cases — **not** evidence of an in-repo automated builder executing this workspace.

For Triumph V2, treat Website Factory materials as **methodology and vocabulary** that should **cite** the paths above when talking about handoff; they do **not** override the **filesystem SoT** in sections 2–6.

## 10. What is NOT authoritative

- **`web-gpt-sources/chat-migration/*`** — migration-era snapshots; may label `shared/` or lanes as unknown; **do not** override this file or current workspace READMEs.
- **Generic “never commit dist”** lines in older project docs — may conflict with the **explicit** Triumph V2 `dist/` allow-list; prefer **this file + V2 workspace `.gitignore` + root `.gitignore`** for V2.
- **Any claim** that MARS “runs” or “verifies” this frontend as a shipped product **from core repo alone** — out of scope; this tree holds **source + generated artifacts under human workflow**.

## 11. Boundary clarifications

| Question | Answer |
|----------|--------|
| Where do I edit the live landing? | **`workspaces/triumph-manipulator-landing-v2/src/`** |
| Where do I compare pixels to design? | **`projects/triumph-manipulator-landing/design/`** mockups (+ PDF / design system) |
| Where is Font Awesome Pro installed for this repo? | **`shared/assets/icon-libraries/Font Awesome Pro 5.15.4/`** |
| Where does `npm run build` write? | **`workspaces/triumph-manipulator-landing-v2/dist/`** |
| Is `shared/` disposable clutter? | **No** — controlled layer; see `shared/README.md`. |

## 12. SAFE UNKNOWN

- **Whether every built page uses** the copied Font Awesome **webfont/CSS bundle** in `dist/` vs **only** the SVG sprite path — not asserted here; inspect built HTML/CSS when that distinction matters for licensing or weight.
- **Exact parity** between every file under `projects/.../design/assets/` and `workspaces/.../src/img/` — both lanes exist; **promotion discipline** is a process question, not recorded byte-for-byte in this file.

## 13. Stabilization intent

This document exists to **anchor paths and roles** for operators and agents. It **does not** instruct pipeline changes, asset moves, vendor reduction, or `dist/` cleanup. When reality drifts (e.g. homepage partial list changes), **update this file** in a small documentation pass — still **no** implied refactor.

---

*Document type: operational canonical state (documentation only).*
